from typing import Optional
from pydantic import BaseModel


class FbrPlShootingStats(BaseModel):
    league: str
    season: str
    team: str
    player: str
    nation: Optional[str] = None
    position: Optional[str] = None    
    age: Optional[int] = None
    born: Optional[int] = None
    minutes_90s: Optional[float] = None
    standard_gls: Optional[int] = None
    standard_sh: Optional[int] = None
    standard_sot: Optional[int] = None
    standard_sot_pct: Optional[float] = None
    standard_sh_per_90: Optional[float] = None
    standard_sot_per_90: Optional[float] = None
    standard_g_sh: Optional[float] = None
    standard_g_sot: Optional[float] = None
    standard_dist: Optional[float] = None
    standard_fk: Optional[int] = None
    standard_pk: Optional[int] = None
    standard_pkatt: Optional[int] = None
    expected_xg: Optional[float] = None
    expected_npxg: Optional[float] = None
    expected_npxg_per_sh: Optional[float] = None
    expected_g_xg: Optional[float] = None
    expected_np_g_xg: Optional[float] = None
