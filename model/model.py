from sklearn.model_selection import GridSearchCV
import sys
import pandas as pd
from pathlib import Path
if sys.path[0][-3:] != 'HW3':
    sys.path[0] = str(Path(sys.path[0]).parent)
from connector.connector import get_data
from conf.tuning import settings
from util.utility import spliting_data
from util.utility import save_model
from conf.tuning import logging as lg
from conf.settings_model import models
from sklearn.metrics import accuracy_score


def train_model(Model, Data:pd.DataFrame, target:str, list_of_param: list) -> None:
    """
    This function find the best model with the given set of parametries and data, after that save it in dir
    """
    featured_model = models[Model] #finding models in dictionary
    splited_data = spliting_data(Data.drop(target, axis=1), Data[target]) #split the data
    lg.info('Data was splitted')
    searcher = GridSearchCV(featured_model(), list_of_param, scoring="neg_root_mean_squared_error", cv=settings.cv) #give gyperparameters to our GridSearch
    searcher.fit(splited_data[0], splited_data[2]) #fit GridSearch
    lg.info(f'Model fitted, best score = {accuracy_score(splited_data[3], searcher.predict(splited_data[1]))}')
    best_model = searcher.best_estimator_ #getting best model
    save_model(settings.dir+f'/model={Model}.pkl', best_model) #save best model
    lg.info(f'Best model was saved')