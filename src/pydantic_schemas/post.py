from pydantic import BaseModel, Field

class Post(BaseModel):
    id : int
    title : str



    # @validator("id")
    # def check_that_id_is_less_than_two(cls, v ):
    #     if v > 2 :
    #         raise ValueError("Id is not less than two")
    #     else:
    #         return v


