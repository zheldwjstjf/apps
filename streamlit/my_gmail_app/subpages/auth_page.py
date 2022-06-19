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
                uploaded_file = self.st.file_uploader("● 認証キーを選択してください。")
                # self.st.write("[DEBUG] uploaded_file info type : ", type(uploaded_file))
                # self.st.write("[DEBUG] uploaded_file info : ", uploaded_file)



            # if self.st.button("認証"):
            if uploaded_file is not None:

                uploaded_file_str = str(uploaded_file)
                uploaded_file_type = uploaded_file_str.split("type=")[1]

                if "json" in uploaded_file_type:

                    # To convert to a string based IO:
                    stringio = StringIO(uploaded_file.getvalue().decode("utf-8"))
                    stringio2 = copy.copy(stringio)

                    self.auth_status = self.authFactory.createAuth(stringio)
                    if self.auth_status == True:
                        gmail_service = self.authFactory.createService(stringio2) 
                        return gmail_service
                        
                    if self.auth_status == None:
                        return False

                    elif self.auth_status == False:
                        return False

                    else:
                        return False

                elif "json" not in uploaded_file_type:
                    return False

                else:
                    return False

            elif uploaded_file is None:
                return None

            else:
                return False
