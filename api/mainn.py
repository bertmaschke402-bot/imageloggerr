from fastapi import FastAPI

# ✅ Wichtig: Muss exakt "app" heißen
app = FastAPI()

@app.get("/")
def root():
    return {"status": "ok"}
