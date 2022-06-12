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

        self.user = "me"

        # get query
        query_key_list = [
            "is"
        ]
        selected_query_key = self.st.st.selectbox("Select Query Key", query_key_list)

        query_val_list = [
            "unread"
        ]
        selected_query_val = self.st.st.selectbox("Select Query Value", query_key_list)

        self.query = selected_query_key + ":" + selected_query_val
        
        # call get_list
        self.get_list()

    def get_list(self):
        maillist = self.gmail_api.getMailList(self.user, self.query)
        self.result_count = maillist['resultSizeEstimate']
        self.st.write("取得条件 : " + self.query)
        self.st.write("取得件数 : " + str(self.result_count) + " 件")