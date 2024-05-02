#!/usr/bin/env python
# coding: utf-8

# In[47]:


import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sb


# In[13]:


#data acquired from https://web.physics.utah.edu/~wik/courses/astr1060fall2019/hw/nearest_brightest.pdf
#data acquired from http://www.astro.wisc.edu/~dolan/constellations/extra/nearest.html
#data acquired from http://cas.sdss.org/dr7/en/proj/advanced/hr/simplehr.asp
#I tried it with luminosity vs temperature but the graphs seemed to just not fit even with log so i switched to absolute mag vs
#temp
L_B = [22,15000,1.5,110,49,42000,7,9000,1100,12000,90,11,150,70,2200,7500,31,17,258000]
T_B = [9600,7350,5800,4960,9600,12300,6700,3600,15200,23000,5400,7900,4400,6100,23000,3700,5200,8800,9040]
abs_B = [1.4,-2.5,4.4,0.2,0.6,0.4,-8.1,2.6,-1.3,-7.2,-4.4,-4.6,2.3,-0.3,-5.2,-3.2,0.7,2.0,7.2]
L_N = [0.00005,1.5,0.4,0.0004,0.00002,0.005,0.00005,0.00003,22,0.002,0.0004,0.0001,0.3,0.0003,0.08,0.04,0.1,0.006,0.0004]
T_N = [3200,5800,5100,3500,3100,3600,3200,3100,9600,25000,3500,3200,5000,3400,4600,4400,4800,3700,3400]
abs_N = [15.5,4.4,5.7,13.2,16.7,10.5,15.5,16.0,1.4,11.2,13.1,14.8,6.1,13.5,7.6,8.4,7.0,10.4,13.4]

logL_B = list(map(np.log10,L_B))
logT_B = list(map(np.log10,T_B))
logL_N = list(map(np.log10,L_N))
logT_N = list(map(np.log10,T_N))


#logabs_N = list(map(np.log10,abs_N))
#logabs_B = list(map(np.log10,abs_B))

plt.scatter(logT_B,abs_B, marker = '.', c = 'blue', label = 'Brightest Stars');
plt.xlabel('log($T_{eff}$ [K])')
#plt.ylabel(r'log($\frac{L}{L_{{\odot}}})$')
plt.ylabel('absolute magnitude')
plt.title('HR Diagram for Nearest and Brightest Stars')
plt.scatter(logT_N,abs_N, marker = 'x', c = 'red', label = 'Nearest Stars');
plt.legend(loc = "upper right");


# The main differences between the two populations is that the nearest stars mostly form the main sequence, with some of the bright stars on the sequence. The majority of the brightest stars sit in the white dwarves section of the HR Diagram.

# In[71]:


#Q5d
def DistanceofStars(M_abs = 4.8, T = 21):
    D = np.zeros(T)
    numlist = np.arange(T)
    for ind in numlist[:T]:   
        D[ind] = 10**((numlist[ind] - M_abs+5)/5)
        D_stars = D[8:21]
    return D_stars
print(DistanceofStars())


def NumberofStars(Dstars=DistanceofStars()):
    T = 13
    V = np.zeros(T)
    numlist = np.arange(T)
    #print(len(numlist))
    for num in numlist[:T]:
        #for dist in Dstars:
        V[num] = (4*Dstars[num]**3)*(np.pi**2)*(1/2160**2)*(1/3)
        Num_stars = V/25
    return Num_stars
print(NumberofStars()) 


m = list(np.arange(8,21))
log_num_stars = list(map(np.log10,NumberofStars()))
plt.plot(m,log_num_stars,marker = '.', c = 'r', markersize = 10)
plt.xlabel('Apparent Magnitude')
plt.ylabel('Number of Stars in $\log_{10}$')
plt.title('Number of Stars against Apparent Magnitude', fontsize = 13)
plt.show();


# Herschel probably thought we were at the centre of the Milky Way due to the scattering of light by dust for stars further away from us. There was very little visibility outwards from the Sun and the Earth due to this.

# In[ ]:




