# Fizyka — od matury rozszerzonej do pierwszego roku politechniki

Otwarta, samodzielna ścieżka nauki fizyki na dwóch poziomach: **matury rozszerzonej** oraz **kursu fizyki z pierwszego roku studiów technicznych** (z rachunkiem różniczkowym i całkowym). Repozytorium jest pomyślane jako darmowa pomoc do nauki przed maturą i studiami, w trakcie pierwszych semestrów albo do odświeżenia wiedzy po latach.

Układ działów opiera się na dwóch standardowych podręcznikach akademickich: **OpenStax *University Physics* (tomy 1–3)** — darmowym, i **Halliday, Resnick, Walker — *Fundamentals of Physics*** (pol. *Podstawy fizyki*, PWN) — płatnym. Każdy temat odsyła do konkretnych rozdziałów obu.

- **Notatki, przykłady i zadania** są napisane po polsku (treść własna repozytorium).
- **Źródła zewnętrzne** (kursy, książki, wykłady wideo, symulacje) są **anglojęzyczne i darmowe**. Książki płatne są wymienione z tytułem i numerem rozdziału, bez treści.
- Linki były sprawdzane przy dodawaniu. Jeśli któryś przestanie działać, zgłoś to w Issues.

* * *

## Jak korzystać z repozytorium

1. Przeczytaj [ROADMAP.md](ROADMAP.md) — kolejność modułów, zależności, trzy ścieżki nauki (matura, politechnika, most między nimi) i szacowany czas.
2. Przejrzyj [RESOURCES.md](RESOURCES.md) — główne podręczniki, kursy i symulacje, do których odwołują się moduły.
3. Zainstaluj narzędzia z [TOOLS.md](TOOLS.md) (wszystkie darmowe; do doświadczeń wystarczy smartfon).
4. Przerabiaj moduły po kolei. Każdy temat ma ten sam układ (pełny opis w [docs/SZABLON-TEMATU.md](docs/SZABLON-TEMATU.md)):

| Sekcja | Co zawiera |
|---|---|
| **Po co to jest** | Gdzie temat wraca w dalszej fizyce i w technice |
| **Teoria w pigułce** | Najważniejsze pojęcia i prawa, bez lania wody |
| **Wzory i założenia** | Wzory razem z warunkami, w których obowiązują |
| **Przykład rozwiązany** | Pełne rozwiązanie krok po kroku; tam gdzie to ma sens — także wersja z pochodną lub całką |
| **Typowe pułapki** | Błędy, które najczęściej kosztują punkty na maturze i kolokwium |
| **Doświadczenie / symulacja** | Pomiar smartfonem (phyphox), symulacja PhET albo krótki program w Pythonie |
| **Zadania** | A — poziom maturalny, B — poziom akademicki; odpowiedzi ukryte pod `<details>` |
| **Źródła** | Konkretne rozdziały i wykłady do pogłębienia |

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
| 00 | [Narzędzia matematyczne fizyka](modules/00-narzedzia-matematyczne) | 🟢🔵 | Analiza matematyczna I (fragmenty), wstęp do Fizyki I | 🔲 szkielet |
| 01 | [Pomiar, jednostki i niepewności](modules/01-pomiary-i-niepewnosci) | 🟢🔵 | Pracownia fizyczna I, wstęp do Fizyki I | 🔲 szkielet |
| 02 | [Kinematyka](modules/02-kinematyka) | 🟢🔵 | Fizyka I — kinematyka punktu materialnego | 🔲 szkielet |
| 03 | [Dynamika punktu materialnego](modules/03-dynamika) | 🟢🔵 | Fizyka I — dynamika | 🔲 szkielet |
| 04 | [Praca, energia i moc](modules/04-praca-i-energia) | 🟢🔵 | Fizyka I — zasady zachowania (energia) | 🔲 szkielet |
| 05 | [Pęd, środek masy i zderzenia](modules/05-ped-i-zderzenia) | 🟢🔵 | Fizyka I — zasady zachowania (pęd) | 🔲 szkielet |
| 06 | [Bryła sztywna, statyka i sprężystość](modules/06-bryla-sztywna) | 🟢🔵 | Fizyka I — ruch obrotowy | 🔲 szkielet |
| 07 | [Grawitacja i elementy astronomii](modules/07-grawitacja-i-astronomia) | 🟢🔵 | Fizyka I — grawitacja; elementy astronomii z matury | 🔲 szkielet |
| 08 | [Mechanika płynów](modules/08-plyny) | 🟢🔵 | Fizyka I — hydrostatyka i hydrodynamika | 🔲 szkielet |
| 09 | [Drgania](modules/09-drgania) | 🟢🔵 | Fizyka I — ruch drgający; Drgania i fale | 🔲 szkielet |
| 10 | [Fale mechaniczne i akustyka](modules/10-fale-i-akustyka) | 🟢🔵 | Fizyka I — fale; Drgania i fale | 🔲 szkielet |
| 11 | [Termodynamika i teoria kinetyczna](modules/11-termodynamika) | 🟢🔵 | Fizyka I — termodynamika fenomenologiczna i kinetyczna teoria gazów | 🔲 szkielet |
| 12 | [Elektrostatyka](modules/12-elektrostatyka) | 🟢🔵 | Fizyka II — pole elektryczne | 🔲 szkielet |
| 13 | [Prąd stały](modules/13-prad-staly) | 🟢🔵 | Fizyka II — prąd elektryczny | 🔲 szkielet |
| 14 | [Pole magnetyczne](modules/14-pole-magnetyczne) | 🟢🔵 | Fizyka II — magnetostatyka | 🔲 szkielet |
| 15 | [Indukcja elektromagnetyczna i prąd przemienny](modules/15-indukcja-i-prad-przemienny) | 🟢🔵 | Fizyka II — indukcja, drgania elektromagnetyczne | 🔲 szkielet |
| 16 | [Równania Maxwella i fale elektromagnetyczne](modules/16-rownania-maxwella-i-fale-em) | 🟢🔵 | Fizyka II — równania Maxwella, fale EM | 🔲 szkielet |
| 17 | [Optyka geometryczna](modules/17-optyka-geometryczna) | 🟢 | Fizyka II — optyka | 🔲 szkielet |
| 18 | [Optyka falowa](modules/18-optyka-falowa) | 🟢🔵 | Fizyka II — interferencja, dyfrakcja, polaryzacja | 🔲 szkielet |
| 19 | [Szczególna teoria względności](modules/19-teoria-wzglednosci) | 🟢🔵 | Fizyka II / Fizyka współczesna — elementy STW | 🔲 szkielet |
| 20 | [Podstawy fizyki kwantowej](modules/20-fizyka-kwantowa) | 🟢🔵 | Fizyka współczesna / Fizyka III — wstęp do mechaniki kwantowej | 🔲 szkielet |
| 21 | [Fizyka atomowa](modules/21-fizyka-atomowa) | 🟢🔵 | Fizyka współczesna — budowa atomu | 🔲 szkielet |
| 22 | [Fizyka jądrowa](modules/22-fizyka-jadrowa) | 🟢🔵 | Fizyka współczesna — jądro atomowe | 🔲 szkielet |
| 23 | [Fizyka ciała stałego](modules/23-fizyka-ciala-stalego) | 🔵 | Fizyka współczesna / Fizyka ciała stałego (wstęp) | 🔲 szkielet |
| 24 | [Cząstki elementarne i kosmologia](modules/24-czastki-i-kosmologia) | 🟢🔵 | Fizyka współczesna — cząstki i Wszechświat | 🔲 szkielet |
| 25 | [Fizyka obliczeniowa w Pythonie](modules/25-fizyka-obliczeniowa) | 🟢🔵 | Metody numeryczne / Fizyka komputerowa (wstęp) | 🔲 szkielet |

🔲 szkielet — struktura tematów i mapowanie źródeł · ✅ pełny — notatki, przykłady, zadania z odpowiedziami, doświadczenia, źródła

Numeracja odpowiada kolejności z podręczników, ale nie jest sztywną kolejnością nauki: **moduł 00 (matematyka) warto przerabiać równolegle z 02–05**, a **25 (fizyka obliczeniowa) — razem z mechaniką i drganiami**. Szczegóły w [ROADMAP.md](ROADMAP.md).

* * *

## Sprawdzanie materiałów

- **Kod w Pythonie** z wszystkich plików `.md` uruchamia skrypt [tools/check_snippets.py](tools/check_snippets.py) (pomija bloki wymagające SymPy lub danych z zewnątrz).
- Sprawdzenie wykonuje automatycznie GitHub Actions przy każdym pushu ([konfiguracja](.github/workflows/checks.yml)) — wynik w zakładce *Actions*.
- Wzory są pisane pod renderer GitHuba (MathJax): przecinek dziesiętny jako `\text{,}`, w tabelach `\lvert … \rvert` zamiast `|`, wektory jako `\vec{v}` lub `\mathbf{F}`.
- Numery rozdziałów Hallidaya podane są według wydania angielskiego 10 (*Fundamentals of Physics Extended*), z którego przetłumaczono polskie wydanie PWN 2015 (tomy 1–5). W innych wydaniach numeracja rozdziałów jest taka sama lub bardzo zbliżona.

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

Treść własna repozytorium (notatki, przykłady, zadania): **CC BY-SA 4.0** — szczegóły w [LICENSE.md](LICENSE.md). Materiały zewnętrzne pozostają własnością ich autorów i są tu tylko linkowane.
