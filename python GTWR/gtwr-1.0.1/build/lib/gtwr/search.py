import numpy as np

def golden_section(a, c, delta, decimal, function, tol, max_iter, verbose=False):
    b = a + delta * np.abs(c - a)
    d = c - delta * np.abs(c - a)
    diff = 1.0e9
    iters = 0
    dict = {}
    while np.abs(diff) > tol and iters < max_iter:
        iters += 1
        b = np.round(b, decimal)
        d = np.round(d, decimal)

        if b in dict:
            score_b = dict[b]
        else:
            score_b = function(b)
            dict[b] = score_b

        if d in dict:
            score_d = dict[d]
        else:
            score_d = function(d)
            dict[d] = score_d

        if score_b <= score_d:
            opt_val = b
            opt_score = score_b
            c = d
            d = b
            b = a + delta * np.abs(c - a)

        else:
            opt_val = d
            opt_score = score_d
            a = b
            b = d
            d = c - delta * np.abs(c - a)

        
        opt_val = np.round(opt_val, decimal)        
        diff = score_b - score_d
        if verbose:
            print('bw:', opt_val, ', score:', np.round(opt_score,2))

    return opt_val



def onestep_golden_section(A, C, x, delta, taudecimal, function, tol, mpi=False):
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
        if mpi:
            from mpi4py import MPI
            comm = MPI.COMM_WORLD
            rank = comm.Get_rank()
            if rank == 0:
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
                opt_tau = np.round(opt_tau, taudecimal)
            B = comm.bcast(B, root=0)
            D = comm.bcast(D, root=0)
            diff = comm.bcast(diff, root=0)
            opt_score = comm.bcast(opt_score, root=0)
            opt_tau = comm.bcast(opt_tau, root=0)
        else:
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

def twostep_golden_section(a, c, A, C, delta, function, 
                        tol, max_iter, bwdecimal, taudecimal, verbose = False, mpi = False):
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
            if mpi:
                tau_b, score_b = onestep_golden_section(A, C, b, delta, taudecimal, function, 
                                            tol, mpi=True)
            else:
                tau_b, score_b = onestep_golden_section(A, C, b, delta, taudecimal, function, 
                                            tol)
            dict[b] = score_b
        if d in dict:
            score_d = dict[d]
        else:
            if mpi:
                tau_d, score_d = onestep_golden_section(A, C, d, delta, taudecimal, function, 
                                            tol, mpi=True)
            else:
                tau_d, score_d = onestep_golden_section(A, C, d, delta, taudecimal, function, 
                                            tol)
            dict[d] = score_d
        if mpi:
            from mpi4py import MPI
            comm = MPI.COMM_WORLD
            rank = comm.Get_rank()
            if rank == 0:
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
                opt_tau = np.round(opt_tau, taudecimal)
                opt_bw = np.round(opt_bw, bwdecimal)
                if verbose:            
                    print('bw: ', opt_bw, ', tau: ', opt_tau, ', score: ', opt_score)
            b = comm.bcast(b, root=0)
            d = comm.bcast(d, root=0)
            diff = comm.bcast(diff, root=0)
            opt_bw = comm.bcast(opt_bw, root=0)
            opt_tau = comm.bcast(opt_tau, root=0)
        else:
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
                print('bw: ', opt_bw, ', tau: ', opt_tau, ', score: ', opt_score)
    return opt_bw, opt_tau
