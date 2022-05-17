import streamlit as st

from pages.sidebar_page import SidebarPage
from pages.main_page import MainPage
from modules.oura_client import OuraClient
from modules.oura_api import OuraApi

class MyOuraApp:

    def __init__(self) -> None:
        """
        - method name : __init__
        - arg(s) : None
        """

        self.sidebarPage = SidebarPage(st)
        self.mainPage = MainPage(st)
        self.ouraClient = OuraClient(st)
        self.ouraApi = OuraApi(st)
    
    def main(self):
        st.set_page_config( # Alternate names: setup_page, page, layout
            layout="wide",  # Can be "centered" or "wide". In the future also "dashboard", etc.
            initial_sidebar_state="collapsed",  # Can be "auto", "expanded", "collapsed"
            page_title="my_sleep_graph",  # String or None. Strings get appended with "• Streamlit". 
            page_icon=None)  # String, anything supported by st.image, or None.

        # 
        self.sidebarPage.sidebar_page()
        user = self.sidebarPage.user
        start_date = self.sidebarPage.start_date
        end_date = self.sidebarPage.end_date
        options1 = self.sidebarPage.options1
        options2 = self.sidebarPage.options2
        options3 = self.sidebarPage.options3

        #
        self.ouraClient(user)
        client = self.ouraClient.client

        #
        self.ouraApi(client)
        sleep = self.ouraApi.sleep

        #
        self.mainPage.main_page(sleep, start_date, end_date, options1, options2, options3)

myOuraApp = MyOuraApp()
myOuraApp.main()
