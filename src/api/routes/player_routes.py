from fastapi import APIRouter, Depends, HTTPException
from ...database.connection import get_supabase
from typing import List

router = APIRouter()

@router.get("/{player_id}")
async def get_player(player_id: str, supabase=Depends(get_supabase)):
    response = supabase.table("players").select("*").eq("player_id", player_id).execute()
    if not response.data:
        raise HTTPException(status_code=404, detail="Player not found")
    return response.data[0]

@router.get("/")
async def list_players(skip: int = 0, limit: int = 100, supabase=Depends(get_supabase)):
    response = supabase.table("players").select("*").range(skip, skip + limit - 1).execute()
    return response.data

@router.post("/")
async def create_player(player: dict, supabase=Depends(get_supabase)):
    response = supabase.table("players").insert(player).execute()
    return response.data[0]

@router.put("/{player_id}")
async def update_player(player_id: str, player: dict, supabase=Depends(get_supabase)):
    response = supabase.table("players").update(player).eq("player_id", player_id).execute()
    if not response.data:
        raise HTTPException(status_code=404, detail="Player not found")
    return response.data[0]

@router.delete("/{player_id}")
async def delete_player(player_id: str, supabase=Depends(get_supabase)):
    response = supabase.table("players").delete().eq("player_id", player_id).execute()
    if not response.data:
        raise HTTPException(status_code=404, detail="Player not found")
    return {"message": "Player deleted successfully"}