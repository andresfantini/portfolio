# V6.1 — Eliminación de links de descarga y párrafo final en Prevención de Fraudes

**Base:** V6.0 en `main` (commit `b745176`).
**Pedido del usuario:** eliminar los 4 links de descarga de la barra lateral del proyecto
Prevención de Fraudes con Tarjeta de Crédito y el párrafo final bajo esos links,
en las tres versiones de idioma.

## Cambios aplicados

- `_source/templates/projects/fraud-detection.html`: se eliminaron 4 `<a href="...">`
  con `download` (01_desarrollo_ejecutado.ipynb, 02_evaluacion_final_ejecutada.ipynb,
  informe_tecnico_2026.md, README.md) y el `<p>` final que insertaba
  `the_original_team_notebooks_have_not_been`. Se conservó el enlace mailto de contacto.
- `content/es.json`, `content/en.json`, `content/pt.json`: se eliminaron 4 claves
  (`the_original_team_notebooks_have_not_been`, `download_notebooks_2026`,
  `download_report_2026`, `download_readme_2026`) y se ajustó la coma final de
  `data_analyst_business_insights_analyst_junior_data` en cada archivo.

## Archivos regenerados por `build.py`

- `projects/fraud-detection.html`
- `en/projects/fraud-detection.html`
- `pt/projects/fraud-detection.html`

## Alcance

- No se modificaron otros proyectos, HOME, CV, estilos ni scripts de `tools/`.
- Los 4 archivos en `assets/projects/fraud-detection/` dejan de estar enlazados
  desde el sitio, pero se conservan en disco (limpieza queda como tarea separada).

## Estado

- [x] Modificación propuesta
- [x] Modificación realizada
- [x] Generación ejecutada
- [x] Validación aprobada
- [x] Verificación visual
- [x] Commit realizado