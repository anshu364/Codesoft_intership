import streamlit as st

st.set_page_config(page_title="To-Do List", page_icon="📝")

# Initialize tasks in session state
if "tasks" not in st.session_state:
    st.session_state.tasks = []

st.title("📝 To-Do List App")
st.write("Manage your tasks efficiently!")

# Input for new task
new_task = st.text_input("Add a new task:")

if st.button("➕ Add Task"):
    if new_task.strip():
        st.session_state.tasks.append({"task": new_task, "done": False})
        st.success(f"Task added: {new_task}")
    else:
        st.warning("Please enter a task before adding.")

st.markdown("---")

# Display tasks with checkboxes
if st.session_state.tasks:
    for idx, task in enumerate(st.session_state.tasks):
        col1, col2 = st.columns([0.8, 0.2])

        with col1:
            st.session_state.tasks[idx]["done"] = st.checkbox(
                task["task"], value=task["done"], key=idx
            )

        with col2:
            if st.button("❌", key=f"del_{idx}"):
                st.session_state.tasks.pop(idx)
                st.experimental_rerun()
else:
    st.info("No tasks yet! Add one above.")

# Option to clear all tasks
if st.session_state.tasks and st.button("🗑️ Clear All Tasks"):
    st.session_state.tasks.clear()
    st.experimental_rerun()