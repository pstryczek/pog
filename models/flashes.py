from db import db
from typing import List
from pymongo import MongoClient

myclient = MongoClient("mongodb://localhost:27017/UTA_Enrollment")
mydb = myclient["UTA_Enrollment"]
mycol = mydb["flashes"]

class FlashesModel(db.Document):
    __tablename__ = "flashes"

    flash_id = db.IntField()
    time = db.StringField( max_length=20)
    lat = db.FloatField()
    lon = db.FloatField()
    region = db.IntField()
    delay = db.FloatField()

    # flash_id = db.Column(db.Integer, primary_key=True)
    # time = db.Column(db.String(20), nullable=False)
    # lat = db.Column(db.Float, nullable=False)
    # lon = db.Column(db.Float, nullable=False)
    # region = db.Column(db.Float, nullable=False)
    # delay = db.Column(db.Float, nullable=False)



    @classmethod
    def find_by_id(cls, flash_id: int) -> "FlashesModel":
        return cls.query.filter_by(flash_id=flash_id).first()

    @classmethod
    def find_by_region(cls, region: int) -> "FlashesModel":
        return cls.query.filter_by(region=region).first()

    @classmethod
    def find_by_lat(cls, lat: int) -> "FlashesModel":
        return cls.query.filter_by(lat=lat).first()

    @classmethod
    def find_by_lon(cls, lon: int) -> "FlashesModel":
        return cls.query.filter_by(lon=lon).first()

    @classmethod
    def find_by_time(cls, time: str) -> "FlashesModel":
        return cls.query.filter_by(time=time).first()

    @classmethod
    def find_all(cls):

        return(mycol.find())

        # return(mydb.collection.find())

        # for cls.x in mycol.find():
        #     return(cls.x)

        # return cls.query.all()

    def save_to_db(self) -> None:
        db.session.add(self)
        db.session.commit()

    def delete_from_db(self) -> None:
        db.session.delete(self)
        db.session.commit()