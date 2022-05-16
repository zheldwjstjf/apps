import json
import os
from datetime import datetime
import streamlit as st
import pandas as pd

from oura import OuraClient

class Oura_sleep_data:

    def __init__(self) -> None:
        pass

    def get_self(self):
        pat = os.getenv("OURA_PAT")
        client = OuraClient(personal_access_token=pat)
        user_info = client.user_info()
        print(user_info)

    def getOuraClient(self, user):
        self.user = user

        if self.user == "jack":
            client_id = st.secrets["client_id_jack"]
            client_secret = st.secrets["client_secret_jack"]
            access_token = st.secrets["access_token_jack"]
            refresh_token = st.secrets["refresh_token_jack"]
        if self.user == "rieko":
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

    def getSleepData(self, *args, **kwargs):
        start_date = kwargs.get("startDate")
        if start_date != None:
            pass
        else:
            if self.user == "rieko":
                start_date = datetime(2021, 7, 2)
            if self.user == "jack":
                start_date = datetime(2022, 1, 1)

        end_date = kwargs.get("endDate")
        if end_date != None:
            pass
        else:
            end_date = datetime.today()

        sleep = client.sleep_summary(str(start_date), str(end_date))

        return sleep

#########################
#########################
#########################

OuraSleepData = Oura_sleep_data()


st.set_page_config( # Alternate names: setup_page, page, layout
    layout="wide",  # Can be "centered" or "wide". In the future also "dashboard", etc.
    initial_sidebar_state="collapsed",  # Can be "auto", "expanded", "collapsed"
    page_title="my_sleep_graph",  # String or None. Strings get appended with "• Streamlit". 
    # page_icon=None,  # String, anything supported by st.image, or None.)
)

user_list = ["jack", "rieko"]
option = st.sidebar.selectbox("▶︎ ユーザをを選択", user_list, index=1)


client = OuraSleepData.getOuraClient(option)

startDate = st.date_input("▶︎ いつから")
endDate = st.date_input("▶︎ いつまで")

sleep = OuraSleepData.getSleepData(start_date=startDate, end_date=endDate)

sleep = sleep["sleep"]

sleep_str = str(sleep)
sleep_str = sleep_str.replace("'", '"')

df = pd.read_json(sleep_str)

key_word_list1 = [
                    "score",
                    "score_deep",
                    "score_disturbances",
                    "score_efficiency",
                    "score_latency",
                    "score_rem",
                    "score_total",
                ]


key_word_list2 = [
                    "duration",
                    "total",
                    "awake",
                    "rem",
                    "deep",
                    "light",
                    "midpoint_time",
                ]

key_word_list3 = [
                    "temperature_deviation",
                    "temperature_trend_deviation",
                    "efficiency",
                    "restless",
                    "onset_latency",
                ]

col1, col2, col3 = st.columns((1,1,1))

options1 = col1.multiselect('▶︎ 項目を選択',key_word_list1, default="score")
# st.write("options : ", options1)

options2 = col2.multiselect('▶︎ 項目を選択',key_word_list2, default="duration")
# st.write("options : ", options2)

options3 = col3.multiselect('▶︎ 項目を選択',key_word_list3, default="temperature_deviation")
# st.write("options : ", options3)

chart_data = pd.DataFrame(df, columns=options1)
st.line_chart(chart_data)

chart_data = pd.DataFrame(df, columns=options2)
st.line_chart(chart_data)

chart_data = pd.DataFrame(df, columns=options3)
st.line_chart(chart_data)

all_key_word_list = [
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
                    "temperature_deviation",
                    "temperature_trend_deviation",
                    "efficiency",
                    "restless",
                    "onset_latency",
                ]

sleep_dict = sleep[0]

st.write("[DEBUG] Sleep_dict : ", sleep_dict[-1])

st.write("**本日のデータ**")

col4, col5, col6 = st.columns((1,1,1))

col4.write(" ▶︎ スコア")
for key_word in key_word_list1:
    col4.write(" - " + str(key_word) + " : " + str(sleep_dict.get(key_word)))

col5.write(" ▶︎ 時間（分）")
for key_word in key_word_list2:
    col5.write(" - " + str(key_word) + " : " + str(sleep_dict.get(key_word)/60))

col6.write(" ▶︎ その他")
for key_word in key_word_list3:
    col6.write(" - " + str(key_word) + " : " + str(sleep_dict.get(key_word)))