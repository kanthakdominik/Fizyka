# 15.07 — Transformator i przesył energii

> **Moduł:** [15 — Indukcja elektromagnetyczna i prąd przemienny](README.md) · **Poziom:** 🟢 matura R · **Status:** ✅ pełny
>
> **Czytaj:**
>
> - OpenStax, *Fizyka dla szkół wyższych*, t. 2, rozdz. 15: [§15.6](https://openstax.org/books/fizyka-dla-szk%C3%B3%C5%82-wy%C5%BCszych-tom-2/pages/15-6-transformatory) · [wstęp do rozdziału](https://openstax.org/books/fizyka-dla-szk%C3%B3%C5%82-wy%C5%BCszych-tom-2/pages/15-wstep)
> - Halliday, Resnick, Walker, *Podstawy fizyki*, wyd. 2015, t. 3: §31.6 (s. 411)
> - Halliday, Resnick, Walker, *Podstawy fizyki*, wyd. 1 (2003), t. 3: §33.11, s. 347 (skan t. 3 na serwerze AGH kończy się na s. 127 — dalsze strony tylko w wydaniu papierowym)

← [Prąd przemienny: wartości skuteczne, impedancja, rezonans, moc](06-prad-przemienny.md) · [spis modułu](README.md) · (koniec modułu) →

## Po co to jest

Transformator zmienia napięcie przemienne prawie bez strat. Dzięki niemu energię z elektrowni przesyła się liniami 110–400 kV (małe straty, 13.03), a w domu korzysta z 230 V. Transformatory siedzą w zasilaczach, ładowarkach, spawarkach, piecykach mikrofalowych (kilka kV dla magnetronu) i w każdej stacji transformatorowej na osiedlu. Działają tylko przy prądzie przemiennym, co przesądziło o wyborze takiego prądu w sieciach energetycznych.

## Teoria w pigułce

**Budowa.** Dwie cewki, pierwotna ($N_1$ zwojów) i wtórna ($N_2$), są nawinięte na wspólny zamknięty rdzeń ferromagnetyczny. Rdzeń prowadzi prawie cały strumień, więc przez każdy zwój obu cewek przechodzi ten sam zmienny strumień $\Phi(t)$.

**Przekładnia napięć.** Z prawa Faradaya w każdym zwoju indukuje się ta sama SEM $d\Phi/dt$:

$$\frac{U_2}{U_1} = \frac{N_2}{N_1}.$$

$N_2 > N_1$ daje transformator podwyższający, a $N_2 < N_1$ obniżający.

**Przekładnia prądów.** W transformatorze idealnym (bez strat) moc wejściowa równa się wyjściowej: $U_1I_1 = U_2I_2$, więc

$$\frac{I_2}{I_1} = \frac{N_1}{N_2}.$$

Podwyższenie napięcia oznacza obniżenie prądu. Dlatego przewody uzwojenia niskonapięciowego są grube.

**Bez obciążenia** transformator pobiera tylko mały prąd magnesujący. Indukcyjność uzwojenia pierwotnego ma dużą reaktancję. Po obciążeniu prąd wtórny wytwarza strumień przeciwny i prąd pierwotny rośnie, tak że moc „przepływa” z sieci do odbiornika.

**Straty w rzeczywistym transformatorze:**
- ciepło w uzwojeniach ($I^2R$, „straty w miedzi”);
- prądy wirowe i histereza w rdzeniu („straty w żelazie”), ograniczane blachami i miękkim materiałem (14.07, 15.03);
- strumień rozproszenia.

Duże transformatory energetyczne mają sprawność ponad 99%.

**Transformator a częstotliwość.** Im wyższa częstotliwość, tym mniejszy rdzeń wystarcza do przeniesienia tej samej mocy. Dlatego nowoczesne ładowarki najpierw prostują napięcie sieci i zamieniają je na prąd o częstotliwości kilkudziesięciu–kilkuset kHz, a transformator w środku jest wielkości paznokcia.

## Wzory i założenia

| Wzór | Znaczenie | Kiedy obowiązuje |
|---|---|---|
| $U_2/U_1 = N_2/N_1$ | przekładnia napięciowa | brak rozproszenia strumienia |
| $I_2/I_1 = N_1/N_2$ | przekładnia prądowa | transformator idealny, obciążony |
| $U_1I_1 = U_2I_2$ | zachowanie mocy | bez strat |
| $\eta = P_2/P_1$ | sprawność | rzeczywisty transformator |

## Przykład rozwiązany

**Zadanie 1.** Zasilacz halogenów obniża 230 V do 12 V. Uzwojenie pierwotne ma 1150 zwojów. Ile zwojów ma wtórne? Lampa pobiera 2 A. Jaki prąd płynie w uzwojeniu pierwotnym?

$N_2 = 1150\cdot12/230 = 60$. $I_1 = I_2N_2/N_1 = 2\cdot60/1150 \approx 0{,}10\ \mathrm A$.

**Zadanie 2.** Elektrownia oddaje 1 MW. Porównaj straty w linii o oporze 5 Ω przy przesyle 10 kV i 400 kV (13.03) i wyjaśnij rolę transformatorów.

Straty wynoszą 50 kW przy 10 kV i 31 W przy 400 kV. Transformator przy elektrowni podnosi napięcie, a transformatory w kolejnych stacjach obniżają je stopniowo do 15–30 kV (sieć średniego napięcia) i do 230/400 V.

## Typowe pułapki

- **Transformator działa na prąd stały.** Przy stałym prądzie strumień jest stały i nic się nie indukuje. Uzwojenie pierwotne podłączone do napięcia stałego stanowi zwarcie przez mały opór drutu.
- **Podwyższanie napięcia daje darmową energię.** Moc nie rośnie. Prąd maleje w tym samym stosunku.
- **Przekładnia prądowa jak napięciowa.** Prądy mają odwrotny stosunek niż liczby zwojów.
- **Prąd pierwotny nie zależy od odbiornika.** Rośnie wraz z obciążeniem po stronie wtórnej.

## Doświadczenie / symulacja

**Transformator rozbieralny.** W szkolnej pracowni zwykle jest rdzeń z wymiennymi cewkami (np. 300, 600, 1200 zwojów) i zasilacz niskiego napięcia przemiennego. Zmierz napięcia dla różnych par cewek i sprawdź przekładnię. Zobacz, jak spada napięcie wtórne, gdy rozsuniesz jarzmo rdzenia (rośnie rozproszenie strumienia). Nigdy nie podłączaj cewek bezpośrednio do sieci 230 V.

**Ładowarka bezprzewodowa** to transformator bez rdzenia. Ma przez to niższą sprawność niż ładowarka przewodowa.

**Symulacja PhET:** *Transformator* (*Transformer*) — część *Laboratorium elektromagnetycznego Faradaya*.

**Python:** sprawność i spadek napięcia prostego modelu transformatora z oporami uzwojeń.

```python
import numpy as np

N1, N2, U1 = 1150, 60, 230.0
k = N2/N1
R1, R2 = 8.0, 0.02                       # opory uzwojeń [Ω]
for R_obc in (60.0, 12.0, 6.0, 3.0):
    # oporność uzwojenia pierwotnego przeniesiona na stronę wtórną: R1·k²
    I2 = k*U1/(R2 + R1*k**2 + R_obc)
    U2 = I2*R_obc
    P2 = U2*I2
    P1 = P2 + I2**2*(R2 + R1*k**2)
    print(f"obciążenie {R_obc:5.1f} Ω: U2 = {U2:5.2f} V, I2 = {I2:5.2f} A, I1 = {I2*k:.3f} A, sprawność {P2/P1*100:5.1f} %")
print(f"idealnie: U2 = {U1*k:.1f} V")
```

## Zadania

### A. Poziom maturalny

1. Transformator ma 500 zwojów pierwotnych i 25 wtórnych. Napięcie pierwotne wynosi 230 V. Oblicz napięcie wtórne. Jaki prąd płynie w uzwojeniu pierwotnym, gdy wtórne zasila odbiornik pobierający 4 A?

<details>
<summary>Odpowiedź</summary>

$U_2 = 11{,}5\ \mathrm V$, $I_1 = 4\cdot25/500 = 0{,}2\ \mathrm A$.
</details>

2. Transformator w kuchence mikrofalowej podnosi 230 V do ok. 2100 V. Jaki jest stosunek zwojów? Jaki prąd pobiera z sieci przy mocy 1200 W (sprawność 100%)?

<details>
<summary>Odpowiedź</summary>

$N_2/N_1 \approx 9{,}1$. $I_1 = 1200/230 \approx 5{,}2\ \mathrm A$.
</details>

3. Dlaczego transformatora nie można podłączyć do baterii?

<details>
<summary>Odpowiedź</summary>

Stały prąd daje stały strumień, więc w uzwojeniu wtórnym nic się nie indukuje. Uzwojenie pierwotne zwiera baterię.
</details>

### B. Poziom akademicki _(opcjonalnie — rozszerzenie z rachunkiem)_

1. Pokaż, że opór $R$ podłączony do uzwojenia wtórnego „widziany” od strony pierwotnej ma wartość $R(N_1/N_2)^2$. Do czego służy to w audio (transformator głośnikowy)?

<details>
<summary>Odpowiedź</summary>

$R' = \dfrac{U_1}{I_1} = \dfrac{U_2N_1/N_2}{I_2N_2/N_1} = R\left(\dfrac{N_1}{N_2}\right)^2$. Transformator dopasowuje opór głośnika (np. 8 Ω) do wymaganego obciążenia wzmacniacza lampowego (kilka kΩ), co daje największą moc (13.04).
</details>

2. Uzwojenie pierwotne bez obciążenia ma indukcyjność 10 H. Jaki prąd pobiera transformator z sieci 230 V, 50 Hz bez obciążenia? Jaką moc czynną (bez strat w rdzeniu)?

<details>
<summary>Odpowiedź</summary>

$I = U/(\omega L) \approx 73\ \mathrm{mA}$. Moc czynna wynosi zero, bo prąd jest przesunięty o $90^\circ$ względem napięcia.
</details>

3. Strumień w rdzeniu ma amplitudę $\Phi_0$. Pokaż, że wartość skuteczna napięcia na uzwojeniu o $N$ zwojach wynosi $U = 4{,}44fN\Phi_0$. Ile zwojów na wolt potrzeba przy 50 Hz, rdzeniu o przekroju 10 cm² i polu 1,2 T?

<details>
<summary>Odpowiedź</summary>

$u = N\omega\Phi_0\cos\omega t$, $U_{\text{sk}} = N2\pi f\Phi_0/\sqrt2 \approx 4{,}44fN\Phi_0$. $\Phi_0 = 1{,}2\cdot10^{-3}\ \mathrm{Wb}$, $N/U = 1/(4{,}44\cdot50\cdot1{,}2\cdot10^{-3}) \approx 3{,}8$ zwoja na wolt.
</details>

## Źródła

- OpenStax, *Fizyka dla szkół wyższych*, t. 2, rozdz. 15 — §15.6: transformatory.
- Halliday, Resnick, Walker, *Podstawy fizyki* — wyd. 2015: t. 3, §31.6; wyd. 1: t. 3, §33.11.
- Symulacja PhET *Laboratorium elektromagnetyczne Faradaya*.
