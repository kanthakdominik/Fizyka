# 16.02 — Płaska fala elektromagnetyczna

> **Moduł:** [16 — Równania Maxwella i fale elektromagnetyczne](README.md) · **Poziom:** 🔵 studia · **Status:** ✅ pełny
>
> **Czytaj:**
>
> - OpenStax, *Fizyka dla szkół wyższych*, t. 2, rozdz. 16: [§16.2](https://openstax.org/books/fizyka-dla-szk%C3%B3%C5%82-wy%C5%BCszych-tom-2/pages/16-2-plaskie-fale-elektromagnetyczne) · [wstęp do rozdziału](https://openstax.org/books/fizyka-dla-szk%C3%B3%C5%82-wy%C5%BCszych-tom-2/pages/16-wstep)
> - Halliday, Resnick, Walker, *Podstawy fizyki*, wyd. 2015, t. 4: §33.1 (s. 1)
> - Halliday, Resnick, Walker, *Podstawy fizyki*, wyd. 1 (2003), t. 4: [§34.1–34.3, s. 2](https://home.agh.edu.pl/~czapli/Resnick_4.pdf#page=17) — PDF z serwera AGH

← [Prąd przesunięcia i równania Maxwella](01-prad-przesuniecia-i-rownania-maxwella.md) · [spis modułu](README.md) · [Energia, wektor Poyntinga i ciśnienie promieniowania](03-energia-i-ped-fali.md) →

## Po co to jest

Fala elektromagnetyczna to sprzężone drgania pól elektrycznego i magnetycznego, które biegną w próżni z prędkością światła. W ten sposób dociera do nas światło Słońca i gwiazd, sygnał radiowy, telewizyjny, GPS i Wi-Fi. Zrozumienie jej budowy (pola prostopadłe, $E = cB$, polaryzacja) jest potrzebne do anten, polaryzatorów w okularach i ekranach LCD, a także do optyki falowej (18).

## Teoria w pigułce

**Fala płaska** biegnąca wzdłuż osi $x$:

$$E_y = E_0\sin(kx - \omega t), \qquad B_z = B_0\sin(kx - \omega t), \qquad c = \frac\omega k = \lambda f.$$

**Własności:**
- Fala jest **poprzeczna**: $\vec E$ i $\vec B$ są prostopadłe do kierunku ruchu i do siebie nawzajem.
- Kierunek biegu fali wskazuje iloczyn $\vec E\times\vec B$.
- Pola drgają **w fazie**, a ich wartości są związane wzorem
  $$E = cB.$$
- Fala nie potrzebuje ośrodka i biegnie w próżni.
- W materiale biegnie wolniej: $v = c/n$, gdzie $n = \sqrt{\varepsilon_r\mu_r}$ to współczynnik załamania (17.02).

**Polaryzacja** to kierunek drgań wektora $\vec E$. Światło ze zwykłych źródeł jest niespolaryzowane (kierunki zmieniają się chaotycznie). Antena dipolowa wysyła falę spolaryzowaną liniowo wzdłuż anteny, dlatego antena odbiorcza najlepiej odbiera, gdy jest równoległa do nadawczej. Polaryzację światła omawia 18.

**Powstawanie fal.** Źródłem fal są **przyspieszane ładunki**. W antenie nadawczej elektrony drgają z częstotliwością nadajnika i wysyłają falę o tej samej częstotliwości. Najsilniej promieniują prostopadle do anteny, wcale wzdłuż niej. Ładunek poruszający się ze stałą prędkością nie promieniuje.

## Wzory i założenia

| Wzór | Znaczenie | Kiedy obowiązuje |
|---|---|---|
| $c = \lambda f = 1/\sqrt{\mu_0\varepsilon_0}$ | prędkość fali EM | próżnia |
| $E = cB$ | związek amplitud | fala biegnąca w próżni |
| $\vec E \perp \vec B \perp \vec v$, $\ \vec v \parallel \vec E\times\vec B$ | poprzeczność fali | — |
| $\dfrac{\partial^2E_y}{\partial x^2} = \mu_0\varepsilon_0\dfrac{\partial^2E_y}{\partial t^2}$ | równanie falowe | próżnia |
| $v = c/n$ | prędkość w ośrodku | — |

## Przykład rozwiązany

**Zadanie.** Fala radiowa o częstotliwości 100 MHz ma amplitudę pola elektrycznego 100 V/m (blisko nadajnika). Oblicz długość fali, liczbę falową i amplitudę pola magnetycznego.

$\lambda = c/f = 3\ \mathrm m$, $k = 2\pi/\lambda \approx 2{,}1\ \mathrm{rad/m}$, $B_0 = E_0/c \approx 3{,}3\cdot10^{-7}\ \mathrm T$, czyli setki razy mniej niż pole Ziemi.

### Wersja z rachunkiem różniczkowym i całkowym

**Wyprowadzenie równania falowego.** Rozważ falę z polami $E_y(x, t)$ i $B_z(x, t)$.

Prawo Faradaya dla małego prostokąta w płaszczyźnie $xy$ (boki $dx$, $h$):

$$[E_y(x + dx) - E_y(x)]h = -\frac{\partial B_z}{\partial t}h\,dx \Rightarrow \frac{\partial E_y}{\partial x} = -\frac{\partial B_z}{\partial t}.$$

Prawo Ampère'a–Maxwella dla prostokąta w płaszczyźnie $xz$ (bez prądów):

$$-\frac{\partial B_z}{\partial x} = \mu_0\varepsilon_0\frac{\partial E_y}{\partial t}.$$

Różniczkując pierwsze po $x$, drugie po $t$ i podstawiając:

$$\frac{\partial^2E_y}{\partial x^2} = \mu_0\varepsilon_0\frac{\partial^2E_y}{\partial t^2}.$$

To równanie falowe (10.02) z $v^2 = 1/(\mu_0\varepsilon_0)$. Wstawiając $E_y = E_0\sin(kx - \omega t)$ do pierwszego równania: $kE_0 = \omega B_0$, czyli $E_0/B_0 = \omega/k = c$.

## Typowe pułapki

- **Fala EM potrzebuje ośrodka (eteru).** Biegnie w próżni. Doświadczenie Michelsona–Morleya nie wykryło eteru (19).
- **$\vec E$ i $\vec B$ przesunięte w fazie o $90^\circ$.** W fali biegnącej w próżni są zgodne w fazie. (Tak bywa w polu bliskim anteny lub w fali stojącej.)
- **Pole magnetyczne fali jest pomijalne, bo $B$ jest małe.** $B = E/c$ ma małą wartość w teslach, ale oba pola niosą dokładnie tyle samo energii (16.03).
- **Każdy ruch ładunku promieniuje.** Promieniuje tylko ładunek przyspieszany.

## Doświadczenie / symulacja

**Fala stojąca w mikrofalówce.** Wyjmij talerz obrotowy, wstaw płaski talerz z warstwą czekolady lub sera (albo kartki faksowej) i podgrzewaj kilkanaście sekund. Pojawią się stopione plamki w strzałkach fali stojącej, odległe o $\lambda/2$. Zmierz odstęp i z częstotliwości z tabliczki (zwykle 2,45 GHz) oblicz $c = \lambda f$. Wychodzi zwykle w granicach 5–10% od właściwej wartości.

**Symulacja PhET:** *Fale radiowe i pola elektromagnetyczne* — obserwuj pole w różnych kierunkach od anteny.

**Python:** migawka fali EM — pola $E$ i $B$ w fazie, prostopadłe.

```python
import numpy as np
import matplotlib.pyplot as plt

c, f, E0 = 299792458.0, 100e6, 100.0
lam = c/f; k = 2*np.pi/lam; w = 2*np.pi*f
x = np.linspace(0, 2*lam, 400)
E = E0*np.sin(k*x)
B = E0/c*np.sin(k*x)
print(f"λ = {lam:.3f} m, k = {k:.3f} rad/m, B0 = {E0/c*1e6:.3f} µT")
# sprawdzenie równania falowego numerycznie w t = 0
dx = x[1] - x[0]
d2E_dx2 = np.gradient(np.gradient(E, dx), dx)
print(f"∂²E/∂x² / (−k² E) w środku przedziału: {d2E_dx2[200]/(-k**2*E[200]):.4f}")

ax = plt.figure(figsize=(8, 4)).add_subplot(projection="3d")
ax.plot(x, E, np.zeros_like(x), label="E (oś y)")
ax.plot(x, np.zeros_like(x), B*c, label="c·B (oś z)")
ax.set_xlabel("x [m]"); ax.legend(); plt.show()
```

## Zadania

### A. Poziom maturalny

1. Oblicz długość fali sygnału GPS (1575 MHz) i Wi-Fi (2,4 GHz).

<details>
<summary>Odpowiedź</summary>

19 cm i 12,5 cm.
</details>

2. Światło biegnie od Słońca do Ziemi (150 mln km). Ile to trwa? A sygnał radiowy z Marsa w odległości 225 mln km?

<details>
<summary>Odpowiedź</summary>

Ok. 500 s (8,3 min) i ok. 12,5 min.
</details>

3. Antena dipolowa ma długość połowy fali. Jaka powinna być antena do odbioru radia UKF (100 MHz)?

<details>
<summary>Odpowiedź</summary>

$\lambda/2 = 1{,}5\ \mathrm m$.
</details>

### B. Poziom akademicki

1. Fala ma postać $\vec E = E_0\sin(kz - \omega t)\hat x$. Wyznacz $\vec B$ (wartość i kierunek).

<details>
<summary>Odpowiedź</summary>

Fala biegnie w stronę $+z$, więc $\vec E\times\vec B \parallel \hat z$: $\hat x\times\hat y = \hat z$. Stąd $\vec B = \dfrac{E_0}{c}\sin(kz - \omega t)\hat y$.
</details>

2. W mikrofalówce (2,45 GHz) odległość między stopionymi plamami czekolady wynosi 6,2 cm. Jaką prędkość światła daje ten pomiar?

<details>
<summary>Odpowiedź</summary>

Plamy są co $\lambda/2$: $\lambda = 12{,}4\ \mathrm{cm}$, $c = \lambda f \approx 3{,}04\cdot10^8\ \mathrm{m/s}$.
</details>

3. Pokaż, że funkcja $E = E_0\sin(kx - \omega t)$ spełnia równanie falowe tylko wtedy, gdy $\omega/k = 1/\sqrt{\mu_0\varepsilon_0}$.

<details>
<summary>Odpowiedź</summary>

$\partial_x^2E = -k^2E$, $\partial_t^2E = -\omega^2E$. Równanie daje $-k^2 = -\mu_0\varepsilon_0\omega^2$, czyli $\omega/k = 1/\sqrt{\mu_0\varepsilon_0}$.
</details>

## Źródła

- OpenStax, *Fizyka dla szkół wyższych*, t. 2, rozdz. 16 — §16.2: płaskie fale elektromagnetyczne.
- Halliday, Resnick, Walker, *Podstawy fizyki* — wyd. 2015: t. 4, §33.1; wyd. 1: t. 4, §34.1–34.3.
- Symulacja PhET *Fale radiowe i pola elektromagnetyczne*.
