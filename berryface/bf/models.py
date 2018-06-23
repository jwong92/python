
from datetime import datetime
from pprint import pprint
import hashlib
import uuid
import json
from django.db import models

# Create your models here.

class MeasureType(models.Model):
    measurement = models.CharField(max_length=200)
    unit = models.CharField(max_length=200)

    def __str__(self):
        return self.measurement

class SensorTypeManager(models.Manager):   
    def insert_sensor(self, sensors):
        for sensor in sensors:
            s = self.filter(name=sensor['sensor_type_name']).exists()
            if not s:
                measuretypes = []
                for mtype in sensor['types']:
                    m = MeasureType.objects.filter(measurement=mtype['measure'])
                    if not m:
                        m = MeasureType(measurement=mtype['measure'],unit=mtype['unit'])
                        m.save()
                        m = MeasureType.objects.filter(measurement=mtype['measure'])
                    measuretypes.append(m.values()[0]['id'])
                new_sensor_type = SensorType(name=sensor['sensor_type_name'])
                new_sensor_type.save()
                for m_item in measuretypes:
                    new_sensor_type.measurements.add(m_item)
        return 'done'

                
class SensorType(models.Model):
    name = models.CharField(max_length=100)
    measurements = models.ManyToManyField(MeasureType)

    objects = SensorTypeManager()

    def __str__(self):
        return self.name

class SensorManager(models.Manager):
    def add_sensor(self, sensors):
        # CHECK IF THE SENSOR EXISTS
        for sensor in sensors:
            given_name_exists = self.filter(given_name=sensor['given_name']).exists()
            # IF THE GIVEN NAME DOES NOT EXIST
            if not given_name_exists:               
                # FIND THE SENSOR TYPE ID FROM THE SENSORTYPE TABLE
                sensor_id =  SensorType.objects.filter(name=sensor["sensor_type_name"])
                # IF THE SENSOR EXISTS
                if sensor_id.exists():
                # CREATE A NEW SENSOR
                    s = sensor_id[0].sensor_set.create(given_name=sensor["given_name"], location=sensor["location"])

class Sensor(models.Model):
    given_name = models.CharField(max_length=200)
    location = models.CharField(max_length=200)
    sensor_type_id = models.ForeignKey(SensorType, on_delete=models.CASCADE)

    def __str__(self):
        return self.given_name

    objects = SensorManager()

class EntryManager(models.Manager):
    def add_entry(self, sensors):
        for sensor in sensors:
            # DETERMINE THE SENSOR AND MEASURE_TYPE_ID
            sensor_type = Sensor.objects.filter(given_name=sensor["given_name"])
            for types in sensor['types']:
                measure_type = MeasureType.objects.filter(measurement=types["measure"])
                if sensor_type.exists() and measure_type.exists():
                    # FOR EACH ENTRY, ADD THE VALUE
                    for entry in types['entries']:
                        obj, e = Entry.objects.get_or_create(date=datetime.strptime(entry['created_at'],"%Y-%m-%d_%H:%M:%S"), defaults={
                            'value': entry['value'],
                            'sensor_type_id': sensor_type[0],
                            'measure_type_id': measure_type[0]
                        },)

class Entry(models.Model):
    value = models.FloatField()
    date = models.DateTimeField()
    sensor_type_id = models.ForeignKey(Sensor, on_delete=models.CASCADE)
    measure_type_id = models.ForeignKey(MeasureType, on_delete=models.CASCADE)

    objects = EntryManager()


class RoleManager(models.Manager):
    def add_role(self, roles):
        for r in roles["roles"]:
            # CHECK IF THE ROLE EXISTS
            role_exists = self.filter(role=r["role"])
            # IF NOT, ADD THE ROLE
            if not role_exists:
                self.create(role=r["role"], description=r["description"])

class Role(models.Model):
    role = models.CharField(max_length=100)
    description = models.CharField(max_length=300)

    objects = RoleManager()

    def __str__(self):
        return self.role

class UserManager(models.Manager):
    def hash_password(self, password):
        hash_obj = hashlib.md5()
        pass_encoded = password.encode('utf-8')
        hash_obj.update(pass_encoded)
        hashed_password = hash_obj.hexdigest()

        return hashed_password

    def insert_user(self, user):
        # CHECK IF THE USER EXISTS
        for u in user["user"]:
            user_exists = self.filter(username=u["username"])
            if not user_exists:
                # HASH THE PASSWORD
                hashed_pass = User.objects.hash_password(u["password"])
                # GET INSTANCE OF THE ROLE
                role_id = Role.objects.filter(pk=u["role_id"])
                # CREATE THE UNIQUE TOKEN
                unique_token = uuid.uuid1()
                # CREATE A NEW USER
                u = self.create(username=u["username"], password=hashed_pass, token=unique_token, role_id=role_id[0])

# GET TOKEN WITH A JSON OBJ PROVIDED
    def get_token(self, user):
        # CHECK THE LOGIN CREDENTIALS
        for user in user["user"]:
            user_exists = self.filter(email=user["email"])
            if user_exists:
                # COMPARE THE THE PASSWORDS
                hashed_password_db = user_exists.values("password")[0]["password"]
                hashed_password = User.objects.hash_password(user["password"])
                if hashed_password_db == hashed_password:
                    # RETURN THE TOKEN
                    return user_exists.values("token")[0]["token"]

# GET TOKEN WITH A USER AND PASS PROVIDED AS A STRING
    def check_cred_get_token(self, in_email, in_password):
        # LOOK FOR THEIR EMAIL
        credentials = []
        email = self.filter(email=in_email)
        if email.exists():
        # COMPARE THE PASSWORDS
            hashed_password_db = email.values("password")[0]['password']
            hashed_password = self.hash_password(in_password)
            if hashed_password_db == hashed_password:
                # RETURN THE TOKEN IF PASSWORD AND EMAIL MATCH (RETURNS IN JSON)
                credentials.append({
                    "token" : email.values("token")[0]["token"],
                    "role_id" : email.values("role_id")[0]['role_id']
                })
                return credentials
            else:
                credentials.append({
                    "token" : False,
                    "role_id" : False
                })
                return credentials
        else:
            credentials.append({
                "token" : False,
                "role_id" : False
                })
            return credentials
        

class User(models.Model):
    username = models.CharField(max_length=250)
    password = models.CharField(max_length=400)
    token = models.CharField(max_length=100)
    role_id = models.ForeignKey(Role, on_delete=models.CASCADE)

    objects = UserManager()

    def __str__(self):
        return self.username
    
# class SensorType(models.Model):
#     sensor = models.ForeignKey(Sensor, on_delete=models.CASCADE)
#     name = models.CharField(max_length=50)
#     unit = models.CharField(max_length=10, blank="true")
#     monitors = models.CharField(max_length=100)         

# class Temperature(models.Model):
#     sensor_type = models.ForeignKey(SensorType, on_delete=models.CASCADE)
#     temp = models.FloatField('Temperature')
#     date = models.DateTimeField('Date Pulled')

# class Humidity(models.Model):
#     sensor_type = models.ForeignKey(SensorType, on_delete=models.CASCADE)
#     humidity = models.FloatField('Humidity')
#     date = models.DateTimeField('Date Pulled')

# class TemperatureManager(models.Manager):
#     def insert_temp(self, info):
#         for item in info:
#             b_name = item['sensor_type_name']
#             for entry in item['entries']:
#                 temp_aux = Temperature(
#                     b_name=b_name, 
#                     temp=entry['value'], 
#                     pub_date=datetime.strptime(entry['created_at'], "%Y-%m-%d_%H:%M:%S"))
#                 temp_aux.save()

# class Temperature(models.Model):
#     b_name = models.CharField(max_length=300)
#     temp = models.FloatField('temperature')
#     pub_date = models.DateTimeField('date pulled')
#     def __str__(self):
#         return self.b_name
    
#     objects =  TemperatureManager()