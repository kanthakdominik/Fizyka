# 06.01 — Kinematyka ruchu obrotowego

> **Moduł:** [06 — Bryła sztywna, statyka i sprężystość](README.md) · **Poziom:** 🟢 matura R · **Status:** ✅ pełny
>
> **Czytaj:**
>
> - OpenStax, *Fizyka dla szkół wyższych*, t. 1, rozdz. 10: [§10.1–10.3](https://openstax.org/books/fizyka-dla-szk%C3%B3%C5%82-wy%C5%BCszych-tom-1/pages/10-1-zmienne-opisujace-ruch-obrotowy) · [wstęp do rozdziału](https://openstax.org/books/fizyka-dla-szk%C3%B3%C5%82-wy%C5%BCszych-tom-1/pages/10-wstep)
> - Halliday, Resnick, Walker, *Podstawy fizyki*, wyd. 2015, t. 1: §10.1–10.3 (s. 325)
> - Halliday, Resnick, Walker, *Podstawy fizyki*, wyd. 1 (2003), t. 1: [§11.1–11.5, s. 260](https://home.agh.edu.pl/~czapli/Resnick_1.pdf#page=272) — PDF z serwera AGH

← (początek modułu) · [spis modułu](README.md) · [Moment bezwładności i twierdzenie Steinera](02-moment-bezwladnosci.md) →

## Po co to jest

Koła, wały silników, wirniki turbin, dyski twarde, Ziemia — ruch obrotowy jest tak samo powszechny jak postępowy. Dobra wiadomość: kinematyka obrotów to dokładna kopia kinematyki ruchu prostoliniowego (02.01–02.03), w której zamiast położenia mamy kąt, zamiast prędkości — prędkość kątową, a zamiast przyspieszenia — przyspieszenie kątowe. Ta analogia prowadzi przez cały moduł 06.

## Teoria w pigułce

**Bryła sztywna** to ciało, którego punkty nie zmieniają wzajemnych odległości. Przy obrocie wokół stałej osi wszystkie jej punkty obracają się o ten sam kąt w tym samym czasie, choć przebywają różne drogi.

**Wielkości kątowe** (kąt w radianach):

| Ruch postępowy | Ruch obrotowy | Związek dla punktu w odległości $r$ od osi |
|---|---|---|
| położenie $x$ | kąt $\theta$ | łuk $s = r\theta$ |
| prędkość $v = dx/dt$ | prędkość kątowa $\omega = d\theta/dt$ | $v = \omega r$ |
| przyspieszenie $a = dv/dt$ | przyspieszenie kątowe $\varepsilon = d\omega/dt$ | $a_t = \varepsilon r$ |
| — | — | $a_n = \omega^2r$ (dośrodkowe) |

**Ruch obrotowy jednostajnie zmienny** ($\varepsilon = \text{const}$) — te same wzory co w 02.02:

$$\omega = \omega_0 + \varepsilon t, \qquad \theta = \theta_0 + \omega_0t + \tfrac12\varepsilon t^2, \qquad \omega^2 = \omega_0^2 + 2\varepsilon(\theta - \theta_0).$$

**Prędkość kątowa jako wektor.** $\vec{\omega}$ leży na osi obrotu, a jego zwrot wyznacza reguła prawej dłoni: palce zgięte w kierunku obrotu, kciuk wskazuje $\vec{\omega}$. Prędkość punktu: $\vec{v} = \vec{\omega}\times\vec{r}$.

**Liczba obrotów** to kąt podzielony przez $2\pi$. Przelicznik: $1\ \mathrm{obr/min} = 2\pi/60\ \mathrm{rad/s} \approx 0{,}105\ \mathrm{rad/s}$.

## Wzory i założenia

| Wzór | Znaczenie | Kiedy obowiązuje |
|---|---|---|
| $\omega = d\theta/dt$, $\ \varepsilon = d\omega/dt$ | definicje | $\theta$ w radianach |
| $\omega = \omega_0 + \varepsilon t$ | prędkość kątowa | $\varepsilon = \text{const}$ |
| $\theta = \omega_0t + \tfrac12\varepsilon t^2$ | kąt obrotu | $\varepsilon = \text{const}$ |
| $\omega^2 = \omega_0^2 + 2\varepsilon\theta$ | bez czasu | $\varepsilon = \text{const}$ |
| $v = \omega r$, $\ a_t = \varepsilon r$, $\ a_n = \omega^2r$ | wielkości liniowe punktu | bryła sztywna, oś stała |

## Przykład rozwiązany

**Zadanie.** Tarcza szlifierki rusza z miejsca i w ciągu 5 s osiąga 3000 obr/min ze stałym przyspieszeniem kątowym. Ile obrotów wykona w tym czasie? Jaką prędkość i jakie przyspieszenia ma punkt na brzegu tarczy ($r = 10\ \mathrm{cm}$) w chwili $t = 5\ \mathrm{s}$?

- $\omega = 3000\cdot2\pi/60 \approx 314\ \mathrm{rad/s}$, $\varepsilon = 314/5 \approx 62{,}8\ \mathrm{rad/s^2}$.
- Kąt: $\theta = \tfrac12\varepsilon t^2 \approx 785\ \mathrm{rad}$, czyli **125 obrotów**.
- Prędkość brzegu: $v = \omega r \approx 31{,}4\ \mathrm{m/s}$ (113 km/h).
- Przyspieszenie styczne: $a_t = \varepsilon r \approx 6{,}3\ \mathrm{m/s^2}$; dośrodkowe: $a_n = \omega^2r \approx 9870\ \mathrm{m/s^2} \approx 1000g$.

Dlatego tarcze szlifierskie mają oznaczoną dopuszczalną prędkość obrotową — przy przekroczeniu rozrywają się.

### Wersja z rachunkiem różniczkowym i całkowym

**Zadanie.** Prędkość kątowa wirnika: $\omega(t) = 4t - t^2$ (rad/s, s). Wyznacz przyspieszenie kątowe, chwilę zatrzymania i kąt obrotu do tej chwili.

$\varepsilon = d\omega/dt = 4 - 2t$. Zatrzymanie: $\omega = 0 \Rightarrow t = 4\ \mathrm{s}$.

$$\theta = \int_0^4(4t - t^2)\,dt = \left[2t^2 - \frac{t^3}{3}\right]_0^4 = 32 - \frac{64}{3} \approx 10{,}7\ \mathrm{rad}.$$

Największą prędkość kątową wirnik ma w $t = 2\ \mathrm{s}$ ($\varepsilon = 0$): $\omega_{\max} = 4\ \mathrm{rad/s}$.

## Typowe pułapki

- **Stopnie i obroty we wzorach.** Wzory $v = \omega r$ i $a_t = \varepsilon r$ działają tylko w radianach.
- **Wszystkie punkty mają tę samą prędkość.** Mają tę samą prędkość kątową; prędkość liniowa rośnie z odległością od osi.
- **Przyspieszenie przy stałym $\omega$.** Punkt na obracającej się bryle zawsze ma przyspieszenie dośrodkowe, nawet gdy $\varepsilon = 0$.
- **Pomylenie liczby obrotów z kątem.** Liczba obrotów to $\theta/(2\pi)$.

## Doświadczenie / symulacja

**Żyroskop w telefonie.** Połóż telefon na obracającym się krześle biurowym lub talerzu gramofonu i uruchom w phyphox eksperyment *Gyroscope (rotation rate)*. Zakręć i obserwuj zanik $\omega(t)$ — czy przyspieszenie kątowe hamowania jest stałe? Scałkuj $\omega(t)$ numerycznie i porównaj kąt z liczbą obrotów policzoną na oko.

**Python:** analogia ruchu obrotowego i postępowego — kąt, prędkość i przyspieszenie kątowe z przykładu.

```python
import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import cumulative_trapezoid

t = np.linspace(0, 4, 401)
omega = 4*t - t**2
eps = np.gradient(omega, t)
theta = cumulative_trapezoid(omega, t, initial=0)
print(f"kąt do zatrzymania: {theta[-1]:.3f} rad (dokładnie {32 - 64/3:.3f}), czyli {theta[-1]/(2*np.pi):.2f} obrotu")

fig, ax = plt.subplots(3, 1, figsize=(6, 7), sharex=True)
for a, y, lab in zip(ax, (theta, omega, eps), ("θ [rad]", "ω [rad/s]", "ε [rad/s²]")):
    a.plot(t, y); a.set_ylabel(lab); a.grid(True)
ax[-1].set_xlabel("t [s]"); plt.tight_layout(); plt.show()
```

## Zadania

### A. Poziom maturalny

1. Wentylator obracający się z prędkością 1200 obr/min zatrzymuje się po wyłączeniu w ciągu 30 s ze stałym opóźnieniem. Oblicz przyspieszenie kątowe i liczbę obrotów do zatrzymania.

<details>
<summary>Odpowiedź</summary>

$\varepsilon = -125{,}7/30 \approx -4{,}19\ \mathrm{rad/s^2}$; 300 obrotów (średnio 600 obr/min przez pół minuty).
</details>

2. Oblicz prędkość kątową Ziemi w ruchu obrotowym (doba gwiazdowa 23 h 56 min).

<details>
<summary>Odpowiedź</summary>

$\omega = 2\pi/86\,164\ \mathrm{s} \approx 7{,}29\cdot10^{-5}\ \mathrm{rad/s}$.
</details>

3. Koło samochodu ma promień 35 cm. Samochód jedzie z prędkością 90 km/h. Oblicz prędkość kątową koła.

<details>
<summary>Odpowiedź</summary>

$\omega = 25/0{,}35 \approx 71{,}4\ \mathrm{rad/s}$ (ok. 680 obr/min).
</details>

4. Płyta winylowa obraca się z prędkością $33\tfrac13$ obr/min. Jaką prędkość liniową ma igła w odległości 14 cm i 6 cm od środka?

<details>
<summary>Odpowiedź</summary>

$\omega \approx 3{,}49\ \mathrm{rad/s}$; $0{,}49\ \mathrm{m/s}$ i $0{,}21\ \mathrm{m/s}$.
</details>

### B. Poziom akademicki _(opcjonalnie — rozszerzenie z rachunkiem)_

1. Przyspieszenie kątowe: $\varepsilon(t) = 6t$ (rad/s², s), $\omega_0 = 2\ \mathrm{rad/s}$, $\theta_0 = 0$. Oblicz kąt po 2 s.

<details>
<summary>Odpowiedź</summary>

$\omega = 2 + 3t^2$, $\theta = 2t + t^3$; $\theta(2) = 12\ \mathrm{rad}$.
</details>

2. Bryła obraca się wokół osi $z$ z prędkością $\omega = 2\ \mathrm{rad/s}$ (przeciwnie do ruchu wskazówek zegara patrząc z góry). Oblicz $\vec{v} = \vec{\omega}\times\vec{r}$ dla punktu $\vec{r} = (0{,}3;\ 0{,}4;\ 1)\ \mathrm{m}$.

<details>
<summary>Odpowiedź</summary>

$\vec{\omega} = (0,\ 0,\ 2)$; $\vec{v} = (-0{,}8;\ 0{,}6;\ 0)\ \mathrm{m/s}$, wartość $1{,}0\ \mathrm{m/s} = \omega\cdot0{,}5$ (odległość od osi).
</details>

3. Koło hamuje tak, że $\varepsilon = -k\omega$. Wyznacz $\omega(t)$ i całkowity kąt obrotu do zatrzymania przy prędkości początkowej $\omega_0$.

<details>
<summary>Odpowiedź</summary>

$\omega = \omega_0e^{-kt}$; $\theta = \omega_0/k$ (skończony, choć czas nieskończony — jak motorówka w 02.03).
</details>

## Źródła

- OpenStax, *Fizyka dla szkół wyższych*, t. 1, rozdz. 10 — §10.1–10.3: wielkości kątowe, ruch ze stałym przyspieszeniem kątowym, związek z wielkościami liniowymi.
- Halliday, Resnick, Walker, *Podstawy fizyki* — wyd. 2015: t. 1, §10.1–10.3; wyd. 1: t. 1, §11.1–11.5.
