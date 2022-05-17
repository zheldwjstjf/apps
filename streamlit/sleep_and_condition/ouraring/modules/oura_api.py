from datetime import datetime

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

    def getSleepData(self, client, start_date, end_date):
        """
        - method name : getSleepData
        - arg(s) : client, start_date, end_date
        """

        if start_date != None:
            pass
        else:
            start_date = datetime(2021, 7, 2)        

        if end_date != None:
            pass
        else:
            end_date = datetime.today()

        self.sleep = client.sleep_summary(str(start_date), str(end_date))
        # self.st.write("sleep : ", sleep)

        return self.sleep
