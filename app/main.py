# app/main.py
from fastapi import FastAPI
from fastapi.responses import FileResponse
from redis_client import get_redis_connection
from models import AutocompleteRequest, AutocompleteResponse
from fastapi.staticfiles import StaticFiles
import uvicorn
    
app = FastAPI()
app.mount("/static", StaticFiles(directory="static"), name="static")

redis_conn = get_redis_connection()

@app.get("/autocomplete/", response_model=AutocompleteResponse)
async def autocomplete(query: str):
    suggestions = redis_conn.keys(f"{query}*")
    suggestions.sort(key=lambda x: -int(redis_conn.get(x) or 0))  # Sort by popularity
    print(suggestions)
    return AutocompleteResponse(suggestions=suggestions[:5])

@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/index.html")
async def index():
    return FileResponse("static/index.html")


if __name__ == "__main__":
    # Run the app with auto-reload using uvicorn
    # Example: uvicorn main:app --reload
    uvicorn.run(app, host="0.0.0.0", port=8000)
