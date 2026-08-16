import streamlit as st
st.title("MY STREAMLIT APP")
name=st.text_input("Enter your name")
if st.button(Submit):
  st.write("Hey, {name}! Welcome to my app")
