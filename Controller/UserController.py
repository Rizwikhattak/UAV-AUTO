import os
from config import db,app
from Model import User, Admin, Operator
from werkzeug.security import generate_password_hash, check_password_hash


# from flask_bcrypt import Bcrypt
class UserController:
    @staticmethod
    def insert_user(data):
        try:
            hashed_password = generate_password_hash(data['password'])
            user = User(name=data['name'], password=hashed_password, role=data['role'], email=data['email'])
            db.session.add(user)
            db.session.commit()
            return {
                "user_id": user.id,
                "name": user.name,
                "password": user.password,
                "role": user.role,
                "email": user.email
            }
        except Exception as e:
            print(e)
            return {}

    @staticmethod
    def insert_admin(data):
        try:
            user = UserController.insert_user(data)
            if user:
                admin = Admin(user_id=user.get('id'), gender=data['gender'], age=data['age'], phone_no=data['phone_no'])
                db.session.add(admin)
                db.session.commit()
                return {
                    "user_id": user.get('id'),
                    "name": user.get('name'),
                    "role": user.get('role'),
                    "email": user.get('email'),
                    "admin_id": admin.id,
                    "age": admin.age,
                    "gender": admin.gender,
                    "phone_no": admin.phone_no
                }
            else:
                return {}
        except Exception as e:
            print(e)
            return {}

    @staticmethod
    def update_admin(data):
        try:
            user = User.query.filter_by(id=data.get('user_id'), validity=1).first()
            admin = Admin.query.filter_by(id=data.get('id'), validity=1).first()
            if user and admin:
                user.name = data.get('name', user.name)
                user.email = data.get('email', user.email)
                user.role = data.get('role', user.role)
                user.password = generate_password_hash(data.get('password', user.password))
                admin.age = data.get('age', admin.age)
                admin.gender = data.get('gender',admin.gender)
                admin.phone_no = data.get('phone_no',admin.phone_no)
                db.session.commit()
                return {
                    "user_id": user.id,
                    "name": user.name,
                    "password": user.password,
                    "role": user.role,
                    "email": user.email,
                    "admin_id": admin.id,
                    "age": admin.age,
                    "gender": admin.gender,
                    "phone_no": admin.phone_no
                }
            else:
                return {}
        except Exception as e:
            print(e)
            return {}

    @staticmethod
    def delete_admin(admin_id):
        try:
            admin = Admin.query.filter_by(id=admin_id, validity=1).first()
            user = User.query.filter_by(id=admin.user_id, validity=1).first()
            if admin & user:
                admin.validity = 0
                user.validity = 0
                db.session.commit()
                return {
                    "user_id": user.id,
                    "name": user.name,
                    "password": user.password,
                    "role": user.role,
                    "email": user.email,
                    "admin_id": admin.id,
                    "age": admin.age,
                    "gender": admin.gender,
                    "phone_no": admin.phone_no
                }
            else:
                return {}
        except Exception as e:
            print(e)
            return {}

    @staticmethod
    def get_all_admins():
        try:
            admins = (db.session.query(Admin,User)
                      .join(User,Admin.user_id == User.id)
                      .filter(User.role == 'admin', Admin.validity == 1, User.validity == 1)
                      .all())
            if admins:
                return [{
                    "user_id": user.id,
                    "name": user.name,
                    "password": user.password,
                    "role": user.role,
                    "email": user.email,
                    "admin_id": admin.id,
                    "age": admin.age,
                    "gender": admin.gender,
                    "phone_no": admin.phone_no
                } for admin,user in admins]
            else:
                return []
        except Exception as e:
            print(e)
            return []

    @staticmethod
    def get_admin_by_id(admin_id):
        try:
            admin,user = (db.session.query(Admin,User)
                          .join(User,Admin.user_id == User.id)
                          .filter(User.role == 'admin', Admin.id == admin_id, Admin.validity == 1, User.validity == 1)
                          .first())
            if admin and user:
                return {
                    "user_id": user.id,
                    "name": user.name,
                    "password": user.password,
                    "role": user.role,
                    "email": user.email,
                    "admin_id": admin.id,
                    "age": admin.age,
                    "gender": admin.gender,
                    "phone_no": admin.phone_no
                }
            else:
                return {}
        except Exception as e:
            print(e)
            return {}

    #Helper Function
    @staticmethod
    def upload_operator_profile_picture(op_id,op_image):
        # op_image.filename  --> You can get the original filename like this
        file = ''
        for filename in os.listdir(app.config['OPERATOR_PROFILE_PICTURES_FOLDER']):
            op_img_filename = op_image.filename.replace(" ", "_")
            if filename == f"{op_id}_{op_img_filename}":
                print(f'File {filename} already exists :',os.path.join(app.config['OPERATOR_PROFILE_PICTURES_FOLDER'],filename).replace(r"\\", "/"))
                return os.path.join(app.config['OPERATOR_PROFILE_PICTURES_FOLDER'],filename).replace(r"\\", "/")
            if filename.split("_")[0] == str(op_id):
                file = filename
        if file:
            os.remove(os.path.join(app.config['OPERATOR_PROFILE_PICTURES_FOLDER'],file))
        image_path = os.path.join(app.config['OPERATOR_PROFILE_PICTURES_FOLDER'],f'{op_id}_{op_image.filename.replace(" ","_")}')
        op_image.save(image_path)
        print(image_path.replace("\\","/"))
        return image_path.replace("\\","/")

    @staticmethod
    def insert_operator(data,op_image):
        try:
            user = UserController.insert_user(data)
            if user:
                operator = Operator(user_id=user.get('id'))
                db.session.add(operator)
                db.session.commit()
                if op_image:
                    op_id = operator.id
                    image_path = UserController.upload_operator_profile_picture(op_id,op_image)
                    operator.image_path = image_path
                    db.session.commit()
                return {"user_id": user.get('id'), "name": user.get('name'),"role": user.get('role'),"email": user.get('email'),"id": operator.id,"image_path": operator.image_path}
            else:
                return {}
        except Exception as e:
            print(e)
            return {}



    @staticmethod
    def update_operator(data,op_image):
        try:
            user = User.query.filter_by(id=data.get('user_id'), validity=1).first()
            operator = Operator.query.filter_by(id=data.get('id'), validity=1).first()
            if user and operator:
                if op_image:
                    image_path = UserController.upload_operator_profile_picture(operator.id,op_image)
                    operator.image_path = image_path
                user.name = data.get('name', user.name)
                user.email = data.get('email', user.email)
                user.role = data.get('role', user.role)
                user.password = generate_password_hash(data.get('password', user.password))
                db.session.commit()
                return {'id': operator.id, 'name': user.name, 'email': user.email, 'user_id': user.id,
                        'image_path': operator.image_path}
            else:
                return {}
        except Exception as e:
            print(e)
            return {}

    @staticmethod
    def delete_operator(operator_id):
        try:
            operator = Operator.query.filter_by(id=operator_id, validity=1).first()
            user = User.query.filter_by(id=operator.user_id, validity=1).first()
            if operator & user:
                operator.validity = 0
                user.validity = 0
                db.session.commit()
                return {'id': operator.id, 'name': user.name, 'email': user.email, 'user_id': user.id,
                        'image_path': operator.image_path}
            else:
                return {}
        except Exception as e:
            print(e)
            return {}

    @staticmethod
    def login_user(data):
        try:
            email = data['email']
            password = data['password']
            user = User.query.filter_by(email=email).first()
            if user is not None:
                print("user password", user.password)
                print("password", password)
                print("is valid", check_password_hash(user.password, password))
                if check_password_hash(user.password, password):
                    return {'name': user.name, 'email': user.email, 'id': user.id}
                else:
                    return {}
            else:
                return {}
        except Exception as e:
            print(e)
            return {}

    @staticmethod
    def get_all_operators():
        try:
            operators = (db.session.query(Operator,User)
                         .join(User,Operator.user_id == User.id)
                         .filter( User.role == 'operator', Operator.validity == 1, User.validity == 1)
                         .all())
            if operators:
                return [{"user_id": user.id, "name": user.name,"role": user.role,"email": user.email,"id": operator.id,"image_path": operator.image_path} for operator,user in operators]
            else:
                return []
        except Exception as e:
            print(e)
            return []

    @staticmethod
    def get_operator_by_id(operator_id):
        try:
            operator,user = (db.session.query(Operator,User)
                             .join(User,Operator.user_id == User.id)
                             .filter(User.role =='operator', Operator.id == operator_id , Operator.validity == 1, User.validity == 1)
                             .first())
            if operator and user:
                return {"user_id": user.id, "name": user.name,"role": user.role,"email": user.email,"id": operator.id,"image_path": operator.image_path}
            else:
                return {}
        except Exception as e:
            print(e)
            return {}
