"""LAB13 · Simulacro de incidente de equidad.

Genera el borrador de reports/lab13/INCIDENT_POSTMORTEM.md para un escenario
hipotético (brecha de recall fuera de tolerancia). Si el postmortem ya fue
completado, no lo sobrescribe salvo que se use --force.

    uv run python scripts/simulate_incident.py [--force]
"""

import argparse
from datetime import datetime, timezone
from pathlib import Path

POSTMORTEM = Path("reports/lab13/INCIDENT_POSTMORTEM.md")


def borrador():
    return (
        "# Incident simulation\n\n"
        f"- detected_at: {datetime.now(timezone.utc).isoformat()}\n"
        "- signal: recall gap exceeded\n"
        "- containment: REVIEW and safe baseline\n"
        "- evidence: preserved report and model version\n"
        "- communication: REPLACE\n"
        "- corrective actions, owners and dates: REPLACE\n"
    )


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--force", action="store_true", help="sobrescribir un postmortem ya completado")
    args = parser.parse_args()

    POSTMORTEM.parent.mkdir(parents=True, exist_ok=True)
    completo = POSTMORTEM.exists() and "REPLACE" not in POSTMORTEM.read_text(encoding="utf-8")
    if completo and not args.force:
        print(f"{POSTMORTEM} ya está completo; use --force para generar un nuevo borrador.")
        return

    POSTMORTEM.write_text(borrador(), encoding="utf-8")
    print(POSTMORTEM)


if __name__ == "__main__":
    main()
