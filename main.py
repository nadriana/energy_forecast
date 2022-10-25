from fastapi import FastAPI
from services.arima import ARIMAService
from services.prophet import ProphetService
from services.sarima import SARIMAService
import pandas as pd
import json

tags_metadata = [
    {
        "name": "prophet",
        "description": "Forecast with Prophet. Returns forecasts for next 24 hours.",
    },
    {
        "name": "arima",
        "description": "Forecast with ARIMA. Returns forecasts for next 24 hours.",
    },
    {
        "name": "sarima",
        "description": "Forecast with SARIMA. Returns forecasts for next 24 hours.",
    }
]

app = FastAPI(title="Granify forecast REST API services",
    description="Forecast",
    version="0.0.1",
    contact={
        "name": "Adriana Tapia",
        "url": "https://www.linkedin.com/in/norma-adriana/",
        "email": "adriana@hey.com",
    },openapi_tags=tags_metadata)

@app.get("/prophet",tags=["Prophet"])
async def prophet():
    df = pd.read_csv("./data/data_prophet.csv")
    service = ProphetService(df)
    
    prophet_fcst = service.forecast()
    parsed = json.loads(prophet_fcst.to_json(orient="records"))
    return parsed


@app.get("/arima",tags=["ARIMA"])
async def arima():
    df = pd.read_csv("./data/power_data.csv", parse_dates = ["Datetime"])
    service = ARIMAService(df)

    arima_fcst = service.forecast()
    parsed = json.loads(arima_fcst.to_json(orient="records"))
    return parsed


@app.get("/sarima",tags=["SARIMA"])
async def sarima():
    df = pd.read_csv("./data/power_data.csv", parse_dates = ["Datetime"])
    service = SARIMAService(df)

    sarima_fcst = service.forecast()
    parsed = json.loads(sarima_fcst.to_json(orient="records"))
    return parsed
    



