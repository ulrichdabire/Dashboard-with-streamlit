from fastapi import FastAPI
from fastapi.responses import JSONResponse
import pandas as pd

app = FastAPI()

# Charger les données et les fusionner
clics = pd.read_csv("./clics.csv")
impressions = pd.read_csv("./impressions.csv")
achats = pd.read_csv("./achats.csv")

merged_data = pd.merge(impressions, clics, on="cookie_id", how="left")
merged_data = pd.merge(merged_data, achats, on="cookie_id", how="left")


@app.get("/dabireapi/data")
async def get_data():
    return JSONResponse(content=merged_data.to_dict(orient="records")) # Retourne les données au format JSON


