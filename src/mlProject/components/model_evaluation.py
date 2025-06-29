import os
import numpy as np
import pandas as pd
from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score
from urllib.parse import urlparse
import mlflow
import mlflow.sklearn
import joblib
import dagshub
from mlflow.models import infer_signature
from mlProject.entity.config_entity import ModelEvaluationConfig
from mlProject.utils.common import save_json
from pathlib import Path

class ModelEvaluation:
    def __init__(self, config: ModelEvaluationConfig):
        self.config = config
        
    
    def eval_matrics(self, actual, pred):
        rmse = np.sqrt(mean_squared_error(actual, pred))
        mae = mean_absolute_error(actual, pred)
        r2 = r2_score(actual, pred)
        
        return rmse, mae, r2
    
    
    def log_into_mlflow(self):
        test_data = pd.read_csv(self.config.test_data_path)
        model = joblib.load(self.config.model_path)
        
        X_test = test_data.drop(columns=self.config.target_column)
        y_test = test_data[self.config.target_column]
        
        y_pred = model.predict(X_test)
        
        mlflow.set_registry_uri(self.config.mlflow_uri)
        tracking_url_type_store = urlparse(mlflow.get_tracking_uri()).scheme
        mlflow.set_experiment("Wine Quality Prediction")
        signature = infer_signature(X_test, model.predict(X_test))
        
        with mlflow.start_run():
            
            (rmse, mae, r2) = self.eval_matrics(y_test, y_pred)
            
            # Saving metrics as local
            scores = {"rmse": rmse, "mae": mae, "r2": r2}
            save_json(path=Path(self.config.metric_file_path), data=scores)
            
            mlflow.log_params(self.config.all_params)
            
            mlflow.log_metric("rmse", rmse)
            mlflow.log_metric("mae", mae)
            mlflow.log_metric("r2", r2)
            
            # Model registry does not work with file store
            if tracking_url_type_store != "file":
                # Register the model
                # There are other ways to use the Model Registry, which depends on nthe use
                mlflow.sklearn.log_model(sk_model=model, name="model", signature=signature, registered_model_name="ElasticnetModel")
            else:
                mlflow.sklearn.log_model(sk_model=model, name="model", signature=signature)