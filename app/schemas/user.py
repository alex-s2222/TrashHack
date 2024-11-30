from pydantic import BaseModel
from typing import Optional, Dict
from fastapi import Request
from fastapi import Query

class getUser(BaseModel):
    __tablename__ = "user"
    id: Optional[int] = None
    orgStructureoOne: Optional[str] = None
    funcBlock: Optional[str] = None
    orgStructureTwo: Optional[str] = None
    orgStructureThree: Optional[str] = None
    orgStructureFour: Optional[str] = None
    post: Optional[str] = None
    role: Optional[str] = None
    lastName: Optional[str] = None
    firstName: Optional[str] = None
    phone: Optional[str] = None
    city: Optional[str] = None
    address: Optional[str] = None

    @classmethod
    def parser(
        cls, 
        request: Request,
        orgStructureoOne: Optional[str] = None,
        funcBlock: Optional[str] = None,
        orgStructureTwo: Optional[str] = None,
        orgStructureThree: Optional[str] = None,
        orgStructureFour: Optional[str] = None,
        post: Optional[str] = None,
        role: Optional[str] = None,
        lastName: Optional[str] = None,
        firstName: Optional[str] = None,
        phone: Optional[str] = None,
        city: Optional[str] = None,
        address: Optional[str] = None
    ) -> Dict:
        return {
                "orgStructureoOne": orgStructureoOne ,
                "funcBlock":  funcBlock,
                "orgStructureTwo":orgStructureTwo ,
                "orgStructureThree": orgStructureThree,
                "orgStructureFour": orgStructureFour,
                "post": post,
                "role": role,
                "lastName": lastName,
                "firstName": firstName,
                "phone": phone,
                "city": city,
                "address":address ,
        }
