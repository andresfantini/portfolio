# Prevención de Fraudes — proyecto académico (2022) y revisión técnica (2026)

Esta carpeta ofrece evidencia verificable de una revisión **personal realizada en 2026** a partir de un proyecto académico **grupal de 2022** (FaMAF / UNC). No debe interpretarse que el código revisado en 2026 fue la entrega presentada en 2022.

## Alcance y fuente de datos

- Dataset público **simulado**, `card_transdata.csv`: 1.000.000 registros, 8 columnas (7 predictores y `fraud`).
- Datos originales no incluidos en la publicación; pueden obtenerse de la fuente pública de Credit Card Fraud disponible en Kaggle. Verificar términos de licencia y procedencia en la fuente.
- SHA-256 del CSV usado: `7013c329bae9ef0ef32d65dbeb095694f0c7cd6c00ff74b2d0087fa1c67b8717`.
- **No es un sistema antifraude desplegado**. No hay validación con transacciones bancarias reales.

## Materiales

| Archivo | Descripción |
|---|---|
| `01_desarrollo_ejecutado.ipynb` | EDA, comparación de modelos, validación cruzada y ajuste del modelo (con salidas). |
| `02_evaluacion_final_ejecutada.ipynb` | Evaluación final con gráficos y métricas (con salidas). |
| `01_desarrollo_fuente.ipynb` | Versión editable, no ejecutada, para reproducción controlada. |
| `02_evaluacion_fuente.ipynb` | Versión editable de la evaluación final, con controles para evitar repetir el test. |
| `informe_tecnico_2026.md` | Protocolo, resultados y limitaciones. |
| `modelo_congelado_pretest.joblib` | Modelo congelado antes de evaluar el test. **Cargar solamente si se confía en su procedencia**. |
| `manifiesto_congelado_pretest.json` | Parámetros, umbral e integridad del modelo pretest. |
| `metricas_prueba_final.json` | Métricas finales conservadas. |

## Resultados del test reservado

200.000 registros simulados: 182.519 verdaderos negativos, 0 falsos positivos, 5 falsos negativos y 17.476 verdaderos positivos. Accuracy 99,9975 %, recall 99,9714 %, precision 100 %. **No extrapolar a transacciones reales.**

## Reproducibilidad

1. Crear un entorno virtual Python e instalar `requirements-fraudes.txt`.
2. Obtener el CSV de la fuente pública y colocarlo en `data/card_transdata.csv`, desde el directorio de trabajo, o definir `FRAUD_CSV_PATH`.
3. Ejecutar `01_desarrollo_fuente.ipynb` para reproducir el entrenamiento. La búsqueda puede requerir recursos significativos.
4. El test final fue ejecutado **una sola vez** en 2026 y sus salidas se conservan. No volver a utilizar ese test para decidir cambios posteriores. Si se desarrolla un modelo alternativo, reservar un nuevo conjunto de evaluación independiente.
5. El modelo congelado original se conserva como evidencia del experimento histórico de revisión; no se debe sustituir silenciosamente por un modelo reentrenado.

**Advertencia:** la deserialización de archivos `joblib` de origen no confiable puede ejecutar código arbitrario.

## Derechos y atribución

Esta publicación incluye solamente la revisión individual de 2026. Se excluyen del paquete público los notebooks históricos y el informe de autoría grupal mientras no se confirme la autorización para su redistribución. No se asigna licencia a material ajeno.
