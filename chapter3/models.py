"""SQLAlchemy models"""

from sqlalchemy import Column, ForeignKey, Integer, String,Float,Date
from sqlalchemy.orm import relationship
from database import Base

class Player(Base):
    __tablename__="player"

    player_id=Column(Integer, primary_key=True, index=True)
    gsis_id=Column(String,nullable=True)
    first_name=Column(String,nullable=False)
    last_name=Column(String,nullable=False)
    position=Column(String,nullable=False)
    last_changed_date=Column(Date,nullable=False)

    performances=relationship("Performance",back_populates="player")

    #Many-to-Many relationship between player and Team Tables
    teams=relationship("Team", secondary="team_player",back_populates="players")

class Performance(Base):


    __tablename__="performance"

    performance_id=Column(Integer,primary_key=True,index=True)
    week_number=Column(String,nullable=False)
    fantasy_points=Column(Float,nullable=False)
    last_changed_date=Column(Date,nullable=False)

    player_id=Column(Integer,ForeignKey("player.player_id"))
    player=relationship("Player",back_populates="performaces")

class League(Base):
    __tablename__="team"

    team_id=Column(Integer,primary_key=True,index=True)
    team_name=Column(String,nullable=False)
    last_changed_date=Column(Date,nullable=False)

    league_id=Column(Integer,ForeignKey("league.league_id"))

    league=relationship("League",back_populates="teams")

class Team(Base):
    __tablename__="team"

    team_id=Column(Integer,primary_key=True,index=True)
    team_name=Column(String,nullable=False)
    last_changed_date=Column(Date,nullable=False)

    league_id=Column(Integer,ForeignKey("league.league_id"))

    league=relationship("League",back_populates="teams")

    player=relationship("Player",secondary="team_player",back_populates="teams")

    class TeamPlayer(Base):
        __tablename__="team_player"
