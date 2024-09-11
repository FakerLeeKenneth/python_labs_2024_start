import streamlit as st

# Title of the app
st.title("Simple Streamlit app")

# Create a text input box
text_input = st.text_input("Enter some text:")

# Create a submit button
if st.button("Submit"):
    st.write("You've inputted:", text_input)