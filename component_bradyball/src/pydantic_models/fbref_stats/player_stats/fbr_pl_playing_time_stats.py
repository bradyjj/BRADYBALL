from typing import Optional
from pydantic import BaseModel


class FbrPlPlayingTimeStats(BaseModel):
    league: str
    season: str
    team: str
    player: str
    nation: Optional[str] = None
    position: Optional[str] = None
    age: Optional[int] = None
    born: Optional[int] = None
    playing_time_mp: Optional[int] = None
    playing_time_min: Optional[int] = None
    playing_time_mn_per_mp: Optional[int] = None
    playing_time_min_pct: Optional[float] = None
    minutes_90s: Optional[float] = None
    starts_starts: Optional[int] = None
    starts_mn_per_start: Optional[int] = None
    starts_compl: Optional[int] = None
    subs_subs: Optional[int] = None
    subs_mn_per_sub: Optional[int] = None
    subs_unsub: Optional[int] = None
    team_success_ppm: Optional[float] = None
    team_success_ong: Optional[int] = None
    team_success_onga: Optional[int] = None
    team_success_plus_minus: Optional[int] = None
    team_success_plus_minus_per_90: Optional[float] = None
    team_success_on_off: Optional[float] = None
    team_success_xg_ongxg: Optional[float] = None
    team_success_xg_ongxga: Optional[float] = None
    team_success_xg_plus_minus: Optional[float] = None
    team_success_xg_plus_minus_per_90: Optional[float] = None
    team_success_xg_on_off: Optional[float] = None
