# Domande aperte del manuale RistoFacile

Elenco generato da tutti i marcatori `DA VERIFICARE` presenti nelle schede.
Aggiornato al 2026-10-28 — **65 domande** su 33 pagine.

Ogni voce corrisponde a un commento HTML dentro la pagina indicata, alla riga
indicata: rispondendo alla domanda, la correzione va fatta nella pagina e il
marcatore va tolto. Per rigenerare questo elenco:

    .venv/Scripts/python.exe tools/domande-aperte.py

## Pubblicare il self order su internet

`docs/appendici/self-order-internet.md`

- [ ] riga 59: con il tunnel sullo stesso PC, oltre a 127.0.0.1 serve anche ::1?
- [ ] riga 75: da quale maschera di Facile si compilano le credenziali di Nexi, e l'indirizzo di produzione di Nexi XPay.

## Accesso operatore

`docs/cassa/accesso.md`

- [ ] riga 42: su un'installazione nuova, senza nessun operatore attivo, da questa schermata non si entra e non c'e' un pulsante per andare avanti. Come si crea il primo operatore (dal gestionale Facile? da un'altra cassa?)
- [ ] riga 107: vedi "Prima di cominciare", da qui non si raggiunge la schermata Operatori.

## Articoli

`docs/cassa/articoli.md`

- [ ] riga 100: la scritta dice di scrivere il prezzo dopo il primo salvataggio, ma il campo è già modificabile e il codice salva il prezzo anche al primo salvataggio. Quale delle due è voluta?
- [ ] riga 248: chi carica l'elenco degli allergeni e come?
- [ ] riga 266: confermare che un articolo modificato da due casse offline non dia avviso di conflitto (vince l'ultima sincronizzazione).

## Asporto e domicilio

`docs/cassa/asporto.md`

- [ ] riga 131: chi porta un ordine nello stato "Programmato"? Dalla cassa non c'e' nessun comando che lo imposti ne' che lo faccia avanzare.
- [ ] riga 180: dalla cassa si puo' correggere l'indirizzo di un ordine gia' creato? Non risulta un comando di modifica.
- [ ] riga 185: come si recupera la comanda rimasta aperta sul tavolo dell'asporto?

## Centri di produzione

`docs/cassa/centri-di-produzione.md`

- [ ] riga 71: dal codice, gli articoli che puntano a un centro spento escono comunque sulla stampante comande della postazione con intestazione CUCINA. È il comportamento voluto?

## Comanda

`docs/cassa/comanda.md`

- [ ] riga 260: in questa schermata il pulsante IMPORTO LIBERO non compare mai (la modalita' banco viene attivata solo da una pagina che la cassa non usa piu'). Va documentato qui o solo in Vendita al banco?

## Conto

`docs/cassa/conto.md`

- [ ] riga 95: come viene stampato sullo scontrino l'importo in "Credito" (voce "non riscosso" della stampante fiscale?) e a chi va intestato il credito.
- [ ] riga 386: in questa modalità, sul conto intero, il riquadro "Dividi il conto" e i campi Sconto/Abbuono restano visibili e utilizzabili su una comanda già chiusa: è voluto?

## Disponibilità

`docs/cassa/disponibilita.md`

- [ ] riga 63: nel codice della Comanda (cassa e palmare) il motivo non risulta mostrato; compare solo in questo elenco.
- [ ] riga 76: chi aggiorna la quantità «Venduta»? Nel codice di cassa e servizio non risulta aggiornata in automatico.
- [ ] riga 138: in Comanda la voce applicata è la prima trovata per l'articolo, senza guardare il giorno: una voce «solo per il giorno X» sembra restare valida anche nei giorni dopo, e con una voce «sempre» e una del giorno vince quella «sempre». Va verificato a schermo.

## Dividi il conto

`docs/cassa/dividi-conto.md`

- [ ] riga 124: confermare che le componenti di un piatto composto (mezza e mezza, menu fisso) seguano davvero il piatto principale quando questo viene assegnato a un conto.

## Fatture

`docs/cassa/fatture.md`

- [ ] riga 33: confermare che l'annullo/nota di credito si fa dal gestionale Facile e con quale maschera, per poterlo citare.
- [ ] riga 42: dove si configura l'invio delle email del servizio (server SMTP, mittente) e se è a carico dell'installatore.
- [ ] riga 98: su Windows si apre la finestra di stampa del sistema per scegliere la stampante? Comportamento su tablet non Windows.

## Impostazioni

`docs/cassa/impostazioni.md`

- [ ] riga 94: la ricerca del servizio per nome del sito e' stata tolta (commit 96b9f62 del repo RistoFacile); confermare che l'indirizzo si scrive sempre a mano e che non tornera'.
- [ ] riga 160: elenco dei campi proposti da "+ Campo" e delle condizioni di "quando?" per ciascun documento: valutare una scheda dedicata ai modelli di stampa.
- [ ] riga 254: a cosa serve in pratica "ID cassa" (con due casse sullo stesso terminale va dato un numero diverso a ciascuna?).
- [ ] riga 299: CashDro provata solo con una macchina finta; su una macchina vera vanno confermati annullo, ripresa dopo un riavvio e certificato (se cambia a ogni riavvio, l'impronta va lasciata vuota).
- [ ] riga 301: Cashlogy provata solo con un Connector finto; su una macchina vera vanno confermati il formato delle risposte e il riavvio del Connector.
- [ ] riga 323: tabella dei codici "Natura" (quale codice corrisponde a SPA, SRL, ecc.) e se Indirizzo/CAP/Citta' sono la sede legale o il domicilio fiscale.

## Mappa della sala

`docs/cassa/mappa-sala.md`

- [ ] riga 183: la finestra dice "Nessuna riga: puoi comunque separare solo i coperti.", ma il servizio risponde "nessuna riga da separare" se non si sceglie almeno una riga. Quale dei due comportamenti e' quello voluto?

## Menu online

`docs/cassa/menu-online.md`

- [ ] riga 73: il campo Token si puo' modificare ma "Salva indirizzo" salva solo indirizzo e nome del sito; dopo il salvataggio il campo torna al token del servizio. Confermare se il token va solo letto (allora andrebbe reso non modificabile) o se deve potersi scrivere da qui.
- [ ] riga 88: ogni quanto il servizio del locale manda il menu aggiornato (piatti, prezzi, foto) al servizio su Internet, e se serve fare qualcosa dopo aver cambiato il menu.
- [ ] riga 111: quale permesso serve per modificare lo stile del menu online e dove si assegna.
- [ ] riga 157: dopo quanto tempo il nuovo aspetto si vede sul telefono dei clienti.

## Menu

`docs/cassa/menu.md`

- [ ] riga 88: nel codice di cassa e servizio questi due indicatori sono solo salvati, non tolgono coperto o servizio dal conto.
- [ ] riga 196: dove si impostano giorni, orari e minimo di persone del menu (gestionale?). Il minimo di persone non risulta applicato in Comanda.

## Messaggi alla cucina

`docs/cassa/messaggi.md`

- [ ] riga 114: il titolo dice "oggi", ma il servizio restituisce i messaggi di oggi e di ieri. Va corretto il titolo o il servizio?

## Modificatori

`docs/cassa/modificatori.md`

- [ ] riga 57: nel codice della cassa la riga della variante stampata porta la Descrizione del modificatore, non la Sigla. Dove viene usata la sigla?

## Operatori

`docs/cassa/operatori.md`

- [ ] riga 70: il campo Badge viene solo salvato; nessuna schermata dell'app lo legge (non si entra col badge). A cosa serve?
- [ ] riga 129: eliminare un operatore che compare su comande e conti già chiusi è consentito? Cosa succede allo storico?

## Portate

`docs/cassa/portate.md`

- [ ] riga 72: l'attesa consigliata non risulta mostrata in Comanda, sul palmare o sul monitor di cucina; dove la vede chi dà il via?

## Prenotazioni

`docs/cassa/prenotazioni.md`

- [ ] riga 154: dalla cassa la durata non si vede ne' si modifica: in che caso puo' comparire questo messaggio?
- [ ] riga 173: e' voluto che una prenotazione confermata non si possa annullare (es. il cliente disdice)?
- [ ] riga 175: dalla cassa come si sposta una prenotazione in un'altra sala, e come si assegna un tavolo a una prenotazione "Senza tavolo" (in modifica il modulo non carica i tavoli di nessuna sala)?

## Regole di composizione

`docs/cassa/regole-di-composizione.md`

- [ ] riga 118: sulle altre casse e sui palmari già aperti la regola nuova compare solo al riavvio dell'app? (le regole stanno in memoria per tutta la sessione)

## Sale e tavoli

`docs/cassa/sale-e-tavoli.md`

- [ ] riga 37: dove si creano i listini (gestionale Facile?)
- [ ] riga 81: i posti massimi hanno effetto anche in vendita o nelle prenotazioni? Nel codice della cassa sono usati solo come limite dei tasti +.

## Statistiche

`docs/cassa/statistiche.md`

- [ ] riga 141: la schermata è accessibile a qualunque operatore? Nel codice non si vede un controllo dei permessi.

## Storico conti

`docs/cassa/storico-conti.md`

- [ ] riga 135: come compaiono qui le vendite al banco e gli ordini d'asporto (sala/tavolo mostrati).

## Tabelle di base

`docs/cassa/tabelle-di-base.md`

- [ ] riga 90: qui non c'è controllo sul massimo; un reparto oltre 9 funziona con la stampante fiscale?
- [ ] riga 124: i prezzi del nuovo listino si inseriscono dalla scheda articolo della cassa o solo dal gestionale?
- [ ] riga 155: cosa succede a una sala il cui listino viene eliminato (torna al listino di default?)
- [ ] riga 157: l'interruttore «Ristorante» ha effetto sulla cassa? Nel codice della cassa la vendita al tavolo parte dal Menu, non dalle categorie.

## Varianti

`docs/cassa/varianti-anagrafica.md`

- [ ] riga 104: nel codice della Comanda contano solo i prezzi «Tutti i listini»; un prezzo legato a un listino preciso non viene mai applicato. È un limite noto o un difetto?

## Vendita al banco

`docs/cassa/vendita-al-banco.md`

- [ ] riga 285: se la sala del tavolo dell'asporto ha una percentuale di servizio, il totale della finestra Incasso la aggiunge, mentre il TOTALE del carrello no: e' voluto al banco?
- [ ] riga 286: durante l'emissione dello scontrino (fino a qualche minuto con alcune stampanti) la finestra Incasso non mostra un indicatore di attesa: confermare cosa vede il cassiere a video.

## Licenza digitale

`docs/introduzione/licenza.md`

- [ ] riga 132: cosa fare se il vecchio dispositivo e' rotto o perso e non si puo' disattivare (lo libera l'assistenza RSA?).
- [ ] riga 179: il modulo del monitor di cucina e' compreso in tutte le edizioni o va acquistato a parte? La cassa lo chiede sempre all'attivazione.
- [ ] riga 203: dopo una scadenza, confermare che basta riavviare l'app con Internet (in demo il controllo giornaliero non gira) e che non serve riscrivere il seriale.

## Prima configurazione

`docs/introduzione/prima-configurazione.md`

- [ ] riga 109: al punto 4 si entra in Operatori senza essere ancora entrati come operatore (la cassa e' arrivata alle Impostazioni da sola perche' non era collegata). Confermare che e' il percorso previsto per creare il primo operatore; se la cassa viene riavviata prima di crearlo, la schermata di accesso mostra "Nessun operatore attivo..." senza un pulsante per proseguire.

## Monitor

`docs/kds/monitor.md`

- [ ] riga 193: c'è un modo per recuperare un piatto toccato per errore in PRONTO (consegnato) e quindi sparito?

## Accesso

`docs/palmare/accesso.md`

- [ ] riga 109: con il messaggio "Nessun operatore attivo" non compaiono ne' RIPROVA ne' IMPOSTAZIONI BACKEND: come si ricarica l'elenco dopo aver creato l'operatore (riavviare l'app?). Il messaggio indica "Impostazioni - Operatori", ma sulla cassa Operatori e' una voce del menu, non delle Impostazioni.

## Conto

`docs/palmare/conto.md`

- [ ] riga 120: «Credito» è il «non riscosso» (importo lasciato a credito del cliente)? Come va spiegato all'utente?
- [ ] riga 241: sul palmare non c'è una riga di stato nella schermata del conto: i messaggi informativi del modello (es. "Carta autorizzata (STAN ...)", "Fattura n. ... di € ...", "La carta e' GIA' stata addebitata ...: premi ...") non compaiono. È voluto?

## Palmare

`docs/palmare/index.md`

- [ ] riga 21: confermare che il palmare occupi un "posto Mobile" della licenza e come va detto all'utente.

## Sala

`docs/palmare/sala.md`

- [ ] riga 88: lo stato "Prenotato" di un tavolo (tessera tutta azzurra) da chi viene impostato? Dal codice la prenotazione in arrivo si vede solo con l'ora e la banda azzurra a destra.
- [ ] riga 182: come si scioglie un'unione dal palmare (riportare libero un tavolo "Unito a")? Dal codice sembra possibile con Separa dal tavolo principale verso il tavolo unito, ma va provato.
