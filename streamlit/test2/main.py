import streamlit as st
from pages.auth_page import AuthPage
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

    def __init__(self) -> None:

        self.st = st

        #
        self.ap = AuthPage(st)
        self.sm = SideMenu(st)
        self.mp = MainPage(st)
        self.cSVTool = CSVTool(self.st)

        print("[DEBUG] credent_status - main.py - 111 : >>> ", str(self.credent_status))

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

        print("[DEBUG] credent_status - main.py - 222 : >>> ", str(self.credent_status))
        
        # sidebar page : 更新
        with st.sidebar.expander("更新"):
            with self.st.form(key='my_form'):
                submit_button = self.st.form_submit_button(label='更新')

        # sidebar page : auth
        if (self.ap.credent_status != False) and (self.ap.credent_status != None):
            self.st.write("main.py", "111>>> ", str(self.credent_status))
            # main page
            self.mp.main_page(df)

            # sidebar page : add data
            with st.sidebar.expander("登録"):
                self.sm.side_menu(df)
        
        elif (self.ap.credent_status == False) or (self.ap.credent_status == None):
            self.st.write("main.py", "333>>> ", str(self.credent_status))
            with st.sidebar.expander("認証"):
                auth_status = self.ap.auth_page()

            if auth_status == True:
                self.st.write("main.py", "333>>> ", str(self.credent_status))
                # main page
                self.mp.main_page(df)

                # sidebar page : add data
                with st.sidebar.expander("登録"):
                    self.sm.side_menu(df)

            elif auth_status == False:
                self.st.write("main.py", "444>>> ", str(self.credent_status))
                st.sidebar.markdown("<h3 style='text-align: left; color: red;'>認証が必要です。</h3>", unsafe_allow_html=True)
            else:
                self.st.write("main.py", "555>>> ", str(self.credent_status))
                pass
        
        else:
            self.st.write("main.py", "666>>> ", str(self.credent_status))
        
        print("[DEBUG] credent_status - main.py - 333 : >>> ", str(self.credent_status))

app = App()
app.main()