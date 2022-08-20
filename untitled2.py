# -*- coding: utf-8 -*-
"""
Created on Sat Aug 20 23:18:13 2022

@author: user
"""

from fastapi import FastAPI
from pydantic import BaseModel
import pickle
import json
app = FastAPI()

class model_input(BaseModel):
        
    shaftSpeeds : int
    TWS : int
    temp : int
    meanDraft : int
           
        
# loading the saved model
loaded_model=pickle.load(open('E:/samidha_SIH/fuel_pred/fuel.sav', 'rb'))

@app.post('/diabetes_prediction')
def diabetes_predd(input_parameters : model_input):
    
    input_data = input_parameters.json()
    input_dictionary = json.loads(input_data)
    
    shaftSpeeds = input_dictionary['shaftSpeeds']
    TWS = input_dictionary['TWS']
    temp  = input_dictionary['temp']
    meanDraft= input_dictionary['meanDraft']
    
    input_list = [shaftSpeeds,TWS,temp,meanDraft]
    
    prediction = loaded_model.predict([input_list])
    return prediction