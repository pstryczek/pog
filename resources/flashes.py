from flask_restful import Resource
from flask import request
from models.flashes import FlashesModel
from schemas.flashes import FlashesSchema
from libs.strings import gettext


flashes_schema = FlashesSchema()
flashes_list_schema = FlashesSchema(many=True)


class Flashes(Resource):
    @classmethod
    def get(cls, flash_id: int):
        flashes = FlashesModel.find_by_id(flash_id)
        if flashes:
            return flashes_schema.dump(flashes), 200

        return {"message": gettext("id_not_found")}, 404

    @classmethod
    def delete(cls, flash_id:int):
        flashes = FlashesModel.find_by_id(flash_id)
        if flashes:
            flashes.delete_from_db()
            return {"message": gettext("ID_deleted")}, 200

        return {"message": gettext("id_not_found")}, 404


class FlashesList(Resource):
    @classmethod
    def get(cls):
        return {"flashes": flashes_list_schema.dump(FlashesModel.find_all())}, 200
