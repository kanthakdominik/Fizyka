# 06 — Bryła sztywna, statyka i sprężystość

> **Status:** 🔲 szkielet · **Poziom:** 🟢🔵 · **Odpowiednik:** Fizyka I — ruch obrotowy · **Czas:** 35–55 h od zera

## Cel modułu

Przenieść dynamikę na ruch obrotowy: moment bezwładności liczony całką, moment siły, toczenie, moment pędu i jego zachowanie, równowaga brył oraz odkształcenia sprężyste.

## Wymagania wstępne

- [05 Pęd, środek masy i zderzenia](../05-ped-i-zderzenia/)

## Tematy

| # | Temat | Poziom | OpenStax (PL) | Halliday — wyd. 2015 (paragraf, strona) · wyd. 1 (PDF) |
|---|---|---|---|---|
| 01 | [Kinematyka ruchu obrotowego](01-kinematyka-obrotow.md) | 🟢 | [t. 1, §10.1–10.3](https://openstax.org/books/fizyka-dla-szk%C3%B3%C5%82-wy%C5%BCszych-tom-1/pages/10-1-zmienne-opisujace-ruch-obrotowy) | t. 1, §10.1–10.3 (s. 325) · wyd. 1: [t. 1, rozdz. 11](https://home.agh.edu.pl/~czapli/Resnick_1.pdf) |
| 02 | [Moment bezwładności i twierdzenie Steinera](02-moment-bezwladnosci.md) | 🟢🔵 | [t. 1, §10.4–10.5](https://openstax.org/books/fizyka-dla-szk%C3%B3%C5%82-wy%C5%BCszych-tom-1/pages/10-4-moment-bezwladnosci-i-energia-kinetyczna-w-ruchu-obrotowym) | t. 1, §10.4–10.5 (s. 343) · wyd. 1: [t. 1, rozdz. 11](https://home.agh.edu.pl/~czapli/Resnick_1.pdf) |
| 03 | [Moment siły i dynamika ruchu obrotowego](03-moment-sily.md) | 🟢 | [t. 1, §10.6–10.8](https://openstax.org/books/fizyka-dla-szk%C3%B3%C5%82-wy%C5%BCszych-tom-1/pages/10-6-moment-sily) | t. 1, §10.6–10.8 (s. 350) · wyd. 1: [t. 1, rozdz. 11](https://home.agh.edu.pl/~czapli/Resnick_1.pdf) |
| 04 | [Toczenie bez poślizgu](04-toczenie.md) | 🟢 | [t. 1, §11.1](https://openstax.org/books/fizyka-dla-szk%C3%B3%C5%82-wy%C5%BCszych-tom-1/pages/11-1-toczenie-sie-cial) | t. 1, §11.1–11.3 (s. 375) · wyd. 1: [t. 1, rozdz. 12](https://home.agh.edu.pl/~czapli/Resnick_1.pdf) |
| 05 | [Moment pędu i zasada jego zachowania](05-moment-pedu.md) | 🟢🔵 | [t. 1, §11.2–11.3](https://openstax.org/books/fizyka-dla-szk%C3%B3%C5%82-wy%C5%BCszych-tom-1/pages/11-2-moment-pedu) | t. 1, §11.4–11.8 (s. 384) · wyd. 1: [t. 1, rozdz. 12](https://home.agh.edu.pl/~czapli/Resnick_1.pdf) |
| 06 | [Precesja żyroskopu](06-precesja.md) | 🔵 | [t. 1, §11.4](https://openstax.org/books/fizyka-dla-szk%C3%B3%C5%82-wy%C5%BCszych-tom-1/pages/11-4-precesja-zyroskopu) | t. 1, §11.9 (s. 403) · wyd. 1: [t. 1, rozdz. 12](https://home.agh.edu.pl/~czapli/Resnick_1.pdf) |
| 07 | [Równowaga statyczna, naprężenia i prawo Hooke'a](07-rownowaga-i-sprezystosc.md) | 🟢🔵 | [t. 1, §12.1–12.4](https://openstax.org/books/fizyka-dla-szk%C3%B3%C5%82-wy%C5%BCszych-tom-1/pages/12-1-warunki-rownowagi-statycznej) | t. 2, §12.1–12.3 (s. 1) · wyd. 1: [t. 2, rozdz. 13](https://home.agh.edu.pl/~czapli/Resnick_2.pdf) |

🟢 matura rozszerzona · 🔵 studia (1. rok) · 🟢🔵 temat maturalny pogłębiany na studiach

## Główne źródła modułu

| Źródło | Zakres |
|---|---|
| [OpenStax, *Fizyka dla szkół wyższych*, t. 1, rozdz. 10](https://openstax.org/books/fizyka-dla-szk%C3%B3%C5%82-wy%C5%BCszych-tom-1/pages/10-wstep) | tekst główny, pytania, zadania z odpowiedziami |
| [OpenStax, *Fizyka dla szkół wyższych*, t. 1, rozdz. 11](https://openstax.org/books/fizyka-dla-szk%C3%B3%C5%82-wy%C5%BCszych-tom-1/pages/11-wstep) | tekst główny, pytania, zadania z odpowiedziami |
| [OpenStax, *Fizyka dla szkół wyższych*, t. 1, rozdz. 12](https://openstax.org/books/fizyka-dla-szk%C3%B3%C5%82-wy%C5%BCszych-tom-1/pages/12-wstep) | tekst główny, pytania, zadania z odpowiedziami |
| Halliday, Resnick, Walker, *Podstawy fizyki*, wyd. 2015: t. 1, rozdz. 10 (od s. 325) · wyd. 1: [t. 1, rozdz. 11](https://home.agh.edu.pl/~czapli/Resnick_1.pdf) | wykład bardziej szczegółowy, zadania i pytania kontrolne |
| Halliday, Resnick, Walker, *Podstawy fizyki*, wyd. 2015: t. 1, rozdz. 11 (od s. 375) · wyd. 1: [t. 1, rozdz. 12](https://home.agh.edu.pl/~czapli/Resnick_1.pdf) | wykład bardziej szczegółowy, zadania i pytania kontrolne |
| Halliday, Resnick, Walker, *Podstawy fizyki*, wyd. 2015: t. 2, rozdz. 12 (od s. 1) · wyd. 1: [t. 2, rozdz. 13](https://home.agh.edu.pl/~czapli/Resnick_2.pdf) | wykład bardziej szczegółowy, zadania i pytania kontrolne |

_Lista zostanie uzupełniona o symulacje, zadania maturalne i inne materiały przy wypełnianiu modułu._

## Test wejściowy (diagnoza)

_do uzupełnienia_

## Projekt modułowy

_do uzupełnienia_

## Sprawdzian końcowy modułu

_do uzupełnienia_
