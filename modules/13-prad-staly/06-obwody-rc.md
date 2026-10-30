# 13.06 — Obwody RC — ładowanie i rozładowanie

> **Moduł:** [13 — Prąd stały](README.md) · **Poziom:** 🔵 studia · **Status:** ✅ pełny
>
> **Czytaj:**
>
> - OpenStax, *Fizyka dla szkół wyższych*, t. 2, rozdz. 10: [§10.5](https://openstax.org/books/fizyka-dla-szk%C3%B3%C5%82-wy%C5%BCszych-tom-2/pages/10-5-obwody-rc) · [wstęp do rozdziału](https://openstax.org/books/fizyka-dla-szk%C3%B3%C5%82-wy%C5%BCszych-tom-2/pages/10-wstep)
> - Halliday, Resnick, Walker, *Podstawy fizyki*, wyd. 2015, t. 3: §27.4 (s. 231)
> - Halliday, Resnick, Walker, *Podstawy fizyki*, wyd. 1 (2003), t. 3: §28.8, s. 171 (skan t. 3 na serwerze AGH kończy się na s. 127 — dalsze strony tylko w wydaniu papierowym)

← [Prawa Kirchhoffa i mierniki](05-prawa-kirchhoffa.md) · [spis modułu](README.md) · (koniec modułu) →

## Po co to jest

Kondensator nie ładuje się natychmiast. Prąd ładowania płynie przez opornik i maleje wykładniczo. Stała czasowa $RC$ odmierza czas w układach czasowych (np. popularny układ 555), ustala częstotliwość migania kierunkowskazu, opóźnienie wyłącznika światła na klatce schodowej i czas ładowania lampy błyskowej. Na niej opierają się filtry dolno- i górnoprzepustowe w elektronice audio i zasilaczach. To także pierwsze równanie różniczkowe w obwodach, wstęp do obwodów RL i RLC (15).

## Teoria w pigułce

**Ładowanie.** W chwili $t = 0$ zamykamy obwód: źródło $\varepsilon$, opornik $R$, nienaładowany kondensator $C$. Z II prawa Kirchhoffa (13.05):

$$\varepsilon - IR - \frac qC = 0, \qquad I = \frac{dq}{dt} \quad\Rightarrow\quad R\frac{dq}{dt} + \frac qC = \varepsilon.$$

Rozwiązanie przy $q(0) = 0$:

$$q(t) = C\varepsilon\left(1 - e^{-t/\tau}\right), \qquad I(t) = \frac\varepsilon Re^{-t/\tau}, \qquad \tau = RC.$$

- Na początku kondensator zachowuje się jak zwarcie: $I_0 = \varepsilon/R$.
- Po długim czasie zachowuje się jak przerwa: $I \to 0$, $U_C \to \varepsilon$.
- Po czasie $\tau$ kondensator ma 63% ładunku końcowego, po $3\tau$ 95%, po $5\tau$ 99,3%.

**Rozładowanie** przez opornik $R$, od ładunku $Q_0$:

$$q(t) = Q_0e^{-t/\tau}, \qquad I(t) = -\frac{Q_0}{RC}e^{-t/\tau}.$$

Po czasie $\tau\ln2 \approx 0{,}69\tau$ zostaje połowa ładunku, jak przy rozpadzie promieniotwórczym (22).

**Bilans energii przy ładowaniu.** Źródło wykonuje pracę $Q\varepsilon = C\varepsilon^2$, a kondensator gromadzi $\tfrac12C\varepsilon^2$ (12.06). Druga połowa zamienia się w ciepło w oporniku, niezależnie od wartości $R$.

Jednostka $[RC] = \Omega\cdot\mathrm F = \dfrac{\mathrm V}{\mathrm A}\cdot\dfrac{\mathrm C}{\mathrm V} = \mathrm s$.

## Wzory i założenia

| Wzór | Znaczenie | Kiedy obowiązuje |
|---|---|---|
| $\tau = RC$ | stała czasowa | — |
| $q = C\varepsilon(1 - e^{-t/\tau})$, $\ I = (\varepsilon/R)e^{-t/\tau}$ | ładowanie | $q(0) = 0$ |
| $q = Q_0e^{-t/\tau}$ | rozładowanie | — |
| $t_{1/2} = \tau\ln2$ | czas połowicznego rozładowania | — |
| $W_{\text{źr}} = C\varepsilon^2$, $W_C = W_R = \tfrac12C\varepsilon^2$ | bilans energii ładowania | pełne naładowanie |

## Przykład rozwiązany

**Zadanie.** Kondensator 100 μF ładujemy z baterii 9 V przez opornik 10 kΩ. Oblicz stałą czasową, prąd początkowy, czas do osiągnięcia 90% napięcia końcowego oraz energię zgromadzoną i straconą.

$\tau = 10^4\cdot10^{-4} = 1\ \mathrm s$. $I_0 = 9/10^4 = 0{,}9\ \mathrm{mA}$.

90%: $1 - e^{-t/\tau} = 0{,}9 \Rightarrow t = \tau\ln10 \approx 2{,}3\ \mathrm s$.

Energia w kondensatorze: $\tfrac12\cdot10^{-4}\cdot81 \approx 4{,}1\ \mathrm{mJ}$. Tyle samo wydzieliło się w oporniku, a bateria oddała 8,1 mJ.

### Wersja z rachunkiem różniczkowym i całkowym

**Rozwiązanie równania ładowania.** Rozdzielamy zmienne:

$$\frac{dq}{C\varepsilon - q} = \frac{dt}{RC} \quad\Rightarrow\quad -\ln\frac{C\varepsilon - q}{C\varepsilon} = \frac{t}{RC} \quad\Rightarrow\quad q = C\varepsilon\left(1 - e^{-t/RC}\right).$$

**Ciepło w oporniku:**

$$W_R = \int_0^\infty I^2R\,dt = \frac{\varepsilon^2}{R}\int_0^\infty e^{-2t/RC}dt = \frac{\varepsilon^2}{R}\cdot\frac{RC}{2} = \frac12C\varepsilon^2.$$

## Typowe pułapki

- **Kondensator naładuje się do końca po czasie $\tau$.** Po $\tau$ ma 63%. Teoretycznie nigdy nie naładuje się w pełni. Praktycznie po $5\tau$.
- **Prąd ładowania rośnie.** Prąd jest największy na początku i maleje wykładniczo. Rośnie napięcie na kondensatorze.
- **Mniejszy opór zmniejszy straty energii.** Straty to zawsze $\tfrac12C\varepsilon^2$. Mniejszy opór tylko przyspiesza ładowanie. Uniknąć strat da się, ładując stopniowo rosnącym napięciem.
- **$\tau$ w mikrosekundach.** μF × kΩ = ms, μF × MΩ = s. Warto sprawdzić rzędy wielkości.
- **Stan ustalony: prąd płynie przez kondensator.** W stanie ustalonym prądu stałego przez kondensator prąd nie płynie.

## Doświadczenie / symulacja

**Rozładowanie kondensatora i pomiar $\tau$.** Kondensator elektrolityczny 1000 μF naładuj z baterii 9 V, a potem rozładowuj przez opornik 10 kΩ ($\tau = 10\ \mathrm s$). Odczytuj napięcie miernikiem co 5 s (najwygodniej nagrać ekran miernika telefonem). Narysuj $\ln U$ od $t$ i wyznacz $\tau$ z nachylenia. Porównaj z $RC$ z wartości nominalnych. Elektrolity mają tolerancję nawet ±20%.

**Arduino jako oscyloskop.** Arduino z wejściem analogowym zapisuje krzywe ładowania z rozdzielczością milisekund (np. $R = 10\ \mathrm{k\Omega}$, $C = 10\ \mu\mathrm F$, $\tau = 0{,}1\ \mathrm s$).

**Symulacja PhET:** *Zestaw do budowy obwodów AC* (*Circuit Construction Kit: AC*) zawiera kondensatory i wykres prądu w czasie.

**Python:** ładowanie i rozładowanie — rozwiązanie numeryczne i wzór, oraz wyznaczanie $\tau$ z „pomiarów”.

```python
import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp

R, C, eps = 1e4, 1e-4, 9.0
tau = R*C
sol = solve_ivp(lambda t, q: [(eps - q[0]/C)/R], (0, 5*tau), [0.0], max_step=0.01)
t = sol.t; U = sol.y[0]/C
print(f"τ = {tau:.2f} s, U(τ) numerycznie = {np.interp(tau, t, U):.3f} V, wzór = {eps*(1 - np.exp(-1)):.3f} V")
print(f"90 % po {tau*np.log(10):.2f} s; energia w C = {0.5*C*eps**2*1e3:.2f} mJ")

rng = np.random.default_rng(0)                         # symulowany pomiar rozładowania 1000 µF / 10 kΩ
tp = np.arange(0, 40, 5.0)
Up = 9*np.exp(-tp/10.0)*(1 + 0.01*rng.standard_normal(tp.size))
a, b = np.polyfit(tp, np.log(Up), 1)
print(f"τ z dopasowania prostej do ln U: {-1/a:.2f} s (nominalnie 10 s)")

plt.plot(t, U, label="U_C ładowanie"); plt.plot(t, eps*np.exp(-t/tau), "--", label="U_R = R·I")
plt.axvline(tau, color="gray", ls=":"); plt.xlabel("t [s]"); plt.ylabel("U [V]"); plt.grid(True); plt.legend(); plt.show()
```

## Zadania

### A. Poziom maturalny _(opcjonalnie — rozgrzewka)_

1. Oblicz stałą czasową obwodu z opornikiem 47 kΩ i kondensatorem 22 μF.

<details>
<summary>Odpowiedź</summary>

$\tau \approx 1{,}03\ \mathrm s$.
</details>

2. Po jakim czasie (w jednostkach $\tau$) rozładowywany kondensator ma połowę ładunku, a po jakim połowę energii?

<details>
<summary>Odpowiedź</summary>

Połowa ładunku po $\tau\ln2 \approx 0{,}69\tau$. Energia $\propto q^2$, więc połowa energii po $\tfrac12\tau\ln2 \approx 0{,}35\tau$.
</details>

### B. Poziom akademicki

1. Wyłącznik światła na klatce schodowej ma wyłączać lampę, gdy napięcie na kondensatorze 470 μF (naładowanym do 12 V) spadnie do 4 V. Jaki opór rozładowania da czas 2 minut?

<details>
<summary>Odpowiedź</summary>

$t = RC\ln(12/4) \Rightarrow R = 120/(470\cdot10^{-6}\cdot\ln3) \approx 232\ \mathrm{k\Omega}$.
</details>

2. Kondensator ładuje się przez opornik $R$ ze źródła $\varepsilon$. Pokaż, że chwilowa moc dostarczana do kondensatora jest największa, gdy napięcie na nim wynosi $\varepsilon/2$.

<details>
<summary>Odpowiedź</summary>

$P_C = U_CI = U_C\dfrac{\varepsilon - U_C}{R}$, maksimum dla $U_C = \varepsilon/2$, czyli w chwili $t = \tau\ln2$.
</details>

3. Ładujemy kondensator dwuetapowo: najpierw do $\varepsilon/2$ ze źródła $\varepsilon/2$, potem do $\varepsilon$ ze źródła $\varepsilon$. Pokaż, że straty w oporniku są dwa razy mniejsze niż przy ładowaniu jednym skokiem.

<details>
<summary>Odpowiedź</summary>

W każdym etapie strata to $\tfrac12C(\Delta U)^2 = \tfrac12C(\varepsilon/2)^2$, razem $\tfrac14C\varepsilon^2$ zamiast $\tfrac12C\varepsilon^2$. Przy $n$ etapach strata maleje jak $1/n$, co wykorzystują układy ładowania „adiabatycznego”.
</details>

4. Kondensator $C$ połączony równolegle z opornikiem $R_2$ ładuje się ze źródła $\varepsilon$ przez opornik $R_1$. Wyznacz napięcie końcowe na kondensatorze i stałą czasową ładowania. Jaka jest stała czasowa rozładowania po odłączeniu źródła?

<details>
<summary>Odpowiedź</summary>

Z praw Kirchhoffa: $C\dfrac{dU}{dt} = \dfrac{\varepsilon - U}{R_1} - \dfrac{U}{R_2}$. Stan końcowy $U_\infty = \varepsilon\dfrac{R_2}{R_1 + R_2}$, stała czasowa ładowania $\tau = C\dfrac{R_1R_2}{R_1 + R_2}$ (źródło zastępcze Thevenina). Po odłączeniu źródła kondensator rozładowuje się tylko przez $R_2$: $\tau = R_2C$.
</details>

## Źródła

- OpenStax, *Fizyka dla szkół wyższych*, t. 2, rozdz. 10 — §10.5: obwody RC.
- Halliday, Resnick, Walker, *Podstawy fizyki* — wyd. 2015: t. 3, §27.4; wyd. 1: t. 3, §28.8.
