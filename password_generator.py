import streamlit as st
import random
import string

# App title
st.title("🔐 Password Generator")

# User input for password length
length = st.number_input("Enter password length:", min_value=4, max_value=100, value=12, step=1)

# Checkbox for complexity options
include_uppercase = st.checkbox("Include Uppercase Letters (A-Z)", value=True)
include_lowercase = st.checkbox("Include Lowercase Letters (a-z)", value=True)
include_digits = st.checkbox("Include Digits (0-9)", value=True)
include_symbols = st.checkbox("Include Symbols (!@#$...) ", value=True)

# Function to generate password
def generate_password(length, uppercase, lowercase, digits, symbols):
    characters = ""
    if uppercase:
        characters += string.ascii_uppercase
    if lowercase:
        characters += string.ascii_lowercase
    if digits:
        characters += string.digits
    if symbols:
        characters += string.punctuation

    if not characters:
        return "Please select at least one character type."

    password = "".join(random.choice(characters) for _ in range(length))
    return password

# Button to generate password
if st.button("Generate Password"):
    password = generate_password(length, include_uppercase, include_lowercase, include_digits, include_symbols)
    st.success(f"Your generated password is:\n\n*{password}*")