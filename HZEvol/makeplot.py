#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import division, print_function, absolute_import, unicode_literals
import matplotlib.pyplot as plt
import vplot as vpl
import subprocess as subp
from pylab import *

# Check correct number of arguments
if (len(sys.argv) != 2):
    print('ERROR: Incorrect number of arguments.')
    print('Usage: '+sys.argv[0]+' <pdf | png>')
    exit(1)
if (sys.argv[1] != 'pdf' and sys.argv[1] != 'png'):
    print('ERROR: Unknown file format: '+sys.argv[1])
    print('Options are: pdf, png')
    exit(1)

# Run the sims
subp.call('cd Kopparapu; vplanet vpl.in',shell=True)
print("Completed Kopparapu simulation.")
subp.call('cd DryLimits; vplanet vpl.in',shell=True)
print("Completed DryLimits simulation.")

# First plot traditional HZ
output = vpl.GetOutput('Kopparapu')

rc('axes',linewidth=2)
plt.rcParams['xtick.major.pad']='8'
plt.rcParams['ytick.major.pad']='5'
plt.rcParams['xtick.major.size'] = 10
plt.rcParams['xtick.major.width'] = 2
plt.rcParams['xtick.minor.size'] = 5
plt.rcParams['xtick.minor.width'] = 1
plt.rcParams['ytick.major.size'] = 10
plt.rcParams['ytick.major.width'] = 2
plt.rcParams['ytick.minor.size'] = 5
plt.rcParams['ytick.minor.width'] = 1

plt.figure(figsize=(7,6), dpi=300)

# Make font size smaller
plt.rcParams.update({'font.size': 18})

vpl.plot(plt.gca(),output.star.Time,output.star.HZLimMoistGreenhouse,color=vpl.colors.pale_blue,label='')
vpl.plot(plt.gca(),output.star.Time,output.star.HZLimMaxGreenhouse,color=vpl.colors.pale_blue,label='')

fbk = {'lw':0.0, 'edgecolor':None}
plt.fill_between(output.star.Time,output.star.HZLimMoistGreenhouse,output.star.HZLimMaxGreenhouse,facecolor=vpl.colors.pale_blue,**fbk)

# Now get dry limits
output = vpl.GetOutput('DryLimits')

vpl.plot(plt.gca(),output.a0.Time,output.a0.HZLimitDryRunaway,color=vpl.colors.red,linestyle='dotted',label='A=0')
vpl.plot(plt.gca(),output.a0.Time,output.a05.HZLimitDryRunaway,color=vpl.colors.red,linestyle='dashed',label='A=0.5')
vpl.plot(plt.gca(),output.a0.Time,output.a08.HZLimitDryRunaway,color=vpl.colors.red,label='A=0.8')

# Fuss with figure
plt.ylabel('Orbital Distance (AU)')
plt.plot([0,1e9],[0.387,0.387],linestyle='dashed',color='k',lw=2)
plt.plot([0,1e9],[0.0485,0.0485],linestyle='solid',color='k',lw=2)
plt.text(1.1e6,0.027,'Orbit of Proxima b',color='k',fontsize=15)
plt.text(1e8,0.365,'Orbit of Mercury',color='k',fontsize=15)
plt.text(2e6,0.16,'Habitable Zone',color='w',rotation=320)
plt.text(2e6,0.095,'Dry Limits',color=vpl.colors.red,rotation=338,fontsize=15)
plt.legend(loc='best',fontsize=15)

plt.ylim(0,0.5)
plt.xlim(1e6,1e9)
plt.xscale('log')
plt.xlabel('Time (years)')

plt.tight_layout()

if (sys.argv[1] == 'pdf'):
    plt.savefig('hzevol.pdf', bbox_inches="tight", dpi=600)
if (sys.argv[1] == 'png'):
    plt.savefig('hzevol.png', bbox_inches="tight", dpi=600)
