import json
from io import StringIO
import importlib
import copy

from modules.auth import AuthFactory

class AuthPage:

    def __init__(self, streamlit) -> None:
        self.st = streamlit
        self.auth_status = None
        self.authFactory = AuthFactory(self.st)

    def auth_page(self):

        if self.auth_status == True:
            
            return True

        else:
            if self.auth_status == None:
                uploaded_file = self.st.file_uploader("▶︎ 認証キーを選択してください。")
                self.st.write("[DEBUG] uploaded_file  : ", uploaded_file)

            # if self.st.button("認証"):
            if uploaded_file is not None:

                # To convert to a string based IO:
                stringio = StringIO(uploaded_file.getvalue().decode("utf-8"))
                stringio2 = copy.copy(stringio)

                self.auth_status = self.authFactory.createAuth(stringio)
                if self.auth_status == True:
                    gmail_service = self.authFactory.createService(stringio2) 

                if self.auth_status == None:
                    return False

                elif self.auth_status == False:
                    return False

                elif (self.auth_status != None) and (self.auth_status == False):
                    return gmail_service

                else:
                    return False

            if uploaded_file is None:
                return None
