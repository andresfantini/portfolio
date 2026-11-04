# Prevención de Fraudes — Informe de cierre técnico de la revisión 2026

## Alcance y procedencia

Esta versión constituye una **revisión metodológica de 2026** del proyecto académico grupal de Prevención de Fraudes. Los documentos de 2022 (`Informe - Grupo 3.pdf` y notebooks históricos) permanecen sin modificar. **No representa retrospectivamente la implementación entregada en 2022.**

El archivo `card_transdata.csv` tiene un millón de registros y corresponde a un **dataset público simulado**, no a transacciones bancarias observadas en producción. El CSV aportado por el usuario se utilizó íntegramente como fuente, sin reescritura.

- SHA256 CSV: `7013c329bae9ef0ef32d65dbeb095694f0c7cd6c00ff74b2d0087fa1c67b8717`.
- Registros totales: **1.000.000**. Legítimas: **912.597**. Fraudes: **87.403** (8,7403 %).
- 8 columnas (7 predictores + `fraud`); tres variables continuas y cuatro binarias, incluida `repeat_retailer`.
- Faltantes: 0; duplicados exactos: 0. No se detectaron valores binarios fuera de {0,1}.
- La procedencia simulada fue contrastada con referencias públicas en la revisión anterior; la mera coincidencia de archivo no prueba aplicabilidad financiera.

## Protocolo fijado antes del test

1. `train_test_split` estratificado con semilla 42 reservó **200.000** observaciones exclusivamente para test (20 %).
2. De las 800.000 restantes se reservaron **160.000** (16 % total) para selección del umbral; **640.000** (64 %) quedaron para desarrollo/entrenamiento.
3. Los preprocesamientos (imputación, escala para Regresión Logística) quedaron dentro de pipelines. La variable objetivo `fraud` nunca es predictor. **No se aplicó SMOTE al conjunto completo ni al test**.
4. Se compararon **seis modelos** sobre los mismos **3 folds estratificados**, usando Average Precision como criterio principal. `Random Forest + submuestreo` aplica el muestreo exclusivamente dentro de cada entrenamiento de fold.
5. Se exploraron **6 configuraciones de Random Forest** con Randomized Search y CV estratificada. Esta búsqueda es **limitada**, no exhaustiva. La reducción respecto del plan inicial de cinco folds/doce iteraciones se realizó antes del test por el límite de memoria del entorno.
6. Se seleccionó el modelo utilizando únicamente resultados de desarrollo. Se entrenó con los 640.000 registros, y el umbral se fijó maximizando F2 en los 160.000 de calibración.
7. Se congeló el modelo y su umbral en archivos con huellas SHA256; el hash de los índices de test también quedó fijado. **Solo después** se ejecutó una evaluación de test.

## Validación cruzada de desarrollo (640.000 registros)

| Modelo | AP media | ROC-AUC media | F2 a umbral 0,5 |
|---|---:|---:|---:|
| Random Forest ponderado | 0.999999973 | 0.999999997 | 0.999843 |
| Random Forest original | 0.999999966 | 0.999999997 | 0.999843 |
| Random Forest + submuestreo | 0.999995142 | 0.999999551 | 0.999600 |
| Árbol de decisión | 0.999745429 | 0.999914379 | 0.999682 |
| Regresión Logística ponderada | 0.754466618 | 0.979267650 | 0.838704 |
| Baseline (prior) | 0.087403125 | 0.500000000 | 0.000000 |

La búsqueda encontró **Random Forest optimizado**: `n_estimators=100`, `max_depth=16`, `min_samples_leaf=1`, `max_features='sqrt'`, `class_weight=None`. Mejor Average Precision de la búsqueda: **0.999999986579**.

El **umbral comprometido** fue **0.62**, determinado exclusivamente con el conjunto de calibración. En esa partición, F2 = **1.00000000** y Average Precision = **1.0000000000**. Son resultados de calibración, **no** del test.

- SHA256 del modelo congelado: `830a35e40efcc642ba8a518a636f2c074b42e8a479ea14e45c879e3850b58214`.
- SHA256 de índices de test precomprometidos: `67133c73a19f1ce5312d53f9f844b3be65999fd1066d2c46cd203848b933c2e2`.
- Versiones de software: numpy=2.3.5, pandas=2.2.3, scikit-learn=1.8.0, imbalanced-learn=0.14.1, matplotlib=3.10.8.

## Evaluación independiente única (200.000 registros)

| Métrica | Resultado |
|---|---:|
| Accuracy | **99.9975 %** |
| Precision | **100.0000 %** |
| Recall | **99.9714 %** |
| F1 | **99.9857 %** |
| F2 | **99.9771 %** |
| Average Precision | **0.9999999935** |
| ROC-AUC | **0.9999999994** |

**Matriz de confusión** (clase positiva = fraude):

| | Predicción legítima | Predicción fraude |
|---|---:|---:|
| **Real legítima** | TN = 182,519 | FP = 0 |
| **Real fraude** | FN = 5 | TP = 17,476 |

Se detectaron **17,476 de 17,481 fraudes** del conjunto de prueba; se produjeron **5 omisiones** y **0 falsas alertas**.

## Diagnóstico metodológico

**Fortalezas verificadas:**

- Separación estratificada anterior a transformaciones supervisadas; test no utilizado para desarrollo.
- Selección de predictores excluyendo explícitamente `fraud`.
- Pipelines para aprendizaje de transformaciones dentro de folds; remuestreo solo de entrenamiento para la variante con submuestreo.
- Comparación homogénea de los mismos folds y criterio explícito de AP.
- Optimización delimitada, selección de umbral separada y congelación criptográfica de modelo, umbral e índices antes del test.
- La prueba final se realizó mediante un notebook separado que recarga el **mismo modelo previamente congelado**, en vez de reentrenarlo o reoptimizar después de consultar test.
- Se conservan gráficas de matriz de confusión, curva precision-recall y ROC.

**Limitaciones de la evidencia:**

1. **Datos simulados**: el rendimiento extraordinariamente alto es compatible con reglas de generación artificiales muy discriminantes. No constituye prueba de utilidad en una entidad financiera real.
2. **Sin validación externa, temporal o por cliente**: el CSV carece de identificadores y marcas temporales para distinguir registros dependientes del mismo cliente o períodos futuros. El test es un *holdout aleatorio del mismo dataset*.
3. **Posible familiaridad histórica**: el conjunto fue explorado durante el proyecto de 2022. Esta revisión reserva una partición independiente *dentro del nuevo entrenamiento*, pero no es un dataset externo completamente desconocido.
4. **Sin análisis económico de errores**: F2 es una elección metodológica, no una función de costos bancaria validada.
5. **Sin estudio de calibración ni deriva**: el puntaje `predict_proba` no queda automáticamente validado como probabilidad de fraude para producción.
6. **Búsqueda acotada**: 3 folds y 6 configuraciones; no se probó exhaustivamente el espacio de hiperparámetros ni todos los métodos de balanceo (SMOTENC no se ejecutó con los datos originales en la corrida completa).
7. **Sin certeza de ausencia total de fugas**: corregimos las fugas identificadas en los notebooks históricos, pero no es posible excluir cualquier correlación inducida por la generación o dependencia oculta del dataset.

## Conclusión profesional

**El procedimiento de clasificación se reconstruyó con una metodología adecuada para un benchmark académico simulado y se ejecutó de principio a fin.** Random Forest fue seleccionado mediante validación cruzada y alcanzó resultados muy altos en un test reservado, con cinco falsos negativos y ningún falso positivo. No corresponde traducir estos resultados en una promesa de precisión sobre transacciones bancarias reales.

Esta revisión aporta evidencia técnica de 2026 para el **Portfolio V5**; debe identificarse por separado del proyecto histórico de 2022 y su evaluación académica. No publicar métricas históricas basadas en SMOTE previo al split como evaluación independiente.

## Archivos y reproducción

- `Prevencion_Fraudes_v3_COMPLETA_DESARROLLO_TEST_CERRADO.ipynb`: notebook de desarrollo completo ejecutado, test cerrado.
- `Prevencion_Fraudes_v3_EVALUACION_TEST_FINAL_EJECUTADO.ipynb`: evaluación final ejecutada **una sola vez**, con salidas y gráficos conservados.
- `Prevencion_Fraudes_metodologia_correcta_2026_v3.ipynb`: fuente editable del desarrollo, con guardia para no sobrescribir la congelación.
- `Prevencion_Fraudes_v3_EVALUACION_TEST_FINAL.ipynb`: fuente de la evaluación, con guardia para no repetir el test si ya hay resultados.
- `outputs/prevencion_fraudes_revision_2026/modelo_congelado_pretest.joblib`: modelo entrenado; `joblib` solo debe cargarse de fuente confiable.
- `outputs/prevencion_fraudes_revision_2026/manifiesto_congelado_pretest.json`: decisiones antes del test.
- `outputs/prevencion_fraudes_revision_2026/metricas_prueba_final.json`: resultados finales.
- `outputs/prevencion_fraudes_revision_2026/*.png`: tres visualizaciones extraídas de las salidas ejecutadas sin reevaluar el test.

Los `.ipynb` ejecutados tienen sus resultados **ya integrados** y pueden revisarse sin volver a entrenar. Para reconstruir de cero usar el CSV original en `data/card_transdata.csv` y un directorio de salidas nuevo, con variables `FRAUD_MODE=completo`, `FRAUD_FOLDS=3`, `FRAUD_SEARCH_ITER=6`, `FRAUD_FINAL=0`. El script de congelación se niega a sobrescribir un manifiesto ya existente. El notebook final se niega a ejecutar un test adicional si `metricas_prueba_final.json` ya existe. Estas protecciones están puestas deliberadamente.
