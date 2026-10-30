# 02.04 — Wektory położenia, prędkości i przyspieszenia w 2D i 3D

> **Moduł:** [02 — Kinematyka](README.md) · **Poziom:** 🟢🔵 matura R + studia · **Status:** ✅ pełny
>
> **Czytaj:**
>
> - OpenStax, *Fizyka dla szkół wyższych*, t. 1, rozdz. 4: [§4.1–4.2](https://openstax.org/books/fizyka-dla-szk%C3%B3%C5%82-wy%C5%BCszych-tom-1/pages/4-1-przemieszczenie-i-predkosc) · [wstęp do rozdziału](https://openstax.org/books/fizyka-dla-szk%C3%B3%C5%82-wy%C5%BCszych-tom-1/pages/4-wstep)
> - Halliday, Resnick, Walker, *Podstawy fizyki*, wyd. 2015, t. 1: §4.1–4.3 (s. 79)
> - Halliday, Resnick, Walker, *Podstawy fizyki*, wyd. 1 (2003), t. 1: [§4.1–4.4, s. 58](https://home.agh.edu.pl/~czapli/Resnick_1.pdf#page=70) — PDF z serwera AGH

← [Ruch o zmiennym przyspieszeniu — całkowanie a(t)](03-zmienne-przyspieszenie.md) · [spis modułu](README.md) · [Rzut poziomy i ukośny](05-rzuty.md) →

## Po co to jest

Ruch po prostej to wyjątek; piłka, samochód na zakręcie czy satelita poruszają się po krzywych. W dwóch i trzech wymiarach położenie, prędkość i przyspieszenie stają się wektorami, a ruch rozkłada się na niezależne ruchy wzdłuż osi. Ta jedna idea wystarcza do rzutów (02.05), ruchu po okręgu (02.06) i ruchu ładunku w polu magnetycznym (14).

## Teoria w pigułce

**Wektor położenia** $\vec{r} = x\hat{\imath} + y\hat{\jmath} + z\hat{k}$ wskazuje ciało z początku układu. Jego koniec rysuje **tor** ruchu.

**Przemieszczenie** $\Delta\vec{r} = \vec{r}_2 - \vec{r}_1$ to wektor od położenia początkowego do końcowego — w linii prostej, niezależnie od kształtu toru.

**Prędkość i przyspieszenie** liczymy składowa po składowej:

$$\vec{v} = \frac{d\vec{r}}{dt} = \left(\frac{dx}{dt}, \frac{dy}{dt}, \frac{dz}{dt}\right), \qquad \vec{a} = \frac{d\vec{v}}{dt}.$$

Prędkość chwilowa jest zawsze **styczna do toru**. Średnie wielkości: $\vec{v}_{\text{śr}} = \Delta\vec{r}/\Delta t$, $\vec{a}_{\text{śr}} = \Delta\vec{v}/\Delta t$.

**Niezależność ruchów.** Ruch wzdłuż $x$ i ruch wzdłuż $y$ opisujemy osobnymi równaniami; łączy je tylko wspólny czas. Dlatego w rzucie poziomym ruch w poziomie jest jednostajny, a w pionie — jednostajnie przyspieszony.

**Przyspieszenie styczne i normalne.** Przyspieszenie można rozłożyć na dwie części:
- **styczną** $a_t$ — wzdłuż prędkości, zmienia **wartość** prędkości: $a_t = \dfrac{d\lvert\vec{v}\rvert}{dt}$;
- **normalną** $a_n$ — prostopadłą do prędkości, zmienia **kierunek** ruchu: $a_n = \dfrac{v^2}{R}$, gdzie $R$ to promień krzywizny toru w danym punkcie.

Gdy $a_n = 0$, ruch jest prostoliniowy; gdy $a_t = 0$, szybkość jest stała, ale kierunek może się zmieniać (ruch jednostajny po okręgu).

## Wzory i założenia

| Wzór | Znaczenie | Uwagi |
|---|---|---|
| $\Delta\vec{r} = \vec{r}_2 - \vec{r}_1$ | przemieszczenie | długość $\lvert\Delta\vec{r}\rvert \le$ droga |
| $\vec{v} = d\vec{r}/dt$, $\ \vec{a} = d\vec{v}/dt$ | prędkość, przyspieszenie | różniczkujemy każdą składową |
| $v = \sqrt{v_x^2 + v_y^2 + v_z^2}$ | szybkość | — |
| $a_t = \dfrac{\vec{v}\cdot\vec{a}}{v}$ | przyspieszenie styczne | rzut $\vec{a}$ na kierunek $\vec{v}$ |
| $a_n = \sqrt{a^2 - a_t^2} = \dfrac{v^2}{R}$ | przyspieszenie normalne | $R$ — promień krzywizny toru |
| $\vec{r}(t) = \vec{r}_0 + \vec{v}_0t + \tfrac12\vec{a}t^2$ | ruch ze stałym $\vec{a}$ | wektorowa wersja wzorów z 02.02 |

## Przykład rozwiązany

**Zadanie (poziom maturalny).** Turysta idzie 3 km na wschód, a potem 4 km na północ; całość zajmuje 1,5 h. Oblicz przemieszczenie, prędkość średnią i szybkość średnią.

- Przemieszczenie: $\Delta\vec{r} = (3,\ 4)\ \mathrm{km}$, $\lvert\Delta\vec{r}\rvert = 5\ \mathrm{km}$, kierunek $\arctan(4/3) \approx 53^\circ$ na północ od wschodu.
- Prędkość średnia: $5/1{,}5 \approx 3{,}3\ \mathrm{km/h}$ w tym kierunku.
- Szybkość średnia: droga $7\ \mathrm{km}$, $7/1{,}5 \approx 4{,}7\ \mathrm{km/h}$.

### Wersja z rachunkiem różniczkowym i całkowym

**Zadanie.** Położenie ciała: $\vec{r}(t) = 3t\,\hat{\imath} + (4t - 2t^2)\,\hat{\jmath}$ (m, s). Wyznacz tor, prędkość i przyspieszenie oraz rozłóż przyspieszenie na składową styczną i normalną w chwili $t = 0$.

**Tor.** Z $x = 3t$: $t = x/3$, więc $y = \dfrac{4x}{3} - \dfrac{2x^2}{9}$ — parabola.

**Prędkość i przyspieszenie.** $\vec{v} = (3,\ 4 - 4t)\ \mathrm{m/s}$, $\vec{a} = (0,\ -4)\ \mathrm{m/s^2}$ — stałe, jak w rzucie ukośnym.

**W chwili $t = 0$:** $\vec{v} = (3,\ 4)$, $v = 5\ \mathrm{m/s}$.

$$a_t = \frac{\vec{v}\cdot\vec{a}}{v} = \frac{0 - 16}{5} = -3{,}2\ \mathrm{m/s^2}, \qquad a_n = \sqrt{16 - 3{,}2^2} = 2{,}4\ \mathrm{m/s^2}.$$

Ciało zwalnia ($a_t < 0$) i skręca. Promień krzywizny toru w tym punkcie: $R = v^2/a_n = 25/2{,}4 \approx 10{,}4\ \mathrm{m}$.

**W chwili $t = 1\ \mathrm{s}$** prędkość $\vec{v} = (3,\ 0)$ jest pozioma — to wierzchołek paraboli. Wtedy $a_t = 0$, a całe przyspieszenie jest normalne.

## Typowe pułapki

- **Długość przemieszczenia to nie droga.** Przy torze krzywoliniowym $\lvert\Delta\vec{r}\rvert$ jest mniejsze od drogi.
- **Szybkość stała ≠ przyspieszenie zerowe.** Zmiana kierunku prędkości też jest przyspieszeniem.
- **Dodawanie wartości zamiast wektorów.** Prędkość średnią liczymy z wektora przemieszczenia, nie z sumy dróg.
- **Mieszanie składowych.** Równanie ruchu wzdłuż $x$ zawiera tylko $v_x$ i $a_x$; nie wstawiaj do niego składowych $y$.

## Doświadczenie / symulacja

**Analiza wideo.** Nagraj telefonem rzut piłki z boku, na tle obiektu o znanej długości (np. metrówki). W programie [Tracker](https://physlets.org/tracker/) zaznacz piłkę w kolejnych klatkach. Program poda $x(t)$ i $y(t)$: sprawdź, że $x(t)$ jest liniowe, a $y(t)$ kwadratowe, i wyznacz $g$ z dopasowania paraboli.

**Python:** tor z przykładu, wektory prędkości i rozkład przyspieszenia na składowe.

```python
import numpy as np
import matplotlib.pyplot as plt

t = np.linspace(0, 2, 201)
x, y = 3*t, 4*t - 2*t**2
vx, vy = 3*np.ones_like(t), 4 - 4*t
ax_, ay_ = 0.0, -4.0

v = np.hypot(vx, vy)
a_t = (vx*ax_ + vy*ay_) / v
a_n = np.sqrt(16 - a_t**2)
R = v**2 / a_n
for tt in (0.0, 1.0, 2.0):
    i = np.argmin(abs(t - tt))
    print(f"t={tt}: v={v[i]:.2f} m/s, a_t={a_t[i]:+.2f}, a_n={a_n[i]:.2f} m/s², R={R[i]:.2f} m")

plt.plot(x, y)
idx = np.arange(0, 201, 25)
plt.quiver(x[idx], y[idx], vx[idx], vy[idx], angles="xy", scale_units="xy", scale=4, color="C1")
plt.xlabel("x [m]"); plt.ylabel("y [m]"); plt.axis("equal"); plt.grid(True); plt.show()
```

## Zadania

### A. Poziom maturalny

1. Ciało przemieściło się z punktu $(1;\ 2)\ \mathrm{m}$ do $(4;\ 6)\ \mathrm{m}$ w ciągu 2 s. Oblicz wektor przemieszczenia, jego długość i wartość prędkości średniej.

<details>
<summary>Odpowiedź</summary>

$\Delta\vec{r} = (3,\ 4)\ \mathrm{m}$, $5\ \mathrm{m}$, $2{,}5\ \mathrm{m/s}$.
</details>

2. Samolot leci 300 km na północ, a potem 400 km na wschód; całość trwa 2 h. Oblicz prędkość średnią i szybkość średnią.

<details>
<summary>Odpowiedź</summary>

Przemieszczenie 500 km, $\bar{v} = 250\ \mathrm{km/h}$ (ok. $53^\circ$ na wschód od północy); $\bar{v}_s = 350\ \mathrm{km/h}$.
</details>

3. Prędkość ciała zmieniła się z $(4;\ 0)\ \mathrm{m/s}$ na $(0;\ 3)\ \mathrm{m/s}$ w ciągu 2 s. Oblicz średnie przyspieszenie.

<details>
<summary>Odpowiedź</summary>

$\vec{a}_{\text{śr}} = (-2;\ 1{,}5)\ \mathrm{m/s^2}$, wartość $2{,}5\ \mathrm{m/s^2}$ — mimo że szybkość zmalała z 4 do 3 m/s.
</details>

4. Samochód jedzie po zakręcie ze stałą szybkością. Czy ma przyspieszenie? W którą stronę jest skierowane?

<details>
<summary>Odpowiedź</summary>

Tak — przyspieszenie normalne, skierowane do środka krzywizny zakrętu.
</details>

### B. Poziom akademicki

1. $\vec{r}(t) = (t^2,\ 2t,\ 1 - t)$ (m, s). Oblicz prędkość, szybkość i przyspieszenie dla $t = 1\ \mathrm{s}$.

<details>
<summary>Odpowiedź</summary>

$\vec{v} = (2,\ 2,\ -1)\ \mathrm{m/s}$, $v = 3\ \mathrm{m/s}$, $\vec{a} = (2,\ 0,\ 0)\ \mathrm{m/s^2}$.
</details>

2. Dla ruchu z przykładu oblicz $a_t$ i $a_n$ w chwili $t = 2\ \mathrm{s}$.

<details>
<summary>Odpowiedź</summary>

$\vec{v} = (3,\ -4)$, $a_t = +3{,}2\ \mathrm{m/s^2}$ (ciało przyspiesza w drodze w dół), $a_n = 2{,}4\ \mathrm{m/s^2}$.
</details>

3. Ruch po linii śrubowej: $\vec{r}(t) = (R\cos\omega t,\ R\sin\omega t,\ ct)$. Oblicz szybkość i przyspieszenie.

<details>
<summary>Odpowiedź</summary>

$v = \sqrt{R^2\omega^2 + c^2}$ — stała; $\vec{a} = -\omega^2(R\cos\omega t,\ R\sin\omega t,\ 0)$, wartość $R\omega^2$, skierowane do osi śruby. (Tak porusza się ładunek w polu magnetycznym — moduł 14.)
</details>

4. Pokaż, że jeśli szybkość jest stała, to przyspieszenie jest prostopadłe do prędkości.

<details>
<summary>Odpowiedź</summary>

$\dfrac{d}{dt}(\vec{v}\cdot\vec{v}) = 2\vec{v}\cdot\vec{a} = \dfrac{d}{dt}v^2 = 0$.
</details>

## Źródła

- OpenStax, *Fizyka dla szkół wyższych*, t. 1, rozdz. 4 — §4.1–4.2: wektory przemieszczenia, prędkości i przyspieszenia.
- Halliday, Resnick, Walker, *Podstawy fizyki* — wyd. 2015: t. 1, §4.1–4.3; wyd. 1: t. 1, §4.1–4.4.
