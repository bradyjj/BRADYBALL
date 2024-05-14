from pydantic import BaseModel, validator

class FbrPlShootingStats(BaseModel):
    team_id: int
    players_used: int
    minutes_90s: float
    standard_gls: int
    standard_sh: int
    standard_sot: int
    standard_sot_pct: float
    standard_sh_per_90: float
    standard_sot_per_90: float
    standard_g_sh: float
    standard_g_sot: float
    standard_dist: float
    standard_fk: int
    standard_pk: int
    standard_pkatt: int
    expected_xg: float
    expected_npxg: float
    expected_npxg_per_sh: float
    expected_g_xg: float
    expected_np_g_xg: float
    url: str