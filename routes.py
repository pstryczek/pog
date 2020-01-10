from . import app
from models.flashes import FlashesModel
from flask import render_template


@app.route("/")
@app.route("/index")
@app.route("/home")
def index():
    return render_template("index.html", index=True)


@app.route("/flashes/")
@app.route("/flashes/<time>")
def flashes():
    thunder = FlashesModel.objects.order_by("time")
    return render_template("flashes.html", ShockData=thunder)