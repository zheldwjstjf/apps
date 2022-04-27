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

csvDATA = StringIO(content)

# @st.cache
def get_utility_costs_data():
    df = pd.read_csv(csvDATA, sep=",")
    st.write(df)
    return df # df.set_index("項目")

try:
    df = get_utility_costs_data()
    utility_costs = st.multiselect(
        "▶︎ 項目を選んでください。", list(df.index), ["電 気 代", "ガ ス 代", "水 道 代"]
    )

    if not utility_costs:
        st.error("１つ以上の項目を選んでください。")
    else:
        data = df.loc[utility_costs]
        data /= 1000000.0
        # st.write("### 光熱費 (円)", data.sort_index())
        st.write("###### 光熱費詳細", data)

        graph_type = st.selectbox(
            '▶︎ 金額の表示タイプを選んでください。',
            ('個別金額', '合計金額')
        )

        if graph_type == "個別金額":
            stack_val = False
        elif graph_type == "合計金額":
            stack_val = True
        else:
            stack_val = None

        data = data.T.reset_index()
        data = pd.melt(data, id_vars=["index"]).rename(
            columns={"index": "年月", "value": "金額 (円)"}
        )
        chart = (
            alt.Chart(data)
            .mark_area(opacity=0.7)
            .encode(
                x="年月",
                y=alt.Y("金額 (円):Q", stack=stack_val),
                color="項目:N",
            )
        )
        st.altair_chart(chart, use_container_width=True)
except URLError as e:
    st.error(
        """
        **This demo requires internet access.**

        Connection error: %s
    """
        % e.reason
    )


# Streamlit widgets automatically run the script from top to bottom. Since
# this button is not connected to any other logic, it just causes a plain
# rerun.
st.button("Re-run")

