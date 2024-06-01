from typing import Optional
from pydantic import BaseModel


class FbrPlMiscStats(BaseModel):
    league: str
    season: str
    team: str
    player: str
    nation: Optional[str] = None
    position: Optional[str] = None
    age: Optional[int] = None
    born: Optional[int] = None
    minutes_90s: Optional[float] = None
    performance_crdy: Optional[int] = None
    performance_crdr: Optional[int] = None
    performance_2crdy: Optional[int] = None
    performance_fls: Optional[int] = None
    performance_fld: Optional[int] = None
    performance_off: Optional[int] = None
    performance_crs: Optional[int] = None
    performance_int: Optional[int] = None
    performance_tklw: Optional[int] = None
    performance_pkwon: Optional[int] = None
    performance_pkcon: Optional[int] = None
    performance_og: Optional[int] = None
    performance_recov: Optional[int] = None
    aerial_duels_won: Optional[int] = None
    aerial_duels_lost: Optional[int] = None
    aerial_duels_won_pct: Optional[float] = None
