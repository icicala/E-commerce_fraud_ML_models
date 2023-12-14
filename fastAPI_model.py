import requests
# import pandas as pd
from fastapi import FastAPI
# import joblib
# import numpy as np
# from pandas import DataFrame
# from pydantic import BaseModel


# class FraudData(BaseModel):
#     user_id: int
#     signup_time: str
#     purchase_time: str
#     purchase_value: int
#     device_id: str
#     source: str
#     browser: str
#     sex: str
#     age: int
#     country: str


# def preprocess_data(data: FraudData) -> DataFrame:
#     data['signup_time'] = pd.to_datetime(data['signup_time'])
#     data['purchase_time'] = pd.to_datetime(data['purchase_time'])
#
#     data['time_difference'] = (data['purchase_time'] - data['signup_time']).dt.total_seconds().astype(int)
#     data['day_purchase'] = data['purchase_time'].dt.day
#     data['hour_purchase'] = data['purchase_time'].dt.hour
#     data['minute_purchase'] = data['purchase_time'].dt.minute
#     data['second_purchase'] = data['purchase_time'].dt.second
#
#     columns_drop = ['signup_time', 'purchase_time', 'time_difference', 'ip_address']
#     data = data.drop(columns_drop, axis=1)
#     dependent_variable = 'class'
#     data = data[[col for col in data.columns if col != dependent_variable] + [dependent_variable]]
#
#     return data



fastAPI_model = FastAPI(title='ML model',
                        description='Deploy the ML model to production',
                        version='1.0')
# Load the trained model
# model = joblib.load('RFC_model.joblib')

@fastAPI_model.get("/")
async def root():
    return {"message": "Landing page for ML Model API"}

# @fraud_app.post("/predict/")
# def predict(data: dict):
#     processed_data = preprocess_data(data)
#
#     # Make predictions using the loaded model
#     prediction = model.predict(processed_data)
#
#     # Combine original data with prediction result
#     original_data = data.dict()
#     prediction_result = {"prediction": prediction.tolist()}
#
#     # Return both original data and prediction result
#     return {"original_data": original_data, "prediction_result": prediction_result}
#