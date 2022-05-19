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

    def sidebar_page(self, key_word_list1, key_word_list2, key_word_list3):
        """
        - method name : sidebar_page
        - arg(s) : None
        """
        
        # select user
        user_list = ["jack", "rieko"]
        self.user = self.st.sidebar.selectbox("▶︎ ユーザをを選択", user_list, index=1)

        # select data
        if self.user == "rieko":
            start_date = datetime(2021, 7, 2)
        if self.user == "jack":
            start_date = datetime(2022, 1, 1)
        end_data = datetime.today()
        
        self.start_date = self.st.sidebar.date_input("▶︎ いつからを選択", start_date)
        self.end_date = self.st.sidebar.date_input("▶︎ いつまでを選択", end_data)

        # select items
        self.options1 = self.st.sidebar.multiselect('▶︎ 項目を選択', key_word_list1, default="総合スコア")
        self.options2 = self.st.sidebar.multiselect('▶︎ 項目を選択', key_word_list2, default="睡眠時間")
        self.options3 = self.st.sidebar.multiselect('▶︎ 項目を選択', key_word_list3, default="temperature_deviation")

        return self.user, self.start_date, self.end_date, self.options1, self.options2, self.options3

