import streamlit as st
import requests
from groq import Groq
from huggingface_hub import InferenceClient
from openai import OpenAI
import os
import re
from transformers import AutoTokenizer, AutoModelForCausalLM

# Configuration for Hugging Face API
# HF_API_KEY = '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'  # Replace with your actual API key
# MODEL_ENDPOINT = 'https://api-inference.huggingface.co/models/your_model_name'  # Replace with your model's endpoint
# headers = {
#     'Authorization': f'Bearer {HF_API_KEY}'
# }

# Function to query the Hugging Face model
def query_huggingface_model(prompt):
  # Load model directly

  tokenizer = AutoTokenizer.from_pretrained("AzmeerFaisal/Llama2STEM")
  model = AutoModelForCausalLM.from_pretrained("AzmeerFaisal/Llama2STEM")
  
  input_text = f"Instruction: {prompt} \n  \
                Input: \
                Output: "
  inputs = tokenizer(input_text, return_tensors="pt")

  # Generate text
  outputs = model.generate(**inputs, max_length=50, num_return_sequences=1)

  # Decode and print the output
  generated_text = tokenizer.decode(outputs[0], skip_special_tokens=True)
  return generated_text
  
  

# Streamlit app layout
st.set_page_config(page_title="STEM Chatbot", page_icon=":robot_face:", layout="wide")

# Custom CSS for yellow and white theme with improved visibility
# Custom CSS for purple and white theme with larger input box

# Header and Sidebar
st.title("⚛️ STEM MATE ")
st.sidebar.header("STEM MATE")
st.sidebar.write("Welcome! Ask me anything bout science, technology, engineering, and mathematics.")

st.markdown("""
<style>
    .stTextArea textarea {
        height: 150px;
        font-size: 16px;
    }
</style>
""", unsafe_allow_html=True)


# Use st.text_area instead of st.text_input
user_input = st.text_area("Ask a STEM question:", key="user_input")


if st.button("Submit"):
    if user_input:
        with st.spinner("Getting response..."):
            result = query_huggingface_model(user_input)
            if "error" in result:
                st.error(f"Error: {result['error']}")
            else:
                response_text = result.get("generated_text", "No response from the model.")
                # Function to process the response and render LaTeX
                def render_latex_response(text):
                    # Split the text into LaTeX and non-LaTeX parts
                    parts = re.split(r'\\\[.*?\\\]', text)
    
                    # Find all LaTeX expressions
                    latex_expressions = re.findall(r'\\\[(.*?)\\\]', text)
                    
                    for i, part in enumerate(parts):
                        # Render non-LaTeX text
                        st.write(part.strip())
                        
                        # Render corresponding LaTeX expression if it exists
                        if i < len(latex_expressions):
                            st.latex(latex_expressions[i].strip())
                            
                # render_latex_response(response_text)
                render_latex_response(response_text)
    else:
        st.warning("Please enter a question before submitting.")
        
st.markdown("""
<script>
    const textbox = document.querySelector('#user_input');
    textbox.addEventListener('input', function() {
        sessionStorage.setItem('user_input', this.value);
    });
    window.addEventListener('load', function() {
        const savedInput = sessionStorage.getItem('user_input');
        if (savedInput) {
            textbox.value = savedInput;
        }
    });
</script>
""", unsafe_allow_html=True)

# Footer
# st.sidebar.write("Created with ❤️ by Your Name")