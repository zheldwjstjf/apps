import os
import sys
import matplotlib.pyplot as plt
from matplotlib import rcParams
from wordcloud import WordCloud, STOPWORDS

from modules.snippet_tools import SnippetTools

class VisualizationTool:
    def __init__(self, streamlit) -> None:
        self.st = streamlit
        self.snippetTools = SnippetTools(self.st)

    def wordcloud(self, mail_body_text):

        stopwords = STOPWORDS
        wc = WordCloud(stopwords=stopwords, background_color="white", max_words=77).generate(mail_body_text)

        img_folder_path = "/app/apps/images/"
        # Check whether the specified path exists or not
        isExist = os.path.exists(img_folder_path)

        if not isExist:        
            # Create a new directory because it does not exist 
            os.makedirs(img_folder_path)

        # 
        img_file_path = img_folder_path + "result_img.png"
        try:
            wc.to_file(img_file_path)
        except Exception as e:
            self.st.error("Exception : " + str(e))

        try:
            self.snippetTools.image_alignment(img_file_path, 1000)
        except Exception as e:
            self.st.error("Exception : " + str(e))



