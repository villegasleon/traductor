# traductor

 1. En la consola debes ingresar en un entorno virtual, por tantot debes ubicarte en la consola dentro de 
la carpeta traductor, despues debes escribir: python -m venv traductor.
2. te regresa a la carpeta, mientras que dentro de ella ya se creo otra carpeta llamada traductor, debes 
acceder: cd traductor
3.Acceder a la carpeta Scripts: cd Scripts.
4. Activar asi:  .\activate
5. Instala las librerias flask: pip install flask
6. INstala libreria SpeechRecognition : pip install SpeechRecognition
7. Instala libreria pyaudio : pip install pyaudio
8. Una vez instaldas todas las librerias que ocuparas en tu entorno virtual, ejecutamos la app:
py app.py
9. Vamos a postman para validar, copiamos la url que nos proporciona la consola cuando inicio:
http://127.0.0.1:5000 
10. completamos la url con el endpoint que tenemos en el archivo voice_view.py , 
el parametro que viene en el Blueprint: voice  y el parametro del route: /get_voice_text
11. Queda asi el endpoint que probaremos, es un metodo GET:  http://127.0.0.1:5000/voice/get_voice_text



