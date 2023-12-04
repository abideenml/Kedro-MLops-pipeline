import pandas as pd
import json
import mlflow


logged_model = 'runs:/c6cd9e660ae14e57b5abdc16b81c8ab2/model'

# Load model as a PyFuncModel.
loaded_model = mlflow.pyfunc.load_model(logged_model)

# Predict on a Pandas DataFrame.
import pandas as pd
loaded_model.predict(pd.DataFrame(data))
