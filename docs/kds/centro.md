---
title: Scelta del centro
description: La configurazione del monitor di cucina - collegamento al servizio, scelta del centro di produzione da mostrare e tema chiaro o scuro.
app: Monitor di cucina
percorso: "All'avvio dell'app (dal tabellone: pastiglia Centro)"
pagina: StazionePage
---

# Scelta del centro

La schermata di configurazione del monitor di cucina: si collega il monitor al servizio del
ristorante, si sceglie quale centro di produzione mostra (cucina, pizzeria, bar…) e si sceglie il
tema. È la prima schermata che compare ogni volta che l'app si avvia; da qui si apre il tabellone.

!!! info "In sintesi"

    - **Dove si trova:** all'avvio dell'app; dal tabellone, pastiglia **Centro** in alto a destra
    - **Chi la usa:** installatore, titolare (una volta); chi accende il monitor (ogni giorno, per toccare **APRI MONITOR**)
    - **Disponibile anche su:** solo monitor di cucina

---

## A cosa serve

Si usa davvero una volta, quando si installa lo schermo: si scrive l'indirizzo del servizio e le
credenziali, si sceglie il centro (es. PIZZERIA) e da quel momento il monitor mostra solo i piatti
della pizzeria. Il monitor ricorda la scelta: alle accensioni successive basta toccare
**APRI MONITOR**.

## Prima di cominciare

- L'indirizzo del servizio RistoFacile del locale (es. http://192.168.1.10:8080), con utente e
  password: li fornisce chi ha installato il servizio.
- Almeno un centro di produzione attivo di tipo **Monitor KDS** o **Stampante + KDS**, impostato
  dalla cassa (vedi [Centri di produzione](../cassa/centri-di-produzione.md)).

## La schermata

![Scelta del centro](../assets/img/kds/centro.png)

In alto il titolo **Monitor di cucina** con «Configura questo schermo: a quale server si collega e
quale centro di produzione mostra.». Sotto, tre passi numerati.

A sinistra:

- **1 Connessione al server**: il campo dell'indirizzo («Base URL (es. http://192.168.1.10:8080)»),
  **Utente** e **Password** affiancati, il pulsante **Salva e connetti** e sotto l'esito, in verde
  quando il collegamento riesce (es. «Connesso a http://192.168.1.10:8080 come cucina.»). Se una
  password è già salvata compare «Password gia' salvata: lascia vuoto per non cambiarla.»;
- **3 Aspetto**: tre riquadri **Scuro**, **Chiaro** e **Sistema** («Sistema» segue il dispositivo).

A destra:

- **2 Centro di produzione**: in alto il riquadro della scelta, «Questo monitor mostra i piatti
  di» seguito dal nome del centro scelto e dal suo tipo e codice (es. «Monitor KDS · codice 2»);
  finché non c'è una scelta dice «Nessun centro selezionato» in giallo e «Scegli qui sotto quale
  cucina/bar guarda questo monitor.». Sotto, le tessere dei centri disponibili, con nome e tipo: il
  centro scelto ha il segno di spunta.

In basso a destra il pulsante **APRI MONITOR**; finché non è scelto un centro accanto compare
«Scegli prima un centro di produzione (passo 2).».

## Campi e indicatori

| Elemento | Descrizione |
|---|---|
| **Base URL** | L'indirizzo del servizio RistoFacile, con il numero di porta. |
| **Utente** | L'utente con cui il monitor si collega al servizio. |
| **Password** | La password. Se è già salvata, lasciando il campo vuoto resta quella. |
| **Esito della connessione** | In verde quando il monitor è collegato. |
| **Questo monitor mostra i piatti di** | Il centro scelto, con tipo e codice. |
| **Tessere dei centri** | I centri attivi di tipo **Monitor KDS** o **Stampante + KDS**. |
| **Scuro / Chiaro / Sistema** | Il tema del monitor. Lo scuro è quello di partenza: stanca meno gli occhi nei turni lunghi; in una cucina molto illuminata si legge meglio il chiaro. |

## Pulsanti e comandi

| Comando | Effetto |
|---|---|
| **Salva e connetti** | Salva indirizzo e credenziali, si collega al servizio e carica i centri. |
| **Tessera di un centro** | Sceglie il centro. La scelta resta memorizzata sul monitor. |
| **Scuro / Chiaro / Sistema** | Cambia il tema subito. |
| **APRI MONITOR** | Apre il [tabellone](monitor.md) del centro scelto. È spento finché non scegli un centro. |

## Come si fa

### Installare un monitor nuovo

1. Avvia l'app del monitor di cucina.
2. In **1 Connessione al server** scrivi l'indirizzo del servizio, l'utente e la password.
3. Tocca **Salva e connetti**: sotto compare «Connesso a … come …» in verde e, a destra, le
   tessere dei centri.
4. In **2 Centro di produzione** tocca la tessera del centro (es. CUCINA): compare la spunta e il
   riquadro dice «Questo monitor mostra i piatti di CUCINA».
5. Se serve, scegli il tema in **3 Aspetto**.
6. Tocca **APRI MONITOR**: si apre il tabellone della cucina.

### Cambiare il centro di un monitor

1. Sul tabellone tocca la pastiglia **Centro** in alto a destra.
2. Tocca la tessera del nuovo centro.
3. Tocca **APRI MONITOR**.

## Controlli e messaggi

| Messaggio | Causa | Cosa fare |
|---|---|---|
| *Non configurato: inserisci indirizzo e credenziali del server.* | Il monitor non è ancora collegato a un servizio. | Compila il passo 1 e tocca **Salva e connetti**. |
| *Base URL e utente sono obbligatori.* | Indirizzo o utente vuoti. | Compilali. |
| *La password e' obbligatoria (nessuna password gia' salvata per questa installazione).* | Primo collegamento senza password. | Scrivi la password. |
| *Connessione fallita: …* | Il servizio non risponde o le credenziali sono sbagliate. | Controlla indirizzo, rete e credenziali. |
| *Impossibile caricare le stazioni. (…)* | Il servizio non ha restituito i centri. | Controlla il collegamento e riprova **Salva e connetti**. |
| *Nessun centro da mostrare a monitor. Sul KDS compaiono solo i centri di tipo «Monitor KDS» o «Stampante + KDS»: imposta il tipo del centro dalla Cassa → Centri di produzione.* | Nessun centro adatto al monitor. | Imposta il tipo del centro dalla cassa ([Centri di produzione](../cassa/centri-di-produzione.md)). |
| *Scegli prima un centro di produzione (passo 2).* | Manca la scelta del centro. | Tocca una tessera. |

## Note

- All'avvio l'app si apre sempre su questa schermata, anche se il centro è già scelto: il tabellone
  si apre solo toccando **APRI MONITOR**.
- La scelta del centro e il tema valgono solo per questo monitor.
- Il monitor ha la sua copia di indirizzo e credenziali del servizio, separata da quella della cassa
  e dei palmari.

## Vedi anche

- [Monitor](monitor.md)
- [Monitor di cucina](index.md)
- [Centri di produzione](../cassa/centri-di-produzione.md)
