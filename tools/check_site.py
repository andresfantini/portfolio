#!/usr/bin/env python3
"""Offline link/asset/anchor validation for this static portfolio. Python stdlib only."""
import re
import sys
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import unquote, urlsplit
ROOT = Path(__file__).resolve().parent.parent
class HTMLIndex(HTMLParser):
    def __init__(self):
        super().__init__();self.links=[];self.ids=set();self.h1_count=0
    def handle_starttag(self, tag, attrs):
        kv=dict(attrs)
        if 'id' in kv:self.ids.add(kv['id'])
        if tag=='a' and 'href' in kv:self.links.append(('href',kv['href']))
        if tag in ('script','img') and 'src' in kv:self.links.append(('src',kv['src']))
        if tag=='link' and 'href' in kv:self.links.append(('href',kv['href']))
        if tag=='h1':self.h1_count+=1

def parsed(path):
    p=HTMLIndex();p.feed(path.read_text(encoding='utf-8'));return p

def check():
    paths=[ROOT/'index.html', *sorted((ROOT/'projects').glob('*.html'))]
    errors=[];counts=0
    indices={path:parsed(path) for path in paths}
    for path,doc in indices.items():
        if doc.h1_count!=1:errors.append(f'{path.name}: expected exactly one H1, got {doc.h1_count}')
        for label,target in doc.links:
            u=urlsplit(target)
            if u.scheme or u.netloc:continue
            if u.path:
                dest=(path.parent/unquote(u.path)).resolve()
                if not dest.is_file():errors.append(f'{path.name}: missing {label} {target}');continue
                if u.fragment and dest in indices and u.fragment not in indices[dest].ids: errors.append(f'{path.name}: missing anchor {target}')
            elif u.fragment and u.fragment not in doc.ids:errors.append(f'{path.name}: missing anchor #{u.fragment}')
            counts+=1
    print(f'Checked {len(paths)} HTML pages and {counts} local links/assets.')
    if errors:
        print('\n'.join(errors));return 1
    print('PASS: No missing local paths or anchors; each page has exactly one H1.')
    return 0
if __name__=='__main__':sys.exit(check())
