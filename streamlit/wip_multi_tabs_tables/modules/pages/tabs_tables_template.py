from modules.csv_tool import CsvTool
from pathlib import Path

class TabsTablestemplate:

    def __init__(self, st, nnf, dbConn):

        #
        self.st = st

        #
        self.nnf = nnf

        #
        self.ct = CsvTool()

        #
        self.dbConn = dbConn

    # =================
    # Outter tabs
    def create_tabs(self, widget_key):

        self.st.write("---")
        self.st.subheader("TABs")

        # selectbox
        outter_tab_count = self.st.selectbox(
            "▶︎ Tab Counts", [1,2,3,4,5,6,7,8,9,10], index = 2,
            key="outter_tab_count"
        )
        self.outter_tab_count = outter_tab_count

        outter_tab_dict = {
                "Tab1": self._tab1, # [ key ] == [ 탭 이름 ]
                "Tab2": self._tab2,
                "Tab3": self._tab3,
                "Tab4": self._tab4,
                "Tab5": self._tab5,
                "Tab6": self._tab6,
                "Tab7": self._tab7,
                "Tab8": self._tab8,
                "Tab9": self._tab9,
                "Tab10": self._tab10,
        }
        outter_tab_dict = dict(list(outter_tab_dict.items())[:self.outter_tab_count])
        outter_tab_content = self.nnf._outter_tabs(widget_key, outter_tab_dict)
        if callable(outter_tab_content):
            outter_tab_content()
        elif type(outter_tab_content) == str:
            self.st.markdown(outter_tab_content, unsafe_allow_html=True)
        else:
            self.st.write(outter_tab_content)


    def _tab1(self):

        self.st.subheader(". EXPANDERs")

        # selectbox
        self.selected_expander_1_count = self.st.selectbox(
            "▶︎ Expander Counts", [1,2,3,4,5,6,7,8,9,10], index = 2,
            key="expander_1_count"
        )
        self.expander_1_count = self.selected_expander_1_count

        for i in range(1, self.expander_1_count+1):
            i = str(i)
            self.create_expander("E"+i, "Outer_tab1"+"expander_"+i)

    def _tab2(self):

        self.st.subheader(". EXPANDERs")

        # selectbox
        expander_2_count = self.st.selectbox(
            "▶︎ Expander Counts", [1,2,3,4,5,6,7,8,9,10], index = 2,
            key="expander_2_count"
        )
        self.expander_2_count = expander_2_count

        for i in range(1, self.expander_2_count+1):
            i = str(i)
            self.create_expander("E"+i, "Outer_tab2"+"expander_"+i)

    def _tab3(self):

        self.st.subheader(". EXPANDERs")

        # selectbox
        expander_3_count = self.st.selectbox(
            "▶︎ Expander Counts", [1,2,3,4,5,6,7,8,9,10], index = 2,
            key="expander_3_count"
        )
        self.expander_3_count = expander_3_count

        for i in range(1, self.expander_3_count+1):
            i = str(i)
            self.create_expander("E"+i, "Outer_tab3"+"expander_"+i)

    def _tab4(self):

        self.st.subheader(". EXPANDERs")

        # selectbox
        expander_4_count = self.st.selectbox(
            "▶︎ Expander Counts", [1,2,3,4,5,6,7,8,9,10], index = 2,
            key="expander_4_count"
        )
        self.expander_4_count = expander_4_count

        for i in range(1, self.expander_4_count+1):
            i = str(i)
            self.create_expander("E"+i, "Outer_tab4"+"expander_"+i)

    def _tab5(self):

        self.st.subheader(". EXPANDERs")

        # selectbox
        expander_5_count = self.st.selectbox(
            "▶︎ Expander Counts", [1,2,3,4,5,6,7,8,9,10], index = 2,
            key="expander_5_count"
        )
        self.expander_5_count = expander_5_count

        for i in range(1, self.expander_5_count+1):
            i = str(i)
            self.create_expander("E"+i, "Outer_tab5"+"expander_"+i)

    def _tab6(self):

        self.st.subheader(". EXPANDERs")

        # selectbox
        expander_6_count = self.st.selectbox(
            "▶︎ Expander Counts", [1,2,3,4,5,6,7,8,9,10], index = 2,
            key="expander_6_count"
        )
        self.expander_6_count = expander_6_count

        for i in range(1, self.expander_6_count+1):
            i = str(i)
            self.create_expander("E"+i, "Outer_tab6"+"expander_"+i)

    def _tab7(self):

        self.st.subheader(". EXPANDERs")

        # selectbox
        expander_7_count = self.st.selectbox(
            "▶︎ Expander Counts", [1,2,3,4,5,6,7,8,9,10], index = 2,
            key="expander_7_count"
        )
        self.expander_7_count = expander_7_count

        for i in range(1, self.expander_7_count+1):
            i = str(i)
            self.create_expander("E"+i, "Outer_tab7"+"expander_"+i)

    def _tab8(self):

        self.st.subheader(". EXPANDERs")

        # selectbox
        expander_8_count = self.st.selectbox(
            "▶︎ Expander Counts", [1,2,3,4,5,6,7,8,9,10], index = 2,
            key="expander_8_count"
        )
        self.expander_8_count = expander_8_count

        for i in range(1, self.expander_8_count+1):
            i = str(i)
            self.create_expander("E"+i, "Outer_tab8"+"expander_"+i)

    def _tab9(self):

        self.st.subheader(". EXPANDERs")

        # selectbox
        expander_9_count = self.st.selectbox(
            "▶︎ Expander Counts", [1,2,3,4,5,6,7,8,9,10], index = 2,
            key="expander_9_count"
        )
        self.expander_9_count = expander_9_count

        for i in range(1, self.expander_9_count+1):
            i = str(i)
            self.create_expander("E"+i, "Outer_tab9"+"expander_"+i)

    def _tab10(self):

        self.st.subheader(". EXPANDERs")

        # selectbox
        expander_10_count = self.st.selectbox(
            "▶︎ Expander Counts", [1,2,3,4,5,6,7,8,9,10], index = 2,
            key="expander_10_count"
        )
        self.expander_10_count = expander_10_count

        for i in range(1, self.expander_10_count+1):
            i = str(i)
            self.create_expander("E"+i, "Outer_tab10"+"expander_"+i)


    # =================
    # Expander template

    def create_expander(self, table_name, widget_key):
        # =================

        with self.st.expander(table_name):

            try:
                self.do_inner_tabs(table_name, widget_key)
            except Exception as e:
                self.st.error(e)


    def create_file(self, csv_file):
        ######### read / write database #########
        self.dbCursor = self.dbConn.cursor()

        # select
        sql_select_inner_tab_name = "SELECT * FROM maindb WHERE ID='" + str("E0") + "'"

        # check if inner_tab_name_changed
        try:
            self.dbCursor.execute(sql_select_inner_tab_name)
        except Exception as e:
            print("Exception - [inner][5] Select : ", e)
        current_selected_items = self.dbCursor.fetchall()
        current_selected_items_tuple = current_selected_items[0]

        self.last_selected_outter_tab = current_selected_items_tuple[2]
        self.csv_file = csv_file.replace("editable_", "editable_"+self.last_selected_outter_tab+"_")

        ######### close database #########
        self.dbConn.commit()
        # self.dbConn.close()

        myfile = Path(self.csv_file)
        try:
            myfile.touch(exist_ok=False)
            f = open(myfile,"a+")
            f.write("item,column1,column2,column3")
            f.write("\n")
            f.write("row1,-,-,-")
            f.write("\n")
            f.write("row2,-,-,-")
            f.write("\n")
            f.write("row3,-,-,-")
            f.close()
        except:
            pass


    # =================
    # Inner tabs

    def do_inner_tabs(self, table_name, widget_key):

        self.st.write("---")
        self.st.subheader(".. TABS")

        # selectbox
        innter_tab_count = self.st.selectbox(
            "▶︎ Tab Counts", [1,2,3,4,5,6,7,8,9,10], index = 2,
            key="innter_tab_count_"+widget_key
        )
        self.inner_tab_count = innter_tab_count

        self.table_name_1 = table_name + "_tab1" # [ key ] == [ 탭 이름 ]
        self.table_name_2 = table_name + "_tab2"
        self.table_name_3 = table_name + "_tab3"
        self.table_name_4 = table_name + "_tab4"
        self.table_name_5 = table_name + "_tab5"
        self.table_name_6 = table_name + "_tab6"
        self.table_name_7 = table_name + "_tab7"
        self.table_name_8 = table_name + "_tab8"
        self.table_name_9 = table_name + "_tab9"
        self.table_name_10 = table_name + "_tab10"

        widget_key = table_name + "-" + widget_key
        
        inner_tab_dict = {
                self.table_name_1: self._inner_tab1,
                self.table_name_2: self._inner_tab2,
                self.table_name_3: self._inner_tab3,
                self.table_name_4: self._inner_tab4,
                self.table_name_5: self._inner_tab5,
                self.table_name_6: self._inner_tab6,
                self.table_name_7: self._inner_tab7,
                self.table_name_8: self._inner_tab8,
                self.table_name_9: self._inner_tab9,
                self.table_name_10: self._inner_tab10,
        }
        inner_tab_dict = dict(list(inner_tab_dict.items())[:self.inner_tab_count])
        inner_tab_content = self.nnf._inner_tabs(widget_key, inner_tab_dict)

        if callable(inner_tab_content):
            inner_tab_content()
        elif type(inner_tab_content) == str:
            self.st.markdown(inner_tab_content, unsafe_allow_html=True)
        else:
            self.st.write(inner_tab_content)

    def _inner_tab1(self):
        self.create_file("data/csv/editable_" + self.table_name_1 + ".csv")
        self.create_table(self.table_name_1, self.table_name_1, self.csv_file)

    def _inner_tab2(self):
        self.create_file("data/csv/editable_" + self.table_name_2 + ".csv")
        self.create_table(self.table_name_2, self.table_name_2, self.csv_file)

    def _inner_tab3(self):
        self.create_file("data/csv/editable_" + self.table_name_3 + ".csv")
        self.create_table(self.table_name_3, self.table_name_3, self.csv_file)

    def _inner_tab4(self):
        self.create_file("data/csv/editable_" + self.table_name_4 + ".csv")
        self.create_table(self.table_name_4, self.table_name_4, self.csv_file)

    def _inner_tab5(self):
        self.create_file("data/csv/editable_" + self.table_name_5 + ".csv")
        self.create_table(self.table_name_5, self.table_name_5, self.csv_file)

    def _inner_tab6(self):
        self.create_file("data/csv/editable_" + self.table_name_6 + ".csv")
        self.create_table(self.table_name_6, self.table_name_6, self.csv_file)

    def _inner_tab7(self):
        self.create_file("data/csv/editable_" + self.table_name_7 + ".csv")
        self.create_table(self.table_name_7, self.table_name_7, self.csv_file)

    def _inner_tab8(self):
        self.create_file("data/csv/editable_" + self.table_name_8 + ".csv")
        self.create_table(self.table_name_8, self.table_name_8, self.csv_file)

    def _inner_tab9(self):
        self.create_file("data/csv/editable_" + self.table_name_9 + ".csv")
        self.create_table(self.table_name_9, self.table_name_9, self.csv_file)

    def _inner_tab10(self):
        self.create_file("data/csv/editable_" + self.table_name_10 + ".csv")
        self.create_table(self.table_name_10, self.table_name_10, self.csv_file)



    # =================
    # Table template

    def create_table(self, table_name, widget_key, csv_file):

        df = self.ct.get_csv_data(csv_file)

        # set index
        df = df.set_index("item")
        # print("\n"*3 + "csv data 2 : ", df)

        self.st.write("---")
        self.st.subheader("... TABLE")
        self.st.write(table_name)

        # multiselect
        utility_costs = self.st.multiselect(
            "▶︎ Select Row(s)", list(df.index), ["row1", "row2", "row3"],
            key=widget_key+"#"
        )
        if not utility_costs:
            self.st.error("No row selected.")
        else:
            # =================
            # table data
            table_data = df.loc[utility_costs]

            # =================
            # table
            self.st.write("\n")
            self.st.write(table_data)

        if self.st.button("EXPORT", key=widget_key+"$"):
            pass