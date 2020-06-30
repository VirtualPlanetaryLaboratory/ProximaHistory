from __future__ import division, print_function, absolute_import, unicode_literals
import matplotlib.pyplot as plt
import vplot as vpl
import numpy as np


# Grab the output from a run
output = vpl.GetOutput()

# Set up a matplotlib plot as usual
fig, ax = plt.subplots(3, 2, figsize = (8, 8))

# Make font size smaller
plt.rcParams.update({'font.size': 10})

for planet in output.bodies:
	vpl.plot(ax[0,0], output.earth.Time, planet.RadPowerTotal)
	vpl.plot(ax[0,1], output.earth.Time, planet.TMan)
	vpl.plot(ax[1,0], output.earth.Time, planet.RIC)
	vpl.plot(ax[1,1], output.earth.Time, planet.MagMom)
	vpl.plot(ax[2,0], output.earth.Time, planet.MagPauseRad*9.103)
	vpl.plot(ax[2,1], output.earth.Time, planet.SurfEnFluxTotal)

ax[0,0].set_ylabel("Radiogenic Power (TW)")
ax[0,0].set_ylim([10e-1,10e3])
ax[0,0].plot([0,7],[20,20],linestyle='dashed',color='k',alpha=0.8)
ax[0,0].set_yscale('log')
ax[0,0].set_xlabel("")

ax[0,1].set_xlabel("")
ax[0,1].set_ylim([2000,3000])

ax[1,0].set_xlabel("")
ax[1,0].plot([0,7],[1220,1220],linestyle='dashed',color='k',alpha=0.8)
ax[1,0].set_ylim([0,3500])

ax[1,1].set_ylabel("Magnetic Moment (Earth Units)")
ax[1,1].legend(['Earth','Chondritic','Inert','26Al'])
ax[1,1].set_ylim([0,5])
ax[1,1].set_xlabel("")

ax[2,0].set_ylabel("Magnetopause Radius (R$_\oplus$)")
#ax[2,0].plot([0,7],[8,8],linestyle='dashed',color='k',alpha=0.8)
ax[2,0].set_ylim([6,14])
ax[2,0].set_xlabel("Time (Gyrs)")

ax[2,1].set_ylabel("Surface Flux (W/m$^2$)")
ax[2,1].plot([0,7],[0.8e-1,0.8e-1],linestyle='dashed',color='k',alpha=0.8)
ax[2,1].set_yscale('log')
ax[2,1].set_ylim([10e-3,10e0])
ax[2,1].set_xlabel("Time (Gyrs)")

#plt.suptitle('Radioactive Models')

vpl.show()
