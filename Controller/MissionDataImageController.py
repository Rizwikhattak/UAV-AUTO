from config import db,app
from Model import MissionDataImage
import os
from ProcessImage import process_single_image,extract_frames
from io import BytesIO
from PIL import Image
class MissionDataImageController():
    @staticmethod
    def insert_mission_data_image(data):
        mission_data_image = MissionDataImage(mission_data_location_id=data['mission_data_location_id'],image_path = data['image_path'])
        db.session.add(mission_data_image)
        db.session.commit()
        return mission_data_image
    @staticmethod
    def upload_image(data):
        processesed_image_path,isDamaged = process_single_image(data)
        # print("PROCESSSED IMAGE",processesed_image_path,type(processesed_image_path))
        # data_path = os.path.join(app.config['UPLOAD_FOLDER'],data.filename)
        # data.save(data_path)
        return processesed_image_path







