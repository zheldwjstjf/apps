class Sidebar:

    def __init__(self, st, dbConn, csvTool) -> None:
        self.st = st
        self.dbConn = dbConn
        self.ct = csvTool
        
    def sidebar_page(self):

        # refresh button
        if self.st.sidebar.button("Reload"):
            pass

        # =================
        # SHOW Last focused tab-table

        ######### read / write database #########
        self.dbCursor = self.dbConn.cursor()

        # [1] select
        sql_select_inner_tab_name = "SELECT * FROM maindb WHERE ID='" + str("E0") + "'"

        # check if inner_tab_name_changed
        try:
            self.dbCursor.execute(sql_select_inner_tab_name)
        except Exception as e:
            print("Exception - [inner][5] Select : ", e)
        current_selected_items = self.dbCursor.fetchall()
        current_selected_items_tuple = current_selected_items[0]
        
        print("\n"*3 + "="*30)
        print(">>> current_selected_items_tuple : ", current_selected_items_tuple)
        # print("current_selected_items_tuple type : ", type(current_selected_items_tuple))

        self.last_selected_outter_tab = current_selected_items_tuple[2]
        print(">>> last_selected_outter_tab : ", self.last_selected_outter_tab)
        # print("last_selected_outter_tab type : ", type(last_selected_outter_tab))

        self.last_selected_inner_tab = current_selected_items_tuple[4]
        print(">>> last_selected_inner_tab : ", self.last_selected_inner_tab)
        # print("last_selected_inner_tab type : ", type(last_selected_inner_tab))
        
        print("="*30 + "\n"*3)

        ######### close database #########
        self.dbConn.commit()
        self.dbConn.close()

        self.st.sidebar.title("=== [ %s_%s ] ===" % (self.last_selected_outter_tab, self.last_selected_inner_tab,))


        # =================
        # T A S K
        self.st.sidebar.title("T A S K")

        # select task
        selected_task = self.st.sidebar.selectbox(
            'Select Task',
            ('ReName', 'Edit Table'), index=1, 
            key="select_task")


        # =================
        # Rename
        if selected_task == "ReName":

            self.st.sidebar.title(" . R E N A M E")

            # select item
            selected_item = self.st.sidebar.selectbox(
                'Select Item',
                ('Outter Tab', 'Expander', 'Inner Tab', 'Inner Table'),
                key="selected_item")

            # select outter tab
            if selected_item == 'Outter Tab':
                selected_outter_tab = self.st.sidebar.selectbox(
                    'Select Outter Tab',
                    ('Tab 1', 'Tab 2', 'Tab 3'),
                    key="selected_outter_tab")

            # select outter Expander
            if selected_item == 'Expander':
                selected_outter_tab = self.st.sidebar.selectbox(
                    'Select Outter Tab',
                    ('Tab 1', 'Tab 2', 'Tab 3'),
                    key="selected_outter_tab")

                selected_expander = self.st.sidebar.selectbox(
                    'Select Expander',
                    ('Expander 1', 'Expander 2', 'Expander 3'),
                    key="selected_outter_expander")

            # select Inner Tab
            if selected_item == 'Inner Tab':
                selected_outter_tab = self.st.sidebar.selectbox(
                    'Select Outter Tab',
                    ('Tab 1', 'Tab 2', 'Tab 3'),
                    key="selected_outter_tab")

                selected_expander = self.st.sidebar.selectbox(
                    'Select Expander',
                    ('Expander 1', 'Expander 2', 'Expander 3'),
                    key="selected_outter_expander")

                selected_expander = self.st.sidebar.selectbox(
                    'Select Inner Tab',
                    ('Inner Tab 1', 'Inner Tab 2', 'Inner Tab 3'),
                    key="selected_inner_expander")

            # select Inner Table
            if selected_item == 'Inner Table':
                selected_outter_tab = self.st.sidebar.selectbox(
                    'Select Outter Tab',
                    ('Tab 1', 'Tab 2', 'Tab 3'),
                    key="selected_outter_tab")

                selected_expander = self.st.sidebar.selectbox(
                    'Select Expander',
                    ('Expander 1', 'Expander 2', 'Expander 3'),
                    key="selected_outter_expander")

                selected_inner_tab = self.st.sidebar.selectbox(
                    'Select Inner Tab',
                    ('Inner Tab 1', 'Inner Tab 2', 'Inner Tab 3'),
                    key="selected_inner_tab")

                selected_inner_table = self.st.sidebar.selectbox(
                    'Select Inner Table',
                    ('Inner Table 1', 'Inner Table 2', 'Inner Table 3'),
                    key="selected_inner_table")

            # input new name
            new_name = self.st.sidebar.text_input("New Name", value="Type New Name Here")

            # save button
            if self.st.sidebar.button("SAVE"):
                "new_name"
                pass

        # =================
        # EDIT Table
        if selected_task == "Edit Table":

            self.st.sidebar.title(" . EDIT TABLE")

            # select edit table task
            selected_edit_table_task = self.st.sidebar.selectbox(
                'Select EDIT Table Task',
                ('UPDATE', 'DELETE', 'ADD'),
                key="edit_table")

            # =================
            # UPDATE
            if selected_edit_table_task == "UPDATE":

                self.st.sidebar.title(" .. U P D A T E")

                # select row
                selected_row = self.st.sidebar.selectbox(
                    'Select Row',
                    ('row1', 'row2', 'row3'),
                    key="select_row")

                # select column
                self.selected_column = self.st.sidebar.selectbox(
                    'Select Column',
                    ('column1', 'column2', 'column3'),
                    key="select_column")

                #
                updated_data = self.st.sidebar.text_input("Data", value="Type Data Here")

                # check selected row
                if selected_row=="row1":
                    row = 0
                if selected_row=="row2":
                    row = 1
                if selected_row=="row3":
                    row = 2

                # save button
                # todo : target csv의 path를 건내주도록 할 것
                if self.st.sidebar.button("SAVE"):
                    self.ct.save_results(self.results_df, row, updated_data)


            # =================
            # DELETE
            if selected_edit_table_task == "DELETE":

                self.st.sidebar.title(" .. D E L E T E")

                selected_delete_task = self.st.sidebar.selectbox(
                    'Select DELETE Item',
                    ('row', 'column'),
                    key="delete_task")

                if selected_delete_task == 'row':
                    # select row
                    selected_row = self.st.sidebar.selectbox(
                        'Select Row',
                        ('row1', 'row2', 'row3'),
                        key="select_row")

                if selected_delete_task == 'column':
                    # select column
                    self.selected_column = self.st.sidebar.selectbox(
                        'Select Column',
                        ('column1', 'column2', 'column3'),
                        key="select_column")

                # Delete button
                if self.st.sidebar.button("DELETE"):
                    pass


            # =================
            # ADD
            if selected_edit_table_task == "ADD":
                # select
                self.st.sidebar.title(" .. A D D")

                selected_add_task = self.st.sidebar.selectbox(
                    'Select ADD Item',
                    ('row', 'column'),
                    key="add_task")

                if selected_add_task == 'row':
                    # select row
                    selected_row = self.st.sidebar.selectbox(
                        'Select Row',
                        ('row1', 'row2', 'row3'),
                        key="select_row")

                if selected_add_task == 'column':
                    # select column
                    self.selected_column = self.st.sidebar.selectbox(
                        'Select Column',
                        ('column1', 'column2', 'column3'),
                        key="select_column")

                # Delete button
                if self.st.sidebar.button("ADD"):
                    pass