from typing import Optional
from pydantic import BaseModel

class FbrTmKeeperAdvStats(BaseModel):
    team_id: str
    team: str
    season: str
    league: Optional[str] = None
    players_used: Optional[int] = None
    minutes_90s: Optional[float] = None
    goals_ga: Optional[int] = None
    goals_pka: Optional[int] = None
    goals_fk: Optional[int] = None
    goals_ck: Optional[int] = None
    goals_og: Optional[int] = None
    expected_psxg: Optional[float] = None
    expected_psxg_sot: Optional[float] = None
    expected_psxg_plus_minus: Optional[float] = None
    expected_per_90: Optional[float] = None
    launched_cmp: Optional[int] = None
    launched_att: Optional[int] = None
    launched_cmp_pct: Optional[float] = None
    passes_att_gk: Optional[int] = None
    passes_thr: Optional[int] = None
    passes_launch_pct: Optional[float] = None
    passes_avg_len: Optional[float] = None
    goal_kicks_att: Optional[int] = None
    goal_kicks_launch_pct: Optional[float] = None
    goal_kicks_avg_len: Optional[float] = None
    crosses_opp: Optional[int] = None
    crosses_stp: Optional[int] = None
    crosses_stp_pct: Optional[float] = None
    sweeper_opa: Optional[int] = None
    sweeper_opa_per_90: Optional[float] = None
    sweeper_avg_dist: Optional[float] = None
    url: str