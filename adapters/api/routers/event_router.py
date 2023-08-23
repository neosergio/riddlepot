from fastapi import APIRouter, Depends
from domain.entities.event import Event
from application.services.event_service import EventService
from config.dependencies import get_event_service


router = APIRouter()

@router.post("/events/", response_model=Event)
async def create_event(
        name: str,
        datetime: str,
        short_description: str,
        event_service: EventService = Depends(get_event_service),
):
    event = event_service.create_event(name, datetime, short_description)
    return event
