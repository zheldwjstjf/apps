import streamlit as st
import pandas as pd
import base64
import requests
import json
from io import StringIO
import os

class CSVTool:
    def __init__(self, streamlit):
        self.st = streamlit

        self.csv_data_file = "utility_costs2.csv"

        current_path = os.getcwd()
        self.st.info("current_path : " + current_path)
        f = open(self.csv_data_file, "w")
        f.write("111")
        f.close() 

        self.url = "https://api.github.com/repos/zheldwjstjf/apps/contents/streamlit/utilitycosts/data/utility_costs.csv"
    
    @st.cache(suppress_st_warning=True)
    def load_data(self):
        """
        load spreadsheet with data to be annotated
        """

        try:
            df = pd.read_csv(self.csv_data_file)
            self.st.warning('ローカルデータを取得しました。')

            return df
        except Exception as e:
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
                # self.st.warning('クラウドデータを取得しました。')

                return df
            else:
                self.st.warning('クラウドデータの取得ができませんでした。しばらく待って再度お試しください。')


    def save_input(self, df, row, amount, selected_date, auth_status):
        """
        save input
        """

        if auth_status == True:
            try:
                # add input amount to selected row
                df = pd.read_csv(self.csv_data_file)
                df.at[row, selected_date] = amount

                # add 0 to unselected rows
                row_list = [0,1,2]
                row_list.pop(row)
                for row in row_list:
                    df.at[row, selected_date] = 0

                # update csv
                df.to_csv(self.csv_data_file, index=None)
                self.st.warning('ローカルデータを変更しました。')

            except Exception as e:
                # print("Exception - save input : ", e)
                # TODO
                # df => StringIO => content => push to github
                # https://gist.github.com/avullo/b8153522f015a8b908072833b95c3408
                pass
                self.st.success("登録しました。")
        else:    
            self.st.warning("認証が必要です。")