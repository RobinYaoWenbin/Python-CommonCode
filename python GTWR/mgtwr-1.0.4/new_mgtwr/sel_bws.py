
import numpy as np
from .diagnosis import get_AICc, get_AIC, get_BIC
from scipy.spatial.distance import pdist
from .gtwr import GTWR
from .search import twod_golden_section, multi_bws

def get_CV(gtwr):
    """
    Get CV value

    Gaussian only

    Methods: p60, (2.31) or p212 (9.4)
    Fotheringham, A. S., Brunsdon, C., & Charlton, M. (2002).
    Geographically weighted regression: the analysis of spatially varying relationships.
    Modification: sum of residual squared is divided by n according to GWR4 results

    """

    cv = gtwr.aa / gtwr.n
    return cv

getDiag = {'AICc': get_AICc, 'AIC': get_AIC, 'BIC': get_BIC, 'CV': get_CV}

class Sel_bws(object):
    """
    Select bandwidth for kernel

    Parameters
    ----------
    coords        : array-like
                    n*2, collection of n sets of (x,y) coordinates of
                    observatons
                        
    t             : array
                    n*1, time location

    y             : array
                    n*1, dependent variable

    X             : array
                    n*k, independent variable, exlcuding the constant    
   
    kernel        : string
                    type of kernel function used to weight observations;
                    available options:
                    'gaussian'
                    'bisquare'
                    'exponential'

    fixed         : boolean
                    True for distance based kernel function and  False for
                    adaptive (nearest neighbor) kernel function (default)

    constant      : boolean
                    True to include intercept (default) in model and False to exclude
                    intercept.
                    
    multi          : True for multiple (covaraite-specific) bandwidths
                     False for a traditional (same for  all covariates)
                     bandwdith; defualt is False.
                     
    Attributes
    ----------
    y              : array
                     n*1, dependent variable.                     
    X              : array
                     n*k, independent variable, exlcuding the constant    
    coords         : list of tuples
                     (x,y) of points used in bandwidth selection
    t             : array
                    n*1, time location    
    kernel         : string
                     type of kernel used and wether fixed or adaptive
    fixed          : boolean
                     True for fixed bandwidth and False for adaptive (NN)
    criterion      : string
                     bw selection criterion: 'AICc', 'AIC', 'BIC', 'CV'
    bw_min         : float
                     min value used in bandwidth search
    bw_max         : float
                     max value used in bandwidth search
    tau_min        : float
                     min value used in spatio-temporal scale search
    tau_max        : float
                     max value used in spatio-temporal scale search    
    tol            : float
                     tolerance used to determine convergence
    max_iter       : integer
                     max interations if no convergence to tol
    multi          : True for multiple (covaraite-specific) bandwidths
                     False for a traditional (same for  all covariates)
                     bandwdith; defualt is False.
    constant       : boolean
                     True to include intercept (default) in model and False to exclude
                     intercept.
    int_score      : boolan
                     True if adaptive bandwidth is being used and bandwdith
                     selection should be discrete. False
                     if fixed bandwidth is being used and bandwidth does not have
                     to be discrete.
    bw             : scalar or array-like
                     Derived optimal bandwidth(s). Will be a scalar for GTWR
                     (multi=False) and a list of scalars for MGTWR (multi=True)
                     with one bandwidth for each covariate.
    tau            : scalar array-like 
                     Derived optimal spatio-temporal scale. Will be a scalar for GTWR
                     (multi=False) and a list of scalars for MGTWR (multi=True)
                     with one Spatio-temporal scale for each covariate.
    Examples
    --------
    >>> import numpy as np
    >>> from mgtwr.sel_bws import Sel_bws
    >>> from mgtwr.gtwr import GTWR, MGTWR
    >>> np.random.seed(10)
    >>> u = np.array([(i-1)%12 for i in range(1,1729)]).reshape(-1,1)
    >>> v = np.array([((i-1)%144)//12 for i in range(1,1729)]).reshape(-1,1)
    >>> t = np.array([(i-1)//144 for i in range(1,1729)]).reshape(-1,1)
    >>> x1 = np.random.uniform(0,1,(1728,1))
    >>> x2 = np.random.uniform(0,1,(1728,1))
    >>> epsilon = np.random.randn(1728,1)
    >>> beta0 = 5
    >>> beta1 = 3 + (u + v + t)/6
    >>> beta2 = 3+((36-(6-u)**2)*(36-(6-v)**2)*(36-(6-t)**2))/128
    >>> y = beta0 + beta1 * x1 + beta2 * x2 + epsilon
    >>> coords = np.hstack([u,v])
    >>> X = np.hstack([x1,x2])
    >>> sel = Sel_bws(coords, t, y, X, kernel = 'gaussian', fixed = True)
    >>> bw, tau = sel.search(bw_max = 40, tau_max = 5, verbose = True)
    0.8, 0.7  
    """
    
    def __init__(self, coords, t, y, X, kernel = 'bisquare', fixed = False, 
                 multi = False, constant=True):
        self.coords = coords
        self.t = t
        self.y = y
        self.X = X
        self.n = X.shape[0]
        self.constant = constant
        if constant:
            self.k = X.shape[1] + 1
        else:
            self.k = X.shape[1]
        self.kernel = kernel
        self.fixed = fixed
        self.multi = multi
        self.int_score = not self.fixed
        
    def search(self, search_method='twod_golden_section', criterion='AICc', 
               bw_min = None, bw_max = None, tau_min = None,
               tau_max = None, tol=1.0e-6, bwdecimal = 1, taudecimal = 1, max_iter = 200,
               init_bw = None, init_tau = None, multi_bw_min = None,
               multi_bw_max = None, multi_tau_min = None, multi_tau_max = None,
               tol_multi = 1.0e-5, max_iter_multi = 200, verbose = False,
               rss_score = False):
        """
        Method to select one unique bandwidth and Spatio-temporal scale for a gtwr model or a
        bandwidth vector and Spatio-temporal scale vector for a mtgwr model.

        Parameters
        ----------
        criterion      : string
                         bw selection criterion: 'AICc', 'AIC', 'BIC', 'CV'
        bw_min         : float
                         min value used in bandwidth search
        bw_max         : float
                         max value used in bandwidth search
        tau_min        : float
                         min value used in spatio-temporal scale search
        tau_max        : float
                         max value used in spatio-temporal scale search     
        multi_bw_min   : list 
                         min values used for each covariate in mgwr bandwidth search.
                         Must be either a single value or have one value for
                         each covariate including the intercept
        multi_bw_max   : list
                         max values used for each covariate in mgwr bandwidth
                         search. Must be either a single value or have one value
                         for each covariate including the intercept
        multi_tau_min  : list
                         min values used for each covariate in mgtwr spatio-temporal scale
                         search. Must be either a single value or have one value
                         for each covariate including the intercept
        multi_tau_max  : max values used for each covariate in mgtwr spatio-temporal scale
                         search. Must be either a single value or have one value
                         for each covariate including the intercept        
        tol            : float
                         tolerance used to determine convergence
        max_iter       : integer
                         max iterations if no convergence to tol
        init_bw        : float
                         None (default) to initialize MGTWR with a bandwidth
                         derived from GTWR. Otherwise this option will choose the
                         bandwidth to initialize MGWR with.
        init_tau       : float
                         None (default) to initialize MGTWR with a spatio-temporal scale
                         derived from GTWR. Otherwise this option will choose the
                         spatio-temporal scale to initialize MGWR with.
        tol_multi      : convergence tolerence for the multiple bandwidth
                         backfitting algorithm; a larger tolerance may stop the
                         algorith faster though it may result in a less optimal
                         model
        max_iter_multi : max iterations if no convergence to tol for multiple
                         bandwidth backfitting algorithm
        rss_score      : True to use the residual sum of sqaures to evaluate
                         each iteration of the multiple bandwidth backfitting
                         routine and False to use a smooth function; default is
                         False        
        verbose        : Boolean
                         If true, bandwidth searching history is printed out; default is False.
        """
        self.search_method = search_method
        self.criterion = criterion
        self.bw_min = bw_min
        self.bw_max = bw_max
        self.tau_min = tau_min
        self.tau_max = tau_max
        self.tol = tol
        self.bwdecimal = bwdecimal
        self.taudecimal = taudecimal
        self.max_iter = max_iter
        self.init_bw = init_bw
        self.init_tau = init_tau
        if self.multi:
            if multi_bw_min is not None:
                if len(multi_bw_min) == self.k:
                    self.multi_bw_min = multi_bw_min
                elif len(multi_bw_min) == 1:
                    self.multi_bw_min = multi_bw_min * self.k
                else:
                    raise AttributeError(
                        "multi_bw_min must be either a list containing"
                        " a single entry or a list containing an entry for each of k"
                        " covariates including the intercept")
            else:
                a = self._init_section(self.X, self.coords, self.constant)[0]
                self.multi_bw_min = [a] * self.k
            
            if multi_bw_max is not None:
                if len(multi_bw_max) == self.k:
                    self.multi_bw_max = multi_bw_max
                elif len(multi_bw_max) == 1:
                    self.multi_bw_max = multi_bw_max * self.k
                else:
                    raise AttributeError(
                        "multi_bw_max must be either a list containing"
                        " a single entry or a list containing an entry for each of k"
                        " covariates including the intercept")
            else:
                c = self._init_section(self.X, self.coords, self.constant)[1]
                self.multi_bw_max = [c] * self.k
            
            if multi_tau_min is not None:
                if len(multi_tau_min) == self.k:
                    self.multi_tau_min = multi_tau_min
                elif len(multi_tau_min) == 1:
                    self.multi_tau_min = multi_tau_min * self.k
                else:
                    raise AttributeError(
                        "multi_tau_min must be either a list containing"
                        " a single entry or a list containing an entry for each of k"
                        " covariates including the intercept")
            else:
                A = self._init_section(self.X, self.coords, self.constant)[2]
                self.multi_tau_min = [A] * self.k
                
            if multi_tau_max is not None:
                if len(multi_tau_max) == self.k:
                    self.multi_tau_max = multi_tau_max
                elif len(multi_tau_max) == 1:
                    self.multi_tau_max = multi_tau_max * self.k
                else:
                    raise AttributeError(
                        "multi_tau_max must be either a list containing"
                        " a single entry or a list containing an entry for each of k"
                        " covariates including the intercept")
            else:
                C = self._init_section(self.X, self.coords, self.constant)[3]
                self.multi_tau_max = [C] * self.k
        
        self.tol_multi = tol_multi
        self.verbose = verbose
        self.max_iter_multi = max_iter_multi
        self.rss_score = rss_score
        if self.multi:
            self._mbw()
            return self.bws[0], self.bws[1]
        else:
            self._bw()
    
            return self.bw, self.tau
    
    def _bw(self):
        gwr_func = lambda bw, tau: getDiag[self.criterion](GTWR(
            self.coords, self.t, self.y, self.X, bw, tau, kernel=self.kernel, 
            fixed=self.fixed, constant=self.constant).fit(final = False))
        self.bw_min, self.bw_max, self.tau_min, self.tau_max = \
            self._init_section(self.X, self.coords, self.constant)
        delta = 0.38197  #1 - (np.sqrt(5.0)-1.0)/2.0
        self.bw, self.tau = twod_golden_section(self.bw_min, self.bw_max, self.tau_min, 
                                                self.tau_max, delta, gwr_func, self.tol,
                                                 self.max_iter, self.bwdecimal, self.taudecimal,
                                                 self.verbose)
        
    def _mbw(self):
        coords = self.coords
        t = self.t
        y = self.y
        n = self.n
        if self.constant:
            X = np.hstack([np.ones((self.n, 1)), self.X])
        else:
            X = self.X
        k = self.k                 
        kernel = self.kernel
        fixed = self.fixed
        search_method = self.search_method
        criterion = self.criterion
        tol = self.tol
        max_iter = self.max_iter
        verbose = self.verbose
        bwdecimal = self.bwdecimal
        taudecimal = self.taudecimal
        bw_min = self.bw_min
        bw_max = self.bw_max
        tau_min = self.tau_min
        tau_max = self.tau_max
        init_bw = self.init_bw
        init_tau = self.init_tau
        multi_bw_min = self.multi_bw_min
        multi_bw_max = self.multi_bw_max
        multi_tau_min = self.multi_tau_min
        multi_tau_max = self.multi_tau_max
                        
        def gtwr_func(y, X, bw, tau):
            return GTWR(coords, t, y, X, bw, tau, kernel = kernel, 
                 fixed = fixed, constant = False).fit(multi = True)
        
        def bw_func(y, X):
            selector = Sel_bws(coords, t, y, X, kernel = kernel, fixed = fixed, 
                               constant = False)
            return selector
        
        def sel_func(bw_func, bw_min = None, bw_max = None, 
                     tau_min = None, tau_max = None):
            return bw_func.search(
                search_method=search_method, criterion=criterion,
                bw_min=bw_min, bw_max=bw_max, tau_min=tau_min, 
                tau_max=tau_max, tol=tol, max_iter=max_iter,
                bwdecimal=bwdecimal,taudecimal=taudecimal,verbose=False)
        self.bws = multi_bws(init_bw, init_tau, y, X, n, k, self.tol_multi,
                           self.max_iter_multi, self.rss_score, gtwr_func,
                           bw_func, sel_func, multi_bw_min, multi_bw_max, 
                           multi_tau_min, multi_tau_max, verbose=verbose)
        self.bw = self.bws[0]
        self.tau = self.bws[1]
    
    def _init_section(self, X, coords, constant):
        # if len(X) > 0:
        #     n_glob = X.shape[1]
        # else:
        #     n_glob = 0
        # if constant:
        #     n_vars = n_glob + 1
        # else:
        #     n_vars = n_glob
        # n = np.array(coords).shape[0]

        # if self.int_score:
        #     a = 40 + 2 * n_vars
        #     c = n
        # else:
        #     sq_dists = pdist(coords)
        #     a = np.min(sq_dists) / 2.0
        #     c = np.max(sq_dists) * 2.0

        # if self.bw_min is not None:
        #     a = self.bw_min
        # if self.bw_max is not None:
        #     c = self.bw_max
        
        # if self.tau_min is not None:
        #     A = self.tau_min
        # else:
        #     A = 0
        # if self.tau_max is not None:
        #     C = self.tau_max
        # else:
        #     C = 2
        if self.bw_min is not None:
            a = self.bw_min
        else:
            a = 0
        if self.bw_max is not None:
            c = self.bw_max
        else:
            c = max(np.max(coords[:,0])-np.min(coords[:,0]),
                    np.max(coords[:,1])-np.min(coords[:,1]))
        
        if self.tau_min is not None:
            A = self.tau_min
        else:
            A = 0
        if self.tau_max is not None:
           C = self.tau_max
        else:
           C = 4
        return a, c, A, C
