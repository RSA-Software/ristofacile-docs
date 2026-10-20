---
title: Conto
description: Incassare un tavolo, un ordine d'asporto o una parte di conto, ed emettere lo scontrino, la fattura o l'addebito in camera.
app: Cassa
percorso: Menu ▸ Vendita ▸ Mappa della sala ▸ tocco su un tavolo ▸ CONTO
pagina: ContoPage
---

# Conto

Il Conto è la schermata in cui si incassa: mostra le voci da pagare e il totale, raccoglie
gli importi per metodo di pagamento e, con **INCASSA E STAMPA**, chiude il conto ed emette il
documento. La usa il cassiere, o chiunque in sala sia abilitato a incassare.

!!! info "In sintesi"

    - **Dove si trova:** dalla [Comanda](comanda.md), pulsante **CONTO** (oppure **Vai al conto** dal preconto); dalla [divisione del conto](dividi-conto.md); dallo [Storico conti](storico-conti.md) per documentare un conto già chiuso
    - **Chi la usa:** cassiere
    - **Disponibile anche su:** [Palmare](../palmare/conto.md)

---

## A cosa serve

A fine pasto il cliente chiede il conto: dalla comanda del tavolo tocchi **CONTO** e arrivi qui.
Scrivi quanto paga in contanti, con carta o con altri metodi (oppure tocchi il nome del metodo e
la cassa ci mette l'importo esatto), scegli se emettere lo scontrino o la fattura e tocchi
**INCASSA E STAMPA**. Lo scontrino lo emette il servizio sulla stampante fiscale dell'impianto;
a chiusura riuscita il tavolo si libera e torni alla mappa della sala.

Se il tavolo paga separatamente, da qui si apre la [divisione del conto](dividi-conto.md), che
ripartisce le voci su più conti e li fa incassare uno per uno, ciascuno con il suo documento.

## Prima di cominciare

- Una **stampante fiscale** configurata sull'impianto ([Impostazioni](impostazioni.md) ▸ **Stampante fiscale**): senza, lo scontrino non si emette e il conto resta aperto (vedi [Controlli e messaggi](#controlli-e-messaggi)).
- Per usare **Sconto** e **Abbuono**, l'operatore deve avere **Puo' applicare sconti** e uno **Sconto massimo** in [Operatori](operatori.md).
- Per **CHIUDI SENZA DOCUMENTO** e per l'addebito in camera, l'operatore deve avere **Puo' chiudere il conto** in [Operatori](operatori.md).
- Se la sala del tavolo prevede una percentuale di servizio ([Sale e tavoli](sale-e-tavoli.md)), in [Articoli](articoli.md) deve esistere l'articolo **SERVIZIO** con un'aliquota IVA che abbia un reparto della cassa.
- Facoltativi, in [Impostazioni](impostazioni.md): **Pagamento con carta** (il terminale POS di questa postazione), **Cassa automatica**, **Stampante preconto** (ricevuta del POS, copia di cortesia della fattura, tagliando dell'addebito in camera), **Hotel** (addebito in camera).

## La schermata

![Conto](../assets/img/cassa/conto.png)

La schermata ha due colonne.

**A sinistra, il conto.** In alto il titolo dice quale conto stai incassando: **Conto** per il
tavolo intero, **Conto 2** (o un altro numero) per una parte del conto, **Resto del conto** per
quello che nessuno ha preso nella divisione. Sotto, l'elenco delle voci: quantità, descrizione e
importo. Il coperto compare come una voce («Coperto», con il numero dei coperti come quantità).
Una voce offerta ha importo € 0,00 e sotto la scritta **OMAGGIO -** seguita dal valore offerto.
Seguono sconto e abbuono, l'eventuale servizio, il **Totale** e, da due coperti in su, la riga
**Parti uguali** con la quota a testa. In fondo, il riquadro **Dividi il conto**.

**A destra, il pagamento.** I cinque metodi di pagamento con il loro importo, il riepilogo
(**Totale**, **Pagato**, **Residuo** o **Resto**), la scelta del documento e i pulsanti finali.

Mentre la cassa lavora (caricamento, emissione, chiusura) la schermata si scurisce e compare una
rotella al centro: aspetta che sparisca prima di toccare altro.

## Campi e indicatori

### Colonna del conto

| Elemento | Descrizione |
|---|---|
| **Conto** / **Conto N** / **Resto del conto** | Quale conto si sta incassando: il tavolo intero, uno dei conti della divisione, oppure il resto non assegnato. |
| Elenco delle voci | Quantità, descrizione, importo. Sono le voci **ancora da pagare**: dopo un pagamento parziale compaiono solo le quantità residue. Gli articoli a peso mostrano la quantità in kg. |
| *Parte di questo tavolo e' gia' stata incassata: qui c'e' solo quello che resta.* | Compare quando una parte del tavolo è già stata pagata (per esempio uno dei conti della divisione). |
| **Subtotale** | Somma delle voci, prima di sconto e servizio. |
| **Sconto** | Percentuale di sconto sul conto. Sotto, la riga **Massimo N% per** *operatore* dice il tetto concesso a chi è in turno, oppure che l'operatore non è abilitato agli sconti. |
| **Abbuono** | *Sconto in euro, oltre alla percentuale*: l'arrotondamento a mano («facciamo 50»). |
| **Sconto applicato** | Lo sconto complessivo (percentuale più abbuono), in euro. Compare solo se c'è uno sconto. |
| Avviso in rosso sotto lo sconto | Dice perché l'incasso è bloccato: operatore non abilitato, sconto massimo non impostato, sconto oltre il massimo (vedi [Controlli e messaggi](#controlli-e-messaggi)). |
| **Servizio N%** | Il servizio della sala, calcolato sul conto già scontato. Compare solo se la sala ha una percentuale di servizio. |
| **Totale** | Quanto si incassa su questo conto. |
| **Parti uguali** | *€ X a testa (N coperti)*: solo un numero da leggere, la quota per persona arrotondata per eccesso. Non divide il conto. Compare sul conto intero, da due coperti in su. |
| **Dividi il conto** | *Assegna le voci a piu' conti e incassali separatamente*. Con **Dividi** apri la [divisione del conto](dividi-conto.md). Non compare quando stai già incassando una parte del conto. |

Sconto e abbuono valgono solo sul conto intero: incassando una parte del conto non compaiono.
Lo sconto si controlla sulla percentuale effettiva (percentuale più abbuono): non si aggira il
tetto con l'abbuono.

### Colonna del pagamento

| Elemento | Descrizione |
|---|---|
| **Pagamento** | *Tocca un metodo per incassare l'importo esatto*: toccando il **nome** di un metodo, la cassa aggiunge a quel metodo quanto manca per coprire il totale. |
| **Contanti** | Importo in contanti. Puoi scrivere la cifra ricevuta (es. 50,00 su un conto di 42,00): il resto viene calcolato. |
| **Carta** | Importo pagato con carta di credito. |
| **Bancomat** | Importo pagato con bancomat. |
| **Buoni pasto** | Importo pagato con buoni pasto. |
| **Credito** | Importo non riscosso: conta come pagamento ai fini della copertura del totale. <!-- DA VERIFICARE: come viene stampato sullo scontrino l'importo in "Credito" (voce "non riscosso" della stampante fiscale?) e a chi va intestato il credito. --> |
| **Totale** | Il totale del conto, ripetuto accanto ai pagamenti. |
| **Pagato** | Somma degli importi scritti nei cinque metodi. |
| **Residuo** | In rosso: quanto manca per coprire il totale. Finché c'è un residuo il conto non si incassa. |
| **Resto** | In verde: quanto rendere al cliente. |
| **Cassa automatica** | Spunta presente solo se su questa postazione è stata scelta una cassa automatica. È accesa all'apertura del conto; spegnila quando il cliente paga al banco a mano o la macchina è in rifornimento. Sotto, la nota dice cosa farà la macchina: **Contanti e carta**, **Solo contanti** oppure **Spenta**. |
| **Documento** | La scelta del documento: **Scontrino** (proposto all'apertura) o **Fattura**. Con l'hotel collegato compare anche **Camera** (e la scritta **Documento** sparisce per fare posto). |
| **Scegli il cliente** | Compare solo con **Fattura**: tocca per scegliere o aggiungere il cliente a cui intestarla. Una volta scelto mostra nome, partita IVA o codice fiscale, recapito e, se prevista, *copia a* indirizzo email. |
| Avviso in rosso sotto il cliente | Con **Fattura**, il primo dato che manca al cliente per la fattura elettronica (es. *Manca: CAP di 5 cifre.*). |
| **Scegli la camera** | Compare solo con **Camera**: tocca per scegliere l'ospite in casa a cui addebitare il conto. |

Una volta che la carta è passata, la cassa automatica ha incassato o lo scontrino è stato emesso,
gli importi non si possono più modificare: il conto registrerà esattamente quello che è avvenuto.

## Pulsanti e comandi

| Comando | Effetto |
|---|---|
| **Dividi** | Apre la [divisione del conto](dividi-conto.md). |
| Nome di un metodo (**Contanti**, **Carta**, **Bancomat**, **Buoni pasto**, **Credito**) | Aggiunge a quel metodo l'importo che manca per coprire il totale. |
| **Scontrino** | Il conto si chiude con lo scontrino, emesso sulla stampante fiscale dell'impianto. |
| **Fattura** | Il conto si chiude con una fattura; se il cliente non è ancora scelto si apre subito il pannello **Cliente della fattura**. |
| **Camera** | Il conto si addebita alla camera di un ospite dell'hotel: niente scontrino, il documento lo emette l'hotel al check-out. Azzera gli importi dei metodi di pagamento e apre la scelta della camera. |
| **INCASSA E STAMPA** | Con **Scontrino**: incassa (carta e cassa automatica, se usate) ed emette lo scontrino. Il testo del pulsante cambia con la situazione: **INCASSA ED EMETTI FATTURA** con la fattura, **ADDEBITA IN CAMERA** con la camera, **STAMPA SCONTRINO** o **EMETTI FATTURA** quando la carta è già stata addebitata. |
| **Annulla** | Torna alla schermata precedente senza incassare. Gli importi scritti non vengono salvati. |
| **CHIUDI SENZA DOCUMENTO** | Chiude il conto e libera il tavolo **senza emettere nessun documento fiscale**, dopo una conferma. Riservato agli operatori con **Puo' chiudere il conto**. Non compare con **Fattura** o **Camera**, né quando stai documentando un conto dallo Storico. |

### Pannello «Cliente della fattura»

![Cliente della fattura](../assets/img/cassa/conto-cliente.png)

Si apre toccando **Fattura** (se il cliente non è ancora scelto) o il campo del cliente. Ha due
passi.

**Ricerca.** Scrivi nel campo *Partita IVA, codice fiscale o ragione sociale* (almeno due
caratteri) e tocca la lente. Tocca un cliente nell'elenco: se ha tutti i dati per la fattura
elettronica viene usato subito, altrimenti si apre la sua scheda per completarla. Se non c'è,
tocca **Cliente nuovo**: la scheda si apre già compilata con quello che avevi cercato (partita
IVA, codice fiscale o ragione sociale).

**Scheda.** *Questi sono i dati che la fattura elettronica pretende.*

| Elemento | Descrizione |
|---|---|
| **Persona** / **Azienda** | Persona fisica o persona giuridica. |
| **Sesso** **M** / **F** | Solo per la persona. |
| **Ditta individuale** | Solo per la persona: se accesa basta la ragione sociale, senza nome. |
| **Cognome** (persona) o **Ragione sociale** | Obbligatorio. |
| **Nome** | Obbligatorio per la persona che non è ditta individuale. |
| **Partita IVA** | Obbligatoria per l'azienda. |
| **Codice fiscale** | Obbligatorio per la persona italiana; 11 o 16 caratteri. |
| **Indirizzo**, **CAP**, **Citta'**, **Prov.**, **Naz.** | Indirizzo obbligatorio; CAP di 5 cifre; provincia di 2 lettere per l'Italia; nazione di 2 lettere. |
| **Invia copia per email** | Se accesa, la fattura in PDF viene spedita all'indirizzo **Email**. Per accenderla serve un indirizzo. |
| **Invia all'Agenzia** | Trasmette la fattura elettronica all'Agenzia delle Entrate. È **spenta a ogni fattura**: va accesa di proposito, ogni volta. |
| **Cod. destinatario** / **oppure PEC** | Uno dei due è obbligatorio; il codice destinatario è di 7 caratteri. |
| **Email**, **Telefono** | Recapiti. |
| **Cerca un altro** | Torna alla ricerca per cambiare cliente. |
| **Usa questo cliente** | Conferma il cliente per la fattura. Se manca qualcosa, la cassa dice cosa. |

Il cliente nuovo, o i dati corretti, vengono salvati nell'archivio insieme alla fattura: se
chiudi il pannello senza emettere, non resta nessun cliente a metà. La X in alto o un tocco
fuori dal pannello lo chiudono.

### Pannello «Addebito in camera»

*Gli ospiti in casa oggi: tocca quello a cui va il conto.* Scrivi nel campo *Numero di camera o
nome dell'ospite* per filtrare l'elenco e tocca l'ospite. Se chiudi il pannello senza scegliere
nessuno, il documento torna su **Scontrino**.

## Come si fa

### Incassare un tavolo con lo scontrino

1. Dalla [Comanda](comanda.md) del tavolo tocca **CONTO**.
2. Controlla voci e **Totale**.
3. Scrivi gli importi nei metodi di pagamento, oppure tocca il nome del metodo (es. **Contanti**) per mettere l'importo esatto.
4. Se il cliente paga in contanti con una banconota più grande, scrivi la cifra ricevuta: la riga **Resto** in verde dice quanto rendere.
5. Controlla che **Residuo** non compaia e che sia acceso **Scontrino**.
6. Tocca **INCASSA E STAMPA**. La schermata si scurisce mentre il servizio emette lo scontrino (con alcune stampanti può volerci qualche decina di secondi).
7. Lo scontrino esce dalla stampante fiscale e torni alla mappa della sala: il tavolo è libero.

### Pagare con la carta sul terminale POS

Se in [Impostazioni](impostazioni.md) ▸ **Pagamento con carta** è stato scelto un terminale per
questa postazione:

1. Scrivi l'importo in **Carta** o **Bancomat** (anche insieme ai contanti).
2. Tocca **INCASSA E STAMPA**.
3. Compare il riquadro *€ X sul terminale: fai passare la carta…* con una barra che si svuota e il tempo che resta (*Ancora N s*): la cassa aspetta il terminale fino a 75 secondi. Confronta l'importo con quello sul display del POS.
4. Il cliente paga sul terminale. Se la stampante preconto è configurata, esce la ricevuta del POS.
5. Subito dopo il servizio emette lo scontrino e il conto si chiude.

![Attesa del terminale POS](../assets/img/cassa/conto-pos.png)

Se su questa postazione non è stato scelto nessun terminale, la carta si batte a mano sul POS e
la cassa prosegue senza aspettare niente.

Se il pagamento con carta riesce ma lo scontrino non esce (stampante spenta, carta finita), il
conto resta aperto e la cassa ricorda che la carta è già stata addebitata, anche se esci dalla
schermata e ci torni: il pulsante diventa **STAMPA SCONTRINO** e non riaddebita la carta. Lo
ricorda solo **questa** postazione.

!!! warning "Carta già addebitata"
    Quando un messaggio dice che la carta è GIÀ stata addebitata, non farla ripassare: risolvi il
    problema della stampante e tocca di nuovo il pulsante (**STAMPA SCONTRINO**).

### Incassare con la cassa automatica

Se su questa postazione è stata scelta una cassa automatica (rendiresto), la spunta **Cassa
automatica** è accesa e:

1. Metti l'importo in **Contanti** (ed eventualmente in **Carta**/**Bancomat**, se la nota dice **Contanti e carta**).
2. Tocca **INCASSA E STAMPA**.
3. Compare il riquadro *€ X nella cassa automatica* con il contatore *Inserito € … — manca € …*. Il cliente inserisce le banconote e le monete nella macchina; la macchina eroga il resto.
4. A incasso completato il servizio emette lo scontrino e il conto si chiude.

![Cassa automatica in incasso](../assets/img/cassa/conto-cassa-automatica.png)

Mentre la macchina incassa, nel riquadro ci sono due pulsanti con effetti opposti:

| Comando | Effetto |
|---|---|
| **Annulla e restituisci** | La macchina restituisce tutto quello che il cliente ha inserito: **niente è incassato** e il conto resta aperto. |
| **Chiudi trattenendo** | La macchina tiene quello che è stato inserito: è un **incasso parziale**, non un annullo. L'importo trattenuto viene scritto in **Contanti** e il conto resta aperto per coprire il resto con un altro metodo, con **Credito** o dividendo il conto. |

Gli esiti possibili:

- **completato**: i soldi sono entrati, si prosegue con lo scontrino. Se la macchina non ha potuto dare tutto il resto, la cassa avvisa di consegnare a mano la differenza;
- **trattenuto** (incasso parziale): vedi **Chiudi trattenendo**;
- **annullato**: la macchina ha restituito i soldi, anche quando l'incasso è stato interrotto dal pannello della macchina stessa; il conto resta aperto;
- **rifiutato**: non è entrato niente; la cassa propone di incassare a mano (**Incasso a mano**, o **Carta a mano** per la carta) e proseguire con la chiusura;
- **incerto**: nessuno sa dove siano i soldi. Controlla la macchina e il giornale del servizio **prima** di ripetere l'incasso.

Se la macchina ha già incassato e poi lo scontrino non esce, rientrando nel conto la cassa non
richiede di nuovo i soldi. Anche questo vale solo per **questa** postazione.

### Emettere la fattura

1. Tocca **Fattura**. Si apre il pannello **Cliente della fattura**.
2. Cerca il cliente per partita IVA, codice fiscale o ragione sociale, oppure tocca **Cliente nuovo**.
3. Completa la scheda se serve e tocca **Usa questo cliente**.
4. Se vuoi trasmettere subito la fattura all'Agenzia delle Entrate, accendi **Invia all'Agenzia** nella scheda del cliente.
5. Scrivi gli importi dei pagamenti e tocca **INCASSA ED EMETTI FATTURA**.
6. Il servizio emette la fattura: la stampante fiscale non viene usata. Il conto si chiude e torni alla mappa della sala.
7. Compare la domanda *Fattura n. … emessa* con le scelte **Stampa la copia di cortesia** (sulla stampante preconto), **Apri la fattura** (il PDF a schermo) e **Niente**.

Se la stampante preconto non è configurata e il PDF si apre dentro l'app, la fattura si apre
subito senza domanda.

### Addebitare il conto in camera

Solo con l'hotel collegato ([Impostazioni](impostazioni.md) ▸ **Hotel**) e per gli operatori con
**Puo' chiudere il conto**.

1. Tocca **Camera**. Si apre l'elenco degli ospiti in casa.
2. Tocca l'ospite.
3. Tocca **ADDEBITA IN CAMERA** e conferma con **Addebita**.
4. L'importo va sul conto della camera; sulla stampante preconto esce il tagliando da far firmare all'ospite. Torni alla mappa della sala.

### Chiudere un conto senza documento

È l'unico modo di liberare il tavolo quando la stampante fiscale non c'è o è guasta.

1. Lascia acceso **Scontrino** (con **Fattura** il pulsante non compare).
2. Tocca **CHIUDI SENZA DOCUMENTO**.
3. Conferma con **Chiudi** il messaggio *Il tavolo verra' chiuso e liberato per € X SENZA emettere nessuno scontrino. Procedere?*
4. Il conto si chiude, il tavolo si libera e torni alla mappa della sala. Nessun documento esce.

In questo caso non serve che i pagamenti coprano il totale, e non vengono interpellati né il
terminale POS né la cassa automatica. La chiusura resta registrata come «senza documento» e lo
scontrino si può emettere più tardi dallo [Storico conti](storico-conti.md).

### Stampare il preconto prima di incassare

Il preconto non si stampa da questa schermata ma dalla [Comanda](comanda.md): **Preconto** mostra
l'anteprima (*documento non valido ai fini fiscali*), **Stampa** la manda alla stampante preconto
e **Vai al conto** porta qui. Il preconto non chiude e non incassa niente: segna soltanto il
tavolo come «preconto» sulla mappa della sala.

## Controlli e messaggi

| Messaggio | Causa | Cosa fare |
|---|---|---|
| *Nessuna voce da incassare su questo conto.* | Il conto non ha voci da pagare. | Torna alla comanda. Un tavolo a zero si chiude dalla comanda stessa, toccando **CONTO**: la cassa propone di chiuderlo senza documento. |
| *Mancano € X da ripartire fra i metodi di pagamento: il conto non si puo' chiudere finche' l'importo non e' coperto per intero.* | Gli importi scritti non coprono il totale. | Completa i pagamenti, o tocca il nome di un metodo per mettere l'importo esatto. |
| *… non e' abilitato ad applicare sconti.* | L'operatore in turno non ha **Puo' applicare sconti**. Il valore scritto viene tolto. | Fai applicare lo sconto a un operatore abilitato. |
| *… non ha uno sconto massimo impostato: va messo in Impostazioni -> Operatori.* | L'operatore è abilitato agli sconti ma con **Sconto massimo** a zero. | Imposta lo sconto massimo in [Operatori](operatori.md). |
| *Sconto N% oltre il massimo consentito a … (M%).* | Lo sconto complessivo (percentuale più abbuono) supera il tetto dell'operatore. | Riduci sconto o abbuono. |
| *Manca: …* | Con **Fattura**: al cliente manca un dato obbligatorio per la fattura elettronica. | Tocca il cliente e completa la scheda. |
| *Per la fattura serve ancora: …* | Hai toccato **Usa questo cliente** con dati mancanti. | Completa i campi elencati. |
| *Scrivi almeno due caratteri: partita IVA, codice fiscale o ragione sociale.* | Ricerca del cliente troppo corta. | Scrivi almeno due caratteri. |
| *Scrivi prima l'indirizzo email del cliente.* | Hai acceso **Invia copia per email** senza indirizzo. | Compila **Email**. |
| *Sul conto c'e' il servizio N%, ma in anagrafica manca l'articolo SERVIZIO con la sua aliquota IVA, o la sua aliquota non ha un reparto della cassa: va creato o sistemato prima di emettere il documento.* | La sala ha il servizio ma l'articolo SERVIZIO manca o è incompleto. | Crea o sistema l'articolo in [Articoli](articoli.md). |
| *Su questo impianto non c'e' una stampante fiscale configurata: per liberare il tavolo usa CHIUDI SENZA DOCUMENTO, e lo scontrino lo emetti piu' tardi da Storico conti.* | Il servizio non ha una stampante fiscale. Il conto resta aperto. | Configura la stampante fiscale, oppure chiudi senza documento e documenta più tardi dallo Storico. |
| *La stampante fiscale non ha risposto: … Premi di nuovo INCASSA E STAMPA: il servizio controlla se lo scontrino e' uscito e non lo ristampa.* | Comunicazione con la stampante interrotta: lo scontrino potrebbe essere uscito. Gli importi si bloccano. | Tocca di nuovo il pulsante: il servizio verifica sulla stampante e non emette due volte. |
| **Scontrino: esito incerto** — *… Guarda la stampante fiscale: lo scontrino di € X e' uscito?* | Il servizio non è riuscito a rileggere la stampante. | Guarda la carta: tocca **E' uscito** o **Non e' uscito**. |
| *… Il conto resta aperto.* | La stampante fiscale ha rifiutato l'emissione (il motivo è nella prima parte del messaggio, quello della stampante). Non è uscito niente. | Risolvi il problema (carta, coperchio, stampante spenta) e tocca di nuovo il pulsante. |
| *Questo conto e' in incasso da un'altra postazione, con uno scontrino in sospeso: l'incasso va finito da li'. Il conto resta aperto.* | Un'altra cassa sta incassando lo stesso tavolo. | Finisci l'incasso dall'altra postazione. |
| *Pagamento con carta non riuscito: … Il conto resta aperto: nessun documento e' stato emesso.* | Il terminale ha rifiutato la carta. | Riprova o cambia metodo. |
| *Nessuna risposta dal terminale: … IL PAGAMENTO POTREBBE ESSERE PASSATO LO STESSO. …* | Il terminale non ha risposto in tempo. | Controlla sul POS (o stampa l'ultima ricevuta) **prima** di riprovare. |
| *La carta e' stata addebitata ma la ricevuta del POS non e' stata stampata.* | Problema sulla stampante preconto. La carta è addebitata. | Non ripassare la carta; il conto prosegue. |
| **Cassa automatica** — *… Vuoi incassare i contanti a mano e proseguire con la chiusura?* | La macchina è occupata, non ha accettato l'incasso o non ha incassato niente. | **Incasso a mano** per proseguire incassando tu, **Annulla** per lasciare il conto aperto. |
| *La cassa automatica ha trattenuto € X: e' un incasso PARZIALE, non un annullo. …* | Hai toccato **Chiudi trattenendo**. | Copri la differenza con un altro metodo o dividi il conto. |
| *Incasso annullato: la cassa ha restituito € X al cliente. …* | Hai toccato **Annulla e restituisci**. | Il conto resta aperto. |
| *La cassa automatica non ha potuto erogare € X di resto: consegnali a mano al cliente.* | Monete o banconote insufficienti nella macchina. | Dai il resto a mano. |
| *Nessuna risposta dalla cassa automatica: … L'INCASSO POTREBBE ESSERE PARTITO LO STESSO. …* / *Non riesco piu' a seguire l'incasso sulla cassa automatica: … IL DENARO POTREBBE ESSERE DENTRO LA MACCHINA. …* | Comunicazione persa con la macchina. | Controlla la macchina (e il giornale del servizio) **prima** di ripetere l'incasso. |
| *La cassa automatica impostata su questa postazione non risulta piu' configurata sul servizio: …* | La macchina scelta in Impostazioni non esiste più sul servizio. | Sistema [Impostazioni](impostazioni.md) ▸ **Cassa automatica**. |
| *Lo scontrino di questo conto e' gia' stato emesso: la fattura va fatta dal gestionale.* | Hai scelto **Fattura** dopo che lo scontrino era già uscito. | Emetti la fattura dal gestionale. |
| *Questo conto si documenta con lo scontrino: la fattura va fatta dal gestionale.* | Stai documentando dallo Storico la parte di un conto diviso. | Usa **Scontrino**. |
| *… non e' abilitato a chiudere un conto senza documento fiscale.* | **CHIUDI SENZA DOCUMENTO** toccato da un operatore senza **Puo' chiudere il conto**. | Fai chiudere a un operatore abilitato. |
| *Stai emettendo una fattura: e' quello il documento del conto. Per chiudere senza documento torna su Scontrino.* | **CHIUDI SENZA DOCUMENTO** con **Fattura** scelta. | Torna su **Scontrino**. |
| *Lo scontrino di questo conto potrebbe essere uscito: premi INCASSA E STAMPA, il servizio controlla la stampante.* | **CHIUDI SENZA DOCUMENTO** dopo un esito incerto della stampante. | Tocca di nuovo il pulsante di incasso. |
| *Su questo conto e' gia' stato incassato qualcosa (carta, contanti o scontrino): non si puo' piu' addebitare in camera.* | **Camera** scelta dopo un incasso già avvenuto. | Completa l'incasso con lo scontrino. |
| *… non e' abilitato a chiudere un conto senza scontrino: l'addebito in camera lo fa chi ha "Puo' chiudere".* | Addebito in camera da un operatore non abilitato. | Fai addebitare a un operatore abilitato. |
| *Addebito registrato, ma la stampante del preconto non e' configurata: il tagliando da firmare non e' uscito.* | Manca la stampante preconto. | L'addebito è fatto; fai firmare a mano. |
| *Il conto era gia' stato chiuso da un'altra postazione: non e' stato addebitato niente in camera.* | Il conto era già chiuso altrove. | Nessuna azione. |
| *Impossibile leggere gli ospiti in casa dall'hotel.* | Il collegamento con l'hotel non risponde. | Riprova; verifica [Impostazioni](impostazioni.md) ▸ **Hotel**. |
| *Conto N incassato. Restano € X da incassare su questo tavolo.* | Hai incassato una parte del conto e il tavolo ha ancora voci da pagare. | Si torna alla divisione: incassa gli altri conti. |
| *Questo conto e' stato chiuso da un altro dispositivo.* | Mentre eri qui il conto è stato incassato da un'altra cassa o da un palmare. | Esci con **Annulla**. |
| *Sconto non registrato sulla comanda: l'incasso prosegue con l'importo mostrato.* | Il servizio non ha salvato lo sconto. | L'incasso prosegue; verifica poi lo sconto nello Storico. |
| *Stampa della copia di cortesia fallita.* / *La fattura e' stata emessa ma non si e' potuta aprire a schermo.* | Problema di stampa o di visualizzazione dopo l'emissione. | La fattura è emessa: ristampala o aprila dalla schermata [Fatture](fatture.md). |
| *Impossibile caricare il conto.* / *Impossibile chiudere il conto.* | Il servizio non risponde o ha dato errore. | Controlla la connessione e riprova. |

## Note

- **Prima i soldi, poi il documento.** Con **INCASSA E STAMPA** la cassa fa nell'ordine: carta sul terminale, contanti nella cassa automatica, documento. Se un passo non riesce non esce nessun documento e il conto resta aperto.
- **Dopo la chiusura.** Con lo scontrino, la chiusura senza documento o l'addebito in camera: la comanda viene chiusa, il tavolo si libera (se non ha altre comande aperte), gli eventuali tavoli uniti tornano separati e torni alla mappa della sala (o all'elenco dell'asporto, se avevi aperto la comanda da lì). Un ordine d'asporto passa a «consegnato»; un ordine a domicilio no: la consegna la segna chi la fa.
- **Incasso di una parte del conto.** Se dopo l'incasso il tavolo ha ancora voci da pagare, si torna alla [divisione](dividi-conto.md); quando l'ultimo conto è incassato la comanda si chiude e si torna alla mappa della sala.
- **Due postazioni sullo stesso tavolo.** Finché stai incassando, la cassa non aggiorna il conto con le modifiche fatte altrove (un totale che cambia sotto un contante già contato è peggio di uno vecchio). Se non hai ancora cominciato, il conto si aggiorna da solo.
- **Ricordo dell'incasso in corso.** Carta già addebitata e incasso della cassa automatica restano ricordati per sette giorni, **solo sulla postazione** che li ha fatti, finché il conto non si chiude.
- **Licenza dimostrativa.** Durante un incasso la finestra della versione dimostrativa non compare: viene rimandata a dopo.
- **Conti documentati dallo Storico.** Aprendo il conto dallo [Storico conti](storico-conti.md) per emettere lo scontrino di un conto chiuso senza documento, si sceglie solo fra **Scontrino** e **Fattura**: terminale POS, cassa automatica, **Camera** e **CHIUDI SENZA DOCUMENTO** non entrano in gioco, perché i soldi sono già stati incassati. <!-- DA VERIFICARE: in questa modalità, sul conto intero, il riquadro "Dividi il conto" e i campi Sconto/Abbuono restano visibili e utilizzabili su una comanda già chiusa: è voluto? -->

## Vedi anche

- [Comanda](comanda.md)
- [Dividi conto](dividi-conto.md)
- [Mappa della sala](mappa-sala.md)
- [Storico conti](storico-conti.md)
- [Fatture](fatture.md)
- [Operatori](operatori.md)
- [Impostazioni](impostazioni.md)
- [Conto sul palmare](../palmare/conto.md)
