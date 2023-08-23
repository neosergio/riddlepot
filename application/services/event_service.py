from domain.repositories.event_repository import EventRepository
from domain.entities.event import Event, EventCreate


class EventService:
    def __init__(self, event_repository: EventRepository):
        self.event_repository = event_repository


    def create_event(self, name: str, datetime: str, short_description: str) -> EventCreate:
        event = Event(name=name, datetime=datetime, short_description=short_description)
        return self.event_repository.create_event(event)
