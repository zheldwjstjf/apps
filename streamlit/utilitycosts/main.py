import streamlit as st

from pages.main_page import MainPage
from pages.side_menu import SideMenu
from modules.csv_tool import CSVTool
from pages.auth_page import AuthPage

# ===================================
# st config
# ===================================
st.set_page_config(  # Alternate names: setup_page, page, layout
    layout="wide",  # Can be "centered" or "wide". In the future also "dashboard", etc.
    initial_sidebar_state="collapsed",  # Can be "auto", "expanded", "collapsed"
    page_title="我が家の光熱費",  # String or None. Strings get appended with "• Streamlit". 
    # page_icon=None,  # String, anything supported by st.image, or None.
)

class App:

    def __init__(self):
        self.st = st

        # =================
        self.sm = SideMenu(st)
        self.ap = AuthPage(st)
        self.mp = MainPage(st)
        self.cSVTool = CSVTool(self.st)
        

    def main(self):

        # =================
        # main page title
        self.st.markdown("<h1 style='text-align: center; color: red;'>光熱費がやばい！</h1>", unsafe_allow_html=True)

        # =================
        # load data
        self.df = self.cSVTool.load_data()

        # main page
        self.mp.main_page(self.df)

        # =================
        # side mmenu title
        st.sidebar.markdown("<h1 style='text-align: center; color: red;'>[ S I D E - M E N U ]</h1>", unsafe_allow_html=True)

        # sidebar page : auth
        with st.sidebar.expander("[ 認証 ]"):
            auth_status = self.ap.auth_page()

            if auth_status == None:
                self.st.warning("未認証")

            if auth_status == True:
                self.st.success("認証済")

            if auth_status == False:
                self.st.error("認証失敗")

        # sidebar page : add data
        with st.sidebar.expander("[ 登録 ]"):
            self.sm.side_menu(self.df, auth_status)

        # reload
        self.st.sidebar.button("更新")

app = App()
app.main()