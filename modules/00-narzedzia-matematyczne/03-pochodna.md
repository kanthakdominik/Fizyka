# 00.03 — Pochodna jako szybkość zmian

> **Moduł:** [00 — Narzędzia matematyczne fizyka](README.md) · **Poziom:** 🟢🔵 matura R + studia · **Status:** ✅ pełny
>
> **Czytaj:**
>
> - OpenStax, *Fizyka dla szkół wyższych*, t. 1, rozdz. 3: [§3.2–3.3](https://openstax.org/books/fizyka-dla-szk%C3%B3%C5%82-wy%C5%BCszych-tom-1/pages/3-2-predkosc-chwilowa-i-szybkosc-srednia) · [wstęp do rozdziału](https://openstax.org/books/fizyka-dla-szk%C3%B3%C5%82-wy%C5%BCszych-tom-1/pages/3-wstep)
> - Halliday, Resnick, Walker, *Podstawy fizyki*, wyd. 2015, t. 1: §2.2–2.3 (s. 22)
> - Halliday, Resnick, Walker, *Podstawy fizyki*, wyd. 1 (2003), t. 1: [§2.4–2.5, s. 18](https://home.agh.edu.pl/~czapli/Resnick_1.pdf#page=30) — PDF z serwera AGH

← [Funkcje i wykresy w fizyce, linearyzacja](02-funkcje-i-wykresy.md) · [spis modułu](README.md) · [Całka jako suma: pole pod wykresem, praca, średnia](04-calka.md) →

## Po co to jest

Fizyka opisuje, **jak szybko coś się zmienia**: prędkość to szybkość zmiany położenia, przyspieszenie — szybkość zmiany prędkości, natężenie prądu — szybkość przepływu ładunku, moc — szybkość wykonywania pracy. Wszystkie te definicje to pochodne. Na maturze wystarczy rozumieć pochodną jako nachylenie stycznej do wykresu i umieć ją policzyć dla wielomianu (to jest też w maturze rozszerzonej z matematyki). Na studiach pochodna jest podstawowym językiem — bez niej nie zapiszesz żadnego równania ruchu.

## Teoria w pigułce

**Szybkość średnia a chwilowa.** Prędkość średnia na odcinku czasu to $\bar{v} = \Delta x/\Delta t$ — nachylenie siecznej wykresu $x(t)$. Gdy $\Delta t$ dąży do zera, sieczna przechodzi w styczną, a iloraz różnicowy w **pochodną**:

$$v(t) = \frac{dx}{dt} = \lim_{\Delta t\to 0}\frac{x(t+\Delta t) - x(t)}{\Delta t}.$$

**Interpretacja geometryczna.** Pochodna w punkcie to nachylenie stycznej do wykresu w tym punkcie. Dodatnia — funkcja rośnie, ujemna — maleje, zero — funkcja ma poziomą styczną (często maksimum albo minimum).

**Pochodne w fizyce.**

| Wielkość | Definicja |
|---|---|
| prędkość | $v = \dfrac{dx}{dt}$ |
| przyspieszenie | $a = \dfrac{dv}{dt} = \dfrac{d^2x}{dt^2}$ |
| natężenie prądu | $I = \dfrac{dq}{dt}$ |
| moc | $P = \dfrac{dW}{dt}$ |
| siła zachowawcza (1D) | $F = -\dfrac{dU}{dx}$ |
| siła wypadkowa (II zasada w ogólnej postaci) | $F = \dfrac{dp}{dt}$ |

**Notacja.** Pochodną po czasie fizycy często zapisują kropką: $\dot{x} = dx/dt$, $\ddot{x} = d^2x/dt^2$. Pochodną po innej zmiennej — primem: $f'(x)$.

**Ekstremum.** Jeśli funkcja ma w punkcie wewnętrznym maksimum albo minimum, to jej pochodna jest tam równa zeru. Tak liczy się np. największą wysokość w rzucie (prędkość pionowa = 0) albo położenie równowagi ($dU/dx = 0$).

## Wzory i założenia

| Wzór | Uwagi |
|---|---|
| $(c)' = 0$, $(x^n)' = nx^{n-1}$ | $n$ dowolne rzeczywiste, np. $(\sqrt{x})' = \tfrac{1}{2\sqrt{x}}$, $(1/x)' = -1/x^2$ |
| $(cf)' = cf'$, $(f + g)' = f' + g'$ | liniowość |
| $(fg)' = f'g + fg'$ | iloczyn |
| $\left(\dfrac{f}{g}\right)' = \dfrac{f'g - fg'}{g^2}$ | iloraz, $g \neq 0$ |
| $\dfrac{d}{dt}f(g(t)) = f'(g(t))\cdot g'(t)$ | pochodna złożenia (reguła łańcuchowa) |
| $(\sin x)' = \cos x$, $(\cos x)' = -\sin x$ | $x$ w **radianach** |
| $(e^{x})' = e^{x}$, $(e^{kx})' = ke^{kx}$, $(\ln x)' = 1/x$ | $x > 0$ dla logarytmu |
| $\dfrac{d}{dt}\sin(\omega t) = \omega\cos(\omega t)$ | reguła łańcuchowa w drganiach |

## Przykład rozwiązany

**Zadanie.** Położenie ciała na prostej opisuje wzór $x(t) = 5 + 12t - 2t^2$ (w metrach i sekundach). Wyznacz prędkość i przyspieszenie, chwilę zatrzymania i największe położenie.

**Prędkość i przyspieszenie.**

$$v(t) = \frac{dx}{dt} = 12 - 4t\ \ \mathrm{[m/s]}, \qquad a(t) = \frac{dv}{dt} = -4\ \mathrm{m/s^2}.$$

Przyspieszenie jest stałe, więc to ruch jednostajnie zmienny (porównaj z $x = x_0 + v_0t + \tfrac12at^2$: $x_0 = 5\ \mathrm{m}$, $v_0 = 12\ \mathrm{m/s}$, $a = -4\ \mathrm{m/s^2}$).

**Zatrzymanie.** $v = 0 \Rightarrow t = 3\ \mathrm{s}$.

**Największe położenie.** W chwili $t = 3\ \mathrm{s}$ prędkość zmienia znak z dodatniego na ujemny, więc $x$ ma maksimum: $x(3) = 5 + 36 - 18 = 23\ \mathrm{m}$.

**Sprawdzenie.** Jednostki: $[12] = \mathrm{m/s}$, $[2] = \mathrm{m/s^2}$, więc $[4t] = \mathrm{m/s}$ — zgadza się.

### Wersja z rachunkiem różniczkowym i całkowym

**Zadanie.** Ciało drga zgodnie z $x(t) = A\sin(\omega t)$. Pokaż, że $a = -\omega^2x$, i znajdź największą prędkość.

Z reguły łańcuchowej:

$$v = \dot{x} = A\omega\cos(\omega t), \qquad a = \ddot{x} = -A\omega^2\sin(\omega t) = -\omega^2 x.$$

Przyspieszenie jest proporcjonalne do wychylenia i do niego przeciwne — to jest definicja ruchu harmonicznego (moduł 09). Największa prędkość: $v_{\max} = A\omega$, osiągana w położeniu równowagi ($x = 0$, gdzie $\lvert\cos\rvert = 1$).

## Typowe pułapki

- **Prędkość średnia ≠ średnia prędkości.** $\bar{v} = \Delta x/\Delta t$, a nie $(v_1 + v_2)/2$ — te wielkości są równe tylko przy stałym przyspieszeniu.
- **Stopnie w funkcjach trygonometrycznych.** Wzór $(\sin x)' = \cos x$ działa tylko w radianach.
- **Zapomniana pochodna wewnętrzna.** $\dfrac{d}{dt}\cos(3t) = -3\sin(3t)$, a nie $-\sin(3t)$.
- **Pochodna zero to nie zawsze ekstremum.** Dla $x = t^3$ w $t = 0$ pochodna jest zerowa, a funkcja rośnie dalej. Sprawdzaj zmianę znaku pochodnej.
- **Nachylenie z kratek.** Na wykresie nachylenie stycznej liczysz w jednostkach osi, a nie w kratkach papieru.

## Doświadczenie / symulacja

**Doświadczenie z telefonem.** W phyphox (eksperyment *Acceleration (without g)*) zarejestruj przyspieszenie telefonu przesuwanego po stole. Zwróć uwagę, że telefon mierzy $a(t)$, a położenie i prędkość trzeba by uzyskać całkowaniem — to temat 04.

**Python:** pochodna numeryczna z danych pomiarowych. Iloraz różnicowy „w przód” ma błąd rzędu $h$, a centralny — rzędu $h^2$; szum pomiarowy jest przy różniczkowaniu wzmacniany.

```python
import numpy as np
import matplotlib.pyplot as plt

t = np.linspace(0, 6, 61)               # krok h = 0,1 s
x = 5 + 12*t - 2*t**2                   # położenie z przykładu
v_true = 12 - 4*t

v_fwd = (x[1:] - x[:-1]) / (t[1] - t[0])          # różnica w przód
v_cen = np.gradient(x, t)                          # różnica centralna (wewnątrz)
print("max błąd w przód  :", np.max(np.abs(v_fwd - v_true[:-1])))
print("max błąd centralny:", np.max(np.abs(v_cen[1:-1] - v_true[1:-1])))

rng = np.random.default_rng(0)
x_noisy = x + rng.normal(0, 0.02, x.size)          # pomiar z niepewnością 2 cm
v_noisy = np.gradient(x_noisy, t)

plt.plot(t, v_true, label="dokładnie")
plt.plot(t, v_noisy, ".", label="z danych z szumem")
plt.xlabel("t [s]"); plt.ylabel("v [m/s]"); plt.grid(True); plt.legend(); plt.show()
```

## Zadania

### A. Poziom maturalny

1. Położenie ciała: $x(t) = 4t^2 - 8t + 1$ (m, s). Wyznacz $v(t)$, chwilę, w której ciało się zatrzymuje, i położenie w tej chwili.

<details>
<summary>Odpowiedź</summary>

$v = 8t - 8$; $t = 1\ \mathrm{s}$; $x(1) = -3\ \mathrm{m}$.
</details>

2. Styczna do wykresu $x(t)$ w chwili $t = 2\ \mathrm{s}$ przechodzi przez punkty $(1\ \mathrm{s};\ 2\ \mathrm{m})$ i $(3\ \mathrm{s};\ 8\ \mathrm{m})$. Ile wynosi prędkość chwilowa w $t = 2\ \mathrm{s}$?

<details>
<summary>Odpowiedź</summary>

$v = \dfrac{8 - 2}{3 - 1} = 3\ \mathrm{m/s}$.
</details>

3. Wysokość piłki rzuconej pionowo: $h(t) = 20t - 5t^2$ (m, s). Oblicz największą wysokość.

<details>
<summary>Odpowiedź</summary>

$\dot{h} = 20 - 10t = 0 \Rightarrow t = 2\ \mathrm{s}$, $h_{\max} = 20\ \mathrm{m}$.
</details>

4. Energia potencjalna ciała zależy od położenia: $U(x) = 2x^2$ (J, m). Oblicz siłę działającą na ciało w punkcie $x = 3\ \mathrm{m}$.

<details>
<summary>Odpowiedź</summary>

$F = -dU/dx = -4x = -12\ \mathrm{N}$ (zwrócona do położenia $x = 0$).
</details>

### B. Poziom akademicki

1. Wychylenie oscylatora: $x(t) = 0{,}5\sin(4t)$ (m, s). Oblicz największą prędkość i największe przyspieszenie.

<details>
<summary>Odpowiedź</summary>

$v_{\max} = 0{,}5\cdot4 = 2\ \mathrm{m/s}$, $a_{\max} = 0{,}5\cdot16 = 8\ \mathrm{m/s^2}$.
</details>

2. Ładunek na rozładowującym się kondensatorze: $q(t) = q_0e^{-t/\tau}$, $q_0 = 2\ \mathrm{mC}$, $\tau = 0{,}5\ \mathrm{s}$. Oblicz natężenie prądu w chwili $t = 0$ i $t = 1\ \mathrm{s}$.

<details>
<summary>Odpowiedź</summary>

$I = -\dfrac{q_0}{\tau}e^{-t/\tau}$; $\lvert I(0)\rvert = 4\ \mathrm{mA}$, $\lvert I(1)\rvert = 4e^{-2} \approx 0{,}54\ \mathrm{mA}$.
</details>

3. Prędkość ciała: $v(t) = \sqrt{1 + t^2}$ (m/s, s). Oblicz przyspieszenie w chwili $t = 1\ \mathrm{s}$.

<details>
<summary>Odpowiedź</summary>

$a = \dfrac{t}{\sqrt{1+t^2}}$, $a(1) = 1/\sqrt{2} \approx 0{,}71\ \mathrm{m/s^2}$.
</details>

4. Energia oddziaływania dwóch atomów: $U(r) = \dfrac{A}{r^{12}} - \dfrac{B}{r^{6}}$, $A, B > 0$. Znajdź odległość równowagi $r_0$.

<details>
<summary>Odpowiedź</summary>

$U'(r) = -\dfrac{12A}{r^{13}} + \dfrac{6B}{r^7} = 0 \Rightarrow r_0 = \left(\dfrac{2A}{B}\right)^{1/6}$.
</details>

5. Pęd ciała zmienia się zgodnie z $p(t) = 3t^2 + 2$ (kg·m/s, s). Jaka siła działa na ciało w chwili $t = 2\ \mathrm{s}$?

<details>
<summary>Odpowiedź</summary>

$F = dp/dt = 6t = 12\ \mathrm{N}$.
</details>

## Źródła

- OpenStax, *Fizyka dla szkół wyższych*, t. 1, rozdz. 3 — §3.2 (prędkość chwilowa jako pochodna) i §3.3 (przyspieszenie chwilowe), z przykładami liczonymi pochodną.
- Halliday, Resnick, Walker, *Podstawy fizyki*, wyd. 2015, t. 1, rozdz. 2 — §2.2–2.3, w tym wyprowadzenie pochodnej z ilorazu różnicowego.
