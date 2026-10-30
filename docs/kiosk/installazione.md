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
creato **un utente web apposta**, che non sia quello di una cassa, e il suo nome va scritto
nell'elenco degli **utenti dei kiosk** nella configurazione dei kiosk sul servizio.

1. Crea l'utente web del kiosk, come gli utenti delle casse.
2. Scrivi il suo nome utente fra gli utenti dei kiosk: nel file della configurazione dei kiosk sul
   servizio è la voce `utenti`, un elenco di nomi (per esempio `["KIOSK"]`). Le maiuscole non
   contano.
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

!!! note "Per ora l'elenco lo scrive l'assistenza"
    La cassa non ha ancora la schermata dei kiosk: arriverà con un prossimo aggiornamento. Fino ad
    allora gli utenti dei kiosk, come il numero e il dispositivo di ogni kiosk, si scrivono nella
    configurazione dei kiosk sul servizio.

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
  - La cassa oggi non apre gli ordini del kiosk (vedi
    [Pagamenti](pagamenti.md#un-pagamento-da-verificare)): un ordine di prova rimasto aperto (da
    verificare, con lo scontrino da emettere, o «paga alla cassa» con l'invio **subito**) non si
    chiude dalla cassa.
  <!-- DA VERIFICARE: prima dell'aggiornamento della cassa (Piano 8), chi e come chiude un ordine di prova del kiosk rimasto aperto (oggi solo con la rotta del servizio, come nel collaudo). -->
- **Uscire dall'app** si può solo dalla configurazione, con **Esci dall'app**: vedi
  [Configurazione](configurazione.md#chiudere-lapp). Per lavorare sul PC o sul tablet va tolto
  anche il blocco del sistema operativo.
- **Il kiosk non legge il QR con la fotocamera**: per i segnaposto col QR serve un lettore 2D
  esterno.

## Vedi anche

- [Configurazione](configurazione.md)
- [Licenza digitale](../introduzione/licenza.md)
- [Impostazioni della cassa](../cassa/impostazioni.md)
