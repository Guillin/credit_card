from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from sklearn.metrics import mean_squared_error as mse
from sklearn.metrics import mean_absolute_error as mae  # noqa
from sklearn.metrics import r2_score as r2              # noqa
from ml_metrics import quadratic_weighted_kappa as kappa    # noqa

import numpy as np
import math
from ..const import EPS


def mape(y, p):
    """Mean Absolute Percentage Error (MAPE).

    Args:
        y (numpy.array): target
        p (numpy.array): prediction

    Returns:
        e (numpy.float64): MAPE
    """

    filt = np.abs(y) > EPS
    return np.mean(np.abs(1 - p[filt] / y[filt]))


def rmse(y_true, y_pred):
    """Root Mean Squared Error (RMSE).

    This function calculates Root mean square error for regression.
    :param y_true: list of true values
    :param y_pred: list of predicted values
    :return: root mean square error
    """

    # check and get number of samples
    assert y.shape == p.shape

    return np.sqrt(mse(y_true, y_pred))



def gini(y, p):
    """Normalized Gini Coefficient.

    Args:
        y (numpy.array): target
        p (numpy.array): prediction

    Returns:
        e (numpy.float64): normalized Gini coefficient
    """

    # check and get number of samples
    assert y.shape == p.shape

    n_samples = y.shape[0]

    # sort rows on prediction column
    # (from largest to smallest)
    arr = np.array([y, p]).transpose()
    true_order = arr[arr[:, 0].argsort()][::-1, 0]
    pred_order = arr[arr[:, 1].argsort()][::-1, 0]

    # get Lorenz curves
    l_true = np.cumsum(true_order) / np.sum(true_order)
    l_pred = np.cumsum(pred_order) / np.sum(pred_order)
    l_ones = np.linspace(1/n_samples, 1, n_samples)

    # get Gini coefficients (area between curves)
    g_true = np.sum(l_ones - l_true)
    g_pred = np.sum(l_ones - l_pred)

    # normalize to true Gini coefficient
    return g_pred / g_true


# Outcome should be a binary list of the ordinal outcome. [0, 1, 0] for exmaple.
# Probs should be a list of probabilities. [0.79, 0.09, 0.12] for example.
# Outcome and Probs must be provided with the same order as probabilities.

def rps(probs, outcome):
    cum_probs = np.cumsum(probs)
    cum_outcomes = np.cumsum(outcome)
    
    
    sum_rps = 0
    for i in range(len(outcome)):         
        sum_rps+= (cum_probs[i] - cum_outcomes[i])**2
    
    return sum_rps/(len(outcome)-1)