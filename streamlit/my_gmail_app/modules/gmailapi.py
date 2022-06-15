# -*- coding: utf-8 -*-
# https://console.developers.google.com/apis/library
# https://console.developers.google.com/apis/library/gmail.googleapis.com
# https://googleapis.github.io/google-api-python-client/docs/dyn/gmail_v1.users.html

import sys
from apiclient.discovery import build
import webbrowser
from oauth2client.client import OAuth2WebServerFlow
from oauth2client.file import Storage
# from oauth2client.tools import run
import httplib2
from apiclient import errors
from multiprocessing import Process, Value

import base64
from email.mime.audio import MIMEAudio
from email.mime.base import MIMEBase
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

class GmailApi():

    def __init__(self, streamlit, service):
        self.st = streamlit
        self.service = service

    def sendMessage(self, user, message):
        """メールを送信します。messageの作り方はcreateMesage関数を参照
            Keyword arguments:
            user -- meを指定する。
            message -- createMessageで生成したオブジェクトを渡す必要があります
            Returns: None
        """
        try:
            message = (self.service.users().messages().send(userId=user, body=message).execute())
            return message
        except errors.HttpError as error:
            print('An error occurred:s' % error)

    def getMailList(self, user, qu):
        ''' メールの情報をリストで取得します
          quの内容でフィルタリングする事が出来ます
           Keyword arguments:
           user -- me又はgoogleDevloperに登録されたアドレスを指定します。
           qu -- queryを設定します
                 例えばexample@gmail.comから送られてきた未読のメールの一覧を取得するには以下のように指定すればよい
                "from: example@gmail.com is:unread"
           Returns: メール情報の一覧　idとThreadIdをKeyとした辞書型のリストになる
             "messages": [
                  {
                   "id": "nnnnnnnnnnnn",
                   "threadId": "zzzzzzzzzzz"
                  },
                  {
                   "id": "aaaaaa",
                   "threadId": "bbbbbb"
                  },,,,
              }
        '''
        messages = []

        try:
            # self.st.write("[DEBUG] Query in getMailList method : ", qu)
            # return self.service.users().messages().list(userId=user, q=qu).execute()

            result = self.service.users().messages().list(userId='me',q=query).execute()
            if 'messages' in result:
                messages.extend(result['messages'])
            while 'nextPageToken' in result:
                page_token = result['nextPageToken']
                result = self.service.users().messages().list(userId='me',q=qu, pageToken=page_token).execute()
                if 'messages' in result:
                    messages.extend(result['messages'])
            return messages

        except errors.HttpError as error:
            print("error [ service.users().messages().list( ) ] : ", error)

    def getMailContent(self, user, i):
        """指定したメールのIDからメールの内容を取得します。
                Keyword arguments:
                user -- meを指定する。
                i -- メールのId getMailList()等を使用して取得したIdを使用する
                Returns: メールの内容を辞書型で取得する
                詳細は以下
                http://developers.google.com/apis-explorer/#p/gmail/v1/gmail.users.messages.get
        """
        try:
            return self.service.users().messages().get(userId=user, id=i).execute()
        except errors.HttpError as error:
            pass

    def archiveMail(self, user, i):
        """
        """
        query = {"removeLabelIds": ["INBOX"]} # Archive the email (skip the inbox)
        self.service.users().messages().modify(userId=user, id=i, body=query).execute()

    def markMailAsRead(self, user, i):
        """指定したメールのIDを既読にします
            Keyword arguments:
            user -- meを指定する。
            i -- メールのId getMailList()等を使用して取得したIdを使用する
            Returns:　なし
        """
        query = {"removeLabelIds": ["UNREAD"]} # Mark as read
        self.service.users().messages().modify(userId=user, id=i, body=query).execute()

    def markMailAsNotSpam(self, user, i):
        """
        """
        query = {"removeLabelIds": ["SPAM"]} # Never mark as spam
        self.service.users().messages().modify(userId=user, id=i, body=query).execute()

    def markMailAsImportant(self, user, i):
        """
        """
        query = {"addLabelIds": ["IMPORTANT"]} # Mark as important
        self.service.users().messages().modify(userId=user, id=i, body=query).execute()

    def _moveMailToTrash(self, user, i):
        """
        """
        query = {"addLabelIds": ["TRASH"]} # Delete the email
        self.service.users().messages().modify(userId=user, id=i, body=query).execute()

    def markMailAsStarred(self, user, i):
        """
        """
        query = {"addLabelIds": ["STARRED"]} # Mark as starred
        self.service.users().messages().modify(userId=user, id=i, body=query).execute()

    def markMailAsUserLabel(self, user, i):
        """
        """
        query = {"addLabelIds": ['<user label id>']} # Tag the mail with a user-defined label. Only one user-defined label is allowed per filter.
        self.service.users().messages().modify(userId=user, id=i, body=query).execute()

    def createFilter(self, user, i):
        """
        Creates a filter.
        https://developers.google.cn/gmail/api/guides/filter_settings?hl=zh-cn#examples
        """
        label_id = 'Label_14' # ID of user label to add
        filter = {
            'criteria': {
                'from': 'cat-enthusiasts@example.com'
            },
            'action': {
                'addLabelIds': [label_id],
                'removeLabelIds': ['INBOX']
            }
        }
        return self.service.users().settings().filters().create(userId='me', body=filter).execute() # WIP

    def deleteFilter(self, user, i):
        """
        Deletes a filter.
        """
        return self.service.users().settings().filters().get(userId=user, id=i).execute() # WIP

    def getFilter(self, user, i):
        """
        Gets a filter.
        """
        return self.service.users().settings().filters().get(userId=user, id=i).execute() # WIP

    def getFilterList(self, user, i):
        """
        Lists the message filters of a Gmail user.
        """
        return self.service.users().settings().filters().list(userId=user).execute()

    def moveMailToTrash(self, user, i):
        """Moves the specified message to the trash.
            Keyword arguments:
            user -- meを指定する。
            i -- メールのId getMailList()等を使用して取得したIdを使用する
            Returns:　If successful, the response body contains an instance of Message
            https://developers.google.com/gmail/api/reference/rest/v1/users.messages/trash
        """
        self.service.users().messages().trash(userId=user, id=i).execute()

    def deleteMail(self, user, i):
        """Moves the specified message to the trash.
            Keyword arguments:
            user -- meを指定する。
            i -- メールのId getMailList()等を使用して取得したIdを使用する
            Returns:　If successful, the response body contains an instance of Message
            https://developers.google.com/gmail/api/reference/rest/v1/users.messages/delete
        """
        self.service.users().messages().delete(userId=user, id=i).execute()

    def createMessage(self, sender, to, subject, message_text):
        """sendMessageで送信するメールを生成します
            Keyword arguments:
            sender -- meを指定する。
            to -- メールのId getMailList()等を使用して取得したIdを使用する
            subject -- 件名
            message_text --　メールの内容
            Returns:　なし
        """
        message = MIMEText(message_text)
        message['to'] = to
        message['from'] = sender
        message['subject'] = subject
        return {'raw': base64.urlsafe_b64encode(message.as_string())}

    def expMailContents(self, user, i, key):
        try:
            content = self.getMailContent(user, i)
            return ([header for header in content["payload"]["headers"] if header["name"] == key])[0]["value"]
        except errors.HttpError as error:
            pass

    def getMailFrom(self, user, i):
        try:
            return self.expMailContents(user, i, "From")
        except errors.HttpError as error:
            pass

    def getMailSubject(self, user, i):
        try:
            return self.expMailContents(user, i, "Subject")
        except errors.HttpError as error:
            pass

    def getLabelList(self, user):
        gmail_label_dict_list = []
        try:
            labelList = self.service.users().labels().list(userId=user).execute()
            # # print("[ DEBUG ] labelList : ", labelList)
            labels = labelList.get("labels")
            i = 1
            for label_dict in labels:
                gmail_label_dict_list.append(label_dict)
                # # print("[ DEBUG ] [ " + str(i) + " ] label name : ", label_dict['name'] )
                i = i + 1
            return gmail_label_dict_list
        except errors.HttpError as error:
            print("error : ", error)
            pass

    def createLabel(self, user, query):
        try:
            self.service.users().labels().create(userId=user, body=query).execute() # ok

        except errors.HttpError as error:
            print("error : ", error)
            pass

    def updateLabel(self, user):
        try:
            gmail_label_dict_list = self.getLabelList(user)
            i = 1
            for label_dict in gmail_label_dict_list:
                print("[ " + str(i) + " ] label id : " + label_dict['id'] + " / label name : " + label_dict['name'])
                i = i + 1
            # self.service.users().labels().update(body=query).execute() # 403 # user == account
        except errors.HttpError as error:
            print("error : ", error)
            pass
