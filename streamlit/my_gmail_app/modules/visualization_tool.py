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
        rcParams['figure.figsize'] = 100, 200

        fig = plt.figure()
        plt.imshow(wordcloud)
        plt.axis("off")
        
        self.st.pyplot(fig)