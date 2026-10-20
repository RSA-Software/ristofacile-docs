"""Raccoglie i marcatori DA VERIFICARE delle schede in DOMANDE-APERTE.md.

Per ogni pagina elenca le domande con il numero di riga del marcatore, cosi'
la correzione si ritrova subito nella scheda.

Uso, dalla radice del repository:

    .venv/Scripts/python.exe tools/domande-aperte.py
"""

import datetime
import pathlib
import re

ROOT = pathlib.Path(__file__).resolve().parent.parent
DOCS = ROOT / "docs"
OUT = ROOT / "DOMANDE-APERTE.md"

MARCATORE = re.compile(r"<!--\s*DA VERIFICARE:\s*(.*?)\s*-->", re.S)


def titolo_scheda(testo: str, f: pathlib.Path) -> str:
    tit = re.search(r"^title:\s*(.+)$", testo, re.M)
    if tit:
        return tit.group(1).strip()
    h1 = re.search(r"^# (.+)$", testo, re.M)
    return h1.group(1).strip() if h1 else f.stem


def main() -> None:
    righe: list[str] = []
    totale = 0
    pagine = 0

    for f in sorted(DOCS.rglob("*.md")):
        testo = f.read_text(encoding="utf-8")
        trovati = list(MARCATORE.finditer(testo))
        if not trovati:
            continue
        pagine += 1
        percorso = f.relative_to(ROOT).as_posix()
        righe.append(f"## {titolo_scheda(testo, f)}\n")
        righe.append(f"`{percorso}`\n")
        for m in trovati:
            riga = testo.count("\n", 0, m.start()) + 1
            righe.append(f"- [ ] riga {riga}: " + " ".join(m.group(1).split()))
            totale += 1
        righe.append("")

    testa = (
        "# Domande aperte del manuale RistoFacile\n\n"
        "Elenco generato da tutti i marcatori `DA VERIFICARE` presenti nelle schede.\n"
        f"Aggiornato al {datetime.date.today().isoformat()} — "
        f"**{totale} domande** su {pagine} pagine.\n\n"
        "Ogni voce corrisponde a un commento HTML dentro la pagina indicata, alla riga\n"
        "indicata: rispondendo alla domanda, la correzione va fatta nella pagina e il\n"
        "marcatore va tolto. Per rigenerare questo elenco:\n\n"
        "    .venv/Scripts/python.exe tools/domande-aperte.py\n\n"
    )
    OUT.write_text(testa + "\n".join(righe), encoding="utf-8", newline="\n")
    print(f"{totale} domande da {pagine} pagine -> {OUT.relative_to(ROOT).as_posix()}")


if __name__ == "__main__":
    main()
