from flask import Blueprint, render_template, 

bp = Blueprint("music", __name__, url_prefix="/music")

@bp.route("/")
def hello_music():
    return "hello music"
