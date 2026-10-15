import csv
from pathlib import Path
import matplotlib.pyplot as plt

ROOT = Path(__file__).resolve().parent
FILES = ["kimi_opus_effort_data.csv", "glm53_effort_data.csv", "sonnet5_effort_data.csv"]

rows = []
for fn in FILES:
    with open(ROOT / fn, encoding="utf-8-sig", newline="") as f:
        for r in csv.DictReader(f):
            rows.append((
                r["Model"], r["Effort"], float(r["Cost USD/task"]),
                int(r["Intelligence Index"]), int(r["Output k"]), int(r["Reasoning k"])
            ))

COLORS = {
    "Kimi K3":"#1f77b4", "GLM-5.3":"#9467bd", "Opus 5":"#ff7f0e",
    "Opus 5.5":"#2ca02c", "Sonnet 5":"#d62728"
}
ORDER = ["Kimi K3","GLM-5.3","Opus 5","Opus 5.5","Sonnet 5"]

COST_OFF = {
("Kimi K3","Low"):(15,-19),("Kimi K3","Max"):(-18,-30),
("GLM-5.3","Low"):(16,18),("GLM-5.3","Max"):(20,23),
("Opus 5","Low"):(18,-8),("Opus 5","Medium"):(20,-30),("Opus 5","High"):(20,-27),("Opus 5","XHigh"):(20,-25),("Opus 5","Max"):(-18,-29),
("Opus 5.5","Low"):(18,20),("Opus 5.5","Medium"):(-18,28),("Opus 5.5","High"):(20,23),("Opus 5.5","XHigh"):(20,25),("Opus 5.5","Max"):(-18,28),
("Sonnet 5","High"):(20,-18),("Sonnet 5","XHigh"):(20,-21),("Sonnet 5","Max"):(20,-18)
}
TOKEN_OFF = {
("Kimi K3","Low"):(15,-20),("Kimi K3","Max"):(-18,-29),
("GLM-5.3","Low"):(18,17),("GLM-5.3","Max"):(18,-29),
("Opus 5","Low"):(17,-8),("Opus 5","Medium"):(18,-29),("Opus 5","High"):(18,19),("Opus 5","XHigh"):(18,-26),("Opus 5","Max"):(18,-26),
("Opus 5.5","Low"):(17,21),("Opus 5.5","Medium"):(-18,28),("Opus 5.5","High"):(18,25),("Opus 5.5","XHigh"):(18,26),("Opus 5.5","Max"):(-18,28),
("Sonnet 5","High"):(-18,-22),("Sonnet 5","XHigh"):(18,-20),("Sonnet 5","Max"):(18,-22)
}

def draw(kind, output):
    fig, ax = plt.subplots(figsize=(23,14))
    idx = 2 if kind == "cost" else 4
    for model in ORDER:
        pts = [r for r in rows if r[0] == model]
        ax.plot([r[idx] for r in pts], [r[3] for r in pts], "-o",
                lw=1.7, ms=8, color=COLORS[model], label=model, zorder=5)

    offsets = COST_OFF if kind == "cost" else TOKEN_OFF
    for model, effort, cost, score, output_k, reasoning_k in rows:
        x = cost if kind == "cost" else output_k
        dx, dy = offsets[(model, effort)]
        detail = (f"${cost:.2f} · {score} pts · {output_k}k out · {reasoning_k}k reason"
                  if kind == "cost" else
                  f"{output_k}k out · {score} pts · {reasoning_k}k reason · ${cost:.2f}")
        ax.annotate(f"{model} · {effort}\n{detail}", (x, score),
                    xytext=(dx,dy), textcoords="offset points",
                    ha="left" if dx > 0 else "right", va="center", fontsize=7.4,
                    bbox=dict(boxstyle="round,pad=.22", fc="white",
                              ec=COLORS[model], lw=.75, alpha=.97),
                    arrowprops=dict(arrowstyle="-", lw=.85, color=COLORS[model],
                                    linestyle=(0,(2,2)), shrinkA=3, shrinkB=6),
                    zorder=4)

    ax.set_ylim(22,64)
    ax.grid(alpha=.16)
    ax.legend(loc="upper left", ncol=5)
    ax.set_ylabel("Artificial Analysis Intelligence Index v4.3.2 — higher is better")

    if kind == "cost":
        ax.set_xlim(0,7.4)
        ax.set_xlabel("Cost per benchmark task (USD) — lower is better")
        ax.set_title("Kimi K3 · GLM-5.3 · Opus 5 · Opus 5.5 · Sonnet 5 — Cost vs Performance", fontsize=17)
    else:
        ax.set_xlim(0,145)
        ax.set_xlabel("Output tokens per benchmark task (thousands) — lower is better")
        ax.set_title("Kimi K3 · GLM-5.3 · Opus 5 · Opus 5.5 · Sonnet 5 — Output Tokens vs Performance", fontsize=17)

    ax.text(.01,-.065, "Source: Artificial Analysis · Sonnet 5 includes High / XHigh / Max only.",
            transform=ax.transAxes, fontsize=9)
    plt.tight_layout()
    fig.savefig(ROOT / output, dpi=300, bbox_inches="tight")
    plt.close(fig)

draw("cost", "effort_cost_with_sonnet5.png")
draw("tokens", "effort_tokens_with_sonnet5.png")
print("Rendered both charts from CSV.")
