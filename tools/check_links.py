#!/usr/bin/env python3
"""Sprawdza odnośniki we wszystkich plikach .md repozytorium.

1. Odnośniki lokalne (względne) — czy plik istnieje.
2. Odnośniki do PDF-ów Hallidaya na serwerze AGH — czy numer strony (#page=N) mieści się w pliku.
3. Odnośniki zewnętrzne — czy serwer odpowiada. Każdy adres (bez części po #) jest sprawdzany raz.
   Błąd:        404/410, nieistniejąca domena.
   Ostrzeżenie: przekroczony czas, 403/429, błędy 5xx (serwery bywają chwilowo niedostępne
                albo blokują automatyczne zapytania) — warto sprawdzić ręcznie, ale nie przerywa testu.

Użycie: python3 tools/check_links.py [katalog] [--tylko-lokalne]
"""
import glob
import os
import re
import socket
import sys
import time
import urllib.error
import urllib.request
from concurrent.futures import ThreadPoolExecutor

root = next((a for a in sys.argv[1:] if not a.startswith("--")), os.path.join(os.path.dirname(__file__), ".."))
tylko_lokalne = "--tylko-lokalne" in sys.argv
os.chdir(root)

# liczba stron w skanach wyd. 1 na serwerze AGH (Resnick_1.pdf … Resnick_5.pdf)
AGH_STRONY = {1: 366, 2: 330, 3: 137, 4: 226, 5: 274}
LINK = re.compile(r"\]\((<?)([^)\s>]+)>?\)")
UA = "Mozilla/5.0 (link-check; https://github.com/kanthakdominik/Fizyka)"

bledy, ostrzezenia, zewnetrzne = [], [], {}
for plik in sorted(glob.glob("**/*.md", recursive=True)):
    tekst = open(plik, encoding="utf-8").read()
    tekst = re.sub(r"```.*?```", "", tekst, flags=re.S)          # pomijamy bloki kodu
    for _, cel in LINK.findall(tekst):
        if cel.startswith(("http://", "https://")):
            m = re.search(r"Resnick_(\d)\.pdf#page=(\d+)", cel)
            if m and int(m.group(2)) > AGH_STRONY[int(m.group(1))]:
                bledy.append(f"{plik}: strona {m.group(2)} poza skanem t. {m.group(1)} ({AGH_STRONY[int(m.group(1))]} stron)")
            zewnetrzne.setdefault(cel.split("#")[0], []).append(plik)
        elif cel.startswith(("#", "mailto:")):
            continue
        else:
            sciezka = os.path.normpath(os.path.join(os.path.dirname(plik), cel.split("#")[0]))
            if not os.path.exists(sciezka):
                bledy.append(f"{plik}: brak pliku {cel}")


def sprawdz(url):
    for proba in range(3):
        for metoda in ("HEAD", "GET"):
            req = urllib.request.Request(url, method=metoda, headers={"User-Agent": UA, "Accept-Language": "pl,en"})
            try:
                with urllib.request.urlopen(req, timeout=30) as r:
                    return url, r.status, ""
            except urllib.error.HTTPError as e:
                if metoda == "HEAD" and e.code in (403, 404, 405, 501):
                    continue                                       # część serwerów nie obsługuje HEAD
                if e.code in (429, 500, 502, 503, 504) and proba < 2:
                    time.sleep(5*(proba + 1))
                    break
                return url, e.code, ""
            except urllib.error.URLError as e:
                if isinstance(e.reason, socket.gaierror):
                    return url, None, "nieistniejąca domena"
                if proba < 2:
                    time.sleep(5)
                    break
                return url, None, str(e.reason)
            except Exception as e:                                 # przekroczony czas itp.
                if proba < 2:
                    time.sleep(5)
                    break
                return url, None, type(e).__name__
    return url, None, "brak odpowiedzi"


if not tylko_lokalne:
    with ThreadPoolExecutor(max_workers=8) as ex:
        for url, kod, opis in ex.map(sprawdz, sorted(zewnetrzne)):
            gdzie = zewnetrzne[url][0] + (f" (+{len(zewnetrzne[url]) - 1})" if len(zewnetrzne[url]) > 1 else "")
            if kod in (404, 410) or opis == "nieistniejąca domena":
                bledy.append(f"{gdzie}: {url} → {kod or opis}")
            elif kod is None or kod >= 400:
                ostrzezenia.append(f"{gdzie}: {url} → {kod or opis}")

for o in ostrzezenia:
    print("OSTRZEŻENIE", o)
for b in bledy:
    print("BŁĄD", b)
print(f"adresy zewnętrzne: {len(zewnetrzne)}, błędy: {len(bledy)}, ostrzeżenia: {len(ostrzezenia)}")
if os.environ.get("GITHUB_ACTIONS"):                               # zbiorcze adnotacje widoczne w podsumowaniu przebiegu
    for rodzaj, lista in (("error", bledy), ("warning", ostrzezenia)):
        if lista:
            print(f"::{rodzaj} title=Odnośniki ({len(lista)})::" + "%0A".join(lista))
sys.exit(1 if bledy else 0)
