import streamlit as st

# Title of the app
st.title('Simple Calculator')

# Input fields for numbers
num1 = st.number_input('Enter the first number', value=0.0)
num2 = st.number_input('Enter the second number', value=0.0)

# Drop-down menu for operation selection
operation = st.selectbox('Choose an operation', ['Add', 'Subtract', 'Multiply', 'Divide'])

# Calculate result based on selected operation
result = None
if operation == 'Add':
    result = num1 + num2
elif operation == 'Subtract':
    result = num1 - num2
elif operation == 'Multiply':
    result = num1 * num2
elif operation == 'Divide':
    if num2 != 0:
        result = num1 / num2
    else:
        result = 'Error: Division by zero'

# Display the result
if result is not None:
    st.write(f'The result of {operation}ing {num1} and {num2} is: {result}')
