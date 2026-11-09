# Reversión de V6.1 — Restauración de links de descarga y párrafo final

**Commit revertido:** `8f57b38` — "fix: elimina links de descarga y parrafo final en fraud-detection (ES/EN/PT) - V6.1".
**Commit de reversión:** `4449ba3` — "revert: restaura links de descarga y parrafo final en fraud-detection (revierte 8f57b38)".

## Motivo

Tras revisar el contenido de los archivos en `assets/projects/fraud-detection/`,
el usuario decidió que los materiales deben seguir siendo accesibles desde el sitio.
Se revierte V6.1 en su totalidad.

## Qué se restaura

- Los 4 enlaces de descarga del sidebar del proyecto Prevención de Fraudes:
  01_desarrollo_ejecutado.ipynb, 02_evaluacion_final_ejecutada.ipynb,
  informe_tecnico_2026.md, README.md.
- El párrafo final "Notebooks e informe técnico de la revisión individual 2026
  disponibles para consulta. Los materiales originales del grupo no se
  redistribuyen aquí." (y sus equivalentes EN y PT).
- Las 4 claves JSON correspondientes en ES/EN/PT.
- Los tres HTML regenerados quedan idénticos a `b745176`.

## Archivos de assets

Los 13 archivos en `assets/projects/fraud-detection/` **no fueron modificados**
ni en V6.1 ni en su reversión. Permanecen íntegros y accesibles.

## Verificación

- `git diff b745176 HEAD -- . ':(exclude)CAMBIOS_*'` → sin salida.
  Los archivos fuente y HTML generados son byte a byte idénticos a V6.0.
- Validaciones post-reversión: pendientes de registrar.

## Estado

- [x] Modificación propuesta
- [x] Modificación realizada
- [x] Reversión ejecutada
- [ ] Validación aprobada
- [ ] Verificación visual
- [ ] Push de la reversión