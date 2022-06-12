from modules.gmailapi import GmailApi

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

    def gmail_page(self):
        """
        - method name : main_page
        - arg(s) : streamlit
        """

        # title
        self.st.markdown("<h1 style='text-align: center; color: red;'>MY GMAIL APP</h1>", unsafe_allow_html=True)

        self.user = "me"

        # get query
        query_is_key_list = [
                "is"
            ]
        selected_query_is_key = self.st.selectbox("Select Query Key", query_is_key_list)

        if selected_query_is_key == "is":
            query_is_val_list = [
                    "read",
                    "unread"
                ]
            selected_query_is_val = self.st.selectbox("Select Query Value", query_is_val_list)

            self.query_is = selected_query_is_key + ":" + selected_query_is_val
        
        self.query = self.query_is

        if self.st.button("更新", key=1):
        
            # call get_list
            self.get_list()

    def get_list(self):
        maillist = self.gmail_api.getMailList(self.user, self.query)
        self.result_count = len(maillist)
        self.st.write("取得条件 : " + self.query)
        self.st.write("取得件数 : " + str(self.result_count) + " 件")