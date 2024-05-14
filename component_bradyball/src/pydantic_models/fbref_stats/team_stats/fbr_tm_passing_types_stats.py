from pydantic import BaseModel, validator

class FbrTmPassingTypesStats(BaseModel):
    team_id: int
    players_used: int
    minutes_90s: float
    total_att: int
    pass_types_live: int
    pass_types_dead: int
    pass_types_fk: int
    pass_types_tb: int
    pass_types_sw: int
    pass_types_crs: int
    pass_types_ti: int
    pass_types_ck: int
    corner_kicks_in: int
    corner_kicks_out: int
    corner_kicks_str: int
    outcomes_cmp: int
    outcomes_off: int
    outcomes_blocks: int
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