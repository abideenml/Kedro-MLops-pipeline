"""Project settings. There is no need to edit this file unless you want to change values
from the Kedro defaults. For further information, including these default values, see
https://kedro.readthedocs.io/en/stable/kedro_project_setup/settings.html."""

from kedro_mlflow.framework.hooks import MlflowHook
HOOKS = (MlflowHook(),)


# Instantiated project hooks.
# For example, after creating a hooks.py and defining a ProjectHooks class there, do
# from churn_modeling.hooks import ProjectHooks
# HOOKS = (ProjectHooks(),)

# Installed plugins for which to disable hook auto-registration.
# DISABLE_HOOKS_FOR_PLUGINS = ("kedro-viz",)

# Class that manages storing KedroSession data.
# from kedro.framework.session.store import BaseSessionStore
# SESSION_STORE_CLASS = BaseSessionStore
# Keyword arguments to pass to the `SESSION_STORE_CLASS` constructor.
# SESSION_STORE_ARGS = {
#     "path": "./sessions"
# }

# Directory that holds configuration.
# CONF_SOURCE = "conf"

# Class that manages how configuration is loaded.
from kedro.config import OmegaConfigLoader  # noqa: import-outside-toplevel

CONFIG_LOADER_CLASS = OmegaConfigLoader
# Keyword arguments to pass to the `CONFIG_LOADER_CLASS` constructor.
# CONFIG_LOADER_ARGS = {
#       "config_patterns": {
#           "spark" : ["spark*/"],
#           "parameters": ["parameters*", "parameters*/**", "**/parameters*"],
#       }
# }

# Class that manages Kedro's library components.
# from kedro.framework.context import KedroContext
# CONTEXT_CLASS = KedroContext

# Class that manages the Data Catalog.
# from kedro.io import DataCatalog
# DATA_CATALOG_CLASS = DataCatalog

# Set up the session store¶
# In the domain of experiment tracking, each pipeline run is considered a session. 
# A session store records all related metadata for each pipeline run, from logged 
# metrics to other run-related data such as timestamp, git username and branch. 
# The session store is a SQLite database that is generated during your first pipeline 
# run after it has been set up in your project.




# To use kedro-viz for experimental tracking:
# from kedro_viz.integrations.kedro.sqlite_store import SQLiteStore
# from pathlib import Path
# SESSION_STORE_CLASS = SQLiteStore
# SESSION_STORE_ARGS = {"path": str(Path(__file__).parents[2] / "data")}
