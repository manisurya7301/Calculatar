import streamlit as st

st.title("Mani ka Web Calculator 🧮")
col1, col2, col3, col4 = st.columns(4)

with col1:
    num1 = st.number_input("Pehla Number")
with col2:
    operation = st.selectbox("Operation", ["+", "-", "×", "÷"])
with col3:
    num2 = st.number_input("Dusra Number")

if st.button("Calculate"):
    if operation == "+": result = num1 + num2
    elif operation == "-": result = num1 - num2
    elif operation == "×": result = num1 * num2
    elif operation == "÷": result = num1 / num2 if num2 !=0 else "Error"
    st.success(f"Result: {result}")
