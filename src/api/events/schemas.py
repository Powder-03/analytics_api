from pydantic import BaseModel, Field 
from typing import Optional, List , Annotated


class EventSchema(BaseModel):
    id: Annotated[int, Field(description="The unique identifier of the event")]
  #  name: Annotated[str, Field(description="The name of the event")]
   # description: Annotated[Optional[str], Field(description="A brief description of the event", default=None)]