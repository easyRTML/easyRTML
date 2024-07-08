import matplotlib.pyplot as plt
import os

class Plot:
    def plot(**kwargs):
        """
        Plot the given dataframe.
        Arguments:
        - kwargs: keyword arguments containing:
          - df: pd.DataFrame, dataframe to plot
        """
        plt.figure(figsize=kwargs.get('figsize', (12, 3)))
        kwargs.get('df').plot(ax=plt.gca())
        plt.xlabel(kwargs.get('xlabel', 'Time'))
        plt.ylabel(kwargs.get('ylabel', 'Amplitude'))
        plt.title(kwargs.get('title', 'Plot'))
        plt.tight_layout()
        plt.show()

    def plot_normalized(**kwargs):
        """
        Plot the normalized dataframe.
        Arguments:
        - kwargs: keyword arguments containing:
          - normalized_df: pd.DataFrame, normalized dataframe to plot
        """
        plt.figure(figsize=kwargs.get('figsize', (12, 3)))
        ax = kwargs.get('normalized_df').drop(columns=kwargs.get('drop_columns', ['label_name'])).plot(ax=plt.gca())
        plt.xlabel(kwargs.get('xlabel', 'Time'))
        plt.ylabel(kwargs.get('ylabel', 'Amplitude'))
        plt.title(kwargs.get('title', 'Normalized Plot'))
        plt.tight_layout()
        plt.show()

    @staticmethod
    def plot_separated(**kwargs):
        """
        Plot separated plots for each unique label in the normalized dataframe.
        Arguments:
        - kwargs: keyword arguments containing:
          - normalized_df: pd.DataFrame, normalized dataframe to plot
        """
        output_dir = kwargs.get('output_dir', 'plots')
        if not os.path.exists(output_dir):
            os.makedirs(output_dir)
