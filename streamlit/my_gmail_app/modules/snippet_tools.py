class SnippetTools:

    def __init__(self, streamlit) -> None:
        self.st = streamlit

    def image_alignment(self, img_path, img_width):
        col1, col2, col3 = self.st.columns((0.1, 8, 10))

        with col1:
            self.st.write("")

        with col2:
            #
            img=img_path
            self.st.image(img, width=img_width)
            
        with col3:
            self.st.write("")