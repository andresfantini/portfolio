# Publicación del portfolio trilingüe V5 en GitHub Pages

## Antes de publicar

1. Revisá `http://localhost:8000/` en español, inglés y portugués. El idioma de inicio es español.
2. Validá que los cuatro proyectos se muestran correctamente y que sus enlaces funcionen.
3. Recordá que **los dos CV estarán disponibles públicamente**: verificá sus datos de contacto, logros y estados de proyecto antes de publicar.
4. Revisá las condiciones de difusión de trabajos grupales OLIST/Fraude y no publiques código o información confidencial de E-60.

## Regeneración y pruebas

```bash
python3 tools/check_content.py
python3 tools/build.py
python3 tools/check_multilingual.py
```

Para ver el resultado sin publicar:

```bash
python3 -m http.server 8000
```

Abrí `http://localhost:8000/` y detené con `Ctrl+C`.

## Publicar usando un repositorio nuevo

1. Ingresá a GitHub y creá un **repositorio público nuevo** (por ejemplo, `portfolio`). No sobrescribas repositorios existentes.
2. Cargá el contenido de la carpeta principal; `index.html` debe quedar en la **raíz** del repositorio. Incluí `content/` y `_source/` si querés conservar la fuente editable en GitHub.
3. En GitHub, entrá a **Settings → Pages → Build and deployment**. Seleccioná **Deploy from a branch** y elegí `main`, directorio `/ (root)`.
4. GitHub indicará el enlace del sitio cuando termine el despliegue.
5. Revisá la página de inicio en español, el selector ES/EN/PT, los cuatro casos de estudio y los enlaces a los CV.
6. Una vez comprobado, incorporá el enlace a LinkedIn y al CV.

Las rutas relativas funcionan tanto en `usuario.github.io/portfolio/` como en `usuario.github.io`.

**No se realizó ninguna publicación automática ni modificación de tu cuenta GitHub.**

## Modificar textos después de publicar

1. Editá el JSON de cada idioma en tu copia local (véase `EDITAR_CONTENIDOS_ES.md`).
2. Regenerá y validá con los tres comandos anteriores.
3. Confirmá los cambios en Git y subí los HTML regenerados junto a los JSON al repositorio.

GitHub Pages publica archivos estáticos; **no ejecuta automáticamente `tools/build.py`** con esta configuración. Por lo tanto, los HTML regenerados deben subirse junto con el contenido JSON.
