import streamlit as st

st.title("Atlas App")

name = st.text_input("Enter your name")
if name:
    st.success(f"Hello, {name}!")

if "count" not in st.session_state:
    st.session_state.count = 0

col1, col2 = st.columns(2)
with col1:
    if st.button("Increment"):
        st.session_state.count += 1
with col2:
    if st.button("Reset"):
        st.session_state.count = 0

st.metric("Count", st.session_state.count)
