from pydantic import BaseModel

class WhoscoredPlayer(BaseModel):
    player_id: int
    shirt_no: int
    name: str
    age: int
    position: str
    team_id: int
    height: int
    weight: int