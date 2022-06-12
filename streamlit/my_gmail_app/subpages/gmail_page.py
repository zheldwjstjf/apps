from modules.gmailapi import GmailApi

class GmailPage:
    """
    - class name : MainPage
    """

    def __init__(self, streamlit, gmail_auth) -> None:
        """
        - method name : __init__
        - arg(s) : streamlit
        """

        self.st = streamlit
        self.gmail_auth = gmail_auth
        self.gmail_api = GmailApi(self.gmail_auth)

    def gmail_page(self):
        """
        - method name : main_page
        - arg(s) : streamlit
        """

        # title
        self.st.markdown("<h1 style='text-align: center; color: red;'>MY GMAIL APP</h1>", unsafe_allow_html=True)

        user = "me"
        query = "is:unread"

        maillist = self.gmail_api.getMailList(user, query)
        self.result_count = maillist['resultSizeEstimate']
        self.st.write("取得条件 : " + query)
        self.st.write("取得件数 : " + str(self.result_count) + " 件")