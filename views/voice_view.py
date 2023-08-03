from flask import Blueprint
from controllers.voice_controller import get_voice_text

voice_bp = Blueprint("voice", __name__)

@voice_bp.route("/get_voice_text", methods=["GET"])
def get_voice_text_route():
    return get_voice_text()
