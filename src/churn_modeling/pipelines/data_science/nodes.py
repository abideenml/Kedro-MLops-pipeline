import logging
from typing import Dict, Tuple

import pandas as pd

from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from xgboost import XGBClassifier
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score, roc_auc_score
from imblearn.combine import SMOTEENN
import mlflow
from mlflow.models import infer_signature


def split_data(data: pd.DataFrame, parameters: Dict) -> Tuple:
    """Splits data into features and targets training and test sets.

    Args:
        data: Data containing features and target.
        parameters: Parameters defined in parameters/data_science.yml.
    Returns:
        Split data.
    """
    X = data.drop('Churn',axis=1)
    y = data['Churn'] 

    X_train, Xg_test, y_train, yg_test = train_test_split(
        X, y, test_size=parameters["test_size"], random_state=parameters["random_state"]
    )

    # Perform standard scaling on the features
    # scaler = StandardScaler()
    # X_train = scaler.fit_transform(X_train)
    # X_test = scaler.fit_transform(X_test)
    sm = SMOTEENN()
    X_resampled, y_resampled = sm.fit_resample(X_train,y_train)
    Xr_train,Xr_test,yr_train,yr_test = train_test_split(X_resampled, y_resampled,test_size=0.2)
    X_train= pd.DataFrame(Xr_train)
    X_test= pd.DataFrame(Xr_test)
    y_train= pd.DataFrame(yr_train)
    y_test= pd.DataFrame(yr_test)
    X_resampled= pd.DataFrame(X_resampled)
    y_resampled= pd.DataFrame(y_resampled)


    return X_train, X_test, y_train, y_test, X_resampled, y_resampled


def train_model(X_resampled: pd.DataFrame, y_resampled: pd.Series, parameters: Dict) -> RandomForestClassifier| XGBClassifier:
    """Trains the Classifier.

    Args:
        X_train: Training data of independent features.
        y_train: Training data for price.

    Returns:
        Trained model.
    """
    if(parameters["classifier"] == "RandomForestClassifier"):
        classifier = RandomForestClassifier(n_estimators=parameters["n_estimators"], criterion=parameters["gini"], 
                                        random_state = parameters["random_state"],max_depth=parameters["max_depth"],
                                        min_samples_leaf=parameters["min_samples_leaf"])
        classifier.fit(X_resampled, y_resampled)
    
    else:
        classifier = XGBClassifier(n_estimators=parameters["n_estimators"],max_depth=parameters["max_depth"])
        classifier.fit(X_resampled, y_resampled)
        
    return classifier



def evaluate_model(
    classifier: RandomForestClassifier | XGBClassifier, X_test: pd.DataFrame, y_test: pd.Series
) -> Dict[str, float]:
    """Calculates and logs the coefficient of determination.

    Args:
        classifier: Trained model.
        X_test: Testing data of independent features.
        y_test: Testing data for price.
    """
    # scaler = StandardScaler()
    # X_test = scaler.fit_transform(X_test)
    
    # Make predictions on the test set
    y_pred = classifier.predict(X_test)
 
    # Evaluate metrics
    accuracy = accuracy_score(y_test, y_pred)
    precision = precision_score(y_test, y_pred)
    recall = recall_score(y_test, y_pred)
    f1 = f1_score(y_test, y_pred)
    roc_auc = roc_auc_score(y_test, y_pred)

    logger = logging.getLogger(__name__)
    logger.info("Accuracy: %.3f", accuracy)
    logger.info("Precision: %.3f", precision)
    logger.info("Recall: %.3f", recall)
    logger.info("F1-score: %.3f", f1)
    logger.info("Roc Auc: %.3f", roc_auc)

    return {"Accuracy": {"value": float(accuracy), "step": 1}, 
            "Precision": {"value": float(precision), "step": 1},
            "Recall": {"value": float(recall), "step": 1},
            "F1": {"value": float(f1), "step": 1}, 
            "Roc Auc": {"value": float(roc_auc), "step": 1}
            }


def test_model(
    classifier: RandomForestClassifier | XGBClassifier, test_x: pd.DataFrame
):
    """Calculates and logs the coefficient of determination.

    Args:
        classifier: Trained model.
        test_x: Testing data of independent features.
    """

    # Make predictions on the test set
    y_pred = classifier.predict(test_x)
    y_pred = pd.DataFrame(y_pred, columns=["Churn"])
    signature = infer_signature(test_x, y_pred)
    # Logger
    logger = logging.getLogger(__name__)
    logger.info("Prediction for test set completed.")
    logger.info("Prediction file stored at '/churn-prediction/data/07_model_output/pred_test.csv'")
    return y_pred, signature



def register_model(
        classifier: RandomForestClassifier | XGBClassifier, parameters: Dict, signature: Dict
):
    
    mlflow.sklearn.log_model(
        sk_model=classifier,
        artifact_path="sklearn-model",
        registered_model_name="sklearn-regmodel",
        signature=signature
    )
    # Stages: Staged, Production, Archived

    return "Model registered successfully"
