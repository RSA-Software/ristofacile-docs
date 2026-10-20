---
title: Le tre app di RistoFacile
description: Cassa, palmare e monitor di cucina - a chi serve ciascuna, come lavorano insieme attorno al servizio del locale, chi fa cosa e cosa serve per installarle.
---

# Le tre app di RistoFacile

RistoFacile non è un programma solo: sono tre app, ciascuna pensata per un posto diverso del
locale, che lavorano sugli stessi tavoli e sulle stesse comande. Questa pagina spiega a chi serve
ciascuna e come si passano il lavoro durante il servizio.

## A chi serve ciascuna

| App | Dove sta | Chi la usa | A cosa serve |
|---|---|---|---|
| **Cassa** | PC o tablet al banco | cassiere, titolare | La mappa della sala, le comande, il preconto, il conto con scontrino o fattura, l'asporto, le prenotazioni. È anche l'unica da cui si preparano le anagrafiche: sale e tavoli, menu, articoli, varianti, portate, centri di produzione, operatori, impostazioni. Vedi [Cassa](../cassa/index.md). |
| **Palmare** | telefono o tablet del cameriere | cameriere | La comanda presa al tavolo: apre il tavolo, batte i piatti, li manda in cucina, dà il **VIA** alle portate, fa il preconto e, se serve, incassa. Vedi [Palmare](../palmare/index.md). |
| **Monitor di cucina** | schermo in cucina, pizzeria o bar | cuoco, pizzaiolo, barista | Il tabellone dei piatti da preparare, al posto dei foglietti: **IN CODA**, **IN LAVORAZIONE**, **PRONTO**. Vedi [Monitor di cucina](../kds/index.md). |

## Come lavorano insieme

Al centro c'è il **servizio** RistoFacile, installato su un computer del locale: è lui che conserva
sale, tavoli, menu, comande e conti, e che emette lo scontrino sulla stampante fiscale. Le tre app
non si parlano fra loro: parlano tutte con il servizio, e per questo quello che si fa su un
dispositivo compare entro pochi secondi su tutti gli altri.

```
   Cassa  ─────┐
               │
   Palmare ────┼────  SERVIZIO del locale  ────  stampante fiscale
               │      (sale, menu, comande,
   Monitor ────┘       conti)                ────  stampanti delle cucine
```

Il percorso di un piatto, dalla comanda al conto:

| Momento | Chi | Dove | Cosa succede |
|---|---|---|---|
| 1. Il cliente ordina | cameriere | Palmare o Cassa | Si apre il tavolo e si battono i piatti nella [Comanda](../palmare/comanda.md). |
| 2. Invio in cucina | cameriere | Palmare o Cassa | **INVIA IN CUCINA**: ogni piatto va al **centro di produzione** assegnato a quel piatto nel [Menu](../cassa/menu.md) - la sua stampante, il suo monitor o tutti e due ([Centri di produzione](../cassa/centri-di-produzione.md)). |
| 3. Le portate | cameriere | Palmare o Cassa | Parte subito la prima portata; le successive aspettano che il cameriere tocchi **VIA** ([Portate](../cassa/portate.md)). |
| 4. La preparazione | cucina | Monitor di cucina | Il cuoco tocca il piatto quando lo inizia, quando è pronto e quando esce ([Monitor](../kds/monitor.md)). In sala la portata risulta pronta e poi servita. |
| 5. Il preconto | cameriere o cassiere | Palmare o Cassa | Un'anteprima del conto da portare al tavolo, non fiscale. |
| 6. Il conto | cassiere o cameriere | Cassa o Palmare | Si incassa e il servizio emette lo scontrino (o la fattura); il tavolo torna libero ([Conto](../cassa/conto.md)). |

Il racconto completo, con un tavolo vero, è in [Una serata, dal tavolo al conto](una-serata.md).

## Chi fa cosa e dove

| Operazione | Cassa | Palmare | Monitor di cucina |
|---|:---:|:---:|:---:|
| Entrare con nome e PIN | ● | ● | - |
| Aprire, spostare, unire, separare i tavoli | ● | ● | - |
| Battere la comanda e mandarla in cucina | ● | ● | - |
| Dare il **VIA** a una portata | ● | ● | - |
| Segnare un piatto in lavorazione, pronto, consegnato | - | - | ● |
| Mandare un messaggio alla cucina | ● | ● | riceve |
| Preconto | ● | ● | - |
| Incassare con scontrino o fattura | ● | ● | - |
| Dividere il conto | ● | ● | - |
| Asporto, domicilio, prenotazioni | ● | ● | - |
| Vendita al banco | ● | solo tablet | - |
| Cassa automatica (rendiresto) | ● | - | - |
| Fatture emesse, storico dei conti, statistiche | ● | - | - |
| Anagrafiche (sale, menu, articoli, varianti, portate, operatori…) | ● | - | - |

Le anagrafiche si preparano solo dalla cassa, dove ci sono lo schermo grande e la tastiera: il
palmare le usa ma non le modifica (vedi [Palmare](../palmare/index.md#cosa-non-ce-sul-palmare)).

## Cosa serve

- **Il servizio RistoFacile** installato su un computer del locale, sempre acceso durante il
  servizio. Il suo indirizzo, con utente e password, lo fornisce chi lo ha installato.
- **Una rete** del locale (cavo o Wi-Fi) che colleghi il servizio a tutti i dispositivi, alle
  stampanti delle cucine, alla stampante fiscale e ai terminali POS.
- **La cassa** su un PC o tablet **Windows**.
- **Il palmare** su un telefono o tablet **Android** o su un **iPhone**.
- **Il monitor di cucina** su uno schermo **Windows** o su un **tablet**.
- **La licenza digitale**: la cassa e ogni palmare occupano un posto della licenza; il monitor di
  cucina è un modulo aggiuntivo della licenza della cassa (vedi [Licenza digitale](licenza.md)).
  Per attivarla serve Internet; per lavorare basta la rete del locale.

L'ordine in cui installare e configurare le tre app è descritto in
[Prima configurazione](prima-configurazione.md).
