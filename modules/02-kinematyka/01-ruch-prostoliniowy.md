# 02.01 — Ruch prostoliniowy: położenie, prędkość, przyspieszenie

> **Moduł:** [02 — Kinematyka](README.md) · **Poziom:** 🟢🔵 matura R + studia · **Status:** ✅ pełny
>
> **Czytaj:**
>
> - OpenStax, *Fizyka dla szkół wyższych*, t. 1, rozdz. 3: [§3.1–3.3](https://openstax.org/books/fizyka-dla-szk%C3%B3%C5%82-wy%C5%BCszych-tom-1/pages/3-1-polozenie-przemieszczenie-predkosc-srednia) · [wstęp do rozdziału](https://openstax.org/books/fizyka-dla-szk%C3%B3%C5%82-wy%C5%BCszych-tom-1/pages/3-wstep)
> - Halliday, Resnick, Walker, *Podstawy fizyki*, wyd. 2015, t. 1: §2.1–2.3 (s. 16)
> - Halliday, Resnick, Walker, *Podstawy fizyki*, wyd. 1 (2003), t. 1: [§2.1–2.5, s. 14](https://home.agh.edu.pl/~czapli/Resnick_1.pdf#page=26) — PDF z serwera AGH

← (początek modułu) · [spis modułu](README.md) · [Ruch jednostajnie zmienny i spadek swobodny](02-ruch-jednostajnie-zmienny.md) →

## Po co to jest

Kinematyka opisuje ruch bez pytania o jego przyczyny: gdzie ciało jest, jak szybko się porusza i jak szybko zmienia prędkość. Ruch po prostej to najprostszy przypadek, na którym uczymy się rozróżniać położenie i drogę, prędkość i szybkość, wartość średnią i chwilową. Te rozróżnienia wracają w każdym kolejnym module — od rzutów (02.05) po drgania (09) i fale (10).

## Teoria w pigułce

**Układ odniesienia.** Ruch opisujemy względem wybranego ciała i osi z zaznaczonym początkiem i zwrotem. Położenie na prostej to współrzędna $x$ — liczba ze znakiem.

**Przemieszczenie a droga.**
- Przemieszczenie $\Delta x = x_2 - x_1$ — zmiana położenia, może być ujemne albo zerowe.
- Droga $s$ — długość przebytego toru, zawsze nieujemna. Jeśli ciało zawraca, droga jest większa od $\lvert\Delta x\rvert$.

**Prędkość średnia a szybkość średnia.**

$$\bar{v} = \frac{\Delta x}{\Delta t}, \qquad \bar{v}_s = \frac{s}{\Delta t}.$$

Biegacz, który zrobił pełne okrążenie stadionu, ma prędkość średnią zero, ale szybkość średnią równą długości bieżni podzielonej przez czas.

**Prędkość chwilowa** to granica prędkości średniej dla coraz krótszego przedziału czasu — nachylenie stycznej do wykresu $x(t)$:

$$v = \lim_{\Delta t\to 0}\frac{\Delta x}{\Delta t} = \frac{dx}{dt}.$$

Szybkość chwilowa to wartość bezwzględna prędkości $\lvert v\rvert$ — to pokazuje prędkościomierz.

**Przyspieszenie** opisuje zmianę prędkości:

$$\bar{a} = \frac{\Delta v}{\Delta t}, \qquad a = \frac{dv}{dt} = \frac{d^2x}{dt^2}.$$

Znak przyspieszenia nie mówi, czy ciało przyspiesza czy hamuje. Ciało **przyspiesza**, gdy $v$ i $a$ mają ten sam znak, a **hamuje**, gdy mają znaki przeciwne.

**Trzy wykresy.** Nachylenie wykresu $x(t)$ to prędkość, nachylenie wykresu $v(t)$ to przyspieszenie. Pole pod wykresem $v(t)$ to przemieszczenie, pole pod wykresem $a(t)$ — zmiana prędkości.

## Wzory i założenia

| Wzór | Znaczenie | Kiedy obowiązuje |
|---|---|---|
| $\Delta x = x_2 - x_1$ | przemieszczenie | zawsze; znak zależy od zwrotu osi |
| $\bar{v} = \Delta x/\Delta t$ | prędkość średnia | zawsze |
| $\bar{v}_s = s/\Delta t$ | szybkość średnia | zawsze; $\bar{v}_s \ge \lvert\bar{v}\rvert$ |
| $v = dx/dt$ | prędkość chwilowa | nachylenie stycznej do $x(t)$ |
| $a = dv/dt$ | przyspieszenie chwilowe | nachylenie stycznej do $v(t)$ |
| $\Delta x = \int v\,dt$ | przemieszczenie z prędkości | pole pod $v(t)$ ze znakiem |
| $1\ \mathrm{m/s} = 3{,}6\ \mathrm{km/h}$ | przelicznik | — |

## Przykład rozwiązany

**Zadanie.** Samochód jedzie z miasta A do B odległego o 60 km w ciągu 1 h, a potem wraca w ciągu 1,5 h. Oblicz prędkość średnią i szybkość średnią całego przejazdu.

**Przemieszczenie** jest zerowe (powrót do A), więc $\bar{v} = 0$.

**Droga** to $120\ \mathrm{km}$, czas $2{,}5\ \mathrm{h}$, więc $\bar{v}_s = 120/2{,}5 = 48\ \mathrm{km/h}$.

**Uwaga.** Średnia z dwóch szybkości ($60$ i $40\ \mathrm{km/h}$) to $50\ \mathrm{km/h}$ — wynik błędny, bo z mniejszą szybkością samochód jechał dłużej.

### Wersja z rachunkiem różniczkowym i całkowym

**Zadanie.** Położenie ciała: $x(t) = t^3 - 6t^2 + 9t$ (m, s). Opisz ruch w przedziale $0 \le t \le 4\ \mathrm{s}$: kiedy ciało zawraca, jaką przebywa drogę, jaka jest prędkość i szybkość średnia.

**Prędkość i przyspieszenie.**

$$v = \frac{dx}{dt} = 3t^2 - 12t + 9 = 3(t-1)(t-3), \qquad a = \frac{dv}{dt} = 6t - 12.$$

**Zawracanie** — gdy $v$ zmienia znak: w $t = 1\ \mathrm{s}$ i $t = 3\ \mathrm{s}$.

**Położenia:** $x(0) = 0$, $x(1) = 4\ \mathrm{m}$, $x(3) = 0$, $x(4) = 4\ \mathrm{m}$.

**Droga** to suma odcinków między punktami zawracania: $4 + 4 + 4 = 12\ \mathrm{m}$. **Przemieszczenie** $\Delta x = 4\ \mathrm{m}$.

$\bar{v} = 4/4 = 1\ \mathrm{m/s}$, $\bar{v}_s = 12/4 = 3\ \mathrm{m/s}$.

**Przyspieszanie i hamowanie.** Dla $1 < t < 2$: $v < 0$, $a < 0$ — ciało przyspiesza w ujemnym kierunku. Dla $2 < t < 3$: $v < 0$, $a > 0$ — hamuje.

## Typowe pułapki

- **Średnia prędkości zamiast prędkości średniej.** Prędkość średnia to całe przemieszczenie przez cały czas, a nie średnia arytmetyczna prędkości z odcinków.
- **Ujemne przyspieszenie = hamowanie.** Nieprawda: jeśli ciało porusza się w ujemnym kierunku, ujemne przyspieszenie je rozpędza.
- **Droga z różnicy położeń.** Gdy ciało zawraca, trzeba podzielić ruch w punktach zawracania ($v = 0$) i sumować wartości bezwzględne.
- **Mylenie wykresów.** Na wykresie $x(t)$ prędkość to nachylenie, a nie wysokość punktu.
- **Jednostki.** Przed wstawieniem do wzorów zamień km/h na m/s (dziel przez 3,6).

## Doświadczenie / symulacja

**Symulacja PhET:** *Ruch człowieka* (*The Moving Man*, [phet.colorado.edu/pl](https://phet.colorado.edu/pl/)). Ustaw stałą prędkość, potem stałe przyspieszenie. Obserwuj jednocześnie trzy wykresy $x(t)$, $v(t)$, $a(t)$ i sprawdź, że nachylenie jednego jest wartością następnego.

**Pomiar.** Nagraj telefonem film kulki toczącej się po stole wzdłuż linijki i wczytaj go do programu [Tracker](https://physlets.org/tracker/). Odczytaj położenie w kolejnych klatkach, narysuj $x(t)$ i wyznacz prędkość jako nachylenie prostej.

**Python:** prędkość i droga z przykładu oraz wykresy trzech wielkości.

```python
import numpy as np
import matplotlib.pyplot as plt

t = np.linspace(0, 4, 401)
x = t**3 - 6*t**2 + 9*t
v = 3*t**2 - 12*t + 9
a = 6*t - 12

dt = t[1] - t[0]
droga = np.sum(np.abs(v[:-1])) * dt        # ∫|v| dt (prosta suma)
print(f"przemieszczenie = {x[-1] - x[0]:.2f} m, droga ≈ {droga:.2f} m")

fig, ax = plt.subplots(3, 1, figsize=(6, 7), sharex=True)
for axis, y, lab in zip(ax, (x, v, a), ("x [m]", "v [m/s]", "a [m/s²]")):
    axis.plot(t, y); axis.axhline(0, color="gray", lw=0.8); axis.set_ylabel(lab); axis.grid(True)
ax[-1].set_xlabel("t [s]")
plt.tight_layout(); plt.show()
```

## Zadania

### A. Poziom maturalny

1. Zawodnik przebiegł jedno okrążenie bieżni o długości 400 m w czasie 50 s, kończąc w miejscu startu. Oblicz jego prędkość średnią i szybkość średnią.

<details>
<summary>Odpowiedź</summary>

$\bar{v} = 0$; $\bar{v}_s = 8\ \mathrm{m/s}$.
</details>

2. Samochód przejechał 30 km z szybkością 60 km/h, a następne 30 km z szybkością 90 km/h. Oblicz szybkość średnią.

<details>
<summary>Odpowiedź</summary>

Czas $0{,}5 + 0{,}333 = 0{,}833\ \mathrm{h}$; $\bar{v}_s = 60/0{,}833 = 72\ \mathrm{km/h}$ (a nie 75 km/h).
</details>

3. Samochód jadący z prędkością 72 km/h zatrzymał się w ciągu 4 s. Oblicz średnie przyspieszenie.

<details>
<summary>Odpowiedź</summary>

$\bar{a} = (0 - 20)/4 = -5\ \mathrm{m/s^2}$.
</details>

4. Wykres $x(t)$ jest prostą przechodzącą przez punkty $(0;\ 2\ \mathrm{m})$ i $(5\ \mathrm{s};\ 12\ \mathrm{m})$. Jaka jest prędkość ciała? Gdzie będzie po 8 s?

<details>
<summary>Odpowiedź</summary>

$v = 2\ \mathrm{m/s}$; $x(8) = 18\ \mathrm{m}$.
</details>

5. Ciało porusza się w ujemnym kierunku osi $x$ z prędkością $-6\ \mathrm{m/s}$, a jego przyspieszenie wynosi $+2\ \mathrm{m/s^2}$. Czy ciało przyspiesza, czy hamuje? Kiedy się zatrzyma?

<details>
<summary>Odpowiedź</summary>

Hamuje (przeciwne znaki $v$ i $a$); zatrzyma się po 3 s.
</details>

### B. Poziom akademicki

1. Położenie: $x(t) = 2t^3 - 9t^2 + 12t$ (m, s). Wyznacz chwile zawracania, przemieszczenie i drogę w przedziale $0 \le t \le 3\ \mathrm{s}$.

<details>
<summary>Odpowiedź</summary>

$v = 6(t-1)(t-2)$, zawracanie w $t = 1$ i $2\ \mathrm{s}$; $x(0) = 0$, $x(1) = 5$, $x(2) = 4$, $x(3) = 9\ \mathrm{m}$. Przemieszczenie $9\ \mathrm{m}$, droga $5 + 1 + 5 = 11\ \mathrm{m}$.
</details>

2. Prędkość: $v(t) = 4 - t^2$ (m/s, s). Oblicz prędkość średnią w przedziale $0 \le t \le 3\ \mathrm{s}$.

<details>
<summary>Odpowiedź</summary>

$\bar{v} = \dfrac{1}{3}\displaystyle\int_0^3(4 - t^2)\,dt = \dfrac{12 - 9}{3} = 1\ \mathrm{m/s}$.
</details>

3. Pokaż, że przy stałym przyspieszeniu prędkość średnia jest średnią arytmetyczną prędkości początkowej i końcowej.

<details>
<summary>Odpowiedź</summary>

$v(t) = v_0 + at$ jest liniowa, więc $\bar{v} = \dfrac{1}{T}\displaystyle\int_0^T(v_0 + at)\,dt = v_0 + \dfrac{aT}{2} = \dfrac{v_0 + v(T)}{2}$.
</details>

4. Prędkość ciała zależy od położenia: $v(x) = 2\sqrt{x}$ (m/s, m). Pokaż, że przyspieszenie jest stałe. (Wskazówka: $a = \dfrac{dv}{dt} = \dfrac{dv}{dx}\dfrac{dx}{dt} = v\dfrac{dv}{dx}$.)

<details>
<summary>Odpowiedź</summary>

$a = 2\sqrt{x}\cdot\dfrac{1}{\sqrt{x}} = 2\ \mathrm{m/s^2}$.
</details>

## Źródła

- OpenStax, *Fizyka dla szkół wyższych*, t. 1, rozdz. 3 — §3.1–3.3; przykłady z wykresami $x(t)$ i $v(t)$.
- Halliday, Resnick, Walker, *Podstawy fizyki* — wyd. 2015: t. 1, rozdz. 2, §2.1–2.3; wyd. 1: t. 1, rozdz. 2, §2.1–2.5 (link na stronę w nagłówku).
- Symulacja PhET *Ruch człowieka*.
