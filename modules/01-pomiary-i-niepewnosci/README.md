# 01 — Pomiar, jednostki i niepewności

> **Status:** ✅ pełny · **Poziom:** 🟢🔵 · **Odpowiednik:** Pracownia fizyczna I, wstęp do Fizyki I · **Czas:** 20–35 h od zera

## Cel modułu

Umieć zmierzyć, oszacować i uczciwie podać wynik: jednostki SI, analiza wymiarowa, rząd wielkości, niepewności i dopasowanie prostej. Ten moduł przewija się przez wszystkie doświadczenia w repozytorium.

## Wymagania wstępne

- [00 Narzędzia matematyczne fizyka](../00-narzedzia-matematyczne/)

## Tematy

| # | Temat | Poziom | OpenStax (PL) | Halliday — wyd. 2015 (paragraf, strona) · wyd. 1 (PDF) |
|---|---|---|---|---|
| 01 | [Układ SI i stałe definicyjne](01-uklad-si.md) | 🟢🔵 | [t. 1, §1.1–1.3](https://openstax.org/books/fizyka-dla-szk%C3%B3%C5%82-wy%C5%BCszych-tom-1/pages/1-1-zakres-stosowalnosci-praw-fizyki) | t. 1, §1.1–1.3 (s. 1) · wyd. 1: t. 1, [§1.1–1.6, s. 2](https://home.agh.edu.pl/~czapli/Resnick_1.pdf#page=14) |
| 02 | [Analiza wymiarowa i szacowanie rzędu wielkości](02-analiza-wymiarowa-i-szacowanie.md) | 🟢🔵 | [t. 1, §1.4–1.5](https://openstax.org/books/fizyka-dla-szk%C3%B3%C5%82-wy%C5%BCszych-tom-1/pages/1-4-analiza-wymiarowa) | t. 1, §1.1 (s. 1) · wyd. 1: t. 1, [§1.3, s. 3](https://home.agh.edu.pl/~czapli/Resnick_1.pdf#page=15) |
| 03 | [Niepewności pomiarowe: typ A, typ B, niepewność złożona](03-niepewnosci-pomiarowe.md) | 🟢🔵 | [t. 1, §1.6](https://openstax.org/books/fizyka-dla-szk%C3%B3%C5%82-wy%C5%BCszych-tom-1/pages/1-6-cyfry-znaczace) | — |
| 04 | [Wykresy, linearyzacja i dopasowanie prostej](04-wykresy-i-dopasowanie.md) | 🟢🔵 | — | — |
| 05 | [Planowanie doświadczenia i raport z pomiarów](05-doswiadczenie-i-raport.md) | 🟢🔵 | [t. 1, §1.7](https://openstax.org/books/fizyka-dla-szk%C3%B3%C5%82-wy%C5%BCszych-tom-1/pages/1-7-rozwiazywanie-zadan-z-zakresu-fizyki) | — |

🟢 matura rozszerzona · 🔵 studia (1. rok) · 🟢🔵 temat maturalny pogłębiany na studiach

Wszystkie wzory modułu na jednej stronie: **[ściąga](SCIAGA.md)**.

## Główne źródła modułu

| Źródło | Zakres |
|---|---|
| [OpenStax, *Fizyka dla szkół wyższych*, t. 1, rozdz. 1](https://openstax.org/books/fizyka-dla-szk%C3%B3%C5%82-wy%C5%BCszych-tom-1/pages/1-wstep) | tekst główny, pytania, zadania z odpowiedziami |
| Halliday, Resnick, Walker, *Podstawy fizyki*, wyd. 2015: t. 1, rozdz. 1 (od s. 1) | wykład bardziej szczegółowy, zadania i pytania kontrolne |
| Halliday, Resnick, Walker, *Podstawy fizyki*, wyd. 1: [t. 1, rozdz. 1 „Pomiar”, od s. 2](https://home.agh.edu.pl/~czapli/Resnick_1.pdf#page=14) | to samo w pierwszym wydaniu (PDF z serwera AGH) |
| [phyphox](https://phyphox.org/) — pomiary smartfonem | doświadczenia w tematach 01.02, 01.03, 01.05 |
| [CKE — Informator o egzaminie maturalnym z fizyki](https://cke.gov.pl/images/_EGZAMIN_MATURALNY_OD_2023/Informatory/2024/Informator_EM2024_fizyka.pdf) i [zadania z arkuszy CKE](../../matura/README.md) | zadania maturalne do tematów 01.03, 01.04, 01.05 |
| [NIST — Fundamental Physical Constants](https://physics.nist.gov/cuu/Constants/) | temat 01.01 (materiał dodatkowy, po angielsku) |
| [JCGM 100:2008 — Guide to the Expression of Uncertainty in Measurement (GUM)](https://www.bipm.org/en/doi/10.59161/jcgm100-2008e) | temat 01.03 (materiał dodatkowy, po angielsku) |
| [NIST/SEMATECH e-Handbook of Statistical Methods](https://www.itl.nist.gov/div898/handbook/) | temat 01.04 (materiał dodatkowy, po angielsku) |

## Test wejściowy (diagnoza)

Rozwiąż bez notatek, około 30 minut.

1. Zamień: $90\ \mathrm{km/h}$ na m/s; $0{,}35\ \mathrm{mm}$ na metry w zapisie naukowym; $1{,}2\ \mathrm{g/cm^3}$ na $\mathrm{kg/m^3}$.
2. Wyraź dżul w jednostkach podstawowych SI.
3. Które wyrażenie jest niepoprawne wymiarowo: $v^2 = 2as$, $s = vt^2$, $E = mc^2$?
4. Oblicz średnią i odchylenie standardowe liczb $4{,}0$; $4{,}4$; $4{,}2$; $3{,}8$; $4{,}1$.
5. Prostokąt ma boki $(10{,}0 \pm 0{,}1)\ \mathrm{cm}$ i $(5{,}0 \pm 0{,}1)\ \mathrm{cm}$. Jaka jest niepewność względna każdego boku?
6. Zaokrąglij poprawnie wynik: $g = 9{,}7863\ \mathrm{m/s^2}$, $u(g) = 0{,}0472\ \mathrm{m/s^2}$.

<details>
<summary>Odpowiedzi</summary>

1. $25\ \mathrm{m/s}$; $3{,}5\cdot10^{-4}\ \mathrm{m}$; $1200\ \mathrm{kg/m^3}$
2. $\mathrm{kg\cdot m^2\cdot s^{-2}}$
3. $s = vt^2$
4. $\bar{x} = 4{,}1$; $s \approx 0{,}22$
5. $1\%$ i $2\%$
6. $g = (9{,}79 \pm 0{,}05)\ \mathrm{m/s^2}$
</details>

## Projekt modułowy: wyznaczenie przyspieszenia ziemskiego dwiema metodami

Celem jest pełne doświadczenie od planu do sprawozdania, z porównaniem dwóch niezależnych metod.

- [ ] **Metoda 1 — swobodny spadek.** Wykonaj pomiary według planu z [tematu 05](05-doswiadczenie-i-raport.md): co najmniej 6 wysokości, po 5 powtórzeń, czas mierzony eksperymentem *Acoustic Stopwatch* w phyphox.
- [ ] **Metoda 2 — wahadło.** Zmierz okres wahadła (telefon na sznurku, eksperyment *Pendulum*, albo ciężarek i stoper — czas 10 okresów) dla co najmniej 5 długości od 0,3 do 1,5 m.
- [ ] Dla obu metod narysuj wykres zlinearyzowany ($h(t^2)$ i $T^2(l)$), dopasuj prostą metodą najmniejszych kwadratów i wyznacz $g$ z niepewnością.
- [ ] Sprawdź, czy oba wyniki są zgodne ze sobą i z wartością $9{,}81\ \mathrm{m/s^2}$.
- [ ] Sporządź budżet niepewności dla obu metod: który składnik dominuje?
- [ ] Napisz sprawozdanie według szablonu z tematu 05 (wystarczy jedna strona plus wykresy). We wnioskach wskaż, która metoda okazała się dokładniejsza i dlaczego.

## Sprawdzian końcowy modułu

- [ ] Przeliczam jednostki z przedrostkami, także w potęgach, i rozpisuję jednostki pochodne na podstawowe.
- [ ] Sprawdzam wzór analizą wymiarową i wyprowadzam postać prostej zależności z dokładnością do stałej.
- [ ] Szacuję rząd wielkości, rozkładając problem na czynniki.
- [ ] Liczę niepewność typu A z serii i typu B z dokładności przyrządu oraz łączę je.
- [ ] Liczę niepewność wielkości obliczanej (suma, iloczyn, potęga, ogólny wzór z pochodnymi) i poprawnie zaokrąglam wynik.
- [ ] Rysuję wykres z niepewnościami, dopasowuję prostą i podaję nachylenie z niepewnością.
- [ ] Planuję doświadczenie, wskazuję dominujące źródło niepewności i możliwe błędy systematyczne.
