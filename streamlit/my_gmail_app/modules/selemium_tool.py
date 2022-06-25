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

