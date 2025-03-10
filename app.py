import streamlit as st
from transformers import pipeline

# Load the code generation model
@st.cache_resource
def load_model():
    return pipeline("text-generation", model="codellama/CodeLlama-7b-hf")

code_generator = load_model()

st.title("CodeGenie: AI-Powered Code Generation using CodeLlama")
st.markdown("""
### Problem Statement:
CodeGenie is an advanced project powered by CodeLlama, an AI model designed to streamline and enhance code generation. This innovative system simplifies the development process by providing accurate and efficient code snippets, comprehensive code explanations, and debugging support. CodeGenie can be utilized across various scenarios, offering robust solutions tailored to different developer needs.

### Expected Solutions:
CodeGenie allows developers to generate code effortlessly. For instance, a programmer can input a brief description of a desired function, and CodeGenie will provide the complete code snippet, including necessary libraries and comments. This feature enables developers to save time, reduce errors, and focus on more complex tasks by automating repetitive coding tasks.

### Technologies & Tools:
- Generative AI (GenAI)
- Python
- Streamlit
- Hugging Face Transformers
""")

# Input prompt for code generation
user_input = st.text_area("Enter a prompt for code generation:")
max_length = st.slider("Max length of generated code", 50, 500, 200)

if st.button("Generate Code"):
    if user_input:
        with st.spinner("Generating code..."):
            generated_code = code_generator(user_input, max_length=max_length, do_sample=True)[0]['generated_text']
        
        st.subheader("Generated Code:")
        st.code(generated_code, language="python")
    else:
        st.warning("Please enter a prompt.")
