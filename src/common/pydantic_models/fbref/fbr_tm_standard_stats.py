from typing import Optional
from pydantic import BaseModel

class FbrTmStandardStats(BaseModel):
    team_id: str
    team: str
    season: str
    league: Optional[str] = None
    players_used: Optional[int] = None
    average_age: Optional[float] = None
    possession_pct: Optional[float] = None
    playing_time_mp: Optional[int] = None
    playing_time_starts: Optional[int] = None
    playing_time_min: Optional[int] = None
    playing_time_90s: Optional[int] = None
    performance_gls: Optional[int] = None
    performance_ast: Optional[int] = None
    performance_g_a: Optional[int] = None
    performance_g_pk: Optional[int] = None
    performance_pk: Optional[int] = None
    performance_pkatt: Optional[int] = None
    performance_crd_y: Optional[int] = None
    performance_crd_r: Optional[int] = None
    expected_xg: Optional[float] = None
    expected_npxg: Optional[float] = None
    expected_xag: Optional[float] = None
    expected_npxg_xag: Optional[float] = None
    progression_prgc: Optional[int] = None
    progression_prgp: Optional[int] = None
    per_90_minutes_gls: Optional[float] = None
    per_90_minutes_ast: Optional[float] = None
    per_90_minutes_g_a: Optional[float] = None
    per_90_minutes_g_pk: Optional[float] = None
    per_90_minutes_g_a_pk: Optional[float] = None
    per_90_minutes_xg: Optional[float] = None
    per_90_minutes_xag: Optional[float] = None
    per_90_minutes_xg_xag: Optional[float] = None
    per_90_minutes_npxg: Optional[float] = None
    per_90_minutes_npxg_xag: Optional[float] = None
    url: str