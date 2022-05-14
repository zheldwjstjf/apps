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

def getOuraClient():
    client_id = st.secrets["client_id_jack"]
    client_secret = st.secrets["client_secret_jack"]
    access_token = st.secrets["access_token_jack"]
    refresh_token = st.secrets["refresh_token_jack"]

    auth_client = OuraClient(
        client_id=client_id,
        client_secret=client_secret,
        access_token=access_token,
        refresh_token=refresh_token,
    )

    return auth_client


if __name__ == "__main__":

    client = getOuraClient()
    start_date = datetime(2022, 1, 1)
    sleep = client.sleep_summary(str(start_date))
    sleep = sleep["sleep"]
    sleep_str = str(sleep)
    sleep_str = sleep_str.replace("'", '"')

df = pd.read_json(sleep_str)

key_word_list_score = [
                    "score",
                    "score_deep",
                    "score_disturbances",
                    "score_efficiency",
                    "score_latency",
                    "score_rem",
                    "score_total"
                ]

key_word_list_duration = [
                    "duration",
                    "total",
                    "awake",
                    "rem",
                    "deep",
                    "light",
                    "midpoint_time"
                ]

key_word_list_temperature = [
                    "temperature_deviation",
                    "temperature_trend_deviation",
                ]

key_word_list_etc = [
                    "efficiency",
                    "restless",
                    "onset_latency",
                ]

col1, col2, col3, col4 = st.columns(1,1,1,1)

options_list = []

option1 = col1.st.multiselect('▶︎ スコア',key_word_list_score)
if option1 != None:
    options_list = options_list.append(option1)

option2 = col2.st.multiselect('▶︎ 時間',key_word_list_duration)
if option2 != None:
    options_list = options_list.append(option2)

option3 = col3.st.multiselect('▶︎ 体温偏差',key_word_list_temperature)
if option3 != None:
    options_list = options_list.append(option3)

option4 = col4.st.multiselect('▶︎ その他',key_word_list_etc)
if option4 != None:
    options_list = options_list.append(option4)


st.set_page_config( # Alternate names: setup_page, page, layout
    layout="wide",  # Can be "centered" or "wide". In the future also "dashboard", etc.
    initial_sidebar_state="collapsed",  # Can be "auto", "expanded", "collapsed"
    page_title="my_sleep_graph",  # String or None. Strings get appended with "• Streamlit". 
    # page_icon=None,  # String, anything supported by st.image, or None.
)

width_num = 1200
height_num = 500
useContainerWidth = True # False

chart_data = pd.DataFrame(df, columns=[options_list])
st.line_chart(chart_data, width=width_num, height=height_num, use_container_width=useContainerWidth)
