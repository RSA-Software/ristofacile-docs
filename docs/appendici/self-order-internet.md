---
title: Pubblicare il self order su internet
description: Per chi installa il servizio - la porta pubblica del self order, l'indirizzo https, il proxy o il tunnel, Nexi per i pagamenti dal telefono e la licenza.
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
separando più indirizzi con una virgola (per un proxy sullo stesso PC del servizio, di solito
`127.0.0.1`). Senza proxy lascia il campo vuoto.

<!-- DA VERIFICARE: con il tunnel sullo stesso PC, oltre a 127.0.0.1 serve anche ::1? -->

## Pagamento dal telefono (Nexi)

Il pagamento dal telefono usa Nexi XPay con i link di pagamento: il cliente paga sulla pagina di
Nexi e il locale non vede mai la carta.

- Le credenziali (indirizzo del servizio di Nexi e chiave API) stanno nel file `cfg\nexi.json` del
  servizio, lo stesso usato dagli altri pagamenti Nexi della suite. Senza, l'interruttore
  **Pagamento dal telefono** non si accende.
- Per le prove si usa l'ambiente di prova di Nexi (sandbox); in produzione l'indirizzo e la chiave
  del locale.
- Il PC del servizio deve avere l'**ora italiana**: la scadenza dei link di pagamento (15 minuti) si
  calcola sull'ora del PC.
- I rimborsi (un pagamento arrivato dopo la chiusura del conto) si fanno dal portale di Nexi.

<!-- DA VERIFICARE: da quale maschera di Facile si compilano le credenziali di Nexi, e l'indirizzo di produzione di Nexi XPay. -->

## Licenza

Il self order, con il pagamento dal telefono, è un modulo della licenza digitale (**Self order**),
come il monitor di cucina. Vedi [Licenza digitale](../introduzione/licenza.md).

## Controllo finale

1. Da un telefono **fuori dalla rete del locale** (rete mobile, Wi-Fi spento) apri l'indirizzo
   pubblico seguito da un codice di tavolo, oppure inquadra un cartoncino.
2. Si deve vedere il menu del locale, con il nome del tavolo in alto.
3. Con il tavolo aperto dalla cassa, manda un ordine di prova: sulla cassa compare l'avviso
   *… ha ordinato dal telefono*.
