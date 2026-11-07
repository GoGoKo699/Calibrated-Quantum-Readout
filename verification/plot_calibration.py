"""Regenerate science/figures/calibration.svg from the exact analytic fraction."""

from pathlib import Path

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np

from readout import calibration_fraction


def main():
    plt.rcParams.update({"font.family": "DejaVu Sans", "font.size": 11,
                         "axes.spines.top": False, "axes.spines.right": False,
                         "svg.fonttype": "none", "svg.hashsalt": "calibrated-readout"})
    epsilon = np.geomspace(1e-10, 0.4, 700)
    fig, ax = plt.subplots(figsize=(7.4, 4.5), layout="constrained")
    for delta, color in ((1e-4, "#007C91"), (1e-3, "#7655A3"), (1e-2, "#CF6933")):
        ax.semilogx(epsilon, calibration_fraction(epsilon, 1 - epsilon, delta, 2),
                    linewidth=2.2, color=color, label=f"Basis error δ = {delta:g} rad")
    ax.axhline(0.25, color="#394451", linewidth=1.4, linestyle="--", label="Exact calibration: 1/4")
    ax.scatter([1e-6], [calibration_fraction(1e-6, 1 - 1e-6, 1e-3, 2)],
               s=40, color="#7655A3", zorder=5)
    ax.annotate("ε = 10⁻⁶, δ = 10⁻³\nRetained fraction ≈ 0.125", xy=(1e-6, 0.125),
                xytext=(1e-8, 0.17), fontsize=10,
                bbox={"facecolor": "white", "edgecolor": "none", "alpha": 0.92, "pad": 2.5},
                arrowprops={"arrowstyle": "-", "color": "#7655A3"})
    ax.set(xlim=(epsilon[0], epsilon[-1]), ylim=(0, 0.265),
           xlabel="Weak occupied eigenvalue ε", ylabel="Retained Fisher fraction Iδ / Jφ",
           title="Calibration sensitivity in a rank-two qutrit")
    ax.grid(axis="y", alpha=0.18)
    ax.legend(loc="lower right", frameon=False, fontsize=9)
    destination = Path(__file__).resolve().parents[1] / "science/figures/calibration.svg"
    destination.parent.mkdir(parents=True, exist_ok=True)
    fig.savefig(destination, metadata={"Date": None})
    print(destination)


if __name__ == "__main__":
    main()
