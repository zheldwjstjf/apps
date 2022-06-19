from datetime import datetime
import time

from modules.gmailapi import GmailApi

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

    def gmail_mng_page(self, service, user, mail_id):
        """
        - method name : tmpPage
        - arg(s) : None
        """

        self.gmail_api = GmailApi(self.st, service)

        self.user = user
        self.mail_id = str(mail_id)
        # self.st.write("● mail_id : ", self.mail_id)
        
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

        col1, col2, col3, col4 = self.st.columns((1,1,1,1))
        col5, col6, col7, col8 = self.st.columns((1,1,1,1))

        ########################## 1st line
        # markMailAsRead
        if col4.button("📬", help="Mark mail as READ", key="read" + self.mail_id):
            try:
                self.gmail_api.markMailAsRead(user, self.mail_id)
                # self.st.balloons()
                self.st.write("メールを既読にしました。")
                time.sleep(0.3); self.st.experimental_rerun()
            except Exception as e:
                self.st.write("メールを既読にできませんでした。")
                self.st.error("" + str(e))

        # markMailAsImportant
        if col2.button("🚩", help="Mark mail as IMPORTANT", key="important_" + self.mail_id):
            try:
                self.gmail_api.markMailAsImportant(user, self.mail_id)
                # self.st.balloons()
                self.st.write("重要なメールと指定しました。")
                time.sleep(0.3); self.st.experimental_rerun()
            except Exception as e:
                self.st.write("重要なメールと指定しました。")
                self.st.error("" + str(e))

        # markMailAsStarred
        if col3.button("⭐️", help="Mark mail as STARRED", key="starred_" + self.mail_id):
            try:
                self.gmail_api.markMailAsStarred(user, self.mail_id)
                # self.st.balloons()
                self.st.write("星を付けました。")
                time.sleep(0.3); self.st.experimental_rerun()
            except Exception as e:
                self.st.write("星が付けられませんでした。")
                self.st.error("" + str(e))

        # markMailAsUnread
        if col1.button("📪", help="Mark mail as UNREAD", key="unread_" + self.mail_id):
            try:
                self.gmail_api.markMailAsUnread(user, self.mail_id)
                # self.st.balloons()
                self.st.write("メールを未読にしました。")
                time.sleep(0.3); self.st.experimental_rerun()
            except Exception as e:
                self.st.write("メールを未読にできませんでした。")
                self.st.error("" + str(e))

        ########################## 2nd line
        # moveMailToTrash
        if col8.button("🗑", help="Move mail to TRASH", key="trash" + self.mail_id):
            try:
                self.gmail_api.moveMailToTrash(user, self.mail_id)
                # self.st.balloons()
                self.st.write("ゴミ箱に移動しました。")
                time.sleep(0.3); self.st.experimental_rerun()
            except Exception as e:
                self.st.write("ゴミ箱に移動できませんでした。")
                self.st.error("" + str(e))

        # deleteMail
        if col7.button("🧨", help="DELETE mail",  key="delete_" + self.mail_id):
            try:
                self.gmail_api.deleteMail(user, self.mail_id)
                # self.st.balloons()
                self.st.write("メールを削除しました。")
                time.sleep(0.3); self.st.experimental_rerun()
            except Exception as e:
                self.st.write("メールを削除できませんでした。")
                self.st.error("" + str(e))

        # markMailAsSpam
        if col6.button("⛔", help="Mark mail as SPAM",  key="spam_" + self.mail_id):
            try:
                self.gmail_api.markMailAsSpam(user, self.mail_id)
                # self.st.balloons()
                self.st.write("SPAMメールに指定しました。")
                time.sleep(0.3); self.st.experimental_rerun()
            except Exception as e:
                self.st.write("メールを削除できませんでした。")
                self.st.error("" + str(e))

        # markMailAsNotSpam
        if col5.button("🔙", help="Mark mail as not SPAM",  key="not_spam_" + self.mail_id):
            try:
                self.gmail_api.markMailAsNotSpam(user, self.mail_id)
                # self.st.balloons()
                self.st.write("SPAMメールの指定を解除しました。")
                time.sleep(0.3); self.st.experimental_rerun()
            except Exception as e:
                self.st.write("メールを削除できませんでした。")
                self.st.error("" + str(e))


    def gmail_mng_batch(self, service, user, maillist):
        """
        - method name : tmpPage
        - arg(s) : None
        """

        self.gmail_api = GmailApi(self.st, service)

        self.user = user
        self.maillist = maillist
        # self.st.write("● mail_id : ", self.mail_id)

        gmail_mng_batch_progress_bar = self.st.progress(0)

        col1, col2, col3, col4 = self.st.columns((1,1,1,1))
        col5, col6, col7, col8 = self.st.columns((1,1,1,1))

        ########################## 1st line
        # markMailAsRead
        if col4.button("📬", help="Mark mail as READ", key="read_"):
            try:
                self.gmail_api.markMailAsRead(user, self.mail_id)
                # self.st.balloons()
                self.st.write("メールを既読にしました。")
                time.sleep(0.3); self.st.experimental_rerun()
            except Exception as e:
                self.st.write("メールを既読にできませんでした。")
                self.st.error("" + str(e))

        # markMailAsImportant
        if col2.button("🚩", help="Mark mail as IMPORTANT", key="important_"):
            try:
                self.gmail_api.markMailAsImportant(user, self.mail_id)
                # self.st.balloons()
                self.st.write("重要なメールと指定しました。")
                time.sleep(0.3); self.st.experimental_rerun()
            except Exception as e:
                self.st.write("重要なメールと指定しました。")
                self.st.error("" + str(e))

        # markMailAsStarred
        if col3.button("⭐️", help="Mark mail as STARRED", key="starred_"):
            try:
                self.gmail_api.markMailAsStarred(user, self.mail_id)
                # self.st.balloons()
                self.st.write("星を付けました。")
                time.sleep(0.3); self.st.experimental_rerun()
            except Exception as e:
                self.st.write("星が付けられませんでした。")
                self.st.error("" + str(e))

        # markMailAsUnread
        if col1.button("📪", help="Mark mail as UNREAD", key="unread_"):
            try:
                self.gmail_api.markMailAsUnread(user, self.mail_id)
                # self.st.balloons()
                self.st.write("メールを未読にしました。")
                time.sleep(0.3); self.st.experimental_rerun()
            except Exception as e:
                self.st.write("メールを未読にできませんでした。")
                self.st.error("" + str(e))

        ########################## 2nd line
        # moveMailToTrash
        if col8.button("🗑", help="Move mail to TRASH", key="trash_"):
            try:
                count = 0
                for mail_id_thread in self.maillist:
                    self.gmail_api.moveMailToTrash(user, mail_id_thread["id"])
                    time.sleep(0.3)
                    count = count + 1
                    gmail_mng_batch_progress_bar.progress(count/len(self.maillist))
                time.sleep(0.3); self.st.balloons()
                self.st.write("ゴミ箱に移動しました。")
                self.st.experimental_rerun()
            except Exception as e:
                self.st.write("ゴミ箱に移動できませんでした。")
                self.st.error("" + str(e))

        # deleteMail
        if col7.button("🧨", help="DELETE mail",  key="delete_"):
            try:
                self.gmail_api.deleteMail(user, self.mail_id)
                # self.st.balloons()
                self.st.write("メールを削除しました。")
                time.sleep(0.3); self.st.experimental_rerun()
            except Exception as e:
                self.st.write("メールを削除できませんでした。")
                self.st.error("" + str(e))

        # markMailAsSpam
        if col6.button("⛔", help="Mark mail as SPAM",  key="spam_"):
            try:
                self.gmail_api.markMailAsSpam(user, self.mail_id)
                # self.st.balloons()
                self.st.write("SPAMメールに指定しました。")
                time.sleep(0.3); self.st.experimental_rerun()
            except Exception as e:
                self.st.write("メールを削除できませんでした。")
                self.st.error("" + str(e))

        # markMailAsNotSpam
        if col5.button("🔙", help="Mark mail as not SPAM",  key="not_spam_"):
            try:
                self.gmail_api.markMailAsNotSpam(user, self.mail_id)
                # self.st.balloons()
                self.st.write("SPAMメールの指定を解除しました。")
                time.sleep(0.3); self.st.experimental_rerun()
            except Exception as e:
                self.st.write("メールを削除できませんでした。")
                self.st.error("" + str(e))