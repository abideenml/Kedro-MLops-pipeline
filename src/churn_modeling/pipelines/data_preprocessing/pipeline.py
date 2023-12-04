from kedro.pipeline import Pipeline, node, pipeline

from .nodes import processing_datatypes_bins, one_hot_encoding, correlation_plots, extra_plots, drift_detection

def create_pipeline(**kwargs) -> Pipeline:
    return pipeline(
        [
            node(
                func=processing_datatypes_bins,
                inputs="raw_data",
                outputs="preprocessed_intermediate_data",
                name="create_intermediate_preprocessing_node",
            ),
            node(
                func=one_hot_encoding,
                inputs="preprocessed_intermediate_data",
                outputs="preprocessed_data",
                name="create_preprocessing_node",
            ),
            node(
                func=correlation_plots,
                inputs="preprocessed_data",
                outputs=["positive_correlation", "negative_correlation"],
                name="create_correlation_plots_node",

            ),
            node(
                func=drift_detection,
                inputs=["classifier", "preprocessed_data"],
                outputs="driftmetric",
                name="create_drift_detection_node",
            )
        ]
    )


            # node(
            #     func=extra_plots,
            #     inputs="preprocessed_data",
            #     outputs=["churn_distribution"],
            #     name="create_extra_plots_node",
            # ),