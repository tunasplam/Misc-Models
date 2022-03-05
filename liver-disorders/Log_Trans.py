from sklearn.base import BaseEstimator, TransformerMixin
import numpy as np


"""
To make something work with openml:
- needs to inherit baseestimator and transformermixin
- needs to have __init__, fit and transform
- fit needs to return self
- needs __version__ global variable
- needs the description. its the doc string below the class def.
- make sure weird values like -inf dont show up anywhere in the data.
"""

__version__ = "1.0"


class Log_Trans(BaseEstimator, TransformerMixin):
    """Use log10 transformation.
    """

    def __init__(self):
        pass

    def fit(self, x, y=None):
        #X.apply(np.log10(X))
        return self

    def transform(self, x):
        return np.log10(x+1)
