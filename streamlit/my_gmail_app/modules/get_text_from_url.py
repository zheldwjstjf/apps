import json
import requests
from requests.models import MissingSchema
from bs4 import BeautifulSoup
import numpy as np
import re

class GetTextFromURL:
    """
    - class name : GetTextFromURL
    """

    def __init__(self, streamlit) -> None:
        """
        - method name : __init__
        - arg(s) : streamlit
        """

        self.st = streamlit

        self.url_list = []

    def beautifulsoup_extract_text_fallback(self, response_content):
        '''
        This is a fallback function, so that we can always return a value for text content.
        Even for when both Trafilatura and BeautifulSoup are unable to extract the text from a 
        single URL.
        '''
        
        # Create the beautifulsoup object:
        soup = BeautifulSoup(response_content, 'html.parser')
        
        # Finding the text:
        text = soup.find_all(text=True)
        
        # Remove unwanted tag elements:
        cleaned_text = ''
        blacklist = [
            '[document]',
            'noscript',
            'header',
            'html',
            'meta',
            'head', 
            'input',
            'script',
            'style',]

        # Then we will loop over every item in the extract text and make sure that the beautifulsoup4 tag
        # is NOT in the blacklist
        for item in text:
            if item.parent.name not in blacklist:
                cleaned_text += '{} '.format(item)
                
        # Remove any tab separation and strip the text:
        cleaned_text = cleaned_text.replace('\t', '')
        return cleaned_text.strip()
        

    def extract_text_from_single_web_page(self, url):        
        try:
            resp = requests.get(url)
            # We will only extract the text from successful requests:
            if resp.status_code == 200:
                return self.beautifulsoup_extract_text_fallback(resp.content)
            else:
                # This line will handle for any failures in both the Trafilature and BeautifulSoup4 functions:
                return np.nan
        # Handling for any URLs that don't have the correct protocol
        except MissingSchema:
            return np.nan
    
    def get_url_from_text(self, input_text):
        # self.url_list = re.findall('https?://(?:[-\w.]|(?:%[\da-fA-F]{2}))+', input_text)
        # self.url_list = re.findall(r'(https?://\S+)', input_text)

        link_regex = re.compile('((https?):((//)|(\\\\))+([\w\d:#@%/;$()~_?\+-=\\\.&](#!)?)*)', re.DOTALL)
        urlList_list = re.findall(link_regex, input_text)

        for url_list in urlList_list:
            url = url_list[:-1]
            self.url_list.append(url)
        self.st.write(self.url_list)

        return self.url_list
            