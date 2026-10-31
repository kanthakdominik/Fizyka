# 08 — Mechanika płynów

> **Status:** ✅ pełny · **Poziom:** 🟢🔵 · **Odpowiednik:** Fizyka I — hydrostatyka i hydrodynamika · **Czas:** 15–25 h od zera

## Cel modułu

Liczyć ciśnienie i wypór w cieczach w spoczynku oraz opisywać przepływ równaniem ciągłości i równaniem Bernoulliego.

## Wymagania wstępne

- [04 Praca, energia i moc](../04-praca-i-energia/)

## Tematy

| # | Temat | Poziom | OpenStax (PL) | Halliday — wyd. 2015 (paragraf, strona) · wyd. 1 (PDF) |
|---|---|---|---|---|
| 01 | [Ciśnienie, prawo Pascala, ciśnienie hydrostatyczne](01-cisnienie-i-prawo-pascala.md) | 🟢 | [t. 1, §14.1–14.3](https://openstax.org/books/fizyka-dla-szk%C3%B3%C5%82-wy%C5%BCszych-tom-1/pages/14-1-plyny-gestosc-i-cisnienie) | t. 2, §14.1–14.4 (s. 78) · wyd. 1: t. 2, [§15.1–15.6, s. 61](https://home.agh.edu.pl/~czapli/Resnick_2.pdf#page=77) |
| 02 | [Prawo Archimedesa i pływanie ciał](02-prawo-archimedesa.md) | 🟢 | [t. 1, §14.4](https://openstax.org/books/fizyka-dla-szk%C3%B3%C5%82-wy%C5%BCszych-tom-1/pages/14-4-prawo-archimedesa-i-sila-wyporu) | t. 2, §14.5 (s. 90) · wyd. 1: t. 2, [§15.7, s. 71](https://home.agh.edu.pl/~czapli/Resnick_2.pdf#page=87) |
| 03 | [Równanie ciągłości i równanie Bernoulliego](03-rownanie-bernoulliego.md) | 🔵 | [t. 1, §14.5–14.6](https://openstax.org/books/fizyka-dla-szk%C3%B3%C5%82-wy%C5%BCszych-tom-1/pages/14-5-dynamika-plynow) | t. 2, §14.6–14.7 (s. 94) · wyd. 1: t. 2, [§15.8–15.10, s. 75](https://home.agh.edu.pl/~czapli/Resnick_2.pdf#page=91) |
| 04 | [Lepkość i turbulencja](04-lepkosc-i-turbulencja.md) | 🔵 | [t. 1, §14.7](https://openstax.org/books/fizyka-dla-szk%C3%B3%C5%82-wy%C5%BCszych-tom-1/pages/14-7-lepkosc-i-turbulencje) | — |

🟢 matura rozszerzona · 🔵 studia (1. rok) · 🟢🔵 temat maturalny pogłębiany na studiach

Wszystkie wzory modułu na jednej stronie: **[ściąga](SCIAGA.md)**.

## Główne źródła modułu

| Źródło | Zakres |
|---|---|
| [OpenStax, *Fizyka dla szkół wyższych*, t. 1, rozdz. 14](https://openstax.org/books/fizyka-dla-szk%C3%B3%C5%82-wy%C5%BCszych-tom-1/pages/14-wstep) | tekst główny, pytania, zadania z odpowiedziami |
| Halliday, Resnick, Walker, *Podstawy fizyki*, wyd. 2015: t. 2, rozdz. 14 (od s. 78) | wykład bardziej szczegółowy, zadania i pytania kontrolne |
| Halliday, Resnick, Walker, *Podstawy fizyki*, wyd. 1: [t. 2, rozdz. 15 „Płyny”, od s. 61](https://home.agh.edu.pl/~czapli/Resnick_2.pdf#page=77) | to samo w pierwszym wydaniu (PDF z serwera AGH) |
| [Symulacje PhET — wersja polska](https://phet.colorado.edu/pl/) | *Pod ciśnieniem* (08.01); *Siła wyporu* (08.02); *Ciśnienie cieczy i przepływ* (08.03) |
| [phyphox](https://phyphox.org/) — pomiary smartfonem | doświadczenie w temacie 08.01 |

## Test wejściowy (diagnoza)

Rozwiąż bez notatek, około 30 minut.

1. Jakie ciśnienie hydrostatyczne panuje na głębokości 5 m w wodzie?
2. Człowiek o masie 80 kg stoi na nartach o łącznym polu $0{,}3\ \mathrm{m^2}$. Jakie ciśnienie wywiera na śnieg?
3. Prasa hydrauliczna ma tłoki o polach $5\ \mathrm{cm^2}$ i $500\ \mathrm{cm^2}$. Jaka siła działa na duży tłok, gdy na mały naciskamy siłą 50 N?
4. Sześcian o boku 10 cm i gęstości $800\ \mathrm{kg/m^3}$ pływa w wodzie. Na jaką głębokość się zanurza?
5. Woda płynie rurą o średnicy 4 cm z prędkością 1 m/s. Jaka jest jej prędkość w miejscu, gdzie rura ma średnicę 2 cm?
6. Dlaczego trudno wyciągnąć nogę z błota albo przyssawkę z gładkiej ściany?

<details>
<summary>Odpowiedzi</summary>

1. $\rho gh \approx 49\ \mathrm{kPa}$ (plus ciśnienie atmosferyczne, razem ok. 150 kPa)
2. $p \approx 2{,}6\ \mathrm{kPa}$
3. $5\ \mathrm{kN}$
4. $8\ \mathrm{cm}$
5. $4\ \mathrm{m/s}$
6. Pod nogą (przyssawką) ciśnienie jest mniejsze niż atmosferyczne; różnica ciśnień razy pole daje dużą siłę
</details>

## Projekt modułowy: hydrostatyka i przepływ w kuchni

- [ ] **Barometr w telefonie.** Z czujnikiem ciśnienia (phyphox, *Pressure*) zmierz zmianę ciśnienia na kolejnych piętrach budynku. Narysuj $p(h)$, dopasuj prostą i wyznacz gęstość powietrza z nachylenia ($dp/dh = -\rho g$). Porównaj z $1{,}2\ \mathrm{kg/m^3}$.
- [ ] **Gęstość z prawa Archimedesa.** Wyznacz wagą kuchenną gęstość trzech przedmiotów (metalowy, kamień, plastik tonący), mierząc masę wypartej wody. Podaj wyniki z niepewnościami i porównaj z tablicami.
- [ ] **Wzór Torricellego.** Zrób otwór w dnie lub boku plastikowej butelki. Mierz co kilka sekund wysokość wody (podziałka na butelce, film). Sprawdź, czy $\sqrt h$ maleje liniowo z czasem, i porównaj nachylenie z teorią $\tfrac{s}{S}\sqrt{g/2}$ — wyznacz „efektywne” pole otworu (współczynnik kontrakcji strumienia).
- [ ] W sprawozdaniu omów, który z pomiarów najbardziej odbiegał od modelu i dlaczego.

## Sprawdzian końcowy modułu

- [ ] Liczę ciśnienie hydrostatyczne i atmosferyczne, stosuję prawo Pascala do pras hydraulicznych i naczyń połączonych.
- [ ] Liczę siłę parcia na ściany i zapory przez całkowanie oraz ciśnienie w atmosferze (wzór barometryczny).
- [ ] Stosuję prawo Archimedesa: warunki pływania, część zanurzona, ciężar pozorny, gęstość z ważenia.
- [ ] Stosuję równanie ciągłości i równanie Bernoulliego (Torricelli, Venturi, Pitot) i rozwiązuję zadanie o opróżnianiu zbiornika.
- [ ] Rozumiem lepkość, liczę przepływ z prawa Poiseuille'a i oceniam rodzaj przepływu z liczby Reynoldsa.
