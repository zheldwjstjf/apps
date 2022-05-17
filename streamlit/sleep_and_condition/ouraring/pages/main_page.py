import json
import pandas as pd

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

    def main_page(self, sleep, start_date, end_date, options1, options2, options3):

        if (start_date!=None) and (end_date!=None):

            sleep = sleep["sleep"]
            sleep_str = str(sleep)
            sleep_str = sleep_str.replace("'", '"')

            df = pd.read_json(sleep_str)

            col1, col2, col3 = self.st.columns((1,1,1))

            chart_data = pd.DataFrame(df, columns=options1)
            self.st.line_chart(chart_data)

            chart_data = pd.DataFrame(df, columns=options2)
            self.st.line_chart(chart_data)

            chart_data = pd.DataFrame(df, columns=options3)
            self.st.line_chart(chart_data)
