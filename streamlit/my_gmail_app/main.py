from asyncio.staggered import staggered_race
import streamlit as st

from subpages.gmail_page import GmailPage
from subpages.sidebar import SidebarPage
from subpages.auth_page import AuthPage
from subpages.admin_page import AdminPage

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
        self.gmailPage = GmailPage(st)
        self.adminPage = AdminPage(st)        

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

        auth_status = True

        if auth_status == None:
            self.st.markdown("<h1 style='text-align: center; color: red;'>NOT AUTHORIZED</h1>", unsafe_allow_html=True)
            # self.st.markdown("![Alt Text](https://raw.githubusercontent.com/zheldwjstjf/apps/dev/streamlit/my_gmail_app/resources/digital_0_1.gif)")
            img="https://raw.githubusercontent.com/zheldwjstjf/apps/dev/streamlit/my_gmail_app/resources/digital_0_1.gif"
            self.st.image(img, width=1380)

        if auth_status == True:
            # gmail page title

            def Gmail():
                st.sidebar.markdown("# Gmail 🎈")
                self.gmailPage.gmail_page()

            def Admin():
                st.sidebar.markdown("# Admin ❄️")
                self.adminPage.admin_page()

            page_names_to_funcs = {
                "Gmail": Gmail,
                "Admin": Admin,
            }

            selected_page = st.sidebar.selectbox("Select a page", page_names_to_funcs.keys())
            page_names_to_funcs[selected_page]()


            # reload
            self.st.sidebar.button("更新")

        if auth_status == False:
            self.st.markdown("<h1 style='text-align: center; color: red;'>AUTHORIZATION FAILED</h1>", unsafe_allow_html=True)
            # self.st.markdown("![Alt Text](https://raw.githubusercontent.com/zheldwjstjf/apps/dev/streamlit/my_gmail_app/resources/locked.gif)")
            img="https://raw.githubusercontent.com/zheldwjstjf/apps/dev/streamlit/my_gmail_app/resources/locked.gif"
            self.st.image(img, width=1380)
        
myGmailApp = MyGmailApp(st)
myGmailApp.main()