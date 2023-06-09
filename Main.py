import streamlit as st
import pandas as pd


st.set_page_config(layout="wide")

col1, col2 = st.columns(2)

with col1:
    st.image("006 images/my_photo7.jpeg")

with col2:
    st.title("Mohamed Ilyan")
    content = """
    Hi, I am Ilyan! I am a Chemical Engineer, Python programmer and Data Scientist. 
    I graduated in 2021 with a Master of Science in Chemical
    Engineering from the National University of Singapore with a focus
    on Process Design, Programming for Data analysis and Simulation, and Project Engineering.
    I have worked with organizations from various countries, such as Trust Your Water ME 
    to provide water solutions for hotels, industrial projects and residentials; 
    Biotech manufacturing at Geb Impact Technology Co. Ltd (Hong Kong); Provide 
    reactor simulation using Python and MATLAB at the National University of Singapore.
    """
    st.info(content)

st.write("Below you find some of the apps I have built in Python, feel free to contact me.")

df = pd.read_csv("006 data.csv")

col3, empty_column, col4 = st.columns([1.5, 0.5, 1.5])
#col3, empty_column, col4 = st.columns([1.5, 0.5, 1.5]), Original columns!
#[4, 0.5, 1.5]

with col3:
    for index, row in df[0:4].iterrows():
        st.header(row["title"])
        st.write(row["description"])
        st.image("006 images/" + row["image"])
        st.write(f"[Source Code]({row['url']})")

with col4:
    for index, row in df[4:].iterrows():
        st.header(row["title"])
        st.write(row["description"])
        st.image("006 images/" + row["image"])
        st.write(f"[Source Code]({row['url']})")
