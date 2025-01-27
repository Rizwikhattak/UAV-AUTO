from config import app, db
from Routes import user_routes,drone_routes,mission_planner_routes,mission_task_routes,location_pin_routes,mission_data_location_routes,mission_data_image_routes,sortie_routes,drone_availability_log_routes,drone_station_mapping_routes,station_routes,mission_station_mapping_routes,routes_controller_routes,mission_video_routes
from Directories import create_all_directories

create_all_directories()
# app.register_blueprint(user_routes, url_prefix='/api')  # Optional: prefix all user routes with '/api'
app.register_blueprint(user_routes)  # Optional: prefix all user routes with '/api'
app.register_blueprint(drone_routes)
app.register_blueprint(mission_planner_routes)
app.register_blueprint(mission_task_routes)
app.register_blueprint(location_pin_routes)
app.register_blueprint(mission_data_location_routes)
app.register_blueprint(mission_data_image_routes)
app.register_blueprint(sortie_routes)
app.register_blueprint(drone_availability_log_routes)
app.register_blueprint(drone_station_mapping_routes)
app.register_blueprint(station_routes)
app.register_blueprint(mission_station_mapping_routes)
app.register_blueprint(routes_controller_routes)
app.register_blueprint(mission_video_routes)
total_routes = len(list(app.url_map.iter_rules()))
print("Total Routes:", total_routes)

if __name__ == "__main__":
    app.run(debug=True,host='0.0.0.0')
