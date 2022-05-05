import sqlite3
from sqlite3 import Error
import importlib

# --------------------
# config
# --------------------


class DbApp:

    def __init__(self):
        pass


    def check_storage_db(self, storage_db_file):

        try:
            conn = sqlite3.connect(storage_db_file)
        except Exception as e:
            # raise e
            print(e)

        self.conn = conn

        # -
        sql_create_table = """CREATE TABLE IF NOT EXISTS maindb (
                                        ID INTEGER,
                                        update_date TIMESTAMP,
                                        outter_tab text,
                                        expander text,
                                        inner_tab text,
                                        inner_table text
                                    );"""

        # -
        sql_create_table2 = """CREATE TABLE IF NOT EXISTS maindb2 (
                                        TMP1 text NULL,
                                        TMP2 text NULL,
                                        TMP3 text NULL,
                                        TMP4 text NULL,
                                        TMP5 text NULL,
                                        TMP6 text NULL,
                                        TMP7 text NULL,
                                        TMP8 text NULL,
                                        TMP9 text NULL,
                                        TMP10 text NULL
                                    );"""


        self.cursor = self.conn.cursor()
        self.cursor.execute(sql_create_table)
        # self.cursor.execute(sql_create_table2)

        return self.conn
