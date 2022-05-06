import json
from io import StringIO
import streamlit as st

from modules.auth import AuthFactory

class AuthPage:

    def __init__(self, streamlit):
        self.st = streamlit
        self.authFactory = AuthFactory(self.st)

    def auth_page(self):

        self.auth_status = False

        print("[DEBUG] auth_status - auth_page.py - 111 : >>> ", str(self.auth_status))

        if (self.auth_status != False):
            self.st.write("auth_page", "111>>> ", str(self.auth_status))
            return True

        elif (self.auth_status == False) or (self.auth_status == None):
            self.st.write("auth_page", "222>>> ", str(self.auth_status))
            self.st.markdown("<h3 style='text-align: left; color: red;'>認証キーを選択してください。</h3>", unsafe_allow_html=True)

            uploaded_file = self.st.file_uploader("Choose a file")

            if uploaded_file is not None:
                self.st.write("auth_page", "333>>> ", str(self.auth_status))
                print("[DEBUG] auth_status - auth_page.py - 333 : >>> ", str(self.auth_status))

                # To convert to a string based IO:
                stringio = StringIO(uploaded_file.getvalue().decode("utf-8"))
                
                self.auth_status = self.authFactory.createService(stringio)

                print("[DEBUG] auth_status - auth_page.py - ### : >>> ", str(self.auth_status))

                if (self.auth_status != False) and (self.auth_status != None):
                    self.auth_status = str(self.auth_status)
                    self.st.write("auth_page", "444>>> ", self.auth_status)
                    print("[DEBUG] auth_status - auth_page.py - 444 : >>> ", str(self.auth_status))
                    self.st.write("認証されました。")

                    return True

                elif (self.auth_status == None):
                    self.st.write("auth_page", "555>>> ", str(self.auth_status))
                    print("[DEBUG] auth_status - auth_page.py - 555 : >>> ", str(self.auth_status))
                    self.st.write("認証されてません。")
                    
                    return None
                
                elif (self.auth_status == False):
                    self.st.write("auth_page", "555>>> ", str(self.auth_status))
                    print("[DEBUG] auth_status - auth_page.py - 555 : >>> ", str(self.auth_status))
                    self.st.write("認証中に問題が発生しました。")
                    
                    return False

                else:
                    self.st.write("auth_page", "666>>> ", str(self.auth_status))
                    print("[DEBUG] auth_status - auth_page.py - 666 : >>> ", str(self.auth_status))
                    self.st.write("認証中に問題が発生しました。")

                    return False

            elif uploaded_file is None:
                self.st.write("auth_page", "777>>> ", str(self.auth_status))
                print("[DEBUG] auth_status - auth_page.py - 777 : >>> ", str(self.auth_status))
                self.st.write("認証キーが選択されてません。")
                    
                return None
            
            else:
                self.st.write("auth_page", "888>>> ", str(self.auth_status))
                print("[DEBUG] auth_status - auth_page.py - 888 : >>> ", str(self.auth_status))
                self.st.write("認証キーが取得できませんでした。")
        
        else:
            self.st.write("auth_page", "999>>> ", str(self.auth_status))
            self.st.write("認証されてません。")

            return False
