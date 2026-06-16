from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def hola_mundo():
    return {"mensaje": "¡El Loro Políglota está cobrando vida! 🦜"}
