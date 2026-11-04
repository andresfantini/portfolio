# Manual breve — Editar los textos del portfolio

**Versión V5.** Los textos de las 15 páginas están centralizados en 3 archivos JSON. No hay que abrir los HTML para cambiar párrafos, títulos, botones ni textos alternativos. El idioma inicial continúa siendo **español**.

## 1. ¿Qué archivo modifico?

- `content/es.json`: textos publicados en español.
- `content/en.json`: textos publicados en inglés.
- `content/pt.json`: textos publicados en portugués de Brasil.

Abrí la carpeta del portfolio en **VS Code**. Por ejemplo, para modificar la presentación de OLIST en español, abrí `content/es.json` y buscá `Participé activamente` (Ctrl+F).

La estructura agrupa el contenido en:

- `shared`: textos reutilizados en distintas páginas (nombre de proyecto, barra de navegación, etc.). Un cambio puede actualizar varias páginas.
- `pages.index`: portada y secciones de inicio.
- `pages.projects/olist-analytics`: estudio de caso OLIST.
- `pages.projects/fraud-detection`: estudio de caso Fraude.
- `pages.projects/e60-costing` y `pages.projects/telemetria-greenhouse`: otros dos casos.

Dentro de cada página, las subsecciones como `hero`, `detail-hero` y `detail-body` reúnen los textos correspondientes.

## 2. Cómo cambiar una frase

Ejemplo simplificado de JSON:

```json
"hero": {
  "from_operations_to": "De los procesos a",
  "reliable_data_systems": "sistemas de datos confiables."
}
```

Podés cambiar solamente lo que está **a la derecha de los dos puntos**, entre comillas, por ejemplo:

```json
"reliable_data_systems": "soluciones de datos confiables."
```

**Conservá** las claves de la izquierda, las comillas, las comas y las llaves. Si el texto contiene comillas dobles, escribilas escapadas como `\"`; si contiene barras invertidas, usá `\\`.

Para modificar la tarjeta de OLIST en la portada, buscá en `shared` la clave `i_participated_actively_in_the_technical_and`. Para modificar el párrafo principal de su página, buscá en `pages` → `projects/olist-analytics` → `detail-hero` la misma frase (el identificador de texto se repite en diferentes secciones, pero sus valores pueden variar).

## 3. Regenerar el sitio

Con una terminal abierta en la carpeta del portfolio, ejecutá:

```bash
python3 tools/check_content.py
python3 tools/build.py
python3 tools/check_multilingual.py
```

Si falta la biblioteca `bs4`, prepará primero el entorno aislado siguiendo el `README.md` y ejecutá los mismos comandos dentro de ese entorno (con `python` en lugar de `python3` si fuera necesario).

El resultado son **15 archivos HTML listos para publicar**, distribuidos así:

- `index.html` y `projects/`: español.
- `en/index.html` y `en/projects/`: inglés.
- `pt/index.html` y `pt/projects/`: portugués.

**Atención:** `build.py` sobrescribe los HTML generados. Los JSON son la única fuente editable de los textos. Cambiar una traducción no actualiza automáticamente las otras dos.

## 4. Vista previa

```bash
python3 -m http.server 8000
```

Entrá en `http://localhost:8000/` y revisá la portada, OLIST y el menú ES / EN / PT. Detené el servidor con `Ctrl+C`.

## 5. Si algo sale mal

- **Error de JSON:** VS Code suele señalar una coma o comilla faltante; `check_content.py` detecta errores de estructura.
- **Texto no aparece:** confirmá que ejecutaste `build.py` y actualizá la página con Ctrl+F5.
- **Texto largo desborda:** acortalo o revisá `assets/css/styles.css`; el diseño no se modifica desde JSON.
- **Necesitás cambiar un enlace:** los destinos URL se mantienen en las plantillas y la estructura HTML; el JSON edita texto visible, no enlaces ni arquitectura.
- **Revertir:** restaurá el JSON desde Git o desde la copia ZIP original, y reconstruí.

## 6. Recomendación de trabajo

Conservá una copia del ZIP V5 antes de editar y utilizá Git para registrar cambios. Si vas a modificar el contenido en un repositorio, revisá el resultado localmente antes de hacer commit y publicar.

**Importante:** el sitio todavía no está publicado en GitHub Pages.
