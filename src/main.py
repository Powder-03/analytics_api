from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Hello World"}

@app.get("/hello/{name}")
def read_item(name: str):
    return {"message": f"Hello {name}"}

@app.get("healthz")
def read_api_health():
    return {"status": "ok"}