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

    # @st.cache(suppress_st_warning=True)
    def createService(self, stringio):
        """
        createService
        """

        auth_info = json.load(stringio)

        try:
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

            self.st.info(self.auth_check_result)

            if False in self.auth_check_result:
                return False
            else:
                if self.auth_check_result.count(True) == 3:
                    return True
                else:
                    return False
        except:
            return False
