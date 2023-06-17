from fastapi import FastAPI
from fastapi import FastAPI, UploadFile, File
from typing import List
import pandas as pd
import os

app = FastAPI()

@app.get("/api/v1")
def read_root():
    marketList = []
    chartList = []
    timeframeList = []

    for market in os.scandir('./transformedData'):
        if market.is_dir():
            marketList.append(market.name)
            for chart in os.scandir(market.path):
                if chart.is_dir():
                    chartList.append(chart.name)
                    for timeframe in os.scandir(chart.path):
                        if timeframe.is_file():
                            timeframeName = os.path.splitext(timeframe.name)[0]
                            if timeframeName not in timeframeList:
                                timeframeList.append(timeframeName)

    response = {
        "Meta Data": {
            "1. Markets": marketList,
            "2. Charts": chartList,
            "3. Timeframes": timeframeList,
        }
    }
    return response

@app.get("/api/v1/{type}/{chart}/{timeframe}")
def upload_csv(type: str, chart: str, timeframe: str):
    file_path = f"./transformedData/{type}/{chart}/{timeframe}.csv"
    df = pd.read_csv(file_path)
    df = df.set_index(df['Datetime'])
    del df["Datetime"]
    df = df.astype(str)

    response = {
        "Meta Data": {
            "1. Information": f"{chart} chart with splits and volume, timeframe: {timeframe}.",
            "2. Symbol": chart,
            "3. Oldest value": df.index[0],
            "4. Latest value": df.index[-1],
            "5. Output Size": f'This chart contains {df.shape[0]} records.',
        },
        "Time Series": df.to_dict(orient="index")
    }
    
    return response