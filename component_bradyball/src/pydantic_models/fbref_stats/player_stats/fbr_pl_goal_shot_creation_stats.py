from pydantic import BaseModel, validator

class FbrPlGoalShotCreationStats(BaseModel):
    team_id: int
    players_used: int
    minutes_90s: float
    sca_total: int
    sca_per_90: float
    sca_types_pass_live: int
    sca_types_pass_dead: int
    sca_types_to: int
    sca_types_sh: int
    sca_types_fld: int
    sca_types_def: int
    gca_total: int
    gca_per_90: float
    gca_types_pass_live: int
    gca_types_pass_dead: int
    gca_types_to: int
    gca_types_sh: int
    gca_types_fld: int
    gca_types_def: int
    url: str