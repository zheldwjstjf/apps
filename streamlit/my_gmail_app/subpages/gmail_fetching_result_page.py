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

class GmailFetchingResultPage:
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

        self.mail_id = None

    def get_mail_content(self, maillist, fetching_count, result_count, service, user):

        self.gmail_api = GmailApi(self.st, service)

        if result_count > fetching_count:
            pass
        elif result_count < fetching_count:
            fetching_count == result_count
        elif result_count == 0:
            fetching_count = 0
        else:
            fetching_count = 1

        
        # TODO
        # for loop 대신에, 
        # id / title만 먼저 가져와서 리스트 가져와서 -> 셀렉트 박스 만들어서
        # 셀렉트 박스에서 하나의 [id / title]를 선택하면 -> 스닛핏 또는 본문 볼 수 있게 하고
        #  스닛핏 또는 본문을 본다음에 -> 개요 정보 입력/업데이터 / 삭제 / 쓰레기토응로 / 본문내용 저장 등등 할수 있게 한다
          
        for i in range(fetching_count):

            self.mail_id = self.mail_id = maillist[i]['id']
            self.mail_content = self.gmail_api.getMailContent(user, self.mail_id)

            # - do mail as read
            self.gmail_api.markMailAsRead(user, self.mail_id)            

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
            
            # getFilterList
            filter_dict = self.gmail_api.getFilterList(user, self.mail_id)
            # self.st.info("[DEBUG] filter_dict : " + str(filter_dict))
            
            try:
                email_address = mail_from.split("@")[1]
                email_address = email_address.replace(">", "")
            except Exception as e:
                self.st.error("email_address - Exception : " + str(e))
                email_address = "email_address - Exception"
            # self.st.info("[DEBUG] email_address : " + email_address)

            if email_address in str(filter_dict):
                filter_list = filter_dict["filter"]

                for filter in filter_list:
                    if email_address in str(filter):
                        filtered_email = filter.get("criteria")
                        filter_action = filter.get("action")
                        self.st.info("Filter : " + str(filtered_email) + " : " + str(filter_action))
            else:
                self.st.info("No Filter")

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