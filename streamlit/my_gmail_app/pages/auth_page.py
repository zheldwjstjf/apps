import json
from io import StringIO
import importlib
import sys
from apiclient.discovery import build
import webbrowser
from oauth2client.client import OAuth2WebServerFlow
from oauth2client.file import Storage
# from oauth2client.tools import run
import httplib2
from apiclient import errors
from multiprocessing import Process, Value

import base64
from email.mime.audio import MIMEAudio
from email.mime.base import MIMEBase
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

from modules.auth import AuthFactory

class AuthPage:

    def __init__(self, streamlit) -> None:
        self.st = streamlit
        self.auth_status = None
        self.authFactory = AuthFactory(self.st)

        # auth_url = "https://accounts.google.com/o/oauth2/auth?"

        self.response_setting = {
            "scope": "https://mail.google.com/",
            "response_type": "code",
        }


    def auth_page(self):

        if self.auth_status == True:
            
            return True

        else:
            if self.auth_status == None:
                uploaded_file = self.st.file_uploader("▶︎ 認証キーを選択してください。")

            # if self.st.button("認証"):
            if uploaded_file is not None:

                # To convert to a string based IO:
                stringio = StringIO(uploaded_file.getvalue().decode("utf-8"))
                self.st.write("stringio : ", stringio)
                self.auth_status = self.authFactory.createAuth(stringio)

                if self.auth_status == None:
                    return None

                if self.auth_status == True:                    
                    return True

                if self.auth_status == False:
                    return False

            if uploaded_file is None:
                return None

    def createService(self, auth_info):
        # -
        auth_storage_path = ""

        # -
        STORAGE = Storage(auth_storage_path + 'gmail.auth.storage')
        credent = STORAGE.get()
        if credent is None or credent.invalid:
            info = auth_info['installed']
            flow = OAuth2WebServerFlow(info["client_id"], info["client_secret"], self.response_setting["scope"], info["redirect_uris"][0])
            auth_url = flow.step1_get_authorize_url()
            webbrowser.open(auth_url)
            code = input("input code : ")
            credent = flow.step2_exchange(code)
            STORAGE.put(credent)
        http = httplib2.Http()
        http = credent.authorize(http)

        gmail_service = build("gmail", "v1", http=http)
        return gmail_service
