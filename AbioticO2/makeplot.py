import vplot
import matplotlib.pyplot as plt
import numpy as np

out = vplot.GetOutput()

fig, ax = plt.subplots(2, 2, figsize=(14, 7.5))
fig.subplots_adjust(wspace=0.25)

bodies = [out.b00, out.b01, out.b02, out.b03, out.b04, out.b05, out.b06, out.b07]
colors = ["cyan", "cyan", "purple", "purple", "orange", "orange", "blue", "blue"]
styles = [
    "-",
    "--",
    "-",
    "--",
    "-",
    "--",
    "-",
    "--",
]
labels = [
    r"1 TO, No O$_2$ Sink",
    r"1 TO, Instant Sink",
    r"3 TO, No O$_2$ Sink",
    r"3 TO, Instant Sink",
    r"5 TO, No O$_2$ Sink",
    r"5 TO, Instant Sink",
    r"10 TO, No O$_2$ Sink",
    r"10 TO, Instant Sink",
]
for body, label, color, style in zip(bodies, labels, colors, styles):
    ax[0, 0].plot(body.Time, body.SurfWaterMass, color=color, ls=style, lw=1.5)
    ax[0, 1].plot(body.Time, body.XO, color=color, ls=style, lw=1.5)
    ax[1, 0].plot(
        body.Time,
        body.OxygenMass + body.OxygenMantleMass,
        color=color,
        label=label,
        ls=style,
        lw=1.5,
    )

ax[1, 1].axis("off")

ax[0, 0].set_ylabel("Water Mass (TO)")
ax[0, 0].set_yscale("log")

ax[0, 1].set_ylabel(r"O$_2$ Mixing Ratio")
ax[0, 1].set_ylim(-0.05, 1.05)

ax[1, 0].set_ylabel(r"O$_2$ Pressure (bars)")
ax[1, 0].set_ylim(-30, 1100)


for axis in ax.flatten():
    axis.set_xlabel("Time (years)")
    axis.set_xscale("log")
    axis.set_xlim(1e6, 4.78e9)

l = ax[1, 0].legend(
    bbox_to_anchor=(1.3, 0.5),
    loc="center left",
    borderaxespad=0,
    title="Initial Water Content",
    ncol=2,
    fontsize=11,
)
plt.setp(l.get_title(), fontsize=12)
fig.savefig("h2o.pdf", bbox_inches="tight")
