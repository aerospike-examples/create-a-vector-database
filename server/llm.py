from google.oauth2 import service_account
import vertexai
from vertexai.generative_models import GenerativeModel

# Credentials to google account to allow login
credentials = service_account.Credentials.from_service_account_file("auth.json")
vertexai.init(project="aero-devrel", location="us-central1", credentials=credentials)

model = GenerativeModel("gemini-1.5-flash-001")

#Using the following context, answer the question and provide an explanation.
#If you are unable to answer the question, ask for more information.

PROMPT_HALLUCINATION = '''\
You are a helpful assistant answering questions about the Creatures Of Mythology Bank which is a fantasy bank that 
services only creatures of mythology. It offers a range of banking services from savings accounts to credit cards 
applying to almost all mythological creatures.

Question: {question}
'''

PROMPT_NO_HALLUCINATION = '''\
You are a helpful assistant answering questions about the Creatures Of Mythology Bank which is a fantasy bank that 
services only creatures of mythology. It offers a range of banking services from savings accounts to credit cards.

Creatures of Mythology Bank was founded in 1777 by William Greystanes in a land far, far away. There remains
mystery around why the bank was founded and if any mythological creatures were involved, but it remains one 
of the most profitable banks of all time due to the ever-lasting nature of the investments.

Using this only information, answer the question. If you are unable to answer the question, ask for more information.

Question: {question}
'''

PROMPT_WITH_VECTOR_SEARCH = '''\
You are a helpful assistant answering questions about the Creatures Of Mythology Bank which is a fantasy bank that 
services only creatures of mythology. It offers a range of banking services from savings accounts to credit cards.
Using the following context, answer the question.

Creatures of Mythology Bank was founded in 1777 by William Greystanes in a land far, far away. There remains
mystery around why the bank was founded and if any mythological creatures were involved, but it remains one 
of the most profitable banks of all time due to the ever-lasting nature of the investments.

Question: {question}
Context: {context}
'''

def create_chat(prompt):
    chat = model.start_chat()
    return chat.send_message(
        content=prompt,
        stream=True,
    )

if __name__ == "__main__":
    # prompt = "What are LLMs best used for in FinServ?"
    chat = model.start_chat(response_validation=False)
    result = chat.send_message(
        content="You are a happy chatbot designed to answer the following question with a rhyme. Do fish breathe air?", 
        stream=False)
    print(result)
    print(result.candidates[0].content.parts[0].text)
