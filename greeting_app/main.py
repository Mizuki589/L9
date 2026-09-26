import requests
import streamlit as st
import random
st.title("海外レシピ検索")
st.write("海外のレシピを検索できます。")
st.write("食材を検索欄に入れると、その食材を使ったレシピが検索できます。")
st.write("好みでなかったら、もう一度、検索ボタンを押してください。")
food = st.text_input("英語で食材を入力してください（例: chicken）")
num=random.randint(0, 40)
if st.button("検索"):
    if food:
        l = "https://www.themealdb.com/api/json/v1/1/filter.php"
        response = requests.get(l, params={"i": food})
        data = response.json()
        if data["meals"]:
            meal = data["meals"][num]#左の[０]を変えることができる。
            st.subheader(meal["strMeal"])
            st.image(meal["strMealThumb"])
            st.write("おいしそうですね！")
        else:
            st.write("レシピが見つかりませんでした。")
    else:
        st.write("食材を入力してください。")