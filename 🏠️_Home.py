import pandas as pd
import streamlit as st
from PIL import Image


st.set_page_config(page_title="Input", page_icon="🏠️", layout="centered", initial_sidebar_state="auto", menu_items=None)

image = Image.open('tek_up.png')

st.image(image)

st.title('Data Visualization Facilitator')

if 'title' in st.session_state:
    title_value = st.session_state['title']
else:
    title_value = ""

title = st.text_input("Enter title", value=title_value, placeholder=None, disabled=False, label_visibility="visible")

uploaded_file = st.file_uploader("Choose file", type=['csv', 'xls', 'xlsx'], accept_multiple_files=False)

def file_reader(uploaded_file):
    """
    convert uploaded_file to a DataFrame
    """
    
    if uploaded_file:
        if uploaded_file.name.endswith('xlsx') or uploaded_file.name.endswith('xls'):
            df = pd.read_excel(uploaded_file)
        elif uploaded_file.name.endswith('csv'):
            df = pd.read_csv(uploaded_file)
        st.session_state['df'] = df
        return df
    else:
        return None

df = file_reader(uploaded_file)

if 'df' in st.session_state:
    df = st.session_state['df']
    edited_df = st.data_editor(df)
    st.session_state['df'] = edited_df

if len(title) > 0:
    st.session_state['title'] = title

