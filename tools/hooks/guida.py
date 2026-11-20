"""Guida contestuale (F1) delle app RistoFacile.

Le app aprono <sito>/guida/<codice>/ (codici in RistoCore/Services/Guida/CodiciGuida.cs). Questo hook legge guida.yml
(codice: pagina.md oppure pagina.md#ancora), verifica a ogni build che pagina e ancora esistano e scrive
site/guida/<codice>/index.html, un rimando immediato alla pagina. Se il manuale si riorganizza si cambia la destinazione
in guida.yml: le casse installate continuano ad aprire lo stesso indirizzo.
"""

import html
import os
import re

import yaml
from mkdocs.exceptions import PluginError

FORMA_CODICE = re.compile(r"^[a-z0-9-]+(\.[a-z0-9-]+)*$")

_mappa = {}   # codice -> (pagina .md, ancora o "")
_url = {}     # pagina .md -> url, per tutte le pagine (anche quelle che --dirty non ricostruisce)
_ids_pagina = {}  # pagina .md -> id dell'indice, solo per le pagine ricostruite in questa build
_guida_yml = None


def on_config(config):
    global _guida_yml
    _mappa.clear()
    _url.clear()
    _ids_pagina.clear()
    percorso = os.path.join(os.path.dirname(config.config_file_path), "guida.yml")
    _guida_yml = percorso
    with open(percorso, encoding="utf-8") as f:
        dati = yaml.safe_load(f) or {}
    for codice, destinazione in dati.items():
        codice = str(codice)
        if not FORMA_CODICE.match(codice):
            raise PluginError(f"guida.yml: codice non valido «{codice}» (solo a-z, 0-9, - a gruppi separati da .)")
        pagina, _, ancora = str(destinazione).partition("#")
        _mappa[codice] = (pagina, ancora)
    return config


def on_serve(server, config, builder):
    # guida.yml sta fuori da docs/: senza questo mkdocs serve non ricostruisce quando cambia.
    if _guida_yml:
        server.watch(_guida_yml)
    return server


def on_files(files, config):
    for f in files.documentation_pages():
        _url[f.src_uri] = f.url
    return files


def _ids(voci):
    for voce in voci:
        yield voce.id
        yield from _ids(voce.children)


def on_page_content(html_pagina, page, config, files):
    _ids_pagina[page.file.src_uri] = set(_ids(page.toc))
    return html_pagina


def on_post_build(config):
    errori = []
    for codice, (pagina, ancora) in sorted(_mappa.items()):
        if pagina not in _url:
            errori.append(f"{codice}: la pagina {pagina} non c'e'")
            continue
        url = _url[pagina]
        # Con --dirty le pagine non ricostruite non hanno l'indice: l'ancora si verifica solo su quelle ricostruite.
        ids = _ids_pagina.get(pagina)
        if ancora and ids is not None and ancora not in ids:
            errori.append(f"{codice}: in {pagina} manca il paragrafo #{ancora}")
            continue
        destinazione = "../../" + url + ("#" + ancora if ancora else "")
        cartella = os.path.join(config.site_dir, "guida", codice)
        os.makedirs(cartella, exist_ok=True)
        d = html.escape(destinazione, quote=True)
        with open(os.path.join(cartella, "index.html"), "w", encoding="utf-8", newline="\n") as f:
            f.write(
                "<!doctype html>\n<html lang=\"it\"><head><meta charset=\"utf-8\">\n"
                "<meta name=\"robots\" content=\"noindex\">\n"
                f"<title>Guida: {html.escape(codice)}</title>\n"
                f"<link rel=\"canonical\" href=\"{d}\">\n"
                f"<meta http-equiv=\"refresh\" content=\"0; url={d}\">\n"
                f"<script>location.replace({destinazione!r});</script>\n"
                f"</head><body><a href=\"{d}\">Vai alla guida</a></body></html>\n"
            )
    if errori:
        raise PluginError("guida.yml rimanda a pagine o paragrafi che non ci sono:\n  " + "\n  ".join(errori))
