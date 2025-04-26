import streamlit as st
import utils as ut
todos = ut.read_todos()
def empty():
    pass
def new_todo():
    todo = st.session_state["new_todo"] + '\n'
    todos.append(todo)
    ut.write_todos(todos)

todos = ut.read_todos() #becomes a list of todos read from the todos file

st.title("Todo App")
st.subheader("This is my simple todo list app")
st.write("I hope this can increase my productivity...")

for index, todo in enumerate(todos):
    checkbox_status = st.checkbox(todo, key=todo+str(index))
    if checkbox_status:
        todos.pop(index)
        ut.write_todos(todos)
        del st.session_state[todo+str(index)]
        st.rerun()

st.text_input(label="Add new Todo",placeholder="Enter a todo....", label_visibility="hidden",on_change= new_todo, key="new_todo" )

st.session_state
