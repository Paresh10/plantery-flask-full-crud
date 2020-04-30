from peewee import *

# import datetime
import datetime

from flask_login import UserMixin


DATABASE = SqliteDatabase('users.sqlite')

# User Class
class User(UserMixin, Model):

    class Meta:
        database = DATABASE

    name=CharField()
    email=CharField(unique=True)
    username=CharField(unique=True)
    password=CharField()

# Plant class
class Plant(Model):

    class Meta:
        database = DATABASE

    name = CharField()
    region = CharField()
    description = CharField()
    posted_on = DateTimeField(default=datetime.datetime.now)
    belongs_to = ForeignKeyField(User, backref='plants')






def connect_to_database():
    DATABASE.connect()

    DATABASE.create_tables([User, Plant], safe=True)
    print("Connect with User database and created tables if there were none")

    DATABASE.close()
