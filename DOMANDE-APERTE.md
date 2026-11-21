# Domande aperte del manuale RistoFacile

Elenco generato da tutti i marcatori `DA VERIFICARE` presenti nelle schede.
Aggiornato al 2026-11-21 — **18 domande** su 8 pagine.

Ogni voce corrisponde a un commento HTML dentro la pagina indicata, alla riga
indicata: rispondendo alla domanda, la correzione va fatta nella pagina e il
marcatore va tolto. Per rigenerare questo elenco:

    .venv/Scripts/python.exe tools/domande-aperte.py

## Pubblicare il self order su internet

`docs/appendici/self-order-internet.md`

- [ ] riga 74: in quale sezione del back-office di Nexi XPay (e del suo ambiente di prova) si crea la chiave API: «Impostazioni ▸ Chiavi API» non è stato controllato sul portale.
- [ ] riga 75: in quale sezione del portale di SumUp si crea la chiave API e dove si legge il codice esercente.
- [ ] riga 76: in quale sezione del portale di Revolut Business (e del suo ambiente di prova) si legge la chiave segreta per i pagamenti online.
- [ ] riga 77: in quale sezione del portale di Dojo si crea la chiave segreta (sk_prod_ / sk_sandbox_).

## Dividi il conto

`docs/cassa/dividi-conto.md`

- [ ] riga 124: confermare che le componenti di un piatto composto (mezza e mezza, menu fisso) seguano davvero il piatto principale quando questo viene assegnato a un conto.

## Fatture

`docs/cassa/fatture.md`

- [ ] riga 33: confermare che l'annullo/nota di credito si fa dal gestionale Facile e con quale maschera, per poterlo citare.
- [ ] riga 98: comportamento della stampa sul tablet Android e su iPad (provata solo su Windows).

## Impostazioni

`docs/cassa/impostazioni.md`

- [ ] riga 216: elenco dei campi proposti da "+ Campo" e delle condizioni di "quando?" per ciascun documento: valutare una scheda dedicata ai modelli di stampa.
- [ ] riga 407: CashDro provata solo con una macchina finta; su una macchina vera vanno confermati annullo, ripresa dopo un riavvio e certificato (se cambia a ogni riavvio, l'impronta va lasciata vuota).
- [ ] riga 412: Cashlogy provata solo con un Connector finto; su una macchina vera vanno confermati il formato delle risposte e il riavvio del Connector.
- [ ] riga 445: tabella dei codici "Natura" (quale codice corrisponde a SPA, SRL, ecc.) e se Indirizzo/CAP/Citta' sono la sede legale o il domicilio fiscale.
- [ ] riga 483: che cosa sono "TLS" e "Passivo" nel collegamento con Digithera (connessione cifrata e modalita' passiva FTP?) e chi fornisce codice di abilitazione, server e porta.

## Self order

`docs/cassa/self-order.md`

- [ ] riga 70: schermata da rifare con la linguetta Pagamento (le linguette in alto ora sono cinque), e da catturare quella della linguetta Pagamento.
- [ ] riga 342: come arriva in cassa un ordine dell'asporto online (avviso, elenco Asporto, comanda in cucina) e come si chiude al ritiro: il pagamento con la carta fatto online compare gia' nel conto come per il self order?

## Tabelle di base

`docs/cassa/tabelle-di-base.md`

- [ ] riga 90: qui non c'è controllo sul massimo; un reparto oltre 9 funziona con la stampante fiscale?

## Licenza digitale

`docs/introduzione/licenza.md`

- [ ] riga 132: cosa fare se il vecchio dispositivo e' rotto o perso e non si puo' disattivare (lo libera l'assistenza RSA?).
- [ ] riga 179: il modulo del monitor di cucina e' compreso in tutte le edizioni o va acquistato a parte? La cassa lo chiede sempre all'attivazione.

## Pagamenti, per il personale

`docs/kiosk/pagamenti.md`

- [ ] riga 281: comportamento sul terminale ECR17 vero (pagato, rifiutato, risposta persa col cavo staccato, kiosk spento durante il PIN): la prova sul POS reale non e' ancora stata fatta; i casi di questa pagina sono stati provati con un POS finto e con casse automatiche finte.
