# Fizyka — od matury rozszerzonej do pierwszego roku politechniki

Otwarta, samodzielna ścieżka nauki fizyki na dwóch poziomach: **matury rozszerzonej** oraz **kursu fizyki z pierwszego roku studiów technicznych** (z rachunkiem różniczkowym i całkowym). Repozytorium jest pomyślane jako darmowa pomoc do nauki przed maturą i studiami, w trakcie pierwszych semestrów albo do odświeżenia wiedzy po latach.

Układ działów opiera się na dwóch podręcznikach akademickich dostępnych po polsku:

- **OpenStax, *Fizyka dla szkół wyższych*, t. 1–3** — darmowe polskie wydanie *University Physics*. Każdy temat linkuje bezpośrednio do właściwego paragrafu.
- **Halliday, Resnick, Walker, *Podstawy fizyki*, t. 1–5** — dokładniejszy i bardziej szczegółowy wykład. Każdy temat podaje paragraf i stronę w wydaniu PWN 2015 oraz w pierwszym wydaniu (2003), z linkiem otwierającym PDF udostępniony na serwerze AGH od razu na właściwej stronie.

Zasady:

- **Notatki, przykłady i zadania** są napisane po polsku (treść własna repozytorium).
- **Źródła zewnętrzne są polskie**: dwa podręczniki powyżej, materiały CKE do matury, polskie wersje symulacji. Kilka materiałów uzupełniających, które nie mają polskiego odpowiednika, jest wyraźnie oznaczonych jako anglojęzyczne.
- Linki były sprawdzane przy dodawaniu. Jeśli któryś przestanie działać, zgłoś to w Issues.

* * *

## Jak korzystać z repozytorium

1. Przeczytaj [ROADMAP.md](ROADMAP.md) — kolejność modułów, zależności, trzy ścieżki nauki (matura, politechnika, most między nimi) i szacowany czas.
2. Przejrzyj [RESOURCES.md](RESOURCES.md) — podręczniki, materiały maturalne i symulacje, do których odwołują się moduły.
3. Zainstaluj narzędzia z [TOOLS.md](TOOLS.md) (wszystkie darmowe; do doświadczeń wystarczy smartfon).
4. Przerabiaj moduły po kolei. Każdy temat ma ten sam układ (pełny opis w [docs/SZABLON-TEMATU.md](docs/SZABLON-TEMATU.md)):

| Sekcja | Co zawiera |
|---|---|
| **Czytaj** | Paragraf w *Fizyce dla szkół wyższych* (link), w *Podstawach fizyki* wyd. 2015 (tom, paragraf, strona) i w wyd. 1 (link do właściwej strony PDF-u) |
| **Po co to jest** | Gdzie temat wraca w dalszej fizyce i w technice |
| **Teoria w pigułce** | Najważniejsze pojęcia i prawa, bez lania wody |
| **Wzory i założenia** | Wzory razem z warunkami, w których obowiązują |
| **Przykład rozwiązany** | Pełne rozwiązanie krok po kroku; tam gdzie to ma sens — także wersja z pochodną lub całką |
| **Typowe pułapki** | Błędy, które najczęściej kosztują punkty na maturze i kolokwium |
| **Doświadczenie / symulacja** | Pomiar smartfonem (phyphox), symulacja PhET albo krótki program w Pythonie |
| **Zadania** | A — poziom maturalny, B — poziom akademicki; odpowiedzi ukryte pod `<details>` |
| **Źródła** | Konkretne rozdziały i strony do pogłębienia |

5. Postęp odznaczaj w checklistach (`- [ ]` → `- [x]`) we własnym forku.

### Oznaczenia poziomu

| Znak | Znaczenie |
|---|---|
| 🟢 | Zakres matury rozszerzonej — bez pochodnych i całek |
| 🔵 | Zakres pierwszego roku studiów — z rachunkiem różniczkowym i całkowym |
| 🟢🔵 | Temat maturalny, który na studiach jest pogłębiany i wyprowadzany z użyciem rachunku |

* * *

## Mapa modułów

| # | Moduł | Poziom | Odpowiednik na studiach | Status |
|---|---|---|---|---|
| 00 | [Narzędzia matematyczne fizyka](modules/00-narzedzia-matematyczne) | 🟢🔵 | Analiza matematyczna I (fragmenty), wstęp do Fizyki I | ✅ pełny |
| 01 | [Pomiar, jednostki i niepewności](modules/01-pomiary-i-niepewnosci) | 🟢🔵 | Pracownia fizyczna I, wstęp do Fizyki I | ✅ pełny |
| 02 | [Kinematyka](modules/02-kinematyka) | 🟢🔵 | Fizyka I — kinematyka punktu materialnego | ✅ pełny |
| 03 | [Dynamika punktu materialnego](modules/03-dynamika) | 🟢🔵 | Fizyka I — dynamika | ✅ pełny |
| 04 | [Praca, energia i moc](modules/04-praca-i-energia) | 🟢🔵 | Fizyka I — zasady zachowania (energia) | ✅ pełny |
| 05 | [Pęd, środek masy i zderzenia](modules/05-ped-i-zderzenia) | 🟢🔵 | Fizyka I — zasady zachowania (pęd) | ✅ pełny |
| 06 | [Bryła sztywna, statyka i sprężystość](modules/06-bryla-sztywna) | 🟢🔵 | Fizyka I — ruch obrotowy | ✅ pełny |
| 07 | [Grawitacja i elementy astronomii](modules/07-grawitacja-i-astronomia) | 🟢🔵 | Fizyka I — grawitacja; elementy astronomii z matury | ✅ pełny |
| 08 | [Mechanika płynów](modules/08-plyny) | 🟢🔵 | Fizyka I — hydrostatyka i hydrodynamika | ✅ pełny |
| 09 | [Drgania](modules/09-drgania) | 🟢🔵 | Fizyka I — ruch drgający; Drgania i fale | ✅ pełny |
| 10 | [Fale mechaniczne i akustyka](modules/10-fale-i-akustyka) | 🟢🔵 | Fizyka I — fale; Drgania i fale | ✅ pełny |
| 11 | [Termodynamika i teoria kinetyczna](modules/11-termodynamika) | 🟢🔵 | Fizyka I — termodynamika fenomenologiczna i kinetyczna teoria gazów | ✅ pełny |
| 12 | [Elektrostatyka](modules/12-elektrostatyka) | 🟢🔵 | Fizyka II — pole elektryczne | ✅ pełny |
| 13 | [Prąd stały](modules/13-prad-staly) | 🟢🔵 | Fizyka II — prąd elektryczny | ✅ pełny |
| 14 | [Pole magnetyczne](modules/14-pole-magnetyczne) | 🟢🔵 | Fizyka II — magnetostatyka | ✅ pełny |
| 15 | [Indukcja elektromagnetyczna i prąd przemienny](modules/15-indukcja-i-prad-przemienny) | 🟢🔵 | Fizyka II — indukcja, drgania elektromagnetyczne | ✅ pełny |
| 16 | [Równania Maxwella i fale elektromagnetyczne](modules/16-rownania-maxwella-i-fale-em) | 🟢🔵 | Fizyka II — równania Maxwella, fale EM | ✅ pełny |
| 17 | [Optyka geometryczna](modules/17-optyka-geometryczna) | 🟢 | Fizyka II — optyka | ✅ pełny |
| 18 | [Optyka falowa](modules/18-optyka-falowa) | 🟢🔵 | Fizyka II — interferencja, dyfrakcja, polaryzacja | ✅ pełny |
| 19 | [Szczególna teoria względności](modules/19-teoria-wzglednosci) | 🟢🔵 | Fizyka II / Fizyka współczesna — elementy STW | ✅ pełny |
| 20 | [Podstawy fizyki kwantowej](modules/20-fizyka-kwantowa) | 🟢🔵 | Fizyka współczesna / Fizyka III — wstęp do mechaniki kwantowej | ✅ pełny |
| 21 | [Fizyka atomowa](modules/21-fizyka-atomowa) | 🟢🔵 | Fizyka współczesna — budowa atomu | ✅ pełny |
| 22 | [Fizyka jądrowa](modules/22-fizyka-jadrowa) | 🟢🔵 | Fizyka współczesna — jądro atomowe | ✅ pełny |
| 23 | [Fizyka ciała stałego](modules/23-fizyka-ciala-stalego) | 🔵 | Fizyka współczesna / Fizyka ciała stałego (wstęp) | 🔲 szkielet |
| 24 | [Cząstki elementarne i kosmologia](modules/24-czastki-i-kosmologia) | 🟢🔵 | Fizyka współczesna — cząstki i Wszechświat | 🔲 szkielet |
| 25 | [Fizyka obliczeniowa w Pythonie](modules/25-fizyka-obliczeniowa) | 🟢🔵 | Metody numeryczne / Fizyka komputerowa (wstęp) | 🔲 szkielet |

🔲 szkielet — struktura tematów i odnośniki do podręczników · ✅ pełny — notatki, przykłady, zadania z odpowiedziami, doświadczenia, źródła

Numeracja odpowiada kolejności z podręczników, ale nie jest sztywną kolejnością nauki: **moduł 00 (matematyka) warto przerabiać równolegle z 02–05**, a **25 (fizyka obliczeniowa) — razem z mechaniką i drganiami**. Szczegóły w [ROADMAP.md](ROADMAP.md).

* * *

## Odnośniki do podręczników

- ***Fizyka dla szkół wyższych*** ma tę samą numerację rozdziałów i paragrafów co angielskie *University Physics*. Link prowadzi do pierwszego paragrafu z podanego zakresu, a obok jest link do wstępu rozdziału.
- ***Podstawy fizyki*, wyd. 2015** (PWN, tłumaczenie 10. wydania *Fundamentals of Physics*) — tom, paragraf i strona, od której paragraf się zaczyna. Każdy tom ma własną numerację stron: t. 1 — rozdz. 1–11, t. 2 — 12–20, t. 3 — 21–32, t. 4 — 33–37, t. 5 — 38–44.
- ***Podstawy fizyki*, wyd. 1** (PWN 2003, tłumaczenie 6. wydania) — paragraf i strona w książce; link otwiera PDF z serwera AGH na tej stronie (`#page=…`, działa w przeglądarkowych czytnikach PDF). To wydanie ma inny podział: t. 1 — rozdz. 1–12, t. 2 — 13–21, t. 3 — 22–33, t. 4 — 34–38, t. 5 — 39–45, i inną numerację rozdziałów (m.in. pęd i zderzenia to osobne rozdziały 9 i 10, a prąd zmienny jest w rozdz. 33, po równaniach Maxwella). Skan t. 3 na serwerze AGH kończy się na s. 127 (koniec rozdz. 26) — dla rozdz. 27–33 podana jest strona bez linku.
- Oba podręczniki są ułożone inaczej, więc ten sam temat bywa u nich w różnych rozdziałach — np. polaryzacja jest w *Fizyce dla szkół wyższych* przy naturze światła (t. 3, §1.7), a u Hallidaya przy falach elektromagnetycznych (§33.4).

* * *

## Sprawdzanie materiałów

- **Kod w Pythonie** z wszystkich plików `.md` uruchamia skrypt [tools/check_snippets.py](tools/check_snippets.py) (pomija bloki wymagające SymPy lub danych z zewnątrz).
- Sprawdzenie wykonuje automatycznie GitHub Actions przy każdym pushu ([konfiguracja](.github/workflows/checks.yml)) — wynik w zakładce *Actions*.
- Wzory są pisane pod renderer GitHuba (MathJax): przecinek dziesiętny jako `{,}` (np. `9{,}81`), w tabelach `\lvert … \rvert` zamiast `|`, wektory jako `\vec{v}` lub `\mathbf{F}`.

* * *

## Zasady pracy, które naprawdę działają

- **Najpierw rysunek i założenia, potem wzory.** Większość błędów w fizyce to zły model, a nie zła algebra.
- **Sprawdzaj jednostki i przypadki graniczne.** Wynik, który ma złą jednostkę albo nie przechodzi w znany przypadek, jest błędny.
- **Rozwiązuj zadania bez notatek.** Przeczytanie rozwiązania to nie to samo, co umiejętność.
- **Mierz, nie tylko licz.** Krótki pomiar smartfonem uczy więcej o niepewnościach niż rozdział teorii.
- **Wracaj do starych tematów.** Co tydzień rozwiąż co najmniej jedno zadanie z wcześniejszych modułów.
- **Moduł jest zaliczony**, gdy rozwiązujesz nowe zadania, potrafisz wyprowadzić użyte zależności i sprawdzić wynik inną metodą.

* * *

## Licencja

Treść własna repozytorium (notatki, przykłady, zadania): **CC BY-SA 4.0** — szczegóły w [LICENSE.md](LICENSE.md). Materiały zewnętrzne pozostają własnością ich autorów i są tu tylko linkowane lub cytowane z numerem strony.
