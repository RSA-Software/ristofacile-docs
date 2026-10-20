"""Copia le catture nel manuale: oscura nomi e dati sensibili (OCR di Windows), riduce, crea i segnaposto."""
import os, re, subprocess
from PIL import Image, ImageDraw, ImageFont, ImageFilter

S = r'C:\Users\filippo\AppData\Local\Temp\claude\C--RSA-CLAUDE-RistoFacile\2f92d64e-beea-4f3e-8f9f-7d91753b0dd1\scratchpad'
SHOT = os.path.join(S, 'shot')
OCR = os.path.join(S, 'ocr', 'bin', 'Debug', 'net10.0-windows10.0.19041.0', 'ocr.exe')
DOCS = r'C:\RSA.CLAUDE\ristofacile-docs\docs'
IMG = os.path.join(DOCS, 'assets', 'img')

MAPPA = {
    'cassa/accesso': 'cassa-accesso', 'cassa/accesso-pin': 'cassa-accesso-pin',
    'cassa/articoli': 'g-articoli', 'cassa/centri-di-produzione': 'g-centri-di-produzione',
    'cassa/centri-di-produzione-scheda': 'h-centri-di-produzione',
    'cassa/comanda': 'tav13-7-inviata', 'cassa/comanda-righe': 'tav13-8', 'cassa/comanda-riga': 'tav13-varianti2',
    'cassa/comanda-preconto': 'cassa-preconto', 'cassa/conto': 'cassa-conto-2', 'cassa/disponibilita': 'h-disponibilita',
    'cassa/dividi-conto': 'cassa-dividi-2', 'cassa/fatture': 'g-fatture',
    'cassa/impostazioni': 'i-turno', 'cassa/impostazioni-turno': 'i-turno', 'cassa/impostazioni-connessione': 'i-connessione',
    'cassa/impostazioni-sala': 'i-sala', 'cassa/impostazioni-preconto': 'i-preconto', 'cassa/impostazioni-modelli': 'i-modelli',
    'cassa/impostazioni-fiscale': 'i-fiscale', 'cassa/impostazioni-carte': 'i-carte',
    'cassa/impostazioni-cassa-automatica': 'i-cassa-automatica', 'cassa/impostazioni-aspetto': 'i-aspetto',
    'cassa/impostazioni-hotel': 'i-hotel', 'cassa/impostazioni-licenza': 'i-licenza',
    'cassa/mappa-sala': 'cassa-unisci-2', 'cassa/mappa-sala-separa': 'cassa-separa-righe',
    'cassa/menu': 'g-menu', 'cassa/menu-composizione': 'menu-composizione-casa', 'cassa/menu-sezione': 'menu-sezione-modale',
    'cassa/menu-piatto': 'menu-piatto-modale', 'cassa/menu-laterale': 'cassa-menu-laterale',
    'cassa/menu-online': 'i-menu-online', 'cassa/menu-online-qrcode': 'i-menu-online',
    'cassa/messaggi': 'v-messaggi', 'cassa/modificatori': 'h-modificatori',
    'cassa/operatori': 'g-operatori', 'cassa/operatori-scheda': 'cassa-operatori-scheda',
    'cassa/portate': 'h-portate', 'cassa/prenotazioni': 'v-prenotazioni', 'cassa/regole-di-composizione': 'h-regole-di-composizione',
    'cassa/sale-e-tavoli': 'g-sale-e-tavoli', 'cassa/sale-e-tavoli-scheda-sala': 'h-sale-e-tavoli',
    'cassa/statistiche': 'g-statistiche', 'cassa/storico-conti': 'g-storico-conti', 'cassa/storico-conti-scheda': 'h-storico-conti-scheda',
    'cassa/tabelle-di-base': 'h-tabelle-di-base', 'cassa/varianti-anagrafica': 'h-varianti-anagrafica',
    'cassa/vendita-al-banco': 'v-banco', 'cassa/asporto': 'v-asporto',
    'introduzione/home': 'cassa-unisci-2', 'introduzione/serata-mappa': 'cassa-sala-principale',
    'introduzione/serata-accesso': 'cassa-accesso-pin', 'introduzione/serata-comanda': 'tav13-7-inviata',
    'introduzione/serata-dettagli': 'tav13-dettagli', 'introduzione/serata-monitor': 'kds-pizzeria-6',
    'introduzione/serata-mezza': 'and-mezza-2', 'introduzione/serata-preconto': 'cassa-preconto',
    'introduzione/serata-conto': 'cassa-conto-2', 'introduzione/serata-dividi': 'cassa-dividi-2',
    'introduzione/licenza': 'and-licenza', 'introduzione/prima-configurazione': 'i-connessione',
    'introduzione/prima-configurazione-kds': 'kds-centro',
    'kds/centro': 'kds-centro', 'kds/index': 'kds-monitor-pieno', 'kds/monitor': 'kds-pizzeria-6',
    'kds/monitor-messaggio': 'kds-messaggio', 'kds/monitor-card': 'kds-pizzeria-5',
    'palmare/accesso': 'and-accesso', 'palmare/accesso-pin': 'and-accesso-pin', 'palmare/sala': 'and-sala',
    'palmare/index': 'and-sala-2', 'palmare/comanda': 'and-comanda-2', 'palmare/comanda-righe': 'and-comanda-via',
    'palmare/comanda-mezza': 'and-mezza-2', 'palmare/conto': 'p-conto', 'palmare/io': 'p-Io', 'palmare/menu': 'p-Menu',
    'palmare/messaggi': 'p-messaggi', 'palmare/ordini': 'p-Ordini', 'palmare/ordini-nuovo': 'p-nuovo-asporto',
    'palmare/prenotazioni': 'p-prenotazioni', 'palmare/prenotazioni-modulo': 'p-prenotazione-modulo',
    'palmare/impostazioni': 'and-aspetto', 'palmare/impostazioni-licenza': 'and-licenza',
    'palmare/impostazioni-connessione': 'and-2',
}
SENSIBILI = re.compile(r'CAPIZZI|FILIPPO|RAFFAELE|CAMILLERI|MARCELLO|camilleri|[A-Za-z0-9]{22,}')


def ocr(path):
    out = subprocess.run([OCR, path], capture_output=True).stdout.decode('latin-1')
    for riga in out.splitlines():
        m = re.match(r'^(\d+) (\d+) (\d+) (\d+) (.*)$', riga.strip('\r'))
        if m:
            yield int(m[1]), int(m[2]), int(m[3]), int(m[4]), m[5]


def oscura(im, path):
    n = 0
    for x, y, w, h, t in ocr(path):
        if SENSIBILI.search(t):
            pad = max(6, h // 3)
            box = (max(0, x - pad), max(0, y - pad), min(im.width, x + w + pad), min(im.height, y + h + pad))
            zona = im.crop(box)
            piccola = zona.resize((max(1, zona.width // 14), max(1, zona.height // 14)))
            im.paste(piccola.resize(zona.size, Image.NEAREST).filter(ImageFilter.GaussianBlur(3)), box)
            n += 1
    return n


for dst, src in MAPPA.items():
    sp = os.path.join(SHOT, src + '.png')
    if not os.path.exists(sp):
        print('MANCA la cattura', src)
        continue
    im = Image.open(sp).convert('RGB')
    n = oscura(im, sp)
    larg = 540 if im.height > im.width else 1600
    if im.width > larg:
        im = im.resize((larg, int(im.height * larg / im.width)), Image.LANCZOS)
    out = os.path.join(IMG, dst + '.png')
    os.makedirs(os.path.dirname(out), exist_ok=True)
    im.save(out, optimize=True)
    print(f'{dst:45s} <- {src:28s} oscurate {n}')

# segnaposto per le immagini citate e non ancora catturate
rif = set()
for radice, _, files in os.walk(DOCS):
    for f in files:
        if f.endswith('.md'):
            testo = open(os.path.join(radice, f), encoding='utf-8').read()
            rif.update(re.findall(r'assets/img/([a-z]+/[a-z0-9-]+)\.png', testo))
mancanti = sorted(r for r in rif if not os.path.exists(os.path.join(IMG, r + '.png')))
font = ImageFont.truetype(r'C:\Windows\Fonts\segoeui.ttf', 30)
for r in mancanti:
    w, h = (540, 900) if r.startswith('palmare/') else (1600, 1000)
    im = Image.new('RGB', (w, h), (245, 246, 248))
    d = ImageDraw.Draw(im)
    d.rectangle([4, 4, w - 5, h - 5], outline=(242, 117, 31), width=4)
    d.multiline_text((w // 2, h // 2), 'Schermata da catturare\n' + r + '.png', fill=(120, 120, 120), font=font, anchor='mm', align='center')
    out = os.path.join(IMG, r + '.png')
    os.makedirs(os.path.dirname(out), exist_ok=True)
    im.save(out, optimize=True)
with open(r'C:\RSA.CLAUDE\ristofacile-docs\tools\schermate-da-catturare.txt', 'w', encoding='utf-8') as f:
    f.write('\n'.join(m + '.png' for m in mancanti) + '\n')
print('segnaposto:', len(mancanti))
