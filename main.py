from presentation_builder import Presentation


if __name__ == "__main__":
    presentation = Presentation()
    presentation.add_slide("Hello", 'world', {'backgroundColor': '#5eba7d'})
    presentation.save('example.md')