import streamlit as st
import datetime
import utils as ut
todos = ut.read_todos()
def empty():
    pass
def new_todo():
    todo = st.session_state["new_todo"] + '\n'
    if todo != "\n":
        print(type(todo))
        todos.append(todo)
        ut.write_todos(todos)
    else:
        print("empty")
        pass

todos = ut.read_todos() #becomes a list of todos read from the todos file

st.title("📝 Your Personal Todo Manager")
st.subheader("Stay Organized, Stay Focused!")

st.divider()

today = datetime.date.today()
st.write(f"📅 **Today:** {today.strftime('%A, %B %d, %Y')}")

st.success("Ready to conquer your tasks today? Let's go! 💪")

st.write("Add, track, and complete your daily tasks effortlessly 🚀")



for index, todo in enumerate(todos):
    checkbox_status = st.checkbox(todo, key=todo+str(index))
    if checkbox_status:
        todos.pop(index)
        ut.write_todos(todos)
        del st.session_state[todo+str(index)]
        st.rerun()

st.text_input(label="Add new Todo",placeholder="Enter a todo....", label_visibility="hidden",on_change= new_todo, key="new_todo" )

