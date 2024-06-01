from typing import Optional
from pydantic import BaseModel


class FbrPlPassingTypesStats(BaseModel):
    league: str
    season: str
    team: str
    player: str
    nation: Optional[str] = None
    position: Optional[str] = None
    age: Optional[int] = None
    born: Optional[int] = None
    minutes_90s: Optional[float] = None
    att: Optional[int] = None
    pass_types_live: Optional[int] = None
    pass_types_dead: Optional[int] = None
    pass_types_fk: Optional[int] = None
    pass_types_tb: Optional[int] = None
    pass_types_sw: Optional[int] = None
    pass_types_crs: Optional[int] = None
    pass_types_ti: Optional[int] = None
    pass_types_ck: Optional[int] = None
    corner_kicks_in: Optional[int] = None
    corner_kicks_out: Optional[int] = None
    corner_kicks_str: Optional[int] = None
    outcomes_cmp: Optional[int] = None
    outcomes_off: Optional[int] = None
    outcomes_blocks: Optional[int] = None
