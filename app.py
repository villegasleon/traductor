from flask import Flask
from views.voice_view import voice_bp

app = Flask(__name__)
app.register_blueprint(voice_bp, url_prefix="/voice")

if __name__ == "__main__":
    app.run(debug=True)
