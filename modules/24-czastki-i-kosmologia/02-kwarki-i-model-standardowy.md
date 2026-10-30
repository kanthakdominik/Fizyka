# 24.02 — Kwarki i Model Standardowy

> **Moduł:** [24 — Cząstki elementarne i kosmologia](README.md) · **Poziom:** 🟢🔵 matura R + studia · **Status:** ✅ pełny
>
> **Czytaj:**
>
> - OpenStax, *Fizyka dla szkół wyższych*, t. 3, rozdz. 11: [§11.3 i §11.5](https://openstax.org/books/fizyka-dla-szk%C3%B3%C5%82-wy%C5%BCszych-tom-3/pages/11-3-kwarki) · [wstęp do rozdziału](https://openstax.org/books/fizyka-dla-szk%C3%B3%C5%82-wy%C5%BCszych-tom-3/pages/11-wstep)
> - Halliday, Resnick, Walker, *Podstawy fizyki*, wyd. 2015, t. 5: §44.3 (s. 253)
> - Halliday, Resnick, Walker, *Podstawy fizyki*, wyd. 1 (2003), t. 5: [§45.7–45.9, s. 212](https://home.agh.edu.pl/~czapli/Resnick_5.pdf#page=228) — PDF z serwera AGH

← [Cząstki elementarne i prawa zachowania](01-czastki-i-prawa-zachowania.md) · [spis modułu](README.md) · [Akceleratory i detektory cząstek](03-akceleratory-i-detektory.md) →

## Po co to jest

W latach 60. znano już setki hadronów i fizyka cząstek przypominała chemię przed układem okresowym. Model kwarków uporządkował ten „ogród zoologiczny”: wszystkie hadrony zbudowane są z kilku rodzajów kwarków. Razem z leptonami i nośnikami oddziaływań kwarki tworzą **Model Standardowy**, najdokładniej sprawdzoną teorię w historii fizyki. Jego ostatni brakujący element, bozon Higgsa, odkryto w CERN w 2012 r. Model Standardowy pojawia się na maturze rozszerzonej (skład kwarkowy protonu i neutronu, ładunki kwarków, rozpad β na poziomie kwarków).

## Teoria w pigułce

**Kwarki** mają ładunki ułamkowe ($+\tfrac23e$ lub $-\tfrac13e$), spin ½ i liczbę barionową ⅓. Występują w trzech generacjach:

| Generacja | Kwark $+\tfrac23e$ | Kwark $-\tfrac13e$ | Lepton naładowany | Neutrino |
|---|---|---|---|---|
| I | $u$ (up), 2,2 MeV/c² | $d$ (down), 4,7 MeV/c² | $e^-$, 0,511 MeV/c² | $\nu_e$ |
| II | $c$ (charm), 1,27 GeV/c² | $s$ (strange), 93 MeV/c² | $\mu^-$, 106 MeV/c² | $\nu_\mu$ |
| III | $t$ (top), 173 GeV/c² | $b$ (bottom), 4,18 GeV/c² | $\tau^-$, 1777 MeV/c² | $\nu_\tau$ |

Zwykła materia składa się tylko z pierwszej generacji: $u$, $d$, elektronów.

**Hadrony:**
- **bariony** = trzy kwarki: $p = uud$ ($\tfrac23 + \tfrac23 - \tfrac13 = 1$), $n = udd$ (0), $\Lambda^0 = uds$, $\Omega^- = sss$;
- **mezony** = kwark + antykwark: $\pi^+ = u\bar d$, $\pi^- = \bar ud$, $K^+ = u\bar s$, $J/\psi = c\bar c$.

Dziwność to liczba antykwarków $\bar s$ minus liczba kwarków $s$.

**Kolor i uwięzienie.** Barion $\Delta^{++} = uuu$ ma trzy identyczne kwarki w tym samym stanie, co łamałoby zakaz Pauliego. Rozwiązaniem jest nowa liczba kwantowa, **kolor** (umownie: czerwony, zielony, niebieski). Każdy hadron jest „biały”: ma trzy różne kolory (barion) albo kolor i antykolor (mezon). Siłę między kwarkami przenoszą **gluony**, które same niosą kolor (teoria: chromodynamika kwantowa, QCD). Energia pola między kwarkami rośnie liniowo z odległością (ok. 1 GeV/fm), więc kwarków nie da się rozdzielić (**uwięzienie**). Przy próbie rozerwania powstaje nowa para kwark–antykwark, a zamiast swobodnych kwarków pojawiają się „dżety” hadronów.

**Masa protonu** tylko w ok. 1% pochodzi z mas kwarków: $2m_u + m_d \approx 9\ \mathrm{MeV}/c^2$ przy 938 MeV/c². Reszta to energia gluonów i ruchu kwarków ($E = mc^2$, 19.05).

**Rozpad β na poziomie kwarków.** W neutronie kwark $d$ zamienia się w $u$, emitując bozon $W^-$, który rozpada się na elektron i antyneutrino:

$$d \to u + W^- \to u + e^- + \bar\nu_e.$$

Tylko oddziaływanie słabe zmienia rodzaj („zapach”) kwarka.

**Model Standardowy** to 6 kwarków, 6 leptonów (i ich antycząstki), nośniki oddziaływań (foton, 8 gluonów, $W^\pm$, $Z^0$) oraz **bozon Higgsa** (125 GeV/c²). Pole Higgsa nadaje masę bozonom W i Z oraz fermionom. Oddziaływania elektromagnetyczne i słabe są dwoma przejawami jednego oddziaływania **elektrosłabego** (Glashow, Salam, Weinberg; W i Z odkryte w CERN w 1983 r.).

**Czego Model Standardowy nie wyjaśnia:** grawitacji, ciemnej materii (24.04), mas neutrin, przewagi materii nad antymaterią we Wszechświecie.

## Wzory i założenia

| Wzór | Znaczenie | Kiedy obowiązuje |
|---|---|---|
| $Q = \sum q_i$, $B = \tfrac13(n_q - n_{\bar q})$ | ładunek i liczba barionowa hadronu | — |
| $S = n_{\bar s} - n_s$ | dziwność | — |
| $V(r) \approx -\dfrac{a}{r} + kr$, $k \approx 1\ \mathrm{GeV/fm}$ | potencjał kwark–antykwark | model, $r \lesssim 1$ fm |
| $\tau = \hbar/\Gamma$ | czas życia z szerokości rezonansu | — |

## Przykład rozwiązany

**Zadanie 1.** Ustal ładunek, liczbę barionową i dziwność cząstek: $uud$, $udd$, $uds$, $sss$, $u\bar s$, $\bar u d$.

| Skład | Q | B | S | Cząstka |
|---|---|---|---|---|
| $uud$ | +1 | 1 | 0 | $p$ |
| $udd$ | 0 | 1 | 0 | $n$ |
| $uds$ | 0 | 1 | −1 | $\Lambda^0$ |
| $sss$ | −1 | 1 | −3 | $\Omega^-$ |
| $u\bar s$ | +1 | 0 | +1 | $K^+$ |
| $\bar ud$ | −1 | 0 | 0 | $\pi^-$ |

**Zadanie 2.** Zapisz rozpad $\beta^+$ protonu w jądrze na poziomie kwarków.

$p \to n + e^+ + \nu_e$, czyli $uud \to udd$: $u \to d + W^+ \to d + e^+ + \nu_e$. Ładunek: $+\tfrac23 = -\tfrac13 + 1$ ✔.

### Wersja z rachunkiem różniczkowym i całkowym

**Zadanie.** Potencjał kwark–antykwark modeluje się wzorem $V(r) = -\dfrac{a}{r} + kr$ z $a \approx 79\ \mathrm{MeV\cdot fm}$ i $k \approx 900\ \mathrm{MeV/fm}$. Oblicz siłę w odległości 1 fm i pracę potrzebną do rozsunięcia kwarków z 0,5 fm do 1,5 fm. Porównaj z masą pary pionów.

$$F = -\frac{dV}{dr} = -\left(\frac{a}{r^2} + k\right) \Rightarrow |F(1\ \mathrm{fm})| \approx 980\ \mathrm{MeV/fm} \approx 1{,}6\cdot10^5\ \mathrm N.$$

To siła ciężkości ok. 16 ton działająca na cząstkę o rozmiarze $10^{-15}$ m.

$$W = \int_{0{,}5}^{1{,}5}\left(\frac{a}{r^2} + k\right)dr = a\left(\frac1{0{,}5} - \frac1{1{,}5}\right) + k\cdot1\ \mathrm{fm} \approx 1005\ \mathrm{MeV}.$$

To dużo więcej niż $2m_\pi c^2 \approx 280\ \mathrm{MeV}$. Zanim kwarki się rozdzielą, z energii pola powstaje nowa para kwark–antykwark i zamiast wolnych kwarków powstają dwa mezony.

## Typowe pułapki

- **Proton to trzy kwarki i nic więcej.** To kwarki „walencyjne”. W protonie jest też morze gluonów i par kwark–antykwark, które niosą większość masy.
- **Ładunek kwarka $d$ to $-\tfrac23e$.** $u$: $+\tfrac23$, $d$: $-\tfrac13$. Sprawdzaj na protonie: $uud \to +1$.
- **Kolor kwarków ma coś wspólnego z barwą światła.** To tylko nazwa ładunku oddziaływania silnego, występującego w trzech rodzajach.
- **Bozon Higgsa nadaje masę całej materii.** Nadaje masę cząstkom elementarnym. Masa protonów i neutronów, a więc prawie całej zwykłej materii, pochodzi głównie z energii oddziaływania silnego.

## Doświadczenie / symulacja

**Dane z LHC.** Portal CERN Open Data i *International Masterclasses* udostępniają prawdziwe przypadki zderzeń z detektorów ATLAS i CMS. Uczniowie identyfikują rozpady $Z \to \mu^+\mu^-$ i rekonstruują masę Z oraz Higgsa (materiał dodatkowy, po angielsku; polskie ośrodki prowadzą warsztaty Masterclasses w języku polskim).

**Python:** generator składu hadronów (ładunek, dziwność) z kwarków i model rozpadu Z z rozkładem Breita–Wignera.

```python
import numpy as np
import matplotlib.pyplot as plt
from itertools import combinations_with_replacement
from fractions import Fraction as F

q = {"u": F(2, 3), "d": F(-1, 3), "s": F(-1, 3)}
print("bariony z kwarków u, d, s (multiplety):")
for trojka in combinations_with_replacement("uds", 3):
    Q = sum(q[k] for k in trojka); S = -trojka.count("s")
    print(f"  {''.join(trojka)}: Q = {str(Q):>2s}, S = {S}")
print("mezony kwark–antykwark:")
for a in "uds":
    for b in "uds":
        print(f"  {a}{b}̄: Q = {str(q[a] - q[b]):>2s}, S = {b.count('s') - a.count('s')}")

# rezonans Z0: rozkład Breita–Wignera, M = 91,19 GeV, Γ = 2,495 GeV
M, G = 91.188, 2.4952
E = np.linspace(85, 97, 12001)
bw = (G/2)**2/((E - M)**2 + (G/2)**2)
pol = E[bw >= 0.5]
print(f"szerokość połówkowa z wykresu: {pol[-1] - pol[0]:.3f} GeV, czas życia Z: {6.582e-25/G:.2e} s")
print(f"liczba rodzajów lekkich neutrin z szerokości niewidzialnej: {0.499/0.1672:.2f}")
plt.plot(E, bw); plt.xlabel("energia zderzenia [GeV]"); plt.ylabel("przekrój czynny (wzgl.)"); plt.grid(True); plt.show()
```

## Zadania

### A. Poziom maturalny

1. Neutron składa się z kwarków $udd$. Oblicz jego ładunek. Jaki skład ma antyneutron?

<details>
<summary>Odpowiedź</summary>

$\tfrac23 - \tfrac13 - \tfrac13 = 0$. Antyneutron: $\bar u\bar d\bar d$ (też obojętny, ale $B = -1$).
</details>

2. Dlaczego nie obserwuje się swobodnych kwarków?

<details>
<summary>Odpowiedź</summary>

Energia oddziaływania silnego rośnie z odległością. Przy próbie rozdzielenia powstaje nowa para kwark–antykwark i powstają nowe hadrony (uwięzienie koloru).
</details>

3. Ile cząstek elementarnych materii (fermionów) zawiera Model Standardowy, nie licząc antycząstek? Które z nich budują atomy?

<details>
<summary>Odpowiedź</summary>

12: 6 kwarków i 6 leptonów. Atomy budują $u$, $d$ (w protonach i neutronach) i elektrony.
</details>

### B. Poziom akademicki

1. Gell-Mann w 1962 r. uporządkował barionowe rezonanse o spinie 3/2 w dekuplet: $\Delta$ (1232 MeV, $S = 0$), $\Sigma^*$ (1385, $S = -1$), $\Xi^*$ (1533, $S = -2$). Przewidź masę brakującej cząstki o $S = -3$ i jej skład.

<details>
<summary>Odpowiedź</summary>

Odstępy ok. 150 MeV, więc ok. 1680 MeV. Skład $sss$, ładunek −1: $\Omega^-$. Odkryta w 1964 r. z masą 1672 MeV/c².
</details>

2. Szerokość bozonu Z to 2,495 GeV. Oblicz jego czas życia. Część szerokości (0,499 GeV) przypada na rozpady „niewidzialne” (na pary neutrin), a jeden rodzaj neutrin daje 0,167 GeV. Ile jest rodzajów lekkich neutrin?

<details>
<summary>Odpowiedź</summary>

$\tau = \hbar/\Gamma \approx 2{,}6\cdot10^{-25}\ \mathrm s$. $0{,}499/0{,}167 \approx 2{,}98$, czyli trzy rodzaje (LEP, 1989). To pośredni dowód, że generacje są dokładnie trzy.
</details>

3. Pokaż, że dla rozkładu Breita–Wignera $f(E) = \dfrac{(\Gamma/2)^2}{(E - M)^2 + (\Gamma/2)^2}$ pełna szerokość w połowie wysokości wynosi $\Gamma$, a pole pod krzywą jest równe $\dfrac{\pi\Gamma}{2}$.

<details>
<summary>Odpowiedź</summary>

$f = \tfrac12 \Leftrightarrow (E - M)^2 = (\Gamma/2)^2 \Rightarrow E = M \pm \Gamma/2$. Pole: podstawienie $x = 2(E - M)/\Gamma$ daje $\dfrac{\Gamma}{2}\displaystyle\int_{-\infty}^{\infty}\frac{dx}{1 + x^2} = \frac{\pi\Gamma}{2}$.
</details>

4. Zapisz na poziomie kwarków rozpad $\Lambda^0 \to p + \pi^-$. Który kwark się zmienia i jakie oddziaływanie za to odpowiada?

<details>
<summary>Odpowiedź</summary>

$uds \to uud + \bar ud$: kwark $s$ zamienia się w $u$ (emitując $W^-$, który tworzy parę $d\bar u$). Zmiana zapachu, więc oddziaływanie słabe.
</details>

## Źródła

- OpenStax, *Fizyka dla szkół wyższych*, t. 3, rozdz. 11 — §11.3 (kwarki) i §11.5 (Model Standardowy).
- Halliday, Resnick, Walker, *Podstawy fizyki* — wyd. 2015: t. 5, §44.3; wyd. 1: t. 5, §45.7–45.9.
- Particle Data Group, *Review of Particle Physics* — masy i własności cząstek ([pdg.lbl.gov](https://pdg.lbl.gov), materiał dodatkowy, po angielsku).
