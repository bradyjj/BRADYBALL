from pydantic import BaseModel, validator

class FbrPlPassingTypesStats(BaseModel):
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