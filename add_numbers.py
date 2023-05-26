import streamlit as st

def add_numbers(num1, num2):
    return num1 + num2

def main():
    st.title("Number Addition")
    
    num1 = st.text_input("Enter the first number:", value='0')
    num2 = st.text_input("Enter the second number:", value='0')
    
    try:
        num1 = float(num1)
        num2 = float(num2)
        result = add_numbers(num1, num2)
        st.success(f"The sum of {num1} and {num2} is: {result}")
    except ValueError:
        st.error("Please enter valid numbers.")

if __name__ == '__main__':
    main()
