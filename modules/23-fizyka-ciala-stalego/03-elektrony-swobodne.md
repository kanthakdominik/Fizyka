# 23.03 — Model elektronów swobodnych w metalach

> **Moduł:** [23 — Fizyka ciała stałego](README.md) · **Poziom:** 🔵 studia · **Status:** ✅ pełny
>
> **Czytaj:**
>
> - OpenStax, *Fizyka dla szkół wyższych*, t. 3, rozdz. 9: [§9.4](https://openstax.org/books/fizyka-dla-szk%C3%B3%C5%82-wy%C5%BCszych-tom-3/pages/9-4-model-elektronow-swobodnych-w-metalach) · [wstęp do rozdziału](https://openstax.org/books/fizyka-dla-szk%C3%B3%C5%82-wy%C5%BCszych-tom-3/pages/9-wstep)
> - Halliday, Resnick, Walker, *Podstawy fizyki*, wyd. 2015, t. 5: §41.1 (s. 130)
> - Halliday, Resnick, Walker, *Podstawy fizyki*, wyd. 1 (2003), t. 5: [§42.5, s. 107](https://home.agh.edu.pl/~czapli/Resnick_5.pdf#page=123) — PDF z serwera AGH

← [Struktura krystaliczna ciał stałych](02-krysztaly.md) · [spis modułu](README.md) · [Teoria pasmowa ciał stałych](04-teoria-pasmowa.md) →

## Po co to jest

Klasyczny model Drudego (13.01) dobrze opisuje prawo Ohma, ale zawodzi przy cieple właściwym metali i drodze swobodnej elektronów. Wyjaśnia to dopiero model kwantowy: elektrony w metalu to gaz fermionów podlegający zakazowi Pauliego (21.04). Wypełniają poziomy aż do **energii Fermiego**, rzędu kilku eV, a tylko te najszybsze, przy samej górze, biorą udział w przewodnictwie i wymianie ciepła. Ten obraz jest wstępem do teorii pasmowej i półprzewodników.

## Teoria w pigułce

**Model elektronów swobodnych.** Elektrony walencyjne metalu poruszają się w krysztale jak w „pudle” o rozmiarach kryształu (20.06), nie oddziałując ze sobą ani z jonami (w pierwszym przybliżeniu). Dozwolone stany to fale stojące o skwantowanych wektorach falowych. Każdy stan może zająć dwa elektrony (spin).

**Gęstość stanów.** Liczba stanów na jednostkę energii i objętości rośnie jak pierwiastek z energii:

$$g(E) = \frac{(2m)^{3/2}}{2\pi^2\hbar^3}\sqrt E.$$

**Energia Fermiego.** W temperaturze 0 K elektrony zajmują po kolei najniższe stany aż do energii $E_F$. Całkowanie $g(E)$ od 0 do $E_F$ daje koncentrację elektronów $n$:

$$E_F = \frac{\hbar^2}{2m}(3\pi^2n)^{2/3}.$$

Dla miedzi ($n = 8{,}5\cdot10^{28}\ \mathrm{m^{-3}}$) $E_F \approx 7\ \mathrm{eV}$. Prędkość Fermiego to ok. 1,6·10⁶ m/s, a temperatura Fermiego $E_F/k \approx 80\,000\ \mathrm K$. Elektrony w metalu poruszają się szybko nawet w zerze bezwzględnym. To skutek zakazu Pauliego, a nie ruchu cieplnego.

**Rozkład Fermiego–Diraca.** W temperaturze $T$ prawdopodobieństwo obsadzenia stanu o energii $E$ wynosi

$$f(E) = \frac{1}{e^{(E - E_F)/kT} + 1}.$$

W 0 K to funkcja schodkowa. W temperaturze pokojowej ($kT \approx 0{,}026\ \mathrm{eV}$) rozmywa się tylko w pasie o szerokości kilku $kT$ wokół $E_F$.

**Konsekwencje:**
- **Ciepło właściwe elektronów** jest małe: wzbudzić termicznie mogą się tylko elektrony z pasa ok. $kT$ wokół $E_F$, czyli ułamek $\sim kT/E_F \approx 0{,}4\%$. Dlatego metale mają ciepło właściwe zbliżone do izolatorów (prawo Dulonga–Petita), co dla fizyki klasycznej było zagadką.
- **Przewodnictwo**: w modelu Drudego trzeba użyć prędkości Fermiego zamiast średniej prędkości termicznej. Droga swobodna wychodzi wtedy ok. 40 nm (13.01). Tak długie drogi są możliwe, bo fala elektronu w idealnej sieci periodycznej się nie rozprasza. Rozpraszają ją tylko drgania sieci i defekty.
- **Praca wyjścia** (20.02) to energia potrzebna, żeby wyciągnąć elektron z poziomu Fermiego na zewnątrz metalu.

## Wzory i założenia

| Wzór | Znaczenie | Kiedy obowiązuje |
|---|---|---|
| $E_F = \dfrac{\hbar^2}{2m}(3\pi^2n)^{2/3}$ | energia Fermiego | gaz elektronów swobodnych |
| $v_F = \sqrt{2E_F/m}$, $T_F = E_F/k$ | prędkość i temperatura Fermiego | — |
| $g(E) \propto\sqrt E$ | gęstość stanów | 3D, elektrony swobodne |
| $f(E) = 1/(e^{(E - E_F)/kT} + 1)$ | rozkład Fermiego–Diraca | fermiony w równowadze |
| $\bar E = \tfrac35E_F$ | średnia energia elektronu | $T = 0$ |

## Przykład rozwiązany

### Wersja z rachunkiem różniczkowym i całkowym

**Zadanie.** Wyprowadź energię Fermiego z gęstości stanów i oblicz ją dla miedzi i sodu ($n_{\mathrm{Na}} = 2{,}65\cdot10^{28}\ \mathrm{m^{-3}}$). Oblicz średnią energię elektronu w 0 K.

$$n = \int_0^{E_F}g(E)\,dE = \frac{(2m)^{3/2}}{2\pi^2\hbar^3}\cdot\frac23E_F^{3/2} \Rightarrow E_F = \frac{\hbar^2}{2m}(3\pi^2n)^{2/3}.$$

Cu: $E_F \approx 7{,}0\ \mathrm{eV}$. Na: $\approx 3{,}2\ \mathrm{eV}$.

Średnia energia: $\bar E = \dfrac{\int_0^{E_F}Eg(E)dE}{\int_0^{E_F}g(E)dE} = \dfrac{\tfrac25E_F^{5/2}}{\tfrac23E_F^{3/2}} = \tfrac35E_F \approx 4{,}2\ \mathrm{eV}$ dla miedzi. Gaz klasyczny miałby w 300 K tylko $\tfrac32kT \approx 0{,}04\ \mathrm{eV}$.

## Typowe pułapki

- **W 0 K elektrony stoją.** Wypełniają stany do $E_F$ i mają energie kinetyczne rzędu eV.
- **Wszystkie elektrony przewodzą prąd.** W przewodnictwie i cieple biorą udział tylko elektrony blisko $E_F$. Głębsze nie mają wolnych stanów, do których mogłyby przejść.
- **$f(E_F) = 1$.** Na poziomie Fermiego prawdopodobieństwo obsadzenia wynosi $\tfrac12$ (dla $T > 0$).
- **Model elektronów swobodnych wyjaśnia izolatory.** Nie wyjaśnia. Do tego potrzebna jest teoria pasmowa (23.04).

## Doświadczenie / symulacja

**Rozkład Fermiego–Diraca w Pythonie.** Narysuj $f(E)$ i $g(E)f(E)$ dla miedzi w 0 K, 300 K i 3000 K. Zobacz, jak mała część elektronów zmienia stan nawet w wysokiej temperaturze.

**Python:** energia Fermiego dla kilku metali, rozkład Fermiego–Diraca i ułamek elektronów wzbudzonych termicznie.

```python
import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import quad

hbar, me, e, k = 1.054571817e-34, 9.1093837e-31, 1.602176634e-19, 1.380649e-23
metale = {"Na": 2.65e28, "Al": 18.1e28, "Cu": 8.49e28, "Ag": 5.86e28}
for nazwa, n in metale.items():
    EF = hbar**2/(2*me)*(3*np.pi**2*n)**(2/3)
    print(f"{nazwa}: E_F = {EF/e:.2f} eV, v_F = {np.sqrt(2*EF/me):.2e} m/s, T_F = {EF/k:.0f} K")

EF = hbar**2/(2*me)*(3*np.pi**2*8.49e28)**(2/3)/e      # Cu, eV
E = np.linspace(0, 9, 600)
for T in (300, 3000, 10000):
    kT = k*T/e
    f = 1/(np.exp((E - EF)/kT) + 1)
    plt.plot(E, np.sqrt(E)*f, label=f"{T} K")
    wzb = quad(lambda x: np.sqrt(x)/(np.exp((x - EF)/kT) + 1), EF, EF + 20*kT)[0]/quad(lambda x: np.sqrt(x), 0, EF)[0]
    print(f"T = {T:5d} K: ułamek elektronów powyżej E_F ≈ {wzb:.4f} (kT/E_F = {kT/EF:.4f})")
plt.xlabel("E [eV]"); plt.ylabel("g(E)·f(E) (wzgl.)"); plt.legend(); plt.grid(True); plt.show()
```

## Zadania

### A. Poziom maturalny _(opcjonalnie — rozgrzewka)_

1. Dlaczego elektrony w metalu mają duże prędkości nawet w zerze bezwzględnym?

<details>
<summary>Odpowiedź</summary>

Zakaz Pauliego nie pozwala im wszystkim zająć najniższego stanu. Wypełniają kolejne stany aż do energii Fermiego, rzędu kilku eV.
</details>

2. Jaka jest wartość $f(E)$ dla $E = E_F$ w dowolnej temperaturze większej od zera?

<details>
<summary>Odpowiedź</summary>

$\tfrac12$.
</details>

### B. Poziom akademicki

1. Oblicz prawdopodobieństwo obsadzenia stanu o energii $E_F + 0{,}1\ \mathrm{eV}$ i $E_F - 0{,}1\ \mathrm{eV}$ w 300 K.

<details>
<summary>Odpowiedź</summary>

$x = 0{,}1/0{,}0259 \approx 3{,}87$: $f = 1/(e^{3{,}87} + 1) \approx 0{,}020$ i $1 - 0{,}020 = 0{,}980$.
</details>

2. Pokaż, że wkład elektronów do ciepła właściwego jest w przybliżeniu $\dfrac{kT}{E_F}$ razy mniejszy od klasycznego $\tfrac32nk$. Ile to dla miedzi w 300 K?

<details>
<summary>Odpowiedź</summary>

Wzbudza się ułamek $\sim kT/E_F$ elektronów, każdy zyskuje energię $\sim kT$. Energia $\sim n(kT)^2/E_F$, więc $C \sim nk\cdot kT/E_F$ (dokładnie $\tfrac{\pi^2}{2}nk\,kT/E_F$). Dla miedzi $kT/E_F \approx 0{,}004$.
</details>

3. Gwiazdy białe karły to gaz zdegenerowanych elektronów o koncentracji ok. $10^{36}\ \mathrm{m^{-3}}$. Oblicz energię Fermiego. Czy elektrony są relatywistyczne?

<details>
<summary>Odpowiedź</summary>

Wzór nierelatywistyczny daje $E_F \approx 0{,}36\ \mathrm{MeV}$, porównywalnie z $m_ec^2 = 0{,}511\ \mathrm{MeV}$, więc elektrony są częściowo relatywistyczne. Ciśnienie Fermiego podtrzymuje gwiazdę przed zapadnięciem do granicy Chandrasekhara (ok. 1,4 masy Słońca).
</details>

## Źródła

- OpenStax, *Fizyka dla szkół wyższych*, t. 3, rozdz. 9 — §9.4: model elektronów swobodnych w metalach.
- Halliday, Resnick, Walker, *Podstawy fizyki* — wyd. 2015: t. 5, §41.1; wyd. 1: t. 5, §42.5.
