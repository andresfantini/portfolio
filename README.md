# Portfolio profesional — Esteban Andrés Fantini

**V6 — Recuperación de modificaciones editoriales conocidas (versión de revisión).** Sitio estático trilingüe: español (inicio), inglés y portugués brasileño. Se conserva el diseño azul petróleo aprobado en V4.

## Edición rápida del contenido

| Idioma | Archivo único de textos |
|---|---|
| Español (idioma inicial) | `content/es.json` |
| Inglés | `content/en.json` |
| Portugués de Brasil | `content/pt.json` |

**Los HTML son archivos generados.** Modificá los valores en los JSON y luego regenerá todas las páginas. Los textos *no* se traducen automáticamente entre idiomas.

Véase **`EDITAR_CONTENIDOS_ES.md`** para el procedimiento detallado y ejemplos.

## Estructura

```text
portfolio-andres-multilingue-v6/
├── content/
│   ├── es.json                     ← textos en español
│   ├── en.json                     ← textos en inglés
│   └── pt.json                     ← textos en portugués brasileño
├── _source/templates/              ← 5 plantillas HTML de diseño, no editar textos aquí
│   ├── index.html
│   └── projects/*.html
├── tools/
│   ├── build.py                    ← genera las 15 páginas
│   ├── check_content.py            ← valida estructura de los JSON
│   └── check_multilingual.py       ← comprueba enlaces y páginas
├── index.html                      ← inicio en español, GENERADO
├── projects/*.html                 ← 4 proyectos español, GENERADOS
├── en/                             ← 5 páginas inglés, GENERADAS
├── pt/                             ← 5 páginas portugués, GENERADAS
├── assets/css/styles.css           ← apariencia
├── assets/js/main.js               ← menú móvil
├── assets/cv/                      ← CV español e inglés
├── requirements.txt                ← dependencias del generador
└── GUIA_PUBLICACION_ES.md
```

## Regenerar páginas tras editar un JSON

Desde la carpeta raíz del proyecto, con Python y Beautiful Soup instalados:

```bash
python3 tools/check_content.py
python3 tools/build.py
python3 tools/check_multilingual.py
```

Para preparar un entorno aislado por única vez:

```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements.txt
```

El generador escribe los HTML de los tres idiomas y **no modifica los JSON**. Si detecta un JSON inválido o una clave faltante, falla antes de escribir archivos.

Para ver el sitio localmente:

```bash
python3 -m http.server 8000
```

Abrir `http://localhost:8000/` y detener con `Ctrl+C`.

## Contenido y alcance

1. E-60 — Sistemas de costeo industrial y software de gestión.
2. TelemetriaGreenhouse — IoT, telemetría y procesamiento Python/PySpark.
3. OLIST — Análisis de e-commerce y colaboración en Data Science.
4. Prevención de Fraudes — Clasificación y análisis de riesgos.
5. Vehicle Market Scraper — Extracción de datos del mercado automotor y arquitectura modular (confidencial).
6. Inventario de Archivos — Automatización de sistemas y scripting con Bash y Python.

Los estudios de caso respetan su carácter académico o profesional y no presentan como comprobados rendimientos predictivos sin revisión independiente ni despliegues no confirmados. Se incorporan notebooks y resultados de la revisión individual de Fraudes 2026. No se incluye `card_transdata.csv` ni código privado del cliente E-60.

Los CV en español, inglés y portugués brasileño están incorporados. El CV PT-BR fue aprobado y después recibió dos cambios puntuales solicitados: subtítulo y tamaño de enlaces. Se mantiene el contenido profesional aprobado.

**Publicación:** activa en GitHub Pages en `https://andresfantini.github.io/portfolio/` (rama `main`, directorio raíz, deploy automático).

## Nota sobre la reversión de V6.1 (Prevención de Fraudes)

En noviembre de 2026 se intentó retirar los cuatro enlaces de descarga y el párrafo final del proyecto de Prevención de Fraudes (commit `8f57b38`). Tras revisar los materiales, se decidió que los archivos (notebooks, informe técnico, modelo y gráficos) debían permanecer accesibles desde la barra lateral del sitio. El cambio se revirtió (commit `4449ba3`) para restaurar los enlaces.

Los archivos en `assets/projects/fraud-detection/` nunca fueron eliminados y continúan disponibles tanto en el repositorio como en el sitio publicado. La justificación editorial completa de esta decisión está documentada en `CAMBIOS_REVERSION_V6_1_2026-11-09.md`.