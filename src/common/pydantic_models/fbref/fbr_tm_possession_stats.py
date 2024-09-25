from typing import Optional
from pydantic import BaseModel

class FbrTmPossessionStats(BaseModel):
    team_id: str
    team: str
    season: str
    league: Optional[str] = None
    players_used: Optional[int] = None
    possession_pct: Optional[float] = None
    minutes_90s: Optional[float] = None
    touches_total: Optional[int] = None
    touches_def_pen: Optional[int] = None
    touches_def_3rd: Optional[int] = None
    touches_mid_3rd: Optional[int] = None
    touches_att_3rd: Optional[int] = None
    touches_att_pen: Optional[int] = None
    touches_live: Optional[int] = None
    take_ons_att: Optional[int] = None
    take_ons_succ: Optional[int] = None
    take_ons_succ_pct: Optional[float] = None
    take_ons_tkld: Optional[int] = None
    take_ons_tkld_pct: Optional[float] = None
    carries_total: Optional[int] = None
    carries_tot_dist: Optional[int] = None
    carries_prg_dist: Optional[int] = None
    carries_prgc: Optional[int] = None
    carries_1_3: Optional[int] = None
    carries_cpa: Optional[int] = None
    carries_mis: Optional[int] = None
    carries_dis: Optional[int] = None
    receiving_rec: Optional[int] = None
    receiving_prg_r: Optional[int] = None
    url: str