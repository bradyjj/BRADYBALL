from fastapi import APIRouter, HTTPException, Query
from src.api.services import BRADYBALL

router = APIRouter()

@router.get("/players")
async def get_player_data(name: str = Query(..., description="Player name")):
    data = await BRADYBALL.get_player_data(name)
    return data

@router.get("/players/combined")
async def get_combined_player_data(name: str = Query(..., description="Player name")):
    data = await BRADYBALL.get_player_data(name)
    combined_data = await BRADYBALL.combine_player_data(name, data)
    return combined_data