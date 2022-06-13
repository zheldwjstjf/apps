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

        # select email
        self.st.subheader("▶︎ Select Email")
        self.query_froms = self.get_query_from()
        self.query = self.query + self.query_from + " "


        col1, col2 = self.st.columns((1,1))

        # get query

        with col1:
            self.st.subheader("▶︎ Main Query設定")

            query_key_list = [
                    "is",
                    "ppp"
                ]
            selected_query_keys = self.st.multiselect("Select Query Keys", query_key_list, key="main")

            if "is" in selected_query_keys:
                self.query_is = self.get_query_is()
                self.query = self.query + self.query_is + " "

            # final query
            self.st.code("Query : " + self.query)

            # call get_list() with query
            self.st.subheader("▶︎ Email取得")
            if self.st.button("取得", key="main"):
                self.get_list()

        with col2:
            self.st.subheader("▶︎ Sub Query設定")

            query_key_list = [
                    "is",
                    "ppp"
                ]
            selected_query_keys = self.st.multiselect("Select Query Keys", query_key_list, key="sub")

            if "is" in selected_query_keys:
                self.query_is = self.get_query_is()
                self.query = self.query + self.query_is + " "

            # final query
            self.st.code("Query : " + self.query)

            # call get_list() with query
            self.st.subheader("▶︎ Email取得")
            if self.st.button("取得", key="sub"):
                self.get_list()


    def get_list(self):
        maillist = self.gmail_api.getMailList(self.user, self.query)
        self.result_count = len(maillist["messages"])
        self.st.write("取得件数 : " + str(self.result_count) + " 件")
        self.st.write("[DEBUG] maillist : ", maillist)        

    def get_query_from(self):
        
        #
        col1, col2 = self.st.columns((1,1))

        query_from_val_list = [
                "editor1@kdnuggets.com",
                "weekly@raspberrypi.com",
                "noreply@medium.com",
                "no-reply@m.ouraring.com",
            ]
        selected_query_from_val = col1.selectbox("Select Email", query_from_val_list, key="from")
        self.query_from = "from:" + selected_query_from_val

        selected_email_info_list = [
            "概要",
            "Email",
            "Site",
        ]        
        self.query_from = "from:" + selected_query_from_val

        selected_info_itme = col2.selectbox("Select Email Info Item", selected_email_info_list, key="email_info")

        # 
        col1, col2 = self.st.columns((1,1))
        col2.write("INFO : " + str(selected_info_itme))
        col2.code(selected_info_itme)

        return self.query_from

    def get_query_is(self):
        col1, col2 = self.st.columns((1,1))

        query_is_val_list = [
                "read",
                "unread",
                "starred",
                "snoozed",
            ]
        selected_query_is_val = col1.selectbox("Select Query Value", query_is_val_list, key="is")
        self.query_is = "is:" + selected_query_is_val
        col2.code("Selected : " + selected_query_is_val)

        return self.query_is


