# Model Card — Regresión logística del DSS territorial

**Versión:** `models/model.joblib` (pipeline de scikit-learn)
**Fecha:** 30/10/2026 · **Próxima revisión:** antes de cualquier despliegue o ante cambios en datos, modelo o política

## 1. Uso previsto

Ordenar casos territoriales **sintéticos** según su prioridad para que una persona autorizada decida cuáles revisar primero. El modelo recomienda; no decide.

## 2. Usos fuera de alcance

Intervención automática, decisiones de elegibilidad, declaración de emergencias o cualquier decisión definitiva sobre personas o comunidades.

## 3. Modelo y datos

- **Algoritmo:** regresión logística con `class_weight="balanced"`, `max_iter=1200`, `random_state=42`.
- **Preprocesamiento:** one-hot para `zone` y `age_band`; estandarización para `previous_incidents`, `infrastructure_score` y `exposure`.
- **Datos:** 640 registros sintéticos (ver `docs/DATASET_CARD.md`).
- **Partición temporal:** entrenamiento hasta el 24/09/2026; prueba desde el 25/09/2026 (160 casos). Se evalúa sobre datos posteriores para no usar el futuro.
- **Atributo protegido:** excluido de las predictoras; se usa solo para la auditoría.

## 4. Evaluación

**Global (160 casos de prueba)**

| Métrica | Logistic | Tree (alternativa) |
|---|---:|---:|
| Accuracy | 71.88 % | 70.63 % |
| Recall | 71.74 % | 71.74 % |
| Precisión | 77.65 % | 75.86 % |
| FPR | 27.94 % | 30.88 % |

**Por grupo (Logistic)**

| Grupo | n | Recall | FPR | Selección |
|---|---:|---:|---:|---:|
| G1 | 101 | 65.3 % | 25.0 % | 44.6 % |
| G2 | 59 | 79.1 % | 37.5 % | 67.8 % |

Brechas G1–G2: **13.76 pp** en recall y **12.50 pp** en FPR, ambas dentro del límite de 16 pp. El árbol supera ese límite (18.13 pp y 16.83 pp), por eso se eligió Logistic.

En LAB13 las cinco puertas técnicas se cumplieron y el pipeline devolvió `GO`. Ese resultado es técnico: no sustituye la aprobación humana.

## 5. Costo computacional (Green AI)

| Indicador | Logistic | Tree |
|---|---:|---:|
| Entrenamiento (LAB12) | 0.0429 s | 0.0414 s |
| Tamaño serializado | 3.56 KB | 7.87 KB |
| Entrenamiento (LAB13) | 0.0480 s | — |
| Latencia por caso (LAB13) | 0.0265 ms | — |

Logistic ocupa menos de la mitad que el árbol con tiempos prácticamente iguales. Son mediciones de una sola ejecución en un equipo personal; no demuestran ahorro energético.

## 6. Limitaciones y supervisión humana

- Los datos son sintéticos y no representan poblaciones reales.
- Una brecha entre grupos requiere investigación; por sí sola no prueba discriminación causal.
- Hay subgrupos interseccionales pequeños (p. ej., G2 de 45–59 años, n = 8) cuyos resultados son inestables.
- Excluir el atributo protegido no elimina sesgos indirectos.
- Toda recomendación pasa por revisión humana y queda registrada; existe una vía de apelación.
- El sistema se suspende si incumple los umbrales de desempeño, equidad o privacidad, o si no hay supervisión efectiva.

## 7. Responsables

- **Product Owner:** responde por el modelo y su despliegue.
- **Institutional Owner:** autoridad final ante incidentes y para reanudar el sistema.

**Evidencia:** `reports/lab12/`, `reports/lab13/deployment_decision.json`, `configs/governance.yml`.
