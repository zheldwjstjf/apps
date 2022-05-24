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

        # title
        self.st.markdown("<h2 style='text-align: center; color: red;'>[ SIDE BAR ]</h2>", unsafe_allow_html=True)        