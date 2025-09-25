from peewee import SqliteDatabase

db = SqliteDatabase('smart_band.db')

def init_db()->None:
    db.connect()
    """TODO: Import Models and create tables"""
    db.close()

