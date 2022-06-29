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

        self.maillist = None
        self.result_count = None

    def get_list(self, user, query):
        if True: # self.st.button("取得", key="get_list"):
            self.maillist = self.gmail_api.getMailList(user, query)

            if self.maillist != None:
                self.result_count = len(self.maillist)
            else:
                self.result_count = 0
            self.st.write("Match 件数 : " + str(self.result_count) + " 件")
            # self.st.write("[DEBUG] maillist : ", self.maillist)

            return self.maillist