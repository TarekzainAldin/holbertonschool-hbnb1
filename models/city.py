from models.base_model import BaseModel

class City(BaseModel):
    def __init__(self, name="", *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.name = name

    def __str__(self):
        return "[City] ({}) {}".format(self.id, self.__dict__)
    