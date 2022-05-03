import pandas as pd
import base64
import requests
import json
from io import StringIO


class CSVTool:
    def __init__(self, streamlit):
        self.st = streamlit
    
    def load_data(self):
        """
        load spreadsheet with data to be annotated
        """

        url = "https://api.github.com/repos/zheldwjstjf/apps/contents/streamlit/utilitycosts/data/utility_costs.csv"
        # url = "https://api.github.com/repos/zheldwjstjf/apps/contents/streamlit/test/data/utility_costs.csv"

        req = requests.get(url)
        
        self.st.error(req.status_code)
        
        if req.status_code == requests.codes.ok:
            req = req.json()  # the response is a JSON
            # req is now a dict with keys: name, encoding, url, size ...
            # and content. But it is encoded with base64.
            try:
                content = base64.b64decode(req['content'])
            except Exception as e:
                print("Exception - load-data : ", e)
            # self.st.write(content)

            content = content.decode('utf-8')
            csvDATA = StringIO(str(content))
            df = pd.read_csv(csvDATA)

            return df
        else:
            self.st.warning('クラウドデータの取得ができませんでした。ローカルデータを取得します。')

            df = pd.read_csv("data/utility_costs.csv")
            return df


    def save_input(self, df, row, amount, selected_date):
        """
        save input
        """
        df.at[row, selected_date] = amount
        df.to_csv("data/utility_costs.csv", index=None)
        
        return None