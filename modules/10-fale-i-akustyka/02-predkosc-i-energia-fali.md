# 10.02 — Prędkość fali, energia i równanie falowe

> **Moduł:** [10 — Fale mechaniczne i akustyka](README.md) · **Poziom:** 🔵 studia · **Status:** ✅ pełny
>
> **Czytaj:**
>
> - OpenStax, *Fizyka dla szkół wyższych*, t. 1, rozdz. 16: [§16.3–16.4](https://openstax.org/books/fizyka-dla-szk%C3%B3%C5%82-wy%C5%BCszych-tom-1/pages/16-3-predkosc-fali-na-naprezonej-strunie) · [wstęp do rozdziału](https://openstax.org/books/fizyka-dla-szk%C3%B3%C5%82-wy%C5%BCszych-tom-1/pages/16-wstep)
> - Halliday, Resnick, Walker, *Podstawy fizyki*, wyd. 2015, t. 2: §16.2–16.4 (s. 165)
> - Halliday, Resnick, Walker, *Podstawy fizyki*, wyd. 1 (2003), t. 2: [§17.6–17.7, s. 131](https://home.agh.edu.pl/~czapli/Resnick_2.pdf#page=147) — PDF z serwera AGH

← [Fala biegnąca i jej opis matematyczny](01-fala-biegnaca.md) · [spis modułu](README.md) · [Superpozycja, interferencja i fale stojące](03-interferencja-i-fale-stojace.md) →

## Po co to jest

Prędkość fali zależy tylko od właściwości ośrodka: struna gra wyżej po mocniejszym napięciu, dźwięk biegnie szybciej w wodzie i stali niż w powietrzu, a z prędkości fal sejsmicznych odczytuje się budowę wnętrza Ziemi. Fala niesie też energię, a jej moc rośnie z kwadratem amplitudy i częstotliwości. Wyprowadzenie równania falowego z zasad dynamiki to klasyczny przykład tego, jak z prostego modelu otrzymuje się prawo ogólne.

## Teoria w pigułce

**Prędkość fali** to zawsze pierwiastek z ilorazu „sprężystości” ośrodka przez jego „bezwładność”:

| Ośrodek | Wzór | Wielkości |
|---|---|---|
| napięta struna | $v = \sqrt{F/\mu}$ | $F$ — siła naciągu, $\mu$ — masa na jednostkę długości |
| ciecz lub gaz (fala podłużna) | $v = \sqrt{K/\rho}$ | $K$ — moduł ściśliwości |
| gaz doskonały | $v = \sqrt{\gamma RT/M}$ | $\gamma = c_p/c_V$ (1,4 dla powietrza), $M$ — masa molowa |
| pręt (fala podłużna) | $v = \sqrt{E/\rho}$ | $E$ — moduł Younga (06.07) |

Przykłady: powietrze w 20°C ok. 343 m/s, woda ok. 1480 m/s, stal ok. 5000 m/s. W powietrzu prędkość rośnie jak $\sqrt T$, w temperaturze pokojowej o ok. 0,6 m/s na kelwin.

**Równanie falowe.** Element struny o długości $dx$ jest odchylony od poziomu, a siły naciągu na jego końcach mają nieco inne kierunki. Wypadkowa siła poprzeczna wynosi $F\,\partial^2y/\partial x^2\,dx$. Z drugiej zasady dynamiki:

$$\mu\,dx\,\frac{\partial^2y}{\partial t^2} = F\frac{\partial^2y}{\partial x^2}dx \quad\Rightarrow\quad \frac{\partial^2y}{\partial t^2} = \frac{F}{\mu}\frac{\partial^2y}{\partial x^2}.$$

To równanie falowe z $v^2 = F/\mu$.

**Energia i moc fali.** Każdy element struny wykonuje ruch harmoniczny z energią $\tfrac12(\mu\,dx)\omega^2A^2$. Energia przypadająca na jednostkę długości wynosi średnio $\tfrac12\mu\omega^2A^2$, a fala przenosi ją z prędkością $v$:

$$\bar P = \tfrac12\mu\omega^2A^2v.$$

Moc rośnie jak $A^2$ i $\omega^2$. Dla fal w przestrzeni używa się **natężenia**, czyli mocy na jednostkę powierzchni (10.05).

## Wzory i założenia

| Wzór | Znaczenie | Kiedy obowiązuje |
|---|---|---|
| $v = \sqrt{F/\mu}$ | fala na strunie | małe wychylenia, struna jednorodna |
| $v = \sqrt{K/\rho}$, $\ v = \sqrt{\gamma RT/M}$ | dźwięk w płynach, w gazie doskonałym | procesy adiabatyczne |
| $v = \sqrt{E/\rho}$ | fala podłużna w cienkim pręcie | — |
| $\partial_t^2y = v^2\partial_x^2y$ | równanie falowe | ośrodek liniowy, bez strat |
| $\bar P = \tfrac12\mu\omega^2A^2v$ | moc fali na strunie | fala harmoniczna |

## Przykład rozwiązany

**Zadanie.** Struna o masie 1 g na metr jest napięta siłą 100 N. Oblicz prędkość fali. Jaką średnią moc niesie fala o częstotliwości 100 Hz i amplitudzie 1 mm?

$v = \sqrt{100/0{,}001} \approx 316\ \mathrm{m/s}$.

$\bar P = \tfrac12\cdot0{,}001\cdot(2\pi\cdot100)^2\cdot(10^{-3})^2\cdot316 \approx 0{,}062\ \mathrm{W}$.

### Wersja z rachunkiem różniczkowym i całkowym

**Zadanie.** Wyprowadź wzór na prędkość dźwięku w powietrzu i oblicz ją dla 20°C. Oblicz pochodną $dv/dT$.

W gazie sprężanym adiabatycznie $pV^\gamma = \text{const}$, więc moduł ściśliwości $K = -V\,dp/dV = \gamma p$. Stąd $v = \sqrt{\gamma p/\rho} = \sqrt{\gamma RT/M}$ (bo $p/\rho = RT/M$, 11.04).

Dla powietrza ($\gamma = 1{,}4$, $M = 0{,}029\ \mathrm{kg/mol}$, $T = 293\ \mathrm{K}$): $v \approx 343\ \mathrm{m/s}$.

$$\frac{dv}{dT} = \frac{v}{2T} \approx 0{,}59\ \mathrm{\frac{m/s}{K}}.$$

Newton przyjął proces izotermiczny ($K = p$) i dostał ok. 290 m/s. Laplace poprawił to, zauważając, że sprężenia w fali dźwiękowej są zbyt szybkie na wymianę ciepła.

## Typowe pułapki

- **Prędkość fali zależy od częstotliwości lub amplitudy.** Na strunie i w powietrzu nie zależy (brak dyspersji). Zależy tylko od ośrodka.
- **$\mu$ to gęstość.** We wzorze dla struny $\mu$ to masa na jednostkę długości, w kg/m.
- **Wzór izotermiczny.** Dla dźwięku proces jest adiabatyczny, więc trzeba wziąć $\gamma$.
- **Dźwięk szybszy w gazach o większej gęstości.** W gazie doskonałym prędkość nie zależy od ciśnienia przy stałej $T$. Decydują $T$ i $M$ (hel: ok. 1000 m/s).

## Doświadczenie / symulacja

**Prędkość dźwięku w phyphox.** Eksperyment *Acoustic Stopwatch* (*Stoper akustyczny*): dwa telefony stoją w odległości kilku metrów, a dwie osoby klaszczą po kolei przy swoich telefonach. Prędkość dźwięku wynika z różnicy czasów zmierzonych przez telefony: $v = 2d/(\Delta t_1 - \Delta t_2)$. Powtórz dla kilku odległości i dopasuj prostą.

**Python:** prędkość dźwięku w funkcji temperatury i porównanie gazów.

```python
import numpy as np
import matplotlib.pyplot as plt

R = 8.314
gases = {"powietrze": (1.40, 0.029), "hel": (1.67, 0.004), "CO2": (1.30, 0.044)}
T = np.linspace(250, 350, 100)
for name, (gam, M) in gases.items():
    v = np.sqrt(gam*R*T/M)
    plt.plot(T - 273.15, v, label=name)
    print(f"{name:10s} 20°C: v = {np.sqrt(gam*R*293.15/M):6.0f} m/s")
v20 = np.sqrt(1.4*R*293.15/0.029)
print(f"dv/dT dla powietrza = {v20/(2*293.15):.2f} m/s na K")
print(f"struna μ = 1 g/m, F = 100 N: v = {np.sqrt(100/1e-3):.0f} m/s")
plt.xlabel("t [°C]"); plt.ylabel("v [m/s]"); plt.yscale("log"); plt.grid(True); plt.legend(); plt.show()
```

## Zadania

### A. Poziom maturalny _(opcjonalnie — rozgrzewka)_

1. Lina o długości 10 m i masie 2 kg jest napięta siłą 200 N. Ile czasu potrzebuje impuls na przebycie liny?

<details>
<summary>Odpowiedź</summary>

$\mu = 0{,}2\ \mathrm{kg/m}$, $v = \sqrt{200/0{,}2} \approx 31{,}6\ \mathrm{m/s}$, $t \approx 0{,}32\ \mathrm{s}$.
</details>

2. Ile razy trzeba zwiększyć siłę naciągu struny, żeby prędkość fali wzrosła dwukrotnie?

<details>
<summary>Odpowiedź</summary>

Czterokrotnie.
</details>

### B. Poziom akademicki

1. Ktoś uderza młotkiem w szynę stalową. Obserwator w odległości 1 km słyszy dwa uderzenia: jedno przez szynę, drugie przez powietrze. Oblicz odstęp czasu ($E = 200\ \mathrm{GPa}$, $\rho = 7800\ \mathrm{kg/m^3}$).

<details>
<summary>Odpowiedź</summary>

$v_{\text{stal}} = \sqrt{E/\rho} \approx 5060\ \mathrm{m/s}$. Czasy wynoszą 0,20 s i 2,92 s, różnica ok. 2,7 s.
</details>

2. Oblicz prędkość dźwięku w wodzie ($K = 2{,}2\ \mathrm{GPa}$).

<details>
<summary>Odpowiedź</summary>

$v = \sqrt{2{,}2\cdot10^9/1000} \approx 1480\ \mathrm{m/s}$.
</details>

3. Jak zmieni się moc fali na strunie, gdy amplituda i częstotliwość wzrosną dwukrotnie, a naciąg się nie zmieni?

<details>
<summary>Odpowiedź</summary>

$\bar P \propto \omega^2A^2$, więc wzrośnie 16 razy.
</details>

4. Pokaż, że wypadkowa siła poprzeczna działająca na element struny wynosi $F\,\partial^2y/\partial x^2\,dx$. Przyjmij małe kąty, czyli $\sin\theta \approx \tan\theta = \partial y/\partial x$.

<details>
<summary>Odpowiedź</summary>

$F_y = F\left[\dfrac{\partial y}{\partial x}\Big\rvert_{x + dx} - \dfrac{\partial y}{\partial x}\Big\rvert_x\right] = F\dfrac{\partial^2y}{\partial x^2}dx$.
</details>

## Źródła

- OpenStax, *Fizyka dla szkół wyższych*, t. 1 — §16.3 (prędkość fali na strunie), §16.4 (energia i moc fali), §17.2 (prędkość dźwięku).
- Halliday, Resnick, Walker, *Podstawy fizyki* — wyd. 2015: t. 2, §16.2–16.4, §17.1; wyd. 1: t. 2, §17.6–17.7, §18.2.
