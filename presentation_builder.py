import os

class Presentation:
    
    _state = "--- \nmarp: true\n"

    _img_actions = {}


    def __init__(self, params: dict = {}, css = "", theme = "", paginate = False) -> None:
        """
        If you prefer to set some params for all slides,
        pass it during initialization and it will apply for the whole
        presentation.
        """
        if params:
            self._set_slide_params(params)
        self._css = css
        self._is_style_added = False
        if theme != "":
            self._state += f"theme: {theme}\n"
        if paginate:
            self._state += "paginate: true\n"

    def _set_slide_params(self, params: dict) -> None:
        for key, value in params.items():
            self._state += f"<!-- {key}: {value} --> \n"

    @staticmethod
    def _build_bg_string(params):
        if params['is_background']:
                    if "split_pct" in params.keys():
                        return f'![bg {params["bg_position"]}:{params["split_pct"]}]({params["image"]})\n'
                    else:
                        return f'![bg {params["bg_position"]}]({params["image"]})\n'
    
    @staticmethod
    def _build_image_string(params):
        img_string = "![" 
        if "width" in params.keys():
            img_string+=f'width:{params["width"]}'
        if "height" in params.keys():
            img_string+=f' height:{params["height"]}'
        return img_string+f']({params["image"]})\n'
        
    @staticmethod
    def _build_filter_string(params):
        if "value" in params.keys():
            return f'![{params["filter"]}:{params["value"]}]({params["image"]}) \n'
        else:
            return f'![{params["filter"]}]({params["image"]}) \n'

    def _try_set_bg_image(self, params):
        if "is_background" in params.keys():
            self._state += self._build_bg_string(params)

    
    def _try_set_img_filter(self, params):
        if "filter" in params.keys():
            self._state += self._build_filter_string(params)
    
    def _try_set_img(self, params):
        set_condition = all(item not in params.keys() for item in ["filter", "is_background"])
        if "is_background" in params.keys():
            if params["is_background" ] == True: 
                set_condition = False
        if set_condition:
            self._state += self._build_image_string(params)


    def _add_image_params(self, params: dict) -> None:
        if not params:
            return
        if isinstance(params, dict):
            self._try_set_bg_image(params)
            self._try_set_img_filter(params)
            self._try_set_img(params)
        elif isinstance(params, list):
            for param in params:
                self._try_set_bg_image(param)
                self._try_set_img_filter(param)
                self._try_set_img(param)
        else:
            raise Exception('Image params is a dict in case of 1 img \
                             and list of dicts in case if there are more than 1 image. \
                             Please provide correrct format of image settings.')
        
    def _add_style(self):
        if not self._is_style_added and self._css!= "":
            self._state += f"\n<style>\n{self._css}\n</style>\n"
            self._is_style_added = True


    
    def add_slide(self, title: str, text:str, 
                  params: dict = {}, image_params: dict = {}) -> None:
        self._end_slide()
        self._add_style()
        self._add_image_params(image_params)
        self._set_slide_params(params)
        self._add_header(title)
        self._add_text(text)
    
    def _get_state(self):
        return self._state
    
    def _add_header(self, title):
        if len(title)!= 0: self._state += f"# {title} \n"
    
    def _add_text(self, text):
        if len(text)!= 0: self._state += f"{text} \n"


    def _end_slide(self) -> None:
        self._state += " \n--- \n"

    def save(self, path: str, format: str) -> None:
        """
        format: pptx, html, pdf, notes, image
        """
        with open(path, 'w') as file:
            file.write(self._state)
        if format != "md": os.system(f"marp --{format} {path}")
        
