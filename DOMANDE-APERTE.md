# Domande aperte del manuale RistoFacile

Elenco generato da tutti i marcatori `DA VERIFICARE` presenti nelle schede.
Aggiornato al 2026-11-20 — **28 domande** su 16 pagine.

Ogni voce corrisponde a un commento HTML dentro la pagina indicata, alla riga
indicata: rispondendo alla domanda, la correzione va fatta nella pagina e il
marcatore va tolto. Per rigenerare questo elenco:

    .venv/Scripts/python.exe tools/domande-aperte.py

## Pubblicare il self order su internet

`docs/appendici/self-order-internet.md`

- [ ] riga 75: da quale maschera di Facile si compilano le credenziali di Nexi, e l'indirizzo di produzione di Nexi XPay.

## Centri di produzione

`docs/cassa/centri-di-produzione.md`

- [ ] riga 71: dal codice, gli articoli che puntano a un centro spento escono comunque sulla stampante comande della postazione con intestazione CUCINA. È il comportamento voluto?

## Conto

`docs/cassa/conto.md`

- [ ] riga 511: in questa modalità, sul conto intero, il riquadro "Dividi il conto" e i campi Sconto/Abbuono restano visibili e utilizzabili su una comanda già chiusa: è voluto?

## Dividi il conto

`docs/cassa/dividi-conto.md`

- [ ] riga 124: confermare che le componenti di un piatto composto (mezza e mezza, menu fisso) seguano davvero il piatto principale quando questo viene assegnato a un conto.

## Fatture

`docs/cassa/fatture.md`

- [ ] riga 33: confermare che l'annullo/nota di credito si fa dal gestionale Facile e con quale maschera, per poterlo citare.
- [ ] riga 98: comportamento della stampa sul tablet Android e su iPad (provata solo su Windows).

## Impostazioni

`docs/cassa/impostazioni.md`

- [ ] riga 117: la ricerca del servizio per nome del sito e' stata tolta (commit 96b9f62 del repo RistoFacile); confermare che l'indirizzo si scrive sempre a mano e che non tornera'.
- [ ] riga 216: elenco dei campi proposti da "+ Campo" e delle condizioni di "quando?" per ciascun documento: valutare una scheda dedicata ai modelli di stampa.
- [ ] riga 364: a cosa serve in pratica "ID cassa" (con due casse sullo stesso terminale va dato un numero diverso a ciascuna?).
- [ ] riga 409: CashDro provata solo con una macchina finta; su una macchina vera vanno confermati annullo, ripresa dopo un riavvio e certificato (se cambia a ogni riavvio, l'impronta va lasciata vuota).
- [ ] riga 414: Cashlogy provata solo con un Connector finto; su una macchina vera vanno confermati il formato delle risposte e il riavvio del Connector.
- [ ] riga 448: tabella dei codici "Natura" (quale codice corrisponde a SPA, SRL, ecc.) e se Indirizzo/CAP/Citta' sono la sede legale o il domicilio fiscale.
- [ ] riga 486: che cosa sono "TLS" e "Passivo" nel collegamento con Digithera (connessione cifrata e modalita' passiva FTP?) e chi fornisce codice di abilitazione, server e porta.
- [ ] riga 626: l'atteso somma i contanti incassati da tutto il locale; in un locale con piu' casse, ognuna col suo cassetto, si contano tutti i cassetti insieme e si scrive la somma in "Contanti contati"?

## Mappa della sala

`docs/cassa/mappa-sala.md`

- [ ] riga 232: la finestra dice "Nessuna riga: puoi comunque separare solo i coperti.", ma il servizio risponde "nessuna riga da separare" se non si sceglie almeno una riga. Quale dei due comportamenti e' quello voluto?

## Messaggi alla cucina

`docs/cassa/messaggi.md`

- [ ] riga 114: il titolo dice "oggi", ma il servizio restituisce i messaggi di oggi e di ieri. Va corretto il titolo o il servizio?

## Prenotazioni

`docs/cassa/prenotazioni.md`

- [ ] riga 173: e' voluto che una prenotazione confermata non si possa annullare (es. il cliente disdice)?

## Self order

`docs/cassa/self-order.md`

- [ ] riga 256: come arriva in cassa un ordine dell'asporto online (avviso, elenco Asporto, comanda in cucina) e come si chiude al ritiro: il pagamento con la carta fatto online compare gia' nel conto come per il self order?
- [ ] riga 257: il tavolo dell'asporto si sceglie per ogni cassa, ma l'asporto online e' unico per l'impianto: quale tavolo vale se due casse ne hanno scelto uno diverso? (al Salva vince quello della cassa che salva)

## Tabelle di base

`docs/cassa/tabelle-di-base.md`

- [ ] riga 90: qui non c'è controllo sul massimo; un reparto oltre 9 funziona con la stampante fiscale?
- [ ] riga 156: cosa succede a una sala il cui listino viene eliminato (torna al listino di default?)

## Vendita al banco

`docs/cassa/vendita-al-banco.md`

- [ ] riga 285: se la sala del tavolo dell'asporto ha una percentuale di servizio, il totale della finestra Incasso la aggiunge, mentre il TOTALE del carrello no: e' voluto al banco?
- [ ] riga 286: durante l'emissione dello scontrino (fino a qualche minuto con alcune stampanti) la finestra Incasso non mostra un indicatore di attesa: confermare cosa vede il cassiere a video.

## Licenza digitale

`docs/introduzione/licenza.md`

- [ ] riga 132: cosa fare se il vecchio dispositivo e' rotto o perso e non si puo' disattivare (lo libera l'assistenza RSA?).
- [ ] riga 179: il modulo del monitor di cucina e' compreso in tutte le edizioni o va acquistato a parte? La cassa lo chiede sempre all'attivazione.

## Monitor

`docs/kds/monitor.md`

- [ ] riga 336: c'è un modo per recuperare un piatto toccato per errore in PRONTO (consegnato) e quindi sparito?

## Pagamenti, per il personale

`docs/kiosk/pagamenti.md`

- [ ] riga 281: comportamento sul terminale ECR17 vero (pagato, rifiutato, risposta persa col cavo staccato, kiosk spento durante il PIN): la prova sul POS reale non e' ancora stata fatta; i casi di questa pagina sono stati provati con un POS finto e con casse automatiche finte.

## Conto

`docs/palmare/conto.md`

- [ ] riga 241: sul palmare non c'è una riga di stato nella schermata del conto: i messaggi informativi del modello (es. "Carta autorizzata (STAN ...)", "Fattura n. ... di € ...", "La carta e' GIA' stata addebitata ...: premi ...") non compaiono. È voluto?
