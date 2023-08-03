from flask import jsonify
from models.voice_model import VoiceModel

def get_voice_text():
    voice_model = VoiceModel()
    text = voice_model.recognize_speech()
    return jsonify({"text": text})
