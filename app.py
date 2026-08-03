import streamlit as st
st.title("checking the person eligible for vote or not")
age=st.number_input("enter your age...")
if st.button("submit"):
 if age>=18:
   st.success("you are eligible to vote..")
else:
  st.success("you are not eligible to vote..")
