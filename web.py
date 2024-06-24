import streamlit as st
import functions

todos = functions.get_todos()

def add_todo():
    new_todo = st.session_state.new_todo.strip() + "\n"
    # Would be great to show some message when duplicate to-do is added
    if new_todo not in todos: # Add this if-condition to fix the issue
        todos.append(new_todo)
        functions.save_todos(todos)
    st.session_state.new_todo = ""



st.title("My Todo App")
st.subheader("This is my todo app.")
st.write("This app is to increase your productivity. No duplicate to-do is allowed.")

for index, todo in enumerate(todos):
    checkbox = st.checkbox(todo, key=f"{index}-{todo}")
    if checkbox:
        print(f"{index}-{todo}")
        todos.pop(index)
        functions.save_todos(todos)
        del st.session_state[f"{index}-{todo}"]
        st.rerun()


# on_change triggered when enter is clicked or out of focus
st.text_input(label="", placeholder="Add new todo...", key="new_todo", on_change=add_todo)

print("Hello")

st.session_state