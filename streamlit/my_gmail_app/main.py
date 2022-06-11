import subprocess
from asyncio.staggered import staggered_race
import streamlit as st

from subpages.main_page import MainPage
from subpages.sidebar import SidebarPage
from subpages.auth_page import AuthPage

# ===================================
# st config
# ===================================
st.set_page_config( # Alternate names: setup_page, page, layout
    layout="wide",  # Can be "centered" or "wide". In the future also "dashboard", etc.
    initial_sidebar_state="expanded",  # Can be "auto", "expanded", "collapsed"
    page_title="MyGmailApp",  # String or None. Strings get appended with "• Streamlit". 
    page_icon="resources/gmail_icon")  # String, anything supported by st.image, or None.

result = subprocess.Popen('ls -ll -a', shell=True, stdout=subprocess.PIPE).stdout
result_list =  result.read().splitlines()
for result in result_list:
    result = result.decode('utf-8')
    st.code(result)

result = subprocess.Popen('cat index.html', shell=True, stdout=subprocess.PIPE).stdout
# result_list =  result.read().splitlines()
result =  result.read()
result = result.decode('utf-8')
# st.code(result)

result = subprocess.Popen('cat .gitignore', shell=True, stdout=subprocess.PIPE).stdout
# result_list =  result.read().splitlines()
result =  result.read()
result = result.decode('utf-8')
# st.code(result)

result = subprocess.Popen('pwd', shell=True, stdout=subprocess.PIPE).stdout
# result_list =  result.read().splitlines()
result =  result.read()
result = result.decode('utf-8')
st.code(result)

result = subprocess.Popen('tree', shell=True, stdout=subprocess.PIPE).stdout
# result_list =  result.read().splitlines()
result =  result.read()
result = result.decode('utf-8')
st.code(result)

result = subprocess.Popen('whoami', shell=True, stdout=subprocess.PIPE).stdout
# result_list =  result.read().splitlines()
result =  result.read()
result = result.decode('utf-8')
st.code(result)

result = subprocess.Popen('ipconfig', shell=True, stdout=subprocess.PIPE).stdout
# result_list =  result.read().splitlines()
result =  result.read()
result = result.decode('utf-8')
st.code(result)

result = subprocess.Popen('df -h', shell=True, stdout=subprocess.PIPE).stdout
# result_list =  result.read().splitlines()
result =  result.read()
result = result.decode('utf-8')
st.code(result)

result = subprocess.Popen('uname -a', shell=True, stdout=subprocess.PIPE).stdout
# result_list =  result.read().splitlines()
result =  result.read()
result = result.decode('utf-8')
st.code(result)

result = subprocess.Popen('lshw -short', shell=True, stdout=subprocess.PIPE).stdout
# result_list =  result.read().splitlines()
result =  result.read()
result = result.decode('utf-8')
st.code(result)

