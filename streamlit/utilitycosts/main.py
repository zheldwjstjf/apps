import streamlit as st
from io import StringIO

from pages.main_page import MainPage
from pages.side_menu import SideMenu
from modules.csv_tool import CSVTool

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

        #
        print("[DEBUG] 00002 - def __init__(self)")
        self.sm = SideMenu(st)
        self.mp = MainPage(st)
        self.cSVTool = CSVTool(self.st)

    def main(self):

        # =================
        # load data
        self.df = self.cSVTool.load_data()

        # =================
        # main page title
        self.st.markdown("<h1 style='text-align: center; color: red;'>我が家の光熱費</h1>", unsafe_allow_html=True)

        # main page
        self.mp.main_page(self.df)

        # =================
        # side mmenu title
        st.sidebar.markdown("<h1 style='text-align: center; color: red;'>[ S I D E - M E N U ]</h1>", unsafe_allow_html=True)

        # sidebar page : add data
        with st.sidebar.expander("[ 登録 ]"):
            self.sm.side_menu(self.df)
        
app = App()
app.main()