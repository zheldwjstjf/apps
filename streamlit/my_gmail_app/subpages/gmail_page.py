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

        self.query = ""

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
                "is",
                "from"
            ]
        selected_query_keys = self.st.multiselect("Select Query Keys", query_key_list)

        if "is" in selected_query_keys:
            self.query_is = self.get_query_is()
            self.query = self.query + self.query_is

        if "from" in selected_query_keys:
            self.query_is = self.get_query_is()
            self.query = self.query + self.query_is

        if self.st.button("取得", key=1):
            # call get_list
            self.get_list()

    def get_list(self):
        maillist = self.gmail_api.getMailList(self.user, self.query)
        self.result_count = len(maillist["messages"])
        self.st.write("取得条件 : " + self.query_is)
        self.st.write("取得件数 : " + str(self.result_count) + " 件")
        self.st.write("[DEBUG] maillist : ", maillist)        

    def get_query_is(self):
        col1, col2 = self.st.columns((1,1))

        query_is_val_list = [
                "read",
                "unread",
                "starred",
                "snoozed",
            ]
        selected_query_is_val = col1.selectbox("Select Query Value", query_is_val_list)
        self.query_is = "is:" + selected_query_is_val
        col2.code("Selected : " + self.query_is)

        return self.query_is