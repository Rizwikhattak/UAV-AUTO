from config import db
from Model import Sortie

class SortieController():
    @staticmethod
    def insert_sortie(data):
        sortie=Sortie(mission_planner_id = data['mission_planner_id'],start_date=data['start_date'],end_date=data['end_date'],start_time=data['start_time'],end_time=data['end_time'],duration=data['duration'])
        db.session.add(sortie)
        db.session.commit()
        return sortie