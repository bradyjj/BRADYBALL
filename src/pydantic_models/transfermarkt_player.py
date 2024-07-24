from datetime import datetime
from typing import List, Optional
from pydantic import BaseModel

class TransfermarktPlayer(BaseModel):
    player_id: int
    player_name: str
    competition_name: str
    url: str
    age: Optional[int] = None
    date_of_birth: Optional[str] = None
    shirt_no: Optional[str] = None
    team_name: Optional[str] = None
    position: Optional[str] = None
    contract_start_date: Optional[str] = None
    contract_expiry_date: Optional[str] = None
    foot: Optional[str] = None
    agent: Optional[str] = None
    outfitter: Optional[str] = None
    citizenship: Optional[str] = None
    birthplace: Optional[str] = None
    market_value: Optional[List[dict]] = None
    transfer_history: Optional[List[dict]] = None