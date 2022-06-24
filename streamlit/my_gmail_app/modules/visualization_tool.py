import os
import sys
import matplotlib.pyplot as plt
from matplotlib import rcParams
from wordcloud import WordCloud, STOPWORDS

class VisualizationTool:
    def __init__(self, streamlit) -> None:
        self.st = streamlit

    def wordcloud(self, mail_body_text, widthsize, maxWords):

        stopwords = STOPWORDS
        try:
            wc = WordCloud(stopwords=stopwords, background_color="red", max_words=maxWords).generate(mail_body_text)

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
                self.st.image(img_file_path, width=widthsize)
            except Exception as e:
                self.st.error("Exception : " + str(e))

        except Exception as e:
            self.st.warning("NO TEXT")





