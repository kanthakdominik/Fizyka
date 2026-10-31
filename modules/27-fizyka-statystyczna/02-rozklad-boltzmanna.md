# 27.02 — Rozkład Boltzmanna i suma statystyczna

> **Moduł:** [27 — Fizyka statystyczna](README.md) · **Poziom:** 🔵 studia · **Status:** ✅ pełny
>
> **Czytaj:**
>
> - OpenStax, *Fizyka dla szkół wyższych*, t. 2, rozdz. 2: [§2.4](https://openstax.org/books/fizyka-dla-szk%C3%B3%C5%82-wy%C5%BCszych-tom-2/pages/2-4-rozklad-predkosci-czasteczek-gazu-doskonalego) · [wstęp do rozdziału](https://openstax.org/books/fizyka-dla-szk%C3%B3%C5%82-wy%C5%BCszych-tom-2/pages/2-wstep)
> - Halliday, Resnick, Walker, *Podstawy fizyki*, wyd. 2015, t. 2: §19.6 (s. 301)
> - Halliday, Resnick, Walker, *Podstawy fizyki*, wyd. 1 (2003), t. 2: [§20.7, s. 236](https://home.agh.edu.pl/~czapli/Resnick_2.pdf#page=252) — PDF z serwera AGH

← [Mikrostany, makrostany i entropia Boltzmanna](01-mikrostany-i-entropia.md) · [spis modułu](README.md) · [Ekwipartycja energii i kwantowe zamrażanie stopni swobody](03-ekwipartycja-i-cieplo-wlasciwe.md) →

## Po co to jest

Czynnik Boltzmanna $e^{-E/kT}$ to najczęściej używany wzór całej fizyki statystycznej. Mówi, jak często układ w temperaturze $T$ znajduje się w stanie o energii $E$. Z niego wynika rozkład prędkości cząsteczek (11.04), spadek ciśnienia z wysokością, szybkość reakcji chemicznych i parowania, obsadzenie poziomów atomowych w gwiazdach (26.01), koncentracja nośników w półprzewodnikach (23.04) i namagnesowanie paramagnetyków (14.07). Wszystko to sprowadza się do porównania energii stanu z energią termiczną $kT$ (ok. 1/40 eV w temperaturze pokojowej).

## Teoria w pigułce

**Układ w kontakcie z termostatem.** Mały układ (np. jedna cząsteczka) wymienia energię z dużym otoczeniem (termostatem) o temperaturze $T$. Prawdopodobieństwo, że układ jest w konkretnym stanie $i$ o energii $E_i$, wynosi

$$P_i = \frac{e^{-E_i/kT}}{Z}, \qquad Z = \sum_ie^{-E_i/kT}.$$

$Z$ to **suma statystyczna** (funkcja podziału), która normalizuje prawdopodobieństwa. Jeśli energia $E$ ma $g$ stanów (poziom zdegenerowany), $P(E) \propto ge^{-E/kT}$.

**Skąd czynnik wykładniczy.** Gdy układ ma energię $E_i$, termostat ma $U - E_i$, a liczba jego mikrostanów to $\Omega_R(U - E_i) = e^{S_R(U - E_i)/k}$. Rozwijając entropię termostatu: $S_R(U - E_i) \approx S_R(U) - E_i\dfrac{\partial S_R}{\partial U} = S_R(U) - \dfrac{E_i}{T}$ (27.01). Stąd $P_i \propto e^{-E_i/kT}$.

**Przykłady:**
- **Wzór barometryczny.** Cząsteczka na wysokości $h$ ma energię potencjalną $mgh$, więc gęstość i ciśnienie atmosfery izotermicznej maleją jak $e^{-mgh/kT} = e^{-h/H}$. Wysokość skali $H = kT/(mg)$ dla azotu w 288 K wynosi 8,7 km (dla tlenu 7,6 km — tlenu ubywa z wysokością nieco szybciej).
- **Rozkład Maxwella** (11.04). Energia kinetyczna $\tfrac12mv^2$ daje rozkład składowej prędkości $\propto e^{-mv_x^2/2kT}$ (rozkład normalny). Uwzględnienie liczby kierunków ($4\pi v^2dv$) daje rozkład wartości prędkości.
- **Układy dwupoziomowe.** Stosunek obsadzeń poziomów różniących się o $\Delta E$: $\dfrac{N_2}{N_1} = \dfrac{g_2}{g_1}e^{-\Delta E/kT}$. W fotosferze Słońca (5772 K) na poziomie $n = 2$ wodoru (10,2 eV powyżej podstawowego) jest tylko $5\cdot10^{-9}$ atomów, a przy 10 000 K — $3\cdot10^{-5}$. Dlatego linie Balmera są silne w gwiazdach typu A (26.01).
- **Paramagnetyzm.** Moment magnetyczny $\mu$ w polu $B$ ma energię $\mp\mu B$. Średnia polaryzacja to $\tanh(\mu B/kT)$, dla małych pól $\approx\mu B/kT$ — **prawo Curie** (namagnesowanie $\propto B/T$). W 1 T i 300 K spolaryzowane jest tylko 0,2% elektronów.
- **Prawo Arrheniusa.** Reakcja wymaga przekroczenia bariery $E_a$; jej szybkość $\propto e^{-E_a/kT}$. Przy $E_a = 0{,}5\ \mathrm{eV}$ wzrost temperatury z 27°C do 37°C prawie podwaja szybkość reakcji.

**Średnia energia z sumy statystycznej.** Oznaczając $\beta = 1/kT$:

$$\langle E\rangle = \frac{\sum E_ie^{-\beta E_i}}{Z} = -\frac{\partial\ln Z}{\partial\beta}.$$

Z $Z$ dostaje się też energię swobodną $F = -kT\ln Z$ i wszystkie wielkości termodynamiczne.

## Wzory i założenia

| Wzór | Znaczenie | Kiedy obowiązuje |
|---|---|---|
| $P_i = e^{-E_i/kT}/Z$, $Z = \sum e^{-E_i/kT}$ | rozkład Boltzmanna | układ w równowadze z termostatem |
| $N_2/N_1 = (g_2/g_1)e^{-\Delta E/kT}$ | stosunek obsadzeń | dwa poziomy |
| $n(h) = n_0e^{-mgh/kT}$, $H = kT/(mg)$ | wzór barometryczny | atmosfera izotermiczna |
| $f(v_x) \propto e^{-mv_x^2/2kT}$ | rozkład składowej prędkości | gaz klasyczny |
| $\langle E\rangle = -\partial\ln Z/\partial\beta$ | średnia energia | $\beta = 1/kT$ |
| $\langle\sigma\rangle = \tanh(\mu B/kT)$ | polaryzacja spinów ½ | paramagnetyk idealny |
| $k = 1{,}380649\cdot10^{-23}\ \mathrm{J/K}$; $kT \approx 0{,}0259\ \mathrm{eV}$ w 300 K | — | — |

## Przykład rozwiązany

**Zadanie 1.** Oblicz wysokość skali atmosfery dla azotu w temperaturze 288 K. Ile razy niższe jest ciśnienie na Mount Everest (8849 m) w modelu izotermicznym?

$H = \dfrac{kT}{mg} = \dfrac{1{,}38\cdot10^{-23}\cdot288}{4{,}65\cdot10^{-26}\cdot9{,}81} \approx 8{,}7\ \mathrm{km}$. $p/p_0 = e^{-8849/8700} \approx 0{,}36$ (zmierzone ok. 0,33 — temperatura spada z wysokością).

**Zadanie 2.** Elektron w polu 1 T ma dwa stany spinowe o energiach $\pm\mu_BB$ ($\mu_B = 9{,}27\cdot10^{-24}\ \mathrm{J/T}$). Jaka część elektronów więcej jest w stanie niższym w 300 K i w 1 K?

Polaryzacja $\tanh(\mu_BB/kT)$: w 300 K $0{,}0022$ (0,2%), w 1 K $0{,}59$. Dlatego silne namagnesowanie paramagnetyków wymaga niskich temperatur.

### Wersja z rachunkiem różniczkowym i całkowym

**Średnia energia kwantowego oscylatora.** Poziomy $E_n = n\hbar\omega$ ($n = 0, 1, 2, \dots$; pomijamy energię zerową). Suma statystyczna to szereg geometryczny:

$$Z = \sum_{n=0}^\infty e^{-n\beta\hbar\omega} = \frac{1}{1 - e^{-\beta\hbar\omega}}, \qquad \langle E\rangle = -\frac{\partial\ln Z}{\partial\beta} = \frac{\hbar\omega}{e^{\beta\hbar\omega} - 1}.$$

Ten sam wynik daje kryształ Einsteina (27.01). Dla $kT \gg \hbar\omega$: $\langle E\rangle \approx kT$.

**Rozkład Maxwella z czynnika Boltzmanna.** Gęstość prawdopodobieństwa wektora prędkości $\propto e^{-m(v_x^2 + v_y^2 + v_z^2)/2kT}$. Wartości prędkości od $v$ do $v + dv$ odpowiada warstwa kulista o objętości $4\pi v^2dv$, więc

$$f(v) = 4\pi v^2\left(\frac{m}{2\pi kT}\right)^{3/2}e^{-mv^2/2kT}.$$

Z normalizacji całki Gaussa $\int_{-\infty}^\infty e^{-ax^2}dx = \sqrt{\pi/a}$. Prędkość najbardziej prawdopodobna: $f'(v) = 0 \Rightarrow v_p = \sqrt{2kT/m}$.

## Typowe pułapki

- **Stan o niższej energii jest zawsze pełny, a wyższy pusty.** Tak jest tylko dla $\Delta E \gg kT$. Przy $\Delta E \ll kT$ obsadzenia są prawie równe.
- **Prawdopodobieństwo poziomu a prawdopodobieństwo stanu.** Poziom o degeneracji $g$ ma $g$ stanów, więc prawdopodobieństwo poziomu zawiera czynnik $g$. W rozkładzie Maxwella rolę „degeneracji” gra $4\pi v^2$ — dlatego najbardziej prawdopodobna wartość prędkości nie jest równa zeru.
- **Czynnik Boltzmanna działa zawsze.** Wymaga równowagi termicznej. W laserze (inwersja obsadzeń) i w plazmie nierównowagowej nie obowiązuje.
- **Mylenie $k$ i $R$.** $k$ dotyczy jednej cząsteczki, $R = N_Ak$ — mola. W czynniku Boltzmanna energia na cząsteczkę dzieli się przez $kT$, energia na mol przez $RT$.

## Doświadczenie / symulacja

**Ciśnienie a wysokość.** Zmierz barometrem w phyphox (*Ciśnienie*) ciśnienie na parterze i na ostatnim piętrze wysokiego budynku (albo w windzie). Ze wzoru barometrycznego wyznacz różnicę wysokości: przy ziemi $\Delta p/p \approx -\Delta h/H$, czyli ok. 12 Pa na metr.

**Symulacja PhET:** *Właściwości gazu* — histogram prędkości cząsteczek dla różnych temperatur ([phet.colorado.edu/pl](https://phet.colorado.edu/pl/)).

**Python:** losowanie prędkości cząsteczek z czynnika Boltzmanna i porównanie z rozkładem Maxwella, wzór barometryczny, obsadzenie poziomów wodoru w gwiazdach i polaryzacja paramagnetyka.

```python
import numpy as np
import matplotlib.pyplot as plt

k, amu, e, muB = 1.380649e-23, 1.66054e-27, 1.602176634e-19, 9.2740100783e-24
m, T = 28*amu, 300                                          # azot
rng = np.random.default_rng(1)
v = np.linalg.norm(rng.normal(0, np.sqrt(k*T/m), (200000, 3)), axis=1)   # składowe z rozkładu Boltzmanna
vv = np.linspace(0, 1500, 300)
maxwell = 4*np.pi*vv**2*(m/(2*np.pi*k*T))**1.5*np.exp(-m*vv**2/(2*k*T))
print(f"N₂, 300 K: v_p = {np.sqrt(2*k*T/m):.0f} m/s, <v> = {v.mean():.0f} m/s (teoria {np.sqrt(8*k*T/(np.pi*m)):.0f}), "
      f"v_sk = {np.sqrt((v**2).mean()):.0f} m/s (teoria {np.sqrt(3*k*T/m):.0f})")

for nazwa, M in [("N₂", 28), ("O₂", 32), ("He", 4)]:
    print(f"wysokość skali {nazwa} w 288 K: {k*288/(M*amu*9.81)/1e3:.1f} km")
for T_gw in (3600, 5772, 10000, 20000):
    print(f"wodór, T = {T_gw:5d} K: N(n=2)/N(n=1) = {4*np.exp(-10.2*e/(k*T_gw)):.1e}")
for Tp in (300, 4.2, 1):
    print(f"spiny elektronów w 1 T, T = {Tp:5.1f} K: polaryzacja {np.tanh(muB*1/(k*Tp)):.4f}")

plt.hist(v, bins=100, density=True, alpha=0.5, label="losowanie (czynnik Boltzmanna)")
plt.plot(vv, maxwell, "r", label="rozkład Maxwella")
plt.xlabel("v [m/s]"); plt.ylabel("f(v)"); plt.legend(); plt.show()
```

## Zadania

### A. Poziom maturalny _(opcjonalnie — rozgrzewka)_

1. Ile wynosi $kT$ w elektronowoltach w temperaturze 300 K i w temperaturze powierzchni Słońca (5800 K)?

<details>
<summary>Odpowiedź</summary>

0,026 eV i 0,50 eV.
</details>

2. Dlaczego hel i wodór uciekają z atmosfery Ziemi, a azot nie?

<details>
<summary>Odpowiedź</summary>

W tej samej temperaturze lżejsze cząsteczki mają większe prędkości ($v \propto 1/\sqrt m$). W „ogonie” rozkładu Maxwella znacznie więcej cząsteczek wodoru i helu przekracza prędkość ucieczki (11,2 km/s) w górnej atmosferze.
</details>

### B. Poziom akademicki

1. Reakcja ma energię aktywacji 0,8 eV. Ile razy przyspieszy przy wzroście temperatury z 20°C do 30°C?

<details>
<summary>Odpowiedź</summary>

$\exp\left[\dfrac{E_a}{k}\left(\dfrac1{293} - \dfrac1{303}\right)\right] = \exp(0{,}80/8{,}617\cdot10^{-5}\cdot1{,}126\cdot10^{-4}) \approx e^{1{,}05} \approx 2{,}8$ razy.
</details>

2. Układ dwupoziomowy: energie 0 i $\varepsilon$. Oblicz $Z$, średnią energię i ciepło właściwe $C = d\langle E\rangle/dT$. Dla jakiego $kT/\varepsilon$ ciepło właściwe jest największe?

<details>
<summary>Odpowiedź</summary>

$Z = 1 + e^{-\beta\varepsilon}$, $\langle E\rangle = \dfrac{\varepsilon}{e^{\beta\varepsilon} + 1}$, $C = k\dfrac{x^2e^x}{(e^x + 1)^2}$ z $x = \varepsilon/kT$. Maksimum (anomalia Schottky'ego) przy $x \approx 2{,}4$, czyli $kT \approx 0{,}42\varepsilon$.
</details>

3. Wyprowadź wzór barometryczny z równowagi hydrostatycznej $dp/dh = -\rho g$ i równania gazu doskonałego $p = \rho kT/m$.

<details>
<summary>Odpowiedź</summary>

$\dfrac{dp}{dh} = -\dfrac{mg}{kT}p \Rightarrow p = p_0e^{-mgh/kT}$. Ten sam wynik daje czynnik Boltzmanna z energią $mgh$.
</details>

4. Pokaż, że średnia energia kinetyczna z rozkładu Maxwella wynosi $\tfrac32kT$, korzystając z $\langle E\rangle = -\partial\ln Z/\partial\beta$ dla $Z = \int e^{-\beta mv^2/2}d^3v$.

<details>
<summary>Odpowiedź</summary>

$Z = (2\pi/(\beta m))^{3/2}$, $\ln Z = -\tfrac32\ln\beta + \text{const}$, $\langle E\rangle = \dfrac{3}{2\beta} = \tfrac32kT$.
</details>

## Źródła

- OpenStax, *Fizyka dla szkół wyższych*, t. 2, rozdz. 2 — §2.4: rozkład prędkości cząsteczek gazu doskonałego.
- Halliday, Resnick, Walker, *Podstawy fizyki* — wyd. 2015: t. 2, §19.6; wyd. 1: t. 2, §20.7 (rozkład prędkości cząsteczek).
- F. Reif, *Fizyka statystyczna* (Kurs Fizyki Berkeley, t. 5), PWN.
- Moduły 11.04 (teoria kinetyczna gazów), 23.04 (półprzewodniki samoistne), 26.01 (widma gwiazd).
- Symulacja PhET *Właściwości gazu*.
