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

def appendFile(filename, token_dict):

    basePath = os.path.dirname(os.path.abspath(__file__))
    fullPath = os.path.join(basePath, filename)
    with open(fullPath, "r+") as file:
        prev = json.load(file)
        curr = {
            "client_id": prev.pop("client_id"),
            "client_secret": prev.pop("client_secret"),
            "access_token": token_dict["access_token"],
            "refresh_token": token_dict["refresh_token"],
            "previous": json.dumps(prev),
        }
        file.seek(0)
        json.dump(curr, file)


def getOuraClient():
    client_id = st.secrets["client_id"]
    client_secret = st.secrets["client_secret"]
    access_token = st.secrets["access_token"]
    refresh_token = st.secrets["refresh_token"]
    # refresh_callback = lambda x: appendFile(envFile, x)

    auth_client = OuraClient(
        client_id=client_id,
        client_secret=client_secret,
        access_token=access_token,
        refresh_token=refresh_token,
        # refresh_callback=refresh_callback,
    )

    return auth_client


if __name__ == "__main__":

    # envFile = "token.json"
    # setEnvironment(envFile)
    client = getOuraClient()
    start_date = datetime(2022, 1, 1)
    # print("start_date : ", start_date)
    # print("start_date type : ", type(start_date))
    sleep = client.sleep_summary(str(start_date))
    sleep = sleep["sleep"]
    sleep_str = str(sleep)
    sleep_str = sleep_str.replace("'", '"')
    print(sleep_str)

df = pd.read_json(sleep_str)
# df = pd.read_json("oura_sleep_2022-05-13T15-08-55.json")

key_word_list_all = [
                    "duration",
                    "total",
                    "awake",
                    "rem",
                    "deep",
                    "light",
                    "midpoint_time",
                    "efficiency",
                    "restless",
                    "onset_latency",
                    "score",
                    "score_alignment",
                    "score_deep",
                    "score_disturbances",
                    "score_efficiency",
                    "score_latency",
                    "score_rem",
                    "score_total",
                    "temperature_deviation",
                    "temperature_trend_deviation",
                    "bedtime_start_delta",
                    "bedtime_end_delta",
                    "midpoint_at_delta",
                    "temperature_delta"
                ]

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


st.set_page_config( # Alternate names: setup_page, page, layout
    layout="wide",  # Can be "centered" or "wide". In the future also "dashboard", etc.
    initial_sidebar_state="collapsed",  # Can be "auto", "expanded", "collapsed"
    page_title="my_sleep_graph",  # String or None. Strings get appended with "• Streamlit". 
    # page_icon=None,  # String, anything supported by st.image, or None.
)

width_num = 1200
height_num = 500
useContainerWidth = True # False

chart_data = pd.DataFrame(df, columns=["score"])
st.line_chart(chart_data, width=width_num, height=height_num, use_container_width=useContainerWidth)

chart_data = pd.DataFrame(df, columns=key_word_list_score)
st.line_chart(chart_data, width=width_num, height=height_num, use_container_width=useContainerWidth)

chart_data = pd.DataFrame(df, columns=key_word_list_duration)
st.line_chart(chart_data, width=width_num, height=height_num, use_container_width=useContainerWidth)

chart_data = pd.DataFrame(df, columns=key_word_list_temperature)
st.line_chart(chart_data, width=width_num, height=height_num, use_container_width=useContainerWidth)

for key_word in key_word_list_all:
    chart_data = pd.DataFrame(df, columns=[key_word])
    st.line_chart(chart_data, width=width_num, height=height_num, use_container_width=useContainerWidth)