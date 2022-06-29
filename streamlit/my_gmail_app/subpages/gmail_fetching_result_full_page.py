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
from modules.summarization_tool import SummarizationTool

import streamlit.components.v1 as components

class GmailFetchingResultFullPage:
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
        self.summarizationTool = SummarizationTool(self.st)

        self.mail_id = None
        self.mail_content = None

    def get_mail_content(self, service, user, mail_id, selected_content_info):

        # selected_content_info
        selected_email_order = selected_content_info[0]
        selected_email_id = selected_content_info[1]
        selected_email_title = selected_content_info[2]

        #
        self.gmail_api = GmailApi(self.st, service)
        
        self.mail_id = mail_id

        try:
            self.mail_content = self.gmail_api.getMailContent(user, self.mail_id)

            mail = self.parse_mail()

            try:
                mail_subject = mail['subject']
            except Exception as e:
                self.st.error("Exception- mail['subject'] : " + "e")

            try:
                mail_date = mail['date']
            except Exception as e:
                self.st.error("Exception- mail['date'] : " + "e")

            try:
                mail_from = mail['from']
            except Exception as e:
                self.st.error("Exception- mail['from'] : " + "e")

            try:
                mail_to = mail['to']
            except Exception as e:
                self.st.error("Exception- mail['to'] : " + "e")

            try:
                mail_snippet = mail['snippet']
            except Exception as e:
                self.st.error("Exception- mail['snippet'] : " + "e")

            try:
                mail_body = mail['body']
            except Exception as e:
                self.st.error("Exception- mail['body'] : " + "e")

            # sub title
            self.st.write("---")
            self.st.markdown("<h2 style='text-align: center; color: red;'>選択したメールの詳細</h2>", unsafe_allow_html=True)
            self.st.write("---")

            # order num / title
            self.st.subheader(selected_email_order)
            self.st.subheader("● mail_subject : " + mail_subject)

            # text
            col1, col2 = self.st.columns((1,1))
            with col1:
                self.st.subheader("● mail_date : \n"); self.st.code(mail_date)
                self.st.subheader("● mail_from : \n"); self.st.code(mail_from)
                self.st.subheader("● mail_to : \n"); self.st.code(mail_to)
                self.st.subheader("● mail_snippet : \n"); self.st.info(mail_snippet)

            with col2:
                if (("<html") in mail_body) and (("/html>") in mail_body) and (("<head") in mail_body) and (("/body>") in mail_body) and (("/body>") in mail_body) or ("<table" in mail_body) and ("/table>" in mail_body) or ("<div" in mail_body) and ("/div>" in mail_body):
                    self.st.subheader("● mail_body（HTML） : \n")
                    components.html(mail_body, height=4300)
                else:
                    self.st.subheader("● mail_body（TXT） : \n")
                    self.st.write(mail_body)

            # - do mail as read
            # self.gmail_api.markMailAsRead(user, self.mail_id)


            # wordcloud - text from url in mail body
            try:
                target_urls = self.getTextFromURL.get_url_from_text(mail_body)
                target_urls = list(set(target_urls))
            except Exception as e:
                target_urls = []
                self.st.error(str(e))

            try:
                for target_url in target_urls:
                    resutl_text = self.getTextFromURL.extract_text_from_single_web_page(url=target_url)
                    self.st.write("---")
                    self.st.write("● URL : " + target_url)

                    # visualization
                    self.visualizationTool.wordcloud(resutl_text, 1400, 100)

                    # full text
                    with self.st.expander("テキストを見る"):
                        self.st.write(type(resutl_text))
                        self.st.write(resutl_text)

                    # summarization
                    self.summarizationTool.generate_summary(resutl_text, top_n=5)

            except Exception as e:
                self.st.error(str(e))

        except Exception as e:
            self.st.error("[DEBUG] Exception - get_mail_content : " + str(e))
            # self.st.warning("No More Email")
            pass

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
