import streamlit as st

class MyGmailApp:

    def __init__(self) -> None:
        """
        - method name : __init__
        - arg(s) : None
        """

    def main(self):
        """
        - method name : main
        - arg(s) : None
        """

        st.set_page_config( # Alternate names: setup_page, page, layout
            layout="wide",  # Can be "centered" or "wide". In the future also "dashboard", etc.
            initial_sidebar_state="collapsed",  # Can be "auto", "expanded", "collapsed"
            page_title="MyGmailApp",  # String or None. Strings get appended with "• Streamlit". 
            page_icon="resources/gmail_icon.icns")  # String, anything supported by st.image, or None.

myGmailApp = MyGmailApp()
myGmailApp.main()