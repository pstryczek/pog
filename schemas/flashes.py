from ma import ma
from models.flashes import FlashesModel


class FlashesSchema(ma.Schema):
    class Meta:
        model = FlashesModel
        # dump_only = ("flash_id", "time",)
