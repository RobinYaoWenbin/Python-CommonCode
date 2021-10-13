import numpy as np
from .kernels import GTWRKernel, GWRKernel
from scipy import linalg
from .model import _compute_betas_gwr
from scipy.stats import f

class test(object):
    
    def __init__(self, coords, t, y, X, bw_GTWR, tau_GTWR, kernel_GTWR = 'gaussian', 
                 fixed_GTWR = False, constant = True):
        
        self.coords = coords
        self.t = t
        self.y = y
        self.n = X.shape[0]
        self.bw_GTWR = bw_GTWR
        self.tau_GTWR = tau_GTWR
        self.kernel_GTWR = kernel_GTWR
        self.fixed_GTWR = fixed_GTWR
        self.constant = constant
        if self.constant:
            self.X = np.hstack([np.ones((self.n, 1)), X])
        else:
            self.X = X
        self.k = self.X.shape[1]
        self.RSS_GTWR = 0
        S = np.empty((self.n,self.n))
        for i in range(self.n):
            wi = GTWRKernel(i, self.coords, self.t, self.bw_GTWR, self.tau_GTWR,
                           self.fixed_GTWR, function = self.kernel_GTWR).kernel.reshape(-1,1)
            wi[wi <= 1e-6] = 1e-6
            betas, xtx_inv_xt = _compute_betas_gwr(self.y, self.X, wi)
            predy = np.dot(self.X[i], betas)[0]
            resid = self.y[i] - predy
            self.RSS_GTWR += float(resid ** 2)
            S[i] = np.dot(self.X[i], xtx_inv_xt)
        self.Rs = np.dot((np.eye(self.n)-S).T, (np.eye(self.n)-S))
        del S
        self.trRs = 0
        trRsRs = 0
        for i in range(self.n):
            self.trRs += self.Rs[i,i]
            trRsRs += float(self.Rs[i,:] @ self.Rs[:,i])
        self.r_s = self.trRs ** 2 / trRsRs
       
    def spacialtimetest(self,):
        
        H = self.X @ np.linalg.inv(self.X.T @ self.X) @ self.X.T
        Rh = (np.eye(self.n)-H).T @ (np.eye(self.n)-H)
        del H
        RSS_OLS = (self.y.T @ Rh @ self.y)[0][0]
        Rhs = Rh - self.Rs
        del Rh
        trRhs = 0
        trRhsRhs = 0
        for i in range(self.n):
            trRhs += Rhs[i,i]
            trRhsRhs += float(Rhs[i,:] @ Rhs[:,i])
        r_h_s = trRhs**2 / trRhsRhs
        gttest = (RSS_OLS - self.RSS_GTWR) / self.RSS_GTWR * self.trRs/trRhs        
        gtF = f.sf(gttest,r_h_s,self.r_s)
        return gttest, gtF, r_h_s, self.r_s
    
    def spacialtest(self, h, kernel_TWR = 'gaussian', fixed_TWR = False):
        
        RSS_TWR = 0
        M = np.empty((self.n,self.n))
        for i in range(self.n):
            wi = GWRKernel(i, self.t, h, fixed=fixed_TWR,
                        function=kernel_TWR).kernel.reshape(-1,1)
            X_derivative = self.X * (self.t-self.t[i])
            X_new = np.hstack([self.X, X_derivative])
            xT = (X_new * wi).T
            xtx_inv_xt = np.dot(np.linalg.inv(np.dot(xT, X_new)), xT)
            xstack = np.hstack([self.X[i].reshape(1,self.k),np.zeros((1,self.k))])
            predy = (np.dot(np.dot(xstack, xtx_inv_xt), self.y))[0] 
            resid = self.y[i] - predy
            RSS_TWR += float(resid ** 2)
            M[i] = np.dot(xstack, xtx_inv_xt)
        Rm = (np.eye(self.n)-M).T @ (np.eye(self.n)-M)
        del M
        Rms = Rm - self.Rs
        del Rm
        trRms = 0
        trRmsRms = 0
        for i in range(self.n):
            trRms += Rms[i,i]
            trRmsRms += float(Rms[i,:] @ Rms[:,i])
        r_m_s = trRms**2 / trRmsRms
        gtest = (RSS_TWR - self.RSS_GTWR) / self.RSS_GTWR * self.trRs/trRms        
        gF = f.sf(gtest,r_m_s,self.r_s)
        return gtest, gF, r_m_s, self.r_s
    
    def timetest(self, bw_GWR, kernel_GWR = 'gaussian', fixed_GWR = False):
        
        RSS_GWR = 0
        L = np.empty((self.n,self.n))
        for i in range(self.n):
            wi = GWRKernel(i, self.coords, bw_GWR, fixed=fixed_GWR,
                        function=kernel_GWR).kernel.reshape(-1,1)
            betas, xtx_inv_xt = _compute_betas_gwr(self.y, self.X, wi)
            predy = np.dot(self.X[i], betas)[0]
            resid = self.y[i] - predy
            RSS_GWR += float(resid ** 2)
            L[i] = np.dot(self.X[i], xtx_inv_xt)
        Rl = (np.eye(self.n)-L).T @ (np.eye(self.n)-L)
        del L
        Rls = Rl - self.Rs
        del Rl
        trRls = 0
        trRlsRls = 0
        for i in range(self.n):
            trRls += Rls[i,i]
            trRlsRls += float(Rls[i,:] @ Rls[:,i])
        r_l_s = trRls**2 / trRlsRls
        ttest = (RSS_GWR - self.RSS_GTWR) / self.RSS_GTWR * self.trRs/trRls                
        tF = f.sf(ttest,r_l_s,self.r_s)
        return ttest, tF, r_l_s, self.r_s
        
        
        

        
        
            
            
        
        