import datetime

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
                width: 480px;
            }
            [data-testid="stSidebar"][aria-expanded="false"] > div:first-child {
                width: 480px;
                margin-left: -480px;
            }
            </style>
            """,
            unsafe_allow_html=True,
        )

        # title
        load_time = datetime.datetime.now()
        self.st.sidebar.code(load_time)
        self.st.sidebar.markdown("<h1 style='text-align: center; color: red;'>[ S I D E - M E N U ]</h1>", unsafe_allow_html=True)        