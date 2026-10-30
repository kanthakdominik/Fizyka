# 12.04 — Strumień pola i prawo Gaussa

> **Moduł:** [12 — Elektrostatyka](README.md) · **Poziom:** 🔵 studia · **Status:** ✅ pełny
>
> **Czytaj:**
>
> - OpenStax, *Fizyka dla szkół wyższych*, t. 2, rozdz. 6: [§6.1–6.4](https://openstax.org/books/fizyka-dla-szk%C3%B3%C5%82-wy%C5%BCszych-tom-2/pages/6-1-strumien-pola-elektrycznego) · [wstęp do rozdziału](https://openstax.org/books/fizyka-dla-szk%C3%B3%C5%82-wy%C5%BCszych-tom-2/pages/6-wstep)
> - Halliday, Resnick, Walker, *Podstawy fizyki*, wyd. 2015, t. 3: §23.1–23.6 (s. 67)
> - Halliday, Resnick, Walker, *Podstawy fizyki*, wyd. 1 (2003), t. 3: [§24.1–24.9, s. 47](https://home.agh.edu.pl/~czapli/Resnick_3.pdf#page=57) — PDF z serwera AGH

← [Pole rozkładów ciągłych ładunku](03-pole-rozkladow-ciaglych.md) · [spis modułu](README.md) · [Potencjał, energia potencjalna i związek E z V](05-potencjal.md) →

## Po co to jest

Prawo Gaussa to drugi, równoważny prawu Coulomba sposób opisu pola, ale znacznie potężniejszy. Gdy rozkład ładunku jest symetryczny, pole wylicza się w kilku linijkach zamiast mozolnego całkowania. Z niego wynika, że ładunek przewodnika zbiera się na powierzchni, że wnętrze metalowej klatki jest osłonięte od pól (klatka Faradaya, kabel koncentryczny, samochód w burzy) i że piorunochron działa dzięki ostrzu. To pierwsze z czterech równań Maxwella (16).

## Teoria w pigułce

**Strumień pola elektrycznego** przez powierzchnię mierzy, „ile linii pola” przez nią przechodzi:

$$\Phi_E = \int\vec E\cdot d\vec A, \qquad \text{dla pola jednorodnego i płaskiej powierzchni} \quad \Phi_E = EA\cos\theta.$$

Wektor $d\vec A$ jest prostopadły do powierzchni. Dla powierzchni zamkniętej wskazuje na zewnątrz.

**Prawo Gaussa.** Strumień przez dowolną zamkniętą powierzchnię jest proporcjonalny do ładunku zamkniętego wewnątrz:

$$\oint\vec E\cdot d\vec A = \frac{Q_{\text{wewn}}}{\varepsilon_0}.$$

Ładunki na zewnątrz nie dają strumienia wypadkowego: ile linii wchodzi, tyle wychodzi. Pole $\vec E$ we wzorze to jednak pole od **wszystkich** ładunków.

**Jak liczyć pole.** Wybierz powierzchnię Gaussa zgodną z symetrią, tak żeby na jej częściach $E$ było stałe i równoległe do $d\vec A$, albo do niej prostopadłe:

| Symetria | Powierzchnia | Wynik |
|---|---|---|
| kulista (ładunek $Q$) | sfera o promieniu $r$ | $E\cdot4\pi r^2 = Q_{\text{wewn}}/\varepsilon_0$; na zewnątrz $E = kQ/r^2$ |
| kula jednorodna, wewnątrz | sfera $r < R$ | $E = kQr/R^3$, rośnie liniowo |
| powłoka kulista, wewnątrz | sfera $r < R$ | $E = 0$ |
| walcowa (nić $\lambda$) | walec o promieniu $r$ | $E\cdot2\pi rL = \lambda L/\varepsilon_0 \Rightarrow E = \lambda/(2\pi\varepsilon_0r)$ |
| płaska (płaszczyzna $\sigma$) | „pudełko” przecinające płaszczyznę | $2EA = \sigma A/\varepsilon_0 \Rightarrow E = \sigma/(2\varepsilon_0)$ |

**Przewodnik w równowadze elektrostatycznej:**
- wewnątrz przewodnika $E = 0$, bo inaczej swobodne elektrony by się poruszały;
- cały nadmiarowy ładunek siedzi na powierzchni;
- pole tuż przy powierzchni jest do niej prostopadłe i wynosi $E = \sigma/\varepsilon_0$;
- we wnęce przewodnika bez ładunków pole jest zerowe (**klatka Faradaya**);
- ładunek gromadzi się najgęściej na ostrzach (mały promień krzywizny), gdzie pole jest największe. Na tym opiera się piorunochron i ulot z ostrzy.

## Wzory i założenia

| Wzór | Znaczenie | Kiedy obowiązuje |
|---|---|---|
| $\Phi_E = \int\vec E\cdot d\vec A$ | strumień pola | — |
| $\oint\vec E\cdot d\vec A = Q_{\text{wewn}}/\varepsilon_0$ | prawo Gaussa | zawsze; do liczenia $E$ — przy symetrii |
| $E = kQ/r^2$ (na zewnątrz), $kQr/R^3$ (wewnątrz) | kula jednorodna | symetria kulista |
| $E = \sigma/\varepsilon_0$ | tuż przy powierzchni przewodnika | równowaga elektrostatyczna |
| $E = 0$ | wnętrze przewodnika | j.w. |

## Przykład rozwiązany

**Zadanie 1.** Ładunek $1\ \mu\mathrm C$ jest rozłożony równomiernie w objętości kuli o promieniu 10 cm. Oblicz pole w odległości 5 cm, 10 cm i 20 cm od środka.

Wewnątrz: $E = kQr/R^3 = 8{,}99\cdot10^9\cdot10^{-6}\cdot0{,}05/10^{-3} \approx 4{,}5\cdot10^5\ \mathrm{N/C}$.

Na powierzchni: $kQ/R^2 \approx 9{,}0\cdot10^5\ \mathrm{N/C}$. W odległości 20 cm: $2{,}25\cdot10^5\ \mathrm{N/C}$.

Gdyby ten sam ładunek był na metalowej kuli, pole w 5 cm wynosiłoby zero.

**Zadanie 2.** Przy powierzchni Ziemi przy pogodzie panuje pole elektryczne ok. 150 N/C skierowane w dół. Oblicz gęstość powierzchniową i całkowity ładunek Ziemi.

$\sigma = -\varepsilon_0E \approx -1{,}3\cdot10^{-9}\ \mathrm{C/m^2}$. $Q = 4\pi R_Z^2\sigma \approx -6{,}8\cdot10^5\ \mathrm C$. Ziemia jest naładowana ujemnie, a ładunek dodatni siedzi w jonosferze. „Kondensator” Ziemia–jonosfera ładują burze.

### Wersja z rachunkiem różniczkowym i całkowym

**Zadanie.** Kula o promieniu $R$ ma gęstość ładunku rosnącą ku powierzchni: $\rho(r) = \rho_0r/R$. Znajdź całkowity ładunek i pole wewnątrz.

Ładunek wewnątrz sfery o promieniu $r$:

$$Q(r) = \int_0^r\rho_0\frac{r'}{R}4\pi r'^2dr' = \frac{\pi\rho_0r^4}{R}, \qquad Q = \pi\rho_0R^3.$$

Z prawa Gaussa: $E\cdot4\pi r^2 = Q(r)/\varepsilon_0 \Rightarrow E = \dfrac{\rho_0r^2}{4\varepsilon_0R} = \dfrac{kQr^2}{R^4}$. Na powierzchni wynik zgadza się z $kQ/R^2$.

## Typowe pułapki

- **Pole we wzorze to pole od ładunku wewnątrz.** $\vec E$ to pole wypadkowe od wszystkich ładunków. Tylko strumień zależy wyłącznie od ładunku wewnętrznego.
- **Prawo Gaussa zawsze daje $E$.** Zawsze jest prawdziwe, ale do obliczenia $E$ nadaje się tylko przy wysokiej symetrii (kula, walec, płaszczyzna).
- **Zerowy strumień = zerowe pole.** Strumień może być zerowy, choć pole na powierzchni nie jest (dipol w środku, ładunek na zewnątrz).
- **Pole przy przewodniku $\sigma/(2\varepsilon_0)$.** Przy powierzchni przewodnika jest $\sigma/\varepsilon_0$, bo wewnątrz pole jest zerowe i cały strumień wychodzi na zewnątrz.
- **Wnętrze przewodnika ma potencjał zero.** Pole jest zerowe, a potencjał stały, ale niekoniecznie zerowy (12.05).

## Doświadczenie / symulacja

**Klatka Faradaya z folii.** Owiń telefon szczelnie folią aluminiową (lub włóż do metalowej puszki z zamykaną pokrywką) i zadzwoń na niego. Zwykle połączenie nie dochodzi, bo fale elektromagnetyczne nie wnikają do zamkniętego przewodnika. Zbadaj, jaka szczelina wystarczy, by sygnał przeszedł.

**Elektroskop i puszka.** Naelektryzowaną kulkę na nitce włóż do metalowej puszki połączonej z elektroskopem i dotknij nią wnętrza. Cały ładunek przechodzi na zewnętrzną powierzchnię puszki (doświadczenie z kubkiem Faradaya).

**Python:** pole kuli jednorodnej i kuli o gęstości $\rho \propto r$ (całkowanie ładunku numerycznie i prawo Gaussa).

```python
import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import quad

eps0 = 8.854e-12
R, Q = 0.1, 1e-6

def E_gauss(r, rho):
    Qw = quad(lambda s: rho(s)*4*np.pi*s**2, 0, min(r, R))[0]
    return Qw/(4*np.pi*eps0*r**2)

rho_jedn = lambda s: Q/(4/3*np.pi*R**3)
rho_lin = lambda s: Q/(np.pi*R**3)*s/R            # ρ0 = Q/(πR³)
for r in (0.05, 0.1, 0.2):
    print(f"r = {r:.2f} m: jednorodna {E_gauss(r, rho_jedn):.3e}, ρ ~ r {E_gauss(r, rho_lin):.3e} N/C")

r = np.linspace(0.002, 0.3, 300)
plt.plot(r*100, [E_gauss(v, rho_jedn) for v in r], label="kula jednorodna")
plt.plot(r*100, [E_gauss(v, rho_lin) for v in r], label="ρ ∝ r")
plt.axvline(R*100, color="gray", ls="--")
plt.xlabel("r [cm]"); plt.ylabel("E [N/C]"); plt.grid(True); plt.legend(); plt.show()
```

## Zadania

### A. Poziom maturalny _(opcjonalnie — rozgrzewka)_

1. Ładunek punktowy $q$ jest w środku sześcianu. Ile wynosi strumień przez całą powierzchnię sześcianu, a ile przez jedną ścianę?

<details>
<summary>Odpowiedź</summary>

$q/\varepsilon_0$ i $q/(6\varepsilon_0)$ z symetrii.
</details>

2. Dlaczego w czasie burzy bezpieczniej jest siedzieć w samochodzie z metalowym nadwoziem niż stać na otwartej przestrzeni?

<details>
<summary>Odpowiedź</summary>

Nadwozie działa jak klatka Faradaya. Prąd pioruna płynie po zewnętrznej powierzchni metalu, a pole wewnątrz pozostaje małe.
</details>

### B. Poziom akademicki

1. Metalowa kula o promieniu 20 cm jest w powietrzu, które ulega przebiciu przy $3\cdot10^6\ \mathrm{V/m}$. Jaki największy ładunek można na niej zgromadzić?

<details>
<summary>Odpowiedź</summary>

$Q = ER^2/k \approx 13\ \mu\mathrm C$.
</details>

2. Kabel koncentryczny: wewnętrzny przewód ma ładunek $+\lambda$ na metr, a zewnętrzny ekran $-\lambda$. Wyznacz pole wewnątrz kabla i na zewnątrz.

<details>
<summary>Odpowiedź</summary>

Między przewodami $E = \lambda/(2\pi\varepsilon_0r)$. Na zewnątrz ładunek wewnątrz powierzchni Gaussa wynosi zero, więc $E = 0$. Kabel nie promieniuje pola na zewnątrz.
</details>

3. Nieskończona płyta o grubości $2a$ ma jednorodną gęstość ładunku $\rho$. Wyznacz $E(x)$ wewnątrz i na zewnątrz ($x$ mierzone od płaszczyzny środkowej).

<details>
<summary>Odpowiedź</summary>

Wewnątrz $E = \rho x/\varepsilon_0$ (liniowo), na zewnątrz $E = \rho a/\varepsilon_0$, czyli jak płaszczyzna o $\sigma = 2\rho a$.
</details>

4. Pokaż, że strumień pola ładunku punktowego przez dowolną sferę z ładunkiem w środku wynosi $q/\varepsilon_0$, niezależnie od promienia. Dlaczego to wymaga prawa $1/r^2$?

<details>
<summary>Odpowiedź</summary>

$\Phi = \dfrac{kq}{r^2}\cdot4\pi r^2 = 4\pi kq = q/\varepsilon_0$. Przy innym wykładniku niż 2 strumień zależałby od promienia i prawo Gaussa by nie obowiązywało.
</details>

## Źródła

- OpenStax, *Fizyka dla szkół wyższych*, t. 2, rozdz. 6 — §6.1 (strumień pola), §6.2 (prawo Gaussa), §6.3 (zastosowania), §6.4 (przewodniki w równowadze elektrostatycznej).
- Halliday, Resnick, Walker, *Podstawy fizyki* — wyd. 2015: t. 3, §23.1–23.6; wyd. 1: t. 3, §24.1–24.9.
