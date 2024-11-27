import pivot
import pivot_nonDA
import numpy as np
import time
import _heartfailure
from SeoulBike.DataForInference import seoulbike
from walmart_dataset import walmart
global seed
def run(iter = 0):    
    seed = int(np.random.rand() * (2**32 - 1))
    # seed = 457262911   
    # print("Seed:",seed)
    ns = 100
    nt = 20
    Xs, Ys = _heartfailure.larger50(ns)
    Xt, Yt = _heartfailure.undereq50(nt)
    p = Xs.shape[1]

    Bs = np.dot(np.dot(np.linalg.inv(np.dot(Xs.T, Xs)), Xs.T) , Ys)
    Bt = np.dot(np.dot(np.linalg.inv(np.dot(Xt.T, Xt)), Xt.T) , Yt)
    Ys_ = Xs.dot(Bs)
    Yt_ = Xt.dot(Bt)
    varYs = 1/(ns - p) * (Ys - Ys_).T.dot(Ys - Ys_)
    varYt = 1/(nt - p) * (Yt - Yt_).T.dot(Yt - Yt_)
    Sigma_s = varYs * np.identity(ns)
    Sigma_t = varYt * np.identity(nt)
    #___________________________________________________________

    # betat = 4
    # true_beta_s = np.full((p,1), 2) #source's beta
    # true_beta_t = np.full((p,1), betat) #target's beta
    k = 3 # k=-1 if choose based criterion
    #___________________________________________________________

    pvalue = pivot.pvalue_SI(seed, ns, nt, p, k, Xs, Xt, Ys, Yt, Sigma_s, Sigma_t, 'para')

    # pvalue = pivot_nonDA.pvalue_SI(seed, ns, p, true_beta_t)

    # Save pvalue into file
    # OCorPARA_FIXorAIC_FPRorTPR = 'para_AIC_time'
    # filename = f'Experiment/Listpvalue_{OCorPARA_FIXorAIC_FPRorTPR}_{ns}_{p}.txt'
    # filename = f'Experiment/Listpvalue_{OCorPARA_FIXorAIC_FPRorTPR}_{ns}_{p}_{betat}.txt'
    # with open(filename, 'a') as f:
    #     f.write(str(en-st)+ '\n')
    return pvalue

if __name__ == "__main__":
    for i in range(130):
        # st = time.time()
        print(f'{i}.')
        print(run())
        # en = time.time()
        # print(f"Time of 1 pvalue {i}: {en - st}")