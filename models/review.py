# models/review.py
from models.base_model import BaseModel

class Review(BaseModel):
    def __init__(self, text="", *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.text = text

    def __str__(self):
        return "[Review] ({}) {}".format(self.id, self.__dict__)
    