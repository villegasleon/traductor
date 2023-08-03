from models.voice_model import VoiceModel

if __name__ == "__main__":
    voice_model = VoiceModel()
    text = voice_model.recognize_speech()
    print("Texto en inglés reconocido: ", text)

    translated_text = voice_model.translate_to_spanish(text)
    print("Texto traducido al español: ", translated_text)
