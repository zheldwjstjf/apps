import subprocess
from subprocess import PIPE, CalledProcessError, check_call, Popen

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

        with self.st.expander("See explanation"):

            commandLine = None
            col1, col2 = self.st.columns((1,1))
            
            # input command line
            commandLine = col1.text_input("Terminal 1", placeholder="Type command line here", key=1)

            if commandLine == None:
                pass
            else:
                result = subprocess.Popen(commandLine, shell=True, stdout=subprocess.PIPE)
                output, err = result.communicate()
                
                # output
                output =  output.read()
                output = output.decode('utf-8')
                col1.code(output)

                # err
                err =  err.read()
                err = err.decode('utf-8')
                col1.code(err)


            # input command line
            commandLine = col2.text_input("Terminal 2", placeholder="Type command line here", key=2)

            if commandLine == None:
                pass
            else:
                result = subprocess.Popen(commandLine, shell=True, stdout=subprocess.PIPE)
                output, err = result.communicate()

                # output                
                output =  output.read()
                output = output.decode('utf-8')
                col2.code(output)

                # err
                err =  err.read()
                err = err.decode('utf-8')
                col2.code(err)


        """
        result = subprocess.Popen('cat .gitignore', shell=True, stdout=subprocess.PIPE).stdout
        # result_list =  result.read().splitlines()
        result =  result.read()
        result = result.decode('utf-8')
        # self.st.code(result)

        result = subprocess.Popen('pwd', shell=True, stdout=subprocess.PIPE).stdout
        # result_list =  result.read().splitlines()
        result =  result.read()
        result = result.decode('utf-8')
        self.st.code(result)

        result = subprocess.Popen('tree', shell=True, stdout=subprocess.PIPE).stdout
        # result_list =  result.read().splitlines()
        result =  result.read()
        result = result.decode('utf-8')
        self.st.code(result)

        result = subprocess.Popen('whoami', shell=True, stdout=subprocess.PIPE).stdout
        # result_list =  result.read().splitlines()
        result =  result.read()
        result = result.decode('utf-8')
        self.st.code(result)

        result = subprocess.Popen('ipconfig', shell=True, stdout=subprocess.PIPE).stdout
        # result_list =  result.read().splitlines()
        result =  result.read()
        result = result.decode('utf-8')
        self.st.code(result)

        result = subprocess.Popen('df -h', shell=True, stdout=subprocess.PIPE).stdout
        # result_list =  result.read().splitlines()
        result =  result.read()
        result = result.decode('utf-8')
        self.st.code(result)

        result = subprocess.Popen('uname -a', shell=True, stdout=subprocess.PIPE).stdout
        # result_list =  result.read().splitlines()
        result =  result.read()
        result = result.decode('utf-8')
        self.st.code(result)

        result = subprocess.Popen('lshw -short', shell=True, stdout=subprocess.PIPE).stdout
        # result_list =  result.read().splitlines()
        result =  result.read()
        result = result.decode('utf-8')
        self.st.code(result)
        """

