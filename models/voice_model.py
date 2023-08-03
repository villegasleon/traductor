import speech_recognition as sr
from googletrans import Translator

class VoiceModel:
    def __init__(self):
        self.recognizer = sr.Recognizer()
        self.translator = Translator()

    def recognize_speech(self):
        with sr.Microphone() as source:
            print("Habla ahora...")
            audio = self.recognizer.listen(source)

        try:
            text = self.recognizer.recognize_google(audio, language="en-US")
            return text
        except sr.UnknownValueError:
            return "No se pudo reconocer el audio"
        except sr.RequestError:
            return "Error al conectar con el servicio de reconocimiento"

    def translate_to_spanish(self, text):
        try:
            translated_text = self.translator.translate(text, src='en', dest='es').text
            return translated_text
        except Exception as e:
            return "Error al traducir el texto: {}".format(str(e))
