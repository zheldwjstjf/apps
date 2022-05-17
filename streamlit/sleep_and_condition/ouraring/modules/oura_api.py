class OuraApi:
    """
    - class name : OuraApi
    """

    def __init__(self, streamlit) -> None:
        """
        - method name : __init__
        - arg(s) : streamlit
        """

        self.st = streamlit

    def getSleepData(client, start_date, end_date):
        """
        - method name : getSleepData
        - arg(s) : client, start_date, end_date
        """
        
        sleep = client.sleep_summary(str(start_date), str(end_date))
        # self.st.write("sleep : ", sleep)

        return sleep
