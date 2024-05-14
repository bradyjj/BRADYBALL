from pydantic import BaseModel, validator

class FbrTmShootingStats(BaseModel):
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
    
    @validator('team_id', pre=True)
    def extract_team_id(cls, v):
        if v:
            # Extract team_id from the URL
            parts = v.split('/')
            for part in parts:
                if len(part) == 8:  # Assuming team_id is always 8 characters long
                    return int(part, 16)  # Convert hexadecimal string to integer
        raise ValueError('Invalid URL format')