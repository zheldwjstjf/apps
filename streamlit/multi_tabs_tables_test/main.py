import streamlit as st
import altair as alt
import sqlite3
from sqlite3 import Error
import datetime

from config.config import *
from modules.pages.side_bar import Sidebar
from modules.csv_tool import CsvTool
from modules.pages.tabs_tables_template import TabsTablestemplate
from modules.pages.non_native_features import NonNativeFeatures
from todo.to_do import todo_list

class MyApp:

    def __init__(self):

        #
        from modules.db import DbApp
        dbApp = DbApp()
        self.dbConn = dbApp.check_storage_db(db_file)

        #
        self.ct = CsvTool()

        #
        self.nnf = NonNativeFeatures(self.dbConn)
        
        #
        self.ttt = TabsTablestemplate(st, self.nnf, self.dbConn)

        #
        self.sb = Sidebar(st, self.dbConn, self.ct)

    def main(self):

        # =================
        # st config
        st.set_page_config(  # Alternate names: setup_page, page, layout
            layout="wide",  # Can be "centered" or "wide". In the future also "dashboard", etc.
            initial_sidebar_state="expanded",  # Can be "auto", "expanded", "collapsed"
            page_title="Editable Table",  # String or None. Strings get appended with "• Streamlit". 
            page_icon=None,  # String, anything supported by st.image, or None.
        )

        # =================
        # main page
        st.title("TABs > EXPANDERs > TABs > TABLE")

        print("\n"*10 + "="*300)
        self.ttt.create_tabs("root")

        self.sb.sidebar_page()

        st.write("---")
        st.subheader("(TO DO)")
        # =================
        # To Do
        with st.expander("TO DO"):
            todo_list_count = len(todo_list)
            for i in range(todo_list_count):
                st.write("["+str(i+1)+"] ___ " + todo_list[i])
                st.write("---")


myApp = MyApp()
myApp.main()