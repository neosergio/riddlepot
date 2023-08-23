from pydantic import BaseModel


class EventBase(BaseModel):
    name: str
    datetime: str


class EventCreate(EventBase):
    short_description: str