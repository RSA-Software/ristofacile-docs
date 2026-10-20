# Strumenti di cattura delle schermate

Usati il 20/10/2026 per la prima passata. I percorsi in testa agli script puntano alla cartella di
lavoro di quella sessione: correggerli prima di riusarli.

- `uia.ps1` — pilotaggio delle app MAUI su Windows con UI Automation (si include con `. .\uia.ps1`):
  `Avvia cassa|palmare|kds`, `Win`, `Tocca <testo>`, `Scrivi`, `Scegli`, `ClicXY`, `F <nome>` (foto
  sul rettangolo DWM). Sui `Button` usa Invoke, sui riquadri con tocco il clic vero del mouse.
  ⚠ In PowerShell `$t` e `$T` sono la stessa variabile: non usare `$t` negli script che includono uiautomation.
  ⚠ Invoke via UIA sui pulsanti +/− della finestra «Righe da separare» ha chiuso la cassa: lì usare `ClicXY`.
- `tel.py` — telefono/emulatore Android via adb + uiautomator (`testi`, `nodi`, `tocca`, `tocca=`,
  `campo <indice> <valore>`, `foto`). Il dispositivo si sceglie con la variabile `TEL`.
- `ocr/` — OCR di Windows (`Windows.Media.Ocr`): stampa `x y w h testo` per riga.
- `pubblica-immagini.py` — copia le catture in `docs/assets/img`, oscura nomi e dati sensibili
  trovati con l'OCR, riduce (cassa 1600, telefono 540) e crea i segnaposto per le immagini mancanti.
- `foglio.py` — foglio provini per controllare molte catture in una volta.
- `menu-casa.ps1` — compone dalla cassa il menu di prova «MENU DELLA CASA».

Emulatore: `pixel_7_-_api_34`; per l'italiano `adb shell cmd locale set-app-locales com.rsa.ristoapp --locales it-IT`.
L'APK Debug installabile va compilato con `-p:EmbedAssembliesIntoApk=true` (quello di VS usa il Fast Deployment).
