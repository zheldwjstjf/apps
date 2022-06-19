from datetime import datetime

class GmailMngPage:
    """
    - class name : TmpPage
    """

    def __init__(self, streamlit) -> None:
        """
        - method name : __init__
        - arg(s) : streamlit
        """

        self.st = streamlit

    def gmail_mng_page(self, mail_id):
        """
        - method name : tmpPage
        - arg(s) : None
        """

        self.mail_id = str(mail_id)
        self.st.write("mail_id : ", self.mail_id)

        
        # getFilterList
        """
        filter_dict = self.gmail_api.getFilterList(user, self.mail_id)
        # self.st.info("[DEBUG] filter_dict : " + str(filter_dict))
        
        try:
            email_address = mail_from.split("@")[1]
            email_address = email_address.replace(">", "")
        except Exception as e:
            self.st.error("email_address - Exception : " + str(e))
            email_address = "email_address - Exception"
        # self.st.info("[DEBUG] email_address : " + email_address)

        if email_address in str(filter_dict):
            filter_list = filter_dict["filter"]

            for filter in filter_list:
                if email_address in str(filter):
                    filtered_email = filter.get("criteria")
                    filter_action = filter.get("action")
                    self.st.info("Filter : " + str(filtered_email) + " : " + str(filter_action))
        else:
            self.st.info("No Filter")
        """

        col11, col12, col13, col14, col15 = self.st.columns((1,1,1,1,1))

        # moveMailToTrash
        if col11.button("🗑", key="trash" + self.mail_id):
            self.st.write("ゴミ箱に移動しました。")

        # deleteMail
        if col12.button("削除", key="delete_" + self.mail_id):
            self.st.write("削除しました。")

        # markMailAsImportant
        if col13.button("重要", key="important_" + self.mail_id):
            self.st.write("重要なメールに指定しました。")

        # markMailAsStarred
        if col14.button("⭐️", key="starred_" + self.mail_id):
            self.st.write("星を付けました。")

        # markMailAsUnread
        if col15.button("未読", key="unread_" + self.mail_id):
            self.st.write("メールを未読に変更しました。")
