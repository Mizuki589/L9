import streamlit as st
st.title("名前記憶")
if "name"not in st.session_state:
    st.session_state.name=""
name=st.text_input("あなたの名前を入力してください")
if st.button("名前を記憶"):
    st.session_state.name=name

st.write(f"記憶している名前：{st.session_state.name}")
