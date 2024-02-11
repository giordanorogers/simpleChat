import os
import streamlit as st
from dotenv import load_dotenv
import routerChat

# Load API Key from Environment Variable
load_dotenv()
OPENAI_API_KEY = os.getenv('OPENAI_API_KEY')

# Set Page Title and Configuration
st.set_page_config(page_title="Chat Demo")
st.title('Chat Demo')

def generate_response(user_input):
  st.info(routerChat.main(user_input))

with st.form('my_form'):
  user_input = st.text_area('Enter text:', 'How do I optimize my delivery business?')
  submitted = st.form_submit_button('Submit')
  if not OPENAI_API_KEY.startswith('sk-'):
    st.warning('Please enter your OpenAI API key!', icon='⚠')
  if submitted and OPENAI_API_KEY.startswith('sk-'):
    generate_response(user_input)