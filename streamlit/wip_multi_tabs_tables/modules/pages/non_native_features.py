import streamlit as st
import sqlite3
from sqlite3 import Error
import importlib
import datetime

from config.config import *

class NonNativeFeatures:

    def __init__(self, dbConn):
        self.dbConn = dbConn


    # ===================================
    # outter tabs
    # ===================================
    def _outter_tabs(self, widgets_key, tabs_data = {}, default_active_tab=0):
            # tab_titles_list / key만 모은 list
            tab_titles_list = list(tabs_data.keys())
            if not tab_titles_list:
                return None
            # active_tab / str / 탭 이름
            active_tab = st.radio("", tab_titles_list, index=default_active_tab, key=widgets_key)
            # str인 active_tab이 몇 번째 child인지 Indexing
            # child는 int
            child = tab_titles_list.index(active_tab)+1
            self.outter_tab_name = tab_titles_list[child-1]

            st.write("selected outter tab name : ", self.outter_tab_name)
            print("\n"*3+"selected outter tab name : ", self.outter_tab_name)

            print("[DEBUG] [outter] child : ", child)

            st.markdown("""  
                <style type="text/css">

                div[role=radiogroup] {
                    flex-direction: unset
                }
                div[role=radiogroup] label {
                    border: 1px solid #999;
                    padding: 4px 20px;
                    border-radius: 4px 4px 0 0;
                    position: relative;
                    top: 1px;
                    }
                div[role=radiogroup] label:nth-child(""" + str(child) + """) {    
                    background: #FFF !important;
                    border-bottom: 1px solid transparent;
                }            
                </style>
            """,unsafe_allow_html=True)
            return tabs_data[active_tab]



    # ===================================
    # inner tabs
    # ===================================
    def _inner_tabs(self, widgets_key, tabs_data = {}, default_active_tab=0):
            tab_titles_list = list(tabs_data.keys())
            if not tab_titles_list:
                return None
            active_tab = st.radio("", tab_titles_list, index=default_active_tab, key=widgets_key)
            child = tab_titles_list.index(active_tab)+1
            inner_tab_name = tab_titles_list[child-1]
            expander_name = inner_tab_name.split("_tab")[0]
            
            st.write("selected inner tab name : ", inner_tab_name)
            print("\n"*3+"selected inner tab name : ", inner_tab_name)

            currentDateTime = datetime.datetime.now()

            print("[DEBUG] [inner] expander_name : ", expander_name)
            print("[DEBUG] [inner] child : ", child)
            
            # [1] select
            sql_select_inner_tab_E0_id = "SELECT ID FROM maindb WHERE ID='" + str("E0") + "'"

            # [2] insert
            row_E0 = "E0",str(currentDateTime),self.outter_tab_name,"-",inner_tab_name,"-"
            sql_insert_inner_tab_E0 = "INSERT INTO maindb VALUES (?, ?, ?, ?, ?, ?)"

            # [3] select
            sql_select_inner_tab_id = "SELECT ID FROM maindb WHERE ID='" + expander_name + "'"

            # [4] insert
            row = expander_name,str(currentDateTime),"-","-",inner_tab_name,"-"
            sql_insert_inner_tab = "INSERT INTO maindb VALUES (?, ?, ?, ?, ?, ?)"

            # [5] select
            sql_select_inner_tab_name = "SELECT inner_tab FROM maindb WHERE ID='" + expander_name + "'"

            # [6] update
            sql_update_inner_tab = 'UPDATE maindb SET inner_tab = "' + inner_tab_name + '",update_date="' + str(currentDateTime) + '",outter_tab="' + self.outter_tab_name + '" WHERE ID ="' + expander_name + '"'

            # [7] update
            sql_update_selected_inner_tab = 'UPDATE maindb SET inner_tab = "' + inner_tab_name + '",update_date="' + str(currentDateTime) + '",outter_tab="' + self.outter_tab_name + '" WHERE ID ="' + "E0" + '"'

            ######### read / write database #########
            self.dbConn = sqlite3.connect(db_file)
            self.dbCursor = self.dbConn.cursor()

            # check if E0 id exists
            try:
                self.dbCursor.execute(sql_select_inner_tab_E0_id)
            except Exception as e:
                print("Exception - [inner][1] Select : ", e)
            result = self.dbCursor.fetchone()

            # insert if id does not exist            
            if result:
                print("[SKIP] [inner] ID : E0가 이미 존재합니다.")
            else:
                print("[INSERT] [inner] ID : E0가 존재하지 않습니다. 인서트합니다.")
                try:
                    self.dbCursor.execute(sql_insert_inner_tab_E0, row_E0)
                except Exception as e:
                    print("Exception - [inner][2] Insert : ", e)

            # check if id exists
            try:
                self.dbCursor.execute(sql_select_inner_tab_id)
            except Exception as e:
                print("Exception - [inner][3] Select : ", e)
            result = self.dbCursor.fetchone()

            # insert if id does not exist            
            if result:
                print("[SKIP] [inner] ID : %s가 이미 존재합니다." % expander_name)
            else:
                print("[INSERT] [inner] ID : %s가 존재하지 않습니다. 인서트합니다." % expander_name)
                try:
                    self.dbCursor.execute(sql_insert_inner_tab, row)
                except Exception as e:
                    print("Exception - [inner][4] Insert : ", e)

            # check if inner_tab_name_changed
            try:
                self.dbCursor.execute(sql_select_inner_tab_name)
            except Exception as e:
                print("Exception - [inner][5] Select : ", e)
            result = self.dbCursor.fetchone()

            # update if inner_tab changed
            print("[inner] expander_name : ", expander_name)
            print("[inner] result : ", result[0])
            print("selected inner_tab_name : ", inner_tab_name)
            
            if inner_tab_name != result[0]:
                print("[UPDATE] inner_tab_name : %s를 갱신합니다." % inner_tab_name)
                try:
                    self.dbCursor.execute(sql_update_inner_tab)
                except Exception as e:
                    print("Exception - [inner][6] Update : ", e)

                try:
                    self.dbCursor.execute(sql_update_selected_inner_tab)
                except Exception as e:
                    print("Exception - [inner][7] Update : ", e)
            else:
                print("[SKIP] inner_tab_name : %s가 변화가 없습니다." % inner_tab_name)


            ######### close database #########
            self.dbConn.commit()
            self.dbConn.close()


            st.markdown("""  
                <style type="text/css">
                div[role=radiogroup] > label > ul:first-of-type {
                display: none
                }
                div[role=radiogroup] {
                    flex-direction: unset
                }
                div[role=radiogroup] label {
                    border: 1px solid #999;
                    padding: 4px 20px;
                    border-radius: 4px 4px 0 0;
                    position: relative;
                    top: 1px;
                    }
                div[role=radiogroup] label:nth-child(""" + str(child) + """) {    
                    background: #FFF !important;
                    border-bottom: 1px solid transparent;
                }            
                </style>
            """,unsafe_allow_html=True)
            return tabs_data[active_tab]
