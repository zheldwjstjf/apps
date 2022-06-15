from shutil import ExecError
import time
import base64
from email.mime.audio import MIMEAudio
from email.mime.base import MIMEBase
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import streamlit as st

from modules.gmailapi import GmailApi

class GmailCrawlingPage:
    """
    - class name : GmailCrawlingPage
    """

    def __init__(self, streamlit, service) -> None:
        """
        - method name : __init__
        - arg(s) : streamlit
        """

        self.st = streamlit
        self.service = service
        self.gmail_api = GmailApi(self.st, self.service)

        self.user = "me"
        self.query = "is:read"
        self.fetching_count = 100

    def gmail_crawling_page(self):
        """
        - method name : main_page
        - arg(s) : streamlit
        """

        # title
        self.st.markdown("<h1 style='text-align: center; color: red;'>Gmail Crawling Page</h1>", unsafe_allow_html=True)

        self.st.subheader("▶︎ Set Email Adress Crawling Count")
        self.fetching_count = int(self.st.number_input("", min_value=1))

        if self.st.button("取得", key="get_list"):

            # すでに読んでるメールを取得
            maillist = self.get_list()
            self.st.subheader("▶︎ Crawled Email Count")
            self.result_count = len(self.maillist)
            self.st.write("取得したメールの件数 : " + str(self.result_count) + " 件")

            # ユニークなメールアドレスを取得
            mail_list_uniq = self.craw_email_address(maillist, self.result_count)

            # 取得したユニークなメールアドレスの件数
            self.st.subheader("▶︎ Crawled Email Address Count")
            uniq_mail_count = len(mail_list_uniq)
            self.st.write("取得したメールアドレスの件数 : " + str(uniq_mail_count) + " 件")

            # 取得したユニークなメールアドレス
            self.st.subheader("▶︎ Crawled Email Address")
            count = 0
            for email_address in mail_list_uniq:
                self.st.write("[ " + str(count+1) + " ] " + email_address)
                count = count + 1

    def get_list(self):
        self.maillist = self.gmail_api.getMailList(self.user, self.query)

        return self.maillist

    def craw_email_address(self, maillist, result_count):

        self.result_count = result_count

        mail_list = []

        if self.result_count > self.fetching_count:
            pass
        elif self.result_count == self.fetching_count:
            pass
        elif self.result_count < self.fetching_count:
            self.fetching_count = self.result_count
        else:
            self.result_count = 1
          
        self.st.subheader("▶︎ Email Crawling Progress")
        craw_email_address_progress_bar = self.st.progress(0)
        
        for i in range(self.fetching_count):

            # time.sleep(0.1)

            try:
                self.mail_id = self.mail_id = maillist[i]['id']
                self.mail_content = self.gmail_api.getMailContent(self.user, self.mail_id)

                mail = self.parse_mail()
                mail_from = mail['from']

                if mail_from not in mail_list:
                    mail_list.append(mail_from)

            except Exception as e:
                pass

            craw_email_address_progress_bar.progress((i+1)/self.fetching_count)

        mail_list_uniq = list(set(mail_list))

        return mail_list_uniq

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
