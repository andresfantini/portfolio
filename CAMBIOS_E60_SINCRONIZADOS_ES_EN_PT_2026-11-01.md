# Portfolio V6 — E-60: sincronización de los dos últimos pedidos (ES / EN / PT)

**Base canónica de esta edición:** `portfolio-andres-multilingue-v6-E60-estado-y-categorias-corregidos.zip`.

## Decisiones aprobadas previamente en español y trasladadas a inglés y portugués

1. **Áreas profesionales relacionadas:** tres áreas (Gestión de Costos / Ingeniería de Datos / Desarrollo de Software), sin enumerar cargos adicionales.
2. **El desafío:** calcular costos de producción, precios de venta, márgenes de rentabilidad, puntos de equilibrio y evaluar escenarios de planificación.
3. **Modelado económico:** integrar presupuestos, determinar costos unitarios, fijos y variables, margen de contribución y puntos de equilibrio; información para recursos, precios y rentabilidad. Mantener la etiqueta del punto.
4. **Categoría superior:** Sistemas de Gestión / Ingeniería de Costos / Desarrollo de Software, traducida por idioma y sin la frase de estado.
5. **Ruta de navegación:** únicamente el vínculo de regreso a los proyectos.
6. **Tarjeta visual:** eliminar el estado de desarrollo.

## Alcance técnico

- `content/en.json` y `content/pt.json`: cuatro campos de E-60 actualizados en cada idioma.
- `tools/build.py`: regla existente de eliminación de ruta y estado extendida a E-60 en los tres idiomas.
- `en/projects/e60-costing.html` y `pt/projects/e60-costing.html`: regeneradas automáticamente. La página E-60 española no cambió.
- Los CV y todas las otras secciones/proyectos siguen sin alteraciones.

**Estado:** integrado localmente; publicación en Internet pendiente. **Próxima actividad acordada:** revisión de los CV de los tres idiomas. No modificar ni simplificar los CV antes de esa revisión.
