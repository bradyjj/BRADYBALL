from sqlalchemy import Column, Integer, String, Date, Float, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Player(Base):
    __tablename__ = 'players'

    id = Column(Integer, primary_key=True)
    player_id = Column(String, unique=True)
    name = Column(String)
    team = Column(String)
    league = Column(String)
    nation = Column(String)
    position = Column(String)
    age = Column(Integer)
    birthdate = Column(Date)
    hometown = Column(String)
    foot = Column(String)
    weight = Column(Float)
    height = Column(Float)
    strengths = Column(String)
    weaknesses = Column(String)

    trophy_cabinet = relationship("TrophyCabinet", back_populates="player")
    market_values = relationship("MarketValue", back_populates="player")
    season_data = relationship("SeasonData", back_populates="player")

class TrophyCabinet(Base):
    __tablename__ = 'trophy_cabinet'

    id = Column(Integer, primary_key=True)
    player_id = Column(Integer, ForeignKey('players.id'))
    competition = Column(String)
    trophies = Column(Integer)
    team = Column(String)
    seasons = Column(String)

    player = relationship("Player", back_populates="trophy_cabinet")

class MarketValue(Base):
    __tablename__ = 'market_values'

    id = Column(Integer, primary_key=True)
    player_id = Column(Integer, ForeignKey('players.id'))
    market_value = Column(Float)
    age = Column(Integer)
    date = Column(Date)
    team_name = Column(String)

    player = relationship("Player", back_populates="market_values")

class SeasonData(Base):
    __tablename__ = 'season_data'

    id = Column(Integer, primary_key=True)
    player_id = Column(Integer, ForeignKey('players.id'))
    season = Column(String)

    player = relationship("Player", back_populates="season_data")
    data_points = relationship("DataPoint", back_populates="season_data")

class DataPoint(Base):
    __tablename__ = 'data_points'

    id = Column(Integer, primary_key=True)
    season_data_id = Column(Integer, ForeignKey('season_data.id'))
    key = Column(String)
    value = Column(String)
    label = Column(String)
    scale = Column(String)

    season_data = relationship("SeasonData", back_populates="data_points")

def player_to_dict(player):
    return {
        "success": True,
        "header": None,
        "data": {
            "PlayerId": player.player_id,
            "Name": player.name,
            "Team": player.team,
            "League": player.league,
            "Nation": player.nation,
            "Position": player.position,
            "Age": player.age,
            "Birthdate": player.birthdate.isoformat() if player.birthdate else None,
            "Hometown": player.hometown,
            "Foot": player.foot,
            "Weight": player.weight,
            "Height": player.height,
            "TrophyCabinet": [
                {
                    "Competition": trophy.competition,
                    "Trophies": trophy.trophies,
                    "Team": trophy.team,
                    "Seasons": trophy.seasons
                } for trophy in player.trophy_cabinet
            ],
            "RecentMarketValue": [
                {
                    "MarketValue": value.market_value,
                    "Age": value.age,
                    "Date": value.date.isoformat() if value.date else None,
                    "TeamName": value.team_name
                } for value in player.market_values
            ],
            "Strengths": player.strengths,
            "Weaknesses": player.weaknesses,
            "Data": [
                {
                    "Season": season_data.season,
                    "DataPoints": [
                        {
                            "Key": point.key,
                            "Value": point.value,
                            "Label": point.label,
                            "Scale": point.scale
                        } for point in season_data.data_points
                    ]
                } for season_data in player.season_data
            ]
        }
    }