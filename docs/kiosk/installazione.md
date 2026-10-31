---
title: Installazione del kiosk
description: "Per chi installa il kiosk - il totem Windows con l'Accesso assegnato e l'avvio automatico, il tablet Android con il blocco dell'app e il permesso USB, e l'utente web dedicato al kiosk con le sue credenziali ristrette."
app: Kiosk
percorso: Installazione sul totem o sul tablet, prima del primo avvio
pagina: RistoKiosk (Windows, Android)
---

# Installazione del kiosk

Questa pagina è per **chi installa il kiosk** nel locale: come preparare il totem Windows o il
tablet Android perché il cliente non possa uscire dall'app, e quale utente del servizio dargli.
La configurazione dell'app, dopo l'installazione, è in [Configurazione](configurazione.md).

!!! info "In sintesi"

    - **Dove si trova:** sul totem o sul tablet, prima del primo avvio di RistoKiosk
    - **Chi la usa:** chi installa (rivenditore, assistenza, titolare esperto)
    - **Disponibile anche su:** Windows e Android

---

## A cosa serve

Il kiosk sta in mano ai clienti. L'app da sola si apre a tutto schermo, non si chiude con Alt+F4,
con la X o con il tasto Indietro, e si esce solo con il PIN del kiosk. Ma il **blocco del sistema
operativo** non lo fa l'app: va impostato su Windows o su Android, così che il cliente non possa
passare ad altri programmi, al desktop o alle impostazioni. Allo stesso modo, il kiosk va
collegato al servizio con un **utente web suo**, che può fare solo quello che serve al kiosk.

## Prima di cominciare

- Il servizio RistoFacile installato e acceso nel locale, raggiungibile dalla rete del kiosk.
- Un **posto Kiosk** libero sulla licenza RistoFacile del locale, oppure la modalità dimostrativa
  (vedi [Licenza digitale](../introduzione/licenza.md)).
- Per un totem Windows: un PC con Windows 10 o 11 e lo schermo del totem; per un tablet: Android usato in
  orizzontale (un tablet da 10 pollici va bene).
- Le periferiche che si useranno: POS, rendiresto, stampante termica (di rete o USB), lettore di
  QR 2D a tastiera per i segnaposto.

<!-- DA VERIFICARE: con quale pacchetto si installa RistoKiosk su Windows e su Android (installatore in preparazione, Piano 9). -->

## La schermata

Non applicabile: l'installazione si fa nel sistema operativo. Dopo il primo avvio il kiosk chiede
di scegliere il PIN (vedi [Configurazione](configurazione.md#il-primo-avvio)).

## Campi e indicatori

Non applicabile.

## Pulsanti e comandi

Non applicabile.

## Come si fa

### L'utente web del kiosk

Il kiosk si collega al servizio con un nome utente e una password, come le casse. Per il kiosk va
creato **un utente web apposta**, che non sia quello di una cassa, con un'**email sua**, e il suo
nome va scritto fra gli **utenti web dei kiosk** in cassa.

1. Crea l'utente web del kiosk, come gli utenti delle casse, con un'email che non sia di un
   operatore.
2. In cassa apri Menu ▸ **Kiosk**, linguetta **Kiosk**, riquadro **Utenti web dei kiosk**: scrivi il
   nome utente, tocca **Aggiungi** e poi **Salva** (vedi
   [Kiosk](../cassa/kiosk.md#dare-al-kiosk-il-suo-utente-web)). Le maiuscole non contano.
3. Sul kiosk scrivi quel nome e la sua password nella configurazione, riquadro **Servizio**, e
   tocca **Salva e verifica**.
4. L'avviso giallo *Attenzione: le credenziali di questo kiosk non sono ristrette. …* non deve
   comparire.

**Perché.** Le credenziali stanno salvate su un dispositivo che resta tutto il giorno davanti ai
clienti. Con le credenziali di una cassa, chi riuscisse a leggerle potrebbe fare tutto quello che fa
una cassa: aprire e chiudere conti, emettere documenti, leggere le configurazioni del servizio.
Quella delle casse automatiche contiene anche la **password della CashDro**. Con un utente scritto
fra gli utenti dei kiosk, invece:

- il servizio accetta le sue credenziali **solo sulle operazioni del kiosk** (stato, menu, foto,
  ordine e pagamento, licenza, POS, rendiresto e stampa); per tutto il resto risponde *Queste
  credenziali sono di un kiosk: operazione non permessa.*;
- quell'utente **non può entrare** come operatore web né chiedere il **recupero della password**;
- stampa solo sulle stampanti **registrate sul servizio** (vedi
  [Configurazione](configurazione.md#registrare-sul-servizio-la-termica-di-rete-del-kiosk)).

Con l'elenco vuoto nessuno è ristretto e il kiosk lo segnala in configurazione.

!!! note "Un'email per ogni kiosk"
    Il servizio riconosce l'utente del kiosk anche dalla sua email. Se la stessa email è anche di un
    operatore, chi entra con quell'email riceve le restrizioni del kiosk: in cassa lo segnala un
    avviso ambra sull'utente (*L'email … è anche di …*). Dai a ogni kiosk un utente e un'email suoi.

### Windows

1. Crea in Windows un **account locale** apposta per il kiosk, senza diritti di amministratore.
2. Installa RistoKiosk sul PC.
3. Fai in modo che il PC, all'accensione, entri da solo con l'account del kiosk e avvii
   RistoKiosk: accesso automatico all'account e RistoKiosk fra le app in esecuzione automatica.
4. Imposta lo schermo del totem come **schermo principale** di Windows. Il kiosk si apre a tutto
   schermo sempre sullo schermo principale; spostarlo su un altro schermo con la tastiera lo fa
   uscire dal tutto schermo.
5. Blocca l'account del kiosk con l'**Accesso assegnato** di Windows (modalità chiosco): l'account
   vede solo RistoKiosk, senza desktop, barra delle applicazioni e menu Start.
6. Riavvia il PC: deve entrare da solo, aprire RistoKiosk a tutto schermo e mostrare l'attesa.

<!-- DA VERIFICARE: l'Accesso assegnato di Windows accetta RistoKiosk come app del chiosco (e' un programma classico, non un'app dello Store), o serve lo Shell Launcher / una configurazione a piu' app? Scrivere i passi esatti per Windows 10 e 11 Pro. -->

Sul totem, con l'Accesso assegnato, di solito non c'è tastiera: tutto quello che serve al
personale passa dalla configurazione del kiosk, con il PIN. Su un PC RistoKiosk gira in una sola
copia.

### Android

1. Installa RistoKiosk sul tablet.
2. Aprilo una prima volta e scegli il PIN del kiosk (vedi
   [Configurazione](configurazione.md#il-primo-avvio)).
3. Nelle impostazioni di Android accendi il **blocco dell'app** (a seconda del produttore si chiama
   «Blocco app», «Fissa app» o «Blocco schermo sull'app»), con la richiesta del PIN o della
   sequenza del tablet per sbloccarla.
4. Apri RistoKiosk e bloccalo sullo schermo dal menu delle app recenti.
5. Con una **stampante termica USB**: collegala, poi nella configurazione del kiosk scegli
   **USB (collegata al kiosk)**, la stampante, e tocca **Usa questa stampante** (o
   **Stampa di prova**). Android chiede se permettere a RistoKiosk di usare la periferica: tocca
   **Consenti**.

L'app da sola tiene il tablet in orizzontale, nasconde le barre di sistema (si riaffacciano solo
per un attimo strisciando dal bordo), tiene lo schermo acceso e ignora il tasto Indietro.

**Il permesso USB** si chiede in tre momenti: nella configurazione (scelta della stampante o
**Stampa di prova**), all'avvio dell'app e **ogni volta che la stampante scelta si ricollega**. Di
solito capita all'avvio o quando colleghi la stampante, con il personale davanti; ma se la
stampante si stacca e si riattacca durante un ordine (per esempio un cavo che fa contatto) la
richiesta di Android può comparire anche davanti al cliente: in quel caso tocca tu **Consenti**.
Le stampe del cliente non aspettano il permesso: se manca, non escono e il kiosk va avanti lo
stesso (vedi [Pagamenti](pagamenti.md#note)).

**La rete.** Il kiosk Android parla con il servizio in `http` sulla rete del locale: nella
configurazione si scrive l'indirizzo con `http://`, come per le casse.

### Aggiornare servizio, casse e kiosk

Con l'aggiornamento che porta in cassa la voce **Kiosk** e gli **Ordini dal kiosk**:

1. **Ferma i kiosk** prima di cominciare (sul kiosk, **Esci dall'app**), a un'ora senza clienti: i
   kiosk restano senza ordini finché l'aggiornamento non è finito.
2. Aggiorna **prima il servizio**. Le schermate nuove della cassa e del kiosk chiedono al servizio
   cose che un servizio vecchio non sa.
3. Aggiorna **i kiosk insieme al servizio**: un kiosk della versione di prima, con il servizio nuovo,
   non riesce a segnalare un pagamento da verificare (il servizio rifiuta la segnalazione). Lasciali
   comunque senza ordini.
4. Aggiorna **tutte le casse e tutti i palmari**. Finché ne resta uno di prima, i kiosk restano
   spenti:
   - una cassa di prima calcola coperto e servizio sul conto di un ordine del kiosk, non conosce i
     pagamenti da verificare né il controllo prima del POS, e mette gli avvisi del kiosk sul tavolo;
   - un palmare di prima apre i tavoli del kiosk come tavoli normali;
   - una cassa di prima, quando salva un piatto nella composizione del [Menu](../cassa/menu.md),
     riaccende **Ordinabile dal kiosk**: il piatto torna sui kiosk.
5. Sulla TV del monitor in sala ricarica la pagina **una volta a mano** (riaprila, o tasto F5): la
   pagina di prima non sa ricaricarsi da sola. Dagli aggiornamenti successivi si ricarica da sola
   quando il servizio cambia (vedi [Chiamate](../cassa/chiamate.md#il-monitor-in-sala)).
6. In cassa apri Menu ▸ [Kiosk](../cassa/kiosk.md) e controlla la configurazione: quello che prima
   scriveva l'assistenza (kiosk, dispositivi, utenti web) ora si vede e si cambia da lì.
7. Per ultimi **riaccendi i kiosk**: avvia RistoKiosk e, se li avevi spenti, accendi **Kiosk accesi**
   e tocca **Salva**.

Il contrario regge: una cassa nuova con un servizio ancora vecchio non vede i tavoli del kiosk e
lavora come prima.

## Controlli e messaggi

| Messaggio | Causa | Cosa fare |
|---|---|---|
| *Queste credenziali sono di un kiosk: operazione non permessa.* | Con l'utente di un kiosk si è tentata un'operazione che non è del kiosk (per esempio da una cassa collegata con quell'utente). | Collega la cassa con il suo utente; l'utente del kiosk serve solo al kiosk. |
| *Permesso USB della stampante non dato: dallo dalla configurazione del kiosk (scegli la stampante o «Stampa di prova»).* | Su Android la stampante USB non ha ancora il permesso. | Apri la configurazione, scegli la stampante o tocca **Stampa di prova** e tocca **Consenti**. |

## Note

- **Prima del cliente.** Dopo l'installazione prova un ordine completo.
  - Un pagamento con la carta o in contanti a un kiosk che incassa **emette uno scontrino vero**
    sulla stampante fiscale assegnata al kiosk: l'ordine di prova si chiude da solo, con il suo
    documento fiscale. Usa importi piccoli, o una stampante fiscale di prova.
  - Senza scontrino si prova con **Pago alla cassa** (se è acceso), con l'invio in cucina **dopo**: l'ordine
    di prova non va in cucina e si annulla da solo alla scadenza (di partenza 30 minuti).
  - Un ordine di prova rimasto aperto si chiude dalla cassa, in
    [Ordini dal kiosk](../cassa/ordini-kiosk.md): **Annulla l'ordine** per un «paga alla cassa»
    non ancora in cucina, **Annulla e rimborsa** per un ordine pagato al kiosk (il rimborso della
    carta di prova si fa sul POS), il conto con **CHIUDI SENZA DOCUMENTO** per un «paga alla cassa»
    già in cucina. Un ordine da verificare si decide prima con **Il denaro è entrato?**.
- **Uscire dall'app** si può solo dalla configurazione, con **Esci dall'app**: vedi
  [Configurazione](configurazione.md#chiudere-lapp). Per lavorare sul PC o sul tablet va tolto
  anche il blocco del sistema operativo.
- **Il kiosk non legge il QR con la fotocamera**: per i segnaposto col QR serve un lettore 2D
  esterno.

## Vedi anche

- [Configurazione](configurazione.md)
- [Licenza digitale](../introduzione/licenza.md)
- [Impostazioni della cassa](../cassa/impostazioni.md)
