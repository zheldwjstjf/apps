import streamlit as st
import datetime
import pandas as pd
import altair as alt

from urllib.error import URLError

# side bar
uploaded_file = st.sidebar.file_uploader("Choose a file")

d = st.sidebar.date_input(
     "日付を指定してください。",
     datetime.date.today())

option = st.sidebar.selectbox(
     '項目を選んでください。',
     ('電 気 代', 'ガ ス 代', '水 道 代'))

number = st.sidebar.number_input('金額を入力してください。')

if st.sidebar.button("反映"):
    st.sidebar.write('反映されました。')
else:
     pass

# main page
st.header('我が家の光熱費')


# Streamlit widgets automatically run the script from top to bottom. Since
# this button is not connected to any other logic, it just causes a plain
# rerun.
st.button("Re-run")
