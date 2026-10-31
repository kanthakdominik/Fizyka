# 25 — ściąga: Fizyka obliczeniowa w Pythonie

Wszystkie tabele **Wzory i założenia** z tematów modułu na jednej stronie — do powtórki i do sprawdzenia, czy pamiętasz, **kiedy** wolno użyć wzoru. Wyprowadzenia, przykłady i zadania są w tematach.

[← spis modułu](README.md)

## [25.01 — Python dla fizyka: NumPy, Matplotlib, SciPy](01-python-dla-fizyka.md)

| Wzór | Znaczenie | Kiedy obowiązuje |
|---|---|---|
| $f'(x) \approx \dfrac{f(x + h) - f(x)}{h}$, błąd $\approx \tfrac{h}{2}\lvert f''\rvert + \dfrac{\varepsilon\lvert f\rvert}{h}$ | iloraz przedni | $h_{\text{opt}} \sim \sqrt\varepsilon \approx 10^{-8}$ |
| $f'(x) \approx \dfrac{f(x + h) - f(x - h)}{2h}$, błąd $\approx \tfrac{h^2}{6}\lvert f'''\rvert + \dfrac{\varepsilon\lvert f\rvert}{h}$ | iloraz centralny | $h_{\text{opt}} \sim \varepsilon^{1/3} \approx 10^{-5}$ |
| $\displaystyle\int_a^bf\,dx \approx h\left[\tfrac12f_0 + f_1 + \dots + f_{n-1} + \tfrac12f_n\right]$ | metoda trapezów, błąd $\sim h^2$ | $f$ gładka |
| metoda Simpsona, błąd $\sim h^4$ | parabole przez trzy punkty | parzysta liczba przedziałów |
| $\varepsilon \approx 2{,}2\cdot10^{-16}$ | precyzja maszynowa (`float64`) | — |

## [25.02 — Całkowanie równań ruchu: Euler, Euler–Cromer, Verlet, RK4](02-calkowanie-rownan-ruchu.md)

| Metoda | Krok | Rząd (błąd globalny) | Obliczeń siły na krok | Energia w drganiach |
|---|---|---|---|---|
| Euler | $x \mathrel{+}= hv$, $v \mathrel{+}= ha$ (stare wartości) | $h$ | 1 | rośnie wykładniczo |
| Euler–Cromer | $v \mathrel{+}= ha$, potem $x \mathrel{+}= hv$ | $h$ | 1 | oscyluje, ograniczona |
| Verlet prędkościowy | jak wyżej, ze średnią przyspieszeń | $h^2$ | 1 | oscyluje, ograniczona |
| RK4 | 4 próbki pochodnej | $h^4$ | 4 | bardzo wolno maleje |

Warunek stabilności dla drgań harmonicznych (Euler–Cromer, Verlet): $h\omega < 2$. W praktyce dla dobrej dokładności $h \lesssim T/50$.

## [25.03 — Rzut z oporem, wahadło nieliniowe, orbity planet](03-symulacje-mechaniki.md)

| Wzór | Znaczenie | Kiedy obowiązuje |
|---|---|---|
| $\ddot{\vec r} = \vec g - k\lvert\vec v\rvert\vec v$, $k = \rho C_xA/(2m)$ | rzut z oporem | $\mathrm{Re} \gtrsim 1000$ |
| $v_{gr} = \sqrt{g/k}$ | prędkość graniczna | spadek pionowy |
| $\ddot\theta = -(g/l)\sin\theta$ | wahadło matematyczne | bez tarcia |
| $T = \dfrac{2T_0}{\pi}K(\sin^2\tfrac{\theta_0}{2})$, $T \approx T_0(1 + \theta_0^2/16)$ | okres przy dużej amplitudzie | $K(m)$ — pełna całka eliptyczna |
| $\ddot{\vec r} = -GM\vec r/r^3$, $GM_\odot = 4\pi^2\ \mathrm{AU^3/rok^2}$ | ruch orbitalny | dwa ciała, $M \gg m$ |
| $E = \tfrac12v^2 - GM/r$, $L = \lvert\vec r\times\vec v\rvert$ | zachowane (na jednostkę masy) | test symulacji |

## [25.04 — Dopasowanie modeli do danych pomiarowych](04-dopasowanie-modeli.md)

| Wzór | Znaczenie | Kiedy obowiązuje |
|---|---|---|
| $\chi^2 = \sum\left(\dfrac{y_i - f(x_i)}{u_i}\right)^2$ | miara zgodności | niezależne pomiary, błędy normalne |
| $\nu = n - m$, oczekiwane $\chi^2 \approx \nu \pm \sqrt{2\nu}$ | stopnie swobody | $m$ parametrów |
| $u(p_k) = \sqrt{C_{kk}}$, $\rho_{kl} = \dfrac{C_{kl}}{\sqrt{C_{kk}C_{ll}}}$ | niepewność i korelacja | z macierzy kowariancji |
| $C = (J^TWJ)^{-1}$, $J_{ik} = \partial f(x_i)/\partial p_k$, $W = \mathrm{diag}(1/u_i^2)$ | kowariancja parametrów | przybliżenie liniowe wokół minimum |
| $u(\ln y) = u(y)/y$ | niepewność po linearyzacji | $u(y) \ll y$ |
| $u(N) = \sqrt N$ | niepewność liczby zliczeń | rozkład Poissona (22.03) |

## [25.05 — Pola i potencjały na siatce — równanie Laplace'a](05-pola-na-siatce.md)

| Wzór | Znaczenie | Kiedy obowiązuje |
|---|---|---|
| $\nabla^2V = 0$ | równanie Laplace'a | obszar bez ładunków; też temperatura w stanie ustalonym |
| $\nabla^2V = -\rho/\varepsilon_0$ | równanie Poissona | z ładunkiem |
| $V_{i,j} = \tfrac14(V_{i\pm1,j} + V_{i,j\pm1}) + \tfrac{h^2\rho_{i,j}}{4\varepsilon_0}$ | schemat pięciopunktowy | siatka kwadratowa, błąd $\sim h^2$ |
| $V \leftarrow V + \omega(\bar V_{\text{sąsiadów}} - V)$, $\omega_{\text{opt}} \approx \dfrac{2}{1 + \sin(\pi/N)}$ | nadrelaksacja | — |
| $\vec E = -\nabla V$ | pole z potencjału | — |

## [25.06 — Metody Monte Carlo: rozpad, błądzenie losowe, całkowanie](06-monte-carlo.md)

| Wzór | Znaczenie | Kiedy obowiązuje |
|---|---|---|
| $p = 1 - e^{-\lambda\Delta t}$ | prawdopodobieństwo rozpadu w kroku | jądra niezależne |
| $P(k) = \dfrac{\mu^ke^{-\mu}}{k!}$, $\sigma = \sqrt\mu$ | rozkład Poissona | zdarzenia rzadkie i niezależne |
| $\langle r^2\rangle = Nl^2$ | błądzenie losowe | kroki niezależne |
| $\langle x^2\rangle = 2Dt$, $D = \dfrac{kT}{6\pi\eta r}$ | dyfuzja, ruchy Browna | kulka w cieczy |
| $\displaystyle\int_Vf \approx V\langle f\rangle$, $u = V\sigma_f/\sqrt N$ | całkowanie Monte Carlo | dowolny wymiar |
