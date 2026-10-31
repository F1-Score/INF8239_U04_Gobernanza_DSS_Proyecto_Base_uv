# Incident Postmortem — LAB13 (simulacro)

> **Simulacro.** El escenario fue generado por `scripts/simulate_incident.py`. No representa una falla real del modelo: la ejecución real de LAB13 obtuvo **GO** (brecha de recall 13.76 pp ≤ 16 pp). No se realizaron comunicaciones, suspensiones ni rollbacks reales.

## 1. Detección

- **detected_at (UTC):** 2026-10-31T00:19:42.114857+00:00 (30/10/2026, 20:19 hora local).
- **Señal simulada:** la brecha de recall entre G1 y G2 supera el límite de 0.16 configurado en `configs/governance.yml`.
- **Severidad propuesta:** media; incumplimiento de equidad sin exposición de datos.
- **Valor real de referencia:** 0.1376 (cumple).

## 2. Contención (prevista)

- Cambiar el estado de la recomendación a **REVIEW** y suspender el uso operativo del DSS.
- Mantener la priorización manual con criterios documentados como alternativa segura.
- **Ejecuta:** ML Engineer. **Autoriza:** Institutional Owner.

## 3. Preservación de evidencia

Se conservaron como evidencia del simulacro:

- `configs/governance.yml` (política y umbrales).
- `reports/lab13/deployment_decision.json` y `reports/lab13/fairness_by_group.csv`.
- `reports/lab12/logistic/global_metrics.json` y `fairness_intersectional.csv`.
- `models/model.joblib` y la versión registrada en Git.

## 4. Comunicación (prevista; no ejecutada)

| Destinatario | Responsable | Momento previsto |
|---|---|---|
| Institutional Owner | ML Engineer | Mismo día de la detección |
| Data Scientist y Data Engineer (consultados) | ML Engineer | Mismo día |
| Área legal (consultada) | Institutional Owner | Según la gravedad |
| Operadores y representantes de afectados (informados) | Institutional Owner | Antes de reanudar o si cambian decisiones previas |

## 5. Rollback (previsto; no ejecutado)

Retornar a la última versión validada del modelo (Logistic con 5/5 puertas aprobadas) o, si no existe, mantener la revisión manual. La reanudación requiere repetir la auditoría y obtener la aprobación del Institutional Owner.

## 6. Acciones correctivas, responsables y plazos simulados

| Acción | Responsable | Plazo simulado | Evidencia de cierre |
|---|---|---|---|
| Confirmar la señal y recalcular métricas por grupo | Data Scientist | 2 días | `fairness_by_group.csv` actualizado |
| Revisar la calidad y la distribución de los datos por grupo | Data Engineer | 3 días | Reporte de validación de datos |
| Evaluar el ajuste del umbral o del modelo y repetir la auditoría | Data Scientist | 5 días | Nuevo `global_metrics.json` |
| Verificar las cinco puertas antes de reanudar | ML Engineer | 6 días | `deployment_decision.json` con GO |
| Revisar la evidencia y autorizar el cierre | Institutional Owner | 7 días | Registro de decisión firmado |

Los plazos son objetivos del ejercicio, no fechas comprometidas.

## 7. Lecciones

- El runbook permite asignar cada fase a un rol definido en `student_inputs/raci.csv`.
- Falta un mecanismo automático que cambie el estado a REVIEW sin intervención manual; queda como mejora pendiente.
- Un GO técnico no sustituye la autorización institucional.
