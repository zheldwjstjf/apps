import streamlit as st

from pages.sidebar_page import SidebarPage
from pages.main_page import MainPage
from modules.oura_auth import OuraAuth
from modules.oura_api import OuraApi

class MyOuraApp:

    def __init__(self) -> None:
        """
        - method name : __init__
        - arg(s) : None
        """

        self.sidebarPage = SidebarPage(st)
        self.mainPage = MainPage(st)
        self.ouraAuth = OuraAuth(st)
        self.ouraApi = OuraApi(st)
    
        self.key_word_list1 = [
                            "総合スコア___",
                            "合計睡眠____",
                            "睡眠効率____",
                            "入眠潜時____",
                            "熟睡______",
                            "レム睡眠____",
                         ]

        self.key_word_list2 = [
                            "横になってた時間",
                            "睡眠時間____",
                            "深い睡眠____",
                            "レム______",
                            "浅眠______",
                            "覚醒______",
                        ]

        self.key_word_list3 = [
                            "temperature_deviation",
                            "temperature_trend_deviation",
                            "efficiency",
                            "restless",
                            "onset_latency",
                        ]

    def main(self):
        st.set_page_config( # Alternate names: setup_page, page, layout
            layout="wide",  # Can be "centered" or "wide". In the future also "dashboard", etc.
            initial_sidebar_state="expanded",  # Can be "auto", "expanded", "collapsed"
            page_title="my_sleep_graph",  # String or None. Strings get appended with "• Streamlit". 
            page_icon=None)  # String, anything supported by st.image, or None.

        #
        key_word_list1 = self.key_word_list1
        key_word_list2 = self.key_word_list2
        key_word_list3 = self.key_word_list3

        # 
        self.sidebarPage.sidebar_page(key_word_list1, key_word_list2, key_word_list3)
        user = self.sidebarPage.user
        start_date = self.sidebarPage.start_date
        end_date = self.sidebarPage.end_date
        # options1 = self.sidebarPage.options1
        # options2 = self.sidebarPage.options2
        # options3 = self.sidebarPage.options3

        #
        self.ouraAuth.getOuraClient(user)
        client = self.ouraAuth.client

        # st.write("[DEBUG] start_date : ", start_date)
        # st.write("[DEBUG] end_date : ", end_date)

        #
        self.ouraApi.getSleepData(client, start_date, end_date)
        sleep = self.ouraApi.sleep

        #
        self.mainPage.main_page(sleep, 
                                start_date, end_date, 
                                # options1, options2, options3, 
                                key_word_list1, key_word_list2, key_word_list3)

myOuraApp = MyOuraApp()
myOuraApp.main()
