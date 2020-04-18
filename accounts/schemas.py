from pydantic import BaseModel, EmailStr


class User(BaseModel):
    display_name: str
    email: EmailStr
    password: str
    email_verified: bool = False
    phone_number: str = None
