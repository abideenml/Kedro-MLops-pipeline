import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from alibi_detect.cd import ClassifierDrift
from sklearn.ensemble import RandomForestClassifier
from xgboost import XGBClassifier

def processing_datatypes_bins(raw_data: pd.DataFrame) -> pd.DataFrame:
    """Processing the datatypes and tenure of customers data.

    Args:
        raw_data: Raw data.
    Returns:
        Intermediate data, with `Total charges` converted to float, and
        `tenure_group` converted into 12 bins.
        """

    replaceStruct = {"Churn":     {"No": 0, "Yes": 1 }  }
    oneHotCols = ["gender","SeniorCitizen","Partner","Dependents","PhoneService","MultipleLines"
                ,"InternetService","OnlineSecurity","OnlineBackup",
                "DeviceProtection","TechSupport","StreamingTV","StreamingMovies",
                "Contract","PaperlessBilling","PaymentMethod"]

    raw_data_2=raw_data.replace(replaceStruct, inplace=True)
    raw_data_2=pd.get_dummies(raw_data, columns=oneHotCols)
    
    return raw_data_2

def one_hot_encoding(raw_data: pd.DataFrame) -> pd.DataFrame:
    """Preprocesses the churn data.

    Args:
        raw_data: Raw data.
    Returns:
        Preprocessed data, with `churn` column one-hot encoded and `customerID`, `tenure`
        dropped.
        """
    raw_data['TotalCharges']=pd.to_numeric(raw_data['TotalCharges'],errors='coerce') #coerce puts NaN values if there are any parsing errors
    raw_data.dropna(inplace=True)
    raw_data=raw_data.drop('customerID',axis=1)
    raw_data_2 = pd.get_dummies(raw_data)
    raw_data_2.rename(columns = {'MultipleLines_No phone service':'MultipleLines_No_phone_service', 'InternetService_Fiber optic':'InternetService_Fiber_optic','OnlineSecurity_No internet service':'OnlineSecurity_No_internet_service','OnlineBackup_No internet service':'OnlineBackup_No_internet_service','DeviceProtection_No internet service':'DeviceProtection_No_internet_service','TechSupport_No internet service':'TechSupport_No_internet_service','StreamingTV_No internet service':'StreamingTV_No_internet_service','StreamingMovies_No internet service':'StreamingMovies_No_internet_service','PaymentMethod_Mailed check':'PaymentMethod_Mailed_check','PaymentMethod_Electronic check':'PaymentMethod_Electronic_check','PaymentMethod_Credit card (automatic)':'PaymentMethod_Credit_card','PaymentMethod_Bank transfer (automatic)':'PaymentMethod_Bank_transfer','Contract_Two year':'Contract_Two_year','Contract_One year':'Contract_One_year','Contract_Month-to-month':'Contract_Month_to_month'}, inplace = True)

    return raw_data_2

def correlation_plots(data: pd.DataFrame):
    """Plots the correlation matrix of the data.

    Args:
        data: Preprocessed data.
    Returns:
        Positive and negative correlation plots.
    """
    
    #Get Correlation of "Churn" with other variables:
    pos = plt.figure(figsize=(20,10))
    data.corr()['Churn'].sort_values(ascending = False)[:20].plot(kind='bar')
    plt.title('Positive Correlation')

    neg=plt.figure(figsize=(20,10))
    data.corr()['Churn'].sort_values(ascending = False)[20:].plot(kind='bar')
    plt.title('Negative Correlation')

    return pos, neg

# def extra_plots(data: pd.DataFrame):
#     """Plots the pairwise plot and churn distribution of the data.

#     Args:
#         data: Preprocessed data.
#     Returns:
#         Pairwise plot and churn distribution.
#     """
#     # pairwise = sns.pairplot(data, hue="Churn", palette="husl")
#     churn_distribution = sns.countplot(x=data['Churn'])
#     plt.title('No of Churned Customers',fontsize=15)

#     return churn_distribution


def drift_detection(model: RandomForestClassifier | XGBClassifier, x_h0: pd.DataFrame):
    """Detects drift in the data.
    
    Args:
        model: Trained model.
        x_h0: Reference data.
    
    Returns:
        Drift output.
    """

    # define drift detector with binarize prediction
    cd = ClassifierDrift(
        x_ref=x_h0,
        model=model,
        backend='sklearn',
        binarize_preds=True,
        n_folds=2,
    )
    drift_output = cd.predict(x=x_h0)
    print("Hello")
    print(drift_output)
    return drift_output