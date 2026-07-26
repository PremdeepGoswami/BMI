import streamlit as st

# -------------------------------------
# PAGE CONFIG
# -------------------------------------
st.set_page_config(
    #page_title="To-Do List",
    page_icon="✅",
    layout="centered"
)

st.title("📝 To-Do List Manager")

# -------------------------------------
# SESSION STATE
# -------------------------------------
if "data" not in st.session_state:
    st.session_state.data = {
        "tasks": {},
        "next_id": 1
    }

# -------------------------------------
# ADD TASK
# -------------------------------------
with st.form("add_task_form"):
    task_name = st.text_input("Enter a task")

    submitted = st.form_submit_button("➕ Add Task")

    if submitted:
        if task_name.strip() != "":
            task_id = st.session_state.data["next_id"]

            st.session_state.data["tasks"][task_id] = {
                "name": task_name,
                "completed": False
            }

            st.session_state.data["next_id"] += 1
            st.success("Task Added Successfully!")
            st.rerun()
        else:
            st.warning("Please enter a task.")

# -------------------------------------
# METRICS
# -------------------------------------
total_tasks = len(st.session_state.data["tasks"])

completed_tasks = sum(
    1
    for task in st.session_state.data["tasks"].values()
    if task["completed"]
)

pending_tasks = total_tasks - completed_tasks

col1, col2, col3 = st.columns(3)

col1.metric("Total", total_tasks)
col2.metric("Completed", completed_tasks)
col3.metric("Pending", pending_tasks)

st.divider()

# -------------------------------------
# DISPLAY TASKS
# -------------------------------------
if total_tasks == 0:
    st.info("No tasks added yet.")

else:

    for task_id, task in list(st.session_state.data["tasks"].items()):

        c1, c2, c3 = st.columns([0.1, 0.7, 0.2])

        # Checkbox
        completed = c1.checkbox(
            "",
            value=task["completed"],
            key=f"check_{task_id}"
        )

        if completed != task["completed"]:
            st.session_state.data["tasks"][task_id]["completed"] = completed
            st.rerun()

        # Task Name
        if task["completed"]:
            c2.markdown(f"~~{task['name']}~~")
        else:
            c2.write(task["name"])

        # Delete Button
        if c3.button("🗑️", key=f"delete_{task_id}"):
            del st.session_state.data["tasks"][task_id]
            st.success("Task Deleted")
            st.rerun()

# -------------------------------------
# DEBUG (Optional)
# -------------------------------------
with st.expander("View Dictionary"):
    st.write(st.session_state.data)
