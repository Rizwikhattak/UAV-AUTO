from Model import LocationPin
from config import db

class LocationPinController():
    @staticmethod
    def insert_location_pins(data):
        location_pin = LocationPin(route_id = data['route_id'],latitude = data['latitude'],longitude = data['longitude'])
        db.session.add(location_pin)
        db.session.commit()
        return {'id':location_pin.id,'route_id':location_pin.route_id,'latitude':location_pin.latitude,'longitude':location_pin.longitude}

    @staticmethod
    def get_location_pins():
        location_pins = LocationPin.query.filter_by(validity=1).all()
        if location_pins:
            return [{'id':l.id,'route_id':l.route_id,'latitude':l.latitude,'longitude':l.longitude} for l in location_pins]
        else:
            return {}
