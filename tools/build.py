#!/usr/bin/env python3
"""Generador determinista del portfolio trilingüe (ES inicial).

Fuente de verdad: content/{es,en,pt}.json.
Diseño HTML: _source/templates/*.html y assets/css/styles.css.
Requisitos: Python 3, beautifulsoup4. No necesita conexión a Internet.
"""
from pathlib import Path
import json, html, re, os, sys
from bs4 import BeautifulSoup

ROOT = Path(__file__).resolve().parent.parent
TEMPLATES = ROOT / '_source' / 'templates'
PAGES = [
    'index.html',
    'projects/e60-costing.html',
    'projects/telemetria-greenhouse.html',
    'projects/olist-analytics.html',
    'projects/fraud-detection.html',
    'projects/vehicle-market-scraper.html',
    'projects/file-inventory.html',
]
LANGS = ('es', 'en', 'pt')
LANG_HTML = {'es': 'es-AR', 'en': 'en', 'pt': 'pt-BR'}
LOCALES = {'es': 'es_AR', 'en': 'en_US', 'pt': 'pt_BR'}
TAG_RE = re.compile(r'@@\{(shared\.[a-z0-9_]+|pages\.[a-z0-9_./-]+)\}@@')


def lookup(data: dict, dotted_key: str) -> str:
    node = data
    for part in dotted_key.split('.'):
        if not isinstance(node, dict) or part not in node:
            raise ValueError(f'Contenido inexistente en content/{data["language"]}.json: {dotted_key}')
        node = node[part]
    if not isinstance(node, str):
        raise ValueError(f'Se esperaba texto en {dotted_key}')
    return node


def read_languages():
    content = {}
    for lang in LANGS:
        path = ROOT / 'content' / f'{lang}.json'
        try:
            data = json.loads(path.read_text(encoding='utf-8'))
        except json.JSONDecodeError as ex:
            raise ValueError(f'JSON inválido: {path.name}, línea {ex.lineno}, columna {ex.colno}: {ex.msg}') from ex
        if data.get('language') != lang:
            raise ValueError(f'Idioma incorrecto en {path.name}: {data.get("language")}')
        content[lang] = data
    return content


def page_location(page: str, lang: str):
    return ROOT / (lang if lang != 'es' else '') / page


def relative_to_page(page: str, lang: str, target: Path):
    return os.path.relpath(target, start=page_location(page, lang).parent).replace(os.sep, '/')


def build_page(page: str, lang: str, texts: dict) -> str:
    template_path = TEMPLATES / page
    body = template_path.read_text(encoding='utf-8')
    body = body.replace('@@LANG@@', LANG_HTML[lang])
    # Escapado tanto para contenido de texto como para atributos HTML.
    body = TAG_RE.sub(lambda m: html.escape(lookup(texts, m.group(1)), quote=True), body)
    if '@@{' in body:
        raise ValueError(f'Hay marcadores sin resolver en {page} ({lang})')
    soup = BeautifulSoup(body, 'html.parser')
    soup.html['lang'] = LANG_HTML[lang]

    # Decisión editorial V6 (ES, EN, PT; E-60): la ruta conserva únicamente
    # el enlace de retorno y la portada no muestra estado de desarrollo.
    # Este control persiste en cada regeneración de HTML.
    if page == 'projects/e60-costing.html':
        breadcrumbs = soup.select_one('nav.crumbs')
        cover_status = soup.select_one('.detail-cover-foot > span')
        if breadcrumbs is None or cover_status is None:
            raise ValueError(f'No se encontraron los elementos editoriales E-60 ({lang})')
        for segment in breadcrumbs.find_all('span', recursive=False):
            segment.decompose()
        cover_status.decompose()


    # Caminos hacia assets compartidos: compatibles con Pages y con rutas /en/ y /pt/.
    for element in soup.find_all(True):
        for attr in ('href', 'src'):
            path = element.get(attr)
            if not isinstance(path, str):
                continue
            match = re.match(r'^(?:\.\./)*assets/(.*)$', path)
            if match:
                element[attr] = relative_to_page(page, lang, ROOT/'assets'/match.group(1))

    # Navegación entre idiomas: mantiene la misma página de proyecto.
    switcher = soup.select_one('.language-switch')
    if not switcher:
        raise ValueError(f'Falta el selector de idioma: {page}')
    for other, a in zip(LANGS, (switcher.find('a', lang=LANG_HTML[l]) for l in LANGS)):
        if a is None:
            raise ValueError(f'Falta opción de idioma {other} para {page}')
        a['href'] = relative_to_page(page, lang, page_location(page,other))
        if other == lang:
            a['aria-current'] = 'true'
        else:
            a.attrs.pop('aria-current', None)

    # CV principal por idioma: ES, EN y PT-BR aprobados.
    cv = soup.select_one('.nav-cta > .btn')
    if cv is None:
        raise ValueError(f'Falta el botón principal de CV en {page}')
    cv_name = {
        'es': 'Esteban_Andres_Fantini_CV_ES.pdf',
        'en': 'Esteban_Andres_Fantini_CV_EN.pdf',
        'pt': 'Esteban_Andres_Fantini_CV_PT_BR.pdf',
    }[lang]
    cv['href'] = relative_to_page(page, lang, ROOT/'assets'/'cv'/cv_name)

    if page == 'index.html':
        # El enlace de trayectoria abre el CV aprobado según el idioma.
        career_link = soup.select_one('.career-text a.text-link')
        if career_link is None:
            raise ValueError(f'Falta el enlace CV de trayectoria en {lang.upper()}')
        career_link['href'] = relative_to_page(
            page, lang, ROOT/'assets'/'cv'/cv_name
        )

    # Accesibilidad: etiquetas del menú editables en JSON.
    button = soup.select_one('.menu-toggle')
    if button:
        button['data-label-open'] = lookup(texts, 'shared.aria_label_open_navigation')
        button['data-label-close'] = texts['shared']['aria_label_close_navigation']

    # SEO: hreflang completo, y español como x-default.
    for alternate in soup.find_all('link', rel='alternate'):
        other_lang = alternate.get('hreflang')
        if other_lang == 'x-default': other_lang = 'es-AR'
        reverse = {v:k for k,v in LANG_HTML.items()}
        alternate['href'] = relative_to_page(page,lang,page_location(page,reverse[other_lang]))
    og = soup.find('meta',attrs={'property':'og:locale'})
    if og:
        og['content'] = LOCALES[lang]

    text = str(soup).replace('<!DOCTYPE html>', '').replace('<!doctype html>', '').strip()
    return '<!doctype html>\n' + text + '\n'


def main():
    content = read_languages()
    # Crear todas las páginas en memoria antes de escribir: ante un error JSON no se
    # produce un sitio parcialmente regenerado.
    generated = {}
    for lang, config in content.items():
        for page in PAGES:
            generated[page_location(page,lang)] = build_page(page,lang,config)
    for target, data in generated.items():
        target.parent.mkdir(parents=True, exist_ok=True)
        target.write_text(data,encoding='utf-8')
    print(f'OK: {len(generated)} páginas generadas ({len(PAGES)} ES + {len(PAGES)} EN + {len(PAGES)} PT); español es idioma inicial.')

if __name__=='__main__':
    try: main()
    except (ValueError, KeyError, OSError) as exc:
        print(f'ERROR: {exc}',file=sys.stderr)
        sys.exit(1)
