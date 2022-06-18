from modules.gmailapi import GmailApi

import streamlit.components.v1 as components

class GmailFetchingPage:
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

    def get_list(self):
        self.maillist = self.gmail_api.getMailList(self.user, self.query)
        self.result_count = len(self.maillist)
        self.st.write("取得件数 : " + str(self.result_count) + " 件")
        # self.st.write("[DEBUG] maillist : ", self.maillist)

        return self.maillist
