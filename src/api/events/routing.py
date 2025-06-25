from fastapi import APIRouter
from .schemas import EventSchema

router = APIRouter()


# /api/events/

@router.get("/")
def read_events():
    # a bunch of items in the table
    return {
        "result": [1,2,3]
    }

@router.get("/{event_id}")
def get_event(event_id: int) -> EventSchema:
    return {
         "id": event_id
    }

