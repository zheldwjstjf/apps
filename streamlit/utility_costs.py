import streamlit as st
import datetime
import pandas as pd
import altair as alt
import base64
import requests
import json

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

url = "https://api.github.com/repos/zheldwjstjf/apps/contents/streamlit/data/utility_costs.csv"
req = requests.get(url)
st.write(req.status_code)
if req.status_code == requests.codes.ok:
    req = req.json()  # the response is a JSON
    st.write("req type : ", type(req))
    st.write("req : ", req)
    # req is now a dict with keys: name, encoding, url, size ...
    # and content. But it is encoded with base64.
    try:
         content = base64.b64decode(req['content'])
    except Exception as e:
          st.write(e)
    st.write(111)
    st.write(content)
    st.write(222)
else:
    st.write('Content was not found.')

