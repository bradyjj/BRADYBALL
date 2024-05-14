from pydantic import BaseModel, validator

class FbrTmMiscStats(BaseModel):
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
    
    @validator('team_id', pre=True)
    def extract_team_id(cls, v):
        if v:
            # Extract team_id from the URL
            parts = v.split('/')
            for part in parts:
                if len(part) == 8:  # Assuming team_id is always 8 characters long
                    return int(part, 16)  # Convert hexadecimal string to integer
        raise ValueError('Invalid URL format')