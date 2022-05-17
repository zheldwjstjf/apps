from datetime import datetime

class SidebarPage:
    """
    - class name : SidebarPage
    """

    def __init__(self, streamlit) -> None:
        """
        - method name : __init__
        - arg(s) : streamlit
        """

        self.st = streamlit

        self.key_word_list1 = [
                            "score",
                            "score_deep",
                            "score_disturbances",
                            "score_efficiency",
                            "score_latency",
                            "score_rem",
                            "score_total",
                        ]


        self.key_word_list2 = [
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

        self.key_word_list3 = [
                            "temperature_deviation",
                            "temperature_trend_deviation",
                            "efficiency",
                            "restless",
                            "onset_latency",
                        ]

    def sidebar_page(self):
        """
        - method name : sidebar_page
        - arg(s) : None
        """
        
        # select user
        user_list = ["jack", "rieko"]
        self.user = self.st.sidebar.selectbox("▶︎ ユーザをを選択", user_list, index=1)

        # select data
        # start_date = datetime(2022, 1, 1)
        self.start_date = self.st.sidebar.date_input("▶︎ いつからを選択")
        self.end_date = self.st.sidebar.date_input("▶︎ いつまでを選択")

        # select items
        self.options1 = self.st.sidebar.multiselect('▶︎ 項目を選択', self.key_word_list1, default="score")
        self.options2 = self.st.sidebar.multiselect('▶︎ 項目を選択', self.key_word_list2, default="duration")
        self.options3 = self.st.sidebar.multiselect('▶︎ 項目を選択', self.key_word_list3, default="temperature_deviation")

        return self.user, self.start_date, self.end_date, self.options1, self.options2, self.options3

