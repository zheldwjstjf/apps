import json
import pandas as pd
import altair as alt
import matplotlib.pyplot as plt

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

    def main_page(self, user, sleep, start_date, end_date, key_word_list1, key_word_list2, key_word_list3):

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

            sleep_str = sleep_str.replace("'bedtime_start'", "'就寝時刻'")
            sleep_str = sleep_str.replace("'bedtime_end'", "'起床時刻'")


            sleep_str = sleep_str.replace("'", '"')

            # self.st.write("[DEBUG] sleep_str : ", sleep_str)


            ##################
            # get df
            ##################
            df = pd.read_json(sleep_str)
            df = df.set_index("summary_date")



            ##################
            # cooking sleep data (json)
            ##################
            sleep = eval(sleep_str)

            sleep_data_count = len(sleep)
            date_list = []
            sleep_start = []
            sleep_end = []
            for i in range(sleep_data_count):
                # summary_date
                sleep_data = sleep[i].get("summary_date")
                date_list.append(sleep_data)

                # sleep_start
                sleep_start_date = sleep[i].get("就寝時刻")
                sleep_start_time = sleep_start_date.split("T")[1]
                sleep_start_time = sleep_start_time.split("+")[0]
                sleep_start_time = sleep_start_time.replace(sleep_start_time[-3:], "") #  초단위 제제거거
                sleep_start_time = sleep_start_time.replace(sleep_start_time[-1:], "0") # 분단위 모모두  0으로 끝나게 처리
                first_digit_of_hour = int(sleep_start_time[:1])
                two_head_digit_of_hour = int(sleep_start_time[:2])
                if first_digit_of_hour == 0:
                    two_head_digit_of_hour = two_head_digit_of_hour + 24
                    sleep_start_time = sleep_start_time.replace(sleep_start_time[:2], "")
                    sleep_start_time = str(two_head_digit_of_hour) + sleep_start_time
                    
                sleep_start.append(sleep_start_time)

                # sleep_end
                sleep_end_time = sleep[i].get("起床時刻")
                sleep_end.append(sleep_end_time)


            ##################
            # show graph
            ##################
            
            self.st.markdown("<h2 style='text-align: left; color: black;'>[ " + user.upper() + " ]</h2>", unsafe_allow_html=True)
            self.st.markdown("<h2 style='text-align: left; color: red;'>睡眠グラフ : " + str(start_date) + " ~ " + str(end_date) + "</h2>", unsafe_allow_html=True)

            options1 = self.st.multiselect('', key_word_list1, default="総合スコア")
            chart_data = pd.DataFrame(df, columns=options1)
            self.st.line_chart(chart_data)

            options2 = self.st.multiselect('▶︎ 項目を選択', key_word_list2, default="睡眠時間")
            chart_data = pd.DataFrame(df, columns=options2)
            self.st.line_chart(chart_data)

            options3 = self.st.multiselect('▶︎ 項目を選択', key_word_list3, default="temperature_deviation")
            chart_data = pd.DataFrame(df, columns=options3)
            self.st.line_chart(chart_data)

            # 
            # chart_data = pd.DataFrame(sleep_start)
            # self.st.line_chart(chart_data)

            #
            x = pd.DataFrame(sleep_start)
            # col3.line_chart(x)
            y = pd.DataFrame(date_list)
            # col4.line_chart(y)

            # data
            plt.scatter(x, y)
            plt.show()

            # fig = plt.figure(figsize=(10, 3))
            # ax = fig.add_subplot(title='simlirity')
            # ax.scatter(x,y)
            # plt.rc('font', size=4.5)
            # plt.xlabel("xlabel")
            # plt.ylabel("ylabel")
            # self.st.pyplot(fig)


            ##################
            # show data
            ##################
            for i in range(5):
                self.st.write("")

            col1,col2,col3 = self.st.columns((2,1,1))
            
            selected_summary_date = col2.selectbox("", date_list, index=(sleep_data_count-1))
            sleep_dict_num = date_list.index(selected_summary_date)
            sleep_dict = sleep[sleep_dict_num]

            col1.markdown("<h2 style='text-align: left; color: red;'>" + "睡眠データ : " + str(sleep_dict.get("summary_date")) + " （夜）</h2>", unsafe_allow_html=True)

            # show sleep date of the selected date
            duration = sleep_dict.get("横になってた時間")

            bedtime_start = sleep_dict.get("就寝時刻")
            bedtime_end = sleep_dict.get("起床時刻")

            self.st.markdown("<h5 style='text-align: left; color: blue;'>" + "就寝時刻 : " + str(bedtime_start) + "</h5>", unsafe_allow_html=True)
            self.st.markdown("<h5 style='text-align: left; color: blue;'>" + "起床時刻 : " + str(bedtime_end) + "</h5>", unsafe_allow_html=True)

            col1, col2, col3, col4 = self.st.columns((2,2,2,1))
            col1.subheader(" ▶︎ スコア")
            for key_word in key_word_list1:
                col1.write(" - " + str(key_word) + " : " + str(sleep_dict.get(key_word)))

            col2.subheader(" ▶︎ 時間")
            for key_word in key_word_list2:
                
                # - second
                data_sec = sleep_dict.get(key_word)

                # - mim
                data_min = data_sec/60

                # - hour
                hour = data_min/60

                # - time
                hours = int(hour)
                minutes = (hour*60) % 60
                seconds = (hour*3600) % 60
                time = ("%d:%02d:%02d" % (hours, minutes, seconds))

                col2.write(" - " + str(key_word) + " : " + str(time) + " (" + str(int((data_sec/duration)*100)) + "%)")

            col3.subheader(" ▶︎ その他")
            for key_word in key_word_list3:
                col3.write(" - " + str(key_word) + " : " + str(sleep_dict.get(key_word)))


            ##################
            # raw data
            ##################

            col1, col2, col3 = self.st.columns((3,1,1))
            expander = col1.expander("Raw Data")
            expander.write(sleep_dict)
