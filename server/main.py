import os
import time
from typing import Annotated
from fastapi import FastAPI, HTTPException, Form, status
from fastapi.responses import StreamingResponse
from fastapi.middleware.cors import CORSMiddleware
from llm import create_chat, PROMPT
from threading import Lock
from data_loader import create_products, read_products
from database import add_entry, similarity_search, get_entry_count
from encoder import create_embedding

embed_lock = Lock()
llm_lock = Lock()
PRODUCT_FILE = '../data/products.csv'

app = FastAPI(
    title="Aerospike Vector RAG Demo",
    openapi_url=None, 
    docs_url=None,
    redoc_url=None,
    swagger_ui_oauth2_redirect_url=None,
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post("/rest/v1/reset/")
async def reset_database():
    create_products(PRODUCT_FILE)

@app.get("/rest/v1/get_products")
async def get_products():
    return read_products(PRODUCT_FILE)
    
@app.get("/rest/v1/create_database")
async def create_database():
    products = read_products(PRODUCT_FILE)
    for p in products:
        print("Adding: ", p)
        add_entry(p)
    return len(products)

@app.post("/rest/v1/chat/")
async def create_chat_completion(text: Annotated[str, Form()]):
    if (get_entry_count() == 0):
        products = read_products(PRODUCT_FILE)
        for p in products:
            add_entry(p)

    with embed_lock:
        embedding = create_embedding(text)
    start = time.time()
    results = similarity_search(embedding, 5)
    time_taken = time.time() - start

    context = ""
    docs = {}
    for idx, data in enumerate(results):
        product = data[1]['data']
        context += f"type {product['type']} name {product['name']} description {product['feature']}\n\n"
        docs[product['name']] = product['type']

    #for result in results:
    #    context += f"{result.fields['content']}\n\n"
    #    docs[result.fields["title"]] = result.fields["url"]

    #context = "Creatures of Mythology Bank was founded in 1777 by William Greystanes in a land far, far away. There remains "
    #"mystery around why the bank was founded and if any mythological creatures were involved." 
    
    return StreamingResponse(
        stream_response(
            PROMPT.format(question=text, context=context),
            time_taken, 
            docs
        ), 
        media_type="text"
    )

def stream_response(prompt, time_taken, docs):
    yield f"_Query executed in {round(time_taken * 1000, 5)} ms_\n\n"
    yield f"The following documents will be used to provide context:\n\n"
    
    for key in docs:
        yield f"- <b>{docs[key]}</b>: {key}\n"
    
    if llm_lock.locked():
        time.sleep(.5)
        yield "\nWaiting for slot...\n\n"

    with llm_lock:
        time.sleep(.5)
        yield "\nGenerating a response...\n\n"
        
        try:

            responses = create_chat(prompt)
            for response in responses:
                print(response)
                yield response.text

            #response = create_chat(prompt)
            #yield "\nGot a response!\n"
            #yield response

            #for chunk in response:
            #    content = chunk.choices[0].delta.content
            #    if content is not None:
            #        yield content
        except:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="An error occurred, please try again."
            )
    
    return


