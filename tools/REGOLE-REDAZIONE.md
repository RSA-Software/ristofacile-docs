# Regole di redazione del manuale RistoFacile

Queste regole valgono per chiunque scriva una scheda (persona o agente).

## Fonti

- I sorgenti sono in `C:\RSA.NET\RistoFacile` (leggere prima il suo `CLAUDE.md`):
  - cassa: `Pages/`, `AppShell.xaml`, `MauiProgram.cs`
  - palmare: `RistoApp/Pages/` (telefono) e `RistoApp/Pages/Vendita/Tablet/` (tablet)
  - monitor di cucina: `RistoKds/Pages/`
  - logica condivisa: `RistoCore/PageModels/` (un PageModel per pagina), `RistoCore/Services/`
- Il backend è `C:\RSA.NET\FacileWepApiServices` (rotte `api/v1/risto/*`): da leggere
  solo quando serve sapere cosa fa davvero il servizio (es. cosa succede alla chiusura del conto).
- Le etichette si prendono dallo XAML (`Text=`, `Placeholder=`, `Title=`), **esatte**,
  maiuscole comprese. I testi costruiti a runtime stanno nel PageModel.
- I messaggi a video stanno nei PageModel: `Avvisi.Attenzione(...)`, `Avvisi.Errore(...)`,
  `Avvisi.ConfermaAsync(...)`, `DisplayAlert`, `StatusMessage = ...`. Riportarli **esatti**.

## Regola fondamentale

Il manuale è per l'utente finale (cassiere, cameriere, cuoco, titolare). Nel testo
**mai** nomi di classi, proprietà, rotte, tabelle o campi del database. L'unico
riferimento tecnico ammesso è il campo `pagina` del front matter.

- ✅ «Il numero di coperti si propone uguale a quello del tavolo.»
- ❌ «`NumeroPersoneText` è inizializzato da `cmd_coperti`.»

## Non inventare

Ogni affermazione deve poggiare su qualcosa letto nel codice. Quando il significato
operativo non si ricava, inserire

    <!-- DA VERIFICARE: <domanda precisa> -->

e andare avanti. Una domanda aperta si recupera; un'affermazione inventata no.
Le parti marcate «GAP ONESTO» nei commenti del codice sono funzioni volutamente
incomplete: vanno dette all'utente come limiti («al momento non è possibile…»), non taciute.

## Stile

- italiano, registro professionale, **tu** («Tocca **Invia**»);
- le app sono touch: si **tocca**, non si clicca; sulla cassa Windows vale anche il mouse;
- etichette di campi e pulsanti in **grassetto**, esatte;
- procedure = elenchi numerati, un'azione per passo, l'ultimo passo dice cosa si vede;
- percorsi con ▸ (Menu ▸ Sale e tavoli);
- `!!! warning` solo per effetti irreversibili o comportamenti non ovvi;
- niente frasi di riempimento.

## Nomi delle tre app

- **Cassa** (l'app RistoFacile, sul PC o tablet al banco)
- **Palmare** (l'app RistoApp, sul telefono o tablet dei camerieri)
- **Monitor di cucina** (l'app RistoKds, lo schermo nei centri di produzione)
- **Servizio** = il servizio RistoFacile installato nel locale, a cui si collegano tutte e tre.

## Schermate (immagini)

- Percorso: `docs/assets/img/<cassa|palmare|kds|introduzione>/<slug>.png`, con lo slug
  della pagina; più immagini per pagina: `<slug>-<parte>.png` (es. `conto-pagamento.png`).
- Nella pagina il riferimento si scrive anche se l'immagine non c'è ancora.
- Le schermate del telefono si scrivono con la classe `telefono`:
  `![Sala](../assets/img/palmare/sala.png){ .telefono }`

## Struttura

Template: `templates/documento-schermata.md`. Non aggiungere, togliere o riordinare
le sezioni. Una schermata che si apre da più punti ha una pagina sola.
