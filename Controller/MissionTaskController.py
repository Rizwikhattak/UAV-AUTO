from Model import MissionTask,MissionPlanner
from config import db

class MissionTaskController():
    @staticmethod
    def insert_mission_task(data):
        try:
            mission_planner = MissionPlanner.query.filter_by(id=data.get('mission_planner_id')).first()
            mission_task = MissionTask(mission_planner_id = data.get('mission_planner_id'), route_id = data.get('route_id'),description=data.get('description'))
            db.session.add(mission_task)
            db.session.commit()
            mission_planner.status = 'active'
            db.session.commit()
            return {
                "id":mission_task.id,
                "mission_planner_id":mission_task.mission_planner_id,
                "route_id":mission_task.route_id,
                "description":mission_task.description
            }
        except Exception as e:
            return {}

    @staticmethod
    def get_all_mission_tasks():
        try:
            mission_tasks = MissionTask.query.filter_by(validity=1).all()
            if mission_tasks:
                return [{
                    "id":mission_task.id,
                    "mission_planner_id":mission_task.mission_planner_id,
                    "route_id":mission_task.route_id,
                    "description":mission_task.description
                } for mission_task in mission_tasks]
            else:
                return []
        except Exception as e:
            print(e)
            return []

    @staticmethod
    def get_mission_task_by_id(id):
        try:
            mission_task = MissionTask.query.filter_by(id=id, validity=1).first()
            if mission_task:
                return {
                    "id":mission_task.id,
                    "mission_planner_id":mission_task.mission_planner_id,
                    "route_id":mission_task.route_id,
                    "description":mission_task.description
                }
            else:
                return {}
        except Exception as e:
            print(e)
            return {}

    @staticmethod
    def update_mission_task(data):
        try:
            mission_task = MissionTask.query.filter_by(id=data.get('id'),validity=1).first()
            if mission_task:
                mission_task.mission_planner_id = data.get('mission_planner_id')
                mission_task.route_id = data.get('route_id')
                mission_task.description = data.get('description')
                db.session.commit()
                return {
                    "id":mission_task.id,
                    "mission_planner_id":mission_task.mission_planner_id,
                    "route_id":mission_task.route_id,
                    "description":mission_task.description
                }
            else:
                return {}
        except Exception as e:
            print(e)
            return {}

    @staticmethod
    def delete_mission_task(id):
        try:
            mission_task = MissionTask.query.filter_by(id=id,validity=1).first()
            mission_planner = MissionPlanner.query.filter_by(id=mission_task.mission_planner_id, validity=1).first()
            if mission_planner:
                mission_planner.status = 'not set'
                db.session.commit()
            if mission_task:
                mission_task.validity = 0
                db.session.commit()
                return {
                    "id":mission_task.id,
                    "mission_planner_id":mission_task.mission_planner_id,
                    "route_id":mission_task.route_id,
                    "description":mission_task.description
                }
            else:
                return {}
        except Exception as e:
            print(e)
            return {}
