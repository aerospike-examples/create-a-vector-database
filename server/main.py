import time
from typing import Annotated
from fastapi import FastAPI, HTTPException, Form, status
from fastapi.responses import StreamingResponse
from fastapi.middleware.cors import CORSMiddleware
from llm import create_chat, PROMPT_WITH_VECTOR_SEARCH, PROMPT_HALLUCINATION, PROMPT_NO_HALLUCINATION
from data_loader import create_products, read_products, get_default_products, read_extra_products
from database import add_entry, similarity_search, get_all_entries, initialize, set_comparator
from embedder import create_embedding, cosineSimilarity, squaredEuclidean
from ComparatorResult import ComparatorResult

PRODUCT_FILE = '../data/products.csv'
EXTRA_PRODUCT_FILE = '../data/createProduct.csv'

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

@app.get("/rest/v1/get_products/")
async def get_products():
    return get_all_entries()
    
@app.get("/rest/v1/get_extra_products/")
async def get_extra_products():
    products = read_extra_products(EXTRA_PRODUCT_FILE)
    for p in products:
        add_entry(p)
    return get_all_entries()
    
@app.get("/rest/v1/create_database/")
async def create_database():
    products = read_products(PRODUCT_FILE)
    for p in products:
        add_entry(p)
    return len(products)

@app.post("/rest/v1/chat/")
async def create_chat_completion(text: Annotated[str, Form()]):
    start = time.time()
    docs = {}
    prompt = text # The default prompt passes the uesr query directly
    
    ##################
    # Use a prompt with provided context from the vector DB
    # embedding = create_embedding(text)
    # start = time.time()
    # results = similarity_search(embedding, 5)
    # context = ""
    
    # for data in results:
    #     product = data[1]['data']
    #     context += f"type {product['type']} name {product['name']} description {product['feature']}\n\n"
    #     docs[product['name']] = product['type']
    
    # prompt = PROMPT_WITH_VECTOR_SEARCH.format(question=text, context=context)
    
    ##################
    # Use a prompt that provides guardrails to combat hallucination
    # prompt = PROMPT_NO_HALLUCINATION.format(question=text)
    
    ##################
    # Use a prompt that may induce hallucination
    # prompt = PROMPT_HALLUCINATION.format(question=text)
    
    time_taken = time.time() - start
    
    return StreamingResponse(
        stream_response(
            prompt,
            time_taken, 
            docs
        ), 
        media_type="text"
    )


def stream_response(prompt: str, time_taken: float, docs: dict):
    yield f"_Query executed in {round(time_taken * 1000, 5)} ms_\n\n"
    
    if docs:
        yield f"The following products will be used to provide context:\n\n"    
        for key in docs:
            yield f"- <b>{docs[key]}</b>: {key}\n"

    yield "\nGenerating a response...\n\n"
    
    try:
        responses = create_chat(prompt)
        for response in responses:
            yield response.text
    except:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="An error occurred, please try again."
        )
    
    return

# Set the database to use cosine similarity for comparisons
set_comparator(cosineSimilarity, ComparatorResult.LARGER_IS_BETTER)
#set_comparator(squaredEuclidean, ComparatorResult.SMALLER_IS_BETTER)

# Initialize the database with the default products on startup
initialize(get_default_products())
