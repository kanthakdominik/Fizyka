# 20.06 — Równanie Schrödingera: studnia potencjału i oscylator

> **Moduł:** [20 — Podstawy fizyki kwantowej](README.md) · **Poziom:** 🔵 studia · **Status:** ✅ pełny
>
> **Czytaj:**
>
> - OpenStax, *Fizyka dla szkół wyższych*, t. 3, rozdz. 7: [§7.3–7.5](https://openstax.org/books/fizyka-dla-szk%C3%B3%C5%82-wy%C5%BCszych-tom-3/pages/7-3-rownanie-schrodingera) · [wstęp do rozdziału](https://openstax.org/books/fizyka-dla-szk%C3%B3%C5%82-wy%C5%BCszych-tom-3/pages/7-wstep)
> - Halliday, Resnick, Walker, *Podstawy fizyki*, wyd. 2015, t. 5: §39.1–39.4 (s. 45)
> - Halliday, Resnick, Walker, *Podstawy fizyki*, wyd. 1 (2003), t. 5: [§40.1–40.7, s. 34](https://home.agh.edu.pl/~czapli/Resnick_5.pdf#page=50) — PDF z serwera AGH

← [Funkcja falowa i zasada nieoznaczoności](05-funkcja-falowa-i-nieoznaczonosc.md) · [spis modułu](README.md) · [Tunelowanie przez barierę potencjału](07-tunelowanie.md) →

## Po co to jest

Równanie Schrödingera jest dla mechaniki kwantowej tym, czym druga zasada dynamiki dla klasycznej. Z niego wynika, że energia cząstki uwięzionej w ograniczonym obszarze może przyjmować tylko określone wartości. Wyjaśnia to widma atomów (21), budowę układu okresowego, wiązania chemiczne, pasma energetyczne w półprzewodnikach (23) i barwę kropek kwantowych w ekranach QLED, zależną od ich rozmiaru. Prosty model „cząstki w pudle” daje już większość tych jakościowych wniosków.

## Teoria w pigułce

**Równanie Schrödingera niezależne od czasu** (w jednym wymiarze) dla cząstki o masie $m$ i energii $E$ w potencjale $U(x)$:

$$-\frac{\hbar^2}{2m}\frac{d^2\psi}{dx^2} + U(x)\psi = E\psi.$$

Pierwszy wyraz odpowiada energii kinetycznej ($p^2/2m$, z $p \leftrightarrow -i\hbar\,d/dx$). Rozwiązania muszą być skończone, ciągłe i normalizowalne. Te warunki dopuszczają tylko wybrane wartości $E$, czyli **kwantyzację energii**.

**Nieskończona studnia potencjału (cząstka w pudle)** o szerokości $L$: wewnątrz $U = 0$, a ściany są nieprzenikalne, więc $\psi(0) = \psi(L) = 0$. Rozwiązania to fale stojące, jak na strunie (10.03):

$$\psi_n = \sqrt{\frac2L}\sin\frac{n\pi x}{L}, \qquad E_n = \frac{n^2h^2}{8mL^2} = n^2E_1, \qquad n = 1, 2, 3, \dots$$

- Najniższa energia $E_1 > 0$: cząstka uwięziona nigdy nie stoi w miejscu (zgodnie z zasadą nieoznaczoności, 20.05).
- Poziomy rosną jak $n^2$, a odstępy rosną, gdy pudło się zmniejsza ($\propto 1/L^2$).
- Funkcja $\psi_n$ ma $n - 1$ węzłów.

**Skończona studnia.** Funkcja falowa wnika w ścianki i zanika w nich wykładniczo. Liczba stanów związanych jest skończona. Wnikanie w barierę prowadzi do tunelowania (20.07).

**Oscylator harmoniczny** ($U = \tfrac12m\omega^2x^2$, model drgań cząsteczek i atomów w krysztale):

$$E_n = \left(n + \tfrac12\right)\hbar\omega, \qquad n = 0, 1, 2, \dots$$

Poziomy są równoodległe, a energia zerowa wynosi $\tfrac12\hbar\omega$.

**Przejścia między poziomami.** Cząstka przechodząca z poziomu $n$ na $m$ emituje lub pochłania foton o energii $hf = \lvert E_n - E_m\rvert$. Tak powstają widma liniowe (21).

**Granica klasyczna.** Dla dużych $n$ (lub dużych $m$, $L$) poziomy leżą tak gęsto, że energia wydaje się ciągła, a $\lvert\psi\rvert^2$ uśredniona po węzłach jest równomierna, jak dla klasycznej kulki odbijającej się w pudle (zasada korespondencji).

## Wzory i założenia

| Wzór | Znaczenie | Kiedy obowiązuje |
|---|---|---|
| $-\frac{\hbar^2}{2m}\psi'' + U\psi = E\psi$ | równanie Schrödingera (1D) | stany stacjonarne |
| $E_n = n^2h^2/(8mL^2)$ | nieskończona studnia | $n = 1, 2, \dots$ |
| $\psi_n = \sqrt{2/L}\sin(n\pi x/L)$ | funkcje własne studni | $0 \le x \le L$ |
| $E_n = (n + \tfrac12)\hbar\omega$ | oscylator harmoniczny | $n = 0, 1, \dots$ |
| $hf = E_n - E_m$ | foton przy przejściu | — |

## Przykład rozwiązany

### Wersja z rachunkiem różniczkowym i całkowym

**Zadanie 1.** Sprawdź, że $\psi = A\sin kx$ spełnia równanie Schrödingera w studni, i wyprowadź warunek kwantyzacji.

$\psi'' = -k^2\psi$, więc $\dfrac{\hbar^2k^2}{2m} = E$. Warunek $\psi(L) = 0$ daje $kL = n\pi$. Stąd $E_n = \dfrac{\hbar^2\pi^2n^2}{2mL^2} = \dfrac{n^2h^2}{8mL^2}$. To warunek fali stojącej: $L = n\lambda/2$ z $\lambda = h/p$.

**Zadanie 2.** Elektron jest uwięziony w studni o szerokości 1 nm (np. kropka kwantowa w uproszczeniu). Oblicz trzy najniższe poziomy energii i długość fali fotonu przy przejściu $2 \to 1$. Jak zmienią się energie dla studni 0,1 nm?

$E_1 = \dfrac{h^2}{8m_eL^2} \approx 0{,}376\ \mathrm{eV}$, $E_2 \approx 1{,}50\ \mathrm{eV}$, $E_3 \approx 3{,}38\ \mathrm{eV}$.

Przejście $2 \to 1$: $\Delta E \approx 1{,}13\ \mathrm{eV}$, $\lambda = hc/\Delta E \approx 1{,}10\ \mu\mathrm m$ (podczerwień).

Dla 0,1 nm energie są 100 razy większe: $E_1 \approx 37{,}6\ \mathrm{eV}$, czyli rząd energii elektronów w atomach. Mniejsza kropka kwantowa świeci bardziej niebiesko.

## Typowe pułapki

- **Najniższa energia w studni to zero.** $E_1 > 0$: dla $n = 0$ funkcja falowa znika wszędzie, czyli nie ma cząstki.
- **Poziomy równoodległe w studni.** W studni rosną jak $n^2$. Równoodległe są w oscylatorze.
- **Cząstka „skacze” przez węzeł.** Węzeł to miejsce zerowego prawdopodobieństwa, ale stan stacjonarny nie opisuje ruchu po torze. Pytanie, jak cząstka przechodzi przez węzeł, wynika z obrazu klasycznego.
- **Równanie Schrödingera dla fotonu.** Opisuje cząstki nierelatywistyczne z masą. Fotony opisuje elektrodynamika kwantowa.

## Doświadczenie / symulacja

**Kropki kwantowe.** Ekrany QLED i niektóre preparaty biologiczne używają kropek kwantowych (nanokryształy CdSe, InP). Barwa zależy od rozmiaru: ok. 2 nm świeci na niebiesko, ok. 6 nm na czerwono. Sprawdź, czy model studni daje właściwy kierunek zależności.

**Symulacja PhET:** *Stany związane kwantowe* (*Quantum Bound States*) — studnia kwadratowa, oscylator, poziomy i funkcje falowe ([phet.colorado.edu/pl](https://phet.colorado.edu/pl/)).

**Python:** numeryczne rozwiązanie równania Schrödingera metodą różnic skończonych (studnia i oscylator).

```python
import numpy as np
from scipy.linalg import eigh_tridiagonal
import matplotlib.pyplot as plt

hbar, me, e = 1.054571817e-34, 9.1093837e-31, 1.602176634e-19

def poziomy(U, x, ile=4):
    dx = x[1] - x[0]
    t = hbar**2/(2*me*dx**2)
    E, psi = eigh_tridiagonal(2*t + U, -t*np.ones(len(x) - 1), select="i", select_range=(0, ile - 1))
    return E/e, psi

L = 1e-9                                            # nieskończona studnia 1 nm (warunki brzegowe: ψ = 0)
x = np.linspace(0, L, 2002)[1:-1]
E, psi = poziomy(np.zeros_like(x), x)
for n, En in enumerate(E, 1):
    print(f"studnia n = {n}: numerycznie {En:.4f} eV, wzór {n**2*(2*np.pi*hbar)**2/(8*me*L**2)/e:.4f} eV")

w = 1e15                                             # oscylator: ħω ≈ 0,658 eV
xo = np.linspace(-3e-9, 3e-9, 3000)
Eo, psio = poziomy(0.5*me*w**2*xo**2/1.0, xo)
print("oscylator E_n/ħω:", np.round(Eo*e/(hbar*w), 4))
for n in range(3):
    plt.plot(x*1e9, psi[:, n]**2/np.max(psi[:, n]**2) + n, label=f"n = {n + 1}")
plt.xlabel("x [nm]"); plt.ylabel("|ψ|² (przesunięte)"); plt.legend(); plt.show()
```

## Zadania

### A. Poziom maturalny _(opcjonalnie — rozgrzewka)_

1. Ile razy energia trzeciego poziomu w studni jest większa od energii pierwszego? Ile węzłów (wewnątrz studni) ma funkcja falowa trzeciego stanu?

<details>
<summary>Odpowiedź</summary>

9 razy; 2 węzły.
</details>

2. Jak zmieni się energia stanu podstawowego, gdy szerokość studni zmaleje dwukrotnie?

<details>
<summary>Odpowiedź</summary>

Wzrośnie czterokrotnie.
</details>

### B. Poziom akademicki

1. Oblicz $E_1$ dla protonu w studni o szerokości $10^{-14}\ \mathrm m$ (rozmiar jądra) w MeV. Porównaj z energiami w atomie.

<details>
<summary>Odpowiedź</summary>

$E_1 = h^2/(8m_pL^2) \approx 2{,}05\ \mathrm{MeV}$. Energie jądrowe są milion razy większe niż atomowe (eV), stąd moc reakcji jądrowych (22).
</details>

2. Dla elektronu w studni oblicz $\langle x\rangle$ i $\langle x^2\rangle$ w stanie $n$. Pokaż, że dla dużych $n$ $\langle x^2\rangle \to L^2/3$, jak dla klasycznej kulki.

<details>
<summary>Odpowiedź</summary>

$\langle x\rangle = L/2$ z symetrii. $\langle x^2\rangle = \dfrac2L\displaystyle\int_0^Lx^2\sin^2\frac{n\pi x}{L}dx = L^2\left(\frac13 - \frac{1}{2n^2\pi^2}\right) \to \frac{L^2}{3}$.
</details>

3. Cząsteczka CO drga z częstotliwością $6{,}4\cdot10^{13}\ \mathrm{Hz}$. Oblicz odstęp poziomów oscylacyjnych w eV i długość fali fotonu pochłanianego przy przejściu $0 \to 1$. W jakim zakresie widma leży? Dlaczego CO₂ i inne cząsteczki gazów cieplarnianych pochłaniają podczerwień?

<details>
<summary>Odpowiedź</summary>

$\hbar\omega = hf \approx 0{,}26\ \mathrm{eV}$, $\lambda = c/f \approx 4{,}7\ \mu\mathrm m$ (podczerwień). Odstępy poziomów oscylacyjnych cząsteczek odpowiadają fotonom podczerwonym, czyli zakresowi, w którym Ziemia wypromieniowuje ciepło (11.03, 16.04).
</details>

## Źródła

- OpenStax, *Fizyka dla szkół wyższych*, t. 3, rozdz. 7 — §7.3 (równanie Schrödingera), §7.4 (cząstka kwantowa w pudle), §7.5 (oscylator harmoniczny).
- Halliday, Resnick, Walker, *Podstawy fizyki* — wyd. 2015: t. 5, §39.1–39.4; wyd. 1: t. 5, §40.1–40.7.
- Symulacja PhET *Stany związane kwantowe*.
