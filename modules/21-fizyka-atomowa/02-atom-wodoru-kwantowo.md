# 21.02 — Atom wodoru w mechanice kwantowej, liczby kwantowe

> **Moduł:** [21 — Fizyka atomowa](README.md) · **Poziom:** 🔵 studia · **Status:** ✅ pełny
>
> **Czytaj:**
>
> - OpenStax, *Fizyka dla szkół wyższych*, t. 3, rozdz. 8: [§8.1](https://openstax.org/books/fizyka-dla-szk%C3%B3%C5%82-wy%C5%BCszych-tom-3/pages/8-1-atom-wodoru) · [wstęp do rozdziału](https://openstax.org/books/fizyka-dla-szk%C3%B3%C5%82-wy%C5%BCszych-tom-3/pages/8-wstep)
> - Halliday, Resnick, Walker, *Podstawy fizyki*, wyd. 2015, t. 5: §39.5 (s. 65), §40.1 (s. 87)
> - Halliday, Resnick, Walker, *Podstawy fizyki*, wyd. 1 (2003), t. 5: [§40.8, s. 50](https://home.agh.edu.pl/~czapli/Resnick_5.pdf#page=66) — PDF z serwera AGH

← [Model Bohra i widmo atomu wodoru](01-model-bohra.md) · [spis modułu](README.md) · [Orbitalny moment magnetyczny i spin elektronu](03-moment-magnetyczny-i-spin.md) →

## Po co to jest

Rozwiązanie równania Schrödingera dla atomu wodoru zastępuje orbity Bohra **orbitalami**, czyli chmurami prawdopodobieństwa o określonych kształtach. Trzy liczby kwantowe $n$, $l$, $m$ (plus spin, 21.03) wyjaśniają układ okresowy pierwiastków, kształty cząsteczek i wiązania chemiczne, reguły wyboru w widmach i działanie MRI. To najważniejszy przykład kwantowej teorii atomu i jedyny atom, dla którego mamy rozwiązanie dokładne.

## Teoria w pigułce

**Równanie Schrödingera w trzech wymiarach** z potencjałem Coulomba $U(r) = -ke^2/r$. Symetria kulista pozwala rozdzielić zmienne we współrzędnych sferycznych: $\psi_{nlm}(r, \theta, \varphi) = R_{nl}(r)Y_{lm}(\theta, \varphi)$. Warunki skończoności i jednoznaczności dają trzy liczby kwantowe.

| Liczba kwantowa | Wartości | Co określa |
|---|---|---|
| główna $n$ | 1, 2, 3, … | energię: $E_n = -13{,}6\ \mathrm{eV}/n^2$ (jak u Bohra) |
| orbitalna $l$ | 0, 1, …, $n - 1$ | wartość momentu pędu: $L = \sqrt{l(l + 1)}\hbar$ |
| magnetyczna $m_l$ | $-l$, …, 0, …, $+l$ | rzut momentu pędu na oś $z$: $L_z = m_l\hbar$ |

Oznaczenia literowe: $l = 0, 1, 2, 3$ to s, p, d, f. Stan $n = 2$, $l = 1$ to 2p.

**Degeneracja.** Energia wodoru zależy tylko od $n$, a stanów o danym $n$ jest $n^2$ (z $l$ i $m_l$). Ze spinem $2n^2$. W atomach wieloelektronowych energia zależy też od $l$ (21.04).

**Stan podstawowy** 1s jest kulisto symetryczny: $\psi_{100} = \dfrac{1}{\sqrt{\pi a_0^3}}e^{-r/a_0}$. Moment pędu wynosi **zero**, wbrew modelowi Bohra.

**Radialna gęstość prawdopodobieństwa.** Prawdopodobieństwo znalezienia elektronu w cienkiej powłoce między $r$ a $r + dr$:

$$P(r)\,dr = \lvert\psi\rvert^24\pi r^2dr.$$

Dla stanu 1s: $P(r) = \dfrac{4r^2}{a_0^3}e^{-2r/a_0}$. Maksimum przypada dokładnie w $r = a_0$, czyli na promieniu orbity Bohra. Średnia odległość to $\langle r\rangle = 1{,}5a_0$.

**Reguły wyboru.** Przy emisji lub pochłanianiu fotonu (który niesie moment pędu $\hbar$) $\Delta l = \pm1$, $\Delta m_l = 0, \pm1$. Przejście 2s→1s jest wzbronione, więc stan 2s żyje długo (ok. 0,1 s).

**Kwantyzacja przestrzenna.** Wektor momentu pędu nie może mieć dowolnego kierunku: jego rzut na oś $z$ przyjmuje tylko $2l + 1$ wartości. Długość wektora $\sqrt{l(l + 1)}\hbar$ jest większa od największego rzutu $l\hbar$, więc wektor nigdy nie leży dokładnie wzdłuż osi.

## Wzory i założenia

| Wzór | Znaczenie | Kiedy obowiązuje |
|---|---|---|
| $E_n = -13{,}6\ \mathrm{eV}/n^2$ | energia | wodór |
| $L = \sqrt{l(l + 1)}\hbar$, $L_z = m_l\hbar$ | moment pędu | $l < n$, $\lvert m_l\rvert \le l$ |
| $\psi_{100} = e^{-r/a_0}/\sqrt{\pi a_0^3}$ | stan podstawowy | — |
| $P(r) = 4\pi r^2\lvert\psi\rvert^2$ | radialna gęstość prawdopodobieństwa | stany kuliście symetryczne |
| $\Delta l = \pm1$ | reguła wyboru | przejścia dipolowe |

## Przykład rozwiązany

**Zadanie.** Wypisz wszystkie stany wodoru dla $n = 3$ (bez spinu). Ile ich jest? Jaki największy moment pędu może mieć elektron w tej powłoce?

$l = 0$: 1 stan (3s). $l = 1$: 3 stany (3p). $l = 2$: 5 stanów (3d). Razem $9 = n^2$, ze spinem 18.

Największe $L = \sqrt{2\cdot3}\hbar = \sqrt6\hbar \approx 2{,}45\hbar$.

### Wersja z rachunkiem różniczkowym i całkowym

**Zadanie.** Dla stanu 1s sprawdź normalizację, znajdź najbardziej prawdopodobny promień i oblicz prawdopodobieństwo, że elektron jest bliżej jądra niż $a_0$.

Normalizacja: $\displaystyle\int_0^\infty\frac{4r^2}{a_0^3}e^{-2r/a_0}dr = \frac{4}{a_0^3}\cdot\frac{2!}{(2/a_0)^3} = 1$.

Maksimum: $\dfrac{d}{dr}(r^2e^{-2r/a_0}) = (2r - 2r^2/a_0)e^{-2r/a_0} = 0 \Rightarrow r = a_0$.

$P(r < a_0) = \displaystyle\int_0^{a_0}P(r)dr = 1 - 5e^{-2} \approx 0{,}32$. Elektron jest częściej dalej niż $a_0$.

## Typowe pułapki

- **Gęstość prawdopodobieństwa największa w $r = a_0$.** $\lvert\psi\rvert^2$ dla 1s jest największa w jądrze ($r = 0$). Największa jest **radialna** gęstość $P(r)$, bo powłoki sferyczne rosną jak $r^2$.
- **Moment pędu $l\hbar$.** Wartość momentu pędu to $\sqrt{l(l + 1)}\hbar$. $l\hbar$ to największy rzut.
- **$l$ może być równe $n$.** $l$ przyjmuje wartości od 0 do $n - 1$.
- **Orbital to tor elektronu.** Orbital to funkcja falowa, a rysunki pokazują obszary dużej gęstości prawdopodobieństwa.

## Doświadczenie / symulacja

**Wizualizacja orbitali.** Narysuj w Pythonie przekroje $\lvert\psi\rvert^2$ dla orbitali 1s, 2s, 2p i 3d (z gotowych funkcji w `scipy.special`). Porównaj z rysunkami z podręcznika chemii.

**Symulacja PhET:** *Modele atomu wodoru* — model Schrödingera z rozkładem prawdopodobieństwa.

**Python:** radialne gęstości prawdopodobieństwa dla wodoru i sprawdzenie całek.

```python
import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import quad
from scipy.special import genlaguerre, factorial

def R_nl(n, l, r):                                 # r w jednostkach a0
    rho = 2*r/n
    N = np.sqrt((2/n)**3*factorial(n - l - 1)/(2*n*factorial(n + l)))
    return N*np.exp(-rho/2)*rho**l*genlaguerre(n - l - 1, 2*l + 1)(rho)

r = np.linspace(0, 25, 1000)
for n, l, nazwa in [(1, 0, "1s"), (2, 0, "2s"), (2, 1, "2p"), (3, 0, "3s"), (3, 2, "3d")]:
    P = r**2*R_nl(n, l, r)**2
    norm = quad(lambda x: x**2*R_nl(n, l, x)**2, 0, np.inf)[0]
    sr = quad(lambda x: x**3*R_nl(n, l, x)**2, 0, np.inf)[0]
    print(f"{nazwa}: normalizacja {norm:.4f}, ⟨r⟩ = {sr:.2f} a0, maksimum P(r) w {r[np.argmax(P)]:.2f} a0")
    plt.plot(r, P, label=nazwa)
print(f"P(r < a0) dla 1s = {quad(lambda x: x**2*R_nl(1, 0, x)**2, 0, 1)[0]:.4f} (1 − 5e⁻² = {1 - 5*np.exp(-2):.4f})")
plt.xlabel("r / a0"); plt.ylabel("P(r)"); plt.legend(); plt.grid(True); plt.show()
```

## Zadania

### A. Poziom maturalny _(opcjonalnie — rozgrzewka)_

1. Jakie wartości może przyjmować $m_l$ dla elektronu w stanie $l = 2$?

<details>
<summary>Odpowiedź</summary>

$-2, -1, 0, 1, 2$.
</details>

2. Ile stanów (ze spinem) ma powłoka $n = 2$?

<details>
<summary>Odpowiedź</summary>

$2n^2 = 8$.
</details>

### B. Poziom akademicki

1. Oblicz $\langle r\rangle$ dla stanu 1s.

<details>
<summary>Odpowiedź</summary>

$\langle r\rangle = \displaystyle\int_0^\infty r\frac{4r^2}{a_0^3}e^{-2r/a_0}dr = \frac{4}{a_0^3}\cdot\frac{3!}{(2/a_0)^4} = \frac32a_0$.
</details>

2. Które z przejść są dozwolone: 3d→2p, 3d→1s, 2p→1s, 3s→2s?

<details>
<summary>Odpowiedź</summary>

Dozwolone 3d→2p i 2p→1s ($\Delta l = \pm1$). 3d→1s ($\Delta l = 2$) i 3s→2s ($\Delta l = 0$) są wzbronione w przybliżeniu dipolowym.
</details>

3. Dla $l = 1$ oblicz kąty, jakie wektor $\vec L$ może tworzyć z osią $z$.

<details>
<summary>Odpowiedź</summary>

$\cos\theta = m_l/\sqrt{l(l + 1)} = m_l/\sqrt2$: $45^\circ$, $90^\circ$, $135^\circ$.
</details>

## Źródła

- OpenStax, *Fizyka dla szkół wyższych*, t. 3, rozdz. 8 — §8.1: atom wodoru.
- Halliday, Resnick, Walker, *Podstawy fizyki* — wyd. 2015: t. 5, §39.5, §40.1; wyd. 1: t. 5, §40.8.
- Symulacja PhET *Modele atomu wodoru*.
