import subprocess

class AdminPage:

    def __init__(self, streamlit) -> None:
        """
        - method name : __init__
        - arg(s) : streamlit
        """

        self.st = streamlit

    def admin_page(self):
        """
        - method name : admin_page
        - arg(s) : 
        """

        # title
        self.st.markdown("<h1 style='text-align: center; color: red;'>Admin Page</h1>", unsafe_allow_html=True)

        with self.st.expander("Streamlit Server Terminal"):

            commandLine = None
            col1, col2 = self.st.columns((1,1))
            
            # input command line
            commandLine = col1.text_input("Terminal 1", placeholder="Type command line here", key=1)

            if commandLine == None:
                pass
            else:
                result = subprocess.Popen(commandLine, shell=True, stdout=subprocess.PIPE).stdout
                result =  result.read()
                result = result.decode('utf-8')
                col1.code(result)

            # input command line
            commandLine = col2.text_input("Terminal 2", placeholder="Type command line here", key=2)

            if commandLine == None:
                pass
            else:
                result = subprocess.Popen(commandLine, shell=True, stdout=subprocess.PIPE).stdout
                result =  result.read()
                result = result.decode('utf-8')
                col2.code(result)


        with self.st.expander("Streamlit Server Log"):

            line_num = self.st.number_input("Enter the maximum number of log lines (up to 100 lines)", min_value=1, max_value=100)
            commandLine = "tail -" + str(line_num) + " /app/app.log"

            if commandLine == None:
                pass
            else:
                result = subprocess.Popen(commandLine, shell=True, stdout=subprocess.PIPE).stdout
                result =  result.read()
                result = result.decode('utf-8')
                self.st.code(result)
