from modules.gmailapi import GmailApi
from modules.visualization_tool import VisualizationTool

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
        self.visualizationTool = VisualizationTool(self.st)

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


        with col1:
            # call get_list() with query
            self.st.subheader("▶︎ Email取得")

            # final query
            self.st.code("Query : " + self.query)

            # select fetch count
            self.fetching_count = int(self.st.number_input("最大取得件数 (上限1000)", min_value=1, max_value=1000))


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

            self.st.write("---")
            self.st.subheader("▶︎ " + str(i+1) + " 件目")


            ########################
            col11, col12, col13, col14, col15, col16, col17, col18, col19, col20 = self.st.columns((1,1,1,1,1,1,1,1,1,1))

            # moveMailToTrash
            with col11:
                if self.st.button("🗑", key="trash"):
                    self.st.write("ゴミ箱に移動しました。")

            # deleteMail
            with col12:
                if self.st.button("削除", key="delete"):
                    self.st.write("削除しました。")

            # markMailAsImportant
            with col13:
                if self.st.button("重要", key="important"):
                    self.st.write("重要なメールに指定しました。")

            # markMailAsStarred
            with col14:
                if self.st.button("⭐️", key="starred"):
                    self.st.write("星を付けました。")

            # markMailAsUnread
            with col15:
                if self.st.button("未読", key="unread"):
                    self.st.write("メールを未読に変更しました。")

            ########################
            # wordcloud
            col5, col6, col7 = self.st.columns((5,0.3,5))

            # wordcloud - mail_from
            with col5:
                self.st.write("---")
                self.st.write("● mail_from")
                self.visualizationTool.wordcloud(mail_from, 700)

            # wordcloud - mail_subject
            with col7:
                self.st.write("---")
                self.st.write("● mail_subject")
                self.visualizationTool.wordcloud(mail_subject, 700)

            # wordcloud - mail_snippet
            with col5:
                self.st.write("---")
                self.st.write("● mail_snippet")
                self.visualizationTool.wordcloud(mail_snippet, 700)

            # wordcloud - mail_body
            with col7:
                self.st.write("---")
                self.st.write("● mail_body")
                if ("http" not in mail_body) and ("</" not in mail_body):
                    input_text = mail_body
                else:
                    input_text = mail_body
                self.visualizationTool.wordcloud(input_text, 700)



            # text
            col1, col2 = self.st.columns((1,1))

            with col1:
                
                self.st.subheader("● mail_subject : \n"); self.st.error(mail_subject)
                self.st.subheader("● mail_date : \n"); self.st.code(mail_date)
                self.st.subheader("● mail_from : \n"); self.st.code(mail_from)
                self.st.subheader("● mail_to : \n"); self.st.code(mail_to)
                self.st.subheader("● mail_snippet : \n"); self.st.error(mail_snippet)

            with col2:
                if (("<html") in mail_body) and (("/html>") in mail_body) and (("<head") in mail_body) and (("/body>") in mail_body) and (("/body>") in mail_body) or ("<table" in mail_body) and ("/table>" in mail_body) or ("<div" in mail_body) and ("/div>" in mail_body):
                    self.st.subheader("● mail_body（HTML） : \n")
                    components.html(mail_body, height=4300)
                else:
                    self.st.subheader("● mail_body（TXT） : \n")
                    self.st.write(mail_body)


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

