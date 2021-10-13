import numpy as np
from scipy.spatial.distance import cdist
class Kernel(object):

    def __init__(self, i, coords, t, bw=None, tau=None, fixed=True, 
                 function='triangular', eps=1.0000001):
    
        self.coords = coords
        self.t = t
        self.tau = tau
        if self.tau == 0:
            self.coords_new = coords
        else:
            self.coords_new = np.hstack([coords, (np.sqrt(tau) * t)])
        self.dvec = cdist([self.coords_new[i]], self.coords_new).reshape(-1)
        self.function = function

        if fixed:
            self.bandwidth = float(bw)
        else:
            self.bandwidth = np.partition(
                self.dvec,
                int(bw) - 1)[int(bw) - 1] * eps  #partial sort in O(n) Time
        self.kernel = self._kernel_funcs(self.dvec / self.bandwidth)

        if self.function == "bisquare":  #Truncate for bisquare
            self.kernel[(self.dvec >= self.bandwidth)] = 0

    def _kernel_funcs(self, zs):
        # functions follow Anselin and Rey (2010) table 5.4
        if self.function == 'triangular':
            return 1 - zs
        elif self.function == 'uniform':
            return np.ones(zs.shape) * 0.5
        elif self.function == 'quadratic':
            return (3. / 4) * (1 - zs**2)
        elif self.function == 'quartic':
            return (15. / 16) * (1 - zs**2)**2
        elif self.function == 'gaussian':
            return np.exp(-0.5 * (zs)**2)
        elif self.function == 'bisquare':
            return (1 - (zs)**2)**2
        elif self.function == 'exponential':
            return np.exp(-zs)
        else:
            print('Unsupported kernel function', self.function)