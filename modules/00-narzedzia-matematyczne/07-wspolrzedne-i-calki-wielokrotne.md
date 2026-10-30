# 00.07 — Współrzędne biegunowe, walcowe, sferyczne i całki wielokrotne

> **Moduł:** [00 — Narzędzia matematyczne fizyka](README.md) · **Poziom:** 🔵 studia · **Status:** ✅ pełny
>
> **Czytaj:**
>
> - OpenStax, *Fizyka dla szkół wyższych*, t. 1, rozdz. 10: [§10.5](https://openstax.org/books/fizyka-dla-szk%C3%B3%C5%82-wy%C5%BCszych-tom-1/pages/10-5-obliczanie-momentu-bezwladnosci) · [wstęp do rozdziału](https://openstax.org/books/fizyka-dla-szk%C3%B3%C5%82-wy%C5%BCszych-tom-1/pages/10-wstep)
> - Halliday, Resnick, Walker, *Podstawy fizyki*, wyd. 2015, t. 1: §10.5 (s. 345)
> - Halliday, Resnick, Walker, *Podstawy fizyki*, wyd. 1 (2003), t. 1: [§9.2, s. 204](https://home.agh.edu.pl/~czapli/Resnick_1.pdf#page=216), [§11.7, s. 273](https://home.agh.edu.pl/~czapli/Resnick_1.pdf#page=285) — PDF z serwera AGH

← [Przybliżenia i szeregi (małe kąty, dwumian, Taylor)](06-przyblizenia-i-szeregi.md) · [spis modułu](README.md) · (koniec modułu) →

## Po co to jest

Ciała w fizyce mają kształt: pręt, tarcza, walec, kula. Żeby policzyć ich masę przy niejednorodnej gęstości, środek masy (05), moment bezwładności (06), pole grawitacyjne kuli (07) albo strumień pola elektrycznego (12), trzeba sumować po długości, powierzchni lub objętości — czyli całkować wielokrotnie. Przy obiektach okrągłych rachunek staje się prosty dopiero we współrzędnych, które pasują do symetrii: biegunowych, walcowych albo sferycznych.

## Teoria w pigułce

**Idea.** Ciało dzielimy na małe kawałki o masie $dm$, każdy traktujemy jak punkt i sumujemy. W zależności od kształtu:

$$dm = \lambda\,dl \ \ (\text{pręt}), \qquad dm = \sigma\,dA \ \ (\text{płytka}), \qquad dm = \rho\,dV \ \ (\text{bryła}),$$

gdzie $\lambda$, $\sigma$, $\rho$ to gęstość liniowa, powierzchniowa i objętościowa.

**Układy współrzędnych.**

- **Biegunowe** (płaszczyzna): $x = r\cos\varphi$, $y = r\sin\varphi$. Element powierzchni: $dA = r\,dr\,d\varphi$ — mały „prostokąt” ma boki $dr$ i $r\,d\varphi$.
- **Walcowe** (przestrzeń): biegunowe plus wysokość $z$. Element objętości: $dV = r\,dr\,d\varphi\,dz$.
- **Sferyczne**: odległość $r$, kąt od osi $z$ $\theta \in [0, \pi]$, kąt azymutalny $\varphi \in [0, 2\pi)$. $x = r\sin\theta\cos\varphi$, $y = r\sin\theta\sin\varphi$, $z = r\cos\theta$. Element objętości: $dV = r^2\sin\theta\,dr\,d\theta\,d\varphi$.

**Symetria upraszcza.** Gdy gęstość zależy tylko od $r$, całki po kątach dają stałe: dla walca $\int_0^{2\pi}d\varphi = 2\pi$, dla kuli $\int_0^{\pi}\sin\theta\,d\theta\int_0^{2\pi}d\varphi = 4\pi$. Wtedy:

$$dA = 2\pi r\,dr \ \ (\text{pierścień}), \qquad dV = 4\pi r^2\,dr \ \ (\text{cienka powłoka kulista}).$$

Często szybciej jest od razu pomyśleć o takim pierścieniu albo powłoce zamiast pisać całkę podwójną.

## Wzory i założenia

| Wielkość | Wzór | Uwagi |
|---|---|---|
| masa | $m = \int\rho\,dV$ | $\rho$ może zależeć od położenia |
| środek masy | $\vec{r}_{\mathrm{SM}} = \dfrac{1}{m}\int\vec{r}\,dm$ | dla ciał symetrycznych leży na osi symetrii |
| moment bezwładności | $I = \int r_\perp^2\,dm$ | $r_\perp$ — odległość od **osi obrotu**, nie od początku układu |
| element powierzchni | $dA = dx\,dy = r\,dr\,d\varphi$ | nie zapomnij czynnika $r$ |
| element objętości | $dV = r\,dr\,d\varphi\,dz = r^2\sin\theta\,dr\,d\theta\,d\varphi$ | walcowe / sferyczne |
| pole koła, objętość kuli | $\int_0^R2\pi r\,dr = \pi R^2$, $\int_0^R4\pi r^2\,dr = \tfrac43\pi R^3$ | sprawdzian poprawności elementu |

## Przykład rozwiązany

### Wersja z rachunkiem różniczkowym i całkowym

**Zadanie.** Oblicz moment bezwładności jednorodnej tarczy o masie $M$ i promieniu $R$ względem osi prostopadłej do tarczy przechodzącej przez jej środek.

**Gęstość powierzchniowa:** $\sigma = M/(\pi R^2)$.

**Podział na pierścienie.** Pierścień o promieniu $r$ i szerokości $dr$ ma masę $dm = \sigma\cdot2\pi r\,dr$, a cała jego masa jest w odległości $r$ od osi:

$$I = \int_0^R r^2\,\sigma\,2\pi r\,dr = 2\pi\sigma\frac{R^4}{4} = \frac{\pi R^4}{2}\cdot\frac{M}{\pi R^2} = \frac12MR^2.$$

**Sprawdzenie.** Wynik jest mniejszy niż dla obręczy ($MR^2$), bo część masy leży bliżej osi. Jednostka: $\mathrm{kg\cdot m^2}$. Zgadza się.

**Zadanie 2.** Kula o promieniu $R$ ma gęstość malejącą liniowo od środka: $\rho(r) = \rho_0(1 - r/R)$. Oblicz jej masę.

$$m = \int_0^R\rho_0\left(1 - \frac{r}{R}\right)4\pi r^2\,dr = 4\pi\rho_0\left(\frac{R^3}{3} - \frac{R^3}{4}\right) = \frac{\pi\rho_0R^3}{3}.$$

To jedna czwarta masy kuli jednorodnej o gęstości $\rho_0$.

## Typowe pułapki

- **Brak jakobianu.** $dA = dr\,d\varphi$ jest błędne — brakuje czynnika $r$. Sprawdzaj każdy element na polu koła albo objętości kuli.
- **Odległość od osi a odległość od środka.** W momencie bezwładności kuli względem osi $z$ liczy się $r_\perp = r\sin\theta$, a nie $r$.
- **Granice kąta $\theta$.** W układzie sferycznym $\theta$ biegnie od 0 do $\pi$, a nie do $2\pi$ — inaczej każdy punkt liczysz dwa razy.
- **Gęstość stała „z przyzwyczajenia”.** Gdy $\rho$ zależy od położenia, musi zostać pod całką.

## Doświadczenie / symulacja

**Python:** moment bezwładności tarczy z całki podwójnej we współrzędnych biegunowych oraz kuli metodą Monte Carlo (losowe punkty w sześcianie, liczymy tylko te wewnątrz kuli).

```python
import numpy as np
from scipy.integrate import dblquad

M, R = 2.0, 0.5
sigma = M / (np.pi * R**2)

# I = ∫∫ r² σ r dr dφ ; dblquad całkuje f(y, x): tu y = r, x = φ
I_disk, _ = dblquad(lambda r, phi: r**2 * sigma * r, 0, 2*np.pi, 0, R)
print(f"tarcza: I = {I_disk:.5f} kg·m², wzór ½MR² = {0.5*M*R**2:.5f}")

# Kula jednorodna: Monte Carlo
rng = np.random.default_rng(42)
pts = rng.uniform(-R, R, size=(400_000, 3))
inside = pts[(pts**2).sum(axis=1) <= R**2]
r_perp2 = inside[:, 0]**2 + inside[:, 1]**2        # odległość od osi z, do kwadratu
I_ball = M * r_perp2.mean()
print(f"kula:   I ≈ {I_ball:.5f} kg·m², wzór 2/5·MR² = {0.4*M*R**2:.5f}")
print(f"ułamek punktów w kuli: {len(inside)/len(pts):.4f} (π/6 = {np.pi/6:.4f})")
```

## Zadania

### A. Poziom maturalny _(opcjonalnie — rozgrzewka)_

1. Zamień punkt $(x, y) = (1, \sqrt3)$ na współrzędne biegunowe.

<details>
<summary>Odpowiedź</summary>

$r = 2$, $\varphi = 60^\circ = \pi/3$.
</details>

2. Oblicz pole pierścienia o promieniach 1 i 2 (w dowolnych jednostkach) jako różnicę pól kół i jako całkę $\int_1^2 2\pi r\,dr$.

<details>
<summary>Odpowiedź</summary>

$4\pi - \pi = 3\pi$; $\pi[r^2]_1^2 = 3\pi$.
</details>

### B. Poziom akademicki

1. Pręt o długości $L$ ma gęstość liniową $\lambda(x) = \lambda_0(1 + x/L)$, $0 \le x \le L$. Oblicz masę i położenie środka masy.

<details>
<summary>Odpowiedź</summary>

$m = \tfrac32\lambda_0L$; $x_{\mathrm{SM}} = \dfrac{\lambda_0(L^2/2 + L^2/3)}{\tfrac32\lambda_0L} = \dfrac59L$ — bliżej cięższego końca.
</details>

2. Wyprowadź objętość kuli z całki potrójnej we współrzędnych sferycznych.

<details>
<summary>Odpowiedź</summary>

$\int_0^R r^2dr\int_0^\pi\sin\theta\,d\theta\int_0^{2\pi}d\varphi = \dfrac{R^3}{3}\cdot2\cdot2\pi = \tfrac43\pi R^3$.
</details>

3. Oblicz moment bezwładności jednorodnej kuli względem osi przechodzącej przez środek. (Wskazówka: $r_\perp = r\sin\theta$, $\int_0^\pi\sin^3\theta\,d\theta = 4/3$.)

<details>
<summary>Odpowiedź</summary>

$I = \rho\int_0^Rr^4dr\int_0^\pi\sin^3\theta\,d\theta\int_0^{2\pi}d\varphi = \rho\dfrac{R^5}{5}\cdot\dfrac43\cdot2\pi = \dfrac{8\pi\rho R^5}{15} = \dfrac25MR^2$.
</details>

4. Cienka tarcza o promieniu $R$ ma gęstość powierzchniową rosnącą od środka: $\sigma(r) = \sigma_0r/R$. Oblicz masę i moment bezwładności względem osi symetrii. Wyraź $I$ przez masę.

<details>
<summary>Odpowiedź</summary>

$M = \int_0^R\sigma_0\dfrac{r}{R}2\pi r\,dr = \dfrac{2\pi\sigma_0R^2}{3}$; $I = \int_0^R r^2\sigma_0\dfrac{r}{R}2\pi r\,dr = \dfrac{2\pi\sigma_0R^4}{5} = \dfrac35MR^2$.
</details>

5. Walec o promieniu $R$ i wysokości $h$ ma gęstość $\rho(r) = \rho_0e^{-r/R}$. Zapisz masę jako całkę we współrzędnych walcowych i oblicz ją. (Wskazówka: $\int_0^1ue^{-u}du = 1 - 2/e$.)

<details>
<summary>Odpowiedź</summary>

$m = \int_0^h\!\int_0^{2\pi}\!\int_0^R\rho_0e^{-r/R}r\,dr\,d\varphi\,dz = 2\pi h\rho_0R^2\left(1 - \tfrac2e\right) \approx 1{,}66\,\rho_0R^2h$.
</details>

## Źródła

- OpenStax, *Fizyka dla szkół wyższych*, t. 1 — §10.5 (obliczanie momentu bezwładności przez całkowanie) i §9.6 (środek masy ciał ciągłych).
- Halliday, Resnick, Walker, *Podstawy fizyki*, wyd. 2015, t. 1, rozdz. 10 — §10.5: obliczanie momentu bezwładności; rozdz. 9, §9.1: środek masy.
