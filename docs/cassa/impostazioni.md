---
title: Impostazioni
description: Le impostazioni della cassa - collegamento al servizio, turno, sala, stampanti, POS, cassa automatica, dati fiscali, aspetto, menu online, hotel e licenza digitale.
app: Cassa
percorso: Menu ▸ Impostazioni
pagina: ImpostazioniPage
---

# Impostazioni

Da qui si prepara la cassa al lavoro: a quale servizio si collega, chi è in turno, su quali
stampanti, terminali POS e casse automatiche lavora, i dati fiscali della ditta, l'aspetto
dell'app, il menu online, l'addebito in camera e la licenza digitale. È la schermata del
titolare o di chi installa l'impianto; il cassiere la apre di solito solo per uscire dal turno.

!!! info "In sintesi"

    - **Dove si trova:** Menu ▸ **Impostazioni**
    - **Chi la usa:** titolare, installatore; cassiere per il turno
    - **Disponibile anche su:** [Palmare](../palmare/impostazioni.md) (con meno sezioni)

---

## A cosa serve

Alcune impostazioni valgono **solo per questa cassa** (il servizio a cui si collega, il tavolo
dell'asporto, quale stampante, quale POS e quale cassa automatica usa, il tema), altre valgono
**per tutto l'impianto** e le vedono tutte le postazioni (l'elenco delle stampanti, dei terminali
POS e delle casse automatiche, la stampante fiscale, i modelli di stampa, i dati della ditta, il
menu online, il codice di addebito in camera). Ogni pannello lo dice nella sua riga di
descrizione o nel messaggio che compare dopo il salvataggio.

Esempio: in un locale con due casse al banco e una sola stampante fiscale, la stampante fiscale si
imposta una volta; la stampante del preconto invece si sceglie su ciascuna cassa, perché ognuna
stampa su quella che ha vicino.

## Prima di cominciare

- Per quasi tutti i pannelli la cassa deve essere collegata al servizio: comincia sempre da
  **Connessione** (vedi [Prima configurazione](../introduzione/prima-configurazione.md)).
- Il tavolo dell'asporto si sceglie fra sale e tavoli già creati in
  [Sale e tavoli](sale-e-tavoli.md).
- Per **Dati fiscali ▸ Fattura** servono le aliquote IVA e gli articoli già presenti in
  [Tabelle di base](tabelle-di-base.md) e [Articoli](articoli.md).

## La schermata

![Impostazioni](../assets/img/cassa/impostazioni.png)

La schermata è divisa in due:

- **a sinistra** l'elenco delle voci: **Turno**, **Connessione**, **Sala**, **Stampante preconto**,
  **Modelli di stampa**, **Stampante fiscale**, **Pagamento con carta**, **Cassa automatica**,
  **Dati fiscali**, **Aspetto**, **Menu online**, **Hotel**, **Licenza**. Sotto ogni nome, in
  piccolo, c'è lo stato attuale (per esempio chi è in turno, l'indirizzo del servizio, il tipo di
  stampante fiscale, il terminale POS in uso);
- **a destra** il pannello della voce scelta, con in testa titolo e una riga che dice a cosa
  serve, e in fondo i pulsanti e il messaggio con l'esito dell'ultima operazione.

All'apertura è selezionata la voce **Turno**. La voce scelta è evidenziata con il bordo arancione.

## Campi e indicatori

### Turno

![Turno](../assets/img/cassa/impostazioni-turno.png)

*Chi sta firmando le comande da questa postazione.*

| Elemento | Descrizione |
|---|---|
| **In turno** | Il nome dell'operatore entrato su questa cassa, oppure *Nessun operatore*. Le comande mandate da qui portano il suo nome. |
| *Per cambiare operatore si esce dal turno; per rientrare serve il PIN.* | Promemoria, visibile quando c'è un operatore in turno. |
| **Esci dal turno** | Chiude il turno (chiede conferma) e riporta alla schermata di [accesso](accesso.md). Compare solo con un operatore in turno. |
| **Accedi** | Apre la schermata di [accesso](accesso.md). Compare solo quando nessuno è in turno. |

### Connessione

![Connessione](../assets/img/cassa/impostazioni-connessione.png)

*Il servizio a cui si collega questa cassa.* Vale solo per questa cassa.

| Elemento | Descrizione |
|---|---|
| **Indirizzo** (riquadro **Servizio**) | L'indirizzo del servizio RistoFacile del locale, con la porta: per esempio `http://192.168.1.50:8080`. Si scrive a mano: chiedilo a chi ha installato il servizio. |
| **Utente** (riquadro **Accesso**) | Il nome utente con cui la cassa si presenta al servizio. |
| **Password** | La password di quell'utente. Non viene mai rimostrata: se ne è già salvata una compare *Password già salvata: lascia vuoto per non modificarla.* |
| **Salva e connetti** | Salva i tre dati e prova subito una lettura vera dal servizio (l'elenco delle sale). Durante la prova gira la rotellina. |
| Riga di esito | *Connesso a* (indirizzo) *come* (utente)*.* se tutto è a posto, *Non configurato.* se la cassa non è collegata. |

Sotto la voce **Connessione**, a sinistra, si legge l'indirizzo in uso.

<!-- DA VERIFICARE: la ricerca del servizio per nome del sito e' stata tolta (commit 96b9f62 del repo RistoFacile); confermare che l'indirizzo si scrive sempre a mano e che non tornera'. -->

### Sala

*Il tavolo dell'asporto e come questa postazione segue la sala.* Due linguette in testa:
**Tavolo asporto** e **Mappa e servizio**.

![Sala - Tavolo asporto](../assets/img/cassa/impostazioni-sala.png)

**Tavolo asporto**

| Elemento | Descrizione |
|---|---|
| **Sala** | Tutte le sale dell'impianto, anche quelle che non compaiono sulla mappa. Tocca la sala che contiene il tavolo virtuale dell'asporto: il suo nome si vede in arancione accanto al titolo. |
| **Tavolo** | I tavoli della sala scelta. Tocca quello da usare per l'asporto (un secondo tocco lo deseleziona). *Il tavolo virtuale su cui si appoggiano gli ordini da asporto: sala e tavolo devono già esistere.* |
| **Salva tavolo asporto** | Salva la scelta **per questa cassa**. |
| Riga di esito | Per esempio *Tavolo asporto: Asporto, tavolo 99.* oppure *Nessun tavolo asporto configurato.* |

Se su questa cassa non è mai stato scelto un tavolo, la cassa prova a ricavarlo dagli ordini di
asporto già fatti; la scelta fatta qui vale sempre di più.

**Mappa e servizio**

| Elemento | Descrizione |
|---|---|
| **Prenotazioni in mappa** | *Con quanto anticipo la mappa segnala un tavolo prenotato. Zero la spegne.* Cursore da 0 a 24 ore (proposta: 1 ora). Sotto, a parole, la scelta: *Le prenotazioni confermate compaiono sulla mappa 2 ore prima.* oppure *Segnalazione disattivata: la mappa non mostra le prenotazioni.* |
| **Aggiornamento automatico** | *Ogni quanti secondi le schermate di sala mostrano il lavoro degli altri dispositivi. Zero lo spegne.* Cursore da 0 a 60 secondi a passi di 5 (proposta: 5). Sotto: *Le schermate di sala controllano ogni 5 secondi se un altro dispositivo ha cambiato qualcosa.* oppure *Aggiornamento automatico spento: le schermate si aggiornano solo riaprendole.* |
| **Tagliando di via in cucina** | *Quando da questa postazione si dà il via a un'uscita, in cucina esce anche il tagliando stampato.* Pulsante **SI'** / **NO** (proposto **SI'**): ogni tocco lo inverte. |

I tre valori valgono solo per questa cassa e si salvano appena li cambi: non c'è un pulsante
**Salva**.

### Stampante preconto

![Stampante preconto](../assets/img/cassa/impostazioni-preconto.png)

*La stampante di rete su cui escono il preconto e il QR del menu.*

| Elemento | Descrizione |
|---|---|
| **Stampanti dell'impianto** (riquadro **Questa cassa stampa su**) | Tendina con le stampanti già registrate sull'impianto. Sceglierne una la rende subito quella di questa cassa. *L'elenco vale per tutte le casse; la scelta solo per questa.* Se l'impianto non ne ha ancora: *Nessuna stampante sull'impianto: scrivi indirizzo e porta qui a fianco e premi Salva.* |
| **Indirizzo IP** (riquadro **Indirizzo della stampante**) | L'indirizzo della stampante in rete, per esempio `192.168.1.200`. Obbligatorio. |
| **Porta** | Di solito `9100` (è la proposta). |
| Riga di esito | Per esempio *Questa cassa stampa su Banco (192.168.1.200:9100).* oppure *Nessuna stampante configurata su questa cassa.* |

Sotto la voce, a sinistra, si legge l'indirizzo della stampante in uso.

### Modelli di stampa

![Modelli di stampa](../assets/img/cassa/impostazioni-modelli.png)

*Come sono fatti il ticket di cucina e il preconto. Il modello vale per tutte le postazioni.*

| Elemento | Descrizione |
|---|---|
| **Comanda di cucina**, **Tagliando di via**, **Messaggio**, **Preconto** | Il documento da modificare. Se il modello aperto ha modifiche non salvate, cambiando documento la cassa chiede conferma. |
| **MODELLO** | La zona di modifica. Si lavora in due modi: **A schede** (ogni riga del documento è una scheda da compilare) o **Testo** (il modello scritto per intero, per chi lo conosce). Se un modello non si può rappresentare a schede la cassa resta sul testo e ne dice il motivo. |
| **COLONNE** **32** / **42** / **48** | Larghezza della carta in caratteri (solo nella modifica a schede): 32 per la carta da 58 mm, 42 per le Epson TM da 80 mm, 48 per quasi tutte le altre da 80 mm. |
| Barra dei tasti (modifica a schede) | Su una riga scelta: grassetto, **ALTA**, **LARGA**, bianco su nero; allineamento a sinistra, al centro, a destra o **nel blocco**; **+ Campo** (inserisce un dato del documento scelto da un elenco, per esempio il nome del piatto); **colonna a destra** (aggiunge una seconda casella allineata a destra, per esempio per i prezzi); **quando?** (*Stampala sempre* oppure *Solo se c'e'* un certo dato); frecce per spostare in alto o in basso; cestino per eliminare. |
| **+ Riga**, **+ Separatore**, **+ Spazio**, **+ Elenco** | Aggiungono una scheda. **+ Elenco** chiede *Di cosa vuoi fare l'elenco?* (per esempio le righe della comanda). |
| **ANTEPRIMA** | Il documento come uscirà sulla carta, composto con dati di prova. |
| Riga in fondo | Da dove viene il modello: *Modello di questo impianto.*, *Modello di questo impianto (ultima copia scaricata: il servizio non risponde).* oppure *Modello predefinito: questo impianto non ne ha ancora uno suo.* |
| **Salva** | Salva il modello sul servizio: *Modello salvato: vale per tutte le postazioni.* |
| **Stampa di prova** | Stampa il modello sulla stampante del preconto di questa cassa. |
| **Ripristina predefinito** | Cancella il modello dell'impianto e torna alla stampa di fabbrica (chiede conferma). |

<!-- DA VERIFICARE: elenco dei campi proposti da "+ Campo" e delle condizioni di "quando?" per ciascun documento: valutare una scheda dedicata ai modelli di stampa. -->

### Stampante fiscale

![Stampante fiscale](../assets/img/cassa/impostazioni-fiscale.png)

*Il registratore telematico su cui esce lo scontrino quando si chiude il conto.* Vale per tutto
l'impianto.

| Elemento | Descrizione |
|---|---|
| **Tipo** | La marca del registratore: **Epson**, **DTR**, **3i**, **RCH**, **Custom**, **Axon**, **Ditron**. |
| **Indirizzo (IP o IP:porta)** | L'indirizzo del registratore in rete, per esempio `192.168.1.100`. Con **Ditron** l'etichetta diventa **Porta logica (driver WinEcrCom)** e si scrive il numero della porta (per esempio `1`): il Ditron non sta in rete ma è collegato al computer del servizio. |
| Riga di esito | Per esempio *Stampante fiscale: Epson - 192.168.1.100.* oppure *Nessuna stampante fiscale configurata.* |

Sotto la voce, a sinistra, si legge il tipo scelto.

### Pagamento con carta

![Pagamento con carta](../assets/img/cassa/impostazioni-carte.png)

*I terminali POS dell'impianto: con INCASSA l'importo in carta viene chiesto al terminale.*
L'elenco dei terminali vale per tutto l'impianto; quale terminale usa questa cassa vale solo qui.

| Elemento | Descrizione |
|---|---|
| **Terminali** | L'elenco dei terminali POS dell'impianto, con nome e indirizzo. Quello usato da questa cassa porta la pastiglia verde **IN USO**. Tocca un terminale per aprirne la scheda. |
| **Scheda del terminale** | Si apre toccando un terminale o **+  NUOVO**. Finché non è aperta compare *Tocca un terminale per vederne la scheda, o premi NUOVO per aggiungerne uno.* |
| **Numero** | Il numero del terminale nell'impianto (maggiore di zero). Per un terminale nuovo è proposto il primo libero. |
| **Descrizione** | Il nome che vedi in elenco, per esempio *POS banco*. |
| **ID terminale** | Il codice del terminale scritto sul POS (per esempio `00000001`); non è il **Numero**. |
| **Indirizzo IP** / **Porta** | Dove si trova il terminale in rete. Porta proposta: `10000`. |
| **ID cassa** (riquadro **Su questa cassa**) | Il numero con cui questa cassa si presenta al terminale. Proposto `1`. |
| **Questa cassa incassa le carte su** | In fondo al pannello: il terminale in uso, oppure *Nessun terminale: le carte si battono a mano sul POS*. Lo stesso testo compare sotto la voce, a sinistra. |

<!-- DA VERIFICARE: a cosa serve in pratica "ID cassa" (con due casse sullo stesso terminale va dato un numero diverso a ciascuna?). -->

Al momento si gestiscono solo i terminali POS standard collegati in rete; i POS in cloud (per
esempio SumUp) non si configurano da qui.

### Cassa automatica

![Cassa automatica](../assets/img/cassa/impostazioni-cassa-automatica.png)

*Le macchine rendiresto dell'impianto: con INCASSA i contanti vengono chiesti alla macchina.*
L'elenco delle macchine vale per tutto l'impianto; quale macchina usa questa cassa vale solo qui.

| Elemento | Descrizione |
|---|---|
| **Macchine** | L'elenco delle casse automatiche dell'impianto; quella usata da questa cassa porta **IN USO**. Tocca una macchina per aprirne la scheda, o **+  NUOVA** per aggiungerne una. |
| **Numero** | Il numero della macchina nell'impianto (maggiore di zero). |
| **Descrizione** | Il nome in elenco, per esempio *Self ingresso*. |
| **Marca** | **PagAmico** o **VNE**. |
| **Indirizzo IP** | Dove si trova la macchina in rete. Obbligatorio. |
| **Porta** | Vuota = la porta di fabbrica della marca (è mostrata in grigio nel campo). |
| **Password erogazione** | Solo per PagAmico: la password di erogazione impostata sulla macchina. Senza, la macchina rifiuta i comandi che danno denaro (resto, prelievo). |
| **POS collegato alla macchina** | **SI'**: *la carta la incassa la macchina.* **NO**: *la carta va sul POS del bancone.* |
| **Questa cassa incassa i contanti su** | In fondo al pannello: la macchina in uso, oppure *Nessuna macchina: i contanti si incassano a mano*. |

Nel riquadro **Su questa cassa**, visibile con una macchina scelta:

| Elemento | Descrizione |
|---|---|
| *Incasso rimasto aperto (per esempio dopo un riavvio)? Sblocca restituisce al cliente quello che ha inserito.* | Spiega il pulsante **Sblocca incasso**. |
| Importo (*€ 0,00*) | L'importo da prelevare. |

La cassa automatica è solo della cassa: il palmare non la usa.

### Dati fiscali

Sotto il titolo compare il nome della ditta. Due linguette: **Ditta** e **Fattura**. Servono
alla fattura elettronica e valgono per tutto l'impianto.

![Dati fiscali - Ditta](../assets/img/cassa/impostazioni-ditta.png)

**Ditta**

| Elemento | Descrizione |
|---|---|
| **Partita IVA**, **Chi è** | In sola lettura: arrivano dall'anagrafica della ditta. **Chi è** vale *Persona giuridica*, *Ditta individuale* o *Persona fisica*; lo stesso testo compare sotto la voce, a sinistra. |
| **Regime fiscale** | Tocca per scegliere da un elenco (da *RF01 Ordinario* a *RF19 Regime forfettario*). Se manca: *Non impostato: la fattura elettronica non esce*. |
| **Indirizzo**, **CAP**, **Città**, **Prov.** | La sede da scrivere in fattura. CAP di 5 cifre, provincia di 2 lettere. |
| **Iscritta al Registro delle Imprese** | **SI'** / **NO**. Con **SI'**, per una persona giuridica, compaiono **Ufficio** (sigla della provincia), **Numero REA** e **Natura** (codice numerico). |
| **Capitale sociale** | Compare solo per le nature giuridiche che lo richiedono. |
| **Socio unico** | **SI'** / **NO**; compare solo per la natura che lo prevede. |
| **Per la fattura elettronica** | *Tutto a posto: la fattura elettronica può uscire.* oppure, in giallo, l'elenco di cosa manca. |
| **Salva dati ditta** | Salva sul servizio. |

<!-- DA VERIFICARE: tabella dei codici "Natura" (quale codice corrisponde a SPA, SRL, ecc.) e se Indirizzo/CAP/Citta' sono la sede legale o il domicilio fiscale. -->

![Dati fiscali - Fattura](../assets/img/cassa/impostazioni-fattura.png)

**Fattura**

| Elemento | Descrizione |
|---|---|
| **Invio per email** | *La casella da cui parte la copia della fattura per il cliente.* |
| **Server**, **Porta** | Il server di posta in uscita (per esempio `smtp.esempio.it`) e la porta (per esempio `587`). |
| **Utente**, **Password** | Le credenziali della casella. Sotto la password: *Non impostata*, *Impostata - lascia vuoto per non cambiarla* oppure *Verra' sostituita al salvataggio*. |
| **SSL**, **TLS** | **SI'** / **NO**, secondo quanto richiede il fornitore della posta. |
| Avviso in giallo | *La copia per email non partirebbe:* seguito da cosa manca. |
| **Salva posta** | Salva i dati della posta. |
| **Coperto e abbuono** | *Non arrivano dalla comanda: senza aliquota prendono quella della ditta, senza articolo escono come riga descrittiva.* |
| **Aliquota del coperto** | Tocca per scegliere un'aliquota IVA; *Default della ditta* se non scelta. **Azzera** la toglie. |
| **Articolo del coperto**, **Articolo dell'abbuono** | Tocca per scegliere un articolo dall'anagrafica (serve se devono muovere il magazzino); *Nessuno* se non scelto. **Azzera** lo toglie. |
| **Salva coperto e abbuono** | Salva le tre scelte sul servizio. |

### Aspetto

![Aspetto](../assets/img/cassa/impostazioni-aspetto.png)

*Come si vede questa applicazione. «Sistema» segue il dispositivo.*

| Elemento | Descrizione |
|---|---|
| **Tema**: **Scuro**, **Chiaro**, **Sistema** | Tocca uno dei tre riquadri: il tema cambia subito e resta salvato su questa cassa. **Sistema** segue l'impostazione chiara/scura di Windows o del tablet. Il tema proposto è **Scuro**. |

### Menu online

*Indirizzo e QR code del menu che i clienti consultano dal tavolo.* Ha tre linguette:
**Qrcode**, **Sincronizzazione** e **Stile**. È descritto nella scheda
[Menu online](menu-online.md). Esiste solo sulla cassa.

### Hotel

![Hotel](../assets/img/cassa/impostazioni-hotel.png)

*Addebito del conto sulla camera dell'ospite, in HotWin. Vale per tutte le casse.*

| Elemento | Descrizione |
|---|---|
| **Codice addebito** | *Il conto entra nell'estratto conto della camera con questo codice: reparto e IVA sono i suoi. Senza codice la cassa non mostra CAMERA.* Elenco dei codici di addebito dell'hotel, ciascuno con il suo reparto: tocca quello da usare. |
| Avviso | *Su questo impianto non ci sono le tabelle dell'hotel: l'addebito in camera non si puo' usare.* quando il locale non è collegato a un hotel. |
| Stato sotto la voce | *Addebito in camera col codice* (codice), *Addebito in camera spento* oppure *Hotel non presente su questo impianto*. |

### Licenza

![Licenza](../assets/img/cassa/impostazioni-licenza.png)

*Attivazione e disattivazione della licenza digitale su questo dispositivo.* Il pannello mostra
lo stato della licenza digitale e i campi **Seriale**, **Edizione** e **Nome del dispositivo**,
con i pulsanti **Attiva** e **Disattiva questo dispositivo**. È descritto nella scheda
[Licenza digitale](../introduzione/licenza.md).

## Pulsanti e comandi

| Comando | Effetto |
|---|---|
| Voce dell'elenco a sinistra | Mostra a destra il pannello corrispondente. |
| **Salva e connetti** (Connessione) | Salva indirizzo, utente e password e verifica il collegamento. |
| **Esci dal turno** / **Accedi** (Turno) | Chiude il turno dell'operatore / apre l'accesso. |
| **Tavolo asporto** / **Mappa e servizio** (Sala) | Passano da una linguetta all'altra. |
| **Salva tavolo asporto** | Salva sala e tavolo dell'asporto per questa cassa. |
| **SI'** / **NO** (Tagliando di via in cucina) | Accende o spegne il tagliando di via stampato. |
| **Salva** (Stampante preconto) | Registra indirizzo e porta nell'elenco dell'impianto (o corregge la stampante scelta) e la usa su questa cassa. *Salva la aggiunge all'elenco dell'impianto, o corregge quella scelta.* |
| **Stampa di prova** (Stampante preconto) | Manda una pagina di prova all'indirizzo scritto. |
| **Verifica stato** (Stampante preconto) | Chiede alla stampante se è pronta. |
| **Togli** (Stampante preconto) | Toglie la stampante scelta dall'elenco dell'impianto, per tutte le casse (chiede conferma). |
| **Salva** / **Verifica stato** (Stampante fiscale) | Salva tipo e indirizzo sull'impianto / interroga il registratore. |
| **+  NUOVO** (Pagamento con carta) | Apre una scheda vuota per un nuovo terminale. |
| **Salva** / **Togli** / **Chiudi** (scheda del terminale) | Salva il terminale nell'elenco dell'impianto / lo toglie (chiede conferma) / chiude la scheda. |
| **Usa su questa cassa** (Pagamento con carta) | Da adesso questa cassa incassa le carte sul terminale scelto, con l'**ID cassa** scritto. |
| **Verifica stato** (Pagamento con carta) | Interroga il terminale scelto e ne riporta la risposta. |
| **Carte a mano** | Questa cassa non usa più nessun terminale: le carte si battono a mano sul POS. |
| **+  NUOVA** (Cassa automatica) | Apre una scheda vuota per una nuova macchina. |
| **Salva** / **Togli** / **Chiudi** (scheda della macchina) | Salva la macchina nell'elenco dell'impianto / la toglie (chiede conferma) / chiude la scheda. |
| **Usa su questa cassa** (Cassa automatica) | Da adesso questa cassa incassa i contanti sulla macchina scelta. |
| **Verifica stato** (Cassa automatica) | Interroga la macchina. |
| **Sblocca incasso** | Chiude un incasso rimasto aperto restituendo al cliente il contante inserito (chiede conferma). |
| **Preleva** | Fa erogare dalla macchina l'importo scritto (chiede conferma). |
| **Ricarica** | Apre la ricarica del fondo cassa (solo PagAmico; sulla VNE la ricarica si fa dal pannello della macchina). |
| **FINE RICARICA** | Nella finestra della ricarica: chiude la ricarica. |
| **Contanti a mano** | Questa cassa non usa più nessuna macchina: i contanti si incassano a mano. |
| **Ditta** / **Fattura** (Dati fiscali) | Passano da una linguetta all'altra. |
| **Salva dati ditta** / **Salva posta** / **Salva coperto e abbuono** | Salvano sul servizio i dati della rispettiva sezione. |
| **Azzera** | Toglie l'aliquota o l'articolo scelto per coperto o abbuono. |
| **Salva** (Hotel) | Salva il codice di addebito scelto per tutto l'impianto. |
| **Spegni addebito** (Hotel) | Toglie la scelta del codice; poi tocca **Salva** per spegnere l'addebito in camera. |

## Come si fa

### Collegare la cassa al servizio

1. Tocca **Connessione**.
2. In **Indirizzo** scrivi l'indirizzo del servizio, per esempio `http://192.168.1.50:8080`.
3. Scrivi **Utente** e **Password**.
4. Tocca **Salva e connetti**.
5. Sotto il pulsante compare *Connesso a http://192.168.1.50:8080 come* (utente)*.*

### Scegliere la stampante del preconto

1. Tocca **Stampante preconto**.
2. Se l'impianto ha già delle stampanti, scegli quella vicina a questa cassa in **Stampanti
   dell'impianto**: è subito attiva.
3. Altrimenti scrivi **Indirizzo IP** e **Porta** e tocca **Salva**.
4. Tocca **Stampa di prova**: dalla stampante esce la pagina di prova e compare *Stampa di prova
   inviata a* (indirizzo)*.*

### Collegare un terminale POS a questa cassa

1. Tocca **Pagamento con carta**.
2. Tocca **+  NUOVO** (o un terminale già in elenco).
3. Compila **Descrizione**, **ID terminale**, **Indirizzo IP** e **Porta**, poi tocca **Salva**.
4. Con il terminale selezionato scrivi l'**ID cassa** e tocca **Usa su questa cassa**.
5. Tocca **Verifica stato** per controllare che il terminale risponda.
6. Il terminale porta la pastiglia **IN USO** e in fondo si legge *Questa cassa incassa le carte
   su* (nome del terminale).

### Ricaricare il fondo della cassa automatica

1. Tocca **Cassa automatica** e tocca la macchina in elenco.
2. Tocca **Ricarica**.
3. Si apre la finestra *Ricarica di* (macchina): inserisci monete e banconote nella macchina.
   L'importo caricato sale mentre inserisci.
4. Tocca **FINE RICARICA**.
5. Al termine compare l'esito della ricarica del fondo cassa.

Finché la finestra della ricarica è aperta la macchina non incassa.

### Spostare il tavolo dell'asporto

1. Tocca **Sala**, linguetta **Tavolo asporto**.
2. Tocca la sala e poi il tavolo virtuale dell'asporto.
3. Tocca **Salva tavolo asporto**.
4. Compare *Tavolo asporto salvato:* (sala)*, tavolo* (numero)*.*

## Controlli e messaggi

| Messaggio | Causa | Cosa fare |
|---|---|---|
| *Base URL e utente sono obbligatori.* | **Salva e connetti** con indirizzo o utente vuoti. | Compila **Indirizzo** e **Utente**. |
| *La password e' obbligatoria (nessuna password gia' salvata per questa installazione).* | Primo salvataggio senza password. | Scrivi la password. |
| *Connessione fallita.* (con il dettaglio) | Il servizio non risponde o rifiuta utente e password. | Controlla indirizzo, porta, utente e password e che il servizio sia acceso. |
| *Seleziona una sala e un tavolo per l'asporto.* | **Salva tavolo asporto** senza sala o tavolo. | Tocca prima la sala, poi il tavolo. |
| *Il tavolo asporto configurato (sala 2, tavolo 99) non esiste piu' in anagrafica: riselezionalo.* | Il tavolo scelto è stato cancellato. | Scegli un altro tavolo e salva. |
| *Impossibile caricare sale e tavoli:* … | La cassa non è collegata al servizio. | Sistema prima la **Connessione**. |
| *Inserisci l'indirizzo IP della stampante comande.* | **Salva**, **Stampa di prova** o **Verifica stato** con l'indirizzo vuoto. | Scrivi l'indirizzo IP. |
| *Porta della stampante comande non valida (di solito 9100).* | Porta non numerica o fuori intervallo. | Correggi la porta. |
| *Salvata solo su questa cassa (*indirizzo*): l'impianto non risponde (*…*).* | Il servizio non risponde: la stampante è stata salvata solo su questa cassa. | Riprova quando il servizio è raggiungibile, per averla nell'elenco dell'impianto. |
| *Stampa di prova non riuscita.* | La stampante non ha stampato. | Controlla che sia accesa, in rete e con la carta. |
| *Scegli prima una stampante dall'elenco dell'impianto.* | **Togli** senza una stampante scelta. | Scegli la stampante in **Stampanti dell'impianto**. |
| *Inserisci l'indirizzo della stampante fiscale.* | **Salva** o **Verifica stato** con l'indirizzo vuoto. | Scrivi l'indirizzo (o la porta logica per Ditron). |
| *Verifica della stampante fiscale fallita.* | Il registratore non risponde o segnala un errore. | Leggi il dettaglio e controlla il registratore. |
| *L'id del terminale dev'essere un numero maggiore di zero.* / *La porta dev'essere un numero maggiore di zero.* | Numero o porta del terminale non validi. | Correggi il campo. |
| *Scegli un terminale dall'elenco.* | **Usa su questa cassa** senza un terminale scelto. | Tocca un terminale in elenco. |
| *Nessun terminale sull'impianto. Premi NUOVO per aggiungerne uno.* | L'impianto non ha terminali. | Tocca **+  NUOVO**. |
| *Il servizio non ha restituito nessun terminale: resta valido quello gia' scelto su questa cassa.* | Il servizio non ha dato l'elenco. | La cassa continua a usare il terminale scelto; riprova più tardi. |
| *Inserisci l'indirizzo IP della cassa automatica.* | **Salva** senza indirizzo. | Scrivi l'indirizzo. |
| *La porta dev'essere un numero maggiore di zero (lasciala vuota per quella di fabbrica).* | Porta non valida. | Correggi o svuota il campo. |
| *Scrivi l'importo da prelevare, per esempio 50 o 12,50.* | **Preleva** senza un importo valido. | Scrivi l'importo. |
| *Prelievo dalla cassa automatica.* (con *Il contante potrebbe essere uscito lo stesso: controlla la macchina prima di riprovare.*) | La macchina non ha risposto durante il prelievo. | Controlla la macchina **prima** di ripetere: potresti prelevare due volte. |
| *Ricarica della cassa automatica.* (con *…premi di nuovo RICARICA per riprenderla.*) | La ricarica non si è aperta o la cassa ha perso il contatto con la macchina. | Tocca di nuovo **Ricarica**: riprende la ricarica rimasta aperta. |
| *Salvataggio dei dati della ditta non riuscito.* | Il servizio ha rifiutato i dati o non risponde. | Leggi il dettaglio e riprova. |
| *Dati della ditta salvati. Restano 2 cose da sistemare per la fattura elettronica.* | Mancano ancora dati obbligatori. | Completa quanto elencato in **Per la fattura elettronica**. |
| *Salvataggio della configurazione fattura non riuscito.* | Il servizio non risponde. | Riprova. |
| *Impossibile leggere i codici addebito dell'hotel:* … | Il servizio non risponde. | Controlla la connessione. |
| *Il modello ha un errore e non e' stato salvato:* … | Il modello di stampa contiene un errore. | Correggi la riga segnalata in rosso. |
| *Stampante comande non configurata: impostala nella sezione "Stampante preconto".* | **Stampa di prova** di un modello senza stampante. | Imposta la **Stampante preconto**. |

## Note

- **Cosa vale per chi.** Collegamento, turno, tavolo dell'asporto, stampante scelta, terminale POS
  e cassa automatica in uso, i tre valori di **Mappa e servizio** e il tema valgono solo per questa
  cassa. Elenco delle stampanti, dei terminali e delle macchine, stampante fiscale, modelli di
  stampa, dati fiscali, menu online e codice di addebito in camera valgono per tutto l'impianto.
- La stampante fiscale si imposta anche dal [palmare](../palmare/impostazioni.md): è la stessa
  impostazione dell'impianto, chi salva per ultimo vince.
- **Togli** su stampanti, terminali e macchine li toglie per **tutte** le casse: quelle che li
  usavano tornano a lavorare a mano finché non ne scelgono un altro.

!!! warning "Prelievo e cassa automatica"

    Se durante un **Preleva** la macchina non risponde, il contante potrebbe essere uscito lo
    stesso. Controlla la macchina prima di ripetere l'operazione.

## Vedi anche

- [Prima configurazione](../introduzione/prima-configurazione.md)
- [Licenza digitale](../introduzione/licenza.md)
- [Menu online](menu-online.md)
- [Accesso operatore](accesso.md)
- [Sale e tavoli](sale-e-tavoli.md)
- [Asporto e domicilio](asporto.md)
- [Conto](conto.md)
- [Impostazioni del palmare](../palmare/impostazioni.md)
