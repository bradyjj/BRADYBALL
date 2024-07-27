from fastapi import FastAPI
from src.api.routes import BRADYBALL

app = FastAPI()

app.include_router(BRADYBALL.router, prefix="/api/BRADYBALL", tags=["BRADYBALL"])

@app.get("/")
async def root():
    return {"message": "Welcome to BRADYBALL API"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)