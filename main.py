from peewee import SqliteDatabase
import models
from models import Unit, Meter, Entry


database = SqliteDatabase("my_db.db")
models.db.initialize(database)
with models.db as db:
    db.create_tables([Unit, Meter, Entry])


def add_unit(name, unit):
    Unit.create(name=name, unit=unit)


def add_meter(name, number, initial_count, unit):
    Meter.create(name=name, number=number, initial_count=initial_count, unit=unit)


def add_entry(count, meter, date):
    Entry.create(count=count, meter=meter, date=date)


def get_all_units():
    return Unit.select()


def get_all_meters():
    return Meter.select()


def get_all_entries():
    return Entry.select()


def get_all_entries_by_meter(meter):
    return Entry.select().where(meter=meter)


if __name__ == '__main__':
    pass
