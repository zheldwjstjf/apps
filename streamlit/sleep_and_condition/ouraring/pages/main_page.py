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

    def main_page(self, sleep, start_date, end_date, options1, options2, options3, key_word_list1, key_word_list2, key_word_list3):

        if (start_date!=None) and (end_date!=None):

            sleep = sleep["sleep"]
            sleep_str = str(sleep)

            sleep_str = sleep_str.replace("'score_deep'", "'熟睡'")
            sleep_str = sleep_str.replace("'score_efficiency'", "'睡眠効率'")
            sleep_str = sleep_str.replace("'score_latency'", "'入眠潜時'")
            sleep_str = sleep_str.replace("'score_rem'", "'レム睡眠'")
            sleep_str = sleep_str.replace("'score_total'", "'合計睡眠'")
            sleep_str = sleep_str.replace("'score'", "'総合スコア'")

            sleep_str = sleep_str.replace("'", '"')

            # self.st.write("[DEBUG] sleep_str : ", sleep_str)

            df = pd.read_json(sleep_str)

            # show graph
            col1, col2, col3 = self.st.columns((1,1,1))

            chart_data = pd.DataFrame(df, columns=options1)
            self.st.line_chart(chart_data)

            chart_data = pd.DataFrame(df, columns=options2)
            self.st.line_chart(chart_data)

            chart_data = pd.DataFrame(df, columns=options3)
            self.st.line_chart(chart_data)


            # show data
            sleep = eval(sleep_str)
            sleep_dict = sleep[-1]

            # self.st.write("[DEBUG] Sleep_dict : ", sleep_dict)

            self.st.write("**詳細データ** : " + str(sleep_dict.get("summary_date")) + "の朝のデータ")

            col4, col5, col6 = self.st.columns((1,1,1))

            col4.write(" ▶︎ スコア")
            for key_word in key_word_list1:
                col4.write(" - " + str(key_word) + " : " + str(sleep_dict.get(key_word)))

            col5.write(" ▶︎ 時間（分）")
            for key_word in key_word_list2:
                col5.write(" - " + str(key_word) + " : " + str(sleep_dict.get(key_word)/60))

            col6.write(" ▶︎ その他")
            for key_word in key_word_list3:
                col6.write(" - " + str(key_word) + " : " + str(sleep_dict.get(key_word)))
