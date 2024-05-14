from pydantic import BaseModel, validator

class FbrTmPossessionStats(BaseModel):
    team_id: int
    players_used: int
    possession_pct: float
    minutes_90s: float
    touches_total: int
    touches_def_pen: int
    touches_def_3rd: int
    touches_mid_3rd: int
    touches_att_3rd: int
    touches_att_pen: int
    touches_live: int
    take_ons_att: int
    take_ons_succ: int
    take_ons_succ_pct: float
    take_ons_tkld: int
    take_ons_tkld_pct: float
    carries_total: int
    carries_tot_dist: int
    carries_prg_dist: int
    carries_prgc: int
    carries_1_3: int
    carries_cpa: int
    carries_mis: int
    carries_dis: int
    receiving_rec: int
    receiving_prg_r: int
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