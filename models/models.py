from peewee import *
from models.ConnectDatabase import ConnectDatabase


class Counter(Model):
    """A base model that will use our Postgresql database"""
    methods = CharField()
    counter = IntegerField(default=0)

    class Meta:
        database = ConnectDatabase().connect()