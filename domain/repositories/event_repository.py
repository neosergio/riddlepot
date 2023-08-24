from domain.entities.event import EventCreate, Event
from adapters.persistance.database import EventTable


class EventRepository:
    def create_event(self, name: str, short_description: str, datetime: str) -> EventCreate:
        event = EventTable({
            # Todo: Implement event_id auto increment
            "event_id" : "1",
            "name" : name,
            "datetime" : datetime,
            "short_description" : short_description})
        event.save()
        return Event(
            id=event.event_id,
            name=event.name,
            datetime=event.datetime
        )

    # ToDo: Refactor generate_next_event_id function
    # def generate_next_event_id(self) -> int:
    #     events = EventTable.scan()
    #     max_id = max([event.event_id for event in events], default=0)
    #     return max_id + 1
