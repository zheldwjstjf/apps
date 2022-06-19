from asyncio.staggered import staggered_race
import streamlit as st
import time
import os

from subpages.gmail_page import GmailPage
from subpages.gmail_fetching_setting_page import GmailFetchingSettingPage
from subpages.gmail_fetching_page import GmailFetchingPage
# from subpages.gmail_fetching_result_page import GmailFetchingResultPage
from subpages.gmail_fetching_result_semi_page import GmailFetchingResultSemiPage
from subpages.gmail_fetching_result_full_page import GmailFetchingResultFullPage

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

# set localtime
os.environ['TZ'] = 'Japan'
time.tzset()

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

        self.auth_none_time = None
        self.auth_fail_time = None
        self.auth_success_time = None
        self.selected_email_id = None

        # 
        self.sidebarPage.sidebar_page()

        # sidebar page : auth
        with st.sidebar.expander("[ ▶︎ 認証 ]"):
            self.auth_result = self.ap.auth_page()

            if self.auth_result == None:
                t = time.localtime()
                self.auth_none_time = time.strftime("%Y-%m-%d %H:%M:%S", t)
                self.st.warning("未認証")

            elif self.auth_result == False:
                t = time.localtime()
                self.auth_fail_time = time.strftime("%Y-%m-%d %H:%M:%S", t)
                self.st.error("認証失敗")

            elif (self.auth_result != None) and (self.auth_result != False):
                t = time.localtime()
                self.auth_success_time = time.strftime("%Y-%m-%d %H:%M:%S", t)
                self.st.success("認証済")
            
            else:
                self.st.error("認証失敗")

            # self.st.info("認証成功 : " + str(self.auth_success_time))
            # self.st.info("認証切れ : " + str(self.auth_none_time))
            # self.st.info("[TODO] 認証維持時間 : ")

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

                # title
                self.st.markdown("<h1 style='text-align: center; color: red;'>MY GMAIL APP</h1>", unsafe_allow_html=True)
                
                ### GmailFetchingSettingPage
                self.gmailFetchingSettingPage = GmailFetchingSettingPage(st)
                with st.sidebar.expander("[ ▶︎ フィルタ ]"):
                    self.gmailFetchingSettingPage.gmail_fetching_setting_page()

                ### GmailFetchingPage
                self.gmailFetchingPage = GmailFetchingPage(st, service)
                user = self.gmailFetchingSettingPage.user
                query = self.gmailFetchingSettingPage.query
                self.gmailFetchingPage.get_list(user, query)

                ### GmailFetchingResultPage
                """
                self.gmailFetchingResultPage = GmailFetchingResultPage(st)
                maillist = self.gmailFetchingPage.maillist
                fetching_count = self.gmailFetchingSettingPage.fetching_count
                result_count = self.gmailFetchingPage.result_count
                if maillist != None:
                    self.gmailFetchingResultPage.get_mail_content(maillist, fetching_count, result_count, service, user)
                """

                ### GmailFetchingResultSemiPage
                self.gmailFetchingResultSemiPage = GmailFetchingResultSemiPage(st)
                maillist = self.gmailFetchingPage.maillist
                fetching_count = self.gmailFetchingSettingPage.fetching_count
                result_count = self.gmailFetchingPage.result_count

                if result_count > 0:
                    if maillist != None:
                        contents_list = self.gmailFetchingResultSemiPage.get_mail_content(maillist, fetching_count, result_count, service, user)

                    with st.sidebar.expander("[ ▶︎ 選択 ]"):

                        operation_type = self.st.radio("● 処理タイプ",('個別', 'Batch'), index=0)

                        if operation_type == '個別':
                            selected_content_info = self.st.selectbox("● SELECT EMAIL", contents_list, key="select_a_mail")
                            selected_email_order = selected_content_info[0]
                            self.selected_email_id = selected_content_info[1]
                            selected_email_title = selected_content_info[2]
                            self.st.write("SELECTED EMAIL : [ " + selected_email_order + " ] " + selected_email_title)

                        if operation_type == 'Batch':
                            self.st.write("Batch処理設定")

                    ### GmailFetchingResultFullPage
                    if self.selected_email_id != None:
                        self.gmailFetchingResultFullPage = GmailFetchingResultFullPage(st)
                        self.gmailFetchingResultFullPage.get_mail_content(service, user, self.selected_email_id, selected_content_info)

                    with st.sidebar.expander("[ ▶︎ 処理 ]"):
                        ### GmailMngPage
                        if self.selected_email_id != None:
                            self.gmailMngPage.gmail_mng_page(service, user, self.selected_email_id)
                        else:
                            pass

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

            selected_page = st.sidebar.selectbox("▶︎ Select Page", page_names_to_funcs.keys())
            page_names_to_funcs[selected_page]()

            # reload
            self.st.sidebar.button("更新")

        else:
            self.st.markdown("<h1 style='text-align: center; color: red;'>AUTHORIZATION FAILED</h1>", unsafe_allow_html=True)
            img_path="https://raw.githubusercontent.com/zheldwjstjf/apps/dev/streamlit/my_gmail_app/resources/digital_0_1.gif"
            self.snippetTools.image_alignment(img_path, 1380)

myGmailApp = MyGmailApp(st)
myGmailApp.main()