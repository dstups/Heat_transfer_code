#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Wed Dec  5 15:35:47 2018

@author: davidstupski
"""

from __future__ import division
import numpy as np
from scipy.integrate import odeint 
import matplotlib.pyplot as plt
from matplotlib import cm
from mpl_toolkits.mplot3d import Axes3D
import pandas as pd

#Need a script that highlights times of events where thermoregulatory thresholds are broken
plt.style.use("seaborn-white")
tamb = []
rad = []
sstemp = []
#mean values of all paramaters
def heat_transfer(Tb, t, i, Ta):
    hK = 0.00334300205882
    #Ta = 10
    alpha = .903
    alpha_reflect = .87
    a_inc = .0000365683
    ireflect = i*.3
    epsilon = .95
    sigma = 5.67*10**-8
    a_surf =.0000731367
    c = 4.31
    m = 0.04
    dTbdt = -1.0 * hK*(Tb-Ta)/(c*m) + alpha *a_inc*i/(c*m)+ alpha_reflect*a_inc*ireflect/(c*m) - epsilon *sigma*a_surf*((Tb+273.15)**4-(Ta+273.15)**4)/(c*m) + ((-29.83514*Tb+1763.0566)/(1000))/c - (.0022*2.71828**(.24413*Tb))/(1000)/c
    return dTbdt
#mean - lower error value for all paramaters    
def heat_transfermin(Tb, t, i, Ta):
    hK = 0.00334300205882+.00029816
    #Ta = 10
    alpha = .903-.0081
    alpha_reflect = .87
    a_inc = .0000365683
    ireflect = i*.3
    epsilon = .95
    sigma = 5.67*10**-8
    a_surf =.0000731367
    c = 4.31
    m = 0.04
    dTbdt = -1.0 * hK*(Tb-Ta)/(c*m) + alpha *a_inc*i/(c*m) + alpha_reflect*a_inc*ireflect/(c*m) - epsilon *sigma*a_surf*((Tb+273.15)**4-(Ta+273.15)**4)/(c*m) + 1.15*(((-29.83514*Tb+1763.0566-56*1.96))/(1000))/c - .90*(.0022*2.71828**(.24413*Tb)-25.81*1.96)/(1000)/c
    return dTbdt
#mean + upper error value for all paramaters
def heat_transfermax(Tb, t, i, Ta):
    hK = 0.00334300205882-.00029816
    #Ta = 10
    alpha = .903+.0081
    alpha_reflect = .87
    a_inc = .0000365683
    ireflect = i*.3
    epsilon = .95
    sigma = 5.67*10**-8
    a_surf =.0000731367
    c = 4.31
    m = 0.04
    dTbdt = -1.0 * hK*(Tb-Ta)/(c*m) + alpha *a_inc*i/(c*m) +alpha_reflect*a_inc*ireflect/(c*m)- epsilon *sigma*a_surf*((Tb+273.15)**4-(Ta+273.15)**4)/(c*m) + .85*(((-29.83514*Tb+1763.0566)+56*1.96)/(1000))/c - (.0022*2.71828**(.24413*Tb)+25.81*1.96)/(1000)/c
    return dTbdt
#initiate numpy array for how many "seconds" we allow the model to run for
t = np.linspace(0,200,500)
#initial temperature of bee, here set to hive temperature
T0= 37.5
#mean bee paramaters + hot july conditions
sol = odeint(heat_transfer, T0, t,args =(1100, 33))
solmax= odeint(heat_transfermax, T0, t, args= (1100, 33))
solmin = odeint(heat_transfermin, T0, t,args = (1100, 33))
solcold =odeint(heat_transfer, T0, t,args =(900, 10))
solcoldmax = odeint(heat_transfermax, T0, t, args= (900, 10))
solcoldmin = odeint(heat_transfermin, T0, t,args = (900, 10))
sol_vals= []
solmax_vals = []
solmin_vals = []
solcold_vals = []
solcoldmax_vals = []
solcoldmin_vals = []
for x in sol:
    for i in x:
        sol_vals.append(i)
for x in solmax:
    for i in x:
        solmax_vals.append(i)
for x in solmin:
    for i in x:
        solmin_vals.append(i)
for x in solcold:
    for i in x:
        solcold_vals.append(i)  
for x in solcoldmax:
    for i in x:
        solcoldmax_vals.append(i) 
for x in solcoldmin:
    for i in x:
        solcoldmin_vals.append(i)         
          

#make data frames, necessary for shade between portion      
new_df = pd.DataFrame()
new_df["Hot Mean"]= sol_vals
new_df["Hot Upper"]= solmax_vals      
new_df["Hot Lower"] = solmin_vals
new_df["Cold Mean"]= solcold_vals
new_df["Cold Upper"] = solcoldmax_vals
new_df["Cold Lower"] = solcoldmin_vals
fig, ax = plt.subplots()
ax.plot(t, sol,color = "red", label = "Hot July Afternoon", linestyle = "-")
ax.plot(t, solmax, color = "green", linestyle = "")
ax.plot(t, solmin, color = "yellow", linestyle = "")
ax.fill_between(t, new_df["Hot Upper"], new_df["Hot Lower"], color = "red", alpha = '0.2')
ax.plot(t, solcold, color = "blue", linestyle = "--", label = "Cold April Morning")
ax.plot(t, solcoldmax, color = "green", linestyle = "")
ax.plot(t, solcoldmin, color = "yellow", linestyle = "")    
ax.fill_between(t, new_df["Cold Upper"], new_df["Cold Lower"], color = "blue", alpha = '0.2')
ax.set_xlim(0, 200)
ax.legend()
ax.set_xlabel("Time (s)", color = "k")
ax.set_ylabel("Internal Temperature (C)", color = "k")
ax.spines["top"].set_visible(False)
ax.spines["right"].set_visible(False)
#plt.savefig("/Users/davidstupski/Desktop/hot_cold.pdf")