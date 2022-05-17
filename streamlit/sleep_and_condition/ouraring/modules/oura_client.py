import os
from oura import OuraClient

class OuraClient:
    """
    - class name : OuraClient
    """

    def __init__(self, streamlit) -> None:
        """
        - method name : __init__
        - arg(s) : streamlit
        """
        
        self.st = streamlit

    def getOuraClient(self, user):
        """
        - method name : getOuraClient
        - arg(s) : user
        """

        if user == "jack":
            client_id = self.st.secrets["client_id_jack"]
            client_secret = self.st.secrets["client_secret_jack"]
            access_token = self.st.secrets["access_token_jack"]
            refresh_token = self.st.secrets["refresh_token_jack"]
        if user == "rieko":
            client_id = self.st.secrets["client_id_rieko"]
            client_secret = self.st.secrets["client_secret_rieko"]
            access_token = self.st.secrets["access_token_rieko"]
            refresh_token = self.st.secrets["refresh_token_rieko"]

        self.client = OuraClient(
            client_id=client_id,
            client_secret=client_secret,
            access_token=access_token,
            refresh_token=refresh_token,
        )

        return self.client

