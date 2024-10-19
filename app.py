!pip install streamlit
import streamlit as st
from llama_cpp import Llama

# Load the pre-trained model
llm = Llama.from_pretrained(
    repo_id="RichardErkhov/mrm8488_-_gpt2-finetuned-recipes-cooking-gguf",
    filename="gpt2-finetuned-recipes-cooking.IQ3_M.gguf",
)

# Function to generate a recipe
def generate_recipe(dish_name):
    response = llm.create_chat_completion(
        messages=[
            {
                "role": "user",
                "content": f"Give me a recipe for {dish_name}"
            }
        ]
    )
    return response['choices'][0]['message']['content']

# Streamlit UI
st.title("Cooking Recipe Finder")
user_input = st.text_input("Enter the name of a dish:")

if user_input:
    recipe = generate_recipe(user_input)
    st.write(f"Recipe for {user_input}:")
    st.write(recipe)
streamlit run app.py
