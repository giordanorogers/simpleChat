import os
from dotenv import load_dotenv
from langchain.chains import LLMMathChain
from langchain_openai import ChatOpenAI

load_dotenv()
OPENAI_API_KEY = os.getenv('OPENAI_API_KEY')

llm = ChatOpenAI(
    temperature=0, 
    openai_api_key=OPENAI_API_KEY
)

llm_math = LLMMathChain.from_llm(
    llm, 
    verbose=True
)

llm_math.run("What is 13.89 raised to the 34 power?")