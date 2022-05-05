import os
import json
import platform
from apiclient.discovery import build
import webbrowser
from oauth2client.client import OAuth2WebServerFlow
from oauth2client.file import Storage
import httplib2
from apiclient import errors
import streamlit as st

class AuthFactory:
    def __init__(self, streamlit) -> None:
        self.st = streamlit
        self.auth_url = "https://accounts.google.com/o/oauth2/auth?"
        self.response_setting = {
            "scope": "https://mail.google.com/",
            "response_type": "code"}

    def createService(self, stringio):
        """
        createService
        """

        auth_info = json.load(stringio)

        if auth_info['installed']["client_id"] == "358645828252-5al16h67s91emmsub4q3gndqbgqlo6rl.apps.googleusercontent.com":
        
            try:
                info = auth_info['installed']
                self.flow = OAuth2WebServerFlow(info["client_id"], info["client_secret"], self.response_setting["scope"], info["redirect_uris"][0])
                self.auth_url = self.flow.step1_get_authorize_url()
                
                # ブラウザを開いて認証する
                # webbrowser.open(self.auth_url)
                self.st.write("auth_url: ", self.auth_url)

                code = self.st.text_input("CODE", placeholder="Paste your code here.")
                # code = input("input code : ")

                print("code : ", code)
                self.st.write("code : ", code)

                if self.st.button("SUBMIT"):
                    self.credent = self.flow.step2_exchange(code)
                    http = httplib2.Http()
                    http = self.credent.authorize(http)

                    try:
                        gmail_service = build("gmail", "v1", http=http)
                        self.st.write("gmail_service : ", gmail_service)

                        return True
                    except Exception as e:
                        return False

            except Exception as e:
                print("Exception : createService : ", e)
                
                return False

        else:
            self.st.write("idが一致しません。")
            return False
