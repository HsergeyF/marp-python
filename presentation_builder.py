import os
from typing import Union

class Presentation:
    
    _state = "--- \nmarp: true\n"

    _img_actions = {}

    def __init__(self, css = "", theme = "", is_paginate = False) -> None:
        """
        If you prefer to set some params for all slides,
        pass it during initialization and it will apply for the whole
        presentation. 
        
        Parameters
        ----------

        css: str
            Css styles that will be applied to all slides

        theme: str 
            Theme name (default, gaia, uncover)

        is_paginate: bool, default=False
            If pagination needed

        Returns
        -------
        None
        """

        self._css = css
        self._is_style_added = False
        if theme != "":
            self._state += f"theme: {theme}\n"
        if is_paginate:
            self._state += "paginate: true\n"
    
    def add_slide(self, title: str, text:str, 
                  params: dict = {}, image_params: Union[dict, list] = {}, style = "") -> None:

        """
        Add slide to presentation and set provided parameters and style.
        
        Parameters
        ----------

        title: str 
            Slide title 

        text: str
            Slide text conten
        
        params: dict
            Slide build-in directives. You can set slide styling with this params. 
            Full list: https://marpit.marp.app/directives (Local directives)

        image_params: Union[dict, list]
            Dict or list of image dict objects with image parameters. If list provided, it will add all all imagegs to slide.
            Image may also be backgroung image or filtered image. See readme for examples.
        
        style: str
            Local css string for this slide

        Returns
        -------
        None
        """

        self._end_slide()
        self._add_style(style)
        self._add_image_params(image_params)
        self._set_slide_params(params)
        self._add_header(title)
        self._add_text(text)

    def _end_slide(self) -> None:
        self._state += " \n--- \n"
    
    def _add_style(self, style: str = ""):
        if not self._is_style_added and self._css!= "":
            if style== "":
                self._state += f"\n<style>\n{self._css}\n</style>\n"
                self._is_style_added = True
            else:
                self._state += f"\n<style>\n{style}\n</style>\n"
                self._is_style_added = False

    def _add_image_params(self, params: Union[dict, list]) -> None:
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
    
    def _set_slide_params(self, params: dict) -> None:
        for key, value in params.items():
            self._state += f"<!-- {key}: {value} --> \n"
    
    def _add_header(self, title: str) -> None:
        if len(title)!= 0: self._state += f"# {title} \n"
    
    def _add_text(self, text: str) -> None:
        if len(text)!= 0: self._state += f"{text} \n"

    def _try_set_bg_image(self, params)->None:
        if "is_background" in params.keys():
            self._state += self._build_bg_string(params)

    def _try_set_img_filter(self, params)->None:
        if "filter" in params.keys():
            self._state += self._build_filter_string(params)
    
    def _try_set_img(self, params)->None:
        set_condition = all(item not in params.keys() for item in ["filter", "is_background"])
        if "is_background" in params.keys():
            if params["is_background" ] == True: 
                set_condition = False
        if set_condition:
            self._state += self._build_image_string(params)

    def save(self, path: str, format: str) -> None:
        """
        Save presentation to provided format.
        
        Parameters
        ----------

        path: str 
            Output file path

        format: str
            One of available presentation formats (pptx, html, pdf, notes, image)

        Returns
        -------
        None
        """

        with open(path, 'w') as file:
            file.write(self._state)
        if format != "md": os.system(f"marp --{format} {path}")

    @staticmethod
    def _build_bg_string(params)->str:
        if params['is_background']:
            if "bg_position" in params.keys():  
                if "split_pct" in params.keys():
                    return f'![bg {params["bg_position"]}:{params["split_pct"]}]({params["image"]})\n'
                return f'![bg {params["bg_position"]}]({params["image"]})\n'
            elif "size" in params.keys():
                return f'![bg {params["size"]}]({params["image"]})\n'
            else:
                raise Exception('Provide one of next properties for correct work: bg_position, size')
    
    @staticmethod
    def _build_image_string(params)->str:
        img_string = "![" 
        if "width" in params.keys():
            img_string+=f'width:{params["width"]}'
        if "height" in params.keys():
            img_string+=f' height:{params["height"]}'
        return img_string+f']({params["image"]})\n'
        
    @staticmethod
    def _build_filter_string(params)->str:
        if "value" in params.keys():
            return f'![{params["filter"]}:{params["value"]}]({params["image"]}) \n'
        else:
            return f'![{params["filter"]}]({params["image"]}) \n'
    
    def _get_state(self) -> str:
        return self._state


    
    
        
