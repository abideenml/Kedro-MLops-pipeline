from kedro.pipeline import Pipeline, node, pipeline

from .nodes import evaluate_model, split_data, train_model,test_model, register_model


def create_pipeline(**kwargs) -> Pipeline:
    return pipeline(
        [
            node(
                func=split_data,
                inputs=["preprocessed_data", "params:model_options"],
                outputs=["train_x", "test_x", "train_y", "test_y", "train_x_smote", "train_y_smote"],
                name="split_data_node",
            ),
            node(
                func=train_model,
                inputs=["train_x", "train_y", "params:model_options"],
                outputs="classifier",
                name="train_model_node",
            ),
            node(
                func=evaluate_model,
                inputs=["classifier", "test_x", "test_y"],
                outputs="metrics",
                name="evaluate_model_node",
            ),
            node(
                func=test_model,
                inputs=["classifier", "test_x"],
                outputs=["pred_test","signatures"],
                name="test_model_node",
            ),
            node(
                func=register_model,
                inputs=["classifier", "params:model_options", "signatures"],
                outputs=None,
                name="register_model_node",
            ),
        ]
    )