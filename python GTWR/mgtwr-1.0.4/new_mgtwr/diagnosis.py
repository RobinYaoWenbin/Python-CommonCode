
import numpy as np

def get_AICc(gtwr):
    """
    Get AICc value
    
    Gaussian: p61, (2.33), Fotheringham, Brunsdon and Charlton (2002)
    
    GWGLM: AICc=AIC+2k(k+1)/(n-k-1), Nakaya et al. (2005): p2704, (36)

    """
    n = gtwr.n
    k = gtwr.tr_S
    
    aicc = get_AIC(gtwr) + 2.0 * k * (k + 1.0) / (n - k - 1.0)
    return aicc


def get_AIC(gtwr):
    """
    Get AIC calue

    Gaussian: p96, (4.22), Fotheringham, Brunsdon and Charlton (2002)

    GWGLM:  AIC(G)=D(G) + 2K(G), where D and K denote the deviance and the effective
    number of parameters in the model with bandwidth G, respectively.
    
    """

    k = gtwr.tr_S

    aic = -2.0 * gtwr.llf + 2.0 * (k + 1)
    
    return aic


def get_BIC(gtwr):
    """
    Get BIC value

    Gaussian: p61 (2.34), Fotheringham, Brunsdon and Charlton (2002)
    BIC = -2log(L)+klog(n)

    GWGLM: BIC = dev + tr_S * log(n)

    """
    n = gtwr.n  # (scalar) number of observations
    k = gtwr.tr_S
    
    bic = -2.0 * gtwr.llf + (k + 1) * np.log(n)
    return bic




def corr(cov):

    invsd = np.diag(1 / np.sqrt(np.diag(cov)))
    cors = np.dot(np.dot(invsd, cov), invsd)
    return cors