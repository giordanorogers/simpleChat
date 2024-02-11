from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain_core.output_parsers import StrOutputParser
from langchain.memory import ConversationSummaryBufferMemory
from langchain.chains import ConversationChain

load_dotenv()

# Define a chat template
chat_template = """
    Give a polite and conversational response to the user input:
    {user_input}
"""

# Declare a model instance with specified temperature
memory_model = ChatOpenAI(temperature=0)
memory = ConversationSummaryBufferMemory(llm=memory_model, max_token_limit=100)
chat_model = ConversationChain(
    llm=ChatOpenAI(temperature=0),
    memory=memory
)

# Declare an output parser instance
chat_output_parser = StrOutputParser()

def generate_response(user_input):
    # Corrected: Use .format correctly by specifying a placeholder name
    formatted_template = chat_template.format(user_input=user_input)
    # Adjust based on actual method to send prompt to the model (assuming invoke is correct)
    model_response = chat_model.invoke(formatted_template)
    response = chat_output_parser.parse(model_response)
    return response['response']

def main(user_input):
    response = generate_response(user_input)
    return response

if __name__ == "__main__":
    main()
