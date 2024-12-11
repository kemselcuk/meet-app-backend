from pydantic import BaseModel
from datetime import datetime
from typing import Optional, List

class UserBase(BaseModel):
    username: str
    email: str

class UserCreate(UserBase):
    password: str

class User(UserBase):
    id: int

    class Config:
        orm_mode = True

class GroupBase(BaseModel):
    name: str
    description: Optional[str] = None

class GroupCreate(GroupBase):
    pass

class Group(GroupBase):
    id: int
    created_at: datetime

    class Config:
        orm_mode = True

class MeetingBase(BaseModel):
    title: str
    description: Optional[str] = None
    location: str
    meeting_time: datetime

class MeetingCreate(MeetingBase):
    group_id: int

class Meeting(MeetingBase):
    id: int
    group_id: int

    class Config:
        orm_mode = True