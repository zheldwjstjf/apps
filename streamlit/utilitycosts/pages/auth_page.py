import json
from io import StringIO

from modules.auth import AuthFactory

class AuthPage:

    def __init__(self, streamlit) -> None:
        self.st = streamlit
        self.auth_status = None
        self.authFactory = AuthFactory(self.st)

    def auth_page(self):

        # with self.st.form(key='my_form'):
        # submit_button = self.st.form_submit_button(label='更新')

        if self.auth_status == True:
            
            return True

        else:
            if self.auth_status == None:
                uploaded_file = self.st.file_uploader("▶︎ 認証キーを選択してください。")

            # if self.st.button("認証"):
            if uploaded_file is not None:

                # To convert to a string based IO:
                stringio = StringIO(uploaded_file.getvalue().decode("utf-8"))
                self.auth_status = self.authFactory.createService(stringio)

                if self.auth_status == None:
                    return None

                if self.auth_status == True:                    
                    return True

                if self.auth_status == False:
                    return False

            if uploaded_file is None:
                return None