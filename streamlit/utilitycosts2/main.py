import streamlit as st
from io import StringIO

import json
from apiclient.discovery import build
from oauth2client.client import OAuth2WebServerFlow
from oauth2client.file import Storage
import httplib2
from apiclient import errors

from pages.main_page import MainPage
from pages.side_menu import SideMenu
from modules.csv_tool import CSVTool

# ===================================
# st config
# ===================================
st.set_page_config(  # Alternate names: setup_page, page, layout
    layout="wide",  # Can be "centered" or "wide". In the future also "dashboard", etc.
    initial_sidebar_state="expanded",  # Can be "auto", "expanded", "collapsed"
    page_title="我が家の光熱費",  # String or None. Strings get appended with "• Streamlit". 
    # page_icon=None,  # String, anything supported by st.image, or None.
)

class App:

    def __init__(self):
        self.st = st

        #
        self.sm = SideMenu(st)
        self.mp = MainPage(st)
        self.cSVTool = CSVTool(self.st)

        self.auth_status = ""


    def main(self):
        # =================
        # main page title
        self.st.markdown("<h1 style='text-align: center; color: red;'>我が家の光熱費</h1>", unsafe_allow_html=True)


        # =================
        # load data
        self.df = self.cSVTool.load_data()


        # =================
        # side mmenu title
        st.sidebar.markdown("<h1 style='text-align: center; color: red;'>[ S I D E - M E N U ]</h1>", unsafe_allow_html=True)


        # =================

        self.auth_status = self.auth()

        if (self.auth_status != None) and (self.auth_status != False):
            # main page
            self.mp.main_page(self.df)

            # sidebar page : add data
            with st.sidebar.expander("[ 登録 ]"):
                self.sm.side_menu(self.df)

        # =================
        if (self.auth_status == None):
            st.sidebar.markdown("<h3 style='text-align: left; color: red;'>認証が必要です。</h3>", unsafe_allow_html=True)

        elif (self.flow_step2 == False):
            st.sidebar.markdown("<h3 style='text-align: left; color: red;'>認証失敗</h3>", unsafe_allow_html=True)



    def auth(self):
        with st.sidebar.expander("[ 認証 ]"):

            self.st.markdown("<h3 style='text-align: left; color: red;'>認証キーを選択してください。</h3>", unsafe_allow_html=True)

            uploaded_file = self.st.file_uploader("▶︎ Choose a file")

            if uploaded_file is not None:

                # To convert to a string based IO:
                stringio = StringIO(uploaded_file.getvalue().decode("utf-8"))

                auth_info = json.load(stringio)

                if auth_info['installed']["client_id"] == st.secrets["_client_id"]:

                    return True

                else:
                    self.st.write("idが一致しません。")

                    return False

            elif uploaded_file is None:
                self.st.write("認証キーが選択されてません。")
                    
                return False

app = App()
app.main()