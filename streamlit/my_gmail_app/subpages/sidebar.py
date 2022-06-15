import os
import time

class SidebarPage:
    """
    - class name : SidebarPage
    """

    def __init__(self, streamlit) -> None:
        """
        - method name : __init__
        - arg(s) : streamlit
        """

        self.st = streamlit

    def sidebar_page(self):
        """
        - method name : sidebar_page
        - arg(s) : None
        """

        self.st.markdown(
            """
            <style>
            [data-testid="stSidebar"][aria-expanded="true"] > div:first-child {
                width: 380px;
            }
            [data-testid="stSidebar"][aria-expanded="false"] > div:first-child {
                width: 380px;
                margin-left: -380px;
            }
            </style>
            """,
            unsafe_allow_html=True,
        )

        # title
        os.environ['TZ'] = 'Japan'
        time.tzset()
        t = time.localtime()
        current_time = time.strftime("%Y-%m-%d %H:%M:%S", t)


        self.st.sidebar.info("Updated at :  " + str(current_time))
        self.st.sidebar.info("[ TODO ] 認証した時刻")
        self.st.sidebar.info("[ TODO ] 認証切れた時刻")

        self.st.sidebar.markdown("<h1 style='text-align: center; color: red;'>[ S I D E - M E N U ]</h1>", unsafe_allow_html=True)        