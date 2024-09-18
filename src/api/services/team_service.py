from sqlalchemy.orm import Session
from models.team import Team

def get_team(db: Session, team_id: str):
    return db.query(Team).filter(Team.team_id == team_id).first()

def list_teams(db: Session, skip: int = 0, limit: int = 100):
    return db.query(Team).offset(skip).limit(limit).all()