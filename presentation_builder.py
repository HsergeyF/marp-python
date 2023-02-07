
class Presentation:
    
    _state = "--- \nmarp: true\n"

    _img_actions = {}

    def __init__(self, params: dict = {}) -> None:
        """
        If you prefer to set some params for all slides,
        pass it during initialization and it will apply for the whole
        presentation.
        """
        if params:
            self._set_slide_params(params)

    def _set_slide_params(self, params: dict) -> None:
        for key, value in params.items():
            self._state += f"<!-- {key}: {value} --> \n"


    def _try_set_bg_image(self, params):
        if "is_background" in params.keys():
                if params['is_background']:
                    if "split_pct" in params.keys():
                        self._state += f'![bg {params["bg_position"]}:{params["split_pct"]}]({params["image"]})\n'
                    else:
                        self._state += f'![bg {params["bg_position"]}]({params["image"]})\n'
    
    def _try_set_img_filter(self, params):
        if "filter" in params.keys():
            if "value" in params.keys():
                self._state += f'![{params["filter"]}:{params["value"]}]({params["image"]}) \n'
            else:
                self._state += f'![{params["filter"]}]({params["image"]}) \n'


    def _add_image_params(self, params: dict) -> None:
        if isinstance(params, dict):
            self._try_set_bg_image(params)
            self._try_set_img_filter(params)
        elif isinstance(params, list):
            for param in params:
                self._try_set_bg_image(param)
                self._try_set_img_filter(param)
        else:
            raise Exception('Image params is a dict in case of 1 img \
                             and list of dicts in case if there are more than 1 image. \
                             Please provide correrct format of image settings.')
        

    
    def add_slide(self, title: str, text:str, 
                  params: dict = {}, image_params: dict = {}) -> None:
        self._end_slide()
        self._add_image_params(image_params)
        self._set_slide_params(params)
        self._add_header(title)
        self._add_text(text)
    
    def _get_state(self):
        return self._state
    
    def _add_header(self, title):
        if len(title)!= 0: self._state += f"# {title} \n"
    
    def _add_text(self, text):
        if len(text)!= 0: self._state += f" {text} \n"


    def _end_slide(self) -> None:
        self._state += " \n--- \n"

    def save(self, path: str) -> None:
        with open(path, 'w') as file:
            file.write(self._state)
