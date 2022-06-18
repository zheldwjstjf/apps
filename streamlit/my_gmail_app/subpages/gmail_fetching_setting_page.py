import streamlit.components.v1 as components

class GmailFetchingSettingPage:
    """
    - class name : MainPage
    """

    def __init__(self, streamlit) -> None:
        """
        - method name : __init__
        - arg(s) : streamlit
        """

        self.st = streamlit
        self.query = ""

    def gmail_fetching_setting_page(self):
        """
        - method name : main_page
        - arg(s) : streamlit
        """

        self.user = "me"

        # get query
        self.st.subheader("▶︎ Query設定")

        query_key_list = [
                "is",
                "subject",
                "to",
                "has",
                "label",
                "after",
                "before",
                "older",
                "newer",
                "older_than",
                "newer_than"
            ]
        selected_query_keys = self.st.multiselect("主なQuery", query_key_list, default=query_key_list[0], key="main")

        if "is" in selected_query_keys:
            self.query_is = self.get_query_is()
            self.query = self.query + self.query_is + " "

        if "subject" in selected_query_keys:
            self.query_subject = self.get_query_subject()
            self.query = self.query + self.query_subject + " "

        if "older_than" in selected_query_keys:
            self.query_older_than = self.get_query_older_than()
            self.query = self.query + self.query_older_than + " "

        if "newer_than" in selected_query_keys:
            self.query_newer_than = self.get_query_newer_than()
            self.query = self.query + self.query_newer_than + " "

        # call get_list() with query
        self.st.subheader("▶︎ Email取得")

        # final query
        self.st.code("Query : " + self.query)

        # select fetch count
        self.fetching_count = int(self.st.number_input("最大取得件数 (上限1000)", min_value=1, max_value=1000))


    def get_priority_label(self):

        priority_label_list = [
            "High",
            "Medium",
            "Low"
        ]
        selected_priority = self.st.multiselect("Select Email", priority_label_list, key="priority")

        return selected_priority     
    
    def get_query_is(self):
        query_is_val_list = [
                "read",
                "unread",
                "starred",
                "snoozed",
            ]
        selected_query_is_val = self.st.selectbox("Select Query Value", query_is_val_list, index=1, key="is")
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


    def get_query_older_than(self):
        query_older_than_val_list = [
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
        selected_query_older_than_val = self.st.selectbox("Select Query Value", query_older_than_val_list, key="older_than")
        self.query_older_than = "older_than:" + selected_query_older_than_val

        return self.query_older_than
