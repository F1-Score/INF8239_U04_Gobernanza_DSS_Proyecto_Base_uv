# Decision Record — LAB11

**Fecha de ejecución:** 30/10/2026  
**Decisión:** **REVIEW** — continuar la evaluación; no se autoriza el despliegue.

## 1. Evidencia

`scripts/lab11_impact.py` validó la evaluación de impacto, las partes interesadas y el registro de riesgos, y calculó la prioridad de cada riesgo (probabilidad × impacto, escala 1–4). Se documentaron ocho riesgos. Los tres prioritarios fueron:

| Riesgo | Probabilidad | Impacto | Prioridad | Control | Responsable |
|---|---:|---:|---:|---|---|
| R02 — Datos incompletos o erróneos producen prioridades equivocadas | 3 | 3 | 9 | Validar calidad e integridad antes de cada predicción | Equipo de datos |
| R01 — El modelo prioriza de forma desigual a los grupos | 2 | 4 | 8 | Auditar la equidad por grupo y exigir revisión humana | Equipo de datos |
| R07 — Se exponen atributos sensibles sin autorización | 2 | 4 | 8 | Restringir el acceso y mantener los atributos protegidos fuera del modelo | Responsable de privacidad |

Las pruebas `tests/test_impact.py` y `tests/test_privacy.py` finalizaron con **3 pruebas aprobadas**. El dataset se validó con 640 registros y 9 columnas (`dataset_status: valid`).

## 2. Interpretación

- **R02** obtiene la mayor puntuación porque es el riesgo con mayor probabilidad estimada: si los datos de entrada son incompletos, todas las prioridades posteriores se ven afectadas.
- **R01** y **R07** tienen menor probabilidad, pero el impacto máximo (4): un trato desigual entre grupos o la exposición de atributos sensibles afectaría directamente a las personas, aunque los datos sean sintéticos.
- El orden de prioridad orienta la atención, pero no sustituye el juicio profesional. R04 (recomendación aplicada como decisión automática) tiene puntuación 4, pero su impacto también es máximo y requiere control permanente.

## 3. Incertidumbre y limitaciones

- Los datos son sintéticos y no representan estadísticas reales de República Dominicana.
- Las puntuaciones son valoraciones del ejercicio, no mediciones empíricas.
- Aún no se dispone de la auditoría de equidad (LAB12) ni de las puertas de gobernanza (LAB13).
- La existencia de un control documentado no demuestra que sea eficaz.

## 4. Responsable

El **responsable institucional del DSS** revisa la evidencia, autoriza cualquier cambio de estado y documenta la decisión. El equipo de datos y el responsable de privacidad ejecutan los controles de R02, R01 y R07.

## 5. Condición de retiro

Suspender el uso del DSS cuando se incumplan los límites aprobados de desempeño, equidad o privacidad, o cuando no exista supervisión humana efectiva. Mientras tanto, se aplica la alternativa no predictiva: priorización manual con criterios documentados y la posibilidad de apelar ante una persona autorizada.
