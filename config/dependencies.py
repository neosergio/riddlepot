from fastapi import Depends
from domain.repositories.event_repository import EventRepository
from application.services.event_service import EventService



# Dependency to get the event repository
def get_event_repository():
    return EventRepository()

def get_event_service(
        event_repository: EventRepository = Depends(get_event_repository)
):
    return EventService(event_repository)
