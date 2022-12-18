import sys
import os
from pathlib import Path
if sys.path[0][-3:] != 'HW3':
    sys.path[0] = str(Path(sys.path[0]).parent)
from conf.tuning import settings
from model.model import train_model
from conf.settings_model import models
from connector.connector import get_data
from conf.tuning import logging as lg
from util.utility import load_model

def prediction(model:str, values:list) -> int:
    """
    This function take the model and values to predict the result, if model exist in path it take it,
    if not it started to fit it as result it return the class
    """
    if model in list(models.keys()):   #Checking that model in our dictionary
        if f'model={model}.pkl' not in os.listdir(settings.dir): #Checking do we have the model in saving files
            lg.info(f'Model={model}.pkl is not in dir, starting fittting')
            data = get_data(settings.link) #taking data
            train_model(model, data, settings.target, settings[model]) #put it in train function
            lg.info('Model trained')
    lg.info('Load the model')
    model = load_model(settings.dir, model) #load model
    lg.info('Model was loaded')
    return model.predict(values)