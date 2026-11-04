# Corrección de textos HOME ES y EN — 2026-11-01

**Estado:** implementado según instrucción literal del usuario. Continúa siendo una versión local, no publicada.

## Español — aprobado para integrar

- Etiqueta de presentación: `Datos & BI | Costos | Pipelines | IoT`
- Párrafo del hero: `Conecto procesos, necesidades del negocio y tecnologías TI para desarrollar flujos de datos confiables y herramientas para mejorar la toma de decisiones.`

## Inglés — aprobado para integrar

- Etiqueta de presentación: `Information technologies | Cost Management  | Business Analytics`
- Párrafo del hero: `I connect processes, business needs, and technology to build dependable data flows and practical tools for take better decisions.`

## Cambios de implementación

1. `content/es.json`: dos valores actualizados en `pages.index.hero`.
2. `content/en.json`: dos valores actualizados en `pages.index.hero`.
3. `index.html` y `en/index.html`: regenerados mediante `python tools/build.py`.
4. `content/pt.json`, `pt/index.html`, los 12 HTML de proyectos, plantillas, estilos y los tres PDF de CV **sin cambios**.

## Controles

- Validación del generador: 15 HTML generados.
- `tools/check_content.py`: OK.
- `tools/check_multilingual.py`: OK (439 referencias internas, 15 páginas).
- `tools/check_site.py`: OK.
- Se contrastaron los archivos anteriores con los nuevos: solo cuatro archivos preexistentes modificados.
- No hay cambios en el contenido de E-60, TelemetriaGreenhouse, Prevención de Fraudes ni OLIST.

**Nota:** en el texto en inglés se respetó literalmente la frase proporcionada, sin corrección gramatical automática.

## Corrección posterior (HOME ES)

Se corrigió únicamente `Custos` → `Costos` en la etiqueta de inicio española. La etiqueta definitiva queda: `Datos & BI | Costos | Pipelines | IoT`. La versión PT, la versión EN y el resto de los contenidos no se modificaron.
