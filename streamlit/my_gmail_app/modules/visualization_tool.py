import os
import sys
from wordcloud import WordCloud
import matplotlib.pyplot as plt
from matplotlib import rcParams
from wordcloud import WordCloud, STOPWORDS

class VisualizationTool:
    def __init__(self, streamlit) -> None:
        self.st = streamlit

    def wordcloud(self):

        mytext = """
        Russian President Vladimir Putin has declared the end of "the era of the unipolar world" in a combative speech that lambasted Western countries at the St. Petersburg International Economic Forum on Friday.
        """

        stopwords = STOPWORDS
        wordcloud = WordCloud(stopwords=stopwords, background_color="white", max_words=50).generate(mytext)
        # rcParams['figure.figsize'] = 100, 200

        # fig, ax = plt.subplots()
        # plt.imshow(wordcloud)
        # self.st.pyplot(fig)

        # 
        img_folder_path = "/app/apps/images/"
        # Check whether the specified path exists or not
        isExist = os.path.exists(img_folder_path)

        if not isExist:        
            # Create a new directory because it does not exist 
            os.makedirs(img_folder_path)

        # 
        img_file_path = img_folder_path + "result.png"
        wordcloud.to_file(img_file_path)
        self.snippetTools.image_alignment(img_file_path, 500)
