# app/models.py
from pydantic import BaseModel

class AutocompleteRequest(BaseModel):
    query: str

class AutocompleteResponse(BaseModel):
    suggestions: list[str]
