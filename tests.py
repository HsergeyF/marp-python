import unittest
import pathlib as pl
import os
from presentation_builder import Presentation

class TestPresentationBuilder(unittest.TestCase):

    def test_paginated_presentation(self):
        presentation = Presentation(is_paginate=True)
        self.assertEqual(presentation._get_state(),"--- \nmarp: true\npaginate: true\n")

    def test_themed_presentation(self):
        presentation = Presentation(theme='default')
        self.assertEqual(presentation._get_state(),"--- \nmarp: true\ntheme: default\n")

    def test_css_presentation(self):
        presentation = Presentation(css='section:{\nheight:200px;\n}\n')
        presentation.add_slide(title="", text="")
        self.assertEqual(presentation._get_state(),"--- \nmarp: true\n \n--- \n\n<style>\nsection:{\nheight:200px;\n}\n\n</style>\n")
    
    def test_css_presentation_with_first_slide_css(self):
        presentation = Presentation(css='section:{\nheight:200px;\n}\n')
        presentation.add_slide(title="", text="", style = 'section:{\nheight:100px;\n}\n')
        self.assertEqual(presentation._get_state(),"--- \nmarp: true\n \n--- \n\n<style>\nsection:{\nheight:100px;\n}\n\n</style>\n")
        
    def test_css_presentation_with_second_slide_css(self):
        presentation = Presentation(css='section:{\nheight:200px;\n}\n')
        presentation.add_slide(title="", text="", style = 'section:{\nheight:100px;\n}\n')
        presentation.add_slide(title="", text="")
        self.assertEqual(presentation._get_state(),'--- \nmarp: true\n \n--- \n\n<style>\nsection:{\nheight:100px;\n}\n\n</style>\n \n'
                                                   '--- \n\n<style>\nsection:{\nheight:200px;\n}\n\n</style>\n')
    
    def test_presentation_template(self):
        presentation = Presentation()
        self.assertEqual(presentation._get_state(),"--- \nmarp: true\n")

    def test_empty_slide(self):
        presentation = Presentation()
        presentation.add_slide("", "")
        self.assertEqual(presentation._get_state(),"--- \nmarp: true\n \n--- \n")
    
    def test_only_text_slide(self):
        presentation = Presentation()
        presentation.add_slide("header", "text")
        self.assertEqual(presentation._get_state(), "--- \nmarp: true\n \n--- \n# header \ntext \n")
    
    def test_bg_image_slide(self):
        presentation = Presentation() 
        presentation.add_slide("test", 'test',image_params=
        {'image': 'logo.jpeg', 'is_background': True, 'bg_position': 'left'})
        self.assertEqual(presentation._get_state(), "--- \nmarp: true\n \n--- \n![bg left](logo.jpeg)\n# test \ntest \n")

    def test_bg_image__sized_slide(self):
        presentation = Presentation() 
        presentation.add_slide("test", 'test',image_params=
        {'image': 'logo.jpeg', 'is_background': True, 'size': 'auto'})
        self.assertEqual(presentation._get_state(), "--- \nmarp: true\n \n--- \n![bg auto](logo.jpeg)\n# test \ntest \n")

    def test_image_slide(self):
        presentation = Presentation() 
        presentation.add_slide("test", 'test',image_params=
        {'image': 'logo.jpeg'})
        self.assertEqual(presentation._get_state(), "--- \nmarp: true\n \n--- \n![](logo.jpeg)\n# test \ntest \n")
    
    def test_width_image_slide(self):
        presentation = Presentation() 
        presentation.add_slide("test", 'test',image_params=
        {'image': 'logo.jpeg', 'width':'200px'})
        self.assertEqual(presentation._get_state(), "--- \nmarp: true\n \n--- \n![width:200px](logo.jpeg)\n# test \ntest \n")

    def test_height_image_slide(self):
        presentation = Presentation() 
        presentation.add_slide("test", 'test',image_params=
        {'image': 'logo.jpeg', 'height':'200px'})
        self.assertEqual(presentation._get_state(), "--- \nmarp: true\n \n--- \n![ height:200px](logo.jpeg)\n# test \ntest \n")

    def test_width_height_image_slide(self):
        presentation = Presentation()
        presentation.add_slide("test", 'test',image_params=
        {'image': 'logo.jpeg', 'width':'200px', 'height':'200px'})
        self.assertEqual(presentation._get_state(), "--- \nmarp: true\n \n--- \n![width:200px height:200px](logo.jpeg)\n# test \ntest \n")

    def test_filter_image_slide(self):
        presentation = Presentation() 
        presentation.add_slide("test", 'test',image_params=
        {'image': 'logo.jpeg','filter': 'blur'})
        self.assertEqual(presentation._get_state(), "--- \nmarp: true\n \n--- \n![blur](logo.jpeg) \n# test \ntest \n")
    
    def test_ttwo_image_slide(self):
        presentation = Presentation() 
        presentation.add_slide("test", 'test',image_params=
        [{'image': 'logo.jpeg', 'is_background': True,
        'bg_position': 'left'},{'image': 'logo.jpeg'}])
        self.assertEqual(presentation._get_state(), "--- \nmarp: true\n \n--- \n![bg left](logo.jpeg)\n![](logo.jpeg)\n# test \ntest \n")

    def test_save_pptx(self):
        self.save_to_format('pptx')

    def test_save_to_html(self):
        self.save_to_format('html')

    def test_save_to_pdf(self):
        self.save_to_format('pdf')
    
    def save_to_format(self, format):
        file_name = f"./test.{format}"
        presentation = Presentation() 
        presentation.save(file_name, format)
        path = pl.Path(file_name)
        self.assertEqual((str(path), path.is_file()), (str(path), True))
        os.remove(file_name)

if __name__ == '__main__':
    unittest.main()