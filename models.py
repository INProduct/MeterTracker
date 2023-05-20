from peewee import *

db = DatabaseProxy()


class BaseModel(Model):
    id = PrimaryKeyField(unique=True)

    class Meta:
        database = db


class Unit(BaseModel):
    name = CharField()
    unit = CharField()

    class Meta:
        db_table = "units"


class Meter(BaseModel):
    name = CharField()
    number = CharField()
    initial_count = DoubleField()
    unit = ForeignKeyField(Unit)

    class Meta:
        db_table = "meters"


class Entry(BaseModel):
    count = DoubleField()
    date = DateField()
    meter = ForeignKeyField(Meter)

    class Meta:
        db_table = "entries"
