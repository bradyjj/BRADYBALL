from typing import Optional
from pydantic import BaseModel


class FbrPlPassingStats(BaseModel):
    league: str
    season: str
    team: str
    player: str
    nation: Optional[str] = None
    position: Optional[str] = None
    age: Optional[int] = None
    born: Optional[int] = None
    minutes_90s: Optional[float] = None
    total_cmp: Optional[int] = None
    total_att: Optional[int] = None
    total_cmp_pct: Optional[float] = None
    total_tot_dist: Optional[int] = None
    total_prg_dist: Optional[int] = None
    short_cmp: Optional[int] = None
    short_att: Optional[int] = None
    short_cmp_pct: Optional[float] = None
    medium_cmp: Optional[int] = None
    medium_att: Optional[int] = None
    medium_cmp_pct: Optional[float] = None
    long_cmp: Optional[int] = None
    long_att: Optional[int] = None
    long_cmp_pct: Optional[float] = None
    ast: Optional[int] = None
    xag: Optional[float] = None
    expected_xa: Optional[float] = None
    expected_a_xag: Optional[float] = None
    kp: Optional[int] = None
    passes_into_final_third: Optional[int] = None
    ppa: Optional[int] = None
    crspa: Optional[int] = None
    prog_passes: Optional[int] = None
