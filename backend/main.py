from fastapi import FastAPI
from fastapi.responses import FileResponse
from gtts import gTTS
import os

app = FastAPI()

@app.get("/")
def hola_mundo():
    return {"mensaje": "El servidor del Loro está vivito y coleando 🦜"}

@app.post("/api/tts")
def texto_a_voz():
    texto_de_prueba = "¡Hola Claudia! Estoy hablando desde tu propio servidor de FastAPI. ¡Cruuac!"
    
    # La IA de gTTS coge el texto y lo convierte en formato audio (en español 'es')
    tts = gTTS(text=texto_de_prueba, lang="en", tld="co.uk")
    
    # Guardamos temporalmente el archivo de audio en tu ordenador
    nombre_archivo = "voz_loro.mp3"
    tts.save(nombre_archivo)
    
    # Devolvemos el PLATO COCINADO: El archivo de audio real con su etiqueta invisible
    return FileResponse(path=nombre_archivo, media_type="audio/mpeg", filename=nombre_archivo)