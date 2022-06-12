class SnippetTools:

    def __init__(self, streamlit) -> None:
        self.st = streamlit

    def image_alignment(self, img_path, img_width):
        col1, col2, col3 = self.st.columns([1,6,1])

        with col1:
            pass

        with col2:
            #
            img=img_path
            self.st.image(img, width=img_width)
            
            #
            # self.st.markdown("![Alt Text](img_path)")

        with col3:
            pass