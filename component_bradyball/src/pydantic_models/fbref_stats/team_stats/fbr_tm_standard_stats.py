from pydantic import BaseModel, validator

class FbrTmStandardStats(BaseModel):
    team_id: int
    players_used: int
    average_age: float
    possession_pct: float
    playing_time_mp: int
    playing_time_starts: int
    playing_time_min: int
    playing_time_90s: float
    performance_gls: int
    performance_ast: int
    performance_g_a: float
    performance_g_pk: int
    performance_pk: int
    performance_pkatt: int
    performance_crd_y: int
    performance_crd_r: int
    expected_xg: float
    expected_npxg: float
    expected_xag: float
    expected_npxg_xag: float
    progression_prgc: int
    progression_prgp: int
    per_90_minutes_gls: float
    per_90_minutes_ast: float
    per_90_minutes_g_a: float
    per_90_minutes_g_pk: float
    per_90_minutes_g_a_pk: float
    per_90_minutes_xg: float
    per_90_minutes_xag: float
    per_90_minutes_xg_xag: float
    per_90_minutes_npxg: float
    per_90_minutes_npxg_xag: float
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