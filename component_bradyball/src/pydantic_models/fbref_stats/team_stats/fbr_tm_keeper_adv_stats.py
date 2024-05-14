from pydantic import BaseModel, validator

class FbrTmKeeperAdvStats(BaseModel):
    team_id: int
    players_used: int
    minutes_90s: float
    goals_ga: int
    goals_pka: int
    goals_fk: int
    goals_ck: int
    goals_og: int
    expected_psxg: float
    expected_psxg_sot: float
    expected_psxg_plus_minus: float
    expected_per_90: float
    launched_cmp: int
    launched_att: int
    launched_cmp_pct: float
    passes_att_gk: int
    passes_thr: int
    passes_launch_pct: float
    passes_avg_len: float
    goal_kicks_att: int
    goal_kicks_launch_pct: float
    goal_kicks_avg_len: float
    crosses_opp: int
    crosses_stp: int
    crosses_stp_pct: float
    sweeper_opa: int
    sweeper_opa_per_90: float
    sweeper_avg_dist: float
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