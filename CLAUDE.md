# CLAUDE.md

Manuale utente MkDocs Material di **RistoFacile** (cassa, palmare, monitor di cucina). Gemello di
`C:\RSA.CLAUDE\facile-docs`: stesse regole e strumenti, adattati alle app MAUI.

- Sorgenti documentati: `C:\RSA.NET\RistoFacile` (leggi il suo `CLAUDE.md`).
- Regole di scrittura: `tools/REGOLE-REDAZIONE.md`; template: `templates/documento-schermata.md`;
  skill: `.claude/skills/manuale-ristofacile`.
- Build: `.venv/Scripts/python.exe -m mkdocs build --strict` deve passare senza avvisi.
- Dopo ogni modifica alle schede: `tools/controlla-intestazioni.py`, `tools/appendice-messaggi.py`,
  `tools/domande-aperte.py`.
- `core.autocrlf=true`, file in UTF-8.
- Le immagini segnaposto sono elencate in `tools/schermate-da-catturare.txt`.
- Mai nomi di persone vere o dati di clienti nelle schermate (oscurare prima di pubblicare).

## Guida contestuale (F1 nelle app)

La cassa apre `<sito>/guida/<codice>/` nel pannello della guida. `guida.yml` (radice del repo) dice a quale
pagina e paragrafo porta ogni codice; l'hook `tools/hooks/guida.py` lo verifica a ogni build (pagina o
ancora mancante = build fallita) e scrive i rimandi in `site/guida/`. I codici li dichiara l'app in
`RistoCore/Services/Guida/CodiciGuida.cs`: un codice nuovo va lì e qui, e `tools/verifica-guida.py` li confronta.
**Rinominando una pagina o un titolo citato in `guida.yml`** si aggiorna la destinazione, mai il codice.
