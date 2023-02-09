import unittest
import pathlib as pl
import os
from presentation_builder import Presentation

class TestPresentationBuilder(unittest.TestCase):
    
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

    def test_filter_image_slide(self):
        presentation = Presentation() 
        presentation.add_slide("test", 'test',image_params=
        {'image': 'logo.jpeg','filter': 'blur'})
        self.assertEqual(presentation._get_state(), "--- \nmarp: true\n \n--- \n![blur](logo.jpeg) \n# test \ntest \n")

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

    def test_image_slide(self):
        pass

    def test_styled_text_slide(self):
        pass

    def test_styled_image_slide(self):
        pass

    def test_list_slide(self):
        pass

    def test_css_style_slide(self):
        pass


if __name__ == '__main__':
    unittest.main()