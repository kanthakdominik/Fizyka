# 11.04 — Gaz doskonały i kinetyczna teoria gazów

> **Moduł:** [11 — Termodynamika i teoria kinetyczna](README.md) · **Poziom:** 🟢🔵 matura R + studia · **Status:** ✅ pełny
>
> **Czytaj:**
>
> - OpenStax, *Fizyka dla szkół wyższych*, t. 2, rozdz. 2: [§2.1–2.4](https://openstax.org/books/fizyka-dla-szk%C3%B3%C5%82-wy%C5%BCszych-tom-2/pages/2-1-model-czasteczkowy-gazu-doskonalego) · [wstęp do rozdziału](https://openstax.org/books/fizyka-dla-szk%C3%B3%C5%82-wy%C5%BCszych-tom-2/pages/2-wstep)
> - Halliday, Resnick, Walker, *Podstawy fizyki*, wyd. 2015, t. 2: §19.1–19.6 (s. 288)
> - Halliday, Resnick, Walker, *Podstawy fizyki*, wyd. 1 (2003), t. 2: [§20.1–20.7, s. 225](https://home.agh.edu.pl/~czapli/Resnick_2.pdf#page=241) — PDF z serwera AGH

← [Przewodnictwo, konwekcja i promieniowanie cieplne](03-transport-ciepla.md) · [spis modułu](README.md) · [I zasada termodynamiki i przemiany gazowe](05-pierwsza-zasada.md) →

## Po co to jest

Równanie stanu gazu doskonałego wiąże ciśnienie, objętość i temperaturę. Działają na nim opony, balony, silniki, prognozy pogody i oddychanie. Teoria kinetyczna wyjaśnia, skąd to prawo się bierze. Ciśnienie to uderzenia cząsteczek o ścianki, a temperatura to średnia energia ich ruchu. To pierwszy przykład fizyki statystycznej: z ruchu $10^{23}$ cząsteczek wynikają proste prawa dla wielkości makroskopowych.

## Teoria w pigułce

**Równanie Clapeyrona** (stanu gazu doskonałego):

$$pV = nRT = NkT,$$

- $n$ — liczba moli, $R = 8{,}314\ \mathrm{J/(mol\cdot K)}$;
- $N$ — liczba cząsteczek, $k = R/N_A = 1{,}381\cdot10^{-23}\ \mathrm{J/K}$ (stała Boltzmanna).

Szczególne przypadki to prawa Boyle'a–Mariotte'a ($T$ = const), Gay-Lussaca ($p$ = const) i Charles'a ($V$ = const). Gaz rzeczywisty zachowuje się jak doskonały przy małej gęstości i temperaturze daleko od skraplania. W warunkach normalnych (0°C, 1013 hPa) mol gazu zajmuje 22,4 L.

**Model kinetyczny.** Gaz to ogromna liczba punktowych cząsteczek w chaotycznym ruchu, zderzających się sprężyście. Cząsteczka o masie $m$ odbija się od ścianki i przekazuje jej pęd $2mv_x$. Sumując po wszystkich cząsteczkach i uśredniając po kierunkach ($\overline{v_x^2} = \overline{v^2}/3$):

$$p = \frac13\frac{N}{V}m\overline{v^2}.$$

Porównując z $pV = NkT$, otrzymujemy związek temperatury z energią:

$$\overline{E_k} = \tfrac12m\overline{v^2} = \tfrac32kT, \qquad v_{\text{śr.kw.}} = \sqrt{\overline{v^2}} = \sqrt{\frac{3kT}{m}} = \sqrt{\frac{3RT}{M}}.$$

Temperatura bezwzględna jest miarą średniej energii kinetycznej ruchu postępowego. Ta energia nie zależy od rodzaju gazu. W tej samej temperaturze lżejsze cząsteczki poruszają się szybciej.

**Zasada ekwipartycji energii.** Na każdy stopień swobody, w którym energia jest kwadratowa, przypada średnio $\tfrac12kT$.
- Gaz jednoatomowy ma 3 stopnie swobody (ruch postępowy), więc $U = \tfrac32nRT$.
- Gaz dwuatomowy w temperaturze pokojowej ma dodatkowo 2 stopnie obrotowe, więc $U = \tfrac52nRT$.
- Drgania cząsteczek włączają się dopiero w wysokich temperaturach. To efekt kwantowy (20).

**Rozkład Maxwella.** Cząsteczki mają różne prędkości. Ułamek cząsteczek o prędkościach w przedziale $(v, v + dv)$ wynosi $f(v)\,dv$:

$$f(v) = 4\pi\left(\frac{m}{2\pi kT}\right)^{3/2}v^2e^{-mv^2/(2kT)}.$$

Wynikają z niego trzy charakterystyczne prędkości:
- najbardziej prawdopodobna $v_p = \sqrt{2kT/m}$;
- średnia $\bar v = \sqrt{8kT/(\pi m)}$;
- średnia kwadratowa $v_{\text{śr.kw.}} = \sqrt{3kT/m}$.

Zachodzi $v_p < \bar v < v_{\text{śr.kw.}}$.

**Średnia droga swobodna** to średnia odległość między zderzeniami: $\lambda = \dfrac{kT}{\sqrt2\pi d^2p}$, gdzie $d$ to średnica cząsteczki. W powietrzu w warunkach normalnych wynosi ok. 70 nm.

## Wzory i założenia

| Wzór | Znaczenie | Kiedy obowiązuje |
|---|---|---|
| $pV = nRT = NkT$ | równanie stanu | gaz doskonały, $T$ w kelwinach |
| $p = \tfrac13(N/V)m\overline{v^2}$ | ciśnienie z teorii kinetycznej | j.w. |
| $\overline{E_k} = \tfrac32kT$ | energia ruchu postępowego | każdy gaz doskonały |
| $v_{\text{śr.kw.}} = \sqrt{3RT/M}$ | prędkość średnia kwadratowa | $M$ w kg/mol |
| $U = \tfrac f2nRT$ | energia wewnętrzna | $f$ = 3 (jednoatomowy), 5 (dwuatomowy) |
| $v_p : \bar v : v_{\text{śr.kw.}} = \sqrt2 : \sqrt{8/\pi} : \sqrt3$ | prędkości z rozkładu Maxwella | — |

## Przykład rozwiązany

**Zadanie.** Oblicz średnią energię kinetyczną cząsteczki gazu w temperaturze 300 K, a także prędkość średnią kwadratową azotu ($M = 28\ \mathrm{g/mol}$) i wodoru ($M = 2\ \mathrm{g/mol}$). Ile cząsteczek zawiera 1 m³ gazu w warunkach normalnych?

$\overline{E_k} = 1{,}5\cdot1{,}381\cdot10^{-23}\cdot300 \approx 6{,}2\cdot10^{-21}\ \mathrm J$, ok. 0,04 eV.

$v_{N_2} = \sqrt{3\cdot8{,}314\cdot300/0{,}028} \approx 517\ \mathrm{m/s}$, $v_{H_2} \approx 1930\ \mathrm{m/s}$. Wodór jest $\sqrt{14} \approx 3{,}7$ razy szybszy.

$N/V = p/(kT) = 101\,325/(1{,}381\cdot10^{-23}\cdot273{,}15) \approx 2{,}69\cdot10^{25}\ \mathrm{m^{-3}}$ (liczba Loschmidta).

### Wersja z rachunkiem różniczkowym i całkowym

**Zadanie.** Z rozkładu Maxwella wyprowadź prędkość najbardziej prawdopodobną i sprawdź numerycznie normalizację oraz $\bar v$ i $v_{\text{śr.kw.}}$ dla azotu w 300 K.

Maksimum $f(v)$: $\dfrac{d}{dv}\left(v^2e^{-av^2}\right) = (2v - 2av^3)e^{-av^2} = 0$, gdzie $a = m/(2kT)$. Stąd $v_p = 1/\sqrt a = \sqrt{2kT/m} \approx 422\ \mathrm{m/s}$.

Całki $\int_0^\infty f\,dv = 1$, $\bar v = \int_0^\infty vf\,dv \approx 476\ \mathrm{m/s}$ i $\sqrt{\int_0^\infty v^2f\,dv} \approx 517\ \mathrm{m/s}$ liczy kod poniżej. Analitycznie wychodzą z całek gaussowskich $\int_0^\infty v^{2n}e^{-av^2}dv$.

## Typowe pułapki

- **Temperatura w stopniach Celsjusza.** We wszystkich wzorach gazowych $T$ musi być w kelwinach.
- **Ciśnienie manometryczne.** Manometr w oponie pokazuje nadwyżkę nad atmosferycznym. W równaniu stanu trzeba użyć ciśnienia bezwzględnego.
- **$M$ w g/mol.** We wzorze $\sqrt{3RT/M}$ masa molowa musi być w kg/mol.
- **Wszystkie cząsteczki mają prędkość $v_{\text{śr.kw.}}$.** To jedna z charakterystyk szerokiego rozkładu.
- **Energia wewnętrzna zależy od rodzaju gazu tylko przez masę.** Zależy od liczby stopni swobody, a nie od masy cząsteczki.

## Doświadczenie / symulacja

**Symulacja PhET:** *Właściwości gazu* (*Gas Properties*) — pompuj cząsteczki do pojemnika, zmieniaj temperaturę i objętość, obserwuj ciśnienie i histogram prędkości. Sprawdź prawo Boyle'a–Mariotte'a i porównaj rozkład prędkości lekkich i ciężkich cząsteczek ([phet.colorado.edu/pl](https://phet.colorado.edu/pl/)).

**Prawo Boyle'a–Mariotte'a strzykawką.** Zatkaj wylot strzykawki i dociskaj tłok ciężarkami (lub wagą łazienkową). Mierz objętość. Ciśnienie to atmosferyczne plus siła przez pole tłoka. Wykres $p$ od $1/V$ powinien być prostą przechodzącą przez zero.

**Python:** rozkład Maxwella dla trzech gazów i sprawdzenie całek.

```python
import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import quad

k, NA = 1.380649e-23, 6.02214076e23

def maxwell(v, M, T):
    m = M/NA
    return 4*np.pi*(m/(2*np.pi*k*T))**1.5*v**2*np.exp(-m*v**2/(2*k*T))

T = 300
for name, M in (("H2", 0.002), ("N2", 0.028), ("CO2", 0.044)):
    norm = quad(maxwell, 0, np.inf, args=(M, T))[0]
    vmean = quad(lambda v: v*maxwell(v, M, T), 0, np.inf)[0]
    vrms = np.sqrt(quad(lambda v: v**2*maxwell(v, M, T), 0, np.inf)[0])
    vp = np.sqrt(2*k*T/(M/NA))
    print(f"{name:4s} całka = {norm:.4f}, v_p = {vp:5.0f}, v_śr = {vmean:5.0f}, v_śr.kw = {vrms:5.0f} m/s")
    v = np.linspace(0, 4000, 800)
    plt.plot(v, maxwell(v, M, T), label=name)
plt.xlabel("v [m/s]"); plt.ylabel("f(v) [s/m]"); plt.title("rozkład Maxwella, 300 K"); plt.legend(); plt.grid(True); plt.show()
```

## Zadania

### A. Poziom maturalny

1. W oponie przy 20°C manometr wskazuje $2{,}2\cdot10^5\ \mathrm{Pa}$ (nadciśnienie). Co pokaże po nagrzaniu opony do 40°C? Przyjmij stałą objętość i ciśnienie atmosferyczne 101 kPa.

<details>
<summary>Odpowiedź</summary>

Ciśnienie bezwzględne $3{,}21\cdot10^5\cdot313/293 \approx 3{,}43\cdot10^5\ \mathrm{Pa}$, więc manometr pokaże ok. $2{,}42\cdot10^5\ \mathrm{Pa}$. Błędne przeskalowanie samego nadciśnienia dałoby $2{,}35\cdot10^5$.
</details>

2. Ile moli i ile kilogramów powietrza ($M = 29\ \mathrm{g/mol}$) jest w pokoju o wymiarach 5 m × 4 m × 2,5 m w 20°C przy ciśnieniu 1013 hPa?

<details>
<summary>Odpowiedź</summary>

$n = pV/(RT) \approx 2080\ \mathrm{mol}$, $m \approx 60\ \mathrm{kg}$.
</details>

3. Ile razy wzrośnie prędkość średnia kwadratowa cząsteczek, gdy temperatura bezwzględna wzrośnie czterokrotnie?

<details>
<summary>Odpowiedź</summary>

Dwukrotnie.
</details>

4. Pęcherzyk powietrza o objętości 1 cm³ wypływa z dna jeziora o głębokości 20 m na powierzchnię. Ile wynosi jego objętość przy powierzchni? Przyjmij stałą temperaturę.

<details>
<summary>Odpowiedź</summary>

Na dnie ciśnienie wynosi ok. $101 + 196 = 297\ \mathrm{kPa}$, więc $V \approx 2{,}9\ \mathrm{cm^3}$.
</details>

### B. Poziom akademicki

1. Oblicz średnią drogę swobodną cząsteczek powietrza w 20°C i 1013 hPa, przyjmując średnicę cząsteczki 0,37 nm. Ile zderzeń na sekundę przeżywa cząsteczka ($\bar v \approx 460\ \mathrm{m/s}$)?

<details>
<summary>Odpowiedź</summary>

$\lambda = kT/(\sqrt2\pi d^2p) \approx 66\ \mathrm{nm}$, czyli ok. 200 razy więcej niż rozmiar cząsteczki. Liczba zderzeń $\bar v/\lambda \approx 7\cdot10^9\ \mathrm{s^{-1}}$.
</details>

2. Wyprowadź wzór $p = \tfrac13(N/V)m\overline{v^2}$, rozważając sześcian o boku $L$ i cząsteczkę odbijającą się od ścianki prostopadłej do osi $x$.

<details>
<summary>Odpowiedź</summary>

Cząsteczka uderza w ściankę co $2L/v_x$ i za każdym razem przekazuje pęd $2mv_x$, więc średnia siła wynosi $mv_x^2/L$. Suma po $N$ cząsteczkach daje $F = Nm\overline{v_x^2}/L$, a $p = F/L^2 = (N/V)m\overline{v_x^2}$. Izotropia daje $\overline{v_x^2} = \overline{v^2}/3$.
</details>

3. W górnej atmosferze (ok. 1000 K) prędkość średnia kwadratowa wodoru H₂ wynosi ok. 3,5 km/s, a prędkość ucieczki z Ziemi 11,2 km/s. Dlaczego Ziemia mimo to straciła prawie cały wodór, a zatrzymała azot? Oblicz, jaka część cząsteczek H₂ i N₂ ma prędkość większą od prędkości ucieczki. Ułamek cząsteczek szybszych niż $xv_p$ wynosi $\operatorname{erfc}(x) + \dfrac{2x}{\sqrt\pi}e^{-x^2}$.

<details>
<summary>Odpowiedź</summary>

Ucieka „ogon” rozkładu Maxwella. Dla H₂: $v_p \approx 2{,}9\ \mathrm{km/s}$, prędkość ucieczki to ok. $3{,}9v_p$, a ułamek wynosi ok. $10^{-6}$. Cząsteczki ze zderzeń stale uzupełniają ogon, więc przez miliardy lat wodór ucieka. Dla N₂: $v_p \approx 0{,}77\ \mathrm{km/s}$, prędkość ucieczki to ok. $14{,}5v_p$, a ułamek jest rzędu $10^{-91}$, czyli zaniedbywalny.
</details>

4. Pokaż, że dla gazu dwuatomowego w temperaturze pokojowej $C_V = \tfrac52R$, i oblicz energię wewnętrzną 1 mola powietrza w 300 K.

<details>
<summary>Odpowiedź</summary>

3 stopnie postępowe i 2 obrotowe dają $U = \tfrac52nRT$, więc $C_V = dU/dT$ na mol wynosi $\tfrac52R$. $U \approx 2{,}5\cdot8{,}314\cdot300 \approx 6{,}2\ \mathrm{kJ}$.
</details>

## Źródła

- OpenStax, *Fizyka dla szkół wyższych*, t. 2, rozdz. 2 — §2.1 (model cząsteczkowy gazu doskonałego), §2.2 (ciśnienie, temperatura i prędkość średnia kwadratowa), §2.3 (pojemność cieplna i ekwipartycja), §2.4 (rozkład Maxwella).
- Halliday, Resnick, Walker, *Podstawy fizyki* — wyd. 2015: t. 2, §19.1–19.6; wyd. 1: t. 2, §20.1–20.7.
- Symulacja PhET *Właściwości gazu*.
