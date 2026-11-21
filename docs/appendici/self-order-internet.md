---
title: Pubblicare il self order su internet
description: Per chi installa il servizio - la porta pubblica del self order, l'indirizzo https, il proxy o il tunnel, i fornitori del pagamento dal telefono (Nexi XPay, SumUp, Revolut, Dojo) e la licenza.
---

# Pubblicare il self order su internet

Questa pagina è per **chi installa il servizio** RistoFacile nel locale. Il personale del locale usa
invece la schermata [Self order](../cassa/self-order.md) della cassa.

I telefoni dei clienti non stanno nella rete del locale: arrivano da internet, spesso dalla rete
mobile. Per questo il self order ha bisogno di un indirizzo pubblico in `https` che porti al servizio
del locale, ed è l'unica cosa del servizio che va resa raggiungibile da fuori.

## La porta pubblica

Il servizio apre per il self order una **porta pubblica**, separata da quelle che usano cassa,
palmare e monitor di cucina. Su quella porta il servizio risponde solo alle pagine e alle richieste
dei telefoni (menu, ordine, conto, pagamento) e al menu online, e accetta solo richieste piccole.

- Si sceglie nel file di configurazione dell'istanza del servizio, alla voce `PortaPubblica` (un
  numero di porta; `0` = spenta).
- Deve essere diversa dalle porte HTTP e HTTPS del servizio: se coincide, il servizio non parte e
  scrive *La porta pubblica del self order deve essere diversa dalle porte HTTP e HTTPS.*
- La porta pubblica parla in `http`: l'`https` lo mette il proxy o il tunnel davanti (vedi sotto).

!!! warning "Su internet solo la porta pubblica"

    Le porte HTTP e HTTPS normali del servizio danno accesso a tutto l'archivio del locale e
    accettano invii grandi (caricamenti, sincronizzazioni): **non vanno mai** rese raggiungibili da
    internet, né aperte nel router né inoltrate dal proxy.

## L'indirizzo https

Davanti alla porta pubblica serve qualcosa che risponda in `https` con un certificato valido e
inoltri le richieste alla porta pubblica del servizio. Va bene uno dei due:

- un **reverse proxy** sul PC del servizio o nella rete del locale (per esempio IIS, nginx o
  Caddy), raggiunto da un indirizzo IP pubblico statico e da un nome a dominio con il suo
  certificato;
- un **tunnel** (per esempio Cloudflare Tunnel), che non richiede né IP statico né porte aperte nel
  router.

L'indirizzo così ottenuto, per esempio `https://ordina.trattoria.it`, è quello da scrivere in
**Indirizzo pubblico** nella schermata [Self order](../cassa/self-order.md): finisce in tutti i QR,
quindi va deciso prima di stampare i cartoncini.

### Proxy fidati

Il servizio limita le richieste per indirizzo del cliente, per esempio quante volte un telefono
può chiamare il cameriere. Dietro un proxy o un tunnel tutte le richieste arrivano dall'indirizzo
del proxy: per riconoscere i clienti il servizio legge l'indirizzo vero che il proxy gli passa, ma
**solo** se la richiesta arriva da un proxy che conosce.

Scrivi in **Proxy fidati** l'indirizzo da cui il proxy o il tunnel si collega al servizio,
separando più indirizzi con una virgola. Per un proxy sullo stesso PC del servizio scrivi
`127.0.0.1, ::1`: il servizio riconosce solo gli indirizzi scritti qui, così come sono, e il proxy
può collegarsi con l'indirizzo locale IPv4 (`127.0.0.1`) o con quello IPv6 (`::1`). Senza proxy
lascia il campo vuoto.

## Pagamento dal telefono

Il pagamento dal telefono, e quello dell'asporto online, passa da un link di pagamento di uno di
questi quattro fornitori: il cliente paga sulla pagina del fornitore e il locale non vede mai la
carta. Il locale ne sceglie uno, con il suo conto presso il fornitore.

| Fornitore | Cosa serve | Dove si prende la chiave | Prove |
|---|---|---|---|
| **Nexi XPay** | Chiave API | Back-office XPay, *Impostazioni ▸ Chiavi API* | Ambiente di prova separato, con la sua chiave |
| **SumUp** | Chiave API e codice esercente | Portale di SumUp | Un indirizzo solo: si prova con la chiave di prova |
| **Revolut** | Chiave segreta | Portale di Revolut Business | Ambiente di prova separato, con la sua chiave |
| **Dojo** | Chiave segreta | Portale di Dojo | Un indirizzo solo: la chiave di prova comincia con `sk_sandbox_`, quella vera con `sk_prod_` |

<!-- DA VERIFICARE: in quale sezione del back-office di Nexi XPay (e del suo ambiente di prova) si crea la chiave API: «Impostazioni ▸ Chiavi API» non è stato controllato sul portale. -->
<!-- DA VERIFICARE: in quale sezione del portale di SumUp si crea la chiave API e dove si legge il codice esercente. -->
<!-- DA VERIFICARE: in quale sezione del portale di Revolut Business (e del suo ambiente di prova) si legge la chiave segreta per i pagamenti online. -->
<!-- DA VERIFICARE: in quale sezione del portale di Dojo si crea la chiave segreta (sk_prod_ / sk_sandbox_). -->

### Dove si scrivono le chiavi

- **Dalla cassa**: Menu ▸ Impostazioni ▸ **Self order**, linguetta **Pagamento** (vedi
  [Scegliere il fornitore del pagamento](../cassa/self-order.md#scegliere-il-fornitore-del-pagamento)).
  Serve il permesso **Pagamenti dal telefono**. Le chiavi si scrivono ma non si rileggono: la casella
  dice solo *impostata*.
- **Da Facile**: *Utility ▸ Impostazioni Sistemi di Pagamento Elettronico*, con le stesse
  credenziali.

In tutti e due i casi le chiavi finiscono negli stessi file del servizio, usati anche dagli altri
pagamenti della suite: `cfg\nexi.json`, `cfg\sumup.json`, `cfg\revolut.json` e `cfg\dojo.json`. Se
Facile e il servizio sono installati in cartelle diverse, il file scritto da Facile va copiato nella
cartella `cfg` del servizio. Un file che manca, vuoto, rovinato o con le credenziali a metà vale
come fornitore non configurato: **Pagamento dal telefono** e **Asporto online acceso** non si
accendono.

Gli indirizzi dei fornitori li scrive la cassa al **Salva**, secondo **Ambiente di prova**:

| Fornitore | Produzione | Prova |
|---|---|---|
| Nexi XPay | `https://xpay.nexigroup.com/api/phoenix-0.0/psp/api` | `https://xpaysandbox.nexigroup.com/api/phoenix-0.0/psp/api` |
| SumUp | `https://api.sumup.com` | lo stesso |
| Revolut | `https://merchant.revolut.com/api` | `https://sandbox-merchant.revolut.com/api` |
| Dojo | `https://api.dojo.tech` | lo stesso |

Un indirizzo diverso, scritto da Facile, al primo **Salva** dalla cassa diventa uno di questi.

### Cambiare fornitore

Il fornitore nuovo vale per i pagamenti che partono dopo il **Salva**. Quelli già partiti si
chiudono, si annullano e scadono con il fornitore di prima, che deve restare configurato finché non
sono finiti: al massimo 15 minuti, la durata di un link. Se intanto le sue chiavi spariscono, quei
pagamenti restano in sospeso.

### Come si comportano i fornitori

- **Lingua.** La pagina di Nexi XPay segue la lingua scelta sul telefono; quelle di SumUp, Revolut e
  Dojo sono nella lingua che decide il fornitore.
- **Rinuncia.** Nexi XPay e Dojo hanno un indirizzo di rinuncia: il cliente che rinuncia torna al
  menu del locale e il pagamento si annulla. SumUp e Revolut no: il cliente torna indietro da sé e
  tocca **Ho rinunciato al pagamento**, oppure il link scade dopo 15 minuti.
- **Pagamenti da confermare.** Con Revolut e Dojo un pagamento autorizzato ma non ancora incassato
  dal fornitore resta *in verifica*: conta come pagato solo quando il fornitore lo incassa. Anche una
  risposta del fornitore che il servizio non capisce vale *in verifica*, mai *rifiutato*: il link
  non si annulla e la quota non si libera per sbaglio.

### Ora del PC e rimborsi

- Il PC del servizio deve avere l'**ora italiana**: la scadenza dei link di pagamento (15 minuti) si
  calcola sull'ora del PC.
- I rimborsi (per esempio un pagamento arrivato dopo la chiusura del conto) si fanno dal portale del
  fornitore con cui il cliente ha pagato: l'avviso 💶 della cassa lo nomina.

## Licenza

Il self order, con il pagamento dal telefono, è un modulo della licenza digitale (**Self order**),
come il monitor di cucina. Vedi [Licenza digitale](../introduzione/licenza.md).

## Controllo finale

1. Da un telefono **fuori dalla rete del locale** (rete mobile, Wi-Fi spento) apri l'indirizzo
   pubblico seguito da un codice di tavolo, oppure inquadra un cartoncino.
2. Si deve vedere il menu del locale, con il nome del tavolo in alto.
3. Con il tavolo aperto dalla cassa, manda un ordine di prova: sulla cassa compare l'avviso
   *… ha ordinato dal telefono*.
