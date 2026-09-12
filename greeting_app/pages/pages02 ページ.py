import requests
import streamlit as st
st.title("翻訳アプリ")
st.write("このページはAIで作りました。APIの制限をテストするためのものです。")
languages = {
    "日本語": "ja",
    "英語": "en",
}
source = st.selectbox("翻訳元", languages.keys())
target = st.selectbox("翻訳先", languages.keys())
text = st.text_area(
    "翻訳する文章",
    placeholder="ここに文章を入力してください"
)
if st.button("翻訳する"):
    if not text.strip():
        st.warning("文章を入力してください。")
    elif source == target:
        st.warning("翻訳元と翻訳先を別の言語にしてください。")
    else:
        try:
            response = requests.get(
                "https://api.mymemory.translated.net/get",
                params={
                    "q": text,
                    "langpair": f"{languages[source]}|{languages[target]}"
                },
                timeout=10
            )

            response.raise_for_status()
            data = response.json()

            result = data["responseData"]["translatedText"]

            st.subheader("翻訳結果")
            st.success(result)
        except requests.exceptions.RequestException as e:
            st.error(f"翻訳中にエラーが発生しました: {e}")
