#!/usr/bin/env python
# coding: utf-8

import numpy as np
import matplotlib.pyplot as plt
from scipy.special import *

# Plot
def plotFunctions(data,outpath):
    functions = {"n": lambda n: n,"2^n": np.exp2,"square": np.square,
                 "fact": factorial,"log":np.log,"root":np.sqrt}
    for label,f in functions.items():
        plt.plot( data,f(data), linewidth=2, linestyle='dashed', label=label)
        plt.ylim((0,150))
        plt.legend()
        plt.savefig(outpath)


if __name__ == "__main__":
    data=[1,10,50,100]
    outpath="results/01/functions.png"
    plotFunctions(data,outpath)
