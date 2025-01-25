from Controller import MissionStationMappingControllerfrom config import dbfrom Model import MissionPlanner, MissionStationMapping, MissionTask, LocationPin, MissionDataLocation, \    MissionDataImage, Sortie, Drone,MissionVideo,DroneAvailabilityLogclass MissionPlannerController():    @staticmethod    def insert_mission_plan(data):        try:            mission_plan = MissionPlanner(                name=data.get('name'),                admin_id=data.get('admin_id'),                drone_id=data.get('drone_id'),                operator_id=data.get('operator_id'),                start_date=data.get('start_date'),                start_time=data.get('start_time'),                status=data.get('status')            )            db.session.add(mission_plan)            db.session.commit()            data['mission_planner_id'] = mission_plan.id            mission_station_mapping = MissionStationMappingController.insert_mission_station_mapping(data)            return {               "id": mission_plan.id,               "name": mission_plan.name,               "admin_id": mission_plan.admin_id,               "drone_id": mission_plan.drone_id,               "operator_id": mission_plan.operator_id,               "start_date": mission_plan.start_date,               "start_time": str(mission_plan.start_time),               "status": mission_plan.status,                "landing_station": mission_station_mapping.get('landing_station'),                "departure_station": mission_station_mapping.get('departure_station')            }        except Exception as e:            print(e)            return {}    @staticmethod    def update_mission_plan(data):        try:            mission_plan = MissionPlanner.query.filter_by(id=data.get('id'),validity=1).first()            mission_station_mapping = MissionStationMapping.query.filter_by(mission_planner_id = mission_plan.id,validity=1).first()            if mission_plan and mission_station_mapping:                mission_plan.name = data.get('name',mission_plan.name)                mission_plan.admin_id = data.get('admin_id',mission_plan.admin_id)                mission_plan.drone_id = data.get('drone_id',mission_plan.drone_id)                mission_plan.operator_id = data.get('operator_id',mission_plan.operator_id)                mission_plan.start_date = data.get('start_date',mission_plan.start_date)                mission_plan.start_time = data.get('start_time',mission_plan.admin_id)                mission_plan.status = data.get('status',mission_plan.status)                mission_station_mapping.landing_station = data.get('landing_station',mission_station_mapping.landing_station)                mission_station_mapping.departure_station = data.get('departure_station',mission_station_mapping.departure_station)                db.session.commit()                return {                    "id": mission_plan.id,                    "name": mission_plan.name,                    "admin_id": mission_plan.admin_id,                    "drone_id": mission_plan.drone_id,                    "operator_id": mission_plan.operator_id,                    "start_date": mission_plan.start_date,                    "start_time": str(mission_plan.start_time),                    "status": mission_plan.status,                    "landing_station": mission_station_mapping.landing_station,                    "departure_station": mission_station_mapping.departure_station                }            else:                return {}        except Exception as e:            print(e)            return {}    @staticmethod    def update_mission_status(data):        try:            mission_plan = MissionPlanner.query.filter_by(id=data.get('id'),validity=1).first()            if mission_plan.status == 'active':                drone_availability_log = DroneAvailabilityLog.query.filter_by(mission_planner_id = mission_plan.id, validity=1).first()                if drone_availability_log:                    drone_availability_log.validity=0                    db.session.commit()            if mission_plan:                mission_plan.status = data.get('status')                db.session.commit()                return {                    "id": mission_plan.id,                    "name": mission_plan.name,                    "admin_id": mission_plan.admin_id,                    "drone_id": mission_plan.drone_id,                    "operator_id": mission_plan.operator_id,                    "start_date": mission_plan.start_date,                    "start_time": str(mission_plan.start_time),                    "status": mission_plan.status                }            else:                return {}        except Exception as e:            print(e)            return {}    def delete_mission_plan(mission_planner_id):        try:            mission_plan = MissionPlanner.query.filter_by(id=mission_planner_id, validity=1).first()            if not mission_plan:                return {}            mission_plan.validity = 0            mission_station_mapping = MissionStationMapping.query.filter_by(mission_planner_id=mission_plan.id,validity=1).first()            if mission_station_mapping:                mission_station_mapping.validity = 0            drone_availability_log = DroneAvailabilityLog.query.filter_by(drone_id=mission_plan.drone_id,validity=1).first()            if drone_availability_log:                drone_availability_log.validity = 0            mission_task = MissionTask.query.filter_by(mission_planner_id=mission_plan.id, validity=1).first()            mission_task.validity = 0            mission_videos = MissionVideo.query.filter_by(mission_task_id = mission_task.id,validity=1).all()            if mission_videos:                for mission_video in mission_videos:                    mission_video.validity = 0                    mission_data_locations = MissionDataLocation.query.filter_by(mission_video=mission_video.id,validity=1).all()                    for mission_data_location in mission_data_locations:                        mission_data_location.validity = 0                        mission_data_images = MissionDataImage.query.filter_by(mission_data_location_id=mission_data_location.id,                                                                               validity=1).all()                        for mission_data_image in mission_data_images:                            mission_data_image.validity = 0            # Commit all changes to the database in one transaction            db.session.commit()            return {                        "id": mission_plan.id,                        "name": mission_plan.name,                        "admin_id": mission_plan.admin_id,                        "drone_id": mission_plan.drone_id,                        "operator_id": mission_plan.operator_id,                        "start_date": mission_plan.start_date,                        "start_time": str(mission_plan.start_time),                        "status": mission_plan.status,                        "landing_station": mission_station_mapping.landing_station,                        "departure_station": mission_station_mapping.departure_station                    }        except Exception as e:            print(e)            return {}    @staticmethod    def get_all_mission_plans():        try:            mission_plans = MissionPlanner.query.filter_by(validity=1).all()            if mission_plans:                return [{                    "id": mission_plan.id,                    "name": mission_plan.name,                    "admin_id": mission_plan.admin_id,                    "drone_id": mission_plan.drone_id,                    "operator_id": mission_plan.operator_id,                    "start_date": mission_plan.start_date,                    "start_time": str(mission_plan.start_time),                    "status": mission_plan.status                }  for mission_plan in mission_plans if mission_plan.status != 'completed' and mission_plan.status != 'aborted']            else:                return []        except Exception as e:            print(e)            return []    @staticmethod    def get_mission_plan_by_id(mission_plan_id):        try:            mission_plan = MissionPlanner.query.filter_by(id=mission_plan_id, validity=1).first()            if mission_plan:                return {                    "id": mission_plan.id,                    "name": mission_plan.name,                    "admin_id": mission_plan.admin_id,                    "drone_id": mission_plan.drone_id,                    "operator_id": mission_plan.operator_id,                    "start_date": mission_plan.start_date,                    "start_time": str(mission_plan.start_time),                    "status": mission_plan.status                }            else:                return {}        except Exception as e:            print(e)            return {}    @staticmethod    def get_history():        try:            missions_data = (            db.session.query(                MissionPlanner,                MissionTask,                MissionDataLocation,                MissionDataImage,                Sortie,                Drone,                MissionVideo,                MissionStationMapping            )            .join(MissionTask, MissionTask.mission_planner_id == MissionPlanner.id)            .join(MissionDataLocation, MissionDataLocation.mission_video_id == MissionVideo.id)            .join(MissionDataImage, MissionDataImage.mission_data_location_id == MissionDataLocation.id)            .join(Sortie, Sortie.mission_planner_id == MissionPlanner.id)            .join(Drone,MissionPlanner.drone_id==Drone.id)            .join(MissionStationMapping, MissionStationMapping.mission_planner_id == MissionPlanner.id)            .join(MissionVideo, MissionVideo.mission_task_id == MissionTask.id)            .filter(MissionPlanner.validity == 1, MissionTask.validity == 1, MissionVideo.validity == 1)            .all()            )            if missions_data:                return [{'id':mission_plan.id,'name':mission_plan.name,                         'admin_id':mission_plan.admin_id,'drone_id':mission_plan.drone_id,                         'operator_id':mission_plan.operator_id,'status':mission_plan.status,                         'mission_task_id':mission_task.id,'description':mission_task.description,                         'latitude':mission_data_location.latitude,'longitude':mission_data_location.longitude,                         "landing_station_id":mission_station_mapping.landing_station_id,"departure_station_id":mission_station_mapping.departure_station_id,                         'image_path':mission_data_image.image_path,'start_date':sortie.start_date,                         'end_date':sortie.end_date,'start_time':str(sortie.start_time),                         'end_time':str(sortie.end_time),'duration':sortie.duration,                         'drone_name':drone.name} for mission_plan,mission_task,mission_data_location,mission_data_image,sortie,drone,mission_station_mapping in missions_data if mission_plan.status == 'completed' or mission_plan.status == 'aborted']            else:                return []        except Exception as e:            print(e)            return []    @staticmethod    def delete_history():        try:            missions_data = (                db.session.query(                    MissionPlanner,                    MissionTask,                    MissionDataLocation,                    MissionDataImage,                    Sortie,                    Drone,                    MissionVideo,                    MissionStationMapping                )                .join(MissionTask, MissionTask.mission_planner_id == MissionPlanner.id)                .join(MissionDataLocation, MissionDataLocation.mission_video_id == MissionVideo.id)                .join(MissionDataImage, MissionDataImage.mission_data_location_id == MissionDataLocation.id)                .join(Sortie, Sortie.mission_planner_id == MissionPlanner.id)                .join(Drone, MissionPlanner.drone_id == Drone.id)                .join(MissionStationMapping, MissionStationMapping.mission_planner_id == MissionPlanner.id)                .join(MissionVideo, MissionVideo.mission_task_id == MissionTask.id)                .filter(MissionPlanner.validity == 1, MissionTask.validity == 1, MissionVideo.validity == 1)                .all()            )            if missions_data:                for mission_plan, mission_task, mission_data_location, mission_data_image, sortie, drone,mission_station_mapping,mission_video in missions_data:                    mission_plan.validity = 0                    mission_task.validity = 0                    mission_data_location.validity = 0                    mission_data_image.validity = 0                    sortie.validity = 0                    mission_video.validity = 0                    drone_availability_log = DroneAvailabilityLog.query.filter_by(drone_id=mission_plan.drone_id,validity=1).first()                    if drone_availability_log:                        drone_availability_log.validity = 0                    db.session.commit()                return [{'id': mission_plan.id, 'name': mission_plan.name,                         'admin_id': mission_plan.admin_id, 'drone_id': mission_plan.drone_id,                         'operator_id': mission_plan.operator_id, 'status': mission_plan.status,                         'mission_task_id': mission_task.id, 'description': mission_task.description,                         'latitude': mission_data_location.latitude, 'longitude': mission_data_location.longitude,                         'image_path': mission_data_image.image_path, 'start_date': sortie.start_date,                         'end_date': sortie.end_date, 'start_time': str(sortie.start_time),                         'end_time': str(sortie.end_time), 'duration': sortie.duration,                         'drone_name': drone.name} for                        mission_plan, mission_task, mission_data_location, mission_data_image, sortie, drone in                        missions_data]            else:                return []        except Exception as e:            print(e)            return []