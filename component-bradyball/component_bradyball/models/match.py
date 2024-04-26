from pydantic import BaseModel
from typing import List

class Match(BaseModel):
    match_id: int
    attendance: int
    venue_name: str
    referee: str
    start_date: str
    start_time: str
    score: str
    ht_score: str
    home_team_id: int
    away_team_id: int
    home_formations: List[dict]
    away_formations: List[dict]