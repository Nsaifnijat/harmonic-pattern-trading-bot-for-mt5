# -*- coding: utf-8 -*-

import pandas as pd
import numpy as np
from scipy.signal import argrelextrema
import matplotlib.pyplot as plt
#import 
import datetime as dt

def peak_detect(price,order=6):
    max_idx=list(argrelextrema(price,np.greater,order=order)[0])
    min_idx=list(argrelextrema(price,np.less,order=order)[0])
    
    idx=max_idx+min_idx+[len(price)-1]

    idx.sort()
    current_idx=idx[-5:]
    #peaks=price.values[idx]
    current_pattern=price[current_idx]
    start=min(current_idx)
    end=max(current_idx)
    return current_idx,current_pattern,start,end

def is_gartley(moves,err_allowed):
    XA=moves[0]
    AB=moves[1]
    BC=moves[2]
    CD=moves[3]
    AB_range=np.array([0.618-err_allowed,0.618+err_allowed])*abs(XA)
    BC_range=np.array([0.382-err_allowed,0.886+err_allowed])*abs(AB)
    CD_range=np.array([1.27-err_allowed,1.618+err_allowed])*abs(BC)
    if XA>0 and AB<0 and BC>0 and CD<0:
        #Bullish Gartley pattern design
        if AB_range[0]<abs(AB)<AB_range[1] and BC_range[0]<abs(BC)<BC_range[1] and CD_range[0]<abs(CD)<CD_range[1]:
            return 1
        else:
            np.NAN
    elif XA<0 and AB>0 and BC<0 and CD>0:
        #Bearish Gartley pattern design
        if AB_range[0]<abs(AB)<AB_range[1] and BC_range[0]<abs(BC)<BC_range[1] and CD_range[0]<abs(CD)<CD_range[1]:
           return -1
        else:
           return np.NAN
       
    else:
        return np.NAN
    
def is_butterfly(moves,err_allowed):
    XA=moves[0]
    AB=moves[1]
    BC=moves[2]
    CD=moves[3]
    AB_range=np.array([0.786-err_allowed,0.786+err_allowed])*abs(XA)
    BC_range=np.array([0.382-err_allowed,0.886+err_allowed])*abs(AB)
    CD_range=np.array([1.618-err_allowed,2.618+err_allowed])*abs(BC)
    if XA>0 and AB<0 and BC>0 and CD<0:
        #Bullish butterfly pattern design
        if AB_range[0]<abs(AB)<AB_range[1] and BC_range[0]<abs(BC)<BC_range[1] and CD_range[0]<abs(CD)<CD_range[1]:
            return 1
        else:
            np.NAN
    elif XA<0 and AB>0 and BC<0 and CD>0:
        #Bearish butterfly pattern design
        if AB_range[0]<abs(AB)<AB_range[1] and BC_range[0]<abs(BC)<BC_range[1] and CD_range[0]<abs(CD)<CD_range[1]:
           return -1
        else:
           return np.NAN
       
    else:
        return np.NAN
      
def is_bat(moves,err_allowed):
    XA=moves[0]
    AB=moves[1]
    BC=moves[2]
    CD=moves[3]
    AB_range=np.array([0.382-err_allowed,0.5+err_allowed])*abs(XA)
    BC_range=np.array([0.382-err_allowed,0.886+err_allowed])*abs(AB)
    CD_range=np.array([1.618-err_allowed,2.618+err_allowed])*abs(BC)
    if XA>0 and AB<0 and BC>0 and CD<0:
        #Bullish bat pattern design
        if AB_range[0]<abs(AB)<AB_range[1] and BC_range[0]<abs(BC)<BC_range[1] and CD_range[0]<abs(CD)<CD_range[1]:
            return 1
        else:
            np.NAN
    elif XA<0 and AB>0 and BC<0 and CD>0:
        #Bearish bat pattern design
        if AB_range[0]<abs(AB)<AB_range[1] and BC_range[0]<abs(BC)<BC_range[1] and CD_range[0]<abs(CD)<CD_range[1]:
           return -1
        else:
           return np.NAN
       
    else:
        return np.NAN
def is_crab(moves,err_allowed):
    XA=moves[0]
    AB=moves[1]
    BC=moves[2]
    CD=moves[3]
    AB_range=np.array([0.382-err_allowed,0.618+err_allowed])*abs(XA)
    BC_range=np.array([0.382-err_allowed,0.886+err_allowed])*abs(AB)
    CD_range=np.array([2.24-err_allowed,3.618+err_allowed])*abs(BC)
    if XA>0 and AB<0 and BC>0 and CD<0:
        #Bullish crab pattern design
        if AB_range[0]<abs(AB)<AB_range[1] and BC_range[0]<abs(BC)<BC_range[1] and CD_range[0]<abs(CD)<CD_range[1]:
            return 1
        else:
            np.NAN
    elif XA<0 and AB>0 and BC<0 and CD>0:
        #Bearish crab pattern design
        if AB_range[0]<abs(AB)<AB_range[1] and BC_range[0]<abs(BC)<BC_range[1] and CD_range[0]<abs(CD)<CD_range[1]:
           return -1
        else:
           return np.NAN
       
    else:
        return np.NAN