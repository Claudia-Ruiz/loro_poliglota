from fastapi import FastAPI
from fastapi.responses import FileResponse
from pydantic import BaseModel
from gtts import gTTS
from deep_translator import GoogleTranslator
import os

app = FastAPI()

# 1. Definimos la plantilla del paquete que nos va a enviar el usuario
# Queremos que nos mande un texto y un idioma (ambos son textos/strings)
class PeticionTTS(BaseModel):
    texto: str
    idioma: str = "es"

@app.get("/")
def hola_mundo():
    return {"mensaje": "El servidor del Loro está vivito y coleando 🦜"}

# 2. Modificamos la carretera para que ACEPTE el paquete del cliente
@app.post("/api/tts")
def texto_a_voz(datos: PeticionTTS):
    # ¡Ahora usamos los datos REALES que nos manda el usuario!
    texto_original = datos.texto
    idioma_destino = datos.idioma

    # 1. TRADUCCIÓN MÁGICA: Traducimos del español (auto) al idioma elegido por el usuario
    texto_traducido = GoogleTranslator(source='auto', target=idioma_destino).translate(texto_original)
    
    # 2. GENERAR VOZ: Ahora le pasamos a la IA de voz el texto ya traducido
    tts = gTTS(text=texto_traducido, lang=idioma_destino)
    
    # Guardamos temporalmente el archivo de audio en tu ordenador
    nombre_archivo = "voz_loro.mp3"
    tts.save(nombre_archivo)
    
    # Devolvemos el PLATO COCINADO: El archivo de audio real con su etiqueta invisible
    return FileResponse(path=nombre_archivo, media_type="audio/mpeg", filename=nombre_archivo)

# 3. CARRETERA DE CONFIGURACIÓN: Le dice a la pantalla qué idiomas aceptamos
@app.get("/api/config")
def obtener_configuracion():
    idiomas_soportados = {
        "es": "Español",
        "en": "Inglés",
        "fr": "Francés",
        "it": "Italiano",
        "ja": "Japonés"
    }
    return {"idiomas": idiomas_soportados}