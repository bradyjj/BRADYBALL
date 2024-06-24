from pydantic import BaseModel, Field
from typing import Optional

class FbrefMatch(BaseModel):
    match_id: int = Field(..., primary_key=True)
    season: str
    league: str
    home_team: str
    away_team: str
    home_team_id: Optional[int] = None
    away_team_id: Optional[int] = None
    home_xg: Optional[float] = None
    away_xg: Optional[float] = None
    score: str
    start_date: str
    round: str
    day: str
    attendance: Optional[int] = None
    venue_name: Optional[str] = None
    referee: Optional[str] = None
    score: Optional[str] = None
    fbref_url: Optional[str] = None
    notes: Optional[str] = None