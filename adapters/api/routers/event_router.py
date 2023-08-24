from fastapi import APIRouter, Depends, Form, Request
from domain.entities.event import Event, EventCreate
from application.services.event_service import EventService
from application.uses_cases.create_event import CreateEventUseCase
from config.dependencies import get_event_service


router = APIRouter()

@router.post("/events/", response_model=Event)
async def create_event(
        event: EventCreate,
        event_service: EventService = Depends(get_event_service),
):
    event = event_service.create_event(event)
    return event
