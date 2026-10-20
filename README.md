# Manuale RistoFacile — repository della documentazione

Manuale utente online di **RistoFacile** — la cassa (app RistoFacile), il palmare
dei camerieri (app RistoApp) e il monitor di cucina (app RistoKds) — scritto in
Markdown e pubblicato come sito statico con
[MkDocs Material](https://squidfunk.github.io/mkdocs-material/).

Una pagina per ogni schermata. Il progetto ricalca quello del manuale di Facile
(`C:\RSA.CLAUDE\facile-docs`): stessa struttura, stesse regole di scrittura.

---

## Contenuto del repository

```
mkdocs.yml                              configurazione del sito e struttura del menu
requirements.txt                        dipendenze Python
start.bat                               anteprima locale (installa i pacchetti se mancano)
templates/documento-schermata.md        template da copiare per ogni nuova scheda
tools/REGOLE-REDAZIONE.md               regole di scrittura (da leggere prima di tutto)
tools/appendice-messaggi.py             rigenera docs/appendici/messaggi.md dalle schede
tools/domande-aperte.py                 rigenera DOMANDE-APERTE.md
tools/controlla-intestazioni.py         controlla che il front matter sia YAML valido
tools/schermate-da-catturare.txt        immagini ancora segnaposto
DOMANDE-APERTE.md                       elenco generato dei marcatori DA VERIFICARE
docs/
  index.md                              home page
  introduzione/                         le tre app, prima configurazione, licenza, una serata, convenzioni
  cassa/                                una scheda per schermata della cassa (ordine del menu laterale)
  palmare/                              le schermate del palmare (ordine delle linguette)
  kds/                                  il monitor di cucina
  appendici/                            glossario, messaggi a video (generato)
  assets/img/<cassa|palmare|kds|introduzione>/   schermate
.claude/skills/manuale-ristofacile/     skill per Claude Code
.github/workflows/pubblica-manuale.yml  build e deploy su GitHub Pages
```

## Avvio in locale

Serve Python 3.9 o superiore. Il modo più semplice è `start.bat`; a mano:

```bash
pip install -r requirements.txt
mkdocs serve
```

Il manuale è su <http://127.0.0.1:8000> e si aggiorna da solo a ogni salvataggio.

Prima di ogni commit:

```bash
mkdocs build --strict
python tools/controlla-intestazioni.py
python tools/appendice-messaggi.py
python tools/domande-aperte.py
```

## Pubblicazione

Il repository non ha ancora un remoto. Per pubblicarlo come facile-docs:

1. creare su GitHub `RSA-Software/ristofacile-docs` e fare `git remote add origin …`;
2. **Settings ▸ Pages ▸ Source** → *GitHub Actions*;
3. controllare `site_url` e `repo_url` in `mkdocs.yml`;
4. `git push` su `main`: il workflow compila e pubblica.

## Schermate

- percorso `docs/assets/img/<app>/<slug>.png`, con lo slug della scheda;
- cassa: finestra 1600×1000 punti (2400×1500 pixel al 150%), tema chiaro, ridotta a 1600 di larghezza;
- palmare: telefono Android in verticale, ridotto a 540 di larghezza, nella pagina con `{ .telefono }`;
- **niente nomi di persone vere né dati di clienti**: gli operatori delle prove sono MARCO VERDI e
  GIULIA ROSSI; i nomi veri, la ditta e i token vanno oscurati prima di pubblicare;
- le immagini non ancora catturate sono segnaposto arancioni «Schermata da catturare»: l'elenco
  è in `tools/schermate-da-catturare.txt`.

## Come si scrive una scheda

Le regole sono in `tools/REGOLE-REDAZIONE.md` e nel template. In sintesi:

- si scrive per chi usa l'app (cassiere, cameriere, cuoco, titolare): mai nomi di classi o campi;
- le etichette si riportano **esatte** come a video, apostrofi compresi («Puo'», «e'»);
- le procedure sono elenchi numerati, un'azione per passo;
- i messaggi si riportano nella scheda della loro schermata; l'appendice si rigenera;
- dove il codice non basta, `<!-- DA VERIFICARE: … -->` invece di inventare.
