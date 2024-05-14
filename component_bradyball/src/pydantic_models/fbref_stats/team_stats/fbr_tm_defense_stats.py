from pydantic import BaseModel, validator

class FbrTmDefenseStats(BaseModel):
    team_id: int
    players_used: int
    minutes_90s: float
    tackles_tkl: int
    tackles_tklw: int
    tackles_def_3rd: int
    tackles_mid_3rd: int
    tackles_att_3rd: int
    challenges_tkl: int
    challenges_att: int
    challenges_tkl_pct: float
    challenges_lost: int
    blocks_blocks: int
    blocks_sh: int
    blocks_pass: int
    interceptions: int
    tackles_plus_interceptions: int
    clearances: int
    errors: int
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