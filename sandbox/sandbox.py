from pydantic_settings import BaseSettings, SettingsConfigDict
from pydantic import BaseModel, Field, RootModel
from fakers import random_number, user_name, first_name, last_name, email, password, phone


class DefaultUser(BaseModel):
    id: int = Field(default_factory=random_number)
    username: str = Field(
        default_factory=user_name
    )
    first_name: str = Field(
        alias='firstName',
        default_factory=first_name
    )
    last_name: str = Field(
        alias='lastName',
        default_factory=last_name
    )
    email: str = Field(
        default_factory=email
    )
    password: str = Field(
        default_factory=password
    )
    phone: str = Field(
        default_factory=phone
    )
    user_status: int = Field(
        alias='userStatus',
        default_factory=random_number
    )

print(DefaultUser().model_dump(by_alias=True))



