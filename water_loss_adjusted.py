#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Thu Dec  6 14:42:48 2018

@author: davidstupski
"""
from __future__ import division
import numpy as np
from scipy.integrate import odeint 
import matplotlib.pyplot as plt
#from matplotlib import cm
#from mpl_toolkits.mplot3d import Axes3D
import pandas as pd

#Need a script that highlights times of events where thermoregulatory thresholds are broken
plt.style.use("seaborn-white")
tamb = []
rad = []
sstemp = []
#mean values of all paramaters
def heat_transfer(Tb, t, i, Ta):
    hK = 0.00424
    #Ta = 10
    alpha = .903
    a_inc = .0000365683
    #i = 550
    epsilon = .95
    sigma = 5.67*10**-8
    a_surf =.0000731367
    c = 4.31
    m = 0.04
    dTbdt = -1.0 * hK*(Tb-Ta)/(c*m) + alpha *a_inc*i/(c*m) - epsilon *sigma*a_surf*((Tb+273.15)**4-(Ta+273.15)**4)/(c*m) + ((-29.83514*Tb+1763.0566)/(1000))/c - (.0022*2.71828**(.24413*Tb))/(1000)/c
    return dTbdt
#mean - lower error value for all paramaters    
def heat_transfermin(Tb, t, i, Ta):
    hK = 0.00424+.00029816
    #Ta = 10
    alpha = .903-.0081*1.96
    a_inc = .0000365683
    #i = 550
    epsilon = .95
    sigma = 5.67*10**-8
    a_surf =.0000731367
    c = 4.31
    m = 0.04
    dTbdt = -1.0 * hK*(Tb-Ta)/(c*m) + alpha *a_inc*i/(c*m) - epsilon *sigma*a_surf*((Tb+273.15)**4-(Ta+273.15)**4)/(c*m) + (((-29.83514*Tb+1763.0566-56*1.96))/(1000))/c - .90*(.0022*2.71828**(.24413*Tb)-25.81*1.96)/(1000)/c
    return dTbdt

def heat_transfermax(Tb, t, i, Ta):
    hK = 0.00424-.00029816
    #Ta = 10
    alpha = .903+.0081
    a_inc = .0000365683
    #i = 550
    epsilon = .95
    sigma = 5.67*10**-8
    a_surf =.0000731367
    c = 4.31
    m = 0.04
    dTbdt = -1.0 * hK*(Tb-Ta)/(c*m) + alpha *a_inc*i/(c*m) - epsilon *sigma*a_surf*((Tb+273.15)**4-(Ta+273.15)**4)/(c*m) + (((-29.83514*Tb+1763.0566)+56*1.96)/(1000))/c - (.0022*2.71828**(.24413*Tb)+25.81*1.96)/(1000)/c
    return dTbdt


def labheat_transfer(Tb, t, i, Ta):
    hK = 0.00217
    #Ta = 10
    alpha = .903
    a_inc = .0000365683
    #i = 550
    epsilon = .95
    sigma = 5.67*10**-8
    a_surf =.0000731367
    c = 4.31
    m = 0.04
    dTbdt = -1.0 * hK*(Tb-Ta)/(c*m) + alpha *a_inc*i/(c*m) - epsilon *sigma*a_surf*((Tb+273.15)**4-(Ta+273.15)**4)/(c*m) + ((-29.83514*Tb+1763.0566)/(1000))/c - (.0022*2.71828**(.24413*Tb))/(1000)/c
    return dTbdt
#mean - lower error value for all paramaters    
def labheat_transfermin(Tb, t, i, Ta):
    hK = 0.00217+.00029816
    #Ta = 10
    alpha = .903-.0081
    a_inc = .0000365683
    #i = 550
    epsilon = .95
    sigma = 5.67*10**-8
    a_surf =.0000731367
    c = 4.31
    m = 0.04
    dTbdt = -1.0 * hK*(Tb-Ta)/(c*m) + alpha *a_inc*i/(c*m) - epsilon *sigma*a_surf*((Tb+273.15)**4-(Ta+273.15)**4)/(c*m) + (((-29.83514*Tb+1763.0566-56*1.96))/(1000))/c - .90*(.0022*2.71828**(.24413*Tb)-25.81*1.96)/(1000)/c
    return dTbdt

def labheat_transfermax(Tb, t, i, Ta):
    hK = 0.00217-.00029816
    #Ta = 10
    alpha = .903+.0081
    a_inc = .0000365683
    #i = 550
    epsilon = .95
    sigma = 5.67*10**-8
    a_surf =.0000731367
    c = 4.31
    m = 0.04
    dTbdt = -1.0 * hK*(Tb-Ta)/(c*m) + alpha *a_inc*i/(c*m) - epsilon *sigma*a_surf*((Tb+273.15)**4-(Ta+273.15)**4)/(c*m) + (((-29.83514*Tb+1763.0566)+56*1.96)/(1000))/c - (.0022*2.71828**(.24413*Tb)+25.81*1.96)/(1000)/c
    return dTbdt

def water_loss_value(Tb):
    waterloss= (.0022*2.71828**(.24413*Tb))
    return waterloss
T0 = 37.5
t = np.linspace(0,250,1000)
test_temps = [20,21,22, 23,24,25, 26,27,28, 29,30,31, 32, 33,34,35,36, 37, 38]
fin_temps_solar = []
fin_temps_solar_max= []
fin_temps_solar_min = []
fin_temps_lab = []
fin_temps_lab_max = []
fin_temps_lab_min = []

for i in test_temps:
    fin_temps_solar.append(odeint(heat_transfer, T0, t,args =(1100, i))[-1][0])
    fin_temps_solar_min.append(odeint(heat_transfermin, T0, t,args =(1100, i))[-1][0])
    fin_temps_solar_max.append(odeint(heat_transfermax, T0, t,args =(1100, i))[-1][0])

for i in test_temps:
    fin_temps_lab.append(odeint(labheat_transfer, T0, t,args =(0, i))[-1][0])
    fin_temps_lab_min.append(odeint(labheat_transfermin, T0, t,args =(0, i))[-1][0])
    fin_temps_lab_max.append(odeint(labheat_transfermax, T0, t,args =(00, i))[-1][0])
  
#print fin_temps_solar
#print fin_temps_solar_max
#print fin_temps_solar_min
water_vector_solar = []
water_vector_solarmax = []
water_vector_solarmin=[]
water_vector_lab = []
water_vector_labmax =[]
water_vector_labmin= []

for i in fin_temps_solar:
    x = water_loss_value(i)
    water_vector_solar.append(x)
for i in fin_temps_solar_max:
    x = water_loss_value(i)
    water_vector_solarmax.append(x)
for i in fin_temps_solar_min:
    x = water_loss_value(i)
    water_vector_solarmin.append(x)

for i in fin_temps_lab:
    x = water_loss_value(i)
    water_vector_lab.append(x)
for i in fin_temps_lab_max:
    x = water_loss_value(i)
    water_vector_labmax.append(x)
for i in fin_temps_lab_min:
    x = water_loss_value(i)
    water_vector_labmin.append(x)

new_df = pd.DataFrame()
new_df["solar"]= water_vector_solar
new_df["solar lower"]= water_vector_solarmin      
new_df["solar upper"] = water_vector_solarmax
new_df["lab"]= water_vector_lab
new_df["lab upper"] = water_vector_labmax
new_df["lab lower"] = water_vector_labmin

fig, ax = plt.subplots()
ax.plot(test_temps, water_vector_solar, color = "red", label = "Insolated")
ax.plot(test_temps, water_vector_lab, color = "blue", label = "Laboratory", linestyle = "--")
ax.plot(test_temps, water_vector_solarmin, color = "red", linestyle = "")
ax.plot(test_temps, water_vector_labmin, color = "blue", linestyle = "")
ax.plot(test_temps, water_vector_solarmax, color = "red", linestyle = "")
ax.plot(test_temps, water_vector_labmax, color = "blue", linestyle = "" )
ax.fill_between(test_temps, new_df["lab upper"], new_df["lab lower"], color = "blue", alpha = '0.2')
ax.fill_between(test_temps, new_df["solar upper"], new_df["solar lower"], color = "red", alpha = '0.2')

ax.spines["top"].set_visible(False)
ax.spines["right"].set_visible(False)
ax.legend()
ax.set_xlabel("Ambient Temperature (C)")
ax.set_ylabel("Predicted Waterloss (mJ/s/g)")
plt.savefig("/Users/davidstupski/Desktop/water_loss_fig.pdf")  
