"""
This is a boilerplate pipeline 'reporting'
generated using Kedro 0.18.13
"""

from kedro.pipeline import Pipeline, pipeline, node
from .nodes import create_confusion_matrix

def create_pipeline(**kwargs) -> Pipeline:
    return pipeline(
        [
            node(
                func=create_confusion_matrix,
                inputs=["test_y", "pred_test"],
                outputs="confusion_matrix",
                name="confusion_matrix_node",
            )
        ]
    )
 