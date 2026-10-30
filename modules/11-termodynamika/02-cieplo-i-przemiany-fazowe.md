# 11.02 — Ciepło, ciepło właściwe, przemiany fazowe, kalorymetria

> **Moduł:** [11 — Termodynamika i teoria kinetyczna](README.md) · **Poziom:** 🟢 matura R · **Status:** ✅ pełny
>
> **Czytaj:**
>
> - OpenStax, *Fizyka dla szkół wyższych*, t. 2, rozdz. 1: [§1.4–1.5](https://openstax.org/books/fizyka-dla-szk%C3%B3%C5%82-wy%C5%BCszych-tom-2/pages/1-4-przekazywanie-ciepla-cieplo-wlasciwe-i-kalorymetria) · [wstęp do rozdziału](https://openstax.org/books/fizyka-dla-szk%C3%B3%C5%82-wy%C5%BCszych-tom-2/pages/1-wstep)
> - Halliday, Resnick, Walker, *Podstawy fizyki*, wyd. 2015, t. 2: §18.4 (s. 254)
> - Halliday, Resnick, Walker, *Podstawy fizyki*, wyd. 1 (2003), t. 2: [§19.6–19.7, s. 197](https://home.agh.edu.pl/~czapli/Resnick_2.pdf#page=213) — PDF z serwera AGH

← [Temperatura i rozszerzalność cieplna](01-temperatura-i-rozszerzalnosc.md) · [spis modułu](README.md) · [Przewodnictwo, konwekcja i promieniowanie cieplne](03-transport-ciepla.md) →

## Po co to jest

Ciepło to energia przekazywana z powodu różnicy temperatur. Bilans cieplny pozwala obliczyć, ile energii zużyje czajnik, jak szybko ostygnie herbata z kostką lodu i ile paliwa trzeba do ogrzania domu. Dzięki dużemu ciepłu właściwemu wody morza łagodzą klimat. Dzięki ciepłu parowania pot chłodzi ciało, a para wodna parzy mocniej niż wrzątek. Kalorymetria była też historycznie drogą do odkrycia, że ciepło jest formą energii (doświadczenie Joule'a).

## Teoria w pigułce

**Ciepło** $Q$ to energia przepływająca między ciałami z powodu różnicy temperatur. Jednostką jest dżul (dawniej kaloria: 1 cal = 4,186 J). Ciało nie „zawiera ciepła”, tylko **energię wewnętrzną** (11.05).

**Ciepło właściwe** $c$ to energia potrzebna do ogrzania 1 kg substancji o 1 K:

$$Q = mc\,\Delta T.$$

Woda ma wyjątkowo dużą wartość, 4190 J/(kg·K). Lód ma ok. 2100, aluminium 900, żelazo 450, miedź 385 J/(kg·K). **Pojemność cieplna** ciała to $C = mc$, a **molowe ciepło właściwe** to $C_{\text{mol}} = Mc$.

**Przemiany fazowe** (topnienie, krzepnięcie, parowanie, skraplanie, sublimacja) zachodzą w stałej temperaturze. Dostarczane ciepło idzie na zerwanie wiązań, a nie na wzrost temperatury:

$$Q = mL.$$

Dla wody ciepło topnienia wynosi $L_t = 334\ \mathrm{kJ/kg}$, a ciepło parowania $L_p = 2256\ \mathrm{kJ/kg}$ w 100°C. Odparowanie wody wymaga ponad 5 razy więcej energii niż ogrzanie jej od 0 do 100°C.

Temperatura wrzenia zależy od ciśnienia. W górach woda wrze poniżej 100°C, a w szybkowarze powyżej. Całość opisuje **wykres fazowy** z punktem potrójnym i krytycznym.

**Bilans cieplny (kalorymetria).** W izolowanym układzie ciepło oddane przez ciała cieplejsze jest równe ciepłu pobranemu przez chłodniejsze:

$$\sum Q_{\text{oddane}} = \sum Q_{\text{pobrane}} \quad \text{lub} \quad \sum_i m_ic_i(T_k - T_i) + \sum Q_{\text{przemian}} = 0.$$

Przy mieszaniu z lodem trzeba najpierw sprawdzić, czy ciepła wystarczy na stopienie całego lodu.

## Wzory i założenia

| Wzór | Znaczenie | Kiedy obowiązuje |
|---|---|---|
| $Q = mc\Delta T$ | ogrzewanie bez przemiany fazowej | $c$ stałe w zakresie temperatur |
| $Q = mL$ | przemiana fazowa | stała temperatura i ciśnienie |
| $\sum m_ic_i(T_k - T_i) = 0$ | temperatura końcowa mieszaniny | układ izolowany, bez przemian |
| $Q = \int mc(T)\,dT$ | gdy $c$ zależy od temperatury | — |
| $c_{\text{wody}} = 4190\ \mathrm{J/(kg\cdot K)}$, $L_t = 334\ \mathrm{kJ/kg}$, $L_p = 2256\ \mathrm{kJ/kg}$ | stałe dla wody | — |

## Przykład rozwiązany

**Zadanie 1.** Do 1 kg wody o temperaturze 80°C wlano 0,5 kg wody o temperaturze 20°C. Oblicz temperaturę końcową.

$1\cdot c(80 - T) = 0{,}5\cdot c(T - 20) \Rightarrow T = \dfrac{80 + 10}{1{,}5} = 60^\circ\mathrm C$. Ciepło właściwe się skraca.

**Zadanie 2.** Do 0,3 kg wody o temperaturze 40°C wrzucono 50 g lodu o temperaturze 0°C. Oblicz temperaturę końcową.

Stopienie lodu wymaga $0{,}05\cdot334\,000 = 16\,700\ \mathrm J$. Ochłodzenie wody do 0°C oddałoby $0{,}3\cdot4190\cdot40 = 50\,280\ \mathrm J$, więc lód stopi się cały.

Bilans: $0{,}3\cdot4190(40 - T) = 16\,700 + 0{,}05\cdot4190\,T$, stąd $T = \dfrac{50\,280 - 16\,700}{0{,}35\cdot4190} \approx 22{,}9^\circ\mathrm C$.

Dla porównania: 50 g wody o temperaturze 0°C dałoby 34,3°C. Ciepło topnienia „zjada” ponad 11 K.

## Typowe pułapki

- **Mieszanie z lodem bez sprawdzenia.** Jeśli ciepła nie wystarcza na stopienie całego lodu, temperatura końcowa wynosi 0°C, a wynik ze wzoru wychodzi absurdalnie ujemny.
- **Podczas wrzenia temperatura rośnie.** Stoi w miejscu, dopóki cała woda nie odparuje, przy stałym ciśnieniu.
- **Ciepło = temperatura.** Ciało gorące może oddać mało ciepła (iskra), a letnie dużo (morze).
- **Znaki w bilansie.** Albo „oddane = pobrane” z dodatnimi wartościami, albo suma wszystkich $Q$ równa zeru ze znakami. Nie należy mieszać tych dwóch zapisów.
- **Pomijanie naczynia.** W kalorymetrze naczynie też pobiera ciepło ($m_kc_k\Delta T$).

## Doświadczenie / symulacja

**Ciepło właściwe wody czajnikiem.** Odmierz 1 kg wody, zmierz temperaturę początkową i czas do zagotowania. Z mocy znamionowej czajnika oblicz $c$ wody (lub sprawność czajnika, przyjmując $c$ z tablic).

**Ciepło topnienia lodu.** Do termosu z ciepłą wodą o znanej masie i temperaturze wrzuć osuszone kostki lodu o znanej masie. Po stopieniu zmierz temperaturę końcową i wyznacz $L_t$. Porównaj z 334 kJ/kg.

**Symulacja PhET:** *Stany skupienia* (*States of Matter*) — przemiany fazowe i wykres fazowy na poziomie cząsteczek ([phet.colorado.edu/pl](https://phet.colorado.edu/pl/)).

**Python:** krzywa ogrzewania 1 kg lodu od −10°C do pary oraz bilans z lodem.

```python
import numpy as np
import matplotlib.pyplot as plt

c_l, c_w, c_p, L_t, L_p = 2100, 4190, 2010, 334e3, 2256e3
m, P = 1.0, 2000.0                                   # 1 kg, grzałka 2 kW
etapy = [("lód −10→0 °C", m*c_l*10, -10, 0), ("topnienie", m*L_t, 0, 0),
         ("woda 0→100 °C", m*c_w*100, 0, 100), ("parowanie", m*L_p, 100, 100), ("para 100→120 °C", m*c_p*20, 100, 120)]
Q = 0
for nazwa, dQ, T1, T2 in etapy:
    plt.plot([Q/1e6, (Q + dQ)/1e6], [T1, T2], lw=2)
    print(f"{nazwa:16s} Q = {dQ/1e3:7.0f} kJ, czas = {dQ/P/60:5.1f} min")
    Q += dQ

def mieszanie(m_w, T_w, m_lod):                      # lód o temperaturze 0 °C
    if m_w*c_w*T_w < m_lod*L_t:
        return 0.0, m_w*c_w*T_w/L_t                   # stopiona tylko część lodu
    return (m_w*c_w*T_w - m_lod*L_t)/((m_w + m_lod)*c_w), m_lod
print("0,3 kg wody 40 °C + 50 g lodu: T = %.1f °C, stopiono %.3f kg" % mieszanie(0.3, 40, 0.05))
print("0,1 kg wody 20 °C + 100 g lodu: T = %.1f °C, stopiono %.3f kg" % mieszanie(0.1, 20, 0.1))
plt.xlabel("Q [MJ]"); plt.ylabel("T [°C]"); plt.grid(True); plt.show()
```

## Zadania

### A. Poziom maturalny

1. Ile czasu czajnik o mocy 2 kW potrzebuje na zagotowanie 1,5 L wody o temperaturze 20°C? Pomiń straty.

<details>
<summary>Odpowiedź</summary>

$Q = 1{,}5\cdot4190\cdot80 \approx 503\ \mathrm{kJ}$, $t \approx 251\ \mathrm s \approx 4{,}2\ \mathrm{min}$.
</details>

2. Dlaczego para wodna o temperaturze 100°C parzy dotkliwiej niż wrzątek? Porównaj ciepło oddane skórze przez 10 g pary i 10 g wrzątku, które ochładzają się do 37°C.

<details>
<summary>Odpowiedź</summary>

Para: $0{,}01(2\,256\,000 + 4190\cdot63) \approx 25\ \mathrm{kJ}$. Wrzątek: $0{,}01\cdot4190\cdot63 \approx 2{,}6\ \mathrm{kJ}$. Para oddaje ok. 10 razy więcej, głównie przy skraplaniu.
</details>

3. Metalowy klocek o masie 0,2 kg i temperaturze 100°C wrzucono do 0,3 kg wody o temperaturze 20°C. Temperatura końcowa wyniosła 25°C. Oblicz ciepło właściwe metalu i zgadnij, co to za metal.

<details>
<summary>Odpowiedź</summary>

$c = \dfrac{0{,}3\cdot4190\cdot5}{0{,}2\cdot75} \approx 419\ \mathrm{J/(kg\cdot K)}$, czyli prawdopodobnie stal lub żelazo.
</details>

4. Do 0,1 kg wody o temperaturze 20°C wrzucono 100 g lodu o temperaturze 0°C. Jaki jest stan końcowy?

<details>
<summary>Odpowiedź</summary>

Ciepła wystarczy tylko na stopienie $0{,}1\cdot4190\cdot20/334\,000 \approx 25\ \mathrm g$ lodu. Zostaje mieszanina wody i 75 g lodu w 0°C.
</details>

### B. Poziom akademicki _(opcjonalnie — rozszerzenie z rachunkiem)_

1. W niskich temperaturach molowe ciepło właściwe miedzi spełnia prawo Debye'a $C = 1944\left(\dfrac{T}{\Theta}\right)^3\ \mathrm{J/(mol\cdot K)}$ z $\Theta = 343\ \mathrm K$. Ile ciepła trzeba, żeby ogrzać mol miedzi od 0 do 20 K?

<details>
<summary>Odpowiedź</summary>

$Q = \displaystyle\int_0^{20}1944\frac{T^3}{\Theta^3}dT = \frac{1944\cdot20^4}{4\Theta^3} \approx 1{,}9\ \mathrm J$. Dla porównania ogrzanie od 300 do 301 K wymaga ok. 24 J.
</details>

2. Ile energii trzeba, żeby zamienić 1 kg lodu o temperaturze −10°C w parę o temperaturze 100°C? Jaki procent przypada na parowanie?

<details>
<summary>Odpowiedź</summary>

$21 + 334 + 419 + 2256 \approx 3030\ \mathrm{kJ}$. Parowanie to ok. 74%.
</details>

3. Ciało o pojemności cieplnej $C$ ogrzewane jest grzałką o mocy $P$ i jednocześnie traci ciepło do otoczenia w tempie $k(T - T_{\text{ot}})$. Zapisz i rozwiąż równanie na $T(t)$, jeśli $T(0) = T_{\text{ot}}$.

<details>
<summary>Odpowiedź</summary>

$C\dfrac{dT}{dt} = P - k(T - T_{\text{ot}})$, stąd $T = T_{\text{ot}} + \dfrac Pk\left(1 - e^{-kt/C}\right)$. Temperatura dąży do $T_{\text{ot}} + P/k$ ze stałą czasową $C/k$ (porównaj ładowanie kondensatora, 13).
</details>

## Źródła

- OpenStax, *Fizyka dla szkół wyższych*, t. 2, rozdz. 1 — §1.4 (przekazywanie ciepła, ciepło właściwe i kalorymetria) i §1.5 (przemiany fazowe).
- Halliday, Resnick, Walker, *Podstawy fizyki* — wyd. 2015: t. 2, §18.4; wyd. 1: t. 2, §19.6–19.7.
- Symulacja PhET *Stany skupienia*.
