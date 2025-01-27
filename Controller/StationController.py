from config import db
from Model import Station

class StationController():
    @staticmethod
    def insert_station(data):
        try:
            station = Station(name=data['name'],latitude=data['latitude'],longitude=data['longitude'])
            db.session.add(station)
            db.session.commit()
            return {'id':station.id,
                    'name':station.name,
                    'latitude':station.latitude,
                    'longitude':station.longitude,
                    'num_drones':station.num_drones}
        except Exception as e:
            print(e)
            return {}

    @staticmethod
    def get_all_stations():
        try:
            stations = Station.query.filter_by(validity=1).all()
            if stations:
                return [{'id':s.id,'name':s.name,'latitude':s.latitude,'longitude':s.longitude,'num_drones':s.num_drones} for s in stations]
            else:
                return []
        except Exception as e:
            print(e)
            return []


    @staticmethod
    def get_station_by_id(station_id):
        try:
            station = Station.query.filter_by(id=station_id,validity=1).first()
            if station:
                return {'id':station.id,'name':station.name,'latitude':station.latitude,'longitude':station.longitude,'num_drones':station.num_drones}
            else:
                return {}
        except Exception as e:
            print(e)
            return {}

    #Helper Function
    @staticmethod
    def increment_num_drones(station_id):
        station = Station.query.get(station_id)
        if station:
            station.num_drones = station.num_drones + 1
            db.session.commit()
            return True
        return False

    #Helper Function
    @staticmethod
    def decrement_num_drones(station_id):
        station = Station.query.get(station_id)
        if station and station.num_drones > 0:
            station.num_drones = station.num_drones - 1
            db.session.commit()
            return True
        return False

    @staticmethod
    def update_station_by_id(data):
        try:
            station = Station.query.filter_by(id=data['id'],validity=1).first()
            if station:
                station.name = data.get('name',station.name)
                station.latitude = data.get('latitude',station.latitude)
                station.longitude = data.get('longitude',station.longitude)
                db.session.commit()
                return {'id':station.id,'name':station.name,'latitude':station.latitude,'longitude':station.longitude,'num_drones':station.num_drones}
            else:
                return {}
        except Exception as e:
            print(e)
            return {}

    @staticmethod
    def delete_station_by_id(id):
        try:
            station = Station.query.filter_by(id=id,validity=1).first()
            if station and station.num_drones == 0:
                station.validity = 0
                db.session.commit()
                return {'id':station.id,'name':station.name,'latitude':station.latitude,'longitude':station.longitude,'num_drones':station.num_drones}
            else:
                return {}
        except Exception as e:
            print(e)
            return {}

