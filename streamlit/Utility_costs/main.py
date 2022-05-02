import streamlit as st
from pages.auth_page import AuthPage
from pages.main_page import MainPage
from pages.side_menu import SideMenu
from modules.csv_tool import CSVTool

"""
import datetime
import pandas as pd
import altair as alt
import base64
import requests
import json
from io import StringIO
import os
from apiclient.discovery import build
import webbrowser
from oauth2client.client import OAuth2WebServerFlow
from oauth2client.file import Storage
import httplib2
from apiclient import errors
"""

# ===================================
# st config
# ===================================
st.set_page_config(  # Alternate names: setup_page, page, layout
    layout="wide",  # Can be "centered" or "wide". In the future also "dashboard", etc.
    initial_sidebar_state="expanded",  # Can be "auto", "expanded", "collapsed"
    page_title="我が家の光熱費",  # String or None. Strings get appended with "• Streamlit". 
    page_icon=None,  # String, anything supported by st.image, or None.
)

class App:

    def __init__(self) -> None:

        self.st = st

        #
        self.ap = AuthPage(st)
        self.sm = SideMenu(st)
        self.mp = MainPage(st)
        self.cSVTool = CSVTool(self.st)

    def main(self):

        # =================
        # main page title
        self.st.markdown("<h1 style='text-align: center; color: red;'>我が家の光熱費</h1>", unsafe_allow_html=True)

        # =================
        # load data
        df = self.cSVTool.load_data()

        # =================
        # side mmenu title
        st.sidebar.markdown("<h1 style='text-align: center; color: red;'>[ S I D E - M E N U ]</h1>", unsafe_allow_html=True)

        # sidebar page : 更新
        with st.sidebar.expander("更新"):
            with self.st.form(key='my_form'):
                submit_button = self.st.form_submit_button(label='更新')

        # sidebar page : auth
        if self.ap.credent_status == True:
            # main page
            self.mp.main_page(df)

            # sidebar page : add data
            with st.sidebar.expander("登録"):
                self.sm.side_menu(df)
        
        if self.ap.credent_status == False:
            with st.sidebar.expander("認証"):
                auth_status = self.ap.auth_page()

            if auth_status == True:
                # main page
                self.mp.main_page(df)

                # sidebar page : add data
                with st.sidebar.expander("登録"):
                    self.sm.side_menu(df)

            elif auth_status == False:
                st.sidebar.markdown("<h3 style='text-align: left; color: red;'>認証が必要です。</h3>", unsafe_allow_html=True)
            else:
                pass

app = App()
app.main()