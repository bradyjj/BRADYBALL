from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from .routes import player_routes, team_routes

app = FastAPI(title="BRADYBALL API", version="1.0.0")

# Configure CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include routers
app.include_router(player_routes.router, prefix="/BRADYBALL/api/players", tags=["players"])
app.include_router(team_routes.router, prefix="/BRADYBALL/api/teams", tags=["teams"])

@app.get("/")
async def root():
    return {"message": "Welcome to the BRADYBALL API"}