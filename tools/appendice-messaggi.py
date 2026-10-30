"""Rigenera l'appendice dei messaggi a video da tutte le schede del manuale.

Legge, in ogni scheda, la sezione «Controlli e messaggi» e ne prende le righe
delle tabelle con le colonne | Messaggio | Causa | Cosa fare |. I messaggi
identici (stesso testo, causa e rimedio) che compaiono su piu' schede
diventano una riga sola; la colonna «Dove» elenca le schede raggruppate per
app (Cassa, Palmare, Monitor di cucina, Kiosk, Guida introduttiva).

Uso, dalla radice del repository:

    .venv/Scripts/python.exe tools/appendice-messaggi.py
"""

import datetime
import pathlib
import re

ROOT = pathlib.Path(__file__).resolve().parent.parent
DOCS = ROOT / "docs"
OUT = DOCS / "appendici" / "messaggi.md"

# Cartella della scheda -> app, nell'ordine in cui compaiono nella colonna «Dove».
APP = {
    "cassa": "Cassa",
    "palmare": "Palmare",
    "kds": "Monitor di cucina",
    "kiosk": "Kiosk",
    "introduzione": "Guida introduttiva",
}
ORDINE_APP = list(APP.values())

# Oltre questo numero di schede il messaggio non e' di una schermata in
# particolare: elencarle tutte occuperebbe piu' spazio del messaggio.
MOLTE = 6

INTESTAZIONE = "| Messaggio | Causa | Cosa fare |"


def sezione_messaggi(testo: str) -> str:
    """La sezione «Controlli e messaggi» della scheda, vuota se non c'e'."""
    m = re.search(r"^## Controlli e messaggi\s*$(.*?)(?=^## |\Z)", testo, re.M | re.S)
    return m.group(1) if m else ""


def normalizza(riga: str) -> str:
    return riga.strip().strip("|").replace(" ", "").lower()


def righe_tabella(sezione: str):
    """Le righe delle sole tabelle con le tre colonne attese."""
    dentro = False
    for riga in sezione.splitlines():
        r = riga.strip()
        if r.startswith("|"):
            if normalizza(r) == normalizza(INTESTAZIONE):
                dentro = True
                continue
            if set(r) <= set("|-: "):
                continue
            if dentro:
                # Le barre protette (\|) non separano le celle.
                celle = [c.strip().replace("\x00", "\\|")
                         for c in r.replace("\\|", "\x00").strip("|").split("|")]
                if len(celle) == 3:
                    yield tuple(celle)
                else:
                    print(f"  ! riga con {len(celle)} celle ignorata: {r[:80]}")
        else:
            if r == "":
                continue
            dentro = False


def chiave_ordine(messaggio: str) -> str:
    return re.sub(r"[^0-9a-zà-ù]", "", messaggio.lower())


def titolo_scheda(testo: str, f: pathlib.Path) -> str:
    tit = re.search(r"^title:\s*(.+)$", testo, re.M)
    if tit:
        return tit.group(1).strip()
    h1 = re.search(r"^# (.+)$", testo, re.M)
    return h1.group(1).strip() if h1 else f.stem


def rilega(testo: str, scheda: pathlib.Path) -> str:
    """Riscrive i collegamenti della cella rispetto alla cartella appendici.

    Nelle schede i collegamenti sono relativi alla cartella della scheda:
    portati qui cosi' come sono, punterebbero a pagine inesistenti. Un
    collegamento a un'ancora della stessa scheda (#sezione) diventa un
    collegamento alla scheda con quell'ancora.
    """
    def sostituisci(m: re.Match) -> str:
        dest = m.group(2)
        if dest.startswith(("http://", "https://", "mailto:")):
            return m.group(0)
        ancora = ""
        if "#" in dest:
            dest, ancora = dest.split("#", 1)
            ancora = "#" + ancora
        assoluto = (scheda.parent / dest).resolve() if dest else scheda.resolve()
        try:
            rel = assoluto.relative_to(DOCS.resolve())
        except ValueError:
            return m.group(0)
        return f"[{m.group(1)}](../{rel.as_posix()}{ancora})"

    return re.sub(r"\[([^\]]*)\]\(([^)]+)\)", sostituisci, testo)


def colonna_dove(schede: list[tuple[str, str, str]]) -> str:
    """Le schede raggruppate per app: «Cassa: [Comanda](…), [Conto](…) · Palmare: …»."""
    if len(schede) > MOLTE:
        return f"Molte schermate ({len(schede)})"
    gruppi = []
    for app in ORDINE_APP:
        link = sorted((t, p) for a, t, p in schede if a == app)
        if link:
            gruppi.append(f"{app}: " + ", ".join(f"[{t}]({p})" for t, p in link))
    return " · ".join(gruppi)


def main() -> None:
    # (messaggio, causa, cosa fare) -> schede (app, titolo, percorso) in cui compare
    voci: dict[tuple[str, str, str], list[tuple[str, str, str]]] = {}

    for f in sorted(DOCS.rglob("*.md")):
        cartella = f.relative_to(DOCS).parts[0]
        if cartella not in APP:
            continue
        testo = f.read_text(encoding="utf-8")
        sez = sezione_messaggi(testo)
        if not sez:
            continue
        scheda = (APP[cartella], titolo_scheda(testo, f), "../" + f.relative_to(DOCS).as_posix())
        for voce in righe_tabella(sez):
            # I commenti (es. DA VERIFICARE) restano nella scheda: qui sarebbero
            # doppioni nell'elenco delle domande aperte.
            voce = tuple(rilega(re.sub(r"\s*<!--.*?-->", "", c).strip(), f) for c in voce)
            voci.setdefault(voce, [])
            if scheda not in voci[voce]:
                voci[voce].append(scheda)

    def ordine(kv):
        (messaggio, causa, _), schede = kv
        prima = min((ORDINE_APP.index(a), t) for a, t, _ in schede)
        return (chiave_ordine(messaggio), prima, causa)

    righe = [
        f"| {messaggio} | {colonna_dove(schede)} | {causa} | {azione} |"
        for (messaggio, causa, azione), schede in sorted(voci.items(), key=ordine)
    ]

    testa = (
        "---\n"
        "title: Messaggi a video\n"
        "description: Elenco alfabetico dei messaggi di cassa, palmare, monitor di "
        "cucina e kiosk, con la schermata che li mostra, la causa e cosa fare.\n"
        "---\n\n"
        "# Messaggi a video\n\n"
        "Tutti i messaggi documentati nelle schede, in un elenco solo. Cerca il\n"
        "testo comparso a video con il campo di ricerca in alto.\n\n"
        f"Aggiornato al {datetime.date.today().isoformat()} — **{len(righe)} messaggi**.\n\n"
        "!!! note \"Come leggere la colonna «Dove»\"\n\n"
        "    Porta alla scheda della schermata che mostra il messaggio, raggruppando\n"
        "    le schede per app: **Cassa**, **Palmare**, **Monitor di cucina**,\n"
        "    **Kiosk** e **Guida introduttiva**. Lo stesso messaggio può comparire sia sulla\n"
        "    cassa sia sul palmare: in quel caso la colonna li elenca tutti e due.\n\n"
        "    L'elenco è **generato dalle schede**: ogni messaggio è spiegato anche\n"
        "    in fondo alla pagina della sua schermata, insieme agli altri che si\n"
        "    incontrano nello stesso momento.\n\n"
        "<!-- File generato da tools/appendice-messaggi.py: non modificarlo a mano. -->\n\n"
        "| Messaggio | Dove | Causa | Cosa fare |\n"
        "|---|---|---|---|\n"
    )
    OUT.write_text(testa + "\n".join(righe) + "\n", encoding="utf-8", newline="\n")
    print(f"{len(righe)} messaggi -> {OUT.relative_to(ROOT).as_posix()}")


if __name__ == "__main__":
    main()
