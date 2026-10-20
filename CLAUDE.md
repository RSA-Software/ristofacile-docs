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
