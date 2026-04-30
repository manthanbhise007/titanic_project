import os
import sys
import numpy as np
import pandas as pd
from sklearn.metrics import accuracy_score
from dataclasses import dataclass
from sklearn.svm import SVC
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.linear_model import SGDClassifier

from src.exception import CustomException
from src.logger import logging
from src.utils import save_object,evaluate_model



@dataclass
class ModelTrainierConfig:
    trained_model_file_path=os.path.join("artifact","model.pkl")

class ModelTrainer:
    def __init__(self):
        self.model_trainer_config=ModelTrainierConfig()

    def initate_model_training(self,train_array,test_array):
        try:
            logging.info("splitting training and test input data")
            X_train,y_train,X_test,y_test=(
                train_array[:,:-1],
                train_array[:,-1],
                test_array[:,:-1],
                test_array[:,-1]
            )
            models={
                "svc":SVC(),
                "RandomForestClassifier":RandomForestClassifier(),
                "DecisionTreeClassifier":DecisionTreeClassifier(),
                "SGDClassifier":SGDClassifier()
            }

            model_report:dict=evaluate_model(X_train=X_train,y_train=y_train,X_test=X_test,y_test=y_test,models=models)
            best_model_score=max(sorted(model_report.values()))
            best_model_name=list(model_report.keys())[list(model_report.values()).index(best_model_score)]
            best_model=models[best_model_name]
            logging.info("best model found on both training and testing dataset")
            save_object(
                file_path=self.model_trainer_config.trained_model_file_path,
                obj=best_model
            )
            predicted=best_model.predict(X_test)
            accuracy_score_=accuracy_score(y_test,predicted)
            return accuracy_score_
        except Exception as e:
            raise CustomException(e,sys)
