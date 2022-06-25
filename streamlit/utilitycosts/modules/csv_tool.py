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

        self.csv_data_file = "/app/apps/data/utility_costs.csv"
    
    # @st.cache(suppress_st_warning=True)
    def load_data(self):
        """
        load spreadsheet with data to be annotated
        """

        try:
            df = pd.read_csv(self.csv_data_file)
            return df

        except Exception as e:
            self.st.error(str(e))

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
                self.st.success("登録しました。")

            except Exception as e:
                self.st.error(str(e))
        else:    
            self.st.warning("認証が必要です。")