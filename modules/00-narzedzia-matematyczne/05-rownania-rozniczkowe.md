# 00.05 — Proste równania różniczkowe w fizyce

> **Moduł:** [00 — Narzędzia matematyczne fizyka](README.md) · **Poziom:** 🔵 studia · **Status:** ✅ pełny
>
> **Czytaj:**
>
> - OpenStax, *Fizyka dla szkół wyższych*, t. 1, rozdz. 15: [§15.1 i §15.5](https://openstax.org/books/fizyka-dla-szk%C3%B3%C5%82-wy%C5%BCszych-tom-1/pages/15-1-ruch-harmoniczny) · [wstęp do rozdziału](https://openstax.org/books/fizyka-dla-szk%C3%B3%C5%82-wy%C5%BCszych-tom-1/pages/15-wstep)
> - Halliday, Resnick, Walker, *Podstawy fizyki*, wyd. 2015, t. 2: §15.1 (s. 116), §15.5 (s. 137)
> - Halliday, Resnick, Walker, *Podstawy fizyki*, wyd. 1 (2003): [t. 2, rozdz. 16](https://home.agh.edu.pl/~czapli/Resnick_2.pdf) — PDF z serwera AGH

← [Całka jako suma: pole pod wykresem, praca, średnia](04-calka.md) · [spis modułu](README.md) · [Przybliżenia i szeregi (małe kąty, dwumian, Taylor)](06-przyblizenia-i-szeregi.md) →

## Po co to jest

Prawa fizyki zwykle mówią, **jak wielkość się zmienia**, a nie ile wynosi: II zasada dynamiki wiąże przyspieszenie (drugą pochodną położenia) z siłą, prawo rozpadu — szybkość ubywania jąder z ich liczbą. Takie związki to **równania różniczkowe**. Trzy równania z tego tematu opisują zaskakująco dużo: rozpad promieniotwórczy, rozładowanie kondensatora, stygnięcie herbaty, spadek ze spadochronem, drgania sprężyny i obwodu LC.

## Teoria w pigułce

**Równanie różniczkowe** to równanie, w którym niewiadomą jest funkcja, a występują w nim jej pochodne. **Rząd** równania to najwyższa pochodna. **Rozwiązanie** to funkcja, która po wstawieniu spełnia równanie tożsamościowo. Rozwiązań jest nieskończenie wiele; jedno wybierają **warunki początkowe** — dla równania 1. rzędu jedna wartość (np. $N(0)$), dla 2. rzędu dwie (np. $x(0)$ i $v(0)$).

**1. Zanik wykładniczy:** $\dfrac{dN}{dt} = -\lambda N$.

Szybkość ubywania jest proporcjonalna do tego, ile jeszcze zostało. Rozdzielamy zmienne i całkujemy:

$$\frac{dN}{N} = -\lambda\,dt \ \Rightarrow\ \ln N = -\lambda t + C \ \Rightarrow\ N(t) = N_0e^{-\lambda t}.$$

Stała czasowa $\tau = 1/\lambda$: po czasie $\tau$ zostaje $1/e \approx 37\%$, po $3\tau$ — ok. 5%, po $5\tau$ — poniżej 1%.

**2. Dążenie do stanu ustalonego:** $\dfrac{dv}{dt} = g - \dfrac{v}{\tau}$.

Tak wygląda spadek z oporem proporcjonalnym do prędkości ($\tau = m/b$). Gdy $v$ rośnie, przyspieszenie maleje; ustala się **prędkość graniczna** $v_g = g\tau$, przy której prawa strona jest zerowa. Podstawiając $u = v - v_g$ dostajemy równanie typu 1, więc

$$v(t) = v_g\left(1 - e^{-t/\tau}\right) \quad\text{dla } v(0) = 0.$$

Ten sam kształt ma ładowanie kondensatora i nagrzewanie się ciała.

**3. Oscylator harmoniczny:** $\ddot{x} = -\omega^2x$.

Przyspieszenie przeciwne do wychylenia. Rozwiązanie ogólne to $x(t) = A\cos(\omega t + \varphi)$ — dwie stałe $A$, $\varphi$ dobieramy z $x(0)$ i $v(0)$. Sprawdzenie: $\ddot{x} = -A\omega^2\cos(\omega t + \varphi) = -\omega^2x$.

**Metoda Eulera.** Gdy równania nie da się rozwiązać na kartce, liczymy krok po kroku: $v_{n+1} = v_n + \dot{v}(t_n, v_n)\,\Delta t$. Prosta, ale przy dużym kroku niedokładna — dokładniejsze metody są w module 25.

## Wzory i założenia

| Równanie | Rozwiązanie | Przykłady |
|---|---|---|
| $\dot{y} = -y/\tau$ | $y = y_0e^{-t/\tau}$ | rozpad ($\tau = 1/\lambda$), rozładowanie $RC$ ($\tau = RC$) |
| $\dot{y} = (y_\infty - y)/\tau$ | $y = y_\infty + (y_0 - y_\infty)e^{-t/\tau}$ | ładowanie $RC$, stygnięcie (prawo Newtona), spadek z oporem liniowym |
| $\ddot{x} = -\omega^2x$ | $x = A\cos(\omega t + \varphi)$, $T = 2\pi/\omega$ | sprężyna ($\omega^2 = k/m$), wahadło dla małych kątów, obwód $LC$ |
| $T_{1/2} = \tau\ln2$ | czas połowicznego zaniku | tylko dla zaniku wykładniczego |
| $A = \sqrt{x_0^2 + (v_0/\omega)^2}$ | amplituda z warunków początkowych | oscylator harmoniczny |

## Przykład rozwiązany

### Wersja z rachunkiem różniczkowym i całkowym

**Zadanie.** Kulka o masie $m = 0{,}1\ \mathrm{kg}$ spada w cieczy z siłą oporu $F_o = bv$, $b = 0{,}05\ \mathrm{kg/s}$ (wypór pomijamy). Startuje z $v = 0$. Oblicz prędkość graniczną, stałą czasową i prędkość po 2 s.

**Równanie ruchu.** $m\dot{v} = mg - bv$, czyli $\dot{v} = g - \dfrac{b}{m}v$.

**Stałe.** $\tau = m/b = 2\ \mathrm{s}$, $v_g = g\tau = 19{,}6\ \mathrm{m/s}$ (gdy $\dot{v} = 0$, opór równoważy ciężar: $bv_g = mg$).

**Rozwiązanie.** Z rozdzielenia zmiennych:

$$\int_0^v\frac{dv'}{v_g - v'} = \int_0^t\frac{dt'}{\tau} \ \Rightarrow\ -\ln\frac{v_g - v}{v_g} = \frac{t}{\tau} \ \Rightarrow\ v = v_g\left(1 - e^{-t/\tau}\right).$$

$v(2\ \mathrm{s}) = 19{,}6\cdot(1 - e^{-1}) \approx 12{,}4\ \mathrm{m/s}$.

**Sprawdzenie.** Dla małych $t$: $e^{-t/\tau} \approx 1 - t/\tau$, więc $v \approx v_gt/\tau = gt$ — na początku kulka spada swobodnie, zanim opór urośnie. Zgadza się.

## Typowe pułapki

- **Brak warunków początkowych.** Rozwiązanie z dowolną stałą to rodzina funkcji; bez $x(0)$, $v(0)$ odpowiedź jest niepełna.
- **Mylenie $\tau$ z $T_{1/2}$.** Po czasie $\tau$ zostaje 37%, a nie 50%. $T_{1/2} = 0{,}693\,\tau$.
- **Znak w równaniu.** $\dot{N} = +\lambda N$ opisuje wzrost wykładniczy, nie zanik. Sprawdź, czy rozwiązanie zachowuje się fizycznie sensownie.
- **Za duży krok w metodzie Eulera.** Dla oscylatora metoda Eulera z każdym okresem zwiększa amplitudę — energia „rośnie z niczego”. Zmniejsz krok albo użyj lepszej metody.
- **Logarytm przy rozdzielaniu zmiennych.** $\int dv/(v_g - v) = -\ln(v_g - v)$ — minus z pochodnej wewnętrznej.

## Doświadczenie / symulacja

**Doświadczenie domowe.** Zmierz termometrem (kuchennym albo z czujnikiem) temperaturę herbaty co 2 minuty przez pół godziny. Narysuj $\ln(T - T_{\text{otoczenia}})$ od czasu: jeśli punkty leżą na prostej, prawo stygnięcia Newtona działa, a nachylenie to $-1/\tau$.

**Python:** metoda Eulera dla spadku z oporem i dla oscylatora.

```python
import numpy as np
import matplotlib.pyplot as plt

g, tau = 9.81, 2.0
dt, t_end = 0.1, 10.0
t = np.arange(0, t_end + dt/2, dt)

# Spadek z oporem liniowym: v' = g - v/τ
v = np.zeros_like(t)
for n in range(len(t) - 1):
    v[n+1] = v[n] + (g - v[n]/tau) * dt
v_exact = g*tau*(1 - np.exp(-t/tau))
print(f"v(2 s): Euler {v[20]:.2f} m/s, dokładnie {v_exact[20]:.2f} m/s")

# Oscylator x'' = -ω² x, metoda Eulera: amplituda rośnie
w = 2.0
x, u = 0.1, 0.0
xs = []
for _ in t:
    xs.append(x)
    x, u = x + u*dt, u - w**2 * x * dt
print(f"amplituda po 10 s (Euler): {max(abs(np.array(xs[-30:]))):.3f} m, powinna być 0,1 m")

fig, ax = plt.subplots(1, 2, figsize=(9, 3.5))
ax[0].plot(t, v, ".", label="Euler"); ax[0].plot(t, v_exact, label="dokładnie")
ax[0].set_xlabel("t [s]"); ax[0].set_ylabel("v [m/s]"); ax[0].legend(); ax[0].grid(True)
ax[1].plot(t, xs, label="Euler"); ax[1].plot(t, 0.1*np.cos(w*t), label="dokładnie")
ax[1].set_xlabel("t [s]"); ax[1].set_ylabel("x [m]"); ax[1].legend(); ax[1].grid(True)
plt.tight_layout(); plt.show()
```

## Zadania

### A. Poziom maturalny _(opcjonalnie — rozgrzewka)_

1. Różnica temperatur herbaty i pokoju maleje $e$-krotnie co 10 minut. Na początku wynosi $70\ ^\circ\mathrm{C}$. Ile wynosi po 20 minutach?

<details>
<summary>Odpowiedź</summary>

$70e^{-2} \approx 9{,}5\ ^\circ\mathrm{C}$.
</details>

2. Czas połowicznego zaniku izotopu wynosi 6 h. Ile wynosi stała czasowa $\tau$? Jaka część jąder zostanie po 18 h?

<details>
<summary>Odpowiedź</summary>

$\tau = 6/\ln2 \approx 8{,}7\ \mathrm{h}$; zostaje $1/8 = 12{,}5\%$.
</details>

### B. Poziom akademicki

1. Kondensator $C = 100\ \mu\mathrm{F}$ rozładowuje się przez opornik $R = 10\ \mathrm{k\Omega}$ zgodnie z $\dot{q} = -q/(RC)$. Ile wynosi stała czasowa i jaka część ładunku zostanie po 3 s?

<details>
<summary>Odpowiedź</summary>

$\tau = RC = 1\ \mathrm{s}$; $e^{-3} \approx 5\%$.
</details>

2. Rozwiąż równanie $\ddot{x} = -4x$ (SI) z warunkami $x(0) = 0{,}1\ \mathrm{m}$, $\dot{x}(0) = 0$. Podaj okres drgań.

<details>
<summary>Odpowiedź</summary>

$x = 0{,}1\cos(2t)$ m, $T = \pi \approx 3{,}14\ \mathrm{s}$.
</details>

3. Ten sam oscylator ($\omega = 2\ \mathrm{s^{-1}}$) startuje z $x(0) = 0$, $\dot{x}(0) = 0{,}6\ \mathrm{m/s}$. Ile wynosi amplituda?

<details>
<summary>Odpowiedź</summary>

$A = v_0/\omega = 0{,}3\ \mathrm{m}$; $x = 0{,}3\sin(2t)$.
</details>

4. Łódź po wyłączeniu silnika hamuje z oporem kwadratowym: $\dot{v} = -kv^2$. Rozwiąż równanie dla $v(0) = v_0$. Czy łódź się zatrzyma w skończonym czasie?

<details>
<summary>Odpowiedź</summary>

$\dfrac{1}{v} = \dfrac{1}{v_0} + kt$, czyli $v = \dfrac{v_0}{1 + kv_0t}$. Prędkość dąży do zera, ale nie osiąga go w skończonym czasie.
</details>

5. Kubek ma temperaturę $90\ ^\circ\mathrm{C}$, pokój $20\ ^\circ\mathrm{C}$, $\tau = 15\ \mathrm{min}$. Po jakim czasie herbata ostygnie do $50\ ^\circ\mathrm{C}$?

<details>
<summary>Odpowiedź</summary>

$t = \tau\ln\dfrac{90 - 20}{50 - 20} = 15\ln\dfrac{7}{3} \approx 12{,}7\ \mathrm{min}$.
</details>

## Źródła

- OpenStax, *Fizyka dla szkół wyższych*, t. 1 — §6.4 (siła oporu i prędkość graniczna), §15.1 (równanie ruchu harmonicznego), §15.5 (drgania tłumione); t. 2, §10.5 (obwody RC).
- Halliday, Resnick, Walker, *Podstawy fizyki*, wyd. 2015, t. 2, rozdz. 15 — §15.1 i §15.5: równanie oscylatora i jego rozwiązanie.
