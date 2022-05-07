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
        self.auth_check_result = []

    @st.cache(suppress_st_warning=True)
    def createService(self, stringio):
        """
        createService
        """

        auth_info = json.load(stringio)

        if auth_info['installed']["product_id"] == self.st.secrets["product_id"]:
            self.auth_check_result.append(True)
        else:
            self.auth_check_result.append(False)

        if auth_info['installed']["client_id"] == self.st.secrets["client_id"]:
            self.auth_check_result.append(True)
        else:
            self.auth_check_result.append(False)

        if auth_info['installed']["client_secret"] == self.st.secrets["client_secret"]:
            self.auth_check_result.append(True)
        else:
            self.auth_check_result.append(False)

        if False in self.auth_check_result:
            self.st.write("認証情報が一致しません。")
            return False
        else:
            if self.auth_check_result.count(True) == 3:
                self.st.write("認証情報が一致しました。")
                return True
            else:
                self.st.write("認証情報が一足りません。")
                return False