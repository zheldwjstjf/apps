import streamlit as st

from pages.main_page import MainPage
from pages.sidebar import SidebarPage
from pages.auth_page import AuthPage

# ===================================
# st config
# ===================================
st.set_page_config( # Alternate names: setup_page, page, layout
    layout="wide",  # Can be "centered" or "wide". In the future also "dashboard", etc.
    initial_sidebar_state="expanded",  # Can be "auto", "expanded", "collapsed"
    page_title="MyGmailApp",  # String or None. Strings get appended with "• Streamlit". 
    page_icon="resources/gmail_icon")  # String, anything supported by st.image, or None.

class MyGmailApp:

    def __init__(self) -> None:
        """
        - method name : __init__
        - arg(s) : None
        """

        self.mainPage = MainPage(st)
        self.sidebarPage = SidebarPage(st)
        self.ap = AuthPage(st)

    def main(self):
        """
        - method name : main
        - arg(s) : None
        """

        # 
        self.sidebarPage.sidebar_page()

        # sidebar page : auth
        with st.sidebar.expander("[ 認証 ]"):
            auth_status = self.ap.auth_page()

            if auth_status == None:
                self.st.warning("未認証")

            if auth_status == True:
                self.st.success("認証済")

            if auth_status == False:
                self.st.error("認証失敗")

        # =================
        # main page

        if auth_status == None:
            self.st.markdown("<h1 style='text-align: center; color: red;'>NOT AUTHORIZED</h1>", unsafe_allow_html=True)

        if auth_status == True:
            # main page title
            self.st.markdown("<h1 style='text-align: center; color: red;'>RIEKOグラフ</h1>", unsafe_allow_html=True)

        if auth_status == False:
            self.st.markdown("<h1 style='text-align: center; color: red;'>NOT AUTHORIZED</h1>", unsafe_allow_html=True)




        # 
        self.mainPage.main_page()

myGmailApp = MyGmailApp()
myGmailApp.main()