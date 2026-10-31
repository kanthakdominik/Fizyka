# 27 — Fizyka statystyczna

> **Status:** ✅ pełny · **Poziom:** 🔵 · **Odpowiednik:** Fizyka statystyczna / Termodynamika statystyczna (wstęp) · **Czas:** 20–35 h od zera

## Cel modułu

Wyprowadzać prawa termodynamiki z zachowania ogromnej liczby cząstek: entropię z liczenia mikrostanów, rozkład Boltzmanna, ciepło właściwe, statystyki kwantowe i przejścia fazowe, z symulacjami w Pythonie.

## Wymagania wstępne

- [11 Termodynamika i teoria kinetyczna](../11-termodynamika/)
- [20 Podstawy fizyki kwantowej](../20-fizyka-kwantowa/)
- [25 Fizyka obliczeniowa w Pythonie](../25-fizyka-obliczeniowa/)

## Tematy

| # | Temat | Poziom | OpenStax (PL) | Halliday — wyd. 2015 (paragraf, strona) · wyd. 1 (PDF) |
|---|---|---|---|---|
| 01 | [Mikrostany, makrostany i entropia Boltzmanna](01-mikrostany-i-entropia.md) | 🔵 | [t. 2, §4.7](https://openstax.org/books/fizyka-dla-szk%C3%B3%C5%82-wy%C5%BCszych-tom-2/pages/4-7-entropia-w-skali-mikroskopowej) | t. 2, §20.4 (s. 352) · wyd. 1: t. 2, [§21.7, s. 276](https://home.agh.edu.pl/~czapli/Resnick_2.pdf#page=292) |
| 02 | [Rozkład Boltzmanna i suma statystyczna](02-rozklad-boltzmanna.md) | 🔵 | [t. 2, §2.4](https://openstax.org/books/fizyka-dla-szk%C3%B3%C5%82-wy%C5%BCszych-tom-2/pages/2-4-rozklad-predkosci-czasteczek-gazu-doskonalego) | t. 2, §19.6 (s. 301) · wyd. 1: t. 2, [§20.7, s. 236](https://home.agh.edu.pl/~czapli/Resnick_2.pdf#page=252) |
| 03 | [Ekwipartycja energii i kwantowe zamrażanie stopni swobody](03-ekwipartycja-i-cieplo-wlasciwe.md) | 🔵 | [t. 2, §2.3](https://openstax.org/books/fizyka-dla-szk%C3%B3%C5%82-wy%C5%BCszych-tom-2/pages/2-3-cieplo-wlasciwe-i-zasada-ekwipartycji-energii) | t. 2, §19.7–19.8 (s. 306) · wyd. 1: t. 2, [§20.8–20.10, s. 239](https://home.agh.edu.pl/~czapli/Resnick_2.pdf#page=255) |
| 04 | [Statystyki kwantowe: fermiony, bozony i promieniowanie cieplne](04-statystyki-kwantowe.md) | 🔵 | [t. 3, §6.1](https://openstax.org/books/fizyka-dla-szk%C3%B3%C5%82-wy%C5%BCszych-tom-3/pages/6-1-promieniowanie-ciala-doskonale-czarnego) | — |
| 05 | [Model Isinga, przejścia fazowe i metoda Metropolisa](05-model-isinga.md) | 🔵 | — | — |

🟢 matura rozszerzona · 🔵 studia (1. rok) · 🟢🔵 temat maturalny pogłębiany na studiach

Wszystkie wzory modułu na jednej stronie: **[ściąga](SCIAGA.md)**.

## Główne źródła modułu

| Źródło | Zakres |
|---|---|
| [OpenStax, *Fizyka dla szkół wyższych*, t. 2, rozdz. 4](https://openstax.org/books/fizyka-dla-szk%C3%B3%C5%82-wy%C5%BCszych-tom-2/pages/4-wstep) | tekst główny, pytania, zadania z odpowiedziami |
| [OpenStax, *Fizyka dla szkół wyższych*, t. 2, rozdz. 2](https://openstax.org/books/fizyka-dla-szk%C3%B3%C5%82-wy%C5%BCszych-tom-2/pages/2-wstep) | tekst główny, pytania, zadania z odpowiedziami |
| [OpenStax, *Fizyka dla szkół wyższych*, t. 3, rozdz. 6](https://openstax.org/books/fizyka-dla-szk%C3%B3%C5%82-wy%C5%BCszych-tom-3/pages/6-wstep) | tekst główny, pytania, zadania z odpowiedziami |
| Halliday, Resnick, Walker, *Podstawy fizyki*, wyd. 2015: t. 2, rozdz. 19 (od s. 288) | wykład bardziej szczegółowy, zadania i pytania kontrolne |
| Halliday, Resnick, Walker, *Podstawy fizyki*, wyd. 2015: t. 2, rozdz. 20 (od s. 332) | wykład bardziej szczegółowy, zadania i pytania kontrolne |
| Halliday, Resnick, Walker, *Podstawy fizyki*, wyd. 1: [t. 2, rozdz. 20 „Kinetyczna teoria gazów”, od s. 225](https://home.agh.edu.pl/~czapli/Resnick_2.pdf#page=241) | to samo w pierwszym wydaniu (PDF z serwera AGH) |
| Halliday, Resnick, Walker, *Podstawy fizyki*, wyd. 1: [t. 2, rozdz. 21 „Entropia i druga zasada termodynamiki”, od s. 260](https://home.agh.edu.pl/~czapli/Resnick_2.pdf#page=276) | to samo w pierwszym wydaniu (PDF z serwera AGH) |
| [Symulacje PhET — wersja polska](https://phet.colorado.edu/pl/) | *Właściwości gazu* (27.01, 27.02, 27.03); *Widmo ciała doskonale czarnego* (27.04) |
| [phyphox](https://phyphox.org/) — pomiary smartfonem | doświadczenia w tematach 27.02, 27.04 |
| F. Reif, *Fizyka statystyczna* (Kurs Fizyki Berkeley, t. 5), PWN | podręcznik na poziomie pierwszych lat studiów |
| K. Huang, *Podstawy fizyki statystycznej*, PWN | wykład akademicki: zespoły statystyczne, statystyki kwantowe, przejścia fazowe |

## Test wejściowy (diagnoza)

Rozwiąż bez notatek, około 30 minut.

1. Na ile sposobów można wybrać 2 elementy z 5? Oblicz $\binom{10}{5}$.
2. Oblicz $\ln(2^{100})$ i $\ln(10!)$ (możesz użyć kalkulatora).
3. Oblicz $\displaystyle\int_0^\infty e^{-ax}\,dx$ i $\displaystyle\sum_{n=0}^\infty q^n$ dla $\lvert q\rvert < 1$.
4. Ile wynosi średnia energia kinetyczna cząsteczki gazu doskonałego w temperaturze 300 K?
5. Gaz doskonały rozpręża się izotermicznie od $V$ do $2V$. Oblicz zmianę entropii 1 mola.
6. Elektron w atomie wodoru przechodzi z $n = 2$ na $n = 1$. Ile wynosi energia fotonu?

<details>
<summary>Odpowiedzi</summary>

1. 10; 252
2. ok. 69,3; ok. 15,1
3. $1/a$; $1/(1 - q)$
4. $\tfrac32kT \approx 6{,}2\cdot10^{-21}\ \mathrm J$
5. $R\ln2 \approx 5{,}76\ \mathrm{J/K}$
6. 10,2 eV
</details>

## Projekt modułowy: od liczenia stanów do przejścia fazowego

- [ ] **Model Einsteina z danych.** Znajdź w tablicach ciepło molowe diamentu, miedzi i ołowiu w kilku temperaturach. Dopasuj temperaturę Einsteina dla każdego materiału (25.04) i porównaj z modelem Debye'a.
- [ ] **Gaz w pudle.** Zasymuluj kilkaset cząstek w dwuwymiarowym pudle z ruchomą przegrodą (lub skorzystaj z symulacji PhET *Właściwości gazu*) i sprawdź, że rozkład prędkości dąży do rozkładu Maxwella niezależnie od stanu początkowego.
- [ ] **Model Isinga.** Rozbuduj symulację z tematu 27.05: zmierz namagnesowanie, podatność i ciepło właściwe dla siatek 16×16, 32×32 i 64×64. Pokaż, jak maksimum ciepła właściwego zbliża się do temperatury Onsagera wraz z rozmiarem siatki.
- [ ] **Stała Boltzmanna z pomiaru.** Zmierz ciśnienie powietrza na różnych wysokościach (barometr w phyphox, wysoki budynek) i wyznacz $k$ ze wzoru barometrycznego przy znanej temperaturze i masie cząsteczki.
- [ ] W sprawozdaniu omów, które wyniki zależą od założenia równowagi termicznej.

## Sprawdzian końcowy modułu

- [ ] Rozróżniam mikrostan i makrostan, liczę wagi statystyczne i entropię Boltzmanna; wyprowadzam $\Delta S$ rozprężania i definicję temperatury $1/T = \partial S/\partial U$.
- [ ] Stosuję rozkład Boltzmanna i sumę statystyczną: wzór barometryczny, obsadzenia poziomów, paramagnetyzm, rozkład Maxwella, średnią energię oscylatora.
- [ ] Stosuję zasadę ekwipartycji i wyjaśniam zamrażanie stopni swobody; liczę ciepło molowe gazów i ciał stałych (Dulong–Petit, model Einsteina).
- [ ] Rozróżniam statystyki Fermiego–Diraca i Bosego–Einsteina, oceniam kryterium $n\lambda_{th}^3$, wyprowadzam prawo Plancka i Stefana–Boltzmanna, liczę temperaturę kondensacji Bosego–Einsteina.
- [ ] Opisuję model Isinga i przejście fazowe, symuluję je metodą Metropolisa i porównuję z rozwiązaniem Onsagera i przybliżeniem pola średniego.
