# Portfolio profesional V6 — Guía de edición sincronizada (ES / EN / PT)

**Proyecto:** Portfolio profesional de Esteban Andrés Fantini  
**Versión de referencia:** V6, contenido editable en JSON  
**Entorno previsto:** Ubuntu + VS Code + Python 3  
**Alcance de esta guía:** editar textos en los tres idiomas, regenerar el sitio y verificar los resultados **sin publicar ni alterar la arquitectura del repositorio**.

> **Distinción fundamental:** la V6 **NO traduce automáticamente**. Se editan los valores correspondientes en `es.json`, `en.json` y `pt.json` (con traducciones revisadas); después, **una sola ejecución** de `tools/build.py` actualiza las **15 páginas HTML**. «Actualizar simultáneamente» significa regenerar los tres idiomas en la misma operación, **no** escribir una frase en español y obtener traducciones automáticas.

---

## 1. Qué archivos son fuente y cuáles son resultado

```text
portfolio-andres-multilingue-v6/
├── content/
│   ├── es.json                        ← TEXTO FUENTE: español, idioma inicial
│   ├── en.json                        ← TEXTO FUENTE: inglés
│   └── pt.json                        ← TEXTO FUENTE: portugués de Brasil
├── _source/templates/                 ← plantillas HTML (no tocar para editar textos)
├── tools/
│   ├── check_content.py              ← valida JSON y claves usadas
│   ├── build.py                      ← genera los 15 HTML en una operación
│   ├── check_multilingual.py          ← valida navegación, enlaces y estructura
│   └── check_site.py                 ← valida estructura local de páginas ES
├── index.html                         ← HTML GENERADO: portada ES
├── projects/                          ← HTML GENERADO: 4 casos ES
├── en/                                ← HTML GENERADO: portada + 4 casos EN
├── pt/                                ← HTML GENERADO: portada + 4 casos PT
└── assets/                            ← CSS, JavaScript, imágenes y CV
```

**Reglas de trabajo:**

1. Para cambiar títulos, párrafos o etiquetas visibles, editá **solo los valores JSON** de `content/`.
2. No edites los HTML generados: `build.py` los sobrescribe en la siguiente generación.
3. No traduzcas los nombres de las **claves** JSON ni las rutas: deben ser idénticas en los tres archivos.
4. No modifiques `"language": "es"`, `"language": "en"` ni `"language": "pt"`.
5. Cada cambio de contenido debe tener una versión equivalente, revisada semánticamente, en los tres idiomas.

---

## 2. Preparación inicial (una sola vez)

### Paso 2.1 — Localizar y abrir la carpeta correcta

Descomprimí el ZIP original de V6, si todavía no lo hiciste. Abrí en VS Code **la carpeta raíz** `portfolio-andres-multilingue-v6`, no un archivo aislado.

Si la descomprimiste dentro de `~/Descargas`:

```bash
cd ~/Descargas/portfolio-andres-multilingue-v6
pwd
ls index.html content/es.json content/en.json content/pt.json tools/build.py
code .
```

**Si el directorio está en otra ubicación**, reemplazá la primera línea por la ruta real. La comprobación `ls` tiene que mostrar esos archivos; si falla, no ejecutes el generador todavía.

### Paso 2.2 — Conservar un respaldo antes de editar

Desde el **directorio padre** de la carpeta del proyecto:

```bash
cd ..
cp -a portfolio-andres-multilingue-v6 "portfolio-v6-respaldo-$(date +%Y%m%d_%H%M%S)"
cd portfolio-andres-multilingue-v6
```

El ZIP de V6 también debe conservarse intacto. El respaldo sirve para revertir accidentalmente cambios de texto o de estructura. **No copies automáticamente archivos del respaldo sobre la versión activa sin revisar qué vas a recuperar.**

### Paso 2.3 — Preparar Python sin modificar el sistema

En la raíz del proyecto:

```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements.txt
```

El comando crea un entorno virtual local e instala `beautifulsoup4`, dependencia de `build.py` y de algunas verificaciones. No hace falta repetir la instalación en cada edición.

Para trabajos posteriores, basta con entrar al directorio raíz y activar el entorno:

```bash
source .venv/bin/activate
```

Al terminar, se puede salir del entorno con:

```bash
deactivate
```

---

## 3. Localizar el texto a modificar sin confundir sus apariciones

En VS Code, en el explorador lateral abrí `content/es.json` y buscá el texto visible de la página con **Ctrl+F**. Si no aparece, utilizá **Ctrl+Shift+F** para buscar en el conjunto del proyecto.

Los JSON tienen esta organización real:

| Sector JSON | Contenido |
|---|---|
| `shared` | Textos compartidos: navegación, tarjetas, títulos de proyectos, botones y etiquetas |
| `pages.index` | Portada: presentación, experiencia, competencias, contacto, metadatos |
| `pages["projects/e60-costing"]` | Página detallada de E-60 |
| `pages["projects/telemetria-greenhouse"]` | Página detallada de TelemetriaGreenhouse |
| `pages["projects/olist-analytics"]` | Página detallada de OLIST |
| `pages["projects/fraud-detection"]` | Página detallada de prevención de fraudes |

**Atención:** los nombres de los proyectos aparecen en JSON como **claves literales con `/`** (por ejemplo, `"projects/olist-analytics"`). No son necesariamente carpetas anidadas dentro del JSON.

Algunas claves aparecen en más de una sección. Por ejemplo, el texto que describe OLIST en su **tarjeta de portada** es un valor dentro de `shared`, mientras que el texto de su **página detallada** se encuentra dentro de `pages` → `"projects/olist-analytics"` → `"detail-hero"`. Son valores independientes: modificá los que correspondan al mensaje que querés comunicar.

---

## 4. Ejemplo completo: modificar una frase en los tres idiomas

Usaremos una **clave real de V6**:

```text
pages → index → hero → reliable_data_systems
```

### Paso 4.1 — Revisar los valores actuales

**`content/es.json`:**

```json
"reliable_data_systems": "sistemas de datos confiables."
```

**`content/en.json`:**

```json
"reliable_data_systems": "reliable data systems."
```

**`content/pt.json`:**

```json
"reliable_data_systems": "sistemas de dados confiáveis."
```

### Paso 4.2 — Definir una nueva formulación en español

Supongamos que querés decir «soluciones de datos confiables» en lugar de «sistemas de datos confiables». **Solo a modo de ejemplo**, la edición coordinada sería:

**ES — `content/es.json`:**

```json
"reliable_data_systems": "soluciones de datos confiables."
```

**EN — `content/en.json`:**

```json
"reliable_data_systems": "reliable data solutions."
```

**PT-BR — `content/pt.json`:**

```json
"reliable_data_systems": "soluções de dados confiáveis."
```

Este ejemplo es **ilustrativo**: la guía no modifica esos textos en el proyecto entregado.

### Paso 4.3 — Cómo editarlos cómodamente en VS Code

1. Abrí `content/es.json`, `content/en.json` y `content/pt.json` en tres pestañas.
2. Opcional: usá **Split Editor** para ver varios archivos lado a lado.
3. Buscá `"reliable_data_systems"` en cada uno.
4. Cambiá **únicamente el texto a la derecha de `:`**. La clave `reliable_data_systems` permanece intacta en los tres idiomas.
5. Guardá los tres archivos (**Ctrl+S** en cada pestaña o **File → Save All**).
6. **No ejecutes `build.py` hasta finalizar las tres versiones.**

**Resultado esperado:** las tres traducciones existen en los JSON, pero los HTML todavía pueden mostrar la versión anterior. El siguiente apartado hace que los cambios se reflejen en todo el sitio.

---

## 5. Validar y aplicar todos los cambios en una sola generación

Con la terminal ubicada en la raíz del proyecto y el entorno virtual activo:

### Paso 5.1 — Validar primero los tres JSON

```bash
python tools/check_content.py
```

En la V6 original, una ejecución correcta informa:

```text
PASS: 3 JSON con las mismas claves; 246 textos/atributos presentes en las plantillas.
```

Esta prueba detecta JSON mal formado, diferencias de claves o marcadores faltantes. **No comprueba que las traducciones sean correctas ni detecta frases desactualizadas en otro idioma.**

### Paso 5.2 — Generar las 15 páginas a la vez

**Solo si el paso anterior terminó correctamente:**

```bash
python tools/build.py
```

Resultado esperado:

```text
OK: 15 páginas generadas (5 ES + 5 EN + 5 PT); español es idioma inicial.
```

El generador lee los tres JSON y prepara los HTML. La operación sobrescribe los HTML generados, **no** los archivos JSON ni los CV.

### Paso 5.3 — Verificar estructura y navegación

```bash
python tools/check_multilingual.py
python tools/check_site.py
```

Con los archivos originales V6, estas comprobaciones produjeron:

```text
Validated 15 pages and 432 internal links/resources
PASS: multilingual site structure and links
Checked 5 HTML pages and 144 local links/assets.
PASS: No missing local paths or anchors; each page has exactly one H1.
```

Estos números corresponden a la versión verificada, no son metas invariables si en el futuro cambia la estructura.

### Paso 5.4 — Comprobar que la nueva frase aparece en los tres HTML

En el ejemplo de la portada, abrí estos tres archivos desde VS Code y buscá la frase correspondiente:

```text
index.html
 en/index.html
 pt/index.html
```

También podés buscar por terminal, sin modificar nada (sustituyendo las frases si editaste otro texto):

```bash
grep -nF 'soluciones de datos confiables.' index.html
grep -nF 'reliable data solutions.' en/index.html
grep -nF 'soluções de dados confiáveis.' pt/index.html
```

**Interpretación:** si cada comando encuentra la frase, los tres HTML contienen la actualización. Si alguno no la encuentra, verificá el valor en el JSON correspondiente y repetí la validación/generación.

**Importante:** algunas frases se usan en una tarjeta y otras en un estudio de caso; en esos casos, buscá el HTML de la página de destino y no solo `index.html`.

---

## 6. Visualizar el resultado en la computadora (sin usar el celular)

Como la prueba desde el teléfono quedó pospuesta, usá por ahora el navegador de Ubuntu:

```bash
python -m http.server 8000 --bind 127.0.0.1
```

Entrá desde la **misma PC** en:

```text
http://127.0.0.1:8000/
http://127.0.0.1:8000/en/
http://127.0.0.1:8000/pt/
```

En Chrome o Firefox, abrí las herramientas para desarrolladores (normalmente **F12**) y activá la vista de dispositivo móvil si querés inspeccionar tamaños de pantalla sin usar el teléfono.

Para forzar la actualización del navegador, usá **Ctrl+F5**. Para detener el servidor, volvé a la terminal y presioná **Ctrl+C**.

La opción `--bind 127.0.0.1` mantiene el servidor accesible únicamente desde la computadora; no lo expone a los dispositivos de la red Wi-Fi.

---

## 7. Cambios más complejos: tarjetas, estudios de caso y SEO

### 7.1 Cambiar una descripción de tarjeta

Ejemplo real: la tarjeta OLIST tiene la clave:

```text
shared → i_participated_actively_in_the_technical_and
```

Aparece en los tres JSON. Editá la descripción en español, construí la versión en inglés y en portugués, y regenerá el sitio. Este cambio afecta la tarjeta que utiliza esa clave, **no necesariamente** el párrafo completo del estudio de caso.

### 7.2 Cambiar la presentación del estudio de caso OLIST

Buscá la ruta JSON:

```text
pages → "projects/olist-analytics" → "detail-hero"
      → "i_participated_actively_in_the_technical_and"
```

Hay una clave parecida o idéntica en `shared`, pero **su valor es independiente**. Si querés coherencia entre la tarjeta y la página detallada, revisá ambas ubicaciones en **cada uno** de los tres JSON.

El HTML resultante se encuentra en:

```text
projects/olist-analytics.html
 en/projects/olist-analytics.html
 pt/projects/olist-analytics.html
```

### 7.3 Cambiar títulos y descripciones que aparecen en buscadores

Los contenidos de `pages` tienen un bloque `metadata` por página y por idioma. Al cambiar el posicionamiento profesional o la descripción de un proyecto, revisá también los metadatos correspondientes: título de página, descripción y título para compartir. **No asumas que editar el texto visible actualiza todos los metadatos.**

### 7.4 Cambiar enlaces, imágenes, CV o diseño

Esto **no es una edición de textos JSON**. El generador toma destinos de URL de las plantillas, los archivos CV de `assets/cv/` y el diseño de `assets/css/styles.css`. No modifiques estos elementos siguiendo el procedimiento de traducción: requieren una tarea de cambio específica y su propia validación.

En V6 hay CV en español e inglés; el botón de la página portuguesa apunta al CV en inglés. No existe un CV portugués incluido en esta versión.

---

## 8. Reglas para evitar errores al editar JSON

**Correcto:**

```json
"view_selected_work": "Ver proyectos"
```

**Incorrecto:** cambiar el identificador de la izquierda:

```json
"ver_los_proyectos": "Ver proyectos"
```

El identificador es utilizado por la plantilla y debe permanecer igual en ES/EN/PT.

Otros cuidados:

- Respetá las comillas dobles (`"`) y las comas entre propiedades. No agregues comentarios `//` dentro de archivos JSON.
- Para incluir comillas dobles dentro de un valor, escribí `\"`; para incluir una barra invertida literal, escribí `\\`.
- Conservá la codificación **UTF-8**, necesaria para tildes, eñes y caracteres portugueses.
- No traduzcas nombres propios ni tecnologías: E-60, TelemetriaGreenhouse, OLIST, PySpark, PostgreSQL, MQTT, etc.
- Revisá el sentido técnico del mensaje, no solo su traducción literal. Un texto correcto en los tres idiomas debe expresar **el mismo hecho verificable**.
- Si cambiás una afirmación sensible (por ejemplo, E-60 «en desarrollo» versus «en producción»), verificá su evidencia antes de cambiar los tres idiomas y los CV asociados.

---

## 9. Qué hacer si una validación falla

| Síntoma | Acción segura |
|---|---|
| `check_content.py` indica JSON inválido | Revisar la línea/columna indicada, comas y comillas. Volver a validar antes de generar. |
| Indica claves diferentes | Comprobar si se alteró una clave en alguno de los tres archivos. Las claves deben coincidir. |
| `build.py` falla | No editar HTML para «arreglarlo»; corregir la fuente JSON o consultar el error, luego regenerar. |
| El texto visible no cambió | Confirmar que se editó la clave correcta, que se ejecutó `build.py` y actualizar el navegador con Ctrl+F5. |
| Solo un idioma tiene el texto nuevo | Completar manualmente la traducción en los otros JSON; `build.py` no traduce. |
| Texto cortado o desbordado | Revisar longitud y redacción; si no alcanza, tratarlo como cambio de diseño en CSS. |
| Necesitás recuperar una versión anterior | Comparar con el respaldo o ZIP original y restaurar selectivamente el JSON correcto. Regenerar y validar. |

**Importante:** aunque el generador prepara las páginas en memoria antes de sobrescribirlas, las validaciones no sustituyen un respaldo. Si se interrumpe la escritura por un problema externo, la copia previa permite recuperar el estado anterior.

---

## 10. Verificación de calidad antes de dar una edición por terminada

Usá esta lista por **cada bloque de contenido modificado**:

- [ ] Se identificó la **clave exacta** y en qué páginas aparece.
- [ ] La frase en `es.json` expresa un hecho verificable.
- [ ] Existe una traducción fiel y natural en `en.json`.
- [ ] Existe una traducción fiel y natural en `pt.json` (portugués de Brasil).
- [ ] Se revisaron otras apariciones relacionadas de la misma afirmación (`shared`, `pages`, `metadata`).
- [ ] Se guardaron los tres JSON y no se alteraron sus claves.
- [ ] Pasó `check_content.py`.
- [ ] Se ejecutó `build.py` **una vez** para los tres idiomas.
- [ ] Pasaron `check_multilingual.py` y `check_site.py`.
- [ ] La modificación aparece en los HTML y se comprobó visualmente en el navegador.
- [ ] Se conservó el respaldo y no se publicó información confidencial.

Una edición está **completa** cuando las tres versiones expresan el mismo contenido y el sitio regenerado supera estas comprobaciones.

---

## 11. Flujo breve para repetir en cada sesión

```text
1. Abrir la carpeta raíz de V6 en VS Code.
2. Elegir texto/clave y página donde aparece.
3. Editar es.json → preparar y revisar traducción EN → preparar y revisar PT-BR.
4. Guardar los tres JSON.
5. Ejecutar los controles y la regeneración desde la raíz:
```

```bash
source .venv/bin/activate
python tools/check_content.py
python tools/build.py
python tools/check_multilingual.py
python tools/check_site.py
```

```text
6. Revisar ES/EN/PT en el navegador local.
7. Si todo está conforme, registrar los cambios (Git, si el proyecto ya está
   versionado) y conservar la versión validada para la futura publicación.
```

**Este documento es una guía operativa descargable; no es un reemplazo de archivos del repositorio y no hay que copiarlo sobre `tools/`, `content/` ni `_source/`.** Podés conservarlo como documentación complementaria.

---

## 12. Si más adelante querés editar una sola vez y traducir automáticamente

**La arquitectura actual no lo hace.** Para lograr «modificar solo el español y actualizar automáticamente inglés y portugués» haría falta **una funcionalidad nueva**, por ejemplo un traductor asistido que:

1. Detecte las claves cambiadas en `es.json`.
2. Proponga traducciones para esas mismas claves en `en.json` y `pt.json`.
3. Muestre las traducciones para **revisión y aprobación humana**, especialmente en afirmaciones profesionales.
4. Escriba los tres JSON únicamente después de esa aprobación.
5. Ejecute las validaciones y regenere los 15 HTML.

Eso requeriría decidir el motor de traducción, la privacidad de los textos, el costo de una API si se usa, el manejo de errores y el control de versiones. **No se ha implementado ni presupuestado en V6** y no es necesario para editar y publicar el sitio ahora.

---

### Alcance de la verificación de esta guía

Procedimiento contrastado con los archivos reales incluidos en `Portfolio_Andres_Fantini_V6_Contenido_Editable_JSON(2).zip`: `README.md`, `EDITAR_CONTENIDOS_ES.md`, los JSON y los scripts de `tools/`. Los comandos de validación y regeneración se ejecutaron sobre una **copia extraída del ZIP**. No se ha modificado ni publicado el repositorio original del usuario.

**Prueba práctica adicional:** se aplicó el ejemplo de `reliable_data_systems` a una **copia temporal** de los tres JSON y se ejecutaron `check_content.py`, `build.py`, `check_multilingual.py` y `check_site.py`: todos terminaron correctamente. Se verificó además que las frases nuevas aparecieran en `index.html`, `en/index.html` y `pt/index.html`. La copia de prueba se descartó y el ZIP original permanece sin cambios.
