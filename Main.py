import streamlit as st
import pandas as pd


st.set_page_config(layout="wide")

col1, col2 = st.columns([1,2.5])

with col1:
    st.image("images/ilyan_image.jpeg", width=300)


with col2:
    st.title("Mohamed Ilyan")
    content = """
    Hi, I am Ilyan! An AI & Data Engineer.
    I graduated in 2021 with a Master in Chemical Engineering from the National University of Singapore with a focus
    on Programming for Data analysis and Simulation, Process Design, and Project Engineering.
    My experience includes working with organizations from various countries and in different sectors,
    including biotech/pharmaceutical manufacturing, water solutions, academic research and Civil Engineering.
    My most recent role is as an AI & Data Engineer at Boskalis Westminister, a Marine Civil Engineering company 
    where we leverage the data and AI/ML to create engineering software that helps in optimizing the operations, 
    iterate to find solutions and for general automation and data management.
    """
    st.info(content)

st.write("---")

st.write("Below you'll find some of the apps I have built as a hobby, since I generally love to "
         "develop new software in my free-time. If you'd love to know more, feel free to get in touch.")

df = pd.read_csv("app_data.csv")

col4, empty_column, col5 = st.columns([1.5, 0.5, 1.5])

with col4:
    for index, row in df[0:4].iterrows():
        st.header(row["title"])
        st.write(row["description"])
        st.image("images/" + row["image"])
        st.write(f"[Source Code]({row['url']})")

with col5:
    for index, row in df[4:].iterrows():
        st.header(row["title"])
        st.write(row["description"])
        st.image("images/" + row["image"])
        st.write(f"[Source Code]({row['url']})")
