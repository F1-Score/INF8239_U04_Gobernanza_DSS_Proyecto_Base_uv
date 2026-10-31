# Dataset Card — `territorial_risk_synthetic.csv`

**Proyecto:** INF-8239 · Unidad 04 · DSS territorial gobernado
**Última revisión:** 30/10/2026

## Resumen

| Atributo | Valor |
|---|---|
| Origen | Generado de forma sintética con semilla fija, para uso académico |
| Registros | 640 |
| Columnas | 9 |
| Variable objetivo | `target` (binaria): 55.2 % positivos, 44.8 % negativos |
| Grupos protegidos | G1: 396 registros · G2: 244 registros |
| Representa personas reales | **No.** No describe personas, territorios ni estadísticas oficiales de República Dominicana |

## Para qué existe

El archivo sirve para practicar, sobre datos sin riesgo, el ciclo completo de un sistema de apoyo a decisiones: validación del contrato de datos, entrenamiento de un clasificador, auditoría de equidad y controles de gobernanza.

## Columnas y uso en el proyecto

| Columna | Qué contiene | Uso |
|---|---|---|
| `case_id` | Identificador técnico del caso | Solo trazabilidad; no entra al modelo |
| `received_date` | Fecha de recepción | Define el corte temporal entrenamiento/prueba; no entra al modelo |
| `zone` | Zona territorial sintética | Variable predictora |
| `age_band` | Rango de edad | Variable predictora y eje del análisis interseccional |
| `previous_incidents` | Incidentes previos registrados | Variable predictora |
| `infrastructure_score` | Indicador sintético de infraestructura | Variable predictora |
| `exposure` | Indicador sintético de exposición | Variable predictora |
| `protected_group` | Grupo protegido (G1/G2) | **Solo auditoría**; nunca entra al modelo |
| `target` | Resultado a predecir | Etiqueta de entrenamiento y evaluación |

## Minimización y privacidad

- El modelo usa cinco variables; `case_id`, `received_date`, `protected_group` y `target` quedan fuera de las predictoras.
- `protected_group` se conserva únicamente para medir diferencias entre grupos, con acceso limitado a quienes realizan la auditoría.
- `configs/governance.yml` prohíbe identificadores directos (nombre, documento, correo, teléfono); `validate_schema` rechaza cualquier archivo que los incluya, y las pruebas `test_data.py` y `test_privacy.py` lo comprueban.
- Quitar el atributo protegido no elimina sesgos indirectos: otras variables pueden correlacionar con él.

## Conservación y acceso (propuesta)

1. Mantener el archivo solo mientras sea necesario para evaluar y reproducir el trabajo académico.
2. Limitar los permisos de modificación a los responsables del proyecto.
3. No añadir datos personales reales al repositorio.
4. Al cerrar el proyecto, revisar si sigue siendo necesario y aplicar las reglas institucionales.

Es una propuesta de gobernanza: no existen mecanismos automáticos de retención o borrado verificados.

## Usos prohibidos

Perfilar personas o territorios reales, decidir elegibilidad, intervenir automáticamente o declarar emergencias. Los resultados no permiten inferir nada sobre poblaciones reales.

**Evidencia:** `scripts/check_environment.py`, `scripts/describe_dataset.py`, `configs/governance.yml`, `tests/test_data.py`, `tests/test_privacy.py`.
