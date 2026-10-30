# 07.01 — Prawo powszechnego ciążenia

> **Moduł:** [07 — Grawitacja i elementy astronomii](README.md) · **Poziom:** 🟢 matura R · **Status:** ✅ pełny
>
> **Czytaj:**
>
> - OpenStax, *Fizyka dla szkół wyższych*, t. 1, rozdz. 13: [§13.1–13.2](https://openstax.org/books/fizyka-dla-szk%C3%B3%C5%82-wy%C5%BCszych-tom-1/pages/13-1-prawo-powszechnego-ciazenia) · [wstęp do rozdziału](https://openstax.org/books/fizyka-dla-szk%C3%B3%C5%82-wy%C5%BCszych-tom-1/pages/13-wstep)
> - Halliday, Resnick, Walker, *Podstawy fizyki*, wyd. 2015, t. 2: §13.1–13.3 (s. 36)
> - Halliday, Resnick, Walker, *Podstawy fizyki*, wyd. 1 (2003), t. 2: [§14.1–14.4, s. 28](https://home.agh.edu.pl/~czapli/Resnick_2.pdf#page=44) — PDF z serwera AGH

← (początek modułu) · [spis modułu](README.md) · [Natężenie pola, potencjał i energia grawitacyjna](02-pole-i-potencjal-grawitacyjny.md) →

## Po co to jest

Prawo powszechnego ciążenia Newtona to pierwsze w historii prawo, które łączy fizykę „ziemską” (spadające jabłko) z ruchem ciał niebieskich (Księżyc, planety). Z jednego wzoru wynika przyspieszenie ziemskie, masa Ziemi i Słońca, ruch satelitów (07.03) i prawa Keplera (07.04). To także wzór dla każdej siły typu „odwrotność kwadratu odległości” — prawo Coulomba (12.01) ma identyczną postać.

## Teoria w pigułce

**Prawo powszechnego ciążenia.** Każde dwa ciała o masach $m_1$ i $m_2$ przyciągają się siłą skierowaną wzdłuż łączącej je prostej:

$$F = G\frac{m_1m_2}{r^2}, \qquad G \approx 6{,}674\cdot10^{-11}\ \mathrm{N\cdot m^2/kg^2}.$$

Wzór obowiązuje dla mas punktowych oraz — co udowodnił Newton — dla kul o sferycznie symetrycznym rozkładzie masy, z $r$ równym odległości środków (07.05).

**Stała $G$ jest bardzo mała** — przyciąganie zwykłych przedmiotów jest niezauważalne. Pierwszy zmierzył je H. Cavendish (1798) wagą skręceń; dlatego mówi się, że „zważył Ziemię”.

**Przyspieszenie grawitacyjne** na powierzchni planety o masie $M$ i promieniu $R$:

$$g = \frac{GM}{R^2}.$$

Na wysokości $h$: $g(h) = \dfrac{GM}{(R + h)^2} = g_0\left(\dfrac{R}{R + h}\right)^2$.

**Test Newtona z Księżycem.** Księżyc jest ok. 60 promieni Ziemi od jej środka. Jeśli grawitacja maleje jak $1/r^2$, przyspieszenie Księżyca powinno wynosić $g/60^2 \approx 2{,}7\cdot10^{-3}\ \mathrm{m/s^2}$ — dokładnie tyle, ile wynosi jego przyspieszenie dośrodkowe obliczone z okresu obiegu (02.06).

**Superpozycja.** Siła od kilku ciał to wektorowa suma sił od każdego z nich.

## Wzory i założenia

| Wzór | Znaczenie | Kiedy obowiązuje |
|---|---|---|
| $F = Gm_1m_2/r^2$ | prawo ciążenia | masy punktowe lub kule o symetrii sferycznej |
| $\vec{F}_{12} = -G\dfrac{m_1m_2}{r^2}\hat{r}_{12}$ | postać wektorowa | $\hat{r}_{12}$ — wersor od 1 do 2 (siła na 2) |
| $g = GM/R^2$ | przyspieszenie na powierzchni | pomijamy obrót planety |
| $g(h) = g_0R^2/(R + h)^2$ | przyspieszenie na wysokości $h$ | nad powierzchnią |
| $M = gR^2/G$ | masa planety z $g$ i $R$ | — |

## Przykład rozwiązany

**Zadanie 1.** Oblicz masę Ziemi z przyspieszenia ziemskiego ($g = 9{,}81\ \mathrm{m/s^2}$, $R = 6371\ \mathrm{km}$).

$M = \dfrac{gR^2}{G} = \dfrac{9{,}81\cdot(6{,}371\cdot10^6)^2}{6{,}674\cdot10^{-11}} \approx 5{,}97\cdot10^{24}\ \mathrm{kg}$.

Średnia gęstość: $\rho = M/(\tfrac43\pi R^3) \approx 5500\ \mathrm{kg/m^3}$ — dwa razy więcej niż skały na powierzchni, więc wnętrze Ziemi musi być znacznie gęstsze (żelazne jądro).

**Zadanie 2.** Z jaką siłą przyciągają się dwie osoby o masie 70 kg stojące 1 m od siebie? Porównaj z ich ciężarem.

$F = 6{,}674\cdot10^{-11}\cdot70\cdot70/1 \approx 3{,}3\cdot10^{-7}\ \mathrm{N}$ — ok. 2 miliardy razy mniej niż ciężar (687 N).

### Wersja z rachunkiem różniczkowym i całkowym

**Zadanie.** Jak szybko maleje przyspieszenie grawitacyjne z wysokością tuż nad powierzchnią Ziemi?

$$\frac{dg}{dh} = \frac{d}{dh}\frac{GM}{(R + h)^2} = -\frac{2GM}{(R + h)^3} \approx -\frac{2g}{R} \approx -3{,}1\cdot10^{-6}\ \mathrm{s^{-2}}.$$

Na każdy kilometr wysokości $g$ maleje o ok. $0{,}003\ \mathrm{m/s^2}$ (0,03%). Gradient grawitacji mierzą grawimetry — tak szuka się złóż rud i pustek pod ziemią.

## Typowe pułapki

- **Odległość od powierzchni zamiast od środka.** We wzorze $r$ to odległość środków.
- **Przyciąganie zależy od jednej masy.** Siła jest symetryczna: Ziemia przyciąga jabłko tą samą siłą co jabłko Ziemię (III zasada); różne są przyspieszenia.
- **„W kosmosie nie ma grawitacji”.** Na wysokości stacji kosmicznej $g$ jest tylko o ok. 12% mniejsze; nieważkość wynika ze swobodnego spadania (orbita).
- **Mylenie $G$ i $g$.** $G$ — uniwersalna stała, $g$ — przyspieszenie przy danej planecie.

## Doświadczenie / symulacja

**Symulacja PhET:** *Laboratorium sił grawitacji* (*Gravity Force Lab*, [phet.colorado.edu/pl](https://phet.colorado.edu/pl/)) — zmieniaj masy i odległość, sprawdź zależność $1/r^2$ (dwukrotnie większa odległość — cztery razy mniejsza siła).

**Python:** test Newtona z Księżycem i $g$ na różnych ciałach Układu Słonecznego.

```python
import numpy as np

G = 6.674e-11
bodies = {                   # masa [kg], promień [m]
    "Ziemia": (5.972e24, 6.371e6), "Księżyc": (7.35e22, 1.737e6),
    "Mars": (6.42e23, 3.39e6), "Jowisz": (1.898e27, 6.99e7),
}
for name, (M, R) in bodies.items():
    print(f"{name:8s}: g = {G*M/R**2:6.2f} m/s²")

r_moon, T_moon = 3.844e8, 27.32*86400
a_orbit = 4*np.pi**2*r_moon/T_moon**2
print(f"Księżyc: a z orbity = {a_orbit:.3e} m/s², g·(R/r)² = {9.81*(6.371e6/r_moon)**2:.3e} m/s²")
```

## Zadania

### A. Poziom maturalny

1. Oblicz przyspieszenie grawitacyjne na powierzchni Księżyca ($M = 7{,}35\cdot10^{22}\ \mathrm{kg}$, $R = 1737\ \mathrm{km}$).

<details>
<summary>Odpowiedź</summary>

$g \approx 1{,}62\ \mathrm{m/s^2}$.
</details>

2. Na jakiej wysokości nad Ziemią przyspieszenie grawitacyjne jest dwa razy mniejsze niż na powierzchni?

<details>
<summary>Odpowiedź</summary>

$R + h = \sqrt2R \Rightarrow h = (\sqrt2 - 1)R \approx 2640\ \mathrm{km}$.
</details>

3. Oblicz siłę, z jaką Słońce przyciąga Ziemię ($M_S = 1{,}99\cdot10^{30}\ \mathrm{kg}$, odległość $1{,}496\cdot10^{11}\ \mathrm{m}$).

<details>
<summary>Odpowiedź</summary>

$F \approx 3{,}5\cdot10^{22}\ \mathrm{N}$.
</details>

4. Jak zmieni się siła przyciągania dwóch ciał, gdy odległość między nimi zmaleje trzykrotnie, a masa jednego z nich wzrośnie dwukrotnie?

<details>
<summary>Odpowiedź</summary>

Wzrośnie 18-krotnie.
</details>

5. Planeta ma dwa razy większy promień i dwa razy większą gęstość niż Ziemia. Ile wynosi na niej $g$?

<details>
<summary>Odpowiedź</summary>

$g = \dfrac{G\rho\tfrac43\pi R^3}{R^2} \propto\rho R$: cztery razy więcej, ok. $39\ \mathrm{m/s^2}$.
</details>

### B. Poziom akademicki _(opcjonalnie — rozszerzenie z rachunkiem)_

1. W którym punkcie między Ziemią a Księżycem siły przyciągania obu ciał się równoważą? Masa Księżyca to 1/81 masy Ziemi, odległość $3{,}84\cdot10^8\ \mathrm{m}$.

<details>
<summary>Odpowiedź</summary>

$\dfrac{M}{x^2} = \dfrac{M/81}{(d - x)^2} \Rightarrow x = \dfrac{9}{10}d \approx 3{,}46\cdot10^8\ \mathrm{m}$ od środka Ziemi.
</details>

2. Trzy masy po 1 kg leżą w wierzchołkach trójkąta równobocznego o boku 1 m. Oblicz wypadkową siłę grawitacji działającą na jedną z nich.

<details>
<summary>Odpowiedź</summary>

Dwie siły po $G$ (w N) pod kątem $60^\circ$: $F = 2G\cos30^\circ = \sqrt3G \approx 1{,}16\cdot10^{-10}\ \mathrm{N}$, skierowana do środka trójkąta.
</details>

3. Grawimetr mierzy $g$ z dokładnością $10^{-8}g$. Jaka zmiana wysokości odpowiada tej czułości?

<details>
<summary>Odpowiedź</summary>

$\Delta g/g = 2\Delta h/R \Rightarrow \Delta h = 10^{-8}R/2 \approx 3\ \mathrm{cm}$.
</details>

## Źródła

- OpenStax, *Fizyka dla szkół wyższych*, t. 1, rozdz. 13 — §13.1 (prawo powszechnego ciążenia) i §13.2 (grawitacja przy powierzchni Ziemi).
- Halliday, Resnick, Walker, *Podstawy fizyki* — wyd. 2015: t. 2, §13.1–13.3; wyd. 1: t. 2, §14.1–14.4.
- Symulacja PhET *Laboratorium sił grawitacji*.
