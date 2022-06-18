from asyncio.staggered import staggered_race
import streamlit as st

from subpages.gmail_page import GmailPage
from subpages.gmail_crawling_page import GmailCrawlingPage
from subpages.sidebar import SidebarPage
from subpages.auth_page import AuthPage
from subpages.admin_page import AdminPage
from modules.snippet_tools import SnippetTools
from subpages.gmail_mng_page import GmailMngPage

# ===================================
# st config
# ===================================
st.set_page_config( # Alternate names: setup_page, page, layout
    layout="wide",  # Can be "centered" or "wide". In the future also "dashboard", etc.
    initial_sidebar_state="expanded",  # Can be "auto", "expanded", "collapsed"
    page_title="MyGmailApp",  # String or None. Strings get appended with "• Streamlit". 
    page_icon="resources/gmail_icon")  # String, anything supported by st.image, or None.

class MyGmailApp:

    def __init__(self, st) -> None:
        """
        - method name : __init__
        - arg(s) : None
        """

        self.st = st

        self.sidebarPage = SidebarPage(st)
        self.ap = AuthPage(st)
        self.adminPage = AdminPage(st)
        self.snippetTools = SnippetTools(st)
        self.gmailMngPage = GmailMngPage(st)

    def main(self):
        """
        - method name : main
        - arg(s) : None
        """

        # 
        self.sidebarPage.sidebar_page()

        # sidebar page : auth
        with st.sidebar.expander("[ 認証 ]"):
            self.auth_result = self.ap.auth_page()

            if self.auth_result == None:
                self.st.warning("未認証")

            elif self.auth_result == False:
                self.st.error("認証失敗")

            elif (self.auth_result != None) and (self.auth_result != False):
                self.st.success("認証済")
            
            else:
                self.st.error("認証失敗")

            self.st.info("[ TODO ] 認証した時刻")
            self.st.info("[ TODO ] 認証切れた時刻")
            self.st.info("[ TODO ] 認証維持時間")

        # =================
        # main page

        if self.auth_result == None:
            # self.st.markdown("<h1 style='text-align: center; color: red;'>NOT AUTHORIZED</h1>", unsafe_allow_html=True)
            img_path="https://raw.githubusercontent.com/zheldwjstjf/apps/dev/streamlit/my_gmail_app/resources/locked.gif"
            self.snippetTools.image_alignment(img_path, 1330)

        elif self.auth_result == False:
            self.st.markdown("<h1 style='text-align: center; color: red;'>AUTHORIZATION FAILED</h1>", unsafe_allow_html=True)
            img_path="https://raw.githubusercontent.com/zheldwjstjf/apps/dev/streamlit/my_gmail_app/resources/digital_0_1.gif"
            self.snippetTools.image_alignment(img_path, 1380)

        elif (self.auth_result != None) and (self.auth_result != False):
            # gmail page title

            def Gmail():
                service = self.auth_result
                self.gmailPage = GmailPage(st, service)
                self.gmailPage.gmail_page()
                self.gmailMngPage.gmail_mng_page(self.gmailPage.mail_id)

            def Gmail_Crawling():
                service = self.auth_result
                self.gmailCrawlingPage = GmailCrawlingPage(st, service)
                self.gmailCrawlingPage.gmail_crawling_page()

            def Admin():
                self.adminPage.admin_page()

            page_names_to_funcs = {
                "Gmail": Gmail,
                "Gmail_Crawling": Gmail_Crawling,
                "Admin": Admin,
            }

            selected_page = st.sidebar.selectbox("Select a page", page_names_to_funcs.keys())
            page_names_to_funcs[selected_page]()

            # reload
            self.st.sidebar.button("更新")

        else:
            self.st.markdown("<h1 style='text-align: center; color: red;'>AUTHORIZATION FAILED</h1>", unsafe_allow_html=True)
            img_path="https://raw.githubusercontent.com/zheldwjstjf/apps/dev/streamlit/my_gmail_app/resources/digital_0_1.gif"
            self.snippetTools.image_alignment(img_path, 1380)

myGmailApp = MyGmailApp(st)
myGmailApp.main()