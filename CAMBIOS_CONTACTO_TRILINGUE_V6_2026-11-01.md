# V6 — Revisión del panel CONTACTO (1 noviembre 2026)

Última fuente: `portfolio-andres-multilingue-v6-4-correcciones-HOME-ES-PT-EN.zip`.

Pedido de usuario: retirar enlaces a los CV dentro del panel de Contacto; encabezado Contactos; incorporar dos teléfonos; agregar un segundo grupo Repositorio con GitHub, traducido a ES/PT/EN.

| Idioma | Encabezado contacto | Encabezado repositorio |
| --- | --- | --- |
| ES | CONTACTOS | REPOSITORIO |
| PT-BR | CONTATOS | REPOSITÓRIO |
| EN | CONTACTS | REPOSITORY |

Contenido por idioma: correo `andres.fantini@mi.unc.edu.ar ↗` (`mailto:`), teléfonos `ARG: +54 9 (351) 234-8539` y `BR / WhatsApp: +55 11 97 859-2020` y enlace GitHub `https://github.com/andresfantini` bajo Repositorio. Sin enlaces CV en ese panel. El resto del sitio, incluidos los CV descargables desde navegación principal, permanece intacto.

Archivos de contenido: `content/es.json`, `content/pt.json`, `content/en.json`.
Plantilla canónica: `_source/templates/index.html`.
Generador: `tools/build.py` (eliminada inserción ad hoc de CV en panel PT).
Estilos: `assets/css/styles.css`.
Generados: `index.html`, `pt/index.html`, `en/index.html`.

**Entrega diferida:** usuario pidió esperar su próximo prompt antes de entregar una nueva versión. Esta carpeta se conserva en `portfolio_V6_WORKING_CONTACTOS_pending` y no se publica.

## SHA256 previos (componentes editados)
- `_source/templates/index.html`: `5c7e3e123891230d3bb57e6d1641c41aeb7bbaf7cc16e0f3f988b9d436230971`
- `tools/build.py`: `4404fe91d86f6eda4f1f692737a48f6d52408560d80d230275c445199dc44044`
- `assets/css/styles.css`: `0cbaf5b6eeb8b096be8dbcb3a202ab484fdf3a5363a622283e2b132141caeec3`
- `content/es.json`: `7686b599469c83c31a4b7823d4d4b6367866db3ec1f88237592d22c4dec23df9`
- `content/pt.json`: `afb1069e6651e9ef25b3f6cb2a65d4d4c5c38c5072595d3ad44750583d082c7a`
- `content/en.json`: `6c88406e31bcc8463b1930053e38014fe88cf7cd3e73f925c3657575e667d562`
