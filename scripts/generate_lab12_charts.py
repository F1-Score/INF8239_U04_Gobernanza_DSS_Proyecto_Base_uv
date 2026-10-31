"""Gráficos de LAB12: desempeño global y brechas de equidad entre G1 y G2.

Lee reports/lab12/<modelo>/global_metrics.json y escribe las figuras en
reports/lab12/graficos/. Ejecutar con:

    uv run python scripts/generate_lab12_charts.py
"""

import json
from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np

BASE = Path("reports/lab12")
OUT = BASE / "graficos"
OUT.mkdir(parents=True, exist_ok=True)

# Paleta validada (separación para daltonismo comprobada); texto en tinta neutra.
MODELOS = {"logistic": ("Logistic", "#A593D3"), "tree": ("Tree", "#A8D8C2")}
# Contorno en un tono más profundo del mismo color: mantiene el borde nítido sobre fondo blanco.
CONTORNO = {"logistic": "#6B58A6", "tree": "#4F9478"}
TINTA, TINTA_2, TENUE = "#0B0B0B", "#52514E", "#898781"
REJILLA, EJE, FONDO = "#E1E0D9", "#C3C2B7", "#FFFFFF"
LIMITE_PP = 16  # tolerancia de brecha configurada en configs/governance.yml

plt.rcParams.update({
    "font.family": "sans-serif",
    "font.sans-serif": ["Segoe UI", "DejaVu Sans", "Arial"],
    "font.size": 11,
    "axes.edgecolor": EJE,
    "axes.labelcolor": TINTA_2,
    "xtick.color": TENUE,
    "ytick.color": TINTA,
})


def cargar(modelo):
    with (BASE / modelo / "global_metrics.json").open(encoding="utf-8") as f:
        return json.load(f)


datos = {m: cargar(m) for m in MODELOS}


def barras_horizontales(ax, etiquetas, valores_por_modelo, xmax, fmt):
    """Barras agrupadas horizontales con etiqueta de valor al final de cada barra."""
    y = np.arange(len(etiquetas))
    alto = 0.34
    for i, (modelo, (nombre, color)) in enumerate(MODELOS.items()):
        pos = y - alto / 2 + i * alto
        valores = valores_por_modelo[modelo]
        ax.barh(pos, valores, height=alto - 0.04, color=color, edgecolor=CONTORNO[modelo],
                linewidth=1.0, label=nombre, zorder=3)
        for p, v in zip(pos, valores):
            ax.text(v + xmax * 0.01, p, fmt(v), va="center", ha="left", color=TINTA, fontsize=10,
                    zorder=5, bbox=dict(facecolor=FONDO, edgecolor="none", pad=1.5))
    ax.set_yticks(y, etiquetas)
    ax.invert_yaxis()
    ax.set_xlim(0, xmax)
    ax.grid(axis="x", color=REJILLA, linewidth=0.8, zorder=0)
    for lado in ("top", "right", "left"):
        ax.spines[lado].set_visible(False)
    ax.tick_params(axis="y", length=0)
    ax.legend(loc="lower right", frameon=False, ncols=2, bbox_to_anchor=(1, 1.0))


# --- Figura 1: desempeño global ---------------------------------------------
metricas = [("accuracy", "Accuracy"), ("recall", "Recall"), ("precision", "Precisión"),
            ("fpr", "FPR (menor es mejor)")]
fig, ax = plt.subplots(figsize=(10, 5.5), facecolor=FONDO)
barras_horizontales(
    ax,
    [e for _, e in metricas],
    {m: [datos[m]["metrics"][k] * 100 for k, _ in metricas] for m in MODELOS},
    xmax=100,
    fmt=lambda v: f"{v:.1f} %",
)
ax.set_xlabel("Porcentaje sobre los 160 casos de prueba")
fig.suptitle("Desempeño global por modelo", x=0.02, ha="left", fontsize=14,
             fontweight="bold", color=TINTA)
fig.text(0.02, 0.915, "Partición temporal · conjunto de prueba desde el 25/09/2026",
         ha="left", color=TINTA_2, fontsize=10)
fig.tight_layout(rect=(0, 0, 1, 0.92))
fig.savefig(OUT / "desempeno_global.png", dpi=300, facecolor=FONDO)
plt.close(fig)

# --- Figura 2: brechas de equidad G1 vs G2 -----------------------------------
brechas = [("recall", "Brecha de recall"), ("fpr", "Brecha de FPR"),
           ("selection_rate", "Brecha de tasa de selección")]
fig, ax = plt.subplots(figsize=(10, 5.5), facecolor=FONDO)
barras_horizontales(
    ax,
    [e for _, e in brechas],
    {m: [datos[m]["differences"][k] * 100 for k, _ in brechas] for m in MODELOS},
    xmax=32,
    fmt=lambda v: f"{v:.2f} pp",
)
# Límite de tolerancia: solo aplica a recall y FPR.
for fila in (0, 1):
    ax.plot([LIMITE_PP, LIMITE_PP], [fila - 0.45, fila + 0.45], color=TINTA,
            linestyle=(0, (4, 3)), linewidth=1.4, zorder=4)
ax.text(LIMITE_PP, -0.62, f"Límite {LIMITE_PP} pp", ha="center", va="bottom",
        color=TINTA, fontsize=9.5)
ax.set_xlabel("Diferencia absoluta entre G1 y G2 (puntos porcentuales)")
fig.suptitle("Brechas de equidad entre grupos", x=0.02, ha="left", fontsize=14,
             fontweight="bold", color=TINTA)
fig.text(0.02, 0.915, "La línea discontinua marca la tolerancia configurada para recall y FPR",
         ha="left", color=TINTA_2, fontsize=10)
fig.tight_layout(rect=(0, 0, 1, 0.92))
fig.savefig(OUT / "brechas_equidad.png", dpi=300, facecolor=FONDO)
plt.close(fig)

print("Gráficos generados:")
print(OUT / "desempeno_global.png")
print(OUT / "brechas_equidad.png")
