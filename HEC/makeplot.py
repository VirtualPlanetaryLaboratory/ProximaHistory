import vplot
import matplotlib.pyplot as plt
import numpy as np

out = vplot.GetOutput()

fig, ax = plt.subplots(2, 2, figsize=(14, 7.5))
fig.subplots_adjust(wspace=0.35, right=0.85)

bodies = [out.b00, out.b01, out.b02, out.b03, out.b04]
colors = ["red", "blue", "orange", "purple", "cyan"]
labels = [
    r"$f_H = 0.01$",
    r"$f_H = 0.001$",
    r"$f_H = 0.0005$",
    r"$f_H = 0.0001$",
    r"$f_H = 0$",
]
for body, label, color in zip(bodies, labels, colors):
    ax[0, 0].plot(body.Time, body.EnvelopeMass, color=color)
    ax[0, 1].plot(body.Time, body.SurfWaterMass, color=color)
    ax[1, 0].plot(body.Time, body.OxygenMass, color=color)
    ax[1, 1].plot(body.Time, body.XO, color=color, label=label)

ax[0, 0].set_ylabel("Envelope Mass (Earth)")
ax[0, 0].set_yscale("log")

ax[0, 1].set_ylabel("Water Mass (TO)")
ax[0, 1].set_yscale("log")

ax[1, 0].set_ylabel(r"O$_2$ Pressure (bars)")
ax[1, 0].set_ylim(-10, 310)

ax[1, 1].set_ylabel(r"O$_2$ Mixing Ratio")
ax[1, 1].set_ylim(-0.01, 1.01)

for axis in ax.flatten():
    axis.set_xlabel("Time (years)")
    axis.set_xscale("log")
    axis.set_xlim(1e6, 4.78e9)

l = plt.legend(
    bbox_to_anchor=(1.04, 1.1),
    loc="center left",
    borderaxespad=0,
    title="Initial Envelope\n Mass Fraction",
)
plt.setp(l.get_title(), fontsize=10)
fig.savefig("h_and_h2o.pdf", bbox_inches="tight")
