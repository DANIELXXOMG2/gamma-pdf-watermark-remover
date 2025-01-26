class WatermarkConfig:
    SIMILARITY_THRESHOLD = 0.8
    TEMPLATE_HISTOGRAM = [0.18865122, 0.01094256, 0.00925421, 0.01066328, 0.00974929, 0.00663916,
                            0.00488734, 0.00410029, 0.00331323, 0.00256427] + ([0] * (256 - 10))

    @staticmethod
    def get_template_histogram_array():
        import numpy as np
        return np.array(WatermarkConfig.TEMPLATE_HISTOGRAM)