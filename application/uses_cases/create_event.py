from domain.repositories.event_repository import EventRepository
from domain.entities.event import EventCreate


class CreateEventUseCase:
    def __init__(self, event_repository: EventRepository):
        self.event_repository = event_repository

    def execute(self, name: str, datetime: str, short_description: str) -> EventCreate:
        event = self.event_repository.create_event(name=name, datetime=datetime, short_description=short_description)
        return event
