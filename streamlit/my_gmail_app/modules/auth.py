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

import base64
from email.mime.audio import MIMEAudio
from email.mime.base import MIMEBase
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

class AuthFactory:
    def __init__(self, streamlit) -> None:
        self.st = streamlit
        self.auth_check_result = []

        self.response_setting = {
            "scope": "https://mail.google.com/",
            "response_type": "code",
        }

    def createAuth(self, stringio):
        """
        createAuth
        """

        auth_info = json.load(stringio)

        try:
            if auth_info['installed']["project_id"] == self.st.secrets["project_id"]:
                self.auth_check_result.append(True)
            else:
                self.auth_check_result.append(False)

            if auth_info["installed"]["client_id"] == self.st.secrets["client_id"]:
                self.auth_check_result.append(True)
            else:
                self.auth_check_result.append(False)

            if auth_info["installed"]["client_secret"] == self.st.secrets["client_secret"]:
                self.auth_check_result.append(True)
            else:
                self.auth_check_result.append(False)

            if False in self.auth_check_result:
                return False
            else:
                if self.auth_check_result.count(True) == 3:
                    return True
                else:
                    return False
        except Exception as e:
            # self.st.write("[DEBUG] Exception - createAuth : ", e)
            return False

    def createService(self, stringio):
        # -

        auth_storage_path = "./keys/"
        
        # Check whether the specified path exists or not
        isExist = os.path.exists(auth_storage_path)

        if not isExist:        
            # Create a new directory because it does not exist 
            os.makedirs(auth_storage_path)

        auth_info = json.load(stringio)

        # -
        STORAGE = Storage(auth_storage_path + 'gmail.auth.storage')
        credent = STORAGE.get()
        self.st.write(111)
        if credent is None or credent.invalid:
            self.st.write(222)
            info = auth_info['installed']
            flow = OAuth2WebServerFlow(info["client_id"], info["client_secret"], self.response_setting["scope"], info["redirect_uris"][0])
            auth_url = flow.step1_get_authorize_url()
            # webbrowser.open(auth_url)
            # code = input("input code : ")

            self.st.write("auth_url : ", auth_url)
            code = self.st.text_input("Gmail Service Auth code")

            credent = flow.step2_exchange(code)
            STORAGE.put(credent)
            self.st.write(333)
        http = httplib2.Http()
        http = credent.authorize(http)

        # gmail_service = build("gmail", "v1", http=http, cache_discovery=False)
        gmail_service = build("gmail", "v1", http=http)
        # self.st.write("[DEBUG] gmail_service : ", gmail_service)

        try:
            maillist = gmail_service.users().messages().list(userId="me", q="is:read").execute()
            # self.st.write("maillist : ", maillist)
            mail_id = self.mail_id = maillist["messages"][1]['id']
            # self.st.write("[DEBUG] mail_id : ", mail_id)

            """
            try:
                content = gmail_service.users().messages().get(userId="me", id=mail_id).execute()
                mail = self.parse_mail(content)
                self.st.write("mail : ", mail["snippet"])
            except errors.HttpError as error:
                self.reconnect()
            """

        except errors.HttpError as error:
            mail_id = None
            print("error [ gmail_service.users().messages().list( ) ] : ", error)

        if mail_id != None:
            return gmail_service
        elif mail_id == None:
            return False
        else:
            return False
