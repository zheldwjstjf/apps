import json
import pandas as pd

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

            ##################
            # show data
            ##################
            sleep = eval(sleep_str)
            sleep_dict = sleep[-1]

            # self.st.write("[DEBUG] Sleep_dict : ", sleep_dict)

            # show last day data
            col1, col2, col3, col4, col5, col6 = self.st.columns((2,1,1,1,1,1))
            self.st.markdown("<h2 style='text-align: left; color: red;'>" + "- 睡眠データ : " + str(sleep_dict.get("summary_date")) + "</h2>", unsafe_allow_html=True)

            
            duration = sleep_dict.get("横になってた時間")

            col1, col2, col3, col4 = self.st.columns((0.5,1,1.3,1))
            col2.write(" ▶︎ スコア")
            for key_word in key_word_list1:
                col2.write(" - " + str(key_word) + " : " + str(sleep_dict.get(key_word)))

            col3.write(" ▶︎ 時間（分）")
            for key_word in key_word_list2:
                col3.write(" - " + str(key_word) + " : " + str(sleep_dict.get(key_word)/60) + " (" + str(int((sleep_dict.get(key_word)/duration)*100)) + "%)")

            col4.write(" ▶︎ その他")
            for key_word in key_word_list3:
                col4.write(" - " + str(key_word) + " : " + str(sleep_dict.get(key_word)))

            ##################
            # show graph
            ##################

            self.st.write("")
            self.st.write("")
            self.st.write("")
            self.st.write("")
            self.st.write("")

            self.st.markdown("<h2 style='text-align: left; color: red;'>- グラフ : " + str(start_date) + " ~ " + str(end_date) + "</h2>", unsafe_allow_html=True)

            col1, col2 = self.st.columns((1.5,8.5))
            options1 = col1.multiselect('▶︎ 項目を選択', key_word_list1, default="総合スコア")
            chart_data = pd.DataFrame(df, columns=options1)
            col2.line_chart(chart_data)

            col3, col4 = self.st.columns((1.5,8.5))
            options2 = col3.multiselect('▶︎ 項目を選択', key_word_list2, default="睡眠時間")
            chart_data = pd.DataFrame(df, columns=options2)
            col4.line_chart(chart_data)

            col5, col6 = self.st.columns((1.5,8.5))
            options3 = col5.multiselect('▶︎ 項目を選択', key_word_list3, default="temperature_deviation")
            chart_data = pd.DataFrame(df, columns=options3)
            col6.line_chart(chart_data)
