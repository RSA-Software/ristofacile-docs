---
name: manuale-ristofacile
description: Scrive o aggiorna una scheda del manuale utente di RistoFacile (cassa, palmare, monitor di cucina) leggendo i sorgenti MAUI e producendo una pagina Markdown per il sito MkDocs. Usare quando si chiede di documentare una schermata di RistoFacile, RistoApp o RistoKds, o di aggiornare il manuale dopo una modifica al codice.
---

# Documentare una schermata di RistoFacile

1. Leggi `tools/REGOLE-REDAZIONE.md` (obbligatorio) e il template `templates/documento-schermata.md`.
2. Trova le fonti in `C:\RSA.NET\RistoFacile`: lo XAML della pagina (etichette esatte), il
   code-behind, il PageModel in `RistoCore/PageModels/` (comandi, messaggi `Avvisi.*`), i servizi
   chiamati e, se serve, il backend `C:\RSA.NET\FacileWepApiServices` (`api/v1/risto/*`).
3. Scrivi la scheda in `docs/<cassa|palmare|kds>/<slug>.md` senza cambiare l'ordine delle sezioni;
   dove il codice non basta lascia `<!-- DA VERIFICARE: … -->`.
4. Mettila nel `nav` di `mkdocs.yml` nella posizione che la schermata ha nell'app (cassa: menu
   laterale; palmare: linguette in basso).
5. Le schermate: `docs/assets/img/<app>/<slug>.png`; se non c'è ancora l'immagine, il riferimento si
   scrive lo stesso e lo script dei segnaposto la crea.
6. Controlla: `mkdocs build --strict`, `tools/controlla-intestazioni.py`, poi rigenera
   `tools/appendice-messaggi.py` e `tools/domande-aperte.py`.

Quando possibile, **prova la schermata sull'app vera** prima di descriverla: il codice dice cosa
dovrebbe succedere, l'app cosa succede. Le prove si fanno sul servizio di prova e i conti si chiudono
con **CHIUDI SENZA DOCUMENTO**, mai con INCASSA E STAMPA (emette uno scontrino fiscale vero).
