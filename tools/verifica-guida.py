r"""Confronta i codici della guida contestuale dichiarati dalle app con guida.yml.

Uso: python tools/verifica-guida.py [cartella di RistoFacile]   (predefinita C:\RSA.NET\RistoFacile)
Exit 1 se un codice dell'app non ha la sua riga in guida.yml (F1 aprirebbe l'indice della cassa).
"""

import pathlib
import re
import sys

import yaml

app = pathlib.Path(sys.argv[1] if len(sys.argv) > 1 else r"C:\RSA.NET\RistoFacile")
codici_cs = app / "RistoCore" / "Services" / "Guida" / "CodiciGuida.cs"
testo = codici_cs.read_text(encoding="utf-8-sig")
nell_app = set(re.findall(r'public const string \w+ = "([^"]+)";', testo))

guida = pathlib.Path(__file__).resolve().parent.parent / "guida.yml"
nel_manuale = {str(k) for k in (yaml.safe_load(guida.read_text(encoding="utf-8")) or {})}

mancanti = sorted(nell_app - nel_manuale)
inutili = sorted(nel_manuale - nell_app)
print(f"Codici nell'app: {len(nell_app)}; in guida.yml: {len(nel_manuale)}")
for c in mancanti:
    print(f"MANCA in guida.yml: {c}")
for c in inutili:
    print(f"non usato dall'app: {c}")
sys.exit(1 if mancanti else 0)
