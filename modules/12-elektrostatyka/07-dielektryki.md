# 12.07 — Dielektryki w polu elektrycznym

> **Moduł:** [12 — Elektrostatyka](README.md) · **Poziom:** 🟢🔵 matura R + studia · **Status:** ✅ pełny
>
> **Czytaj:**
>
> - OpenStax, *Fizyka dla szkół wyższych*, t. 2, rozdz. 8: [§8.4–8.5](https://openstax.org/books/fizyka-dla-szk%C3%B3%C5%82-wy%C5%BCszych-tom-2/pages/8-4-kondensator-z-dielektrykiem) · [wstęp do rozdziału](https://openstax.org/books/fizyka-dla-szk%C3%B3%C5%82-wy%C5%BCszych-tom-2/pages/8-wstep)
> - Halliday, Resnick, Walker, *Podstawy fizyki*, wyd. 2015, t. 3: §25.5–25.6 (s. 160)
> - Halliday, Resnick, Walker, *Podstawy fizyki*, wyd. 1 (2003), t. 3: [§26.6–26.8, s. 115](https://home.agh.edu.pl/~czapli/Resnick_3.pdf#page=125) — PDF z serwera AGH

← [Kondensatory: pojemność, łączenie, energia](06-kondensatory.md) · [spis modułu](README.md) · (koniec modułu) →

## Po co to jest

Izolator włożony między okładki kondensatora zwiększa jego pojemność nawet tysiące razy. Dzięki temu mieści się ona w małej obudowie, a izolator chroni przed przebiciem. Dielektryki wyjaśniają, dlaczego woda tak dobrze rozpuszcza sole (osłabia przyciąganie jonów 80 razy), jak działa kuchenka mikrofalowa i jak błona komórkowa utrzymuje napięcie potrzebne do przewodzenia impulsów nerwowych. Przenikalność elektryczna i wytrzymałość na przebicie to podstawowe parametry materiałów w elektrotechnice.

## Teoria w pigułce

**Polaryzacja dielektryka.** W izolatorze ładunki nie mogą płynąć, ale mogą się nieco przesunąć:
- w cząsteczkach niepolarnych pole rozsuwa chmurę elektronową względem jąder (**polaryzacja indukowana**);
- trwałe dipole, np. $\mathrm{H_2O}$, ustawiają się częściowo wzdłuż pola (**polaryzacja orientacyjna**), co zaburzają ruchy cieplne.

W efekcie na powierzchniach dielektryka pojawiają się **ładunki związane** przeciwnego znaku niż na sąsiednich okładkach. Ich pole osłabia pole wewnątrz.

**Przenikalność względna** $\varepsilon_r$ (stała dielektryczna) mówi, ile razy dielektryk osłabia pole przy tym samym ładunku swobodnym:

$$E = \frac{E_0}{\varepsilon_r}, \qquad C = \varepsilon_rC_0 = \frac{\varepsilon_r\varepsilon_0A}{d}.$$

Przykładowe wartości:

| Materiał | $\varepsilon_r$ | Wytrzymałość na przebicie |
|---|---|---|
| powietrze | 1,0006 | ok. 3 MV/m |
| papier | ok. 3,5 | ok. 15 MV/m |
| szkło | 5–10 | ok. 10 MV/m |
| woda | ok. 80 | — |
| ceramika tytanianowa | do kilku tysięcy | — |

Powyżej wytrzymałości na przebicie dielektryk zaczyna przewodzić. Tak powstaje iskra albo przebicie kondensatora.

**Ładunek związany na powierzchni** wynosi $\sigma_b = \sigma\left(1 - \dfrac{1}{\varepsilon_r}\right)$. W wodzie prawo Coulomba dla jonów ma postać $F = \dfrac{kq_1q_2}{\varepsilon_rr^2}$, a siła jest 80 razy słabsza, więc kryształy soli łatwo się rozpadają.

**Wkładanie dielektryka do kondensatora:**

| Wielkość | Odłączony od źródła ($Q$ stałe) | Podłączony do źródła ($U$ stałe) |
|---|---|---|
| $C$ | rośnie $\varepsilon_r$ razy | rośnie $\varepsilon_r$ razy |
| $Q$ | bez zmian | rośnie $\varepsilon_r$ razy |
| $U$ | maleje $\varepsilon_r$ razy | bez zmian |
| $E$ | maleje $\varepsilon_r$ razy | bez zmian |
| $W$ | maleje $\varepsilon_r$ razy (dielektryk jest wciągany) | rośnie $\varepsilon_r$ razy (energię dostarcza źródło) |

**Prawo Gaussa w dielektryku** można pisać tylko z ładunkiem swobodnym, jeśli użyje się wektora **indukcji elektrycznej** $\vec D = \varepsilon_r\varepsilon_0\vec E$: $\oint\vec D\cdot d\vec A = Q_{\text{swob}}$.

## Wzory i założenia

| Wzór | Znaczenie | Kiedy obowiązuje |
|---|---|---|
| $C = \varepsilon_rC_0$ | kondensator wypełniony dielektrykiem | dielektryk wypełnia całą przestrzeń |
| $E = E_0/\varepsilon_r$ | osłabienie pola | stały ładunek swobodny |
| $\sigma_b = \sigma(1 - 1/\varepsilon_r)$ | ładunek związany | dielektryk liniowy |
| $w = \tfrac12\varepsilon_r\varepsilon_0E^2$ | gęstość energii | — |
| $\oint\vec D\cdot d\vec A = Q_{\text{swob}}$, $\ \vec D = \varepsilon_r\varepsilon_0\vec E$ | prawo Gaussa w dielektryku | dielektryk liniowy, izotropowy |

## Przykład rozwiązany

**Zadanie.** Kondensator z 12.06 (88,5 pF) naładowano do 100 V i odłączono. Między okładki wsunięto szkło o $\varepsilon_r = 5$, wypełniające całą przestrzeń. Oblicz nowe napięcie, energię i gęstość ładunku związanego.

$C = 5\cdot88{,}5 \approx 443\ \mathrm{pF}$. $Q = 8{,}85\ \mathrm{nC}$ bez zmian, więc $U = Q/C = 20\ \mathrm V$.

Energia: z $0{,}44\ \mu\mathrm J$ do $0{,}089\ \mu\mathrm J$. Różnicę dostało szkło jako pracę wciągania.

$\sigma = Q/A = 8{,}85\cdot10^{-7}\ \mathrm{C/m^2}$, $\sigma_b = 0{,}8\sigma \approx 7{,}1\cdot10^{-7}\ \mathrm{C/m^2}$. Pole wewnątrz: $(\sigma - \sigma_b)/\varepsilon_0 = 2\cdot10^4\ \mathrm{V/m} = U/d$, zgodnie z oczekiwaniem.

### Wersja z rachunkiem różniczkowym i całkowym

**Zadanie.** Między okładki kondensatora płaskiego (pole $A$, odległość $d$) wsunięto płytkę dielektryka o grubości $t < d$ i przenikalności $\varepsilon_r$, równoległą do okładek. Wyprowadź pojemność.

Przy ładunku $Q$ w szczelinach powietrznych (łącznie $d - t$) pole wynosi $E_0 = Q/(\varepsilon_0A)$, a w dielektryku $E_0/\varepsilon_r$. Napięcie to całka pola wzdłuż odstępu:

$$U = \int_0^dE\,dx = E_0(d - t) + \frac{E_0}{\varepsilon_r}t \quad\Rightarrow\quad C = \frac{\varepsilon_0A}{d - t + t/\varepsilon_r}.$$

To dwa kondensatory połączone szeregowo. Wynik nie zależy od położenia płytki. Dla $t = d$ wychodzi $\varepsilon_rC_0$, a płytka metalowa ($\varepsilon_r \to \infty$) działa jak zmniejszenie odstępu do $d - t$.

## Typowe pułapki

- **Dielektryk zawsze zmniejsza energię.** Tylko w kondensatorze odłączonym. W podłączonym energia rośnie kosztem źródła.
- **W dielektryku płynie prąd.** Ładunki tylko się przesuwają i nie płyną. Prąd w izolatorze to przebicie.
- **$\varepsilon_r$ dla przewodnika.** Metal w polu statycznym zachowuje się jak $\varepsilon_r \to \infty$: pole wewnątrz jest zerowe.
- **Wzór $\varepsilon_rC_0$ dla częściowo wypełnionego kondensatora.** Wtedy trzeba policzyć układ szeregowy lub równoległy (zadanie B).
- **Woda zawsze ma $\varepsilon_r = 80$.** To wartość statyczna. Przy częstotliwościach światła $\varepsilon_r$ wody wynosi ok. 1,8, bo dipole nie nadążają za polem.

## Doświadczenie / symulacja

**Pojemność a przekładka.** Kondensator z folii aluminiowej (12.06) zmierz miernikiem z przekładką z kartki, folii spożywczej, szkła z ramki do zdjęć i bez przekładki (z dystansami). Wyznacz $\varepsilon_r$ materiałów jako stosunek pojemności przy tej samej odległości.

**Strumień wody i balon.** Zbliż naelektryzowany balon do cienkiego strumienia wody z kranu. Strumień się odgina, bo cząsteczki wody to dipole wciągane w obszar silniejszego pola.

**Symulacja PhET:** *Laboratorium kondensatora* (*Capacitor Lab*) — zakładka *Dielektryk*: wsuwaj dielektryk przy odłączonej i podłączonej baterii, obserwuj ładunek, napięcie i energię.

**Python:** pojemność i energia przy częściowym wsuwaniu dielektryka (dwa kondensatory równolegle).

```python
import numpy as np
import matplotlib.pyplot as plt

eps0, eps_r = 8.854e-12, 5.0
a, d, U0 = 0.1, 1e-3, 100.0                     # kwadrat 10 cm, 1 mm
C0 = eps0*a*a/d
Q = C0*U0                                       # odłączony: stały ładunek
x = np.linspace(0, a, 200)                      # długość wsuniętej części
C = eps0*a*(eps_r*x + (a - x))/d                 # równolegle: część z dielektrykiem + powietrze
W_Q = Q**2/(2*C)                                # stały ładunek
W_U = 0.5*C*U0**2                               # stałe napięcie
F = -np.gradient(W_Q, x)                        # siła wciągająca przy stałym Q
print(f"C0 = {C0*1e12:.1f} pF, C po wsunięciu = {C[-1]*1e12:.1f} pF")
print(f"odłączony: U = {Q/C[-1]:.1f} V, W: {W_Q[0]*1e6:.3f} → {W_Q[-1]*1e6:.3f} µJ")
print(f"podłączony: W: {W_U[0]*1e6:.3f} → {W_U[-1]*1e6:.3f} µJ")
print(f"siła wciągania na początku (stałe Q): {F[1]*1e6:.2f} µN")
plt.plot(x*100, W_Q*1e6, label="odłączony (Q = const)"); plt.plot(x*100, W_U*1e6, label="podłączony (U = const)")
plt.xlabel("wsunięcie [cm]"); plt.ylabel("W [µJ]"); plt.grid(True); plt.legend(); plt.show()
```

## Zadania

### A. Poziom maturalny

1. Kondensator powietrzny o pojemności 100 pF wypełniono papierem o $\varepsilon_r = 3{,}5$. Jaka jest nowa pojemność? Jakie najwyższe napięcie wytrzyma, jeśli grubość papieru to 0,1 mm, a wytrzymałość 15 MV/m?

<details>
<summary>Odpowiedź</summary>

350 pF; $U_{\max} = E_{\max}d = 1500\ \mathrm V$.
</details>

2. Kondensator podłączony do baterii wypełniono dielektrykiem o $\varepsilon_r = 4$. Jak zmieniły się napięcie, ładunek i energia?

<details>
<summary>Odpowiedź</summary>

Napięcie bez zmian; ładunek i energia wzrosły 4 razy.
</details>

3. Dlaczego sól kuchenna rozpuszcza się w wodzie, a w benzynie nie?

<details>
<summary>Odpowiedź</summary>

Woda ma $\varepsilon_r \approx 80$ i osłabia przyciąganie jonów $\mathrm{Na^+}$ i $\mathrm{Cl^-}$ 80 razy, a jej dipole otaczają jony. Benzyna ma $\varepsilon_r \approx 2$.
</details>

### B. Poziom akademicki

1. Błona komórkowa ma grubość ok. 8 nm i $\varepsilon_r \approx 7$. Oblicz pojemność na cm² i natężenie pola przy napięciu spoczynkowym 70 mV. Porównaj z wytrzymałością powietrza.

<details>
<summary>Odpowiedź</summary>

$C/A = \varepsilon_r\varepsilon_0/d \approx 7{,}7\cdot10^{-3}\ \mathrm{F/m^2} \approx 0{,}8\ \mu\mathrm F/\mathrm{cm^2}$ (zmierzone: ok. 1 μF/cm²). $E = 0{,}07/8\cdot10^{-9} \approx 9\cdot10^6\ \mathrm{V/m}$, trzy razy więcej, niż wytrzymuje powietrze.
</details>

2. Kondensator płaski wypełniono w połowie **powierzchni** dielektrykiem o $\varepsilon_r$ (dielektryk sięga od okładki do okładki). Oblicz pojemność.

<details>
<summary>Odpowiedź</summary>

Dwa kondensatory równolegle: $C = \dfrac{\varepsilon_0(A/2)}{d}(1 + \varepsilon_r) = C_0\dfrac{1 + \varepsilon_r}{2}$.
</details>

3. Kondensator odłączony od źródła ma ładunek $Q$. Płyta dielektryka o szerokości $a$ jest wsunięta na długość $x$ (okładki kwadratowe o boku $a$). Pokaż, że siła wciągająca płytę wynosi $F = \dfrac{Q^2(\varepsilon_r - 1)d}{2\varepsilon_0a[\varepsilon_rx + (a - x)]^2}$.

<details>
<summary>Odpowiedź</summary>

$C(x) = \dfrac{\varepsilon_0a}{d}[\varepsilon_rx + (a - x)]$, $W = Q^2/(2C)$, $F = -\dfrac{dW}{dx} = \dfrac{Q^2}{2C^2}\dfrac{dC}{dx}$, a $\dfrac{dC}{dx} = \dfrac{\varepsilon_0a(\varepsilon_r - 1)}{d}$. Siła wciąga płytę.
</details>

## Źródła

- OpenStax, *Fizyka dla szkół wyższych*, t. 2, rozdz. 8 — §8.4 (kondensator z dielektrykiem) i §8.5 (molekularny model dielektryka).
- Halliday, Resnick, Walker, *Podstawy fizyki* — wyd. 2015: t. 3, §25.5–25.6; wyd. 1: t. 3, §26.6–26.8.
- Symulacja PhET *Laboratorium kondensatora*.
