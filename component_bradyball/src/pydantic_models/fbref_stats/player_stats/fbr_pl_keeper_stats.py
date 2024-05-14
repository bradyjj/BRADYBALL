from pydantic import BaseModel, validator

class FbrPlKeeperStats(BaseModel):
    team_id: int
    players_used: int
    playing_time_mp: int
    playing_time_starts: int
    playing_time_min: int
    playing_time_90s: float
    performance_ga: int
    performance_ga90: float
    performance_sota: int
    performance_saves: int
    performance_save_pct: float
    performance_w: int
    performance_d: int
    performance_l: int
    performance_cs: int
    performance_cs_pct: float
    penalty_kicks_pkatt: int
    penalty_kicks_pka: int
    penalty_kicks_pksv: int
    penalty_kicks_pkm: int
    penalty_kicks_save_pct: float
    url: str