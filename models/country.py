# models/country.py
from models.base_model import BaseModel

class Country(BaseModel):
    def __init__(self, name="", *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.name = name

    def __str__(self):
        return "[Country] ({}) {}".format(self.id, self.__dict__)
    