# Declaración de uso de Inteligencia Artificial

**Asignatura:** INF-8239 · Ciencia de Datos II  
**Unidad:** 04 · Ética y roles en Ciencia de Datos  
**Actividades:** LAB11, LAB12 y LAB13  
**Fecha:** 30/10/2026

## 1. Herramienta utilizada

Se utilizó **Claude (Anthropic)** como asistente para ejecutar y verificar los laboratorios, comparar los resultados con los valores de referencia y redactar la documentación.

## 2. Material de partida

El trabajo se realizó sobre el proyecto base compartido para LAB11–13 (datos sintéticos, código, configuración y pruebas). Las entradas de `student_inputs/`, la Dataset Card, la Model Card y el Runbook se redactaron de nuevo con apoyo de la IA, conservando las puntuaciones de riesgo, los roles y las conclusiones; `lab11_impact.py` y `simulate_incident.py` se reescribieron con la misma salida y una protección para no sobrescribir documentos ya completados.

## 3. Actividades asistidas

1. **Ejecución:** instalación del entorno con `uv sync --frozen` y ejecución de `check_environment.py`, `describe_dataset.py`, `lab11_impact.py`, `lab12_audit.py` (logistic y tree), `validate_lab12_decision.py`, `lab13_governance.py` y `simulate_incident.py`.
2. **Verificación:** comparación de las métricas obtenidas con los valores de referencia de la guía de ejecución.
3. **Documentación:** redacción de `reports/lab11/DECISION_RECORD.md` y `reports/lab13/INCIDENT_POSTMORTEM.md`, y actualización de `docs/MODEL_CARD.md` con las mediciones propias.
4. **Gráficos:** elaboración de nuevos scripts de gráficos (`generate_lab12_charts.py` y `generate_lab13_chart.py`) con paleta validada para daltonismo, y generación de las figuras a partir de los resultados propios.
5. **Control de versiones:** preparación del historial Git propio del proyecto.

## 4. Verificaciones realizadas

| Comprobación | Resultado |
|---|---|
| Entorno y dataset | 640 registros, 9 columnas, `dataset_status: valid` |
| LAB11 | 8 riesgos; prioritarios R02 (9), R01 (8) y R07 (8); 3 pruebas aprobadas |
| LAB12 Logistic | Accuracy 71.88 %, recall 71.74 %, brecha de recall 13.76 pp, brecha de FPR 12.50 pp |
| LAB12 Tree | Accuracy 70.63 %, brecha de recall 18.13 pp, brecha de FPR 16.83 pp |
| Validación LAB12 | `decision_status: documented`; 2 pruebas aprobadas |
| LAB13 | `GO`, cinco puertas aprobadas; latencia 0.0265 ms |
| Simulacro | Ejecutado el 30/10/2026 y documentado como hipotético |
| Streamlit | Tablero verificado visualmente |
| Pruebas finales | 10 aprobadas |

## 5. Responsabilidad y limitaciones

- Las métricas provienen de los scripts del proyecto; la IA no las generó ni las modificó.
- Las puntuaciones de riesgo son valoraciones del ejercicio, no mediciones empíricas.
- El incidente fue simulado; no se realizaron comunicaciones, suspensiones ni rollbacks reales.
- La decisión técnica `GO` no constituye autorización institucional; la recomendación documentada es **REVIEW**.
- La revisión de los resultados, las interpretaciones y la responsabilidad académica corresponden a la estudiante.
