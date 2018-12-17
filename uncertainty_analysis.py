#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Tue Nov 20 20:22:28 2018

@author: davidstupski
"""

from __future__ import division
import numpy as np
from scipy.integrate import odeint 
import matplotlib.pyplot as plt
from matplotlib import cm
from mpl_toolkits.mplot3d import Axes3D
import pandas as pd
from operator import sub
#Need a script that highlights times of events where thermoregulatory thresholds are broken
plt.style.use("ggplot")
tamb = []
rad = []
sstemp = []
#mean values of all paramaters
#Make a function for each paramater that we'll need to take the partial derivative of the model for 
#then for the correct paramater, add or subtract its standard error of the mean
def heat_transfer(Tb, t, i, Ta):
    hK = 0.00334300205882
    #Ta = 10
    alpha = .903
    #i = 550
    epsilon = .95
    sigma = 5.67*10**-8
    a_surf =.000086722
    a_inc=a_surf/2.
    c = 4.31
    m = 0.04
    dTbdt = -1.0 * hK*(Tb-Ta)/(c*m) + alpha *a_inc*i/(c*m) - epsilon *sigma*a_surf*((Tb+273.15)**4-(Ta+273.15)**4)/(c*m) + ((-29.83514*Tb+1763.0566)/(1000))/c - (.0022*2.71828**(.24413*Tb))/(1000)/c
    return dTbdt
def heat_transferdconv(Tb, t, i, Ta):
    hK = 0.00334300205882 + (.00019085)**2.
    #Ta = 10
    alpha = .903
    #i = 550
    epsilon = .95
    sigma = 5.67*10**-8
    a_surf =.000086722
    a_inc = a_surf/2.
    c = 4.31
    m = 0.04
    dTbdt = -1.0 * hK*(Tb-Ta)/(c*m) + alpha *a_inc*i/(c*m) - epsilon *sigma*a_surf*((Tb+273.15)**4-(Ta+273.15)**4)/(c*m) + ((-29.83514*Tb+1763.0566)/(1000))/c - (.0022*2.71828**(.24413*Tb))/(1000)/c
    return dTbdt
def heat_transferdalpha(Tb, t, i, Ta):
    hK = 0.00334300205882
    #Ta = 10
    alpha = .903+(.003847)**2
    #i = 550
    epsilon = .95
    sigma = 5.67*10**-8
    a_surf =.000086722
    a_inc = a_surf/2.
    c = 4.31
    m = 0.04
    dTbdt = -1.0 * hK*(Tb-Ta)/(c*m) + alpha *a_inc*i/(c*m) - epsilon *sigma*a_surf*((Tb+273.15)**4-(Ta+273.15)**4)/(c*m) + ((-29.83514*Tb+1763.0566)/(1000))/c - (.0022*2.71828**(.24413*Tb))/(1000)/c
    return dTbdt
def heat_transferdsurfA(Tb, t, i, Ta):
    hK = 0.00334300205882
    #Ta = 10
    alpha = .903
    #i = 550
    epsilon = .95
    sigma = 5.67*10**-8
    a_surf =.000086722+(8.027*10**-7)**2
    a_inc= a_surf/2.
    c = 4.31
    m = 0.04
    dTbdt = -1.0 * hK*(Tb-Ta)/(c*m) + alpha *a_inc*i/(c*m) - epsilon *sigma*a_surf*((Tb+273.15)**4-(Ta+273.15)**4)/(c*m) + ((-29.83514*Tb+1763.0566)/(1000))/c - (.0022*2.71828**(.24413*Tb))/(1000)/c
    return dTbdt
def heat_transferdmetbeta2(Tb, t, i, Ta):
    hK = 0.00334300205882
    #Ta = 10
    alpha = .903
    #i = 550
    epsilon = .95
    sigma = 5.67*10**-8
    a_surf =.000086722
    a_inc= a_surf/2.
    c = 4.31
    m = 0.04
    dTbdt = -1.0 * hK*(Tb-Ta)/(c*m) + alpha *a_inc*i/(c*m) - epsilon *sigma*a_surf*((Tb+273.15)**4-(Ta+273.15)**4)/(c*m) + (((-29.83514+3.33958^2)*Tb+1763.0566)/(1000))/c - (.0022*2.71828**(.24413*Tb))/(1000)/c
    return dTbdt
def heat_transferdmetbeta3(Tb, t, i, Ta):
    hK = 0.00334300205882
    #Ta = 10
    alpha = .903
    #i = 550
    epsilon = .95
    sigma = 5.67*10**-8
    a_surf =.000086722
    a_inc= a_surf/2.
    c = 4.31
    m = 0.04
    dTbdt = -1.0 * hK*(Tb-Ta)/(c*m) + alpha *a_inc*i/(c*m) - epsilon *sigma*a_surf*((Tb+273.15)**4-(Ta+273.15)**4)/(c*m) + ((-29.83514*Tb+(1763.0566+)/(1000))/c - (.0022*2.71828**(.24413*Tb))/(1000)/c
    return dTbdt
def heat_transferdevapbeta4(Tb, t, i, Ta):
    hK = 0.00334300205882
    #Ta = 10
    alpha = .903
    #i = 550
    epsilon = .95
    sigma = 5.67*10**-8
    a_surf =.000086722
    a_inc= a_surf/2.
    c = 4.31
    m = 0.04
    dTbdt = -1.0 * hK*(Tb-Ta)/(c*m) + alpha *a_inc*i/(c*m) - epsilon *sigma*a_surf*((Tb+273.15)**4-(Ta+273.15)**4)/(c*m) + ((-29.83514*Tb+1763.0566)/(1000))/c - (.0022*2.71828**(.24413*Tb))/(1000)/c
    return dTbdt
def heat_transferdevapdata5(Tb, t, i, Ta):
    hK = 0.00334300205882
    #Ta = 10
    alpha = .903
    #i = 550
    epsilon = .95
    sigma = 5.67*10**-8
    a_surf =.000086722
    a_inc= a_surf/2.
    c = 4.31
    m = 0.04
    dTbdt = -1.0 * hK*(Tb-Ta)/(c*m) + alpha *a_inc*i/(c*m) - epsilon *sigma*a_surf*((Tb+273.15)**4-(Ta+273.15)**4)/(c*m) + ((-29.83514*Tb+1763.0566)/(1000))/c - (.0022*2.71828**(.24413*Tb))/(1000)/c
    return dTbdt
def heat_transferdmass(Tb, t, i, Ta):
    hK = 0.00334300205882
    #Ta = 10
    alpha = .903
    #i = 550
    epsilon = .95
    sigma = 5.67*10**-8
    a_surf =.0000731367
    a_inc= a_surf/2.
    c = 4.31
    m = 0.04
    dTbdt = -1.0 * hK*(Tb-Ta)/(c*m) + alpha *a_inc*i/(c*m) - epsilon *sigma*a_surf*((Tb+273.15)**4-(Ta+273.15)**4)/(c*m) + ((-29.83514*Tb+1763.0566)/(1000))/c - (.0022*2.71828**(.24413*Tb))/(1000)/c
    return dTbdt
#create time vector
t = np.linspace(0,250,500)
#Declare initial temp
T0= 38
#Youll need to creat a bunch of lists to eventually store the important parts
#of the numpy arrays that you'll get from the odeint function-you wont remember why
#later, but just remember that this makes things a lot easier when you come back to this
#, future David, or future dumbass who joined this lab
average = []
dconv = []
dalpha= []
dsolsurf = []
dsurf=[]
dmetbeta2=[]
dmetbeta3=[]
devapbeta4=[]
devapbeta5=[]

#set up simulations for each variable for which you're taking the partial derivative
modelaverage = odeint(heat_transfer, T0, t,args =(1200, 32))
modeldconv = odeint(heat_transferdconv, T0, t,args =(1200, 32))
modeldalpha = odeint(heat_transferdalpha, T0, t,args =(1200, 32))
modeldsurf = odeint(heat_transferdsurfA, T0, t,args =(1200, 32))
modeldmetbeta2= odeint(heat_transferdmetbeta2, T0, t,args =(1200, 32))
modeldmetbeta3=odeint(heat_transferdmetbeta3, T0, t,args =(1200, 32))
modeldevapbeta4=odeint(heat_transferdevapbeta4, T0, t,args =(1200, 32))
modeldevapbeta5=odeint(heat_transferdevapdata5, T0, t,args =(1200, 32))
#modeldmass=odeint(heat_transferdmass, T0, t,args =(1200, 32))

#put numpy arrays into their appropriate lists
for x in modelaverage:
    for i in x:
        average.append(i)
for x in modeldconv:
    for i in x:
        dconv.append(i)
for x in modeldalpha:
    for i in x:
        dalpha.append(i)
for x in modeldsurf:
    for i in x:
        dsurf.append(i)
for x in modeldmetbeta2:
    for i in x:
        dmetbeta2.append(i)
for x in modeldmetbeta3:
    for i in x:
        dmetbeta3.append(i)
for x in modeldevapbeta4:
    for i in x:
        devapbeta4.append(i)
for x in modeldevapbeta5:
    for i in x:
        devapbeta5.append(i)
#test printing before we get too far
#print average
#print dconv 
#print dalpha
#print dsolsurf
#print dradsurf
#print dmetbeta2
#print dmetbeta3
#print devapbeta4
#print devapbeta5
#so far so good
        
#now we need to summate the model difference from the mean for each variable simulation
# at each time point in the simulation vector, this will become the upper model limit
#Perhaps creat a list of lists and cycle through each one and 
#map function makes this pretty easy
#create a mapping of the derivative run and the average model and another divided by the magnitude of the standard error        
dconv_exec = map(sub, dconv,average)
dalpha_exec =map(sub, dalpha,average)
dsurf_exec=map(sub, dsurf,average)
dmetbeta2_exec=map(sub, dmetbeta2,average)
dmetbeta3_exec=map(sub, dmetbeta3,average)
devapbeta4_exec= map(sub, devapbeta4,average)
devapbeta5_exec = map(sub, devapbeta5,average)

##Now Summate the dModel/d
