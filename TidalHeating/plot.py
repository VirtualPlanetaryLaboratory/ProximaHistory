from __future__ import division, print_function, absolute_import, unicode_literals
import matplotlib.pyplot as plt
import vplot as vpl

output = vpl.GetOutput('.')
fig, ax = plt.subplots(3, 3, figsize = (12, 8))
plt.rcParams.update({'font.size': 10})

vpl.plot(ax[0,0], output.b_low.Time, output.b_low.PowerEqtide, color = vpl.colors.pale_blue); vpl.plot(ax[0,0], output.b_med.Time, output.b_med.PowerEqtide, color = vpl.colors.orange); vpl.plot(ax[0,0], output.b_high.Time, output.b_high.PowerEqtide, color = vpl.colors.purple)
vpl.plot(ax[0,1], output.b_low.Time, output.b_low.TMan, color = vpl.colors.pale_blue); vpl.plot(ax[0,1], output.b_med.Time, output.b_med.TMan, color = vpl.colors.orange); vpl.plot(ax[0,1], output.b_high.Time, output.b_high.TMan, color = vpl.colors.purple)
vpl.plot(ax[0,2], output.b_low.Time, output.b_low.RIC, color = vpl.colors.pale_blue); vpl.plot(ax[0,2], output.b_med.Time, output.b_med.RIC, color = vpl.colors.orange); vpl.plot(ax[0,2], output.b_high.Time, output.b_high.RIC, color = vpl.colors.purple)

vpl.plot(ax[1,0], output.b_low.Time, output.b_low.MagMom, color = vpl.colors.pale_blue); vpl.plot(ax[1,0], output.b_med.Time, output.b_med.MagMom, color = vpl.colors.orange); vpl.plot(ax[1,0], output.b_high.Time, output.b_high.MagMom, color = vpl.colors.purple)
vpl.plot(ax[1,1], output.b_low.Time, output.b_low.MagPauseRad*9.103, color = vpl.colors.pale_blue); vpl.plot(ax[1,1], output.b_med.Time, output.b_med.MagPauseRad*9.103, color = vpl.colors.orange); vpl.plot(ax[1,1], output.b_high.Time, output.b_high.MagPauseRad*9.103, color = vpl.colors.purple)
vpl.plot(ax[1,2], output.b_low.Time, output.b_low.SurfEnFluxTotal, color = vpl.colors.pale_blue, label='e=0.05'); vpl.plot(ax[1,2], output.b_med.Time, output.b_med.SurfEnFluxTotal, color = vpl.colors.orange, label='e=0.1'); vpl.plot(ax[1,2], output.b_high.Time, output.b_high.SurfEnFluxTotal, color = vpl.colors.purple, label='e=0.2')

vpl.plot(ax[2,0], output.b_low.Time, output.b_low.Eccentricity, color = vpl.colors.pale_blue); vpl.plot(ax[2,0], output.b_med.Time, output.b_med.Eccentricity, color = vpl.colors.orange); vpl.plot(ax[2,0], output.b_high.Time, output.b_high.Eccentricity, color = vpl.colors.purple)
vpl.plot(ax[2,1], output.b_low.Time, output.b_low.TidalQ, color = vpl.colors.pale_blue); vpl.plot(ax[2,1], output.b_med.Time, output.b_med.TidalQ, color = vpl.colors.orange); vpl.plot(ax[2,1], output.b_high.Time, output.b_high.TidalQ, color = vpl.colors.purple)
vpl.plot(ax[2,2], output.b_low.Time, output.b_low.SemiMajorAxis, color = vpl.colors.pale_blue), vpl.plot(ax[2,2], output.b_med.Time, output.b_med.SemiMajorAxis, color = vpl.colors.orange); vpl.plot(ax[2,2], output.b_high.Time, output.b_high.SemiMajorAxis, color = vpl.colors.purple)

# Add legends
ax[0,0].set_xlabel(''); ax[0,0].set_ylabel('Tidal Power (TW)'); ax[0,0].set_yscale('log'); ax[0,0].set_ylim(10e-1,10e2)
ax[0,1].set_xlabel(''); ax[0,1].set_ylabel('Mantle Temp. (K)'); #ax[0,1].set_ylim(2000,3000)
ax[0,2].set_xlabel(''); ax[0,2].set_ylabel('Inner Core Radius (km)'); ax[0,2].set_ylim(0,3500)

ax[1,0].set_xlabel(''); ax[1,0].set_ylabel('Mag. Mom.'); #ax[1,0].set_ylim(50,150)
ax[1,1].set_xlabel(''); ax[1,1].set_ylabel('Magnetopause Radius (R_$\oplus$)'); #ax[1,1].set_ylim(8,11)
ax[1,2].set_xlabel(''); ax[1,2].set_ylabel('Surface Flux'); ax[1,2].legend(); ax[1,2].set_ylim(0,1)

ax[2,0].set_ylabel('Eccentricity'); ax[2,0].set_ylim(0,0.4)
ax[2,1].set_ylabel('Tidal Q'); #ax[2,1].set_ylim(100,1000)
ax[2,2].set_ylabel('Semi-Major Axis'); #ax[2,2].set_ylim(0.049,0.051)

# Add a title
#plt.suptitle('Tidal Models')

# Show it
vpl.show()
