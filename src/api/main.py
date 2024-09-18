# api/main.py

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from api.routes import player_routes, team_routes

app = FastAPI(title="Sports Data API", version="1.0.0")

# Configure CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allows all origins
    allow_credentials=True,
    allow_methods=["*"],  # Allows all methods
    allow_headers=["*"],  # Allows all headers
)

# Include routers
app.include_router(player_routes.router, prefix="/api/players", tags=["players"])
app.include_router(team_routes.router, prefix="/api/teams", tags=["teams"])

@app.get("/")
async def root():
    return {"message": "Welcome to the Sports Data API"}

# api/routes/player_routes.py

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from api.services import player_service
from database.connection import get_db

router = APIRouter()

@router.get("/{player_id}")
async def get_player(player_id: str, db: Session = Depends(get_db)):
    player = player_service.get_player(db, player_id)
    if player is None:
        raise HTTPException(status_code=404, detail="Player not found")
    return player

@router.get("/")
async def list_players(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    players = player_service.list_players(db, skip=skip, limit=limit)
    return players

# api/routes/team_routes.py

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from api.services import team_service
from database.connection import get_db

router = APIRouter()

@router.get("/{team_id}")
async def get_team(team_id: str, db: Session = Depends(get_db)):
    team = team_service.get_team(db, team_id)
    if team is None:
        raise HTTPException(status_code=404, detail="Team not found")
    return team

@router.get("/")
async def list_teams(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    teams = team_service.list_teams(db, skip=skip, limit=limit)
    return teams