import json
from io import StringIO

from modules.auth import AuthFactory

class AuthPage:

    def __init__(self, streamlit) -> None:
        self.st = streamlit
        self.credent_status = False
        self.authFactory = AuthFactory(self.st)

    def auth_page(self):

        if self.credent_status != False:
            pass

        if self.credent_status == False:
            self.st.markdown("<h3 style='text-align: left; color: red;'>認証キーを選択してください。</h3>", unsafe_allow_html=True)

            uploaded_file = self.st.file_uploader("Choose a file")

            if uploaded_file is not None:

                # To convert to a string based IO:
                stringio = StringIO(uploaded_file.getvalue().decode("utf-8"))
                auth_status = self.authFactory.createService(stringio)

                if auth_status != False:
                    self.st.write("認証されました。")
                    
                    return True

                if auth_status == False:
                    self.st.write("認証中に問題が発生しました。")
                    
                    return False

            if uploaded_file is  None:
                    self.st.write("認証キーが選択されてません。")
                    
                    return False