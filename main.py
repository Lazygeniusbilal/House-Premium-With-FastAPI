from fastapi import FastAPI
from pydantic import BaseModel
import pandas as pd
import joblib

# Define the FastAPI app
app = FastAPI()

# Load the preprocessor and model at startup
preprocessor = joblib.load("preprocessor.pkl")
model = joblib.load("best_lasso_model.pkl")

# Define the request body using Pydantic
class InputData(BaseModel):
    house_age: int
    construction_type: str
    matrial_status: str
    number_of_bedrooms: int
    coverage_type: str

# Define a prediction endpoint
@app.post("/predict")
def predict(input_data: InputData):
    # Convert input data to DataFrame
    data_df = pd.DataFrame([input_data.dict()])
    
    # Preprocess the input data
    transformed_data = preprocessor.transform(data_df)
    
    # Make the prediction
    prediction = model.predict(transformed_data)
    
    # Return the prediction as a response
    return {"prediction": prediction[0]}


