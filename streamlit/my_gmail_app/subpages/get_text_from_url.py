import urllib

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

        self.result_text = ""

    def get_text_from_url(self, target_url):

        url = target_url
        file = urllib.request.urlopen(url)

        for line in file:
            decoded_line = line.decode("utf-8")
            self.result_text = self.result_text + decoded_line
        
        return self.result_text
