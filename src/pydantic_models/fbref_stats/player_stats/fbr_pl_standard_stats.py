from typing import Optional
from pydantic import BaseModel


class FbrPlStandardStats(BaseModel):
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
    progression_prgr: Optional[int] = None
    p90_gls: Optional[float] = None
    p90_ast: Optional[float] = None
    p90_g_a: Optional[float] = None
    p90_g_pk: Optional[float] = None
    p90_g_a_pk: Optional[float] = None
    p90_xg: Optional[float] = None
    p90_xag: Optional[float] = None
    p90_xg_xag: Optional[float] = None
    p90_npxg: Optional[float] = None
    p90_npxg_xag: Optional[float] = None
