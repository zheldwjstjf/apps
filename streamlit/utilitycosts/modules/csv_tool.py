import pandas as pd
import base64
import requests
import json
from io import StringIO


class CSVTool:
    def __init__(self, streamlit):
        self.st = streamlit

        self.url = "https://api.github.com/repos/zheldwjstjf/apps/contents/streamlit/utilitycosts/data/utility_costs.csv"
    
    def load_data(self):
        """
        load spreadsheet with data to be annotated
        """

        try:
            df = pd.read_csv("data/utility_costs.csv")
            self.st.warning('ローカルデータを取得しました。')

            return df
        except Exception as e:
            self.st.warning('クラウドデータを取得します。')

            req = requests.get(self.url)
            # self.st.error(req.status_code)
            
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

                self.st.warning('クラウドデータを取得しました。')

                return df
            else:
                self.st.warning('クラウドデータの取得ができませんでした。しばらく待って再度お試しください。')


    def save_input(self, df, row, amount, selected_date):
        """
        save input
        """
        try:
            df = pd.read_csv("data/utility_costs.csv")
            df.at[row, selected_date] = amount
            df.to_csv("data/utility_costs.csv", index=None)

            self.st.warning('ローカルデータを変更しました。')

        except Exception as e:
            print("Exception - save input : ", e)
            # TODO
            # df => StringIO => content => push to github
            # https://gist.github.com/avullo/b8153522f015a8b908072833b95c3408
            
            self.st.warning("対応中です。2")