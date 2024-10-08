from typing import Optional
from pydantic import BaseModel


class FbrPlGoalShotCreationStats(BaseModel):
    league: str
    season: str
    team: str
    player: str
    nation: Optional[str] = None
    position: Optional[str] = None
    age: Optional[int] = None
    born: Optional[int] = None
    minutes_90s: Optional[float] = None
    sca_total: Optional[int] = None
    sca_per_90: Optional[float] = None
    sca_types_pass_live: Optional[int] = None
    sca_types_pass_dead: Optional[int] = None
    sca_types_to: Optional[int] = None
    sca_types_sh: Optional[int] = None
    sca_types_fld: Optional[int] = None
    sca_types_def: Optional[int] = None
    gca_total: Optional[int] = None
    gca_per_90: Optional[float] = None
    gca_types_pass_live: Optional[int] = None
    gca_types_pass_dead: Optional[int] = None
    gca_types_to: Optional[int] = None
    gca_types_sh: Optional[int] = None
    gca_types_fld: Optional[int] = None
    gca_types_def: Optional[int] = None
