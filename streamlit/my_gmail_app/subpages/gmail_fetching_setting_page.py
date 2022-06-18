from modules.gmailapi import GmailApi
from modules.visualization_tool import VisualizationTool

import json

import base64
from email.mime.audio import MIMEAudio
from email.mime.base import MIMEBase
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

import streamlit.components.v1 as components

class GmailFetchingSettingPage:
    """
    - class name : MainPage
    """

    def __init__(self, streamlit) -> None:
        """
        - method name : __init__
        - arg(s) : streamlit
        """

        self.st = streamlit
        self.query = ""

    def gmail_fetching_setting_page(self):
        """
        - method name : main_page
        - arg(s) : streamlit
        """

        # title
        self.st.markdown("<h1 style='text-align: center; color: red;'>MY GMAIL APP</h1>", unsafe_allow_html=True)

        self.user = "me"

        # select priority label
        col1, col2 = self.st.columns((1,1))
        with col1:
            self.st.subheader("▶︎ Select Priority Label")
            self.priority_label = self.get_priority_label()

        # select email
        self.st.subheader("▶︎ Select Email")
        self.query_froms = self.get_query_from(self.priority_label)
        self.query = self.query + self.query_from + " "

        # get query
        self.st.subheader("▶︎ Query設定")

        col1, col2 = self.st.columns((1,1))

        with col1:
            query_key_list = [
                    "is",
                    "subject",
                    "to",
                    "has",
                    "label"
                ]
            selected_query_keys = self.st.multiselect("主なQuery", query_key_list, default=query_key_list[0], key="main")

            if "is" in selected_query_keys:
                self.query_is = self.get_query_is()
                self.query = self.query + self.query_is + " "

            if "subject" in selected_query_keys:
                self.query_subject = self.get_query_subject()
                self.query = self.query + self.query_subject + " "

        with col2:
            query_key_list = [
                    "after",
                    "before",
                    "older",
                    "newer",
                    "older_than",
                    "newer_than"
                ]
            selected_query_keys = self.st.multiselect("その他のQuery", query_key_list, key="sub")

            if "newer_than" in selected_query_keys:
                self.query_newer_than = self.get_query_newer_than()
                self.query = self.query + self.query_newer_than + " "

            if "older_than" in selected_query_keys:
                self.query_older_than = self.get_query_older_than()
                self.query = self.query + self.query_older_than + " "

    def get_priority_label(self):

        priority_label_list = [
            "High",
            "Medium",
            "Low"
        ]
        selected_priority = self.st.multiselect("Select Email", priority_label_list, key="priority")

        return selected_priority     
    

    def get_query_from(self, priority_label):

        self.priority_label = priority_label
        
        #
        col1, col2 = self.st.columns((1,1))

        # TODO 데이터베이스에서 가져오도록 할 것
        email_list = [
                "All High priority email",
                "editor1@kdnuggets.com",
                "weekly@raspberrypi.com",
                "noreply@medium.com",
                "no-reply@m.ouraring.com",
                "All Medium priority email",
                "change@f.change.org",
                "no-reply@sender.skyscanner.com",
                "All Low priority email",
                "reminders@facebookmail.com",
                "noreply@uber.com",
            ]

        selected_query_from_val = col1.selectbox("Select Email", email_list, key="from")
        selected_query_from_val = str(selected_query_from_val)
        if "@" not in selected_query_from_val:
            selected_query_from_val = ""
        self.query_from = "from:" + selected_query_from_val

        selected_email_info_list = [
            "[ TODO ] 메일 제목의 주요 키워드（시각화 ）",
            "[ TODO ] 메일 본문의 주요 키워드（시각화 ）",
            "[ TODO ] 메일 발송 시각 분포",
            "[ TODO ] 메일 발송 빈도",
        ]        
        self.query_from = "from:" + selected_query_from_val

        selected_info_itme = col2.selectbox("Select Email Info Item", selected_email_info_list, key="email_info")

        # 
        col1, col2 = self.st.columns((1,1))
        col2.write("INFO : " + str(selected_info_itme))
        col2.code(selected_info_itme)

        return self.query_from

    def get_query_is(self):
        query_is_val_list = [
                "read",
                "unread",
                "starred",
                "snoozed",
            ]
        selected_query_is_val = self.st.selectbox("Select Query Value", query_is_val_list, index=1, key="is")
        self.query_is = "is:" + selected_query_is_val

        return self.query_is

    def get_query_subject(self):
        selected_query_subject_val = self.st.text_input("", placeholder="ここに入力")
        self.query_subject = "subject:" + selected_query_subject_val

        return self.query_subject

    def get_query_newer_than(self):
        query_newer_than_val_list = [
                "1d",
                "2d",
                "3d",
                "4d",
                "5d",
                "6d",
                "7d",
                "10d",
                "15d",
                "20d",
                "1m",
                "2m",
                "3m",
                "4m",
                "5m",
                "6m",
                "7m",
                "8m",
                "9m",
                "10m",
                "11m",
                "1y",
                "2y",
                "3y",
                "4y",
                "5y",
            ]
        selected_query_newer_than_val = self.st.selectbox("Select Query Value", query_newer_than_val_list, key="newer_than")
        self.query_newer_than = "newer_than:" + selected_query_newer_than_val

        return self.query_newer_than


    def get_query_older_than(self):
        query_older_than_val_list = [
                "1d",
                "2d",
                "3d",
                "4d",
                "5d",
                "6d",
                "7d",
                "10d",
                "15d",
                "20d",
                "1m",
                "2m",
                "3m",
                "4m",
                "5m",
                "6m",
                "7m",
                "8m",
                "9m",
                "10m",
                "11m",
                "1y",
                "2y",
                "3y",
                "4y",
                "5y",
            ]
        selected_query_older_than_val = self.st.selectbox("Select Query Value", query_older_than_val_list, key="older_than")
        self.query_older_than = "older_than:" + selected_query_older_than_val

        return self.query_older_than
