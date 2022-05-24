class MainPage:
    """
    - class name : MainPage
    """

    def __init__(self, streamlit) -> None:
        """
        - method name : __init__
        - arg(s) : streamlit
        """

        self.st = streamlit

    def main_page(self):

        self.st.markdown("<h1 style='text-align: center; color: red;'>MY GMAIL APPs</h1>", unsafe_allow_html=True)