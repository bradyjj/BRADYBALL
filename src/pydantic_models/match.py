from pydantic import BaseModel, Field
from typing import List, Optional

class Match(BaseModel):
    match_id: int = Field(..., primary_key=True)
    season: str
    league: str
    home_team: str
    away_team: str
    home_team_id: Optional[int] = None
    away_team_id: Optional[int] = None
    start_date: str
    start_time: str
    attendance: Optional[int] = None
    venue_name: Optional[str] = None
    referee: Optional[str] = None
    score: Optional[str] = None
    ht_score: Optional[str] = None
    home_formations: Optional[List[dict]] = None
    away_formations: Optional[List[dict]] = None
    whoscored_url: Optional[str] = None
    stage: Optional[str] = None