from presentation_builder import Presentation

if __name__ == "__main__":
    css = open("theme.css", "r").read()
    presentation = Presentation(css = css, theme = "", is_paginate = False)
    presentation.add_slide("Optimization 2022", '1. First bullet \n2. Second bullet \n',{'backgroundColor': '#f7d064'}, 
    [{'image': 'logo.jpeg', 'is_background': True,
    'bg_position': 'left'},{'image': 'logo.jpeg'}])
    presentation.add_slide("Hello", 'world')
    presentation.add_slide("Hello", 'wosrld')
    presentation.save('example.md', 'html')