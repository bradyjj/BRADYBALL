from sqlalchemy import Column, Integer, String, Date, Float, ForeignKey, JSON
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Team(Base):
    __tablename__ = 'teams'

    id = Column(Integer, primary_key=True)
    team_id = Column(String, unique=True)
    team_name = Column(String)
    league = Column(String)
    nation = Column(String)
    stadium = Column(String)
    hometown = Column(String)
    birthdate = Column(Date)
    squad_size = Column(Integer)
    foreigners = Column(Integer)
    homegrown_players = Column(Integer)
    average_age = Column(Float)
    manager = Column(String)
    current_transfer_record = Column(String)
    recent_market_value = Column(Float)

    team_colors = relationship("TeamColors", uselist=False, back_populates="team")
    trophy_cabinet = relationship("TeamTrophyCabinet", back_populates="team")
    season_data = relationship("TeamSeasonData", back_populates="team")

class TeamColors(Base):
    __tablename__ = 'team_colors'

    id = Column(Integer, primary_key=True)
    team_id = Column(Integer, ForeignKey('teams.id'), unique=True)
    primary_badge_color = Column(String)
    secondary_badge_color = Column(String)
    third_badge_color = Column(String)
    fourth_badge_color = Column(String)
    fifth_badge_color = Column(String)
    primary_team_color = Column(String)
    secondary_team_color = Column(String)
    third_team_color = Column(String)
    fourth_team_color = Column(String)
    fifth_team_color = Column(String)

    team = relationship("Team", back_populates="team_colors")

class TeamTrophyCabinet(Base):
    __tablename__ = 'team_trophy_cabinet'

    id = Column(Integer, primary_key=True)
    team_id = Column(Integer, ForeignKey('teams.id'))
    competition = Column(String)
    trophies = Column(Integer)
    seasons = Column(String)

    team = relationship("Team", back_populates="trophy_cabinet")

class TeamSeasonData(Base):
    __tablename__ = 'team_season_data'

    id = Column(Integer, primary_key=True)
    team_id = Column(Integer, ForeignKey('teams.id'))
    season = Column(String)

    team = relationship("Team", back_populates="season_data")
    data_points = relationship("TeamDataPoint", back_populates="season_data")

class TeamDataPoint(Base):
    __tablename__ = 'team_data_points'

    id = Column(Integer, primary_key=True)