from pydantic import BaseModel, validator

class FbrTmKeeperStats(BaseModel):
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
    
    @validator('team_id', pre=True)
    def extract_team_id(cls, v):
        if v:
            # Extract team_id from the URL
            parts = v.split('/')
            for part in parts:
                if len(part) == 8:  # Assuming team_id is always 8 characters long
                    return int(part, 16)  # Convert hexadecimal string to integer
        raise ValueError('Invalid URL format')