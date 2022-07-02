import json

import base64
from email.mime.audio import MIMEAudio
from email.mime.base import MIMEBase
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

from modules.gmailapi import GmailApi
from modules.visualization_tool import VisualizationTool
from modules.get_text_from_url import GetTextFromURL

import streamlit.components.v1 as components

class GmailFetchingResultTitlePage:
    """
    - class name : MainPage
    """

    def __init__(self, streamlit) -> None:
        """
        - method name : __init__
        - arg(s) : streamlit
        """

        self.st = streamlit
        self.visualizationTool = VisualizationTool(self.st)
        self.getTextFromURL = GetTextFromURL(self.st)

        self.mail_id = None

    def get_mail_content(self, maillist, fetching_count, result_count, service, user):

        contents_list = []

        self.gmail_api = GmailApi(self.st, service)

        if result_count > fetching_count:
            pass
        elif result_count < fetching_count:
            fetching_count = result_count
        elif result_count == fetching_count:
            pass
        elif result_count == 0:
            fetching_count = 0
        else:
            fetching_count = 1

          
        # sub title
        self.st.write("---")
        self.st.markdown("<h2 style='text-align: center; color: red;'>マッチしたメールのLIST</h2>", unsafe_allow_html=True)
        self.st.write("---")

        for i in range(fetching_count):

            content_info = []

            content_info.append("▶︎ " + str(i+1) + " 件目")

            try:
                self.mail_id = self.mail_id = maillist[i]['id']
                self.mail_content = self.gmail_api.getMailContent(user, self.mail_id)

                content_info.append(self.mail_id)

                # - do mail as read
                # self.gmail_api.markMailAsRead(user, self.mail_id)            

                mail = self.parse_mail()

                try:
                    mail_subject = mail['subject']
                    content_info.append(mail_subject)
                except Exception as e:
                    self.st.error("Exception - mail['subject'] : " + "e")

                try:
                    mail_date = mail['date']
                    content_info.append(mail_date)
                except Exception as e:
                    self.st.error("Exception - mail['date'] : " + "e")

                try:
                    mail_from = mail['from']
                    content_info.append(mail_from)
                except Exception as e:
                    self.st.error("Exception - mail['from'] : " + "e")

                try:
                    mail_to = mail['to']
                    content_info.append(mail_to)
                except Exception as e:
                    self.st.error("Exception - mail['to'] : " + "e")

                try:
                    mail_snippet = mail['snippet']
                    content_info.append(mail_snippet)
                except Exception as e:
                    self.st.error("Exception - mail['snippet'] : " + "e")

                try:
                    mail_body = mail['body']
                    content_info.append(mail_body)
                except Exception as e:
                    self.st.error("Exception - mail['body'] : " + "e")

                # order count
                self.st.subheader("▶︎ " + str(i+1) + " 件目")

                contents_list.append(content_info)

                ########################

                # mail_subject
                self.st.subheader("[ " + mail_subject + " ]")
                self.st.info(mail_date)

            except Exception as e:
                self.st.warning("No more Email")

            # line
            self.st.write("---")

        self.st.success("Fetching Done")
        return contents_list


    def parse_mail(self):
        content = self.mail_content

        mail = {}

        if 'parts' in content['payload'].keys():
            parts = content['payload']['parts'][0]
            # # print("[ DEBUG 7 ] type parts : ", type(parts))
            # print(parts)
            if 'parts' in parts.keys():
                try:
                    raw_body = parts['parts'][0]['body']['data']
                except Exception as e:
                    raw_body = parts['parts'][0]['parts'][0]['body']['data']
            else:
                raw_body = parts['body']['data']
        else:
            raw_body = content['payload']['body']['data']
        mail['body'] = base64.urlsafe_b64decode(raw_body).decode('utf-8')
        mail['snippet'] = content['snippet']
        headers = content['payload']['headers']
        for header in headers:
            if header['name'] == 'From':
                mail['from'] = header['value']
            elif header['name'] == 'To':
                mail['to'] = header['value']
            elif header['name'] == 'Subject':
                mail['subject'] = header['value']
            elif header['name'] == 'Date':
                mail['date'] = header['value']

        self.mail = mail
        return self.mail
