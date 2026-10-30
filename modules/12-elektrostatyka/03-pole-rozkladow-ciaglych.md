# 12.03 — Pole rozkładów ciągłych ładunku

> **Moduł:** [12 — Elektrostatyka](README.md) · **Poziom:** 🔵 studia · **Status:** ✅ pełny
>
> **Czytaj:**
>
> - OpenStax, *Fizyka dla szkół wyższych*, t. 2, rozdz. 5: [§5.5](https://openstax.org/books/fizyka-dla-szk%C3%B3%C5%82-wy%C5%BCszych-tom-2/pages/5-5-wyznaczanie-natezenia-pola-elektrycznego-rozkladu-ladunkow) · [wstęp do rozdziału](https://openstax.org/books/fizyka-dla-szk%C3%B3%C5%82-wy%C5%BCszych-tom-2/pages/5-wstep)
> - Halliday, Resnick, Walker, *Podstawy fizyki*, wyd. 2015, t. 3: §22.4–22.5 (s. 39)
> - Halliday, Resnick, Walker, *Podstawy fizyki*, wyd. 1 (2003), t. 3: [§23.6–23.7, s. 27](https://home.agh.edu.pl/~czapli/Resnick_3.pdf#page=37) — PDF z serwera AGH

← [Natężenie pola, linie pola i dipol](02-pole-elektryczne.md) · [spis modułu](README.md) · [Strumień pola i prawo Gaussa](04-prawo-gaussa.md) →

## Po co to jest

Prawdziwe ładunki rzadko są punktowe. Siedzą na przewodach, okładkach kondensatorów, pierścieniach i chmurach burzowych. Pole takiego rozkładu oblicza się, dzieląc go na małe kawałki i całkując pola od nich. To pierwsze w fizyce całki z wektorów: trzeba korzystać z symetrii, rozkładać na składowe i dobrze dobierać zmienną. Wyniki dla nici, pierścienia i płaszczyzny to wzory, które wracają w całej elektryczności i elektronice.

## Teoria w pigułce

**Gęstości ładunku:**
- liniowa $\lambda = dq/dl$ (C/m), np. naładowany drut;
- powierzchniowa $\sigma = dq/dA$ (C/m²), np. okładka kondensatora;
- objętościowa $\rho = dq/dV$ (C/m³), np. chmura ładunku.

**Metoda.** Element $dq$ wytwarza pole jak ładunek punktowy, a całe pole to suma (całka) tych przyczynków:

$$\vec E = \int k\frac{dq}{r^2}\hat r.$$

W praktyce:
1. Narysuj element $dq$ i wektor $d\vec E$ od niego.
2. Wykorzystaj symetrię: znajdź składowe, które się znoszą.
3. Zapisz pozostałą składową przez jedną zmienną (długość, kąt) i całkuj.

**Najważniejsze wyniki:**

| Rozkład | Pole | Uwagi |
|---|---|---|
| nieskończona nić $\lambda$ | $E = \dfrac{\lambda}{2\pi\varepsilon_0r}$ | prostopadle do nici, maleje jak $1/r$ |
| pierścień $Q$, promień $R$, na osi | $E = \dfrac{kQz}{(z^2 + R^2)^{3/2}}$ | zero w środku; dla $z \gg R$ jak ładunek punktowy |
| dysk $\sigma$, promień $R$, na osi | $E = \dfrac{\sigma}{2\varepsilon_0}\left(1 - \dfrac{z}{\sqrt{z^2 + R^2}}\right)$ | — |
| nieskończona płaszczyzna $\sigma$ | $E = \dfrac{\sigma}{2\varepsilon_0}$ | nie zależy od odległości |
| dwie płaszczyzny $\pm\sigma$ | $E = \dfrac{\sigma}{\varepsilon_0}$ między nimi, 0 na zewnątrz | kondensator płaski (12.06) |

Pole płaszczyzny nie maleje z odległością, bo w miarę oddalania „widać” coraz większy jej fragment pod tym samym kątem.

## Wzory i założenia

| Wzór | Znaczenie | Kiedy obowiązuje |
|---|---|---|
| $d\vec E = k\,dq\,\hat r/r^2$ | przyczynek elementu | — |
| $dq = \lambda\,dl = \sigma\,dA = \rho\,dV$ | element ładunku | — |
| $E = \lambda/(2\pi\varepsilon_0r)$ | nieskończona nić | $r \ll$ długość nici |
| $E = kQz/(z^2 + R^2)^{3/2}$ | pierścień, na osi | — |
| $E = \sigma/(2\varepsilon_0)$ | nieskończona płaszczyzna | $z \ll$ rozmiar płaszczyzny |

## Przykład rozwiązany

### Wersja z rachunkiem różniczkowym i całkowym

**Zadanie 1.** Wyprowadź pole na osi pierścienia o promieniu $R$ z ładunkiem $Q$. Oblicz je dla $Q = 10\ \mathrm{nC}$, $R = 10\ \mathrm{cm}$ w odległości $z = 10\ \mathrm{cm}$ i znajdź punkt, w którym jest największe.

Każdy element $dq$ jest w tej samej odległości $\sqrt{z^2 + R^2}$. Składowe prostopadłe do osi się znoszą parami. Składowa wzdłuż osi to $dE\cos\alpha$, gdzie $\cos\alpha = z/\sqrt{z^2 + R^2}$:

$$E = \int\frac{k\,dq}{z^2 + R^2}\cdot\frac{z}{\sqrt{z^2 + R^2}} = \frac{kQz}{(z^2 + R^2)^{3/2}}.$$

Liczbowo: $E = \dfrac{8{,}99\cdot10^9\cdot10^{-8}\cdot0{,}1}{(0{,}02)^{3/2}} \approx 3180\ \mathrm{N/C}$.

Maksimum: $\dfrac{dE}{dz} = 0 \Rightarrow (z^2 + R^2) - 3z^2 = 0 \Rightarrow z = R/\sqrt2 \approx 7{,}1\ \mathrm{cm}$, gdzie $E \approx 3460\ \mathrm{N/C}$.

**Zadanie 2.** Pręt o długości $L = 20\ \mathrm{cm}$ ma ładunek $Q = 10\ \mathrm{nC}$. Oblicz pole w punkcie na symetralnej, w odległości $y = 10\ \mathrm{cm}$ od pręta. Porównaj z wzorem dla nici nieskończonej.

Element $dq = \lambda\,dx$ w położeniu $x$. Składowe wzdłuż pręta się znoszą, a składowa prostopadła wynosi:

$$E = \int_{-L/2}^{L/2}\frac{k\lambda y\,dx}{(x^2 + y^2)^{3/2}} = \frac{k\lambda L}{y\sqrt{y^2 + L^2/4}} = \frac{kQ}{y\sqrt{y^2 + L^2/4}} \approx 6360\ \mathrm{N/C}.$$

Wzór dla nici nieskończonej daje $\lambda/(2\pi\varepsilon_0y) \approx 8990\ \mathrm{N/C}$, czyli o 40% za dużo, bo tutaj $y$ nie jest małe w porównaniu z $L$. Dla $L \to \infty$ całka daje dokładnie $2k\lambda/y$.

## Typowe pułapki

- **Całkowanie wartości $dE$.** Całkuje się składowe. Najpierw trzeba usunąć składowe, które się znoszą z symetrii.
- **Odległość $r$ stała.** Dla pręta $r$ zależy od położenia elementu. Dla pierścienia na osi jest stała.
- **Wzór dla nici nieskończonej dla krótkiego pręta.** Działa tylko blisko pręta i daleko od jego końców.
- **Pole płaszczyzny $\sigma/\varepsilon_0$.** Dla jednej płaszczyzny to $\sigma/(2\varepsilon_0)$. Wartość $\sigma/\varepsilon_0$ jest między okładkami kondensatora albo tuż przy powierzchni przewodnika (12.04).
- **Pierścień = ładunek punktowy w środku.** W środku pierścienia pole wynosi zero.

## Doświadczenie / symulacja

**Symulacja PhET:** *Ładunki i pola* (*Charges and Fields*) — ustaw rząd ładunków jako model pręta lub dwa rzędy jako kondensator i sprawdź czujnikiem, jak pole zależy od odległości.

**Python:** pole pręta z całkowania numerycznego (suma po elementach) w porównaniu ze wzorem.

```python
import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import quad

k, eps0 = 8.9875e9, 8.854e-12
Q, L = 1e-8, 0.2
lam = Q/L

def E_numer(y):                       # składowa prostopadła z całki
    return quad(lambda x: k*lam*y/(x**2 + y**2)**1.5, -L/2, L/2)[0]

def E_wzor(y):
    return k*Q/(y*np.sqrt(y**2 + L**2/4))

for y in (0.01, 0.1, 1.0):
    print(f"y = {y:5.2f} m: całka {E_numer(y):10.1f}, wzór {E_wzor(y):10.1f}, "
          f"nić nieskończona {lam/(2*np.pi*eps0*y):10.1f}, punkt {k*Q/y**2:10.1f} N/C")

y = np.logspace(-2.5, 1, 200)
plt.loglog(y, [E_numer(v) for v in y], label="pręt 20 cm")
plt.loglog(y, lam/(2*np.pi*eps0*y), "--", label="nić nieskończona ~1/r")
plt.loglog(y, k*Q/y**2, ":", label="ładunek punktowy ~1/r²")
plt.xlabel("y [m]"); plt.ylabel("E [N/C]"); plt.grid(True, which="both"); plt.legend(); plt.show()
```

## Zadania

### A. Poziom maturalny _(opcjonalnie — rozgrzewka)_

1. Jaka jest wartość pola w środku jednorodnie naładowanego pierścienia? Uzasadnij z symetrii.

<details>
<summary>Odpowiedź</summary>

Zero. Pola od przeciwległych elementów mają równe wartości i przeciwne zwroty.
</details>

2. Duża płyta ma gęstość ładunku $1\ \mu\mathrm C/\mathrm m^2$. Oblicz pole w odległości 1 cm i 2 cm od niej.

<details>
<summary>Odpowiedź</summary>

W obu miejscach $\sigma/(2\varepsilon_0) \approx 5{,}6\cdot10^4\ \mathrm{N/C}$.
</details>

### B. Poziom akademicki

1. Wyprowadź pole nieskończonej nici, całkując po kącie $\theta$ ($x = y\tan\theta$).

<details>
<summary>Odpowiedź</summary>

$dx = y\,d\theta/\cos^2\theta$, $x^2 + y^2 = y^2/\cos^2\theta$, więc $E = \dfrac{k\lambda}{y}\displaystyle\int_{-\pi/2}^{\pi/2}\cos\theta\,d\theta = \dfrac{2k\lambda}{y} = \dfrac{\lambda}{2\pi\varepsilon_0y}$.
</details>

2. Wyprowadź pole na osi dysku, sumując pierścienie o promieniu $r$ i szerokości $dr$. Pokaż, że dla $R \to \infty$ wychodzi pole płaszczyzny.

<details>
<summary>Odpowiedź</summary>

$dE = \dfrac{k\sigma2\pi r\,dr\,z}{(z^2 + r^2)^{3/2}}$, $E = \dfrac{\sigma z}{2\varepsilon_0}\left[\dfrac{1}{z} - \dfrac{1}{\sqrt{z^2 + R^2}}\right]$. Dla $R \to \infty$: $\sigma/(2\varepsilon_0)$.
</details>

3. Ładunek $Q$ rozłożono równomiernie na półokręgu o promieniu $R$. Oblicz pole w środku okręgu.

<details>
<summary>Odpowiedź</summary>

$\lambda = Q/(\pi R)$. Składowe wzdłuż średnicy się znoszą: $E = \displaystyle\int_0^\pi\frac{k\lambda R\,d\theta}{R^2}\sin\theta = \frac{2k\lambda}{R} = \frac{2kQ}{\pi R^2}$.
</details>

4. Ładunek punktowy $q$ może poruszać się wzdłuż osi pierścienia o ładunku $Q$ przeciwnego znaku. Pokaż, że przy małych wychyleniach ze środka wykonuje drgania harmoniczne, i podaj częstość.

<details>
<summary>Odpowiedź</summary>

Dla $z \ll R$: $F \approx -\dfrac{k\lvert qQ\rvert}{R^3}z$, więc $\omega = \sqrt{\dfrac{k\lvert qQ\rvert}{mR^3}}$.
</details>

## Źródła

- OpenStax, *Fizyka dla szkół wyższych*, t. 2, rozdz. 5 — §5.5: wyznaczanie natężenia pola elektrycznego rozkładu ładunków.
- Halliday, Resnick, Walker, *Podstawy fizyki* — wyd. 2015: t. 3, §22.4–22.5; wyd. 1: t. 3, §23.6–23.7.
