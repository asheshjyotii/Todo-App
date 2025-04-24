import streamlit as st
import utils as ut

todos = ut.read_todos() #becomes a list of todos read from the todos file

st.title("Todo App")
st.subheader("This is my simple todo list app")
st.write("I hope this can increase my productivity...")

for todo in todos:
    st.checkbox(todo)

st.text_input(label="Add new Todo",placeholder="Enter a todo....", label_visibility="hidden")