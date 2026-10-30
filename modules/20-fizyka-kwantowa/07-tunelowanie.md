# 20.07 — Tunelowanie przez barierę potencjału

> **Moduł:** [20 — Podstawy fizyki kwantowej](README.md) · **Poziom:** 🔵 studia · **Status:** ✅ pełny
>
> **Czytaj:**
>
> - OpenStax, *Fizyka dla szkół wyższych*, t. 3, rozdz. 7: [§7.6](https://openstax.org/books/fizyka-dla-szk%C3%B3%C5%82-wy%C5%BCszych-tom-3/pages/7-6-tunelowanie-czastek-przez-bariery-potencjalu) · [wstęp do rozdziału](https://openstax.org/books/fizyka-dla-szk%C3%B3%C5%82-wy%C5%BCszych-tom-3/pages/7-wstep)
> - Halliday, Resnick, Walker, *Podstawy fizyki*, wyd. 2015, t. 5: §38.8–38.9 (s. 29)
> - Halliday, Resnick, Walker, *Podstawy fizyki*, wyd. 1 (2003), t. 5: [§39.9, s. 22](https://home.agh.edu.pl/~czapli/Resnick_5.pdf#page=38) — PDF z serwera AGH

← [Równanie Schrödingera: studnia potencjału i oscylator](06-rownanie-schrodingera.md) · [spis modułu](README.md) · (koniec modułu) →

## Po co to jest

Klasyczna piłka, której brakuje energii, nigdy nie przejdzie przez wzgórze. Cząstka kwantowa może przeniknąć przez barierę, choć ma za mało energii, żeby ją pokonać. To tunelowanie. Wyjaśnia rozpad alfa (22) i reakcje syntezy w Słońcu, które bez niego by nie zachodziły. Działa na nim skaningowy mikroskop tunelowy (pierwsze obrazy pojedynczych atomów, Nobel 1986), pamięć flash w każdym pendrivie i dysku SSD, diody tunelowe i złącza Josephsona w kubitach komputerów kwantowych.

## Teoria w pigułce

**Bariera prostokątna.** Cząstka o energii $E$ pada na barierę o wysokości $U > E$ i szerokości $L$. W obszarze bariery równanie Schrödingera (20.06) ma postać $\psi'' = \kappa^2\psi$ z

$$\kappa = \frac{\sqrt{2m(U - E)}}{\hbar}.$$

Rozwiązania nie oscylują, tylko zanikają wykładniczo: $\psi \propto e^{-\kappa x}$. Jeśli bariera jest skończenie gruba, po drugiej stronie zostaje niewielka fala przechodząca.

**Współczynnik przejścia** dla bariery grubej ($\kappa L \gg 1$):

$$T \approx e^{-2\kappa L}.$$

(Dokładniejszy wzór ma przed wykładnikiem czynnik rzędu jedności, $16\dfrac{E}{U}\left(1 - \dfrac EU\right)$.)

**Silna zależność od szerokości i wysokości bariery.** Wykładnik sprawia, że:
- zwiększenie szerokości o 0,1 nm zmniejsza $T$ kilka do kilkunastu razy (dla elektronów i barier kilku eV);
- cięższe cząstki tunelują dużo słabiej (masa pod pierwiastkiem w wykładniku);
- makroskopowe ciała nie tunelują w praktyce nigdy.

**Zastosowania:**
- **Skaningowy mikroskop tunelowy (STM)**: ostrze w odległości ok. 0,5 nm od powierzchni. Prąd tunelowy zmienia się kilkakrotnie przy zmianie odległości o 0,01 nm, co pozwala „wyczuć” pojedyncze atomy.
- **Rozpad alfa**: cząstka alfa jest uwięziona w jądrze przez barierę kulombowską o wysokości ok. 25 MeV, mając energię ok. 4–9 MeV. Okresy połowicznego rozpadu od mikrosekund do miliardów lat wynikają z wykładniczej zależności od energii (prawo Geigera–Nuttalla, 22).
- **Synteza w Słońcu**: protony w temperaturze 15 mln K mają energię ok. 1 keV, a bariera kulombowska wynosi ok. 1 MeV. Bez tunelowania Słońce by nie świeciło.
- **Pamięć flash**: elektrony tunelują przez cienką warstwę tlenku na pływającą bramkę tranzystora i zostają tam uwięzione na lata.

## Wzory i założenia

| Wzór | Znaczenie | Kiedy obowiązuje |
|---|---|---|
| $\kappa = \sqrt{2m(U - E)}/\hbar$ | stała zaniku w barierze | $E < U$ |
| $\psi \propto e^{-\kappa x}$ | zanik w barierze | — |
| $T \approx e^{-2\kappa L}$ | współczynnik przejścia | $\kappa L \gg 1$ |
| $T \approx 16\frac EU(1 - \frac EU)e^{-2\kappa L}$ | dokładniejszy | bariera prostokątna |
| $T \approx \exp\left(-\frac2\hbar\int\sqrt{2m(U(x) - E)}dx\right)$ | bariera dowolnego kształtu (WKB) | wolno zmienne $U$ |

## Przykład rozwiązany

### Wersja z rachunkiem różniczkowym i całkowym

**Zadanie 1.** Elektron o energii 1 eV pada na barierę o wysokości 5 eV i szerokości 0,5 nm. Oblicz współczynnik przejścia. Jak zmieni się dla szerokości 1 nm? A dla protonu przy 0,5 nm?

$\kappa = \sqrt{2\cdot9{,}11\cdot10^{-31}\cdot4\cdot1{,}6\cdot10^{-19}}/1{,}055\cdot10^{-34} \approx 1{,}02\cdot10^{10}\ \mathrm{m^{-1}}$.

$L = 0{,}5\ \mathrm{nm}$: $2\kappa L \approx 10{,}2$, $T \approx e^{-10{,}2} \approx 3{,}5\cdot10^{-5}$ (z czynnikiem przed wykładnikiem ok. $9\cdot10^{-5}$).

$L = 1\ \mathrm{nm}$: $T \approx 1{,}3\cdot10^{-9}$, prawie 30 000 razy mniej.

Proton: $\kappa$ jest $\sqrt{1836} \approx 43$ razy większe, więc $T \approx e^{-440}$, czyli praktycznie zero.

**Zadanie 2.** Mikroskop STM: o ile zmienia się prąd tunelowy przy zmianie odległości ostrza o 0,1 nm (bariera ok. 4 eV)?

$I \propto e^{-2\kappa d}$, a $e^{2\kappa\cdot0{,}1\ \mathrm{nm}} \approx e^{2{,}05} \approx 7{,}8$. Zmiana o 0,01 nm zmienia prąd o ok. 23%, co daje rozdzielczość pionową rzędu pikometrów.

## Typowe pułapki

- **Cząstka „przeskakuje” barierę dzięki pożyczonej energii.** Energia jest zachowana. Fala po prostu nie znika natychmiast w obszarze klasycznie zabronionym.
- **Tunelowanie zależy liniowo od szerokości bariery.** Zależy wykładniczo.
- **Wysoka bariera zawsze zatrzymuje.** Liczy się iloczyn $\kappa L$: wysoka, ale bardzo cienka bariera może być przenikalna.
- **Odbicie zawsze zachodzi tylko dla $E < U$.** Kwantowo cząstka częściowo odbija się też od bariery niższej od swojej energii.

## Doświadczenie / symulacja

**Analogia optyczna: sfrustrowane całkowite wewnętrzne odbicie.** Dwa pryzmaty (lub dwa szklane klocki) zbliżone na odległość ułamka długości fali przepuszczają część światła, choć na granicy szkło–powietrze zachodzi całkowite wewnętrzne odbicie (17.02). Fala zanikająca w szczelinie „tuneluje” do drugiego pryzmatu. Z mikrofalami (λ ≈ 3 cm) i klinami z parafiny pokazuje się to w pracowniach na odległościach centymetrowych.

**Symulacja PhET:** *Tunelowanie kwantowe i paczki falowe* (*Quantum Tunneling and Wave Packets*) — zmieniaj energię, wysokość i szerokość bariery ([phet.colorado.edu/pl](https://phet.colorado.edu/pl/)).

**Python:** współczynnik przejścia przez barierę — wzór dokładny i przybliżenie wykładnicze.

```python
import numpy as np
import matplotlib.pyplot as plt

hbar, me, mp, e = 1.054571817e-34, 9.1093837e-31, 1.67262192e-27, 1.602176634e-19

def T_dokladne(E, U, L, m):
    k = np.sqrt(2*m*(U - E)*e)/hbar
    return 1/(1 + (U**2*np.sinh(k*L)**2)/(4*E*(U - E)))

def T_przybl(E, U, L, m):
    k = np.sqrt(2*m*(U - E)*e)/hbar
    return 16*E/U*(1 - E/U)*np.exp(-2*k*L)

for L in (0.2e-9, 0.5e-9, 1e-9):
    print(f"elektron 1 eV, bariera 5 eV, L = {L*1e9:.1f} nm: T = {T_dokladne(1, 5, L, me):.2e} "
          f"(przybliżenie {T_przybl(1, 5, L, me):.2e}, e^(−2κL) = {np.exp(-2*np.sqrt(2*me*4*e)/hbar*L):.2e})")
print(f"proton, L = 0,5 nm: T ≈ e^{-2*np.sqrt(2*mp*4*e)/hbar*0.5e-9:.0f}")
k = np.sqrt(2*me*4*e)/hbar
print(f"STM: zmiana prądu przy Δd = 0,1 nm: × {np.exp(2*k*0.1e-9):.1f}")

L = np.linspace(0.05e-9, 1.2e-9, 300)
plt.semilogy(L*1e9, T_dokladne(1, 5, L, me))
plt.xlabel("szerokość bariery [nm]"); plt.ylabel("T"); plt.title("elektron 1 eV, bariera 5 eV"); plt.grid(True, which="both"); plt.show()
```

## Zadania

### A. Poziom maturalny _(opcjonalnie — rozgrzewka)_

1. Dlaczego piłka nie przenika przez ścianę, a elektron przez cienką warstwę izolatora tak?

<details>
<summary>Odpowiedź</summary>

Prawdopodobieństwo tunelowania maleje wykładniczo z masą i szerokością bariery. Dla piłki i ściany wykładnik jest astronomicznie duży.
</details>

2. Wymień dwa urządzenia lub zjawiska, które działają dzięki tunelowaniu.

<details>
<summary>Odpowiedź</summary>

Na przykład: mikroskop STM, pamięć flash, rozpad alfa, synteza jądrowa w Słońcu, dioda tunelowa.
</details>

### B. Poziom akademicki

1. Jak zmieni się współczynnik przejścia elektronu (1 eV, bariera 5 eV, 0,5 nm), gdy wysokość bariery wzrośnie do 9 eV?

<details>
<summary>Odpowiedź</summary>

$U - E$ rośnie z 4 do 8 eV, więc $\kappa$ rośnie $\sqrt2$ razy, a $2\kappa L$ z 10,2 do 14,5. $T$ maleje ok. 70 razy, do ok. $5\cdot10^{-7}$.
</details>

2. Przybliżenie WKB dla bariery o dowolnym kształcie: $T \approx \exp\left(-\dfrac2\hbar\displaystyle\int_a^b\sqrt{2m(U(x) - E)}\,dx\right)$. Oblicz $T$ dla bariery trójkątnej $U(x) = U_0(1 - x/L)$ na odcinku $[0, L]$ dla cząstki o energii $E \to 0$.

<details>
<summary>Odpowiedź</summary>

$\displaystyle\int_0^L\sqrt{2mU_0(1 - x/L)}dx = \sqrt{2mU_0}\cdot\frac23L$, więc $T \approx \exp\left(-\frac{4L\sqrt{2mU_0}}{3\hbar}\right)$. To model emisji polowej elektronów z metalu w silnym polu (Fowler–Nordheim).
</details>

3. Pokaż, że w obszarze bariery funkcje $e^{\pm\kappa x}$ spełniają równanie Schrödingera z $\kappa = \sqrt{2m(U - E)}/\hbar$.

<details>
<summary>Odpowiedź</summary>

$\psi'' = \kappa^2\psi$, a równanie daje $-\dfrac{\hbar^2}{2m}\kappa^2\psi + U\psi = E\psi$, czyli $\kappa^2 = 2m(U - E)/\hbar^2$.
</details>

## Źródła

- OpenStax, *Fizyka dla szkół wyższych*, t. 3, rozdz. 7 — §7.6: tunelowanie cząstek kwantowych przez bariery potencjału.
- Halliday, Resnick, Walker, *Podstawy fizyki* — wyd. 2015: t. 5, §38.8–38.9; wyd. 1: t. 5, §39.9.
- Symulacja PhET *Tunelowanie kwantowe i paczki falowe*.
