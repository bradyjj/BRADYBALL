from pydantic import BaseModel, validator

class FbrPlMiscStats(BaseModel):
    team_id: int
    players_used: int
    minutes_90s: float
    performance_crdy: int
    performance_crdr: int
    performance_2crdy: int
    performance_fls: int
    performance_fld: int
    performance_off: int
    performance_crs: int
    performance_int: int
    performance_tklw: int
    performance_pkwon: int
    performance_pkcon: int
    performance_og: int
    performance_recov: int
    aerial_duels_won: int
    aerial_duels_lost: int
    aerial_duels_won_pct: float
    url: str