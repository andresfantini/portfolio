#!/usr/bin/env python3
"""Local structural checks for all three languages and their project pages."""
from pathlib import Path
from bs4 import BeautifulSoup
from urllib.parse import urlsplit
ROOT=Path(__file__).resolve().parent.parent
LANGS={'en':'en','es':'es-AR','pt':'pt-BR'}
PAGES=['index.html','projects/e60-costing.html','projects/telemetria-greenhouse.html','projects/olist-analytics.html','projects/fraud-detection.html','projects/vehicle-market-scraper.html','projects/file-inventory.html']
errors=[];checked=0
for l,html_lang in LANGS.items():
 for page in PAGES:
  f=(ROOT/(l if l!='es' else '')/page)
  if not f.is_file():errors.append(f'Missing {f}');continue
  soup=BeautifulSoup(f.read_text(encoding='utf-8'),'html.parser')
  if soup.html.get('lang')!=html_lang:errors.append(f'{f}: language mismatch')
  if len(soup.select('.language-switch a'))!=3:errors.append(f'{f}: missing language switch')
  if len(soup.select('link[rel="alternate"][hreflang]'))!=4:errors.append(f'{f}: hreflang count')
  if page=='index.html' and l=='es' and f != ROOT/'index.html':errors.append('Spanish not at root')
  for el in soup.select('[href], [src]'):
   url=el.get('href') or el.get('src')
   sp=urlsplit(url)
   if sp.scheme or url.startswith('//') or url.startswith('data:'):continue
   path=sp.path
   target=(f.parent / path).resolve() if path else f
   if not target.is_file():errors.append(f'{f.relative_to(ROOT)}: {url} missing')
   if sp.fragment and (path.endswith('.html') or not path):
    target_dom=BeautifulSoup(target.read_text(encoding='utf-8'),'html.parser') if target.suffix=='.html' else soup
    if not target_dom.find(id=sp.fragment):errors.append(f'{f.relative_to(ROOT)}: invalid anchor {url}')
   checked+=1
  for a in soup.select('.language-switch a'):
   expected=(ROOT/(a.get_text(strip=True).lower() if a.get_text(strip=True)!='ES' else '')/page).resolve()
   actual=(f.parent / a['href']).resolve()
   if expected!=actual:errors.append(f'{f}: wrong language link {a.get_text(strip=True)} -> {a["href"]}')
  h1=soup.find('h1')
  if not h1:errors.append(f'{f}: missing H1')
  if page=='index.html':
   if len(soup.select('.project-card'))!=6:errors.append(f'{f}: projects missing')
  else:
   if len(soup.select('.article h2'))!=4:errors.append(f'{f}: incomplete project content')
print(f'Validated {len(LANGS)*len(PAGES)} pages and {checked} internal links/resources')
if errors:
 print('\n'.join(errors[:100]));raise SystemExit(f'FAILED: {len(errors)} issues')
print('PASS: multilingual site structure and links')
