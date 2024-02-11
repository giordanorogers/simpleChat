from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain_core.output_parsers import StrOutputParser
from langchain.chains import LLMMathChain

load_dotenv()

# Define a chat template
math_template = """
    Answer this math question:
    {user_input}
"""

# Declare a model instance with specified temperature
math_model = LLMMathChain.from_llm(
    llm=ChatOpenAI(temperature=0)
)

# Declare an output parser instance
math_output_parser = StrOutputParser()

def generate_math_response(user_input):
    # Corrected: Use .format correctly by specifying a placeholder name
    formatted_template = math_template.format(user_input=user_input)
    # Adjust based on actual method to send prompt to the model (assuming invoke is correct)
    model_response = math_model.run(formatted_template)
    response = math_output_parser.parse(model_response)
    return response

def main(user_input):
    response = generate_math_response(user_input)
    return response

if __name__ == "__main__":
    main()
