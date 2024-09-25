from fastapi import APIRouter, Depends, HTTPException
from ...database.connection import get_supabase
from typing import List

router = APIRouter()

@router.get("/{team_id}")
async def get_team(team_id: str, supabase=Depends(get_supabase)):
    response = supabase.table("teams").select("*").eq("team_id", team_id).execute()
    if not response.data:
        raise HTTPException(status_code=404, detail="Team not found")
    return response.data[0]

@router.get("/")
async def list_teams(skip: int = 0, limit: int = 100, supabase=Depends(get_supabase)):
    response = supabase.table("teams").select("*").range(skip, skip + limit - 1).execute()
    return response.data

@router.post("/")
async def create_team(team: dict, supabase=Depends(get_supabase)):
    response = supabase.table("teams").insert(team).execute()
    return response.data[0]

@router.put("/{team_id}")
async def update_team(team_id: str, team: dict, supabase=Depends(get_supabase)):
    response = supabase.table("teams").update(team).eq("team_id", team_id).execute()
    if not response.data:
        raise HTTPException(status_code=404, detail="Team not found")
    return response.data[0]

@router.delete("/{team_id}")
async def delete_team(team_id: str, supabase=Depends(get_supabase)):
    response = supabase.table("teams").delete().eq("team_id", team_id).execute()
    if not response.data:
        raise HTTPException(status_code=404, detail="Team not found")
    return {"message": "Team deleted successfully"}