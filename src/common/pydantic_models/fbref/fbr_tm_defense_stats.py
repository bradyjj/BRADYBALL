from typing import Optional
from pydantic import BaseModel

class FbrTmDefenseStats(BaseModel):
    team_id: str
    team: str
    season: str
    league: Optional[str] = None
    players_used: Optional[int] = None
    minutes_90s: Optional[float] = None
    tackles_tkl: Optional[int] = None
    tackles_tklw: Optional[int] = None
    tackles_def_3rd: Optional[int] = None
    tackles_mid_3rd: Optional[int] = None
    tackles_att_3rd: Optional[int] = None
    challenges_tkl: Optional[int] = None
    challenges_att: Optional[int] = None
    challenges_tkl_pct: Optional[float] = None
    challenges_lost: Optional[int] = None
    blocks_blocks: Optional[int] = None
    blocks_sh: Optional[int] = None
    blocks_pass: Optional[int] = None
    interceptions: Optional[int] = None
    tackles_plus_interceptions: Optional[int] = None
    clearances: Optional[int] = None
    errors: Optional[int] = None
    url: str