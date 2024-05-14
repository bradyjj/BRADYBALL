from pydantic import BaseModel, validator

class FbrTmPlayingTimeStats(BaseModel):
    team_id: int
    players_used: int
    average_age: float
    playing_time_mp: int
    playing_time_min: int
    playing_time_mn_per_mp: float
    playing_time_min_pct: float
    playing_time_90s: float
    starts_starts: int
    starts_mn_per_start: float
    starts_compl: int
    subs_subs: int
    subs_mn_per_sub: float
    subs_unsub: int
    team_success_ppm: float
    team_success_ong: int
    team_success_onga: int
    team_success_plus_minus: int
    team_success_plus_minus_per_90: float
    team_success_xg_ongxg: float
    team_success_xg_ongxga: float
    team_success_xg_xg_plus_minus: float
    team_success_xg_xg_plus_minus_per_90: float
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