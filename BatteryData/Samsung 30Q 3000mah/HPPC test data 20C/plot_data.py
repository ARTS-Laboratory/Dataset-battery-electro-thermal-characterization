# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import IPython as IP
IP.get_ipython().magic('reset -sf')

import numpy as np
import scipy as sp
import pandas as pd
from scipy import fftpack, signal # have to add 
import matplotlib as mpl
import matplotlib.pyplot as plt
import sklearn as sk
import time as time
from sklearn import linear_model
from sklearn import pipeline
from sklearn import datasets
from sklearn import multiclass
import json as json


# set default fonts and plot colors
plt.rcParams.update({'image.cmap': 'viridis'})
cc = plt.rcParams['axes.prop_cycle'].by_key()['color']
plt.rcParams.update({'font.serif':['Times New Roman', 'Times', 'DejaVu Serif',
 'Bitstream Vera Serif', 'Computer Modern Roman', 'New Century Schoolbook',
 'Century Schoolbook L',  'Utopia', 'ITC Bookman', 'Bookman', 
 'Nimbus Roman No9 L', 'Palatino', 'Charter', 'serif']})
plt.rcParams.update({'font.family':'serif'})
plt.rcParams.update({'font.size': 10})
plt.rcParams.update({'mathtext.rm': 'serif'})
plt.rcParams.update({'mathtext.fontset': 'custom'})
plt.close('all')


rc = {"font.family" : "serif", 
      "mathtext.fontset" : "stix"}
plt.rcParams.update(rc)
plt.rcParams["font.serif"] = ["Times New Roman"] + plt.rcParams["font.serif"]

plt.close('all')





#%% plot the surfface map

#file = '5%SoCsteps_5_16_2023'
file = '10%SoCsteps_5_16_23'

D = np.loadtxt(file+'.txt',skiprows=12)

# time, Current, Voltage, Power, Battery Temp, and Chamber Temp

tt = D[:,0]/3600
cr = D[:,1]
vo = D[:,2]
po = D[:,3]
bt = D[:,4]
ct = D[:,5]




fig, ax = plt.subplots(ncols=1,nrows=2,figsize=(6,5))
ax[0].set_title('data for '+file)
ax1 = ax[0]
ax2 = ax1.twinx()
ax1.plot(tt,cr,color=cc[0],label='current')
ax2.plot(tt,vo,color=cc[1],label='voltage')
fig.legend(framealpha=1,loc='upper right', bbox_to_anchor=(0.89, 0.93))
ax1.set_ylabel('current (A)')
ax2.set_ylabel('voltage (V)')


ax[1].plot(tt,ct,label='chamber')
ax[1].plot(tt,bt,label='battery')
ax[1].grid('on')
ax[1].legend(framealpha=1)
ax[1].set_xlabel('time (hr)')
ax[1].set_ylabel('temperature (C$^\circ$)')
plt.tight_layout()

plt.savefig('plots/'+file,dpi=300)



#%% plot the data is two plots

# fig, ax1 = plt.subplots(figsize=(6,4))
# ax2 = ax1.twinx()
# ax1.plot(tt,cr,color=cc[0],label='current')
# ax2.plot(tt,vo,color=cc[1],label='voltage')
# ax2.legend(framealpha=1)
# ax1.set_xlabel('time (s)')
# ax1.set_ylabel('current (A)')
# ax2.set_ylabel('voltage (V)')
# plt.tight_layout()


# plt.figure(figsize=(6,4))
# plt.plot(tt,ct,label='chamber')
# plt.plot(tt,bt,label='battery')
# plt.grid('on')
# plt.legend(framealpha=1)
# plt.xlabel('time (s)')
# plt.ylabel('temperature (C$^\circ$)')
# plt.tight_layout()


















