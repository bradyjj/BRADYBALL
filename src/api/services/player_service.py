from sqlalchemy.orm import Session
from models.player import Player

def get_player(db: Session, player_id: str):
    return db.query(Player).filter(Player.player_id == player_id).first()

def list_players(db: Session, skip: int = 0, limit: int = 100):
    return db.query(Player).offset(skip).limit(limit).all()