from typing import Optional
from pydantic import BaseModel

class FbrPlKeeperStats(BaseModel):
    league: str
    season: str
    team: str
    player: str
    nation: Optional[str] = None
    position: Optional[str] = None
    age: Optional[int] = None
    born: Optional[int] = None
    playing_time_mp: Optional[int] = None
    playing_time_starts: Optional[int] = None
    playing_time_min: Optional[int] = None
    playing_time_90s: Optional[float] = None
    performance_ga: Optional[int] = None
    performance_ga90: Optional[float] = None
    performance_sota: Optional[int] = None
    performance_saves: Optional[int] = None
    performance_save_pct: Optional[float] = None
    performance_w: Optional[int] = None
    performance_d: Optional[int] = None
    performance_l: Optional[int] = None
    performance_cs: Optional[int] = None
    performance_cs_pct: Optional[float] = None
    penalty_kicks_pkatt: Optional[int] = None
    penalty_kicks_pka: Optional[int] = None
    penalty_kicks_pksv: Optional[int] = None
    penalty_kicks_pkm: Optional[int] = None
    penalty_kicks_save_pct: Optional[float] = None