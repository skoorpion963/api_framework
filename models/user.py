from pydantic import BaseModel, Field, model_validator



class User(BaseModel):
    email: str = Field()
    password: str = Field()