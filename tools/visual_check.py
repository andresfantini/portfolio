#!/usr/bin/env python3
"""Headless viewports, navigation and multilingual URL checks for local static site."""
from pathlib import Path
from playwright.sync_api import sync_playwright
from bs4 import BeautifulSoup
import base64
R=Path(__file__).resolve().parent.parent
css=(R/'assets/css/styles.css').read_text(encoding='utf-8')
js=(R/'assets/js/main.js').read_text(encoding='utf-8')
def inline(path):
 soup=BeautifulSoup(path.read_text(encoding='utf-8'),'html.parser')
 for tag in soup.find_all('link',rel='stylesheet'):tag.decompose()
 style=soup.new_tag('style');style.string=css;soup.head.append(style)
 for img in soup.find_all('img',src=True):
  if not img['src'].startswith('data:'):
   file=(path.parent/img['src']).resolve();img['src']='data:image/svg+xml;base64,'+base64.b64encode(file.read_bytes()).decode('ascii')
 for tag in soup.find_all('script',src=True):tag.decompose()
 tag=soup.new_tag('script');tag.string=js;soup.body.append(tag)
 return str(soup)
with sync_playwright() as p:
 browser=p.chromium.launch(executable_path='/usr/bin/chromium',args=['--no-sandbox'],headless=True)
 for lang in ['en','es','pt']:
  for page in ['index.html','projects/telemetria-greenhouse.html','projects/olist-analytics.html']:
   for width in [320,390,768,850,1024,1440]:
    tab=browser.new_page(viewport={'width':width,'height':900},device_scale_factor=1)
    errs=[];tab.on('pageerror',lambda e:errs.append(str(e)))
    f=R/(lang if lang!='es' else '')/page
    tab.set_content(inline(f),wait_until='load')
    result=tab.evaluate('''()=>({scrollWidth:document.documentElement.scrollWidth,width:innerWidth,lang:document.documentElement.lang,h1:document.querySelector('h1').textContent.trim(),visible:document.querySelectorAll('.language-switch a').length})''')
    if result['scrollWidth']>width+1:
     culprits=tab.evaluate('''()=>Array.from(document.querySelectorAll('body *')).filter(x=>x.getBoundingClientRect().right>innerWidth+2).slice(0,12).map(x=>({tag:x.tagName,cls:x.className,txt:x.textContent.slice(0,60),width:x.getBoundingClientRect().width,right:x.getBoundingClientRect().right}))''')
     print('OVERFLOW',lang,page,width,result,culprits)
     raise AssertionError('Overflow')
    if errs:raise AssertionError(f'Page JS error: {errs}')
    if result['visible']!=3:raise AssertionError('Language links not rendered')
    if 'telemetria' in page:
     assert tab.locator('h1').inner_text()=='TelemetriaGreenhouse'
     single=tab.evaluate('''()=>{let h=document.querySelector('h1'),cs=getComputedStyle(h);let ctx=document.createElement('canvas').getContext('2d');ctx.font=cs.font;return [cs.whiteSpace,ctx.measureText(h.textContent.trim()).width,h.getBoundingClientRect().width]}''')
     assert single[0]=='nowrap' and single[1]<=single[2]+1,(lang,width,single)
    if page=='index.html' and width==390:
     tab.locator('.menu-toggle').click()
     assert tab.locator('#primary-menu').evaluate('(el)=>getComputedStyle(el).display')=='flex'
     tab.locator('.menu-toggle').click()
    if page=='index.html' and width in [390,1440]:
     tab.screenshot(path=str(R.parent/f'Portfolio_Multilingue_{lang}_{width}.png'),full_page=False)
    if 'olist' in page and width==1440:
     tab.screenshot(path=str(R.parent/f'Portfolio_Multilingue_OLIST_{lang}.png'),full_page=False)
    tab.close()
 browser.close()
print('PASS: 54 responsive combinations; mobile menu; OLIST; title width; 0 JS errors')
