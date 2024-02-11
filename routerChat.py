from dotenv import load_dotenv
import classifyChat
import simplestChat
import mathChat

load_dotenv()

def generate_classification(user_input):
    # Corrected: Use .format correctly by specifying a placeholder name
    formatted_template = classifyChat.class_template.format(user_input=user_input)
    # Adjust based on actual method to send prompt to the model (assuming invoke is correct)
    model_response = classifyChat.class_model.invoke(formatted_template)
    response = classifyChat.class_output_parser.parse(model_response)
    return response['response']

def generate_math_responese(user_input):
    # Corrected: Use .format correctly by specifying a placeholder name
    formatted_template = mathChat.math_template.format(user_input=user_input)
    # Adjust based on actual method to send prompt to the model (assuming invoke is correct)
    response = mathChat.math_model.run(formatted_template)
    return response

def generate_response(user_input):
    # Corrected: Use .format correctly by specifying a placeholder name
    formatted_template = simplestChat.chat_template.format(user_input=user_input)
    # Adjust based on actual method to send prompt to the model (assuming invoke is correct)
    model_response = simplestChat.chat_model.invoke(formatted_template)
    response = simplestChat.chat_output_parser.parse(model_response)
    return response['response']

def main(user_input):
    classifier = generate_classification(user_input)
    if classifier == "Math":
        response = generate_math_responese(user_input)
    else:
        response = generate_response(user_input)
    return response

if __name__ == "__main__":
    main()
