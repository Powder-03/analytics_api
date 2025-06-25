from fastapi import FastAPI
from api.events import router as events_router  

app = FastAPI()
app.include_router(events_router, prefix="/api/events")

@app.get("/")
def read_root():
    return {"message": "Hello World"}

@app.get("/hello/{name}")
def read_item(name: str):
    return {"message": f"Hello {name}"}

@app.get("/healthz")
def read_api_health():
    return {"status": "ok"}