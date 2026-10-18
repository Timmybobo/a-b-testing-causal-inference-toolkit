"""
A/B Testing & Causal Inference Toolkit

Assembled from your step-by-step solutions.
"""

import numpy as np

# Step 1 - standard_normal_cdf
import math
import numpy as np
from scipy.special import erf

def standard_normal_cdf(z):
    # TODO: return P(Z <= z) for a standard normal Z, supporting float or numpy array input
    z = np.asarray(z)
    result = 0.5 * (1.0 + erf(z / np.sqrt(2.0)))

    if result.ndim == 0:
        return float(result)
    return result

