# 13 — Prąd stały

> **Status:** ✅ pełny · **Poziom:** 🟢🔵 · **Odpowiednik:** Fizyka II — prąd elektryczny · **Czas:** 25–40 h od zera

## Cel modułu

Rozumieć przepływ prądu od strony mikroskopowej, liczyć obwody z prawami Kirchhoffa i opisywać ładowanie kondensatora.

## Wymagania wstępne

- [12 Elektrostatyka](../12-elektrostatyka/)

## Tematy

| # | Temat | Poziom | OpenStax (PL) | Halliday — wyd. 2015 (paragraf, strona) · wyd. 1 (PDF) |
|---|---|---|---|---|
| 01 | [Natężenie i gęstość prądu, model przewodnictwa](01-prad-i-model-przewodnictwa.md) | 🟢🔵 | [t. 2, §9.1–9.2](https://openstax.org/books/fizyka-dla-szk%C3%B3%C5%82-wy%C5%BCszych-tom-2/pages/9-1-prad-elektryczny) | t. 3, §26.1–26.2 (s. 178) · wyd. 1: t. 3, §27.1–27.3, s. 129 |
| 02 | [Opór, opór właściwy i prawo Ohma](02-opor-i-prawo-ohma.md) | 🟢 | [t. 2, §9.3–9.4](https://openstax.org/books/fizyka-dla-szk%C3%B3%C5%82-wy%C5%BCszych-tom-2/pages/9-3-rezystywnosc-i-rezystancja) | t. 3, §26.3–26.4 (s. 187) · wyd. 1: t. 3, §27.4–27.6, s. 135 |
| 03 | [Praca i moc prądu](03-praca-i-moc-pradu.md) | 🟢 | [t. 2, §9.5](https://openstax.org/books/fizyka-dla-szk%C3%B3%C5%82-wy%C5%BCszych-tom-2/pages/9-5-energia-i-moc-elektryczna) | t. 3, §26.5 (s. 196) · wyd. 1: t. 3, §27.7, s. 144 |
| 04 | [SEM, opór wewnętrzny, łączenie oporników](04-sem-i-laczenie-opornikow.md) | 🟢 | [t. 2, §10.1–10.2](https://openstax.org/books/fizyka-dla-szk%C3%B3%C5%82-wy%C5%BCszych-tom-2/pages/10-1-sila-elektromotoryczna) | t. 3, §27.1–27.2 (s. 210) · wyd. 1: t. 3, §28.1–28.5, s. 155 |
| 05 | [Prawa Kirchhoffa i mierniki](05-prawa-kirchhoffa.md) | 🟢 | [t. 2, §10.3–10.4](https://openstax.org/books/fizyka-dla-szk%C3%B3%C5%82-wy%C5%BCszych-tom-2/pages/10-3-prawa-kirchhoffa) | t. 3, §27.2–27.3 (s. 222) · wyd. 1: t. 3, §28.6–28.7, s. 164 |
| 06 | [Obwody RC — ładowanie i rozładowanie](06-obwody-rc.md) | 🔵 | [t. 2, §10.5](https://openstax.org/books/fizyka-dla-szk%C3%B3%C5%82-wy%C5%BCszych-tom-2/pages/10-5-obwody-rc) | t. 3, §27.4 (s. 231) · wyd. 1: t. 3, §28.8, s. 171 |

🟢 matura rozszerzona · 🔵 studia (1. rok) · 🟢🔵 temat maturalny pogłębiany na studiach

## Główne źródła modułu

| Źródło | Zakres |
|---|---|
| [OpenStax, *Fizyka dla szkół wyższych*, t. 2, rozdz. 9](https://openstax.org/books/fizyka-dla-szk%C3%B3%C5%82-wy%C5%BCszych-tom-2/pages/9-wstep) | tekst główny, pytania, zadania z odpowiedziami |
| [OpenStax, *Fizyka dla szkół wyższych*, t. 2, rozdz. 10](https://openstax.org/books/fizyka-dla-szk%C3%B3%C5%82-wy%C5%BCszych-tom-2/pages/10-wstep) | tekst główny, pytania, zadania z odpowiedziami |
| Halliday, Resnick, Walker, *Podstawy fizyki*, wyd. 2015: t. 3, rozdz. 26 (od s. 178) | wykład bardziej szczegółowy, zadania i pytania kontrolne |
| Halliday, Resnick, Walker, *Podstawy fizyki*, wyd. 2015: t. 3, rozdz. 27 (od s. 210) | wykład bardziej szczegółowy, zadania i pytania kontrolne |
| Halliday, Resnick, Walker, *Podstawy fizyki*, wyd. 1: t. 3, rozdz. 27 „Prąd elektryczny i opór elektryczny”, od s. 129 (poza zakresem skanu) | to samo w pierwszym wydaniu (PDF z serwera AGH) |
| Halliday, Resnick, Walker, *Podstawy fizyki*, wyd. 1: t. 3, rozdz. 28 „Obwody elektryczne”, od s. 155 (poza zakresem skanu) | to samo w pierwszym wydaniu (PDF z serwera AGH) |
| [Symulacje PhET — wersja polska](https://phet.colorado.edu/pl/) | *Zestaw do budowy obwodów DC* (13.01, 13.04, 13.05); *Prawo Ohma* (13.02); *Zestaw do budowy obwodów AC* (13.06) |
| [CKE — Informator o egzaminie maturalnym z fizyki](https://cke.gov.pl/images/_EGZAMIN_MATURALNY_OD_2023/Informatory/2024/Informator_EM2024_fizyka.pdf) i [zadania z arkuszy CKE](../../matura/README.md) | zadania maturalne do tematów 13.02, 13.03, 13.04, 13.05 |

## Test wejściowy (diagnoza)

Rozwiąż bez notatek, około 30 minut.

1. Ładunek 2 C przechodzi przez różnicę potencjałów 6 V. Jaką energię zyskuje lub traci?
2. Oblicz pojemność zastępczą kondensatorów 4 μF i 4 μF połączonych szeregowo.
3. Rozwiąż układ równań: $x + y = 3$, $2x - y = 0$.
4. Rozwiąż równanie różniczkowe $\dfrac{dy}{dt} = -\dfrac{y}{2}$ z warunkiem $y(0) = 5$.
5. Ile to $e^{-1}$, $e^{-3}$ i $\ln 2$ (w przybliżeniu)?
6. Ile dżuli to 1 kWh?

<details>
<summary>Odpowiedzi</summary>

1. 12 J
2. 2 μF
3. $x = 1$, $y = 2$
4. $y = 5e^{-t/2}$
5. 0,368; 0,050; 0,693
6. $3{,}6\cdot10^6\ \mathrm J$
</details>

## Projekt modułowy: pracownia obwodów na płytce stykowej

- [ ] **Charakterystyki.** Zmierz $I(U)$ dla opornika, żarówki i diody LED. Wskaż element omowy i oszacuj opór żarówki na zimno i na gorąco.
- [ ] **SEM i opór wewnętrzny.** Wyznacz $\varepsilon$ i $r$ nowej i zużytej baterii z wykresu $U(I)$. Sprawdź, przy jakim oporze obciążenia moc jest największa.
- [ ] **Prawa Kirchhoffa.** Zbuduj obwód z dwoma źródłami i trzema opornikami, zmierz wszystkie prądy i napięcia. Porównaj z rozwiązaniem macierzowym (13.05).
- [ ] **Stała czasowa.** Zmierz krzywą rozładowania kondensatora (miernik i nagranie ekranu albo Arduino). Wyznacz $\tau$ z dopasowania i porównaj z $RC$ z wartości nominalnych, uwzględniając tolerancje elementów.
- [ ] W sprawozdaniu oceń wpływ oporu mierników na wyniki.

## Sprawdzian końcowy modułu

- [ ] Wiążę natężenie prądu z ładunkiem, gęstością nośników i prędkością dryfu; znam mikroskopowe prawo Ohma i model Drudego.
- [ ] Liczę opór przewodników z oporu właściwego, uwzględniam temperaturę, odróżniam elementy omowe od nieomowych.
- [ ] Liczę moc i energię prądu, koszty energii i straty przesyłu.
- [ ] Uwzględniam opór wewnętrzny źródła, łączę oporniki i ogniwa, liczę dzielnik napięcia i warunek dopasowania mocy.
- [ ] Rozwiązuję obwody z kilkoma źródłami prawami Kirchhoffa, dobieram bocznik i posobnik, liczę mostek Wheatstone'a.
- [ ] Rozwiązuję równanie obwodu RC, liczę stałą czasową, przebiegi ładowania i rozładowania oraz bilans energii.
