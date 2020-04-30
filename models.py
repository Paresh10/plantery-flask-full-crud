from peewee import *

from flask_login import UserMixin


DATABASE = SqliteDatabase('users.sqlite')


class User(UserMixin, Model):

    class Meta:
        database = DATABASE

    name=CharField()
    email=CharField(unique=True)
    username=CharField(unique=True)
    password=CharField()


def connect_to_database():
    DATABASE.connect()

    DATABASE.create_tables([User], safe=True)
    print("Connect with User database and created tables if there were none")

    DATABASE.close()
