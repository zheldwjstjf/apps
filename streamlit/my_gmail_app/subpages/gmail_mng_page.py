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

        col11, col12, col13, col14, col15, col16, col17, col18, col19, col20 = self.st.columns((1,1,1,1,1,2,2,2,2,2))

        # moveMailToTrash
        with col11:
            if self.st.button("🗑", key="trash"): # _" + self.mail_id):
                self.st.write("ゴミ箱に移動しました。1" + str(datetime.now()))
                self.st.write("ゴミ箱に移動しました。2" + str(datetime.now()))

        # deleteMail
        with col12:
            if self.st.button("削除", key="delete"):
                self.st.write("削除しました。")

        # markMailAsImportant
        with col13:
            if self.st.button("重要", key="important_" + self.mail_id):
                self.st.write("重要なメールに指定しました。")

        # markMailAsStarred
        with col14:
            if self.st.button("⭐️", key="starred_" + self.mail_id):
                self.st.write("星を付けました。")

        # markMailAsUnread
        with col15:
            if self.st.button("未読", key="unread_" + self.mail_id):
                self.st.write("メールを未読に変更しました。")
