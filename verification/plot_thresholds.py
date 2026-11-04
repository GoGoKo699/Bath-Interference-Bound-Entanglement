#!/usr/bin/env python3
"""Plot the exact threshold functions; run after verification/run_all.py."""

from __future__ import annotations

import json
from pathlib import Path

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np

from exact_formulas import thresholds


def main() -> None:
    root = Path(__file__).resolve().parent.parent
    result_path = root / "verification" / "results" / "verification.json"
    if not result_path.exists():
        raise SystemExit("Run python verification/run_all.py before generating the figure.")
    result = json.loads(result_path.read_text(encoding="utf-8"))
    if not all(check["passed"] for check in result["checks"].values()):
        raise SystemExit("The saved verification record does not report a passing run.")

    eta = np.linspace(0.0, 1.0, 501)
    roots = np.asarray([thresholds(float(value)) for value in eta])
    time_ppt, time_eb = roots[:, 0], roots[:, 1]
    plt.rcParams.update({"font.family": "DejaVu Sans", "font.size": 11,
                         "axes.spines.top": False, "axes.spines.right": False,
                         "svg.fonttype": "none", "svg.hashsalt": "bath-interference-thresholds-v1"})
    figure, axis = plt.subplots(figsize=(7.4, 4.9), layout="constrained")
    axis.set_facecolor("#ffffff")
    axis.fill_between(eta, time_ppt, time_eb, color="#f3d99b", alpha=0.9,
                      label="PPT-entangled interval")
    axis.plot(eta, time_eb, color="#913f32", linewidth=2.4,
              label=r"$t_E$: entanglement breaking")
    axis.plot(eta, time_ppt, color="#17657c", linewidth=2.4,
              label=r"$t_P$: PPT / zero two-way capacity")
    axis.scatter([0.0], [time_ppt[0]], color="#28343b", s=28, zorder=5)
    axis.text(0.025, 0.2055, "Measure-and-prepare channels", color="#624039", fontsize=11)
    axis.text(0.025, 0.1595, "Positive two-way quantum capacity", color="#15596d", fontsize=11)
    axis.text(0.72, 0.1813, "PPT and entangled", color="#61470d", fontsize=11,
              ha="center")
    axis.set_xlim(0.0, 1.0)
    axis.set_ylim(0.155, 0.214)
    axis.set_xticks(np.linspace(0.0, 1.0, 6))
    axis.set_yticks([0.16, 0.17, 0.18, 0.19, 0.20, 0.21])
    axis.set_xlabel(r"Bath pathway interference $\eta$")
    axis.set_ylabel(r"Dimensionless evolution time $t$")
    axis.set_title(r"Exact equilibrium thresholds at $\beta=0$", loc="left", pad=13)
    axis.grid(axis="y", color="#e3e7e9", linewidth=0.7, zorder=0)
    axis.legend(loc="upper center", bbox_to_anchor=(0.5, -0.18), ncol=1,
                frameon=False, fontsize=10)
    destination = root / "figures"
    destination.mkdir(exist_ok=True)
    figure.savefig(destination / "thresholds.svg", metadata={"Date": None,
                    "Description": "Exact PPT and entanglement-breaking thresholds near their onset, for the specified infinite-temperature Davies family."})
    svg_path = destination / "thresholds.svg"
    svg_path.write_text("\n".join(line.rstrip() for line in
                       svg_path.read_text(encoding="utf-8").splitlines()) + "\n",
                       encoding="utf-8")
    figure.savefig(destination / "thresholds.png", dpi=180)
    plt.close(figure)
    print("Wrote figures/thresholds.svg and figures/thresholds.png")


if __name__ == "__main__":
    main()
