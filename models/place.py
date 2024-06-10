# models/place.py
from models.base_model import BaseModel

class Place(BaseModel):
    def __init__(self, name="", description="", *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.name = name
        self.description = description

    def __str__(self):
        return "[Place] ({}) {}".format(self.id, self.__dict__)
    