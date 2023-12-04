import matplotlib.pyplot as plt
import seaborn as sn
import pandas as pd



def create_confusion_matrix(test_y: pd.DataFrame, pred_test: pd.DataFrame):
    """Plots the confusion matrix of the data.

    Args:
        test_y: Testing data of independent features.
        pred_test: Testing data for price.
    """
    actuals = test_y["Churn"].to_list()
    predicted = pred_test["Churn"].to_list()

    data = {"y_Actual": actuals, "y_Predicted": predicted}
    df = pd.DataFrame(data, columns=["y_Actual", "y_Predicted"])
    confusion_matrix = pd.crosstab(
        df["y_Actual"], df["y_Predicted"], rownames=["Actual"], colnames=["Predicted"]
    )
    sn.heatmap(confusion_matrix, annot=True)
    return plt


