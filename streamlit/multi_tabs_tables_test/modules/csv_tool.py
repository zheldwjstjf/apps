import pandas as pd
import numpy as np

from config.config import *

class CsvTool:

    def __init__(self):
        pass

    def create_empty_csv(self):
        """
        todo : 건내받은 target csv의 path의 csv가 없으면 생성하도록 할 것
        """        
        pass

    def get_csv_data(self, csv_file):
        """
        todo : 건내받은 target csv의 path의 csv를 load하도록 할 것
        """
        self.csv_file = csv_file

        df = pd.read_csv(self.csv_file)
        # print("\n"*3 + "csv data 1 : ", df)

        return df

    def save_results(self, results_df, row, amount):
        """
        save annotated results after every button click
        todo : 건내받은 target csv의 path의 csv애 쓰고/저장 하도록 할 것
        """
        results_df.at[row, self.selected_column] = amount
        results_df.to_csv(self.csv_file, index=None)
        
        return None

    def load_data(self):
        df = pd.read_csv(self.csv_file)
        
        return df