# 25 — Fizyka obliczeniowa w Pythonie

> **Status:** ✅ pełny · **Poziom:** 🟢🔵 · **Odpowiednik:** Metody numeryczne / Fizyka komputerowa (wstęp) · **Czas:** 30–50 h od zera

## Cel modułu

Rozwiązywać numerycznie to, czego nie da się policzyć na kartce: równania ruchu, nieliniowe oscylatory, orbity, pola na siatce, dopasowanie modeli i symulacje Monte Carlo.

## Wymagania wstępne

- [00 Narzędzia matematyczne fizyka](../00-narzedzia-matematyczne/)
- [01 Pomiar, jednostki i niepewności](../01-pomiary-i-niepewnosci/)

## Tematy

| # | Temat | Poziom | OpenStax (PL) | Halliday — wyd. 2015 (paragraf, strona) · wyd. 1 (PDF) |
|---|---|---|---|---|
| 01 | [Python dla fizyka: NumPy, Matplotlib, SciPy](01-python-dla-fizyka.md) | 🔵 | — | — |
| 02 | [Całkowanie równań ruchu: Euler, Euler–Cromer, Verlet, RK4](02-calkowanie-rownan-ruchu.md) | 🔵 | — | — |
| 03 | [Rzut z oporem, wahadło nieliniowe, orbity planet](03-symulacje-mechaniki.md) | 🔵 | — | — |
| 04 | [Dopasowanie modeli do danych pomiarowych](04-dopasowanie-modeli.md) | 🟢🔵 | — | — |
| 05 | [Pola i potencjały na siatce — równanie Laplace'a](05-pola-na-siatce.md) | 🔵 | — | — |
| 06 | [Metody Monte Carlo: rozpad, błądzenie losowe, całkowanie](06-monte-carlo.md) | 🔵 | — | — |

🟢 matura rozszerzona · 🔵 studia (1. rok) · 🟢🔵 temat maturalny pogłębiany na studiach

Wszystkie wzory modułu na jednej stronie: **[ściąga](SCIAGA.md)**.

## Główne źródła modułu

| Źródło | Zakres |
|---|---|
| [Symulacje PhET — wersja polska](https://phet.colorado.edu/pl/) | *Ładunki i pola* (25.05) |
| [phyphox](https://phyphox.org/) — pomiary smartfonem | doświadczenia w tematach 25.01, 25.02, 25.03, 25.04 |
| [Tracker](https://physlets.org/tracker/) — analiza ruchu z nagrania | temat 25.03 |
| [`scipy.optimize.curve_fit`](https://docs.scipy.org/doc/scipy/reference/generated/scipy.optimize.curve_fit.html) | temat 25.04 (materiał dodatkowy, po angielsku) |
| [Dokumentacja Pythona — samouczek](https://docs.python.org/pl/3/tutorial/) | podstawy języka, po polsku |
| Z. Fortuna, B. Macukow, J. Wąsowski, *Metody numeryczne*, WNT/PWN | podręcznik akademicki: błędy, całkowanie, równania różniczkowe, aproksymacja |
| B. Zglinicki, *Programowanie i metody numeryczne* (Wydział Fizyki UW) — ćwiczenia: [zestaw 12 (Monte Carlo)](https://www.fuw.edu.pl/~bzglinicki/teaching/pmn/cwiczenia/12/PMN_Cwiczenia-12.pdf), [zestaw 14 (równania cząstkowe)](https://www.fuw.edu.pl/~bzglinicki/teaching/pmn/cwiczenia/14) | zadania z metod numerycznych, po polsku |
| [M. Newman, *Computational Physics* — rozdziały przykładowe](https://websites.umich.edu/~mejn/cp/chapters.html) | Python dla fizyka, dokładność obliczeń, całki i pochodne (materiał dodatkowy, po angielsku) |
| Dokumentacja [NumPy](https://numpy.org/doc/stable/), [SciPy](https://docs.scipy.org/doc/scipy/) i [Matplotlib](https://matplotlib.org/stable/) | opis funkcji (po angielsku) |

## Test wejściowy (diagnoza)

Rozwiąż bez notatek, około 30 minut. Pytania 5–6 sprawdzają podstawy programowania. Jeśli ich nie znasz, zacznij od rozdziałów 3–5 polskiego samouczka Pythona (link w temacie 25.01).

1. Oblicz pochodną $x(t) = 3\sin(2t)$ i drugą pochodną. Jakie równanie różniczkowe spełnia $x(t)$?
2. Rozwiń $e^h$ w szereg Taylora do wyrazu $h^3$. Jaki jest błąd przybliżenia $e^h \approx 1 + h$ dla $h = 0{,}1$?
3. Oblicz $\int_0^2x^2\,dx$ dokładnie i metodą trapezów z dwoma przedziałami.
4. Zmierzono 5 razy okres: 2,01; 1,98; 2,03; 2,00; 1,99 s. Oblicz średnią i niepewność standardową średniej.
5. Co wypisze program: `s = 0` / `for i in range(1, 5): s = s + i` / `print(s)`?
6. Napisz funkcję w Pythonie, która dla masy $m$ i prędkości $v$ zwraca energię kinetyczną.

<details>
<summary>Odpowiedzi</summary>

1. $\dot x = 6\cos(2t)$, $\ddot x = -12\sin(2t) = -4x$; równanie oscylatora $\ddot x = -4x$
2. $1 + h + h^2/2 + h^3/6$; błąd ok. $h^2/2 = 0{,}005$ (dokładnie 0,00517)
3. $8/3 \approx 2{,}667$; trapezy: $1\cdot(0/2 + 1 + 4/2) = 3$
4. $\bar T = 2{,}002\ \mathrm s$, $u = s/\sqrt5 \approx 0{,}009\ \mathrm s$
5. 10
6. `def ek(m, v): return m*v**2/2`
</details>

## Projekt modułowy: od pomiaru do modelu numerycznego

- [ ] **Pomiar.** Wybierz jedno zjawisko: wahadło o dużej amplitudzie, drgania tłumione telefonu na sprężynie lub spadek lekkiego ciała (muffinka papierowa, balonik) z oporem powietrza. Zmierz przebieg w phyphox lub nagraj film i odczytaj położenia (Tracker).
- [ ] **Model i symulacja.** Zapisz równanie ruchu z wszystkimi istotnymi siłami i rozwiąż je numerycznie (Verlet lub `solve_ivp`). Sprawdź zbieżność względem kroku i test na przypadku z rozwiązaniem analitycznym.
- [ ] **Dopasowanie.** Dopasuj nieznane parametry modelu (np. współczynnik oporu, tłumienie) do danych pomiarowych z niepewnościami. Podaj $\chi^2/\nu$ i wykres reszt.
- [ ] **Monte Carlo niepewności.** Powtórz dopasowanie dla 500 zestawów danych z dodanym szumem o wielkości niepewności pomiaru i porównaj rozrzut parametrów z niepewnościami z macierzy kowariancji.
- [ ] W sprawozdaniu (Jupyter lub PDF) oceń, które założenia modelu najbardziej ograniczają zgodność z pomiarem.

## Sprawdzian końcowy modułu

- [ ] Posługuję się NumPy (tablice, wektoryzacja), Matplotlib (wykresy z opisami i niepewnościami) i SciPy (`quad`, `brentq`, `solve_ivp`, `curve_fit`); rozumiem precyzję maszynową i utratę cyfr znaczących.
- [ ] Implementuję metody Eulera, Eulera–Cromera, Verleta i RK4; wyznaczam rząd metody z wykresu błędu i wyjaśniam zachowanie energii w każdej z nich.
- [ ] Symuluję rzut z oporem kwadratowym, wahadło nieliniowe i orbity; sprawdzam wynik testem analitycznym, zbieżnością i zasadami zachowania.
- [ ] Dopasowuję modele liniowe i nieliniowe z niepewnościami, interpretuję macierz kowariancji, $\chi^2/\nu$ i reszty; poprawnie linearyzuję zależności.
- [ ] Rozwiązuję równanie Laplace'a i Poissona na siatce (Jacobi, nadrelaksacja), wyznaczam pole z potencjału i rysuję ekwipotencjale.
- [ ] Stosuję metody Monte Carlo: symuluję rozpad i błądzenie losowe, liczę całki z niepewnością $\sim1/\sqrt N$ i wyjaśniam, kiedy ta metoda wygrywa z siatkową.
