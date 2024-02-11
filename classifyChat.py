from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain_core.output_parsers import StrOutputParser
from langchain.chains import ConversationChain

load_dotenv()

# Define a chat template
class_template = """
    Given the user question below, classify it as either being about `Math`, `Business`, or `Other`.
    Do not respond with more than one word.
        
    <question>
    {user_input}
    </question>

    Classification:
"""

# Declare a model instance with specified temperature
class_model = ConversationChain(
    llm=ChatOpenAI(temperature=0)
)

# Declare an output parser instance
class_output_parser = StrOutputParser()

def generate_classification(user_input):
    # Corrected: Use .format correctly by specifying a placeholder name
    formatted_template = class_template.format(user_input=user_input)
    # Adjust based on actual method to send prompt to the model (assuming invoke is correct)
    model_response = class_model.invoke(formatted_template)
    classifier = class_output_parser.parse(model_response)
    return classifier['response']

def main(user_input):
    classifier = generate_classification(user_input)
    return classifier

if __name__ == "__main__":
    main()
