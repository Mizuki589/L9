import streamlit as st
import requests
st.title("年齢予測アプリ")
name = st.text_input("名前")
if st.button("年齢を予測する"):
    if not name:
        st.warning("名前を入力してください。")
        st.stop()
    params = {"name": name}
    response = requests.get(
        "https://api.agify.io",
        params=params
    )
    if response.ok:
        data = response.json()
        if data["age"] is not None:
            st.metric(
                label=f"{data['name']} の推定年齢",
                value=f"{data['age']}歳"
            )
            
        else:
            st.warning("この名前のデータが見つかりませんでした。")
    else:
        st.error("APIとの通信に失敗しました。")
        st.write(response.status_code)
        st.write(response.text)
        

