from fastapi import FastAPI
from pydantic import BaseModel
import joblib
import json

# FastAPI instance
app = FastAPI()

class model_input(BaseModel):
    # Specify the correct data types
    house_age: int
    construction_type: str
    marital_status: str  
    number_of_bedrooms: int
    coverage_type: str

# Load the saved files
preprocessor = joblib.load("preprocessor.pkl")
lasso_model = joblib.load("best_lasso_model.pkl")

# Create API
@app.get('/')
def premium_prediction(input_parameters: model_input):
    input_data = input_parameters.json()
    input_dictionary = json.loads(input_data)

    # Extract values from the dictionary
    house_age = input_dictionary["house_age"]
    construction_type = input_dictionary["construction_type"]
    marital_status = input_dictionary["marital_status"]
    number_of_bedrooms = input_dictionary["number_of_bedrooms"]
    coverage_type = input_dictionary["coverage_type"]

    # Convert to list
    input_data = [house_age, construction_type, marital_status, number_of_bedrooms, coverage_type]

    # Preprocess the data and predict the output
    transformed_data = preprocessor.transform([input_data])
    prediction = lasso_model.predict(transformed_data)

    # Return the prediction
    return {"Premium": prediction[0]}
