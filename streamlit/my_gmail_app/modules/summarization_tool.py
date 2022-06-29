from nltk.corpus import stopwords
from nltk.cluster.util import cosine_distance
import numpy as np
import networkx as nx

class SummarizationTool:

    def __init__(self, streamlit) -> None:
        self.st = streamlit

    def read_article(self, file_name):
        file = open(file_name, "r")
        filedata = file.readlines()
        article = filedata[0].split(". ")
        sentences = []

        for sentence in article:
            print(sentence)
            sentences.append(sentence.replace("[^a-zA-Z]", " ").split(" "))
        sentences.pop() 
        
        return sentences

    def sentence_similarity(self, sent1, sent2, stopwords=None):
        if stopwords is None:
            stopwords = []
    
        sent1 = [w.lower() for w in sent1]
        sent2 = [w.lower() for w in sent2]
    
        all_words = list(set(sent1 + sent2))
    
        vector1 = [0] * len(all_words)
        vector2 = [0] * len(all_words)
    
        # build the vector for the first sentence
        for w in sent1:
            if w in stopwords:
                continue
            vector1[all_words.index(w)] += 1
    
        # build the vector for the second sentence
        for w in sent2:
            if w in stopwords:
                continue
            vector2[all_words.index(w)] += 1
    
        return 1 - cosine_distance(vector1, vector2)
    
    def build_similarity_matrix(self, sentences, stop_words):
        # Create an empty similarity matrix
        similarity_matrix = np.zeros((len(sentences), len(sentences)))
    
        for idx1 in range(len(sentences)):
            for idx2 in range(len(sentences)):
                if idx1 == idx2: #ignore if both are same sentences
                    continue 
                similarity_matrix[idx1][idx2] = self.sentence_similarity(sentences[idx1], sentences[idx2], stop_words)

        return similarity_matrix


    def generate_summary(self, file_name, top_n=5):
        stop_words = stopwords.words('english')

        
        sentences = []
        summarize_text = []

        # Step 1 - Read text anc split it
        # sentences =  read_article(file_name)
        sentences_text = """組み込み型
        以下のセクションでは、インタプリタに組み込まれている標準型について記述します。
        主要な組み込み型は、数値、シーケンス、マッピング、クラス、インスタンス、および例外です。
        コレクションクラスには、ミュータブルなものがあります。コレクションのメンバをインプレースに足し、引き、または並べ替えて、特定の要素を返さないメソッドは、コレクション自身ではなく None を返します。
        演算には、複数の型でサポートされているものがあります; 特に、ほぼ全てのオブジェクトは、等価比較でき、真理値を判定でき、 (repr() 関数や、わずかに異なる str() 関数によって) 文字列に変換できます。オブジェクトが print() 関数で印字されるとき、文字列に変換する関数が暗黙に使われます。
        真理値判定
        どのようなオブジェクトでも真理値として判定でき、 if や while の条件あるいは以下のブール演算の被演算子として使えます。
        オブジェクトは、デフォルトでは真と判定されます。ただしそのクラスが __bool__() メソッドを定義していて、それが False を返す場合、または __len__() メソッドを定義していて、それが 0 を返す場合は偽と判定されます。 1 主な組み込みオブジェクトで偽と判定されるものを次に示します:
        偽であると定義されている定数: None と False
        数値型におけるゼロ: 0, 0.0, 0j, Decimal(0), Fraction(0, 1)
        空のシーケンスまたはコレクション: '', (), [], {}, set(), range(0)
        ブール値の結果を返す演算および組み込み関数は、特に注釈のない限り常に偽値として 0 または False を返し、真値として 1 または True を返します。 (重要な例外: ブール演算 or および and は常に被演算子のうちの一つを返します。)
        """
        sentences_list_tmp = sentences_text.splitlines()
        for line in sentences_list_tmp:
            if len(line) > 0:
                sentences.append(line)
        print(sentences)

        # Step 2 - Generate Similary Martix across sentences
        sentence_similarity_martix = self.build_similarity_matrix(sentences, stop_words)

        # Step 3 - Rank sentences in similarity martix
        sentence_similarity_graph = nx.from_numpy_array(sentence_similarity_martix)
        scores = nx.pagerank(sentence_similarity_graph)

        # Step 4 - Sort the rank and pick top sentences
        ranked_sentence = sorted(((scores[i],s) for i,s in enumerate(sentences)), reverse=True)    
        print("Indexes of top ranked_sentence order are ", ranked_sentence)    

        for i in range(top_n):
            summarize_text.append(" ".join(ranked_sentence[i][1]))

        # Step 5 - Offcourse, output the summarize texr
        print("Summarize Text: \n", ". ".join(summarize_text))
