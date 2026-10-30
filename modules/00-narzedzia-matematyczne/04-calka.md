# 00.04 — Całka jako suma: pole pod wykresem, praca, średnia

> **Moduł:** [00 — Narzędzia matematyczne fizyka](README.md) · **Poziom:** 🔵 studia · **Status:** ✅ pełny
>
> **Czytaj:**
>
> - OpenStax, *Fizyka dla szkół wyższych*, t. 1, rozdz. 3: [§3.6](https://openstax.org/books/fizyka-dla-szk%C3%B3%C5%82-wy%C5%BCszych-tom-1/pages/3-6-wyznaczanie-rownan-ruchu-metoda-calkowania) · [wstęp do rozdziału](https://openstax.org/books/fizyka-dla-szk%C3%B3%C5%82-wy%C5%BCszych-tom-1/pages/3-wstep)
> - Halliday, Resnick, Walker, *Podstawy fizyki*, wyd. 2015, t. 1: §2.6 (s. 36)
> - Halliday, Resnick, Walker, *Podstawy fizyki*, wyd. 1 (2003), t. 1: [§2.7, s. 26](https://home.agh.edu.pl/~czapli/Resnick_1.pdf#page=38) — PDF z serwera AGH

← [Pochodna jako szybkość zmian](03-pochodna.md) · [spis modułu](README.md) · [Proste równania różniczkowe w fizyce](05-rownania-rozniczkowe.md) →

## Po co to jest

Pochodna mówi, jak szybko coś się zmienia; całka pozwala z tej szybkości odtworzyć całkowitą zmianę. Z przyspieszenia liczysz prędkość, z prędkości — położenie, z siły zależnej od położenia — pracę, z natężenia prądu — ładunek. Na maturze ta sama idea występuje jako **pole pod wykresem**. Na studiach całki są wszędzie: praca siły zmiennej (04), środek masy i moment bezwładności (05, 06), potencjał pola (07, 12), prawo Gaussa (12).

## Teoria w pigułce

**Pole pod wykresem.** Jeśli prędkość jest stała, droga to $v\cdot\Delta t$ — pole prostokąta pod wykresem $v(t)$. Gdy prędkość się zmienia, dzielimy czas na małe odcinki $\Delta t_i$, na każdym traktujemy prędkość jako stałą i sumujemy:

$$\Delta x \approx \sum_i v(t_i)\,\Delta t_i \ \xrightarrow{\ \Delta t_i\to0\ }\ \Delta x = \int_{t_1}^{t_2} v(t)\,dt.$$

To jest **całka oznaczona** — granica sumy bardzo wielu bardzo małych składników.

**Całka jako odwrotność pochodnej.** Funkcja $F$, której pochodna to $f$ ($F' = f$), nazywa się **funkcją pierwotną** $f$. Zasadnicze twierdzenie rachunku całkowego:

$$\int_a^b f(x)\,dx = F(b) - F(a).$$

Dlatego, znając $v(t)$, położenie dostajesz jako $x(t) = x_0 + \int_0^t v(t')\,dt'$, a znając $a(t)$ — prędkość $v(t) = v_0 + \int_0^t a(t')\,dt'$. Stałe $x_0$ i $v_0$ to **warunki początkowe** — całka sama ich nie zna.

**Całki w fizyce.**

| Wielkość | Całka |
|---|---|
| przemieszczenie | $\Delta x = \int v\,dt$ |
| zmiana prędkości | $\Delta v = \int a\,dt$ |
| praca siły (1D) | $W = \int F\,dx$ |
| popęd siły | $J = \int F\,dt = \Delta p$ |
| przepływający ładunek | $q = \int I\,dt$ |
| wartość średnia | $\bar{f} = \dfrac{1}{b-a}\int_a^b f\,dx$ |

**Znak.** Pole pod osią liczy się z minusem: ujemna prędkość daje ujemne przemieszczenie. Droga (długość toru) to $\int\lvert v\rvert\,dt$.

## Wzory i założenia

| Całka nieoznaczona | Uwagi |
|---|---|
| $\int x^n\,dx = \dfrac{x^{n+1}}{n+1} + C$ | $n \neq -1$ |
| $\int \dfrac{dx}{x} = \ln\lvert x\rvert + C$ | $x \neq 0$ |
| $\int e^{kx}\,dx = \dfrac{1}{k}e^{kx} + C$ | $k \neq 0$ |
| $\int \sin(\omega t)\,dt = -\dfrac{1}{\omega}\cos(\omega t) + C$ | radiany |
| $\int \cos(\omega t)\,dt = \dfrac{1}{\omega}\sin(\omega t) + C$ | radiany |
| $\int (af + bg)\,dx = a\int f\,dx + b\int g\,dx$ | liniowość |
| $\int f(g(x))\,g'(x)\,dx = \int f(u)\,du$ | podstawienie $u = g(x)$ |
| $\int_a^b f\,dx = -\int_b^a f\,dx$ | zmiana kierunku całkowania zmienia znak |

## Przykład rozwiązany

**Zadanie (poziom maturalny).** Samochód rusza i przez 4 s jednostajnie przyspiesza do $8\ \mathrm{m/s}$, potem jedzie ze stałą prędkością przez 6 s. Jaką drogę przejechał?

Pole pod wykresem $v(t)$: trójkąt $\tfrac12\cdot4\cdot8 = 16\ \mathrm{m}$ plus prostokąt $6\cdot8 = 48\ \mathrm{m}$, razem $64\ \mathrm{m}$.

### Wersja z rachunkiem różniczkowym i całkowym

**Zadanie.** Sprężyna o współczynniku sprężystości $k$ jest rozciągana od długości swobodnej o $x$. Siła potrzebna do utrzymania wydłużenia $s$ wynosi $F = ks$. Oblicz pracę rozciągania.

Siła nie jest stała, więc $W = F\cdot x$ nie działa. Dzielimy rozciąganie na małe przyrosty $ds$, na każdym praca to $F\,ds$:

$$W = \int_0^x ks\,ds = k\left[\frac{s^2}{2}\right]_0^x = \frac{kx^2}{2}.$$

To jest energia potencjalna sprężystości. Geometrycznie — pole trójkąta pod wykresem $F(s)$ o podstawie $x$ i wysokości $kx$.

**Zadanie 2.** Ciało rusza z miejsca z przyspieszeniem $a(t) = 6t$ (m/s², s). Gdzie będzie po 2 s?

$$v(t) = \int_0^t 6t'\,dt' = 3t^2, \qquad x(t) = \int_0^t 3t'^2\,dt' = t^3, \qquad x(2) = 8\ \mathrm{m}.$$

Wzór $x = \tfrac12at^2$ dałby tu zły wynik — obowiązuje tylko przy stałym przyspieszeniu.

## Typowe pułapki

- **Wzory ruchu jednostajnie przyspieszonego przy zmiennym przyspieszeniu.** Gdy $a$ zależy od czasu, trzeba całkować.
- **Zapominanie o stałej całkowania.** Całka nieoznaczona jest wyznaczona z dokładnością do stałej; tę stałą ustala warunek początkowy.
- **Mylenie przemieszczenia z drogą.** Gdy prędkość zmienia znak, $\int v\,dt$ to przemieszczenie, a droga to $\int\lvert v\rvert\,dt$.
- **Jednostki pola pod wykresem.** Pole ma jednostkę „$y$ razy $x$”: pod $F(x)$ — dżule, pod $I(t)$ — kulomby.
- **Granice całkowania po podstawieniu.** Zmieniając zmienną, zmień też granice (albo wróć do starej zmiennej przed wstawieniem granic).

## Doświadczenie / symulacja

**Python:** całkowanie numeryczne metodą trapezów. Tak opracowuje się dane z czujnika przyspieszenia w telefonie: z $a(t)$ dostajemy $v(t)$, z $v(t)$ — $x(t)$. Zwróć uwagę, jak szybko narasta błąd położenia, gdy przyspieszenie ma mały stały błąd (dryf czujnika).

```python
import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import trapezoid, cumulative_trapezoid

t = np.linspace(0, 2, 201)
a = 6 * t                                         # a(t) = 6t z przykładu
v = cumulative_trapezoid(a, t, initial=0)
x = cumulative_trapezoid(v, t, initial=0)
print(f"x(2) numerycznie = {x[-1]:.4f} m (dokładnie 8 m)")

# Praca sprężyny k = 200 N/m przy wydłużeniu 0,1 m
s = np.linspace(0, 0.1, 51)
print(f"W = {trapezoid(200 * s, s):.4f} J (dokładnie 1 J)")

# Dryf: czujnik zawyża przyspieszenie o 0,05 m/s²
x_drift = cumulative_trapezoid(cumulative_trapezoid(a + 0.05, t, initial=0), t, initial=0)
plt.plot(t, x, label="dokładnie")
plt.plot(t, x_drift, "--", label="z dryfem 0,05 m/s²")
plt.xlabel("t [s]"); plt.ylabel("x [m]"); plt.grid(True); plt.legend(); plt.show()
```

## Zadania

### A. Poziom maturalny _(opcjonalnie — rozgrzewka)_

1. Prąd o stałym natężeniu $2\ \mathrm{A}$ płynął przez 30 s, potem przez 10 s malał jednostajnie do zera. Jaki ładunek przepłynął?

<details>
<summary>Odpowiedź</summary>

$2\cdot30 + \tfrac12\cdot2\cdot10 = 70\ \mathrm{C}$.
</details>

2. Siła rozciągająca sprężynę rośnie liniowo od 0 do $20\ \mathrm{N}$ przy wydłużeniu od 0 do $0{,}1\ \mathrm{m}$. Oblicz pracę z pola pod wykresem $F(x)$.

<details>
<summary>Odpowiedź</summary>

$W = \tfrac12\cdot0{,}1\cdot20 = 1\ \mathrm{J}$.
</details>

3. Wykres $v(t)$: od 0 do 2 s prędkość rośnie liniowo od 0 do $4\ \mathrm{m/s}$, od 2 do 4 s maleje liniowo do $-4\ \mathrm{m/s}$. Oblicz przemieszczenie i drogę po 4 s.

<details>
<summary>Odpowiedź</summary>

Pole nad osią: trójkąt $0$–$3\ \mathrm{s}$ o polu $\tfrac12\cdot3\cdot4 = 6\ \mathrm{m}$; pod osią: trójkąt $3$–$4\ \mathrm{s}$ o polu $\tfrac12\cdot1\cdot4 = 2\ \mathrm{m}$. Przemieszczenie $4\ \mathrm{m}$, droga $8\ \mathrm{m}$.
</details>

### B. Poziom akademicki

1. Oblicz $\displaystyle\int_0^{\pi}\sin x\,dx$ oraz średnią wartość funkcji $\sin^2(\omega t)$ w jednym okresie. (Wskazówka: $\sin^2\alpha = \tfrac12(1 - \cos2\alpha)$.)

<details>
<summary>Odpowiedź</summary>

$2$; średnia $\sin^2$ wynosi $\tfrac12$ — dlatego wartość skuteczna prądu sinusoidalnego to $I_0/\sqrt2$.
</details>

2. Na ciało działa siła $F(x) = 3x^2$ (N, m). Oblicz pracę przy przesunięciu od $x = 1\ \mathrm{m}$ do $x = 2\ \mathrm{m}$.

<details>
<summary>Odpowiedź</summary>

$W = [x^3]_1^2 = 7\ \mathrm{J}$.
</details>

3. Podczas uderzenia w piłkę siła zmienia się jak $F(t) = F_0\sin(\pi t/T)$ dla $0 \le t \le T$, gdzie $F_0 = 500\ \mathrm{N}$, $T = 0{,}01\ \mathrm{s}$. Oblicz popęd siły i średnią siłę.

<details>
<summary>Odpowiedź</summary>

$J = \dfrac{2F_0T}{\pi} \approx 3{,}18\ \mathrm{N\cdot s}$; $\bar{F} = J/T = 2F_0/\pi \approx 318\ \mathrm{N}$.
</details>

4. Oblicz pracę potrzebną do oddalenia ciała o masie $m$ z powierzchni planety (promień $R$, masa $M$) do nieskończoności. Siła grawitacji: $F = GMm/r^2$.

<details>
<summary>Odpowiedź</summary>

$W = \displaystyle\int_R^{\infty}\frac{GMm}{r^2}\,dr = \frac{GMm}{R}$. Wynik jest skończony mimo nieskończonej drogi.
</details>

5. Prędkość ciała: $v(t) = v_0e^{-t/\tau}$. Jaką drogę przebędzie ciało do całkowitego zatrzymania ($t\to\infty$)?

<details>
<summary>Odpowiedź</summary>

$s = \displaystyle\int_0^\infty v_0e^{-t/\tau}\,dt = v_0\tau$.
</details>

## Źródła

- OpenStax, *Fizyka dla szkół wyższych*, t. 1, rozdz. 3 — §3.6: wyznaczanie prędkości i położenia przez całkowanie przyspieszenia.
- Halliday, Resnick, Walker, *Podstawy fizyki*, wyd. 2015, t. 1, rozdz. 2 — §2.6: całkowanie graficzne w analizie ruchu; rozdz. 7, §7.5: praca siły zmiennej.
