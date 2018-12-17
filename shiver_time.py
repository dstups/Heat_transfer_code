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
    alpha_reflect = 0.8735
    #i = 550
    epsilon = .95
    sigma = 5.67*10**-8
    a_surf =.0000731367
    a_inc = a_surf/2
    c = 4.31
    m = 0.04
    dTbdt = -1.0 * hK*(Tb-Ta)/(c*m) + alpha *a_inc*i/(c*m)+alpha_reflect*a_inc*i*.26 - epsilon *sigma*a_surf*((Tb+273.15)**4-(Ta+273.15)**4)/(c*m) + ((-29.83514*Tb+1763.0566)/(1000))/c - (.0022*2.71828**(.24413*Tb))/(1000)/c
    return dTbdt
#mean - lower error value for all paramaters    
def heat_transfermin(Tb, t, i, Ta):
    hK = 0.00334300205882+.00029816/1.96
    #Ta = 10
    alpha = .903-.0081/1.96
    alpha_reflect= 0.8735+ .00557
    #i = 550
    epsilon = .95
    sigma = 5.67*10**-8
    a_surf =.0000731367-.000005
    a_inc = a_surf/2
    c = 4.31
    m = 0.04-.002/1.96
    dTbdt = -1.0 * hK*(Tb-Ta)/(c*m) + alpha *a_inc*i/(c*m)+ alpha_reflect*a_inc*i*.26 - epsilon *sigma*a_surf*((Tb+273.15)**4-(Ta+273.15)**4)/(c*m) + (((-29.83514*Tb+1763.0566-56))/(1000))/c - (.0022*2.71828**(.24413*Tb)-25.81)/(1000)/c
    return dTbdt
#mean + upper error value for all paramaters
def heat_transfermax(Tb, t, i, Ta):
    hK = 0.00334300205882-.00029816/1.96
    #Ta = 10
    alpha = .903+.0081/1.96
    alpha_reflect = 0.8735 +.00557
    epsilon = .95
    sigma = 5.67*10**-8
    a_surf =.0000731367+.000005
    a_inc = a_surf/2
    c = 4.31
    m = 0.04+.002/1.96
    dTbdt = -1.0 * hK*(Tb-Ta)/(c*m) + alpha *a_inc*i/(c*m) + alpha_reflect*a_inc*i*.26  - epsilon *sigma*a_surf*((Tb+273.15)**4-(Ta+273.15)**4)/(c*m) + (((-29.83514*Tb+1763.0566)+56)/(1000))/c - (.0022*2.71828**(.24413*Tb)+25.81)/(1000)/c
    return dTbdt
#initiate numpy array for how many "seconds" we allow the model to run for
t = np.linspace(0,50,500)
#initial temperature of bee, here set to hive temperature
T0= 37.5
#mean bee paramaters + hot july conditions
sol = odeint(heat_transfer, T0, t,args =(1260, 4.5))
solmax= odeint(heat_transfermax, T0, t, args= (1260, 4.5))
solmin = odeint(heat_transfermin, T0, t,args = (1260, 4.5))
sol_vals= []
solmax_vals = []
solmin_vals = []
for x in sol:
    for i in x:
        sol_vals.append(i)
for x in solmax:
    for i in x:
        solmax_vals.append(i)
for x in solmin:
    for i in x:
        solmin_vals.append(i)
#make data frames, necessary for shade between portion      
new_df = pd.DataFrame()
new_df["Mean"]= sol_vals
new_df["Upper"]= solmax_vals      
new_df["Lower"] = solmin_vals
fig, ax = plt.subplots()
ax.plot(t, sol,color = "blue", label = "Simulated Bee Temperature", linestyle = "-")
ax.plot(t, solmax, color = "green", linestyle = "")
ax.plot(t, solmin, color = "yellow", linestyle = "")
ax.fill_between(t, new_df["Upper"], new_df["Lower"], color = "blue", alpha = '0.2')
#plt.axhline(y=sol[-1], color = "r", linestyle = "--", label = "Steady State Solution")
ax.set_title("Predicted Shivering Timing")
ax.set_xlabel("Time (s)")
ax.set_ylabel("Thorax Temperature (C)")
ax.set_xlim(0, 50)
ax.axvline(x = np.where(solmax <35.1)[0][0]/10, color = "red", linestyle = "")
ax.axvline(x = np.where(sol < 35.1)[0][0]/10, color = "red", linestyle = "-", label = "Model Predicted Shivering Timing")
ax.axvline(x=10.0, color = "k", linestyle = "--", label = "Field Observation-Esch")
ax.axvline(x = np.where(solmin <35.1)[0][0]/10, color = "red", linestyle = "")
ax.axvspan(np.where(solmin <35.1)[0][0]/10,np.where(solmax <35.1)[0][0]/10 , color = "red", alpha = 0.2)
ax.legend(loc= "best")
ax.spines["top"].set_visible(False)
ax.spines["right"].set_visible(False)

#plt.savefig("/Users/davidstupski/Desktop/shiver_time.pdf")
#print sol[0]
print np.where(sol < 35.1)[0][0]
print np.where(solmax < 35.1)[0][0]
print np.where(solmin < 35.1)[0][0]
#print np.where(solmax <35.1)
#print np.where(solmin <35.1)

