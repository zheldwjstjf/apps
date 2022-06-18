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

class GmailFetchingResultSemiPage:
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
            fetching_count = result_count
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

            try:
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

                ########################

                # mail_subject
                self.st.subheader("[] " + mail_subject + " ]")

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

            except Exception as e:
                self.st.warning("No more Email")



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
