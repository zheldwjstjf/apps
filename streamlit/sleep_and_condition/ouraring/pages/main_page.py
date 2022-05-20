import json
import pandas as pd
import altair as alt

class MainPage:
    """
    - class name : MainPage
    """

    def __init__(self, streamlit) -> None:
        """
        - method name : __init__
        - arg(s) : streamlit
        """

        self.st = streamlit

    def main_page(self, sleep, start_date, end_date, key_word_list1, key_word_list2, key_word_list3):

        if (start_date!=None) and (end_date!=None):

            sleep = sleep["sleep"]
            sleep_str = str(sleep)

            ##################
            # replace english keywords with japaense keywords
            ##################
            sleep_str = sleep_str.replace("'score_deep'", "'熟睡'")
            sleep_str = sleep_str.replace("'score_efficiency'", "'睡眠効率'")
            sleep_str = sleep_str.replace("'score_latency'", "'入眠潜時'")
            sleep_str = sleep_str.replace("'score_rem'", "'レム睡眠'")
            sleep_str = sleep_str.replace("'score_total'", "'合計睡眠'")
            sleep_str = sleep_str.replace("'score'", "'総合スコア'")

            sleep_str = sleep_str.replace("'total'", "'睡眠時間'")
            sleep_str = sleep_str.replace("'duration'", "'横になってた時間'")
            sleep_str = sleep_str.replace("'deep'", "'深い睡眠'")
            sleep_str = sleep_str.replace("'rem'", "'レム'")
            sleep_str = sleep_str.replace("'light'", "'浅眠'")
            sleep_str = sleep_str.replace("'awake'", "'覚醒'")

            sleep_str = sleep_str.replace("'", '"')

            # self.st.write("[DEBUG] sleep_str : ", sleep_str)

            df = pd.read_json(sleep_str)
            df = df.set_index("summary_date")


            ##################
            # show graph
            ##################
            self.st.markdown("<h2 style='text-align: left; color: red;'>睡眠グラフ : " + str(start_date) + " ~ " + str(end_date) + "</h2>", unsafe_allow_html=True)

            col1, col2 = self.st.columns((1.5,8.5))
            options1 = col1.multiselect('▶︎ 項目を選択', key_word_list1, default="総合スコア")
            chart_data = pd.DataFrame(df, columns=options1)
            col2.line_chart(chart_data)

            ###
            graph_data = pd.melt(graph_data, id_vars=["index"]).rename(
                columns={"index": "年月", "value": "金額 (円)"}
            )
            # write graphs
            line = (
                alt.Chart(graph_data
                )
                .mark_line(opacity=0.9)
                .encode(
                    x="summary_date",
                    y=alt.Y("金額 (円):Q", stack=False),
                    color="項目:N",
                )
            )
            chart = line

            self.st.altair_chart(chart, use_container_width=True)

            ###

            col3, col4 = self.st.columns((1.5,8.5))
            options2 = col3.multiselect('▶︎ 項目を選択', key_word_list2, default="睡眠時間")
            chart_data = pd.DataFrame(df, columns=options2)
            col4.line_chart(chart_data)

            col5, col6 = self.st.columns((1.5,8.5))
            options3 = col5.multiselect('▶︎ 項目を選択', key_word_list3, default="temperature_deviation")
            chart_data = pd.DataFrame(df, columns=options3)
            col6.line_chart(chart_data)


            ##################
            # show data
            ##################
            for i in range(5):
                self.st.write("")

            sleep = eval(sleep_str)

            sleep_data_count = len(sleep)
            date_list = []
            for i in range(sleep_data_count):
                sleep_data = sleep[i].get("summary_date")
                # self.st.write(sleep_data)
                date_list.append(sleep_data)

            # sleep_dict = sleep[-1]
            # self.st.write("[DEBUG] Sleep_dict : ", sleep_dict)

            col1,col2,col3 = self.st.columns((2,1,1))
            
            selected_summary_date = col2.selectbox("", date_list, index=(sleep_data_count-1))
            sleep_dict_num = date_list.index(selected_summary_date)
            sleep_dict = sleep[sleep_dict_num]

            col1.markdown("<h2 style='text-align: left; color: red;'>" + "睡眠データ : " + str(sleep_dict.get("summary_date")) + "</h2>", unsafe_allow_html=True)

            # show sleep date of the selected date
            duration = sleep_dict.get("横になってた時間")

            col1, col2, col3, col4 = self.st.columns((2,2,2,1))
            col1.write(" ▶︎ スコア")
            for key_word in key_word_list1:
                col1.write(" - " + str(key_word) + " : " + str(sleep_dict.get(key_word)))

            col2.write(" ▶︎ 時間（分）")
            for key_word in key_word_list2:
                col2.write(" - " + str(key_word) + " : " + str(sleep_dict.get(key_word)/60) + " (" + str(int((sleep_dict.get(key_word)/duration)*100)) + "%)")

            col3.write(" ▶︎ その他")
            for key_word in key_word_list3:
                col3.write(" - " + str(key_word) + " : " + str(sleep_dict.get(key_word)))
