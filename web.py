import streamlit as st
import functions

todos = functions.get_todos()


st.set_page_config(layout="wide")


def add_todo():
    todo = st.session_state["new_todo"] + "\n"
    todos.append(todo)
    functions.write_todos(todos)


st.title("My Todo App")
st.subheader("This is my Todo App.")

st.write("This app is to increase your <b>productivity</b>.",
         unsafe_allow_html=True)

st.text_input(label="", placeholder="Add a new to-do...",
              on_change=add_todo, key='new_todo')

st.write("This app is to increase your productivity.")


for index, todo in enumerate(todos):
    check_box = st.checkbox(todo, key=todo)
    if check_box:
        todos.pop(index)
        functions.write_todos(todos)
        del st.session_state[todo]
        st.experimental_rerun()


st.text_input(label="", placeholder="Add a new to-do...",
              on_change=add_todo, key='new_todo')


