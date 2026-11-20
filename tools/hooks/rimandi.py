"""Pagine spostate o rinominate: il vecchio indirizzo resta e rimanda a quello nuovo.

Chi aveva salvato o inoltrato il link (email, segnalibri, motori di ricerca) non trova una pagina vuota. Per aggiungere
un rimando: vecchio indirizzo del sito (cartella, con la barra finale) -> pagina Markdown di destinazione. La build fallisce
se la destinazione non esiste piu'.
"""
import html
import os

from mkdocs.exceptions import PluginError

RIMANDI = {
    "cassa/menu-online/": "cassa/sito-menu.md",  # 20/11/2026: Menu online diventato Sito del menu
}

_url = {}


def on_files(files, config):
    _url.clear()
    for f in files.documentation_pages():
        _url[f.src_uri] = f.url
    return files


def on_post_build(config):
    errori = []
    for vecchio, pagina in sorted(RIMANDI.items()):
        if pagina not in _url:
            errori.append(f"{vecchio}: la pagina {pagina} non c'e'")
            continue
        risalita = "../" * vecchio.strip("/").count("/") + "../"
        destinazione = risalita + _url[pagina]
        cartella = os.path.join(config.site_dir, *vecchio.strip("/").split("/"))
        os.makedirs(cartella, exist_ok=True)
        d = html.escape(destinazione, quote=True)
        with open(os.path.join(cartella, "index.html"), "w", encoding="utf-8", newline="\n") as f:
            f.write(
                "<!doctype html>\n<html lang=\"it\"><head><meta charset=\"utf-8\">\n"
                "<meta name=\"robots\" content=\"noindex\">\n"
                "<title>Pagina spostata</title>\n"
                f"<link rel=\"canonical\" href=\"{d}\">\n"
                f"<meta http-equiv=\"refresh\" content=\"0; url={d}\">\n"
                f"<script>location.replace({destinazione!r});</script>\n"
                f"</head><body><a href=\"{d}\">La pagina si e' spostata: vai qui</a></body></html>\n"
            )
    if errori:
        raise PluginError("rimandi verso pagine che non ci sono:\n  " + "\n  ".join(errori))
