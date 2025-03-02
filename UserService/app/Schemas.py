from pydantic import BaseModel




class userSchema(BaseModel):
    username : str 
    password : str

class registerSchema(userSchema):
    vpassword : str

class userRespSchema(userSchema):
    pass
    model_config = {
        "from_attributes": True 
    }
