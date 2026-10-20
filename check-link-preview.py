#!/usr/bin/env python3
"""Checks the link preview of your live GitHub Pages site the way WhatsApp/Facebook read it.
Usage:  python3 check-link-preview.py https://YOUR-USERNAME.github.io/YOUR-REPO/
"""
import sys,urllib.request,re,io
from html.parser import HTMLParser
url=sys.argv[1] if len(sys.argv)>1 else input('Your site address: ').strip()
def get(u,limit=None):
    r=urllib.request.Request(u,headers={'User-Agent':'WhatsApp/2.23 facebookexternalhit/1.1'})
    with urllib.request.urlopen(r,timeout=30) as f: return f.status,f.headers.get('Content-Type',''),(f.read(limit) if limit else f.read())
st,ct,html=get(url,400000);html=html.decode('utf8','ignore')
class P(HTMLParser):
    def __init__(s):super().__init__();s.m={}
    def handle_starttag(s,t,a):
        a=dict(a)
        if t=='meta' and a.get('property','').startswith('og:'):s.m.setdefault(a['property'],a.get('content'))
p=P();p.feed(html);m=p.m;bad=0
def chk(ok,msg):
    global bad;print(('OK    ' if ok else 'FIX   ')+msg);bad+=0 if ok else 1
chk(st==200,'page loads (HTTP %s)'%st)
for k in ('og:title','og:description','og:image','og:url'): chk(bool(m.get(k)) and 'YOUR-' not in m[k],'%s = %s'%(k,m.get(k)))
img=m.get('og:image','')
if img and 'YOUR-' not in img:
    st2,ct2,data=get(img);chk(st2==200 and ct2.startswith('image/'),'image address works (%s, %s, %d KB)'%(st2,ct2,len(data)//1024))
    chk(len(data)<300*1024,'image is under 300 KB (WhatsApp limit for best results)')
    chk(img.startswith('https://'),'image address is https and absolute')
print('\nAll good: the preview should show the red curtain image.' if not bad else '\n%d item(s) to fix, see FIX lines above.'%bad)
