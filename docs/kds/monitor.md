---
title: Monitor
description: Il tabellone del monitor di cucina - i piatti in coda, in lavorazione e pronti, i tempi d'attesa e i colori, l'avanzamento con un tocco e i messaggi dalla sala.
app: Monitor di cucina
percorso: Scelta del centro ▸ APRI MONITOR
pagina: MonitorPage
---

# Monitor

Il tabellone della cucina: tutti i piatti del centro di produzione, divisi in tre colonne secondo
lo stato - **IN CODA**, **IN LAVORAZIONE**, **PRONTO** - con il tavolo, la quantità, le note e da
quanto aspettano. Chi cucina tocca un piatto per farlo avanzare. Serve alla cucina (o al bar, alla
pizzeria) per tutto il servizio.

!!! info "In sintesi"

    - **Dove si trova:** Scelta del centro ▸ **APRI MONITOR**
    - **Chi la usa:** cuoco, pizzaiolo, barista
    - **Disponibile anche su:** solo monitor di cucina

---

## A cosa serve

Al posto dei foglietti appesi: il cameriere invia la comanda e i piatti compaiono **IN CODA**. Il
cuoco tocca quelli che inizia (vanno **IN LAVORAZIONE**), li tocca quando sono finiti (vanno in
**PRONTO**: in sala il cameriere lo vede sul palmare) e li tocca di nuovo quando escono dal passe
(spariscono). Il colore e il tempo di ogni piatto dicono quali sono in ritardo.

Esempio: alle 20:40 la colonna IN CODA mostra «Sala principale - Tavolo 12» con tre piatti da 15
minuti, il bordo giallo: è il tavolo da fare per primo.

## Prima di cominciare

- Il monitor collegato al servizio e con il centro scelto (vedi [Scelta del centro](centro.md)).
- Gli articoli del menu assegnati al centro di produzione giusto (vedi [Menu](../cassa/menu.md)).
- La licenza digitale con il modulo del monitor di cucina (vedi [Monitor di cucina](index.md)).

## La schermata

![Monitor](../assets/img/kds/monitor.png)

### La testata

Da sinistra:

- la pastiglia arancione con il **nome del centro** (es. CUCINA): dice quale cucina è questo
  schermo;
- **Aggiornato alle 20:41:15**: l'ora dell'ultimo aggiornamento riuscito. Se l'ora resta ferma, il
  monitor non riceve più dati dal servizio (non è «una cucina tranquilla»). Mentre un tocco viene
  registrato compaiono una rotellina e «Salvataggio…»;
- la pastiglia del **raggruppamento**: **Portata** oppure **Tavolo** (vedi sotto);
- la pastiglia dell'**operatore**: il nome di chi lavora al centro, oppure «Seleziona operatore» in
  arancione;
- la pastiglia **Centro**, che torna alla [Scelta del centro](centro.md).

### Le tre colonne

| Colonna | Colore | Cosa contiene | Se è vuota |
|---|---|---|---|
| **IN CODA** | ambra | Piatti arrivati che nessuno ha ancora iniziato, e in fondo quelli **in attesa** del via. | «Nessun piatto in coda» |
| **IN LAVORAZIONE** | azzurro | Piatti che qualcuno sta preparando. | «Nessun piatto in lavorazione» |
| **PRONTO** | verde | Piatti finiti che aspettano di uscire in sala. | «Niente da ritirare» |

In testa a ogni colonna c'è il **numero di piatti da fare**. Nella colonna IN CODA, accanto, «+3 in
attesa» conta a parte i piatti fermi in attesa del via.

Le colonne non scorrono: se i piatti non stanno in una schermata si dividono in **pagine**. In fondo
a ogni colonna compare «1 / 3» fra due frecce, oppure «tutto a schermo» quando non c'è niente di
nascosto. Le pagine girano da sole ogni otto secondi; toccando una freccia (o un piatto) la rotazione
si ferma per 25 secondi, così chi sta leggendo una pagina non se la vede cambiare sotto gli occhi.

### I gruppi

Dentro ogni colonna i piatti sono raggruppati su due livelli, con la pastiglia del raggruppamento:

- **Portata** (di partenza): prima la portata (es. «Antipasti», «Primi», «Senza portata»), nell'ordine
  in cui escono, e dentro ogni portata i tavoli. Serve a sapere «quanti antipasti devo fare».
- **Tavolo**: prima il tavolo (es. «Sala principale - Tavolo 12», oppure «n. 27 · Asporto - Rossi -
  ritiro 20:30»), dal più vecchio, e dentro ogni tavolo le portate. Serve a far uscire un tavolo tutto
  insieme.

Ogni gruppo ha una testata con il nome, il conteggio e l'attesa più lunga (es. «3 piatti · da 12'»;
«in attesa» per i gruppi fermi; «adesso» per quelli appena arrivati). Un gruppo che continua dalla
pagina precedente porta «(segue)»; un gruppo in attesa porta «· IN ATTESA».

### Gli ordini da asporto e del kiosk

![Titoli degli ordini da asporto e del kiosk](../assets/img/kds/monitor-titoli.png)

Al posto del tavolo, gli ordini da asporto hanno un titolo che comincia con il **numero
dell'ordine**, quello che si chiama al banco e sul monitor in sala (vedi [Chiamate](../cassa/chiamate.md)).
Il numero sta in testa perché, se il titolo è lungo o la colonna è stretta, il monitor taglia la
fine del titolo:

| Ordine | Titolo |
|---|---|
| Kiosk, il cliente mangia nel locale con il segnaposto 12 | «Ordine 27 · Segnaposto 12» |
| Kiosk, da portare via | «Ordine 27 · Porta via» |
| Asporto preso dalla cassa o dal palmare | «n. 27 · Asporto - Rossi - ritiro 20:30» (il titolo di sempre, preceduto dal numero) |

A video i titoli dei gruppi sono in maiuscolo. Un ordine senza numero del giorno (preso prima
dell'aggiornamento che ha introdotto i numeri) ha il titolo di sempre, senza il numero.

Gli ordini del kiosk da pagare **non arrivano in cucina finché non sono pagati**: un ordine pagato
al kiosk compare appena è pagato, uno da pagare alla cassa compare quando la cassa lo incassa (a
meno che i kiosk siano impostati per mandarlo in cucina subito: vedi l'invio in cucina in
[Configurazione del kiosk](../kiosk/configurazione.md#le-impostazioni-del-servizio)).

### La card del piatto

![Card dei piatti](../assets/img/kds/monitor-card.png)

Ogni piatto è una card con:

- la **quantità** in un riquadro (es. «2×»);
- il **nome del piatto**, su più righe se serve;
- la **nota** del cameriere, in giallo (es. «senza cipolla»);
- a destra il **tempo** in minuti (es. «12'»; «—» se non è disponibile). In IN CODA e IN
  LAVORAZIONE è l'attesa da quando il piatto è arrivato in cucina; in PRONTO è da quanto il piatto
  aspetta al passe, e sotto c'è il tempo di preparazione (es. «prep. 8'») o «al passe»;
- accanto alla card, nelle colonne IN LAVORAZIONE e PRONTO, il pulsante con la freccia per
  **tornare indietro** di uno stato.

I piatti **in attesa** del via sono sbiaditi e non si possono toccare.

### I colori del tempo

| Colonna | Bordo giallo | Bordo rosso |
|---|---|---|
| IN CODA e IN LAVORAZIONE | da 10 minuti d'attesa | da 20 minuti d'attesa |
| PRONTO | da 3 minuti al passe | da 6 minuti al passe |

Il colore è sul bordo della card, sul tempo e sulle barre colorate a sinistra della card e del gruppo, e il conteggio del
gruppo diventa rosso quando c'è un piatto in ritardo grave. In PRONTO le soglie sono più strette:
un piatto pronto da sei minuti si sta raffreddando.

## Campi e indicatori

| Elemento | Descrizione |
|---|---|
| **Nome del centro** | Il centro di produzione mostrato da questo schermo. |
| **Aggiornato alle …** | L'ora dell'ultimo aggiornamento riuscito. |
| **Portata / Tavolo** | Il raggruppamento in uso. |
| **Operatore** | Chi lavora al centro: il suo nome viene registrato su chi ha preso in carico i piatti. |
| **Conteggio della colonna** | I piatti da fare, esclusi quelli in attesa. |
| **+N in attesa** | Piatti fermi in attesa del via del cameriere. |
| **1 / 3** / **tutto a schermo** | La pagina mostrata della colonna. |
| **2×** | La quantità del piatto. |
| **Nota in giallo** | La nota del cameriere per la cucina. |
| **12'** | Minuti d'attesa (o al passe, in PRONTO). |
| **prep. 8'** / **al passe** | Solo in PRONTO: quanto ci è voluto a preparare il piatto. |

## Pulsanti e comandi

| Comando | Effetto |
|---|---|
| **Tocco sulla card** | Fa avanzare il piatto di uno stato: da IN CODA a IN LAVORAZIONE, da IN LAVORAZIONE a PRONTO, da PRONTO a consegnato (sparisce dal monitor). Nessuna conferma. |
| **Freccia accanto alla card** | Riporta il piatto allo stato precedente (da PRONTO a IN LAVORAZIONE, da IN LAVORAZIONE a IN CODA). |
| **Avvia / Pronto / Consegna** (testata di un gruppo interno) | Fa avanzare insieme tutti i piatti del gruppo. |
| **Avvia tutto / Tutto pronto / Tutto consegnato** (testata del tavolo, solo nel raggruppamento per **Tavolo**) | Fa avanzare insieme tutti i piatti del tavolo in quella colonna. |
| **Frecce in fondo alla colonna** | Pagina precedente / successiva. |
| **Portata / Tavolo** | Cambia il raggruppamento. La scelta resta memorizzata su questo monitor. |
| **Operatore** | Apre la finestra **Chi lavora in questo centro**. |
| **Centro** | Torna alla [Scelta del centro](centro.md). |
| **LETTO** | Chiude il messaggio dalla sala (vedi sotto). |

Su un gruppo spezzato fra due pagine, i pulsanti del gruppo fanno avanzare solo i piatti che si
vedono. Sui gruppi in attesa del via il pulsante non c'è: il via lo dà il cameriere.

### Chi lavora in questo centro

![Chi lavora in questo centro](../assets/img/kds/monitor-operatore.png)

La pastiglia dell'operatore apre l'elenco degli operatori attivi: tocca il tuo nome (compare la
spunta). «Serve a registrare chi ha preso in carico i piatti. Si puo' lavorare anche senza
sceglierlo.» Se c'è un solo operatore attivo è scelto da solo. Si chiude con la **X** o toccando
fuori.

### Messaggio dalla sala

![Messaggio dalla sala](../assets/img/kds/monitor-messaggio.png)

Quando la sala manda un messaggio a questo centro (vedi [Messaggi](../palmare/messaggi.md)), il
tabellone viene coperto da un riquadro con il bordo giallo: **MESSAGGIO DALLA SALA**, chi l'ha
mandato e a che ora (es. «da Mario alle 20:41»), il testo in grande e il pulsante **LETTO**. Se i
messaggi da leggere sono più di uno, in alto a destra c'è «1 di 3». Il riquadro non si chiude
toccando fuori: solo con **LETTO**. Entro pochi secondi il cameriere vede «LETTO» con l'ora e il nome di chi
lavora al centro (o del centro, se nessuno si è selezionato). Mentre c'è un messaggio le pagine non
girano.

## Come si fa

### Preparare e far uscire un piatto

1. Quando inizi un piatto in **IN CODA**, toccalo: passa in **IN LAVORAZIONE**.
2. Quando è pronto, toccalo: passa in **PRONTO**. Sul palmare del cameriere la portata risulta
   pronta.
3. Quando il cameriere lo porta via, toccalo: sparisce dal monitor.

### Far uscire tutto un tavolo insieme

1. Tocca la pastiglia **Portata** per passare a **Tavolo**.
2. Nella colonna **IN LAVORAZIONE** trova il tavolo.
3. Quando tutto è pronto tocca **Tutto pronto** nella testata del tavolo.
4. Tutti i piatti del tavolo passano in **PRONTO**.

### Correggere un tocco sbagliato

1. Trova il piatto nella colonna in cui è finito per errore.
2. Tocca la freccia accanto alla card.
3. Il piatto torna nella colonna precedente.

Un piatto già consegnato (sparito da PRONTO) non torna indietro dal monitor.
<!-- DA VERIFICARE: c'è un modo per recuperare un piatto toccato per errore in PRONTO (consegnato) e quindi sparito? -->

## Controlli e messaggi

| Messaggio | Causa | Cosa fare |
|---|---|---|
| *Impossibile avanzare il ticket. (…)* | Il servizio non ha registrato il tocco. | Il monitor rilegge lo stato vero: ritocca il piatto se serve. |
| *L'avanzamento e' andato a buon fine solo in parte. (…)* | Con un pulsante di gruppo, alcuni piatti sono avanzati e altri no. | Controlla i piatti rimasti e toccali uno per uno. |
| *Impossibile riportare indietro il ticket. (…)* | Il servizio non ha registrato il ritorno indietro. | Riprova. |
| *Impossibile aggiornare i ticket. (…)* / *Aggiornamento dei ticket non riuscito.* | Il servizio non risponde. L'ora di «Aggiornato alle» resta ferma. | Controlla la rete e il servizio; il monitor riprova da solo. |
| *RistoFacile in modalità demo* | Una cassa del locale è in prova. | Nessuna: il monitor funziona. |
| *Il monitor di cucina è un modulo aggiuntivo di RistoFacile e la licenza digitale di questo ristorante non lo comprende.* | La licenza non comprende il monitor di cucina. Le comande non vengono mostrate. | Contatta il rivenditore. Quando il modulo viene attivato le comande ricompaiono da sole alla verifica successiva (il monitor chiede ogni ora, e a ogni riapertura del tabellone). |

## Note

- **Il tocco non chiede conferma**: si corregge con la freccia. Toccare una card in PRONTO la fa
  sparire dal monitor.
- Se due monitor guardano lo stesso centro, un tocco su uno si vede sull'altro al giro successivo.
- Un piatto **stornato** dal cameriere sparisce dal monitor; quando il conto del tavolo viene chiuso
  spariscono anche i suoi piatti rimasti (non quelli degli ordini d'asporto, che restano finché non
  vengono consegnati).
- I piatti **in attesa** del via restano in fondo alla colonna IN CODA, sbiaditi; compaiono come
  normali quando il cameriere tocca **VIA** sul palmare o sulla cassa.
- Il monitor si aggiorna da solo ogni quattro secondi.
- Gli ordini da asporto si riconoscono dal titolo, che comincia con il numero dell'ordine:
  «n. 27 · Asporto - nome - ritiro 20:30», e per il kiosk «Ordine 27 · Porta via» o
  «Ordine 27 · Segnaposto 12» (vedi sopra).
- **Ordini da portare via e monitor in sala**: quando tutti i piatti di un ordine da asporto o del
  kiosk, già incassato, sono consegnati qui, il suo numero sparisce subito dal monitor in sala (vedi
  [Chiamate](../cassa/chiamate.md)). Toccare «consegnato» subito dopo «pronto» lascia il numero
  sulla TV solo pochi secondi: per questi ordini segna consegnato quando il cliente ha ritirato.
  Quando invece li consegna il banco dalla schermata Chiamate, qui restano nella colonna PRONTO e
  vanno tolti toccandoli.
- Quando la cucina segna pronto un piatto, sul [palmare](../palmare/comanda.md) lo stato della
  portata diventa «pronta» (o «2 pronti») e, se il cameriere ha acceso il richiamo, arriva una
  notifica sul telefono.

## Vedi anche

- [Scelta del centro](centro.md)
- [Monitor di cucina](index.md)
- [Comanda sul palmare](../palmare/comanda.md)
- [Messaggi alla cucina](../palmare/messaggi.md)
- [Centri di produzione](../cassa/centri-di-produzione.md)
- [Chiamate](../cassa/chiamate.md)
