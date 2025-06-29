"""SQLAlchemy Query Functions"""

from sqlalchemy.orm import Session
from sqlalchemy.orm import joinedload
from datetime import date

import models

def get_player(db:Session,player_id:int):
    return db.query(models.Player).filter(
        models.Player.player_id==player_id).first()

def get_players(db:Session,skip:int=0,limit:int=100,min_last_changed_date:date=None,last_name:str=None,first_name:str=None,):
    query=db.query(models.Player)
    if min_last_changed_date:
        query=query.filter(models.Player.last_changed_date>=min_last_changed_date)
    if first_name:
        query=query.filter(models.Player.first_name==first_name)
    if last_name:
        query=query.filter(models.Player.last_name==last_name)
    return query.offset(skip).limit(limit).all()

def get_performances(db:Session,skip:int=0,limit:int=100,min_last_changed_date:date=None):
    query=db.query(models.Performance)

    if min_last_changed_date:
        query=query.filter(models.Performance.last_changed_date>=min_last_changed_date)
    return query.offset(skip).limit(limit).all()



