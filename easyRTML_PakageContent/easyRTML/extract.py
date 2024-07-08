import pandas as pd
import numpy as np

class Extractor:
    def __init__(self, **kwargs):
        """
        Initialize the Extractor class.
        Arguments:
        - kwargs: keyword arguments containing:
          - sampling_freq: int, sampling frequency
          - mean_gesture_duration: int, mean gesture duration in ms
          - shift: float, shift factor
        """
        self.sampling_freq = kwargs.get('sampling_freq', 1000)
        self.mean_gesture_duration = kwargs.get('mean_gesture_duration', 1000)
        self.shift = kwargs.get('shift', 0.3)
        self.variables = {}

    def calculate_features(self, **kwargs):
        """
        Calculate features from a window of data.
        Arguments:
        - kwargs: keyword arguments containing:
          - window: np.array, data window
        Returns:
        - tuple: calculated features (min, max, mean, rms)
        """
        window = kwargs.get('window')
        min_val = np.min(window)
        max_val = np.max(window)
        mean_val = np.mean(window)
        rms_val = np.sqrt(np.mean(window ** 2))
        return min_val, max_val, mean_val, rms_val

    def extract_features(self, **kwargs):
        """
        Extract features from the dataframe.
        Arguments:
        - kwargs: keyword arguments containing:
          - dataframe: pd.DataFrame, input dataframe
          - window_length: int, length of the window
          - hop_size: int, size of the hop
        Returns:
        - pd.DataFrame, dataframe with extracted features
        """

    def process_data(self, **kwargs):
        """
        Process normalized dataframe to extract features.
        Arguments:
        - kwargs: keyword arguments containing:
          - normalized_df: pd.DataFrame, normalized input dataframe
        Returns:
        - tuple: features dataframe, shuffled dataframe, and variables
        """
        
        unique_labels = normalized_df['label_name'].unique()
        features_dfs = []
        for label_name in unique_labels:
            subset_df = normalized_df[normalized_df['label_name'] == label_name]
            features_df = self.extract_features(dataframe=subset_df, window_length=window_length, hop_size=hop_size)
            features_dfs.append(features_df)

        features_df = pd.concat(features_dfs, ignore_index=True)
        self.variables = {
            'num_columns': num_columns,
            'window_length': window_length,
            'hop_size': hop_size,
            'buffer_length': buffer_length,
            'rem_length': rem_length,
            'shift_length': shift_length
        }

        return self.features_df, self.variables

    def get_variables(self, **kwargs):
        """
        Get the variables dictionary.
        Arguments:
        - kwargs: keyword arguments (not used)
        Returns:
        - dict, variables dictionary
        """
        return self.variables

    def get_shuffled_df(self, **kwargs):
        """
        Get the shuffled dataframe.
        Arguments:
        - kwargs: keyword arguments (not used)
        Returns:
        - pd.DataFrame, shuffled dataframe
        """
        return self.shuffled_df
