# Runbook de incidentes — DSS territorial

Procedimiento propuesto para responder a fallas del DSS sintético. Se probó mediante el simulacro de LAB13 (`reports/lab13/INCIDENT_POSTMORTEM.md`); no se ha ejecutado en un entorno real.

## Roles

| Rol | Responsabilidad |
|---|---|
| ML Engineer | Ejecuta la contención técnica y coordina las acciones |
| Institutional Owner | Responsable final: autoriza suspender, reanudar y cerrar |
| Data Scientist / Data Engineer | Investigan la causa en el modelo y en los datos |
| Legal | Se consulta cuando hay obligaciones de notificación |

## 1. Detectar y clasificar

Se abre un incidente cuando ocurre cualquiera de estas señales:

| Señal | Umbral |
|---|---|
| Recall global | < 0.68 |
| Brecha de recall entre grupos | > 0.16 |
| Brecha de FPR entre grupos | > 0.16 |
| Latencia por caso | > 500 ms |
| Tamaño del modelo | > 1024 KB |
| Datos prohibidos o uso no autorizado | Cualquier ocurrencia |

**Severidad**
- **Alta:** exposición de datos o uso del DSS como decisión automática.
- **Media:** incumplimiento de una métrica o cambio relevante en los datos.
- **Baja:** anomalía sin impacto confirmado.

## 2. Contener

1. El ML Engineer cambia el estado a `REVIEW` y detiene el uso operativo.
2. Mientras dure el incidente, los casos se priorizan manualmente con criterios documentados.
3. El Institutional Owner confirma la suspensión.

## 3. Preservar la evidencia

Guardar antes de cualquier cambio: fecha y descripción, métricas y alertas, versión del modelo, configuración aplicada y acciones tomadas. No incluir datos personales ni credenciales.

## 4. Comunicar

- El ML Engineer avisa al Institutional Owner el mismo día y consulta al equipo de datos.
- El Institutional Owner decide si se informa a operadores o personas afectadas y consulta a Legal cuando corresponde.
- Cada comunicación queda registrada.

## 5. Revertir

Volver a la última versión validada del modelo. Si no existe una versión segura, mantener la priorización manual. Reanudar exige repetir las pruebas y obtener la autorización del Institutional Owner.

## 6. Cerrar con postmortem

Documentar causa (o hipótesis pendiente), alcance, acciones correctivas, responsable de cada acción, fecha límite y evidencia de verificación. El ML Engineer coordina las acciones; el Institutional Owner aprueba el cierre. Los plazos dependen de la severidad y se registran por escrito.
