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
        # driver = webdriver.Firefox(options=firefoxOptions, service=service)
        # driver.get(URL)

