# 15 — Indukcja elektromagnetyczna i prąd przemienny

> **Status:** 🔲 szkielet · **Poziom:** 🟢🔵 · **Odpowiednik:** Fizyka II — indukcja, drgania elektromagnetyczne · **Czas:** 30–50 h od zera

## Cel modułu

Stosować prawo Faradaya i regułę Lenza, liczyć indukcyjność i energię pola magnetycznego, opisywać obwody RL, LC, RLC oraz prąd przemienny i transformator.

## Wymagania wstępne

- [14 Pole magnetyczne](../14-pole-magnetyczne/)
- [09 Drgania](../09-drgania/)

## Tematy

| # | Temat | Poziom | OpenStax (PL) | Halliday — wyd. 2015 (paragraf, strona) · wyd. 1 (PDF) |
|---|---|---|---|---|
| 01 | [Prawo Faradaya i reguła Lenza](01-prawo-faradaya-i-lenza.md) | 🟢 | [t. 2, §13.1–13.2](https://openstax.org/books/fizyka-dla-szk%C3%B3%C5%82-wy%C5%BCszych-tom-2/pages/13-1-prawo-faradaya) | t. 3, §30.1 (s. 329) · wyd. 1: t. 3, §31.1–31.4, s. 248 |
| 02 | [SEM ruchu i indukowane pole elektryczne](02-sem-ruchu-i-pole-indukowane.md) | 🟢🔵 | [t. 2, §13.3–13.4](https://openstax.org/books/fizyka-dla-szk%C3%B3%C5%82-wy%C5%BCszych-tom-2/pages/13-3-sila-elektromotoryczna-wywolana-ruchem) | t. 3, §30.2–30.3 (s. 338) · wyd. 1: t. 3, §31.5–31.6, s. 256 |
| 03 | [Prądy wirowe, prądnice i SEM wsteczna](03-pradnice-i-prady-wirowe.md) | 🟢 | [t. 2, §13.5–13.7](https://openstax.org/books/fizyka-dla-szk%C3%B3%C5%82-wy%C5%BCszych-tom-2/pages/13-5-prady-wirowe) | t. 3, §30.2 (s. 338) · wyd. 1: t. 3, §31.5, s. 256 |
| 04 | [Indukcyjność własna i wzajemna, energia pola magnetycznego](04-indukcyjnosc.md) | 🟢🔵 | [t. 2, §14.1–14.3](https://openstax.org/books/fizyka-dla-szk%C3%B3%C5%82-wy%C5%BCszych-tom-2/pages/14-1-indukcyjnosc-wzajemna) | t. 3, §30.4–30.5 (s. 348), §30.7–30.9 (s. 357) · wyd. 1: t. 3, §31.7–31.8, s. 264, §31.10–31.12, s. 271 |
| 05 | [Obwody RL, LC i RLC — drgania elektromagnetyczne](05-obwody-rl-lc-rlc.md) | 🔵 | [t. 2, §14.4–14.6](https://openstax.org/books/fizyka-dla-szk%C3%B3%C5%82-wy%C5%BCszych-tom-2/pages/14-4-obwody-rl) | t. 3, §30.6 (s. 352), §31.1–31.2 (s. 378) · wyd. 1: t. 3, §31.9, s. 267, §33.1–33.5, s. 320 |
| 06 | [Prąd przemienny: wartości skuteczne, impedancja, rezonans, moc](06-prad-przemienny.md) | 🟢🔵 | [t. 2, §15.1–15.5](https://openstax.org/books/fizyka-dla-szk%C3%B3%C5%82-wy%C5%BCszych-tom-2/pages/15-1-zrodla-pradu-zmiennego) | t. 3, §31.3–31.5 (s. 389) · wyd. 1: t. 3, §33.6–33.10, s. 330 |
| 07 | [Transformator i przesył energii](07-transformator.md) | 🟢 | [t. 2, §15.6](https://openstax.org/books/fizyka-dla-szk%C3%B3%C5%82-wy%C5%BCszych-tom-2/pages/15-6-transformatory) | t. 3, §31.6 (s. 411) · wyd. 1: t. 3, §33.11, s. 347 |

🟢 matura rozszerzona · 🔵 studia (1. rok) · 🟢🔵 temat maturalny pogłębiany na studiach

## Główne źródła modułu

| Źródło | Zakres |
|---|---|
| [OpenStax, *Fizyka dla szkół wyższych*, t. 2, rozdz. 13](https://openstax.org/books/fizyka-dla-szk%C3%B3%C5%82-wy%C5%BCszych-tom-2/pages/13-wstep) | tekst główny, pytania, zadania z odpowiedziami |
| [OpenStax, *Fizyka dla szkół wyższych*, t. 2, rozdz. 14](https://openstax.org/books/fizyka-dla-szk%C3%B3%C5%82-wy%C5%BCszych-tom-2/pages/14-wstep) | tekst główny, pytania, zadania z odpowiedziami |
| [OpenStax, *Fizyka dla szkół wyższych*, t. 2, rozdz. 15](https://openstax.org/books/fizyka-dla-szk%C3%B3%C5%82-wy%C5%BCszych-tom-2/pages/15-wstep) | tekst główny, pytania, zadania z odpowiedziami |
| Halliday, Resnick, Walker, *Podstawy fizyki*, wyd. 2015: t. 3, rozdz. 30 (od s. 329) | wykład bardziej szczegółowy, zadania i pytania kontrolne |
| Halliday, Resnick, Walker, *Podstawy fizyki*, wyd. 2015: t. 3, rozdz. 31 (od s. 378) | wykład bardziej szczegółowy, zadania i pytania kontrolne |
| Halliday, Resnick, Walker, *Podstawy fizyki*, wyd. 1: t. 3, rozdz. 31 „Zjawisko indukcji i indukcyjność”, od s. 248 (poza zakresem skanu) | to samo w pierwszym wydaniu (PDF z serwera AGH) |
| Halliday, Resnick, Walker, *Podstawy fizyki*, wyd. 1: t. 3, rozdz. 33 „Drgania elektromagnetyczne i prąd zmienny”, od s. 320 (poza zakresem skanu) | to samo w pierwszym wydaniu (PDF z serwera AGH) |

_Lista zostanie uzupełniona o symulacje, zadania maturalne i inne materiały przy wypełnianiu modułu._

## Test wejściowy (diagnoza)

_do uzupełnienia_

## Projekt modułowy

_do uzupełnienia_

## Sprawdzian końcowy modułu

_do uzupełnienia_
