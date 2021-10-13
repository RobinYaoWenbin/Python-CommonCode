import numpy as np
from copy import deepcopy

def golden_section(A, C, x, delta, taudecimal, function, tol):
    iters = 0
    dict = {}
    diff = 1e9
    opt_score = None
    opt_tau = None
    B = A + delta * np.abs(C - A)
    D = C - delta * np.abs(C - A)
    while np.abs(diff) > tol and iters < 200:
        iters += 1
        B = np.round(B, taudecimal)
        D = np.round(D, taudecimal)
        if B in dict:
            score_B = dict[B]
        else:
            score_B = function(x, B)
            dict[B] = score_B

        if D in dict:
            score_D = dict[D]
        else:
            score_D = function(x, D)
            dict[D] = score_D
        if score_B <= score_D:
            opt_score = score_B
            opt_tau = B
            C = D
            D = B
            B = A + delta * np.abs(C - A)
        else:
            opt_score = score_D
            opt_tau = D
            A = B
            B = D
            D = C - delta * np.abs(C - A)
            diff = score_B - score_D     
    return opt_tau, opt_score

def twod_golden_section(a, c, A, C, delta, function, 
                        tol, max_iter, bwdecimal, taudecimal, verbose = False):
    b = a + delta * np.abs(c - a)
    d = c - delta * np.abs(c - a)
    opt_score = None
    opt_bw = None
    opt_tau = None
    diff = 1e9
    dict = {}
    iters = 0
    while np.abs(diff) > tol and iters < 200:
        iters += 1
        b = np.round(b, bwdecimal)
        d = np.round(d, bwdecimal)
        if b in dict:
            score_b = dict[b]
        else:
            tau_b, score_b = golden_section(A, C, b, delta, taudecimal, function, 
                                            tol)
            dict[b] = score_b
        if d in dict:
            score_d = dict[d]
        else:
            tau_d, score_d = golden_section(A, C, d, delta, taudecimal, function, 
                                            tol)
            dict[d] = score_d
        if score_b <= score_d:
            opt_score = score_b
            opt_bw = b
            opt_tau = tau_b
            c = d
            d = b
            b = a + delta * np.abs(c - a)
        else:
            opt_score = score_d
            opt_bw = d
            opt_tau = tau_d
            a = b
            b = d
            d = c - delta * np.abs(c - a) 
        diff = score_b - score_d
        if verbose:
            print('bw, tau, score:', opt_bw, opt_tau, opt_score)
    return opt_bw, opt_tau


def multi_bws(init_bw, init_tau, y, X, n, k, tol, max_iter, rss_score, 
              gtwr_func, bw_func, sel_func, multi_bw_min, multi_bw_max, 
              multi_tau_min, multi_tau_max, verbose=False):
    """
    Multiscale GTWR bandwidth search procedure using iterative GAM backfitting
    """
    if init_bw or init_tau is None:
        bw, tau = sel_func(bw_func(y, X))
        optim_model = gtwr_func(y, X, bw, tau)
    else:
        bw, tau = init_bw, init_tau
        optim_model = gtwr_func(y, X, bw, tau)
    bw_gtwr = bw
    tau_gtwr = tau
    err = optim_model.resid
    betas = optim_model.betas

    XB = np.multiply(betas, X)
    if rss_score:
        rss = np.sum((err)**2)
    iters = 0
    scores = []
    delta = 1e6
    bws = np.empty(k)
    taus = np.empty(k)
    BWs = []
    Taus = []
   
    for iters in range(1, max_iter + 1):
        new_XB = np.zeros_like(X)
        Betas = np.zeros_like(X)

        for j in range(k):
            temp_y = XB[:, j].reshape((-1, 1))
            temp_y = temp_y + err
            temp_X = X[:, j].reshape((-1, 1))
            bw_class = bw_func(temp_y, temp_X)

            bw, tau = sel_func(bw_class, multi_bw_min[j], multi_bw_max[j],
                                 multi_tau_min[j], multi_tau_max[j])        

            optim_model = gtwr_func(temp_y, temp_X, bw, tau)
            err = optim_model.resid
            betas = optim_model.betas
            new_XB[:, j] = (betas * temp_X).reshape(-1)
            Betas[:, j] = betas.reshape(-1)
            bws[j] = bw
            taus[j] = tau

        num = np.sum((new_XB - XB)**2) / n
        den = np.sum(np.sum(new_XB, axis=1)**2)
        score = (num / den)**0.5
        XB = new_XB

        if rss_score:
            predy = np.sum(np.multiply(betas, X), axis=1).reshape((-1, 1))
            new_rss = np.sum((y - predy)**2)
            score = np.abs((new_rss - rss) / new_rss)
            rss = new_rss
        scores.append(deepcopy(score))
        delta = score
        BWs.append(deepcopy(bws))
        Taus.append(deepcopy(taus))

        if verbose:
            print("Current iteration:", iters, ",SOC:", np.round(score, 7))
            print("Bandwidths:", ', '.join([str(bw) for bw in bws]))
            print("taus:", ','.join([str(tau) for tau in taus]))

        if delta < tol:
            break
    opt_bws = BWs[-1]
    opt_tau = Taus[-1]
    return (opt_bws, opt_tau, np.array(BWs), np.array(Taus), np.array(scores), 
                Betas, err, bw_gtwr, tau_gtwr)