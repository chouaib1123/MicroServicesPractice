from fastapi import APIRouter,Response
from app.Schemas import registerSchema,userRespSchema,userSchema
from app.utils import user_Service

router = APIRouter()



@router.post("/register/" , response_model=userRespSchema)
def register(service : user_Service , newUser : registerSchema ):
    return service.register(newUser)
    



@router.post("/login/")
def login(service: user_Service, user: userSchema, response: Response):
    return service.login(user, response)

