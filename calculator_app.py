import streamlit as st

# Set page title
st.title("🧮 Simple Calculator")

# Input: Two numbers
num1 = st.number_input("Enter the first number:", value=0.0)
num2 = st.number_input("Enter the second number:", value=0.0)

# Select operation
operation = st.selectbox(
    "Choose an operation:",
    ("Addition", "Subtraction", "Multiplication", "Division")
)

# Perform calculation
if st.button("Calculate"):
    if operation == "Addition":
        result = num1 + num2
    elif operation == "Subtraction":
        result = num1 - num2
    elif operation == "Multiplication":
        result = num1 * num2
    elif operation == "Division":
        if num2 != 0:
            result = num1 / num2
        else:
            st.error("Cannot divide by zero!")
            result = None

    if result is not None:
        st.success(f"The result of {operation.lower()} is: {result}")