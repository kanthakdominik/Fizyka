# 16 — Równania Maxwella i fale elektromagnetyczne

> **Status:** ✅ pełny · **Poziom:** 🟢🔵 · **Odpowiednik:** Fizyka II — równania Maxwella, fale EM · **Czas:** 15–25 h od zera

## Cel modułu

Zebrać elektromagnetyzm w czterech równaniach Maxwella, wyprowadzić z nich falę elektromagnetyczną i opisać jej energię, pęd i widmo.

## Wymagania wstępne

- [15 Indukcja elektromagnetyczna i prąd przemienny](../15-indukcja-i-prad-przemienny/)
- [10 Fale mechaniczne i akustyka](../10-fale-i-akustyka/)

## Tematy

| # | Temat | Poziom | OpenStax (PL) | Halliday — wyd. 2015 (paragraf, strona) · wyd. 1 (PDF) |
|---|---|---|---|---|
| 01 | [Prąd przesunięcia i równania Maxwella](01-prad-przesuniecia-i-rownania-maxwella.md) | 🔵 | [t. 2, §16.1](https://openstax.org/books/fizyka-dla-szk%C3%B3%C5%82-wy%C5%BCszych-tom-2/pages/16-1-rownania-maxwella-i-fale-elektromagnetyczne) | t. 3, §32.1–32.3 (s. 426) · wyd. 1: t. 3, §32.2, s. 290, §32.9–32.11, s. 306 |
| 02 | [Płaska fala elektromagnetyczna](02-fala-elektromagnetyczna.md) | 🔵 | [t. 2, §16.2](https://openstax.org/books/fizyka-dla-szk%C3%B3%C5%82-wy%C5%BCszych-tom-2/pages/16-2-plaskie-fale-elektromagnetyczne) | t. 4, §33.1 (s. 1) · wyd. 1: t. 4, [§34.1–34.3, s. 2](https://home.agh.edu.pl/~czapli/Resnick_4.pdf#page=17) |
| 03 | [Energia, wektor Poyntinga i ciśnienie promieniowania](03-energia-i-ped-fali.md) | 🔵 | [t. 2, §16.3–16.4](https://openstax.org/books/fizyka-dla-szk%C3%B3%C5%82-wy%C5%BCszych-tom-2/pages/16-3-energia-niesiona-przez-fale-elektromagnetyczne) | t. 4, §33.2–33.3 (s. 11) · wyd. 1: t. 4, [§34.4–34.5, s. 11](https://home.agh.edu.pl/~czapli/Resnick_4.pdf#page=26) |
| 04 | [Widmo fal elektromagnetycznych](04-widmo-fal-em.md) | 🟢 | [t. 2, §16.5](https://openstax.org/books/fizyka-dla-szk%C3%B3%C5%82-wy%C5%BCszych-tom-2/pages/16-5-widmo-promieniowania-elektromagnetycznego) | t. 4, §33.1 (s. 1) · wyd. 1: t. 4, [§34.1, s. 2](https://home.agh.edu.pl/~czapli/Resnick_4.pdf#page=17) |

🟢 matura rozszerzona · 🔵 studia (1. rok) · 🟢🔵 temat maturalny pogłębiany na studiach

## Główne źródła modułu

| Źródło | Zakres |
|---|---|
| [OpenStax, *Fizyka dla szkół wyższych*, t. 2, rozdz. 16](https://openstax.org/books/fizyka-dla-szk%C3%B3%C5%82-wy%C5%BCszych-tom-2/pages/16-wstep) | tekst główny, pytania, zadania z odpowiedziami |
| Halliday, Resnick, Walker, *Podstawy fizyki*, wyd. 2015: t. 3, rozdz. 32 (od s. 426) | wykład bardziej szczegółowy, zadania i pytania kontrolne |
| Halliday, Resnick, Walker, *Podstawy fizyki*, wyd. 2015: t. 4, rozdz. 33 (od s. 1) | wykład bardziej szczegółowy, zadania i pytania kontrolne |
| Halliday, Resnick, Walker, *Podstawy fizyki*, wyd. 1: t. 3, rozdz. 32 „Magnetyzm materii; równania Maxwella”, od s. 290 (poza zakresem skanu) | to samo w pierwszym wydaniu (PDF z serwera AGH) |
| Halliday, Resnick, Walker, *Podstawy fizyki*, wyd. 1: [t. 4, rozdz. 34 „Fale elektromagnetyczne”, od s. 2](https://home.agh.edu.pl/~czapli/Resnick_4.pdf#page=17) | to samo w pierwszym wydaniu (PDF z serwera AGH) |

## Test wejściowy (diagnoza)

Rozwiąż bez notatek, około 30 minut.

1. Zapisz prawo Gaussa dla pola elektrycznego i prawo Faradaya w postaci całkowej.
2. Oblicz gęstość energii pola elektrycznego 1000 V/m i pola magnetycznego 1 mT.
3. Fala na strunie ma postać $y = A\sin(kx - \omega t)$. Podaj jej prędkość i kierunek ruchu.
4. Oblicz $\vec a\times\vec b$ dla $\vec a = \hat x$, $\vec b = \hat y$, a następnie $\hat y\times\hat x$.
5. Źródło dźwięku o mocy 1 W promieniuje równomiernie. Jakie natężenie jest w odległości 2 m?
6. Ile wynosi średnia z $\sin^2(\omega t)$ w okresie?

<details>
<summary>Odpowiedzi</summary>

1. $\oint\vec E\cdot d\vec A = Q/\varepsilon_0$; $\oint\vec E\cdot d\vec l = -d\Phi_B/dt$
2. $\tfrac12\varepsilon_0E^2 \approx 4{,}4\cdot10^{-6}\ \mathrm{J/m^3}$; $B^2/(2\mu_0) \approx 0{,}40\ \mathrm{J/m^3}$
3. $v = \omega/k$, w stronę $+x$
4. $\hat z$; $-\hat z$
5. $I = 1/(4\pi\cdot4) \approx 0{,}02\ \mathrm{W/m^2}$
6. $\tfrac12$
</details>

## Projekt modułowy: fale elektromagnetyczne w domu

- [ ] **Prędkość światła z mikrofalówki.** Zmierz odległość między stopionymi plamami czekolady (sera) w kuchence bez talerza obrotowego. Z częstotliwości z tabliczki oblicz $c$ z niepewnością. Powtórz trzy razy w różnych miejscach komory.
- [ ] **Polaryzacja fal.** Sprawdź, jak zmienia się poziom sygnału Wi-Fi (aplikacja do analizy sieci) albo jasność ekranu LCD oglądanego przez okulary polaryzacyjne, gdy obracasz telefon lub okulary. Opisz wynik za pomocą kierunku wektora $\vec E$.
- [ ] **Ekranowanie.** Zbadaj, które materiały blokują sygnał telefonu lub Wi-Fi (folia aluminiowa, siatka metalowa o różnych oczkach, woda w pojemniku, karton). Wyjaśnij wyniki porównaniem rozmiaru oczek z długością fali.
- [ ] W sprawozdaniu podaj długości fal wszystkich użytych źródeł i oszacuj energię ich fotonów.

## Sprawdzian końcowy modułu

- [ ] Wyjaśniam prąd przesunięcia, zapisuję cztery równania Maxwella i interpretuję każde z nich.
- [ ] Wyprowadzam równanie falowe dla pól $E$ i $B$, stosuję $c = 1/\sqrt{\mu_0\varepsilon_0}$, $E = cB$ i poprzeczność fali.
- [ ] Liczę gęstość energii, wektor Poyntinga, natężenie, pęd i ciśnienie promieniowania.
- [ ] Znam zakresy widma elektromagnetycznego, ich źródła, zastosowania i oddziaływanie z materią; przeliczam długość fali, częstotliwość i energię fotonu.
