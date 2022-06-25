import os
import sys
import streamlit as st

class SeleniumTool:
    def __init__(self, streamlit) -> None:
        self.st = streamlit

    @st.experimental_singleton
    def installff():
        os.system('sbase install geckodriver')
        os.system('ln -s /home/appuser/venv/lib/python3.9/site-packages/seleniumbase/drivers/geckodriver /home/appuser/venv/bin/geckodriver')

    
    _ = installff()
    
    from selenium import webdriver
    from selenium.webdriver.firefox.firefox_binary import FirefoxBinary
    from selenium.webdriver import FirefoxOptions
    opts = FirefoxOptions()
    opts.add_argument("--headless")
    
    try:
        browser = webdriver.Firefox(executable_path="/home/appuser/venv/lib/python3.9/site-packages/seleniumbase/drivers/geckodriver", options=opts)
    except Exception as e:
        st.error(e)

    """
    browser.get('https://www.python.org/')
    st.write(browser.page_source)
    """


"""
import os
import sys
import streamlit as st
from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from webdriver_manager.firefox import GeckoDriverManager

class SeleniumTool:
    def __init__(self, streamlit) -> None:
        self.st = streamlit

    # @st.experimental_singleton
    def main(self):
        URL = "https://www.python.org/"

        st.title("Test Selenium")

        firefoxOptions = Options()
        firefoxOptions.add_argument("--headless")
        service = Service(GeckoDriverManager().install())
        driver = webdriver.Firefox(options=firefoxOptions, service=service)
        
        driver.get(URL)
"""
