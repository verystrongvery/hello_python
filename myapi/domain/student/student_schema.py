from typing import Optional

from pydantic import BaseModel, field_validator, Field

class CreateStudent(BaseModel):
    name: str
    age: int
    email: str

    @field_validator('name')
    def name_not_empty(cls, v):
        if not v or not v.strip():
            raise ValueError('빈 값 불가')
        return v
    @field_validator('age')
    def age_range(cls, v):
        if v <= 0:
            raise ValueError('1세 이상')
        return v
    @field_validator('email')
    def email_not_empty(cls, v):
        if not v or not v.strip():
            raise ValueError('빈 값 불가')
        return v

class UpdateStudent(BaseModel):
    id: int
    name: Optional[str] = Field(default=None)
    age: Optional[int] = Field(default=None)
    email: Optional[str] = Field(default=None)

    @field_validator('age')
    def age_range(cls, v):
        if v is not None:
            if v <= 0:
                raise ValueError('1세 이상')
        return v

class Student(BaseModel):
    id: int
    name: str
    age: int
    email: str