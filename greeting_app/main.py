import streamlit as st
st.title("設定")

if "user_name"not in st.session_state:
    st.session_state.user_name=""
if "user_gakunen"not in st.session_state:
    st.session_state.user_gakunen=""
if "user_hobby"not in st.session_state:
    st.session_state.user_hobby=[]

name=st.text_input("あなたの名前を入力してください")
gakunen=st.selectbox("学年",
["小学三年生","小学四年生","小学五年生","小学六年生","中学一年生","中学二年生"])
hobby=st.multiselect("趣味",
["読書","スポーツ","ゲーム","動画視聴","音楽","絵画","その他"])

if st.button("情報を記憶"):
    st.session_state.user_name=name
    st.session_state.user_gakunen=gakunen
    st.session_state.user_hobby=hobby
    st.success("情報を保存しました")
st.write(f"記憶している名前：{st.session_state.user_name}")
