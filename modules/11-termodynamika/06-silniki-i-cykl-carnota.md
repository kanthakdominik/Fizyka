# 11.06 — Silniki cieplne, chłodziarki i cykl Carnota

> **Moduł:** [11 — Termodynamika i teoria kinetyczna](README.md) · **Poziom:** 🟢 matura R · **Status:** ✅ pełny
>
> **Czytaj:**
>
> - OpenStax, *Fizyka dla szkół wyższych*, t. 2, rozdz. 4: [§4.1–4.5](https://openstax.org/books/fizyka-dla-szk%C3%B3%C5%82-wy%C5%BCszych-tom-2/pages/4-1-procesy-odwracalne-i-nieodwracalne) · [wstęp do rozdziału](https://openstax.org/books/fizyka-dla-szk%C3%B3%C5%82-wy%C5%BCszych-tom-2/pages/4-wstep)
> - Halliday, Resnick, Walker, *Podstawy fizyki*, wyd. 2015, t. 2: §20.2–20.3 (s. 341)
> - Halliday, Resnick, Walker, *Podstawy fizyki*, wyd. 1 (2003), t. 2: [§21.4–21.6, s. 267](https://home.agh.edu.pl/~czapli/Resnick_2.pdf#page=283) — PDF z serwera AGH

← [I zasada termodynamiki i przemiany gazowe](05-pierwsza-zasada.md) · [spis modułu](README.md) · [Entropia i II zasada termodynamiki](07-entropia-i-druga-zasada.md) →

## Po co to jest

Silnik samochodu, turbina elektrowni, lodówka i pompa ciepła to maszyny cieplne. Zamieniają ciepło na pracę albo pracą przepompowują ciepło od zimnego do ciepłego. Fizyka nakłada na nie twarde ograniczenie: żaden silnik nie zamieni całego ciepła na pracę, a sprawność ogranicza różnica temperatur. Ta wiedza pozwala ocenić, dlaczego elektrownie mają sprawność ok. 40%, dlaczego pompa ciepła daje 3–4 razy więcej ciepła niż zużywa prądu i jakie obietnice wynalazców są niemożliwe.

## Teoria w pigułce

**Silnik cieplny** działa cyklicznie:
1. pobiera ciepło $Q_H$ ze źródła gorącego o temperaturze $T_H$;
2. wykonuje pracę $W$;
3. oddaje ciepło $Q_C$ do chłodnicy o temperaturze $T_C$ (otoczenie, rzeka, chłodnia kominowa).

W cyklu $\Delta U = 0$, więc $W = Q_H - Q_C$ (wartości dodatnie). **Sprawność**:

$$\eta = \frac{W}{Q_H} = 1 - \frac{Q_C}{Q_H}.$$

**Druga zasada termodynamiki** ma dwa równoważne sformułowania:
- **Kelvin–Planck**: nie da się zbudować silnika, który w cyklu zamienia całe ciepło z jednego źródła na pracę, bo zawsze $Q_C > 0$.
- **Clausius**: ciepło nie przepływa samorzutnie od ciała zimniejszego do cieplejszego; wymaga to pracy.

**Chłodziarka i pompa ciepła** to silnik odwrócony. Praca $W$ przepompowuje ciepło $Q_C$ z zimnego do gorącego, gdzie oddawane jest $Q_H = Q_C + W$. Ocenia się je **współczynnikiem wydajności** (COP):

$$\text{COP}_{\text{chł}} = \frac{Q_C}{W}, \qquad \text{COP}_{\text{pc}} = \frac{Q_H}{W} = \text{COP}_{\text{chł}} + 1.$$

COP może i powinien być większy od 1, bo nie jest to sprawność zamiany energii. Pompa ciepła nie wytwarza ciepła, tylko je przenosi.

**Cykl Carnota** to idealny cykl odwracalny złożony z dwóch izoterm (w $T_H$ i $T_C$) i dwóch adiabat. **Twierdzenie Carnota**: żaden silnik pracujący między tymi temperaturami nie ma większej sprawności niż odwracalny, a wszystkie odwracalne mają ją równą:

$$\eta_C = 1 - \frac{T_C}{T_H}, \qquad \text{COP}_{\text{chł},C} = \frac{T_C}{T_H - T_C}, \qquad \text{COP}_{\text{pc},C} = \frac{T_H}{T_H - T_C}.$$

Temperatury muszą być w kelwinach. Sprawność rośnie z różnicą temperatur, a COP pompy ciepła maleje.

**Cykle rzeczywiste:**
- **Otto** (silnik benzynowy, 2 adiabaty + 2 izochory): $\eta = 1 - r^{1 - \gamma}$, gdzie $r$ to stopień sprężania. Teoretycznie ok. 60% dla $r = 10$, w praktyce 25–35%.
- **Diesel**: wyższy stopień sprężania i nieco wyższa sprawność.
- **Rankine** (elektrownie parowe): ok. 35–45%.
- **Gazowo-parowy**: do ok. 60%.

## Wzory i założenia

| Wzór | Znaczenie | Kiedy obowiązuje |
|---|---|---|
| $W = Q_H - Q_C$ | bilans silnika | cykl, wartości dodatnie |
| $\eta = W/Q_H = 1 - Q_C/Q_H$ | sprawność silnika | — |
| $\eta_C = 1 - T_C/T_H$ | sprawność Carnota (maksymalna) | odwracalny, $T$ w kelwinach |
| $\text{COP}_{\text{chł}} = Q_C/W \le T_C/(T_H - T_C)$ | chłodziarka | — |
| $\text{COP}_{\text{pc}} = Q_H/W \le T_H/(T_H - T_C)$ | pompa ciepła | — |
| $\eta_{\text{Otto}} = 1 - r^{1 - \gamma}$ | cykl Otto | gaz doskonały, cykl idealny |

## Przykład rozwiązany

**Zadanie 1.** Para w elektrowni ma temperaturę 527°C, a chłodnica 20°C. Jaka jest największa możliwa sprawność? Elektrownia o mocy elektrycznej 1 GW ma rzeczywistą sprawność 33%. Ile ciepła na sekundę oddaje do otoczenia?

$\eta_C = 1 - 293/800 \approx 63\%$. Przy $\eta = 33\%$: $Q_H = 1/0{,}33 \approx 3{,}0\ \mathrm{GW}$, więc do otoczenia trafia $Q_C \approx 2{,}0\ \mathrm{GW}$, dwa razy więcej niż energii elektrycznej.

**Zadanie 2.** Pompa ciepła ogrzewa dom do 20°C, pobierając ciepło z gruntu o temperaturze 0°C. Jaki jest teoretyczny maksymalny COP? Ile ciepła daje rzeczywista pompa o COP = 4 przy poborze 3 kW?

$\text{COP}_C = 293/20 \approx 14{,}7$. Rzeczywista pompa daje $4\cdot3 = 12\ \mathrm{kW}$ ciepła, z czego 9 kW pochodzi z gruntu. Ogrzewanie grzałką dałoby za ten sam prąd tylko 3 kW.

**Zadanie 3.** Oblicz sprawność idealnego cyklu Otto dla stopnia sprężania 10 ($\gamma = 1{,}4$).

$\eta = 1 - 10^{-0{,}4} \approx 60\%$. Rzeczywiste silniki osiągają ok. połowę tej wartości z powodu tarcia, strat ciepła i nieidealnego spalania.

## Typowe pułapki

- **Temperatury w °C we wzorze Carnota.** 1 − 20/527 to błąd. Trzeba wziąć 1 − 293/800.
- **COP > 1 łamie zasadę zachowania energii.** Pompa przenosi ciepło, nie wytwarza go. Energia się zgadza: $Q_H = Q_C + W$.
- **Lodówka z otwartymi drzwiami ochłodzi kuchnię.** Oddaje do kuchni $Q_C + W$, więc ją ogrzewa.
- **Sprawność Carnota to sprawność silników rzeczywistych.** To górna granica. Rzeczywiste silniki są nieodwracalne i mają mniejszą sprawność.
- **Większa sprawność = większa moc.** Silnik Carnota działa nieskończenie wolno (procesy kwazistatyczne). Silniki rzeczywiste są kompromisem między sprawnością a mocą.

## Doświadczenie / symulacja

**Lodówka w kuchni.** Zmierz watomierzem gniazdkowym energię zużytą przez lodówkę w ciągu doby. Oszacuj ciepło przenoszone (ok. 3 razy więcej, jeśli COP ≈ 3) i sprawdź dłonią, że kratka z tyłu lodówki jest ciepła.

**Silnik Stirlinga.** Mały silnik Stirlinga na kubek z gorącą wodą (do kupienia jako zabawka) działa przy różnicy temperatur kilkudziesięciu kelwinów. Sprawdź, że postawiony na kostkach lodu też się kręci, ale w przeciwną stronę, i że staje, gdy temperatury się wyrównają.

**Python:** cykl Carnota na wykresie $p$–$V$ i sprawdzenie sprawności z bilansu ciepła.

```python
import numpy as np
import matplotlib.pyplot as plt

R, n, gam = 8.314, 1.0, 1.4
TH, TC = 800.0, 293.0
V1 = 1e-3; V2 = 3e-3                                 # izoterma gorąca V1 → V2
V3 = V2*(TH/TC)**(1/(gam - 1))                       # adiabata V2 → V3
V4 = V1*(TH/TC)**(1/(gam - 1))                       # izoterma zimna V3 → V4, adiabata V4 → V1
QH = n*R*TH*np.log(V2/V1)
QC = n*R*TC*np.log(V3/V4)
print(f"QH = {QH:.0f} J, QC = {QC:.0f} J, W = {QH - QC:.0f} J")
print(f"η z bilansu = {(QH - QC)/QH:.4f}, η Carnota = {1 - TC/TH:.4f}")

def seg(Va, Vb, f): V = np.linspace(Va, Vb, 100); return V, f(V)
for (Va, Vb, f) in [(V1, V2, lambda V: n*R*TH/V), (V2, V3, lambda V: n*R*TH/V2*(V2/V)**gam),
                    (V3, V4, lambda V: n*R*TC/V), (V4, V1, lambda V: n*R*TC/V4*(V4/V)**gam)]:
    V, p = seg(Va, Vb, f); plt.plot(V*1e3, p/1e5)
plt.xlabel("V [L]"); plt.ylabel("p [bar]"); plt.title("cykl Carnota 800 K / 293 K"); plt.grid(True); plt.show()
```

## Zadania

### A. Poziom maturalny

1. Silnik pobiera w każdym cyklu 2000 J ciepła i oddaje 1400 J. Oblicz pracę i sprawność.

<details>
<summary>Odpowiedź</summary>

$W = 600\ \mathrm J$, $\eta = 30\%$.
</details>

2. Wnętrze lodówki ma 5°C, a kuchnia 25°C. Oblicz największy możliwy COP. Rzeczywista lodówka ma COP = 4 i odbiera z wnętrza 100 W. Ile mocy pobiera i ile ciepła oddaje do kuchni?

<details>
<summary>Odpowiedź</summary>

$\text{COP}_C = 278/20 \approx 13{,}9$. Pobiera 25 W i oddaje 125 W.
</details>

3. Wynalazca twierdzi, że jego silnik pracujący między 400 K a 300 K ma sprawność 30%. Czy to możliwe?

<details>
<summary>Odpowiedź</summary>

Nie. Sprawność Carnota wynosi $1 - 300/400 = 25\%$.
</details>

4. Dlaczego pompy ciepła działają lepiej z ogrzewaniem podłogowym (ok. 35°C) niż z grzejnikami wysokotemperaturowymi (ok. 60°C)?

<details>
<summary>Odpowiedź</summary>

$\text{COP} \le T_H/(T_H - T_C)$ maleje, gdy rośnie $T_H$. Mniejsza różnica temperatur oznacza większy COP.
</details>

### B. Poziom akademicki _(opcjonalnie — rozszerzenie z rachunkiem)_

1. Wyprowadź sprawność cyklu Carnota. Oblicz ciepło na izotermach jako $nRT\ln(V_{\text{końc}}/V_{\text{pocz}})$ i wykaż z równania adiabat, że $V_2/V_1 = V_3/V_4$.

<details>
<summary>Odpowiedź</summary>

$Q_H = nRT_H\ln(V_2/V_1)$, $Q_C = nRT_C\ln(V_3/V_4)$. Z adiabat $T_HV_2^{\gamma-1} = T_CV_3^{\gamma-1}$ i $T_HV_1^{\gamma-1} = T_CV_4^{\gamma-1}$. Dzieląc stronami: $V_2/V_1 = V_3/V_4$, więc $Q_C/Q_H = T_C/T_H$.
</details>

2. Wyprowadź sprawność cyklu Otto: adiabatyczne sprężanie $V_1 \to V_1/r$, izochoryczne spalanie, adiabatyczne rozprężanie, izochoryczne oddanie ciepła.

<details>
<summary>Odpowiedź</summary>

$Q_H = nC_V(T_3 - T_2)$, $Q_C = nC_V(T_4 - T_1)$. Z adiabat $T_2 = T_1r^{\gamma-1}$ i $T_3 = T_4r^{\gamma-1}$, więc $Q_C/Q_H = r^{1-\gamma}$ i $\eta = 1 - r^{1-\gamma}$.
</details>

3. Pompa ciepła powietrze–woda pracuje zimą przy −10°C na zewnątrz, grzejąc wodę do 35°C. Oblicz COP Carnota i porównaj z typowymi 2,5–3 w takich warunkach. Ile razy mniej prądu niż grzałka zużywa pompa o COP = 3?

<details>
<summary>Odpowiedź</summary>

$\text{COP}_C = 308/45 \approx 6{,}8$. Rzeczywista pompa osiąga ok. 40% tej wartości i zużywa 3 razy mniej prądu niż grzałka.
</details>

## Źródła

- OpenStax, *Fizyka dla szkół wyższych*, t. 2, rozdz. 4 — §4.1 (procesy odwracalne i nieodwracalne), §4.2 (silniki cieplne), §4.3 (chłodziarki i pompy ciepła), §4.4 (sformułowania II zasady), §4.5 (cykl Carnota).
- Halliday, Resnick, Walker, *Podstawy fizyki* — wyd. 2015: t. 2, §20.2–20.3; wyd. 1: t. 2, §21.4–21.6.
