# 04.01 — Praca siły stałej i zmiennej

> **Moduł:** [04 — Praca, energia i moc](README.md) · **Poziom:** 🟢🔵 matura R + studia · **Status:** ✅ pełny
>
> **Czytaj:**
>
> - OpenStax, *Fizyka dla szkół wyższych*, t. 1, rozdz. 7: [§7.1](https://openstax.org/books/fizyka-dla-szk%C3%B3%C5%82-wy%C5%BCszych-tom-1/pages/7-1-praca) · [wstęp do rozdziału](https://openstax.org/books/fizyka-dla-szk%C3%B3%C5%82-wy%C5%BCszych-tom-1/pages/7-wstep)
> - Halliday, Resnick, Walker, *Podstawy fizyki*, wyd. 2015, t. 1: §7.2–7.5 (s. 189)
> - Halliday, Resnick, Walker, *Podstawy fizyki*, wyd. 1 (2003), t. 1: [§7.2, s. 142](https://home.agh.edu.pl/~czapli/Resnick_1.pdf#page=154), [§7.4–7.6, s. 147](https://home.agh.edu.pl/~czapli/Resnick_1.pdf#page=159) — PDF z serwera AGH

← (początek modułu) · [spis modułu](README.md) · [Energia kinetyczna i twierdzenie o pracy i energii](02-energia-kinetyczna.md) →

## Po co to jest

Praca to sposób, w jaki siła przekazuje energię ciału. Zamiast śledzić siły w każdej chwili (moduł 03), możemy policzyć, ile energii zostało przekazane po drodze — i to często od razu daje odpowiedź. Pojęcie pracy wraca w energii potencjalnej (04.04), w termodynamice (praca gazu, 11), w elektrostatyce (praca pola, napięcie, 12) i w obwodach (praca prądu, 13).

## Teoria w pigułce

**Praca stałej siły** na prostoliniowym przemieszczeniu to iloczyn skalarny:

$$W = \vec{F}\cdot\Delta\vec{r} = Fs\cos\alpha,$$

gdzie $\alpha$ to kąt między siłą a przemieszczeniem. Jednostka: dżul, $1\ \mathrm{J} = 1\ \mathrm{N\cdot m}$.

**Znak pracy.**
- $\alpha < 90^\circ$ — praca dodatnia, siła przekazuje ciału energię (pomaga w ruchu).
- $\alpha = 90^\circ$ — praca zerowa: siła prostopadła do ruchu nie zmienia energii (siła dośrodkowa, siła nacisku na poziomej powierzchni).
- $\alpha > 90^\circ$ — praca ujemna, siła odbiera energię (tarcie, hamowanie).

**Praca siły zmiennej.** Gdy siła zmienia się wzdłuż drogi, dzielimy drogę na małe odcinki $d\vec{r}$ i sumujemy:

$$W = \int_A^B\vec{F}\cdot d\vec{r}, \qquad \text{w 1D: } W = \int_{x_1}^{x_2}F(x)\,dx.$$

Graficznie: **pole pod wykresem $F(x)$** (ze znakiem).

**Praca siły sprężystości.** Do rozciągnięcia sprężyny od $x_1$ do $x_2$ trzeba wykonać pracę $\tfrac12k(x_2^2 - x_1^2)$ — pole trapezu pod prostą $F = kx$.

**Praca siły ciężkości** przy przemieszczeniu z wysokości $h_1$ na $h_2$: $W = mg(h_1 - h_2)$ — niezależnie od kształtu drogi. To cecha sił zachowawczych (04.04).

**Praca wypadkowej** to suma prac wszystkich sił; równa się zmianie energii kinetycznej (04.02).

## Wzory i założenia

| Wzór | Znaczenie | Kiedy obowiązuje |
|---|---|---|
| $W = Fs\cos\alpha$ | praca stałej siły | prostoliniowe przemieszczenie |
| $W = \int\vec{F}\cdot d\vec{r}$ | praca siły zmiennej | dowolny tor |
| $W = \int_{x_1}^{x_2}F\,dx$ | praca w 1D | pole pod $F(x)$ |
| $W_g = mg(h_1 - h_2)$ | praca siły ciężkości | $g = \text{const}$; nie zależy od drogi |
| $W_s = \tfrac12k(x_1^2 - x_2^2)$ | praca siły sprężystości | prawo Hooke'a; nie zależy od drogi |
| $W_T = -\mu_kNs$ | praca tarcia kinetycznego | stała siła nacisku; zawsze ujemna |

## Przykład rozwiązany

**Zadanie.** Dziecko ciągnie sanki o masie 10 kg na odcinku 20 m po poziomym śniegu siłą 50 N skierowaną pod kątem $30^\circ$ do poziomu; $\mu_k = 0{,}1$. Oblicz pracę każdej siły i pracę wypadkową.

- **Siła ciągnąca:** $W_F = 50\cdot20\cdot\cos30^\circ \approx 866\ \mathrm{J}$.
- **Nacisk podłoża** (pionowo): $N = mg - F\sin30^\circ = 98{,}1 - 25 = 73{,}1\ \mathrm{N}$ — praca zerowa, bo siła prostopadła do ruchu.
- **Ciężar:** praca zerowa.
- **Tarcie:** $T = 0{,}1\cdot73{,}1 = 7{,}31\ \mathrm{N}$, $W_T = -7{,}31\cdot20 \approx -146\ \mathrm{J}$.
- **Praca wypadkowa:** $866 - 146 = 720\ \mathrm{J}$ — o tyle wzrośnie energia kinetyczna sanek (04.02).

### Wersja z rachunkiem różniczkowym i całkowym

**Zadanie.** Na ciało działa siła $F(x) = 10 - 2x$ (N, m) skierowana wzdłuż osi $x$. Oblicz pracę przy przesunięciu od $x = 0$ do $x = 5\ \mathrm{m}$ oraz od $0$ do $8\ \mathrm{m}$.

$$W(0 \to 5) = \int_0^5(10 - 2x)\,dx = [10x - x^2]_0^5 = 25\ \mathrm{J},$$

$$W(0 \to 8) = [10x - x^2]_0^8 = 80 - 64 = 16\ \mathrm{J}.$$

Dla $x > 5\ \mathrm{m}$ siła zmienia znak i wykonuje pracę ujemną. Graficznie: pole trójkąta nad osią (25 J) minus pole trójkąta pod osią (9 J).

## Typowe pułapki

- **Praca = siła razy droga zawsze.** Tylko gdy siła jest stała i równoległa do przemieszczenia.
- **Siła prostopadła do ruchu wykonuje pracę.** Nie wykonuje — np. siła dośrodkowa w ruchu po okręgu.
- **Trzymanie ciężaru to praca.** W sensie fizycznym nie (brak przemieszczenia), choć mięśnie zużywają energię.
- **Dodatni kąt, dodatnia praca.** Liczy się kąt między siłą a przemieszczeniem, a nie kąt z osią.
- **Praca tarcia $= -\mu mgs$ przy ukośnej sile.** Nacisk zmienia się, gdy siła ciągnąca ma składową pionową.

## Doświadczenie / symulacja

**Symulacja PhET:** *Rampa: siły i ruch* — zakładka z wykresami energii i pracy. Wciągnij szafkę na rampę i porównaj pracę siły przyłożonej, pracę ciężaru i pracę tarcia.

**Pomiar.** Siłomierzem (albo wagą bagażową) ciągnij skrzynkę ze stałą prędkością na znanym odcinku, odczytując siłę co 20 cm. Narysuj $F(x)$ i oblicz pracę jako pole pod wykresem.

**Python:** praca jako pole pod wykresem siły zmiennej (dane „pomiarowe” i całkowanie numeryczne).

```python
import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import trapezoid

x = np.linspace(0, 8, 33)
F = 10 - 2*x
W = trapezoid(F, x)
print(f"W(0 → 8 m) = {W:.2f} J (dokładnie 16 J)")

plt.plot(x, F, "o-")
plt.fill_between(x, F, where=F >= 0, alpha=0.3, label="praca dodatnia")
plt.fill_between(x, F, where=F < 0, alpha=0.3, color="C3", label="praca ujemna")
plt.axhline(0, color="gray"); plt.xlabel("x [m]"); plt.ylabel("F [N]"); plt.grid(True); plt.legend(); plt.show()
```

## Zadania

### A. Poziom maturalny

1. Jaką pracę trzeba wykonać, żeby podnieść skrzynkę o masie 20 kg na wysokość 1,5 m ze stałą prędkością?

<details>
<summary>Odpowiedź</summary>

$W = mgh \approx 294\ \mathrm{J}$.
</details>

2. Walizkę ciągniemy na odcinku 100 m siłą 40 N skierowaną pod kątem $60^\circ$ do poziomu. Oblicz pracę tej siły.

<details>
<summary>Odpowiedź</summary>

$W = 40\cdot100\cdot0{,}5 = 2000\ \mathrm{J}$.
</details>

3. Skrzynka o masie 2 kg przesuwa się po poziomej podłodze na odcinku 5 m; $\mu_k = 0{,}3$. Oblicz pracę tarcia.

<details>
<summary>Odpowiedź</summary>

$W_T = -0{,}3\cdot2\cdot9{,}81\cdot5 \approx -29{,}4\ \mathrm{J}$.
</details>

4. Siła rośnie liniowo od 0 do 20 N na pierwszych 2 m drogi, a potem jest stała i równa 20 N na kolejnych 3 m. Oblicz pracę.

<details>
<summary>Odpowiedź</summary>

$W = \tfrac12\cdot2\cdot20 + 3\cdot20 = 80\ \mathrm{J}$.
</details>

5. Jaką pracę wykonuje siła dośrodkowa w czasie jednego obiegu satelity po orbicie kołowej? Uzasadnij.

<details>
<summary>Odpowiedź</summary>

Zero — siła jest w każdej chwili prostopadła do prędkości.
</details>

### B. Poziom akademicki

1. Sprężynę o współczynniku $400\ \mathrm{N/m}$ rozciągnięto z wydłużenia 10 cm do 20 cm. Jaką pracę wykonano?

<details>
<summary>Odpowiedź</summary>

$W = \tfrac12\cdot400(0{,}04 - 0{,}01) = 6\ \mathrm{J}$.
</details>

2. Łańcuch o długości $L$ i masie $M$ zwisa pionowo z krawędzi dachu. Jaką pracę trzeba wykonać, żeby wciągnąć go na dach?

<details>
<summary>Odpowiedź</summary>

Wciągając odcinek $dy$ z głębokości $y$: $dW = \dfrac{M}{L}g\,y\,dy$; $W = \dfrac{MgL}{2}$ (środek masy podnosi się o $L/2$).
</details>

3. Siła $\vec{F} = (2y,\ x)$ (N, m). Oblicz jej pracę przy przejściu z $(0,0)$ do $(1,1)$ a) wzdłuż prostej $y = x$, b) najpierw wzdłuż osi $x$, potem pionowo. Co z tego wynika?

<details>
<summary>Odpowiedź</summary>

a) $\int_0^1(2x + x)\,dx = 1{,}5\ \mathrm{J}$; b) $0 + \int_0^1 1\,dy = 1\ \mathrm{J}$. Praca zależy od drogi — siła nie jest zachowawcza (04.04).
</details>

4. Siła oporu $F = -bv$ działa na ciało poruszające się ze stałą prędkością $v$ przez czas $t$. Oblicz pracę oporu. Jaką moc musi dostarczać silnik?

<details>
<summary>Odpowiedź</summary>

$W = -bv\cdot vt = -bv^2t$; moc $P = bv^2$.
</details>

## Źródła

- OpenStax, *Fizyka dla szkół wyższych*, t. 1, rozdz. 7 — §7.1: praca stałej i zmiennej siły, praca jako całka.
- Halliday, Resnick, Walker, *Podstawy fizyki* — wyd. 2015: t. 1, §7.2–7.5; wyd. 1: t. 1, §7.2 i §7.4–7.6.
