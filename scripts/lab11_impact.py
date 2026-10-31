"""LAB11 · Evaluación de impacto ético.

Valida las entradas de student_inputs/, calcula la prioridad de cada riesgo
(probabilidad × impacto) y escribe la evidencia en reports/lab11/.

    uv run python scripts/lab11_impact.py
"""

import json
from pathlib import Path

import pandas as pd
import yaml

from inf8239_u04.impact import score_risks, validate_impact

ENTRADAS = Path("student_inputs")
SALIDA = Path("reports/lab11")
PLANTILLA_DECISION = (
    "# Decision record\n\n"
    "REPLACE with evidence, uncertainty, owner and GO/REVIEW/STOP.\n"
)


def main():
    SALIDA.mkdir(parents=True, exist_ok=True)

    impacto = yaml.safe_load((ENTRADAS / "lab11_impact.yml").read_text(encoding="utf-8"))
    validate_impact(impacto)

    interesados = pd.read_csv(ENTRADAS / "stakeholders.csv")
    if interesados.astype(str).apply(lambda col: col.str.contains("REPLACE")).any().any():
        raise ValueError("Complete stakeholders.csv")

    riesgos = score_risks(pd.read_csv(ENTRADAS / "risk_register.csv"))
    riesgos.to_csv(SALIDA / "risk_register_scored.csv", index=False)
    interesados.to_csv(SALIDA / "stakeholders.csv", index=False)

    resumen = {
        "GOVERN": "owner and policy",
        "MAP": f"{len(riesgos)} documented risks",
        "MEASURE": "LAB12 pending",
        "MANAGE": "withdrawal and appeal documented",
    }
    (SALIDA / "rmf_summary.json").write_text(json.dumps(resumen, indent=2), encoding="utf-8")

    # Crear la plantilla solo si el registro de decisión aún no se ha completado.
    registro = SALIDA / "DECISION_RECORD.md"
    if not registro.exists() or "REPLACE" in registro.read_text(encoding="utf-8"):
        registro.write_text(PLANTILLA_DECISION, encoding="utf-8")
    else:
        print(f"{registro} ya está completo; no se sobrescribe.")

    print(riesgos[["id", "priority", "owner"]].head(3).to_string(index=False))


if __name__ == "__main__":
    main()
