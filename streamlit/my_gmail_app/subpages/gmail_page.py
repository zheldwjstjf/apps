from modules.gmailapi import GmailApi

import base64
from email.mime.audio import MIMEAudio
from email.mime.base import MIMEBase
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

import streamlit.components.v1 as components

class GmailPage:
    """
    - class name : MainPage
    """

    def __init__(self, streamlit, service) -> None:
        """
        - method name : __init__
        - arg(s) : streamlit
        """

        self.st = streamlit
        self.service = service
        self.gmail_api = GmailApi(self.st, self.service)

        self.query = ""

    def gmail_page(self):
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
            selected_query_keys = self.st.multiselect("主なQuery", query_key_list, key="main")

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

        with col1:
            # call get_list() with query
            self.st.subheader("▶︎ Email取得")

            # final query
            self.st.code("Query : " + self.query)

            # select fetch count
            self.fetching_count = int(self.st.number_input("最大取得件数 (上限100)", min_value=1, max_value=100))


        # with col1:
        if self.st.button("取得", key="get_list"):
            self.maillist = self.get_list()
        
            # get_mail_contents 
            self.get_mail_content(self.maillist)

    def get_priority_label(self):

        priority_label_list = [
            "High",
            "Medium",
            "Low"
        ]
        selected_priority = self.st.multiselect("Select Email", priority_label_list, key="priority")

        return selected_priority     

    def get_list(self):
        self.maillist = self.gmail_api.getMailList(self.user, self.query)
        self.result_count = len(self.maillist)
        self.st.write("取得件数 : " + str(self.result_count) + " 件")
        # self.st.write("[DEBUG] maillist : ", self.maillist)

        return self.maillist
    

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
        selected_query_is_val = self.st.selectbox("Select Query Value", query_is_val_list, key="is")
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


    def get_mail_content(self, maillist):

        if self.result_count > self.fetching_count:
            pass
        elif self.result_count > self.fetching_count:
            pass
        elif self.result_count < self.fetching_count:
            self.fetching_count == self.result_count
        else:
            self.result_count = 1

        
        # TODO
        # for loop 대신에, 
        # id / title만 먼저 가져와서 리스트 가져와서 -> 셀렉트 박스 만들어서
        # 셀렉트 박스에서 하나의 [id / title]를 선택하면 -> 스닛핏 또는 본문 볼 수 있게 하고
        #  스닛핏 또는 본문을 본다음에 -> 개요 정보 입력/업데이터 / 삭제 / 쓰레기토응로 / 본문내용 저장 등등 할수 있게 한다
          
        for i in range(self.fetching_count):

            self.mail_id = self.mail_id = maillist[i]['id']
            self.mail_content = self.gmail_api.getMailContent(self.user, self.mail_id)

            # - do mail as read
            self.gmail_api.markMailAsRead(self.user, self.mail_id)            

            mail = self.parse_mail()

            mail_subject = mail['subject']
            mail_date = mail['date']
            mail_from = mail['from']
            mail_to = mail['to']            
            mail_snippet = mail['snippet']
            mail_body = mail['body']

            for foo in range(5):
                self.st.write("---")
            self.st.write("▶︎ " + str(i+1) + " 件目")
            self.st.write("- mail_subject : \n", mail_subject)
            self.st.write("- mail_date : \n", mail_date)
            self.st.write("- mail_from : \n", mail_from)
            self.st.write("- mail_to : \n", mail_to)
            self.st.write("- mail_snippet : \n", mail_snippet)
            self.st.write("- mail_body : \n")
            self.st.write("---")
            if (("<html") in mail_body) and (("/html>") in mail_body) and (("<head") in mail_body) and (("/body>") in mail_body) and (("/body>") in mail_body):
                components.html(mail_body, height=2000)
            else:
                self.st.write(mail_body)
            self.st.write("---")


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

