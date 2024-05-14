from pydantic import BaseModel, validator

class FbrPlDefenseStats(BaseModel):
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