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

        print("[DEBUG] 00001 - def __init__(self)")

        self.st = st

        #
        print("[DEBUG] 00002 - def __init__(self)")
        self.sm = SideMenu(st)
        self.mp = MainPage(st)
        self.cSVTool = CSVTool(self.st)

        #
        print("[DEBUG] 00003 - def __init__(self)")
        self.auth_url = "https://accounts.google.com/o/oauth2/auth?"
        self.response_setting = {
            "scope": "https://mail.google.com/",
            "response_type": "code"}

        #
        print("[DEBUG] 00004 - def __init__(self)")
        self.auth_status = ""
        self.auth_status2 = ""
        self.code = ""
        self.flow_step2 = ""

        print("[DEBUG] 00005 - def __init__(self)")



    def main(self):

        print("[DEBUG] 00006 - def main(self)")

        # =================
        # main page title
        print("[DEBUG] 00007 - def main(self)")
        self.st.markdown("<h1 style='text-align: center; color: red;'>我が家の光熱費</h1>", unsafe_allow_html=True)


        # =================
        # load data
        self.df = self.cSVTool.load_data()


        # =================
        # side mmenu title
        print("[DEBUG] 00008 - def main(self)")
        st.sidebar.markdown("<h1 style='text-align: center; color: red;'>[ S I D E - M E N U ]</h1>", unsafe_allow_html=True)


        # =================
        print("[DEBUG] 00009 - def main(self)")
        self.auth_status = self.auth()

        if (self.auth_status == None) and (self.code != ""):
            self.flow_step2 = True
            self.auth_status2 = "abcd"
        print("[DEBUG] auth_status - main.py - 555 : >>> ", str(self.auth_status))
        print("[DEBUG] auth_status2 - main.py - 555 : >>> ", str(self.auth_status2))
        print("[DEBUG] self.code - main.py - 555 : >>> ", str(self.code))
        print("[DEBUG] flow_step2 - main.py - 555 : >>> ", str(self.flow_step2))


        # =================
        print("[DEBUG] 00010 - def main(self)")
        if (self.auth_status == None) and (self.code == ""):
            st.sidebar.markdown("<h3 style='text-align: left; color: red;'>認証が必要です。</h3>", unsafe_allow_html=True)

        elif (self.flow_step2 == "") and (self.code == ""):
            st.sidebar.markdown("<h3 style='text-align: left; color: red;'>認証失敗</h3>", unsafe_allow_html=True)

        
        elif (self.auth_status != False) and (self.flow_step2 != "") and (self.code != ""):
        # elif (self.flow_step2 != "") and (self.auth_status2 != "") and (self.code != ""):
        # elif (self.auth_status != False) and (self.code != ""):
            st.sidebar.markdown("<h3 style='text-align: left; color: red;'>認証成功</h3>", unsafe_allow_html=True)

            # main page
            self.mp.main_page(self.df)

            # sidebar page : add data
            with st.sidebar.expander("[ 登録 ]"):
                self.sm.side_menu(self.df)
        
        print("[DEBUG] 00011 - def main(self)")


    def auth(self):
    
        print("[DEBUG] auth_status - main.py - 111 : >>> ", str(self.auth_status))
        print("[DEBUG] auth_status2 - main.py - 111 : >>> ", str(self.auth_status2))
        print("[DEBUG] self.code - main.py - 111 : >>> ", str(self.code))
        print("[DEBUG] flow_step2 - main.py - 111 : >>> ", str(self.flow_step2))

        with st.sidebar.expander("[ 認証 ]"):

            self.st.write("auth_page", "111>>> ", str(self.auth_status))

            self.st.markdown("<h3 style='text-align: left; color: red;'>認証キーを選択してください。</h3>", unsafe_allow_html=True)

            uploaded_file = self.st.file_uploader("▶︎ Choose a file")

            if uploaded_file is not None:
                self.st.write("auth_page", "222>>> ", str(self.auth_status))
                print("[DEBUG] auth_status - main.py - 333 : >>> ", str(self.auth_status))
                print("[DEBUG] auth_status2 - main.py - 333 : >>> ", str(self.auth_status2))
                print("[DEBUG] self.code - main.py - 333 : >>> ", str(self.code))
                print("[DEBUG] flow_step2 - main.py - 333 : >>> ", str(self.flow_step2))

                # To convert to a string based IO:
                stringio = StringIO(uploaded_file.getvalue().decode("utf-8"))

                auth_info = json.load(stringio)

                if auth_info['installed']["client_id"] == "358645828252-5al16h67s91emmsub4q3gndqbgqlo6rl.apps.googleusercontent.com":
                
                    info = auth_info['installed']
                    self.flow = OAuth2WebServerFlow(info["client_id"], info["client_secret"], self.response_setting["scope"], info["redirect_uris"][0])
                    self.auth_url = self.flow.step1_get_authorize_url()
                    
                    # ブラウザを開いて認証する
                    # webbrowser.open(self.auth_url)
                    self.st.write("auth_url: ", self.auth_url)
    
                    # code = input("input code : ")
                    self.code = self.st.text_input("▶︎ Input Authentication Code", placeholder="Paste your code here.")
                    print("code : ", self.code)
                    self.st.write("code : ", self.code)

                    print("[DEBUG] auth_status - main.py - 444 : >>> ", str(self.auth_status))
                    print("[DEBUG] auth_status2 - main.py - 444 : >>> ", str(self.auth_status2))
                    print("[DEBUG] self.code - main.py - 444 : >>> ", str(self.code))
                    print("[DEBUG] flow_step2 - main.py - 444 : >>> ", str(self.flow_step2))
                    

                    if self.st.button("▶︎ SUBMIT"):
                    # with self.st.form(key='my_form'):
                    # submit_button = self.st.form_submit_button(label='更新')
                        
                        if (self.code != "") and (self.auth_status2 == ""):

                            self.tmp()

                            """
                            try:
                                self.credent = self.flow.step2_exchange(self.code)
                                http = httplib2.Http()
                                http = self.credent.authorize(http)

                                self.auth_status2 = build("gmail", "v1", http=http)
                                
                                self.st.write("認証されました。")

                                self.auth_status2 = str(self.auth_status2)

                                print("[DEBUG] auth_status2 - main.py - 444 : >>> ", self.auth_status2)
                                self.st.write("auth_status2 : ", self.auth_status2)

                                self.flow_step2 = True

                                return True

                            except Exception as e:
                                self.st.write("auth_page", "666>>> ", str(self.auth_status))
                                print("[DEBUG] auth_status - main.py - 666 : >>> ", str(self.auth_status))
                                self.st.write("認証中に問題が発生しました。")

                                self.flow_step2 = False

                                return False
                            """
                        
                        else:
                            print("[DEBUG] auth_status - main.py - 666-222 : >>> ", str(self.auth_status))
                            print("[DEBUG] auth_status2 - main.py - 666-222 : >>> ", str(self.auth_status2))
                            # if (str(self.auth_status2) != "") and (self.code != ""):
                            if (self.flow_step2 == True) and (self.code != ""):
                                return True
                            else:
                                return False

                    else:
                        return False

                else:
                    self.st.write("idが一致しません。")
                    return False


            elif uploaded_file is None:
                self.st.write("auth_page", "777>>> ", str(self.auth_status))
                print("[DEBUG] auth_status - main.py - 777 : >>> ", str(self.auth_status))
                self.st.write("認証キーが選択されてません。")
                    
                return False


    @st.cache(suppress_st_warning=True)
    def tmp(self):

        try:
            self.credent = self.flow.step2_exchange(self.code)
            http = httplib2.Http()
            http = self.credent.authorize(http)

            self.auth_status2 = build("gmail", "v1", http=http)
            
            self.st.write("認証されました。")

            self.auth_status2 = str(self.auth_status2)

            print("[DEBUG] auth_status2 - main.py - 444 : >>> ", self.auth_status2)
            self.st.write("auth_status2 : ", self.auth_status2)

            self.flow_step2 = True

            return True

        except Exception as e:
            self.st.write("auth_page", "666>>> ", str(self.auth_status))
            print("[DEBUG] auth_status - main.py - 666 : >>> ", str(self.auth_status))
            self.st.write("認証中に問題が発生しました。")

            self.flow_step2 = False

            return False

app = App()
app.main()