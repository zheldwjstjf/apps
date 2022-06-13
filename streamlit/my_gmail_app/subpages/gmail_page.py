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

        # select priority label
        col1, col2 = self.st.columns((1,1))
        with col1:
            self.st.subheader("▶︎ Select Priority Label")
            self.priority_label = self.get_priority_label()

        # select email
        self.st.subheader("▶︎ Select Email")
        self.query_froms = self.get_query_from(self.priority_label)
        self.query = self.query + self.query_from + " "

        # get query
        self.st.subheader("▶︎ Query設定")

        col1, col2 = self.st.columns((1,1))

        with col1:
            query_key_list = [
                    "is",
                    "subject",
                    "to",
                    "has",
                    "label"
                ]
            selected_query_keys = self.st.multiselect("主なQuery", query_key_list, key="main")

            if "is" in selected_query_keys:
                self.query_is = self.get_query_is()
                self.query = self.query + self.query_is + " "

            if "subject" in selected_query_keys:
                self.query_subject = self.get_query_subject()
                self.query = self.query + self.query_subject + " "

        with col2:
            query_key_list = [
                    "after",
                    "before",
                    "older",
                    "newer",
                    "older_than",
                    "newer_than"
                ]
            selected_query_keys = self.st.multiselect("その他のQuery", query_key_list, key="sub")

            if "newer_than" in selected_query_keys:
                self.query_newer_than = self.get_query_newer_than()
                self.query = self.query + self.query_newer_than + " "

        with col1:

            # call get_list() with query
            self.st.subheader("▶︎ Email取得")

            # final query
            self.st.code("Query : " + self.query)

            if self.st.button("取得", key="get_list"):
                self.get_list()


    def get_priority_label(self):
        priority_label_list = [
            "High",
            "Medium",
            "Low"
        ]
        selected_priority = self.st.multiselect("Select Email", priority_label_list, key="priority")

        return selected_priority     


    def get_list(self):
        maillist = self.gmail_api.getMailList(self.user, self.query)
        self.result_count = len(maillist["messages"])
        self.st.write("取得件数 : " + str(self.result_count) + " 件")
        self.st.write("[DEBUG] maillist : ", maillist)        

    def get_query_from(self, priority_label):

        email_list = []

        self.priority_label = priority_label
        
        #
        col1, col2 = self.st.columns((1,1))

        if self.priority_label == "High":
            email_list_high = [
                    "All High priority email",
                    "editor1@kdnuggets.com",
                    "weekly@raspberrypi.com",
                    "noreply@medium.com",
                    "no-reply@m.ouraring.com",
                ]
            
            email_list = email_list + email_list_high

        if self.priority_label == "High":
            email_list_medium = [
                    "All Medium priority email",
                    "change@f.change.org",
                    "no-reply@sender.skyscanner.com",
                ]
            
            email_list = email_list + email_list_medium

        if self.priority_label == "High":
            email_list_low = [
                    "All Low priority email",
                    "reminders@facebookmail.com",
                    "noreply@uber.com",
                ]
            
            email_list = email_list + email_list_low

        selected_query_from_val = col1.selectbox("Select Email", email_list, key="from")
        if "@" not in selected_query_from_val:
            selected_query_from_val = ""
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
        query_is_val_list = [
                "read",
                "unread",
                "starred",
                "snoozed",
            ]
        selected_query_is_val = self.st.selectbox("Select Query Value", query_is_val_list, key="is")
        self.query_is = "is:" + selected_query_is_val

        return self.query_is

    def get_query_subject(self):
        selected_query_subject_val = self.st.text_input("", placeholder="ここに入力")
        self.query_subject = "subject:" + selected_query_subject_val

        return self.query_subject

    def get_query_newer_than(self):
        query_newer_than_val_list = [
                "1d",
                "2d",
                "3d",
                "4d",
                "5d",
                "6d",
                "7d",
                "10d",
                "15d",
                "20d",
                "1m",
                "2m",
                "3m",
                "4m",
                "5m",
                "6m",
                "7m",
                "8m",
                "9m",
                "10m",
                "11m",
                "1y",
                "2y",
                "3y",
                "4y",
                "5y",
            ]
        selected_query_newer_than_val = self.st.selectbox("Select Query Value", query_newer_than_val_list, key="newer_than")
        self.query_newer_than = "newer_than:" + selected_query_newer_than_val

        return self.query_newer_than

