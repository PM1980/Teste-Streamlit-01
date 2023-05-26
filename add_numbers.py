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
    
    st.write("** Olá Mundo! **")
    st.markdown("**Olá Daniel!**")
    st.write("Esse é o primeiro exemplo de um aplicativo web elaborado em Python e compartilhado utilizando o Streamlit. Desenvolvido por Paulo em 26-05-2023 com auxílio do Chat-GPT")

if __name__ == '__main__':
    main()
