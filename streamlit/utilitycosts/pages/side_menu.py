import datetime

from modules.csv_tool import CSVTool

class SideMenu:
    def __init__(self, streamlit):
        self.st = streamlit
        self.cSVTool = CSVTool(self.st)

    # ===================================
    # side bar
    # ===================================
    def side_menu(self, df):

        selected_date = self.st.date_input(
            "▶︎ 日付を指定してください。",
            datetime.date.today()
        )
        selected_date = selected_date.strftime("%Y-%m")


        option = self.st.selectbox(
            '▶︎ 項目を選んでください。',
            ('電 気 代', 'ガ ス 代', '水 道 代'))

        if option=="電 気 代":
            row = 0
        if option=="ガ ス 代":
            row = 1
        if option=="水 道 代":
            row = 2

        # enter your biking info for the day
        amount = self.st.number_input("▶︎ 金額(円)", min_value=0, value=3000, step=1000)

        # save button
        self.col1, self.col2 = self.st.columns((3,1))
        if self.col2.button("保存"):
            # TODO
            # self.cSVTool.save_input(df, row, int(amount), selected_date)
            # self.col1.write("保存されました。")

            self.st.warning("対応中です。")
