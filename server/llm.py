from google.oauth2 import service_account
import vertexai
from vertexai.generative_models import GenerativeModel

credentials = service_account.Credentials.from_service_account_file("auth.json")
vertexai.init(project="aero-devrel", location="us-central1", credentials=credentials)

model = GenerativeModel("gemini-1.5-flash-001")

#Using the following context, answer the question and provide an explanation.
#If you are unable to answer the question, ask for more information.

PROMPT = '''\
You are a helpful assistant answering questions about the Creatures Of Mythology Bank which is a fantasy bank that 
services only creatures of mythology. It offers a range of banking services from savings accounts to credit cards.

Creatures of Mythology Bank was founded in 1777 by William Greystanes in a land far, far away. There remains
mystery around why the bank was founded and if any mythological creatures were involved, but it remains one 
of the most profitable banks of all time due to the ever-lasting nature of the investments.

Question: {question}
'''


PROMPT = '''\
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
    print(prompt)
    chat = model.start_chat()
    return chat.send_message(
        content=prompt,
        stream=True,
    )

#prompt = PROMPT.format(question = "What products are available for griffins?")
#result = create_chat(prompt)
#print(result)
