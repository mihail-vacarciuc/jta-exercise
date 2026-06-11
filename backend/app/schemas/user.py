from pydantic import BaseModel, EmailStr, AnyHttpUrl
from typing import Optional, List

class AddressSchema (BaseModel):
    address: str
    city:str
    state:str
    postalCode:str
    country: str

class CompanySchema (BaseModel):
    department: Optional[str]
    name: str
    title: Optional[str]
    address: AddressSchema

class UserSchame (BaseModel):
    id: int
    firstName:str
    lastName:str
    age: int
    gender: str
    email: EmailStr
    birthDate: Optional[str]
    image: AnyHttpUrl
    address: AddressSchema
    university: str
    company: CompanySchema
    role: str
    
class UsersResponseSchema(BaseModel):
    users: List[UserSchame]
    total: int
    skip: int
    limit: int
