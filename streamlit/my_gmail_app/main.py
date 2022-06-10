import subprocess
from asyncio.staggered import staggered_race
import streamlit as st

from subpages.main_page import MainPage
from subpages.sidebar import SidebarPage
from subpages.auth_page import AuthPage

# ===================================
# st config
# ===================================
st.markdown(
    """
    <style>
    [data-testid="stSidebar"][aria-expanded="true"] > dvi:first-child {
        width: 1000px;
    }
    [data-testid="stSidebar"][aria-expanded="false"] > dvi:first-child {
        width: 1000px;
        margin-left: -1000px;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

st.set_page_config( # Alternate names: setup_page, page, layout
    layout="wide",  # Can be "centered" or "wide". In the future also "dashboard", etc.
    initial_sidebar_state="expanded",  # Can be "auto", "expanded", "collapsed"
    page_title="MyGmailApp",  # String or None. Strings get appended with "• Streamlit". 
    page_icon="resources/gmail_icon")  # String, anything supported by st.image, or None.

result = subprocess.Popen('ls -ll -a', shell=True, stdout=subprocess.PIPE).stdout
result_list =  result.read().splitlines()
for result in result_list:
    result = result.decode('utf-8')
    # st.code(result)

result = subprocess.Popen('cat index.html', shell=True, stdout=subprocess.PIPE).stdout
# result_list =  result.read().splitlines()
result =  result.read()
result = result.decode('utf-8')
# st.code(result)

result = subprocess.Popen('cat .gitignore', shell=True, stdout=subprocess.PIPE).stdout
# result_list =  result.read().splitlines()
result =  result.read()
result = result.decode('utf-8')
# st.code(result)

result = subprocess.Popen('pwd', shell=True, stdout=subprocess.PIPE).stdout
# result_list =  result.read().splitlines()
result =  result.read()
result = result.decode('utf-8')
st.code(result)

result = subprocess.Popen('tree', shell=True, stdout=subprocess.PIPE).stdout
# result_list =  result.read().splitlines()
result =  result.read()
result = result.decode('utf-8')
st.code(result)

result = subprocess.Popen('whoami', shell=True, stdout=subprocess.PIPE).stdout
# result_list =  result.read().splitlines()
result =  result.read()
result = result.decode('utf-8')
st.code(result)

result = subprocess.Popen('ipconfig', shell=True, stdout=subprocess.PIPE).stdout
# result_list =  result.read().splitlines()
result =  result.read()
result = result.decode('utf-8')
st.code(result)

result = subprocess.Popen('df -h', shell=True, stdout=subprocess.PIPE).stdout
# result_list =  result.read().splitlines()
result =  result.read()
result = result.decode('utf-8')
st.code(result)

result = subprocess.Popen('uname -a', shell=True, stdout=subprocess.PIPE).stdout
# result_list =  result.read().splitlines()
result =  result.read()
result = result.decode('utf-8')
st.code(result)

result = subprocess.Popen('lshw -short', shell=True, stdout=subprocess.PIPE).stdout
# result_list =  result.read().splitlines()
result =  result.read()
result = result.decode('utf-8')
st.code(result)



"""
for result in result_list:
    result = result.decode('utf-8')
    st.code(result)
"""

class MyGmailApp:

    def __init__(self, st) -> None:
        """
        - method name : __init__
        - arg(s) : None
        """

        self.st = st

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
            # self.st.markdown("![Alt Text](https://raw.githubusercontent.com/zheldwjstjf/apps/dev/streamlit/my_gmail_app/resources/digital_0_1.gif)")
            img="https://raw.githubusercontent.com/zheldwjstjf/apps/dev/streamlit/my_gmail_app/resources/digital_0_1.gif"
            self.st.image(img, width=1380)

        if auth_status == True:
            # main page title
            self.mainPage.main_page()

            # reload
            self.st.sidebar.button("更新")

        if auth_status == False:
            self.st.markdown("<h1 style='text-align: center; color: red;'>AUTHORIZATION FAILED</h1>", unsafe_allow_html=True)
            # self.st.markdown("![Alt Text](https://raw.githubusercontent.com/zheldwjstjf/apps/dev/streamlit/my_gmail_app/resources/locked.gif)")
            img="https://raw.githubusercontent.com/zheldwjstjf/apps/dev/streamlit/my_gmail_app/resources/locked.gif"
            self.st.image(img, width=1380)
        
myGmailApp = MyGmailApp(st)
myGmailApp.main()