import requests
import streamlit as st
import random
st.title("レシピ検索")
food = st.text_input("英語で食材を入力してください（例: chicken）")
num=random.randint(0, 20)
if st.button("検索"):
    if food:
        l = "https://www.themealdb.com/api/json/v1/1/filter.php"
        response = requests.get(l, params={"i": food})
        data = response.json()
        if data["meals"]:
            meal = data["meals"][num]#左の[０]を変えることができる。
            st.subheader(meal["strMeal"])
            st.image(meal["strMealThumb"])
        else:
            st.write("レシピが見つかりませんでした。")
    else:
        st.write("食材を入力してください。")
