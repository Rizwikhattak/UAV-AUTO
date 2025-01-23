from Model import Routes,LocationPin
from config import db

class RoutesController():

    @staticmethod
    def insert_route(data):
        route = Routes(admin_id=data['admin_id'],name=data['name'])
        db.session.add(route)
        db.session.commit()
        return {'id':route.id,'admin_id':route.admin_id,'name':route.name}

    @staticmethod
    def get_routes():
        routes = Routes.query.filter_by(validity=1).all()
        if routes:
            return [{'id':r.id,'admin_id':r.admin_id,'name':r.name} for r in routes]
        return {}

    @staticmethod
    def get_all_routes():
        routes = (db.session.query(Routes, LocationPin)
                  .join(LocationPin, Routes.id == LocationPin.route_id)
                  .filter(Routes.validity == 1)
                  .all())
        if routes:
            # Create a dictionary to group location pins by route
            route_dict = {}
            for route, location in routes:
                if route.id not in route_dict:
                    route_dict[route.id] = {
                        'id': route.id,
                        'admin_id': route.admin_id,
                        'name': route.name,
                        'locations': []  # Initialize the list of locations
                    }
                # Append location data to the corresponding route
                route_dict[route.id]['locations'].append({
                    'location_pin_id': location.id,
                    'latitude': location.latitude,
                    'longitude': location.longitude
                })
            # Convert the dictionary to a list of routes
            return list(route_dict.values())

        return []

    @staticmethod
    def delete_route(route_id):
        route = Routes.query.filter_by(id=route_id, validity=1).first()
        location_pins = LocationPin.query.filter_by(route_id=route_id).all()
        if route:
            route.validity = 0
            db.session.commit()
            if location_pins:
                for location_pin in location_pins:
                    location_pin.validity = 0
                    db.session.commit()
            return {'id':route.id,'admin_id':route.admin_id,'name':route.name}
        return {}