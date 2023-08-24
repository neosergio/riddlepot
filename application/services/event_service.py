from domain.repositories.event_repository import EventRepository
from domain.entities.event import Event, EventCreate


class EventService:
    def __init__(self, event_repository: EventRepository):
        self.event_repository = event_repository


    def create_event(self, event: EventCreate) -> Event:
        name = event.name
        datetime = event.datetime
        short_description = event.short_description
        event = EventCreate(name=name, datetime=datetime, short_description=short_description)
        return self.event_repository.create_event(name=event.name, datetime=event.datetime, short_description=event.short_description)
