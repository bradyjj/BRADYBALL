from pydantic import BaseModel, validator

class FbrTmPassingStats(BaseModel):
    team_id: int
    league: str
    season: str
    team: str
    players_used: int
    minutes_90s: float
    total_cmp: int
    total_att: int
    total_cmp_pct: float
    total_tot_dist: int
    total_prg_dist: int
    short_cmp: int
    short_att: int
    short_cmp_pct: float
    medium_cmp: int
    medium_att: int
    medium_cmp_pct: float
    long_cmp: int
    long_att: int
    long_cmp_pct: float
    ast: int
    xag: float
    expected_xa: float
    expected_a_xag: float
    kp: int
    passes_into_final_third: int
    ppa: int
    crspa: int
    prog_passes: int
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