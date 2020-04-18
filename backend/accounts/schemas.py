from pydantic import BaseModel, constr


class User(BaseModel):
    email: constr(regex=r'\d{2}im\d{4}@i-u.ac.jp')
    password: str
    email_verified: bool = False
