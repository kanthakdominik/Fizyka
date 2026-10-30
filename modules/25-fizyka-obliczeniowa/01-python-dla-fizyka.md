# 25.01 — Python dla fizyka: NumPy, Matplotlib, SciPy

> **Moduł:** [25 — Fizyka obliczeniowa w Pythonie](README.md) · **Poziom:** 🔵 studia · **Status:** ✅ pełny
>
> **Czytaj:**
>
> - _Podręczniki główne nie mają osobnego paragrafu na ten temat — materiały są w sekcji „Źródła”._

← (początek modułu) · [spis modułu](README.md) · [Całkowanie równań ruchu: Euler, Euler–Cromer, Verlet, RK4](02-calkowanie-rownan-ruchu.md) →

## Po co to jest

Większości realnych problemów fizyki nie da się rozwiązać „na kartce”: opór powietrza zależny od kwadratu prędkości, wahadło o dużej amplitudzie, ruch trzech ciał, pole w pudle o dowolnym kształcie. Komputer rozwiązuje je w kilka sekund. Python z bibliotekami NumPy, SciPy i Matplotlib stał się standardem w fizyce: od analizy danych z laboratorium szkolnego i phyphox po obróbkę danych z LHC i teleskopów. Ten temat zbiera narzędzia używane w całym kursie (w każdym temacie jest blok kodu) i uczy, czemu ufać w wyniku numerycznym, a czemu nie.

## Teoria w pigułce

**Środowisko.** Wystarczy Python 3 z bibliotekami `numpy`, `scipy`, `matplotlib` (instalacja: `pip install numpy scipy matplotlib`). Wygodne są notatniki Jupyter albo Google Colab (działa w przeglądarce, bez instalacji).

**NumPy — tablice zamiast pętli.** Operacje działają na całych tablicach naraz (wektoryzacja), co jest zwięzłe i 10–100 razy szybsze od pętli w Pythonie:

```python
import numpy as np

g = 9.81
t = np.linspace(0, 3, 7)            # 7 równo rozłożonych chwil od 0 do 3 s
h = 45 - g*t**2/2                   # wysokość w spadku swobodnym z 45 m — dla całej tablicy naraz
for ti, hi in zip(t, h):
    print(f"t = {ti:.1f} s   h = {hi:6.2f} m")
print("czas spadku:", np.sqrt(2*45/g), "s")
```

Najważniejsze funkcje: `np.linspace`, `np.arange`, `np.zeros`, operacje element po elemencie (`+`, `*`, `**`, `np.sin`, `np.exp`), `np.sum`, `np.mean`, `np.std`, `np.diff`, `np.cumsum`, `np.gradient`, `np.loadtxt` (wczytywanie danych z pliku CSV, np. eksportu z phyphox).

**Matplotlib — wykresy.** `plt.plot(x, y)`, `plt.errorbar(x, y, yerr=u)`, opisy osi z jednostkami, `plt.legend()`, `plt.grid(True)`, `plt.savefig("wykres.png", dpi=200)`.

**SciPy — gotowe metody numeryczne:**

| Zadanie | Funkcja | Przykład w kursie |
|---|---|---|
| stałe fizyczne | `scipy.constants` | $h$, $c$, $k_B$, $e$ |
| całka oznaczona | `scipy.integrate.quad` | praca, rozkład Plancka (20.01) |
| całka z danych | `scipy.integrate.trapezoid`, `simpson` | droga z wykresu prędkości |
| pierwiastek równania | `scipy.optimize.brentq` | prawo Wiena, poziomy w studni (20.06) |
| równania różniczkowe | `scipy.integrate.solve_ivp` | ruch z oporem (25.03) |
| dopasowanie modelu | `scipy.optimize.curve_fit` | 25.04 |
| funkcje specjalne | `scipy.special` | całki eliptyczne (wahadło), funkcje Bessela |

**Arytmetyka zmiennoprzecinkowa.** Liczby typu `float` mają ok. 16 cyfr znaczących (precyzja maszynowa $\varepsilon \approx 2{,}2\cdot10^{-16}$). Konsekwencje:
- `0.1 + 0.2 == 0.3` daje `False`. Liczby porównuje się z tolerancją: `np.isclose`.
- **Utrata cyfr znaczących przy odejmowaniu** bliskich liczb: $1 - \cos(10^{-8})$ daje 0 zamiast $5\cdot10^{-17}$. Pomaga przekształcenie wzoru: $1 - \cos x = 2\sin^2(x/2)$.
- Zakres: ok. $10^{-308}$ do $10^{308}$. Funkcje takie jak `np.expm1`, `np.log1p` liczą $e^x - 1$ i $\ln(1 + x)$ dokładnie dla małych $x$.

**Pochodna numeryczna.** Iloraz różnicowy przedni $\dfrac{f(x + h) - f(x)}{h}$ ma błąd $\sim h$, centralny $\dfrac{f(x + h) - f(x - h)}{2h}$ — błąd $\sim h^2$. Zbyt małe $h$ zwiększa jednak błąd zaokrągleń, który rośnie jak $\varepsilon/h$.

## Wzory i założenia

| Wzór | Znaczenie | Kiedy obowiązuje |
|---|---|---|
| $f'(x) \approx \dfrac{f(x + h) - f(x)}{h}$, błąd $\approx \tfrac{h}{2}\lvert f''\rvert + \dfrac{\varepsilon\lvert f\rvert}{h}$ | iloraz przedni | $h_{\text{opt}} \sim \sqrt\varepsilon \approx 10^{-8}$ |
| $f'(x) \approx \dfrac{f(x + h) - f(x - h)}{2h}$, błąd $\approx \tfrac{h^2}{6}\lvert f'''\rvert + \dfrac{\varepsilon\lvert f\rvert}{h}$ | iloraz centralny | $h_{\text{opt}} \sim \varepsilon^{1/3} \approx 10^{-5}$ |
| $\displaystyle\int_a^bf\,dx \approx h\left[\tfrac12f_0 + f_1 + \dots + f_{n-1} + \tfrac12f_n\right]$ | metoda trapezów, błąd $\sim h^2$ | $f$ gładka |
| metoda Simpsona, błąd $\sim h^4$ | parabole przez trzy punkty | parzysta liczba przedziałów |
| $\varepsilon \approx 2{,}2\cdot10^{-16}$ | precyzja maszynowa (`float64`) | — |

## Przykład rozwiązany

**Zadanie.** Oblicz pochodną $\sin x$ w $x = 1$ ilorazem przednim i centralnym dla $h = 10^{-2}, 10^{-4}, \dots, 10^{-12}$ i porównaj z $\cos 1$.

| $h$ | błąd przedni | błąd centralny |
|---|---|---|
| $10^{-2}$ | $4{,}2\cdot10^{-3}$ | $9\cdot10^{-6}$ |
| $10^{-4}$ | $4{,}2\cdot10^{-5}$ | $9\cdot10^{-10}$ |
| $10^{-6}$ | $4{,}2\cdot10^{-7}$ | $3\cdot10^{-11}$ |
| $10^{-8}$ | $3\cdot10^{-9}$ | $3\cdot10^{-9}$ |
| $10^{-12}$ | $4\cdot10^{-5}$ | $1\cdot10^{-5}$ |

Błąd maleje proporcjonalnie do $h$ (przedni) i $h^2$ (centralny), aż zaczynają dominować zaokrąglenia. Dla $h = 10^{-12}$ wynik jest gorszy niż dla $h = 10^{-2}$.

### Wersja z rachunkiem różniczkowym i całkowym

**Skąd się bierze optymalne $h$.** Z rozwinięcia Taylora $f(x + h) = f + hf' + \tfrac{h^2}{2}f'' + \dots$ błąd obcięcia ilorazu przedniego to $\tfrac h2f''$. Wartości funkcji są obarczone błędem zaokrąglenia ok. $\varepsilon f$, który po podzieleniu przez $h$ daje $\varepsilon f/h$. Całkowity błąd

$$E(h) = \frac h2\lvert f''\rvert + \frac{\varepsilon\lvert f\rvert}{h}, \qquad E'(h) = 0 \Rightarrow h_{\text{opt}} = \sqrt{\frac{2\varepsilon\lvert f\rvert}{\lvert f''\rvert}} \approx 2\cdot10^{-8},$$

a najmniejszy osiągalny błąd jest rzędu $\sqrt\varepsilon \approx 10^{-8}$. Dla ilorazu centralnego $E(h) = \tfrac{h^2}{6}\lvert f'''\rvert + \varepsilon\lvert f\rvert/h$, więc $h_{\text{opt}} \sim \varepsilon^{1/3} \approx 10^{-5}$ i błąd ok. $10^{-11}$, zgodnie z tabelą.

## Typowe pułapki

- **„Komputer liczy dokładnie”.** Każdy wynik numeryczny ma błąd metody (obcięcia) i błąd zaokrągleń. Zawsze sprawdzaj wynik na przypadku ze znanym rozwiązaniem i przy zmienionym kroku.
- **Mniejszy krok zawsze daje lepszy wynik.** Tylko do pewnej granicy. Potem rosną błędy zaokrągleń i czas obliczeń.
- **Mieszanie jednostek.** Kod nie pilnuje jednostek. Najlepiej liczyć konsekwentnie w SI, a jednostki zapisywać w komentarzach i nazwach zmiennych.
- **`np.trapz` i stare przykłady z internetu.** Nazwy funkcji się zmieniają (w NumPy 2.0 `np.trapz` zastąpiono `np.trapezoid`). Bezpieczniej używać `scipy.integrate.trapezoid`.
- **Pętla po elementach tablicy** tam, gdzie wystarczy działanie na całej tablicy. Kod jest wolniejszy i dłuższy.

## Doświadczenie / symulacja

**Własne dane z phyphox.** Nagraj w phyphox przyspieszenie windy lub spadającego telefonu (na poduszkę), wyeksportuj CSV, wczytaj `np.loadtxt(..., delimiter=",", skiprows=1)` i scałkuj numerycznie przyspieszenie do prędkości i położenia (`scipy.integrate.cumulative_trapezoid`). Zobacz, jak szybko narasta błąd całkowania przy niezerowym przesunięciu (offsecie) czujnika.

**Python:** zestaw podstawowych narzędzi — pochodna numeryczna i jej błąd, całkowanie trapezami i Simpsonem, pierwiastek równania (prawo Wiena) i całka niewłaściwa (prawo Stefana–Boltzmanna).

```python
import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import quad, trapezoid, simpson
from scipy.optimize import brentq
from scipy import constants as C

hs = np.logspace(-14, -1, 60)
przedni = np.abs((np.sin(1 + hs) - np.sin(1))/hs - np.cos(1))
centralny = np.abs((np.sin(1 + hs) - np.sin(1 - hs))/(2*hs) - np.cos(1))
print(f"najlepsze h: przedni {hs[np.argmin(przedni)]:.0e}, centralny {hs[np.argmin(centralny)]:.0e}")

for n in (5, 11, 21, 41):
    x = np.linspace(0, np.pi, n)
    print(f"n = {n:2d}: trapezy błąd {abs(trapezoid(np.sin(x), x) - 2):.1e}, Simpson błąd {abs(simpson(np.sin(x), x=x) - 2):.1e}")

xw = brentq(lambda x: 5*(1 - np.exp(-x)) - x, 1, 10)     # maksimum rozkładu Plancka: x = hc/(λ k T)
print(f"x = {xw:.6f}, stała Wiena b = hc/(x k) = {C.h*C.c/(xw*C.k):.4e} m·K")
I = quad(lambda x: x**3/np.expm1(x), 0, 50)[0]
print(f"∫ x³/(eˣ − 1) dx = {I:.6f} (π⁴/15 = {np.pi**4/15:.6f})")
sigma = 2*np.pi**5*C.k**4/(15*C.h**3*C.c**2)
print(f"stała Stefana–Boltzmanna z całki: {sigma:.4e} W/(m²K⁴) (scipy: {C.sigma:.4e})")
print("0.1 + 0.2 == 0.3:", 0.1 + 0.2 == 0.3, "| np.isclose:", np.isclose(0.1 + 0.2, 0.3))
print(f"1 − cos(1e-8) = {1 - np.cos(1e-8)}, 2 sin²(5e-9) = {2*np.sin(0.5e-8)**2:.3e}")

plt.loglog(hs, przedni, label="iloraz przedni"); plt.loglog(hs, centralny, label="iloraz centralny")
plt.xlabel("h"); plt.ylabel("błąd pochodnej"); plt.legend(); plt.grid(True, which="both"); plt.show()
```

## Zadania

### A. Poziom maturalny _(opcjonalnie — rozgrzewka)_

1. Napisz program, który dla rzutu pionowego w górę z prędkością 20 m/s wypisze co 0,5 s wysokość i prędkość aż do upadku. Kiedy ciało osiąga maksymalną wysokość?

<details>
<summary>Odpowiedź</summary>

`t = np.arange(0, 4.1, 0.5); h = 20*t - 9.81*t**2/2; v = 20 - 9.81*t`. Maksimum przy $t = 20/9{,}81 \approx 2{,}04\ \mathrm s$, $h_{\max} \approx 20{,}4\ \mathrm m$, upadek po ok. 4,08 s.
</details>

2. Dlaczego w programie `0.1 + 0.2 == 0.3` daje `False`?

<details>
<summary>Odpowiedź</summary>

Liczby 0,1 i 0,2 nie mają skończonego zapisu dwójkowego. Komputer przechowuje ich przybliżenia i suma różni się od przybliżenia 0,3 o ok. $5\cdot10^{-17}$.
</details>

### B. Poziom akademicki

1. Wyznacz stałą Wiena: maksimum rozkładu Plancka w funkcji długości fali spełnia $5(1 - e^{-x}) = x$, gdzie $x = hc/(\lambda kT)$. Rozwiąż równanie numerycznie.

<details>
<summary>Odpowiedź</summary>

`brentq` w przedziale [1, 10] daje $x = 4{,}9651$, czyli $b = hc/(xk) = 2{,}898\cdot10^{-3}\ \mathrm{m\cdot K}$.
</details>

2. Oblicz numerycznie $\displaystyle\int_0^\infty\frac{x^3}{e^x - 1}dx$ i porównaj z $\pi^4/15$. Wyprowadź z niej stałą Stefana–Boltzmanna $\sigma = \dfrac{2\pi^5k^4}{15h^3c^2}$.

<details>
<summary>Odpowiedź</summary>

6,493939 (zgodnie z $\pi^4/15$ do 9 cyfr). $\sigma \approx 5{,}670\cdot10^{-8}\ \mathrm{W/(m^2K^4)}$.
</details>

3. Oblicz $\int_0^\pi\sin x\,dx$ metodą trapezów i Simpsona dla 4, 10, 20 i 40 przedziałów. Ile razy maleje błąd, gdy podwajasz liczbę przedziałów? Co z tego wynika o rzędzie metod?

<details>
<summary>Odpowiedź</summary>

Trapezy: błąd maleje ok. 4 razy (rząd $h^2$; 0,104 → 0,016 → 0,0041 → 0,0010). Simpson: ok. 16 razy (rząd $h^4$; $1{,}1\cdot10^{-4} \to 6{,}8\cdot10^{-6} \to 4{,}2\cdot10^{-7}$).
</details>

4. Policz $\dfrac{\sqrt{1 + x} - 1}{x}$ dla $x = 10^{-15}$ bezpośrednio i po przekształceniu do $\dfrac{1}{\sqrt{1 + x} + 1}$. Wyjaśnij różnicę.

<details>
<summary>Odpowiedź</summary>

Wzór bezpośredni daje ok. 0,444 (zamiast 0,5), bo $\sqrt{1 + x}$ i 1 różnią się dopiero na 16. cyfrze i odejmowanie traci prawie wszystkie cyfry znaczące. Postać przekształcona daje 0,5 z pełną dokładnością.
</details>

## Źródła

- Dokumentacja Pythona — [samouczek w języku polskim](https://docs.python.org/pl/3/tutorial/) (rozdz. 3–5: liczby, listy, pętle, funkcje; rozdz. 15: arytmetyka zmiennoprzecinkowa).
- Z. Fortuna, B. Macukow, J. Wąsowski, *Metody numeryczne*, WNT/PWN — rozdziały o błędach numerycznych, różniczkowaniu i całkowaniu.
- M. Newman, *Computational Physics* — przykładowe rozdziały 2–5 ([websites.umich.edu/~mejn/cp/chapters.html](https://websites.umich.edu/~mejn/cp/chapters.html)): Python dla fizyka, wykresy, dokładność, całki i pochodne (materiał dodatkowy, po angielsku).
- Moduły 00.03 (pochodna) i 00.04 (całka) — podstawy matematyczne.
