# Domande aperte del manuale RistoFacile

Elenco generato da tutti i marcatori `DA VERIFICARE` presenti nelle schede.
Aggiornato al 2026-11-24 — **4 domande** su 2 pagine.

Ogni voce corrisponde a un commento HTML dentro la pagina indicata, alla riga
indicata: rispondendo alla domanda, la correzione va fatta nella pagina e il
marcatore va tolto. Per rigenerare questo elenco:

    .venv/Scripts/python.exe tools/domande-aperte.py

## Impostazioni

`docs/cassa/impostazioni.md`

- [ ] riga 427: CashDro provata solo con una macchina finta; su una macchina vera vanno confermati annullo, ripresa dopo un riavvio e certificato (se cambia a ogni riavvio, l'impronta va lasciata vuota).
- [ ] riga 429: Cashmatic provata solo con il simulatore CTS_REST di Cashmatic; su una macchina vera vanno confermati ricarica (il simulatore non conta il denaro caricato) e certificato.
- [ ] riga 434: Cashlogy provata solo con un Connector finto; su una macchina vera vanno confermati il formato delle risposte e il riavvio del Connector.

## Pagamenti, per il personale

`docs/kiosk/pagamenti.md`

- [ ] riga 281: comportamento sul terminale ECR17 vero (pagato, rifiutato, risposta persa col cavo staccato, kiosk spento durante il PIN): la prova sul POS reale non e' ancora stata fatta; i casi di questa pagina sono stati provati con un POS finto e con casse automatiche finte.
