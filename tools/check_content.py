#!/usr/bin/env python3
"""Comprobar coherencia, cobertura y seguridad de la fuente JSON de los 3 idiomas."""
from pathlib import Path
import json,re,sys
ROOT=Path(__file__).resolve().parent.parent
MARKER=re.compile(r'@@\{(shared\.[a-z0-9_]+|pages\.[a-z0-9_./-]+)\}@@')
PAGES=['index.html',*[f'projects/{slug}.html' for slug in ['e60-costing','telemetria-greenhouse','olist-analytics','fraud-detection']]]

def flatten(obj,prefix=''):
    for k,v in obj.items():
        key=prefix+'.'+k if prefix else k
        if isinstance(v,dict):yield from flatten(v,key)
        elif isinstance(v,str):yield key,v
        else:raise ValueError(f'Valor no textual en {key}: {type(v)}')

def main():
    contents={lang:json.loads((ROOT/'content'/f'{lang}.json').read_text(encoding='utf-8')) for lang in ('es','en','pt')}
    keys={k:set(name for name,_ in flatten(data['shared'])) | set(name for name,_ in flatten(data['pages'])) for k,data in contents.items()}
    if not (keys['es']==keys['en']==keys['pt']):
        raise ValueError('Las claves de los JSON no coinciden entre idiomas')
    tokens=set()
    for page in PAGES:
        t=(ROOT/'_source'/'templates'/page).read_text(encoding='utf-8')
        found=set(MARKER.findall(t))
        tokens |= found
        if re.sub(MARKER,'',t).find('@@{')!=-1:
            raise ValueError(f'Marcadores mal formados en {page}')
    for lang,data in contents.items():
        full={'shared.'+k:v for k,v in flatten(data['shared'])}
        full.update({'pages.'+k:v for k,v in flatten(data['pages'])})
        missing=tokens-set(full)
        if missing:raise ValueError(f'Faltan {len(missing)} textos para {lang}: {sorted(missing)[:5]}')
        if any('@@{' in v for v in full.values()):raise ValueError(f'Hay marcadores incrustados en content/{lang}.json')
    print(f'PASS: 3 JSON con las mismas claves; {len(tokens)} textos/atributos presentes en las plantillas.')

if __name__=='__main__':
    try:main()
    except (OSError,ValueError,json.JSONDecodeError) as exc:
        print(f'ERROR: {exc}',file=sys.stderr)
        sys.exit(1)
