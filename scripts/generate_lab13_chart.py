"""Gráfico de LAB13: tablero de las cinco puertas técnicas del DSS.

Lee reports/lab13/deployment_decision.json y configs/governance.yml, y escribe
reports/lab13/graficos/puertas_gobernanza.png. Ejecutar con:

    uv run python scripts/generate_lab13_chart.py
"""

import json
from pathlib import Path

import matplotlib.pyplot as plt
import yaml

decision = json.loads(Path("reports/lab13/deployment_decision.json").read_text(encoding="utf-8"))
gates = yaml.safe_load(Path("configs/governance.yml").read_text(encoding="utf-8"))["gates"]

TINTA, TINTA_2, TENUE = "#0B0B0B", "#52514E", "#898781"
REJILLA, FONDO = "#E1E0D9", "#FFFFFF"
# Insignias pastel con icono oscuro: el estado siempre va con icono y texto, nunca solo color.
BIEN, BIEN_ICONO = "#C9DCEE", "#2E4F73"
CRITICO, CRITICO_ICONO = "#F2C9C4", "#8A2E27"

m, g, r = decision["metrics"], decision["gaps"], decision["resources"]
filas = [
    ("Recall global", f"{m['recall'] * 100:.2f} %", f"≥ {gates['min_recall'] * 100:.0f} %", "recall"),
    ("Brecha de recall", f"{g['recall_gap'] * 100:.2f} pp", f"≤ {gates['max_recall_gap'] * 100:.0f} pp", "recall_gap"),
    ("Brecha de FPR", f"{g['fpr_gap'] * 100:.2f} pp", f"≤ {gates['max_fpr_gap'] * 100:.0f} pp", "fpr_gap"),
    ("Latencia por caso", f"{r['latency_ms']:.4f} ms", f"≤ {gates['max_latency_ms']} ms", "latency"),
    ("Tamaño del modelo", f"{r['model_kb']:.2f} KB", f"≤ {gates['max_model_kb']:,} KB", "model_size"),
]

plt.rcParams.update({"font.family": "sans-serif", "font.sans-serif": ["Segoe UI", "DejaVu Sans", "Arial"]})
fig, ax = plt.subplots(figsize=(10, 5.2), facecolor=FONDO)
ax.set_xlim(0, 10)
ax.set_ylim(len(filas) + 0.9, -0.6)
ax.axis("off")

cols = {"Puerta": 0.2, "Observado": 4.3, "Umbral": 6.4, "Estado": 8.3}
for nombre, x in cols.items():
    ax.text(x, -0.15, nombre.upper(), color=TENUE, fontsize=9.5, fontweight="bold", va="center")
ax.plot([0.1, 9.9], [0.25, 0.25], color=TINTA_2, linewidth=1)

for i, (puerta, observado, umbral, clave) in enumerate(filas, start=1):
    y = i - 0.25
    ok = decision["decision"]["checks"][clave]
    ax.text(cols["Puerta"], y, puerta, color=TINTA, fontsize=12, va="center")
    ax.text(cols["Observado"], y, observado, color=TINTA, fontsize=12, va="center", fontweight="bold")
    ax.text(cols["Umbral"], y, umbral, color=TINTA_2, fontsize=12, va="center")
    color, icono = (BIEN, BIEN_ICONO) if ok else (CRITICO, CRITICO_ICONO)
    ax.scatter([cols["Estado"] + 0.12], [y], s=260, color=color, edgecolor=icono, linewidth=0.8, zorder=3)
    ax.text(cols["Estado"] + 0.12, y, r"$\checkmark$" if ok else r"$\times$", color=icono, fontsize=10,
            ha="center", va="center", fontweight="bold", zorder=4)
    ax.text(cols["Estado"] + 0.38, y, "Cumple" if ok else "No cumple", color=TINTA,
            fontsize=12, va="center")
    ax.plot([0.1, 9.9], [i + 0.25, i + 0.25], color=REJILLA, linewidth=0.8)

estado = decision["decision"]["status"]
aprobadas = sum(decision["decision"]["checks"].values())
ax.text(0.2, len(filas) + 0.65,
        f"Decisión técnica: {estado} · {aprobadas} de {len(filas)} puertas aprobadas · "
        "requiere revisión y autorización humana",
        color=TINTA_2, fontsize=10, va="center")

fig.suptitle("Puertas técnicas del DSS", x=0.02, ha="left", fontsize=14,
             fontweight="bold", color=TINTA)
fig.tight_layout(rect=(0, 0, 1, 0.95))
salida = Path("reports/lab13/graficos")
salida.mkdir(parents=True, exist_ok=True)
fig.savefig(salida / "puertas_gobernanza.png", dpi=300, facecolor=FONDO)
plt.close(fig)
print("Gráfico generado:", salida / "puertas_gobernanza.png")
