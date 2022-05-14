import json
import os
from datetime import datetime
import streamlit as st
import pandas as pd

from oura import OuraClient


def get_self():
    pat = os.getenv("OURA_PAT")
    client = OuraClient(personal_access_token=pat)
    user_info = client.user_info()
    print(user_info)

# @st.cache(suppress_st_warning=True)
def getOuraClient(user):
    if user == "jack":
        client_id = st.secrets["client_id_jack"]
        client_secret = st.secrets["client_secret_jack"]
        access_token = st.secrets["access_token_jack"]
        refresh_token = st.secrets["refresh_token_jack"]
    if user == "rieko":
        client_id = st.secrets["client_id_rieko"]
        client_secret = st.secrets["client_secret_rieko"]
        access_token = st.secrets["access_token_rieko"]
        refresh_token = st.secrets["refresh_token_rieko"]

    auth_client = OuraClient(
        client_id=client_id,
        client_secret=client_secret,
        access_token=access_token,
        refresh_token=refresh_token,
    )

    return auth_client

@st.cache(suppress_st_warning=True)
def getSleepData(start_date):
    sleep = client.sleep_summary(str(start_date))

    return sleep


st.set_page_config( # Alternate names: setup_page, page, layout
    layout="wide",  # Can be "centered" or "wide". In the future also "dashboard", etc.
    # initial_sidebar_state="collapsed",  # Can be "auto", "expanded", "collapsed"
    page_title="my_sleep_graph",  # String or None. Strings get appended with "• Streamlit". 
    # page_icon=None,  # String, anything supported by st.image, or None.)
)

user_list = ["jack", "rieko"]
option = st.sidebar.selectbox("▶︎ ユーザをを選択", user_list, index=0)


client = getOuraClient(option)
start_date = datetime(2022, 1, 1)
sleep = getSleepData(start_date)
sleep = sleep["sleep"]
sleep_str = str(sleep)
sleep_str = sleep_str.replace("'", '"')

df = pd.read_json(sleep_str)

key_word_list = [
                    "score",
                    "score_deep",
                    "score_disturbances",
                    "score_efficiency",
                    "score_latency",
                    "score_rem",
                    "score_total",
                    "duration",
                    "total",
                    "awake",
                    "rem",
                    "deep",
                    "light",
                    "midpoint_time",
                    "temperature_deviation",
                    "temperature_trend_deviation",
                    "efficiency",
                    "restless",
                    "onset_latency",
                ]

options = st.multiselect('▶︎ 項目を選択',key_word_list, default="score")
st.write("options : ", options)

chart_data = pd.DataFrame(df, columns=options)
st.line_chart(chart_data)
