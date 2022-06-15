from modules.gmailapi import GmailApi

import base64
from email.mime.audio import MIMEAudio
from email.mime.base import MIMEBase
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

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
        self.st.markdown("<h1 style='text-align: center; color: red;'>GMAIL Crawling Page</h1>", unsafe_allow_html=True)

        #
        self.maillist = self.get_list()

        # select email
        mail_list_uniq = self.craw_email_address(self.maillist)

        self.st.subheader("▶︎ Crawled Email")
        selected_email = self.st.selectbox("Select Email", mail_list_uniq, key="crawled_email_list")

        self.st.write("selected_email : ", selected_email)

    def get_list(self):
        self.maillist = self.gmail_api.getMailList(self.user, self.query)
        # self.st.write("[DEBUG] maillist : ", self.maillist)
        self.result_count = len(self.maillist)
        self.st.write("取得件数 : " + str(self.result_count) + " 件")

        return self.maillist

    def craw_email_address(self, maillist):

        mail_list = []

        if self.result_count > self.fetching_count:
            pass
        elif self.result_count > self.fetching_count:
            pass
        elif self.result_count < self.fetching_count:
            self.fetching_count == self.result_count
        else:
            self.result_count = 1
          
        for i in range(self.fetching_count):

            self.mail_id = self.mail_id = maillist[i]['id']
            self.mail_content = self.gmail_api.getMailContent(self.user, self.mail_id)

            mail = self.parse_mail()
            mail_from = mail['from']

            mail_list.append(mail_from)

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

