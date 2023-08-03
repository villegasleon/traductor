import speech_recognition as sr

class VoiceModel:
    def __init__(self):
        self.recognizer = sr.Recognizer()

    def recognize_speech(self):
        with sr.Microphone() as source:
            print("Habla ahora...")
            audio = self.recognizer.listen(source)

        try:
            text = self.recognizer.recognize_google(audio, language="es-ES")
            return text
        except sr.UnknownValueError:
            return "No se pudo reconocer el audio"
        except sr.RequestError:
            return "Error al conectar con el servicio de reconocimiento"
