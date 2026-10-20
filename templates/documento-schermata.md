---
title: <Nome della schermata come appare nel titolo>
description: <Una riga: a cosa serve la schermata. Compare nei risultati di ricerca.>
app: <Cassa | Palmare | Monitor di cucina>
percorso: <Menu ▸ Vendita ▸ Mappa della sala ▸ tocco su un tavolo>
pagina: <nome tecnico della pagina, es. ComandaPage — utile per ritrovare il codice>
---

<!--
  TEMPLATE DOCUMENTO-SCHERMATA — Manuale RistoFacile
  Copiare questo file, rinominarlo con lo slug della schermata e compilarlo.
  Regole: non eliminare sezioni; se una sezione non si applica scrivere
  "Non applicabile." Il blocco "In sintesi" e' un ELENCO PUNTATO: senza il
  trattino Markdown le righe si fondono in un paragrafo.
-->

# <Nome della schermata>

<Una o due frasi: cosa permette di fare questa schermata e a chi serve
(cassiere, cameriere, cuoco, titolare). Niente gergo interno.>

!!! info "In sintesi"

    - **Dove si trova:** Menu ▸ <Voce> (oppure: dalla Mappa della sala, tocco su un tavolo)
    - **Chi la usa:** <cassiere / cameriere / cucina / titolare>
    - **Disponibile anche su:** <Palmare (link) / solo cassa>

---

## A cosa serve

<Il contesto operativo: in quale momento del servizio si usa e quale problema
risolve. 3-6 righe. Un esempio concreto vale più di una definizione.>

## Prima di cominciare

- <dato o configurazione necessaria, con link alla schermata dove si imposta>

Se non serve nulla, scrivere: *Nessun prerequisito.*

## La schermata

![<Nome della schermata>](../assets/img/<app>/<slug>.png)

<Descrizione della struttura: le zone della schermata (intestazione, elenco,
pannello laterale, barra in basso) e cosa contiene ciascuna.>

## Campi e indicatori

| Elemento | Descrizione |
|---|---|
| **<Etichetta esatta come appare a video>** | <cosa contiene, come si compila, valori ammessi> |

Nelle schede di inserimento i campi obbligatori sono segnati a video con un
asterisco (**Descrizione \***) e il pulsante **Salva** resta spento finché non
sono compilati.

## Pulsanti e comandi

| Comando | Effetto |
|---|---|
| **<Etichetta del pulsante>** | <cosa succede quando lo tocchi> |

## Come si fa

### <Operazione tipica, es. "Aprire un tavolo e mandare la comanda in cucina">

1. <Passo all'imperativo, un'azione per passo: "Tocca il tavolo.">
2. <...>
3. <Ultimo passo: il risultato che si vede: "Il tavolo diventa rosso (In cucina).">

## Controlli e messaggi

| Messaggio | Causa | Cosa fare |
|---|---|---|
| *<testo esatto del messaggio a video>* | <perché compare> | <come risolvere> |

## Note

<Comportamenti non ovvi, effetti irreversibili, interazioni con le altre app
(palmare, monitor di cucina, stampanti). Se non ce ne sono, scrivere
«Nessuna nota.»>

## Vedi anche

- [<Schermata collegata>](<file>.md)
