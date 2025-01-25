from Model import LocationPin
from config import db

class LocationPinController():
    @staticmethod
    def insert_location_pins(data):
        try:
            location_pin = LocationPin(route_id = data['route_id'],latitude = data['latitude'],longitude = data['longitude'])
            db.session.add(location_pin)
            db.session.commit()
            return {'id':location_pin.id,'route_id':location_pin.route_id,'latitude':location_pin.latitude,'longitude':location_pin.longitude}
        except Exception as e:
            print(e)
            return {}

    @staticmethod
    def get_location_pins():
        try:
            location_pins = LocationPin.query.filter_by(validity=1).all()
            if location_pins:
                return [{'id':l.id,'route_id':l.route_id,'latitude':l.latitude,'longitude':l.longitude} for l in location_pins]
            else:
                return {}
        except Exception as e:
            print(e)
            return {}

    @staticmethod
    def get_location_pin_by_id(location_id):
        try:
            location_pin = LocationPin.query.filter_by(id=location_id,validity=1).first()
            if location_pin:
                return {'id':location_pin.id,'route_id':location_pin.route_id,'latitude':location_pin.latitude,'longitude':location_pin.longitude}
            else:
                return {}
        except Exception as e:
            print(e)
            return {}

    @staticmethod
    def update_location_pin(data):
        try:
            location_pin = LocationPin.query.filter_by(id=data.get('id'),validity=1).first()
            if location_pin:
                location_pin.latitude = data.get('latitude')
                location_pin.longitude = data.get('longitude')
                db.session.commit()
                return {'id':location_pin.id,'route_id':location_pin.route_id,'latitude':location_pin.latitude,'longitude':location_pin.longitude}
            else:
                return {}
        except Exception as e:
            print(e)
            return {}

    @staticmethod
    def delete_location_pin(location_id):
        try:
            location_pin = LocationPin.query.filter_by(id=location_id,validity=1).first()
            if location_pin:
                location_pin.validity = 0
                db.session.commit()
                return {'id':location_pin.id,'route_id':location_pin.route_id,'latitude':location_pin.latitude,'longitude':location_pin.longitude}
            else:
                return {}
        except Exception as e:
            print(e)
            return {}
