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

        result = subprocess.Popen('ls -ll -a', shell=True, stdout=subprocess.PIPE).stdout
        result_list =  result.read().splitlines()
        for result in result_list:
            result = result.decode('utf-8')
            self.st.code(result)

        result = subprocess.Popen('cat index.html', shell=True, stdout=subprocess.PIPE).stdout
        # result_list =  result.read().splitlines()
        result =  result.read()
        result = result.decode('utf-8')
        # self.st.code(result)

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

