import os
from google.oauth2 import service_account
from google.auth.transport.requests import Request
import vertexai
from openai import OpenAI

# Initilize OpenAI client
client = OpenAI()

# Get env variables
model = os.getenv("MODEL_ID")
project = os.getenv('PROJECT_ID')
location = os.getenv('LOCATION')

# Setup client for OpenAI or Gemini
if not os.getenv("OPENAI_API_KEY"):
    # Credentials to google account to allow login
    vertexai.init(project=project, location=location)
    credentials = service_account.Credentials.from_service_account_file(os.getenv("PATH_TO_AUTH"), scopes=["https://www.googleapis.com/auth/cloud-platform"])
    credentials.refresh(Request())    
    client.api_key = credentials.token
    client.base_url = f"https://{location}-aiplatform.googleapis.com/v1beta1/projects/{project}/locations/{location}/endpoints/openapi"
# If using OpenAI and a project is set, add to the client
elif project:
    client.project = project

PROMPT_HALLUCINATION = '''\
You are a helpful assistant answering questions about the Creatures Of Mythology Bank which is a fantasy bank that 
services only creatures of mythology. It offers a range of banking services from savings accounts to credit cards 
applying to almost all mythological creatures.

Question: {question}
'''

PROMPT_NO_HALLUCINATION = '''\
You are a helpful assistant answering questions about the Creatures Of Mythology Bank which is a fantasy bank that 
services only creatures of mythology. It offers a range of banking services from savings accounts to credit cards
applying to almost all mythological creatures.

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
    return client.chat.completions.create(
        model=model,
        messages=[{"role": "user", "content": prompt}],
        stream=True,
    )

if __name__ == "__main__":
    prompt = "You are a happy chatbot designed to answer the following question with a haiku. Do fish breathe air?"
    result = client.chat.completions.create(
        model=model,
        messages=[{"role": "user", "content": prompt}]
    )    
    print(result)
    print(result.choices[0].message.content)
