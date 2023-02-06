class Presentation:
    
    _state = "--- \nmarp: true"

    def __init__(self, params: dict = {}) -> None:
        self.is_initial_slide = True
        if params:
            self.set_slide_params(params)
        self._end_slide()

    def set_slide_params(self, params: dict) -> None:
        for key, value in params.items():
            self._state += f"<!-- {key}: {value}--> \n"

    
    def add_slide(self, title: str, text:str, params: dict) -> None:
        self.set_slide_params(params)
        self._state += f"# {title} \n"
        self._state += f" {text} \n"
        if self.is_initial_slide:
            self.is_initial_slide = False
        else:
            self._end_slide()
    
    def _end_slide(self) -> None:
        self._state += " \n--- \n"

    def save(self, path: str) -> None:
        with open(path, 'w') as file:
            file.write(self._state)
