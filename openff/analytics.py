import numpy as np


def zscore(x):
    """ Standardization (z-score)
    """
    return (x - np.mean(x, axis=0)) / np.std(x, axis=0)


def small_number_adjustment(num: int):
    """ Variance penalty for small sample sizes
    """
    return min(1.0, np.sqrt(num / 30.))


def compscore(z):
    """ Competiveness score based on correlations between tests
    """
    rho = np.corrcoef(z, rowvar=False)
    rvec = rho[np.tril_indices(rho.shape[0], -1)]  # only i>j
    cs = 1.0 - np.abs(np.mean(rvec))
    return cs, rho
