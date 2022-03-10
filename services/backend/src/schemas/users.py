from tortoise.contrib.pydantic import pydantic_model_creator

from src.config.models import Users
from pydantic import BaseModel


UserIn= pydantic_model_creator(
    Users, name="UserIn", exclude_readonly=True
)


UserOut = pydantic_model_creator(
    Users, name="UserOut", exclude=["id","password", "created_at", "modified_at"]
)


UserDatabaseSchema = pydantic_model_creator(
    Users, name="User", exclude=["created_at", "modified_at"]
)

class UserLogin(BaseModel):
    username: str
    password: str