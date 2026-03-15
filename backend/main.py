from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def read_root():
    return {"message": "Welcome to MeatMap API!"}


@app.get("/translations/{cut}")
def get_translation(cut: str):
    # Placeholder: Replace with real data later
    translations = {
        "entrecote": {
            "fr_FR": "Entrecôte",
            "fr_CH": "Entrecôte (Suisse)",
            "en_US": "Ribeye",
        }
    }
    return translations.get(cut, {"error": "Cut not found"})
