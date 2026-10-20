"""Aiuto per il collaudo sul telefono Android (adb + uiautomator).
    python tel.py testi                 i testi a video
    python tel.py tocca "<testo>"       tocca il primo elemento il cui testo contiene <testo>
    python tel.py scrivi "<testo>"      scrive nel campo che ha il fuoco
    python tel.py indietro              tasto indietro
    python tel.py foto <file.png>       fotografa lo schermo
"""
import re
import sys as _s
_s.stdout.reconfigure(encoding="utf-8", errors="replace")
import subprocess
import sys
import xml.etree.ElementTree as ET

ADB = r"C:\Program Files (x86)\Android\android-sdk\platform-tools\adb.exe"


import os
SERIALE = os.environ.get('TEL', 'emulator-5554')


def adb(*a, testo=True):
    r = subprocess.run([ADB, '-s', SERIALE, *a], capture_output=True)
    return r.stdout.decode('utf-8', 'replace') if testo else r.stdout


def nodi():
    adb('shell', 'uiautomator', 'dump', '/sdcard/rsa-ui.xml')
    x = adb('shell', 'cat', '/sdcard/rsa-ui.xml')
    x = x[x.find('<?xml'):]
    return [n for n in ET.fromstring(x).iter('node')]


def testo(n):
    return (n.get('text') or n.get('content-desc') or '').strip()


cmd = sys.argv[1]
if cmd == 'testi':
    print(' | '.join(t for t in (testo(n) for n in nodi()) if t))
elif cmd in ('tocca', 'tocca='):
    for n in reversed(nodi()) if cmd == 'tocca=' else nodi():
        if (testo(n) == sys.argv[2]) if cmd == 'tocca=' else (sys.argv[2] in testo(n)):
            x1, y1, x2, y2 = map(int, re.findall(r'\d+', n.get('bounds')))
            adb('shell', 'input', 'tap', str((x1 + x2) // 2), str((y1 + y2) // 2))
            print('toccato', testo(n), 'abilitato' if n.get('enabled') == 'true' else 'SPENTO')
            break
    else:
        print('NON TROVATO', sys.argv[2])
        sys.exit(1)
elif cmd == 'scrivi':
    adb('shell', 'input', 'text', sys.argv[2].replace(' ', '%s'))
elif cmd == 'indietro':
    adb('shell', 'input', 'keyevent', 'KEYCODE_BACK')
elif cmd == 'campo':
    # campo di testo n-esimo (indice) fra gli EditText a video: tel.py campo <indice> <valore>
    ed = [n for n in nodi() if n.get('class') == 'android.widget.EditText']
    n = ed[int(sys.argv[2])]
    x1, y1, x2, y2 = map(int, re.findall(r'\d+', n.get('bounds')))
    adb('shell', 'input', 'tap', str((x1 + x2) // 2), str((y1 + y2) // 2))
    adb('shell', 'input', 'keyevent', 'KEYCODE_MOVE_END')
    adb('shell', 'input', 'keyevent', *(['KEYCODE_DEL'] * 40))
    adb('shell', 'input', 'text', sys.argv[3].replace(' ', '%s'))
    print('scritto nel campo', sys.argv[2])
elif cmd == 'nodi':
    for n in nodi():
        t = testo(n)
        if t or n.get('clickable') == 'true':
            print(repr(t), n.get('class'), n.get('bounds'), 'hint=' + (n.get('hint') or ''))
elif cmd == 'foto':
    open(sys.argv[2], 'wb').write(adb('exec-out', 'screencap', '-p', testo=False))
