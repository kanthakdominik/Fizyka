# 11.07 — Entropia i II zasada termodynamiki

> **Moduł:** [11 — Termodynamika i teoria kinetyczna](README.md) · **Poziom:** 🔵 studia · **Status:** ✅ pełny
>
> **Czytaj:**
>
> - OpenStax, *Fizyka dla szkół wyższych*, t. 2, rozdz. 4: [§4.6–4.7](https://openstax.org/books/fizyka-dla-szk%C3%B3%C5%82-wy%C5%BCszych-tom-2/pages/4-6-entropia) · [wstęp do rozdziału](https://openstax.org/books/fizyka-dla-szk%C3%B3%C5%82-wy%C5%BCszych-tom-2/pages/4-wstep)
> - Halliday, Resnick, Walker, *Podstawy fizyki*, wyd. 2015, t. 2: §20.1 (s. 332), §20.4 (s. 352)
> - Halliday, Resnick, Walker, *Podstawy fizyki*, wyd. 1 (2003), t. 2: [§21.1–21.3, s. 260](https://home.agh.edu.pl/~czapli/Resnick_2.pdf#page=276), [§21.7, s. 276](https://home.agh.edu.pl/~czapli/Resnick_2.pdf#page=292) — PDF z serwera AGH

← [Silniki cieplne, chłodziarki i cykl Carnota](06-silniki-i-cykl-carnota.md) · [spis modułu](README.md) · (koniec modułu) →

## Po co to jest

Dlaczego kawa sama stygnie, a nigdy sama się nie podgrzewa? Dlaczego rozbite jajko się nie składa, choć zasada zachowania energii by na to pozwalała? Odpowiedzią jest entropia. To wielkość, która w układzie izolowanym nigdy nie maleje, i wyznacza kierunek procesów, czyli „strzałkę czasu”. Z niej wynika ograniczenie sprawności silników (11.06). W ujęciu statystycznym (Boltzmann) entropia mierzy liczbę mikroskopowych sposobów realizacji stanu, co łączy termodynamikę z teorią informacji i fizyką statystyczną.

## Teoria w pigułce

**Procesy odwracalne i nieodwracalne.** Proces odwracalny przebiega przez stany równowagi i można go cofnąć bez śladu w otoczeniu. To idealizacja. Wszystkie procesy rzeczywiste są nieodwracalne, na przykład:
- tarcie;
- przepływ ciepła przy skończonej różnicy temperatur;
- rozprężanie swobodne;
- mieszanie.

**Entropia (definicja Clausiusa):**

$$dS = \frac{dQ_{\text{odwr}}}{T}, \qquad \Delta S = \int_1^2\frac{dQ_{\text{odwr}}}{T}.$$

Entropia jest **funkcją stanu**. Dla procesu nieodwracalnego zmianę entropii liczy się po dowolnej **odwracalnej** drodze między tymi samymi stanami.

**Typowe zmiany entropii:**

| Proces | $\Delta S$ |
|---|---|
| ogrzewanie ($c$ stałe) | $mc\ln(T_2/T_1)$ |
| przemiana fazowa | $mL/T$ |
| gaz doskonały, izotermicznie | $nR\ln(V_2/V_1)$ |
| gaz doskonały, ogólnie | $nC_V\ln(T_2/T_1) + nR\ln(V_2/V_1)$ |
| rozprężanie swobodne (do próżni) | $nR\ln(V_2/V_1)$, choć $Q = 0$ |
| odwracalna adiabata | 0 |

**Druga zasada termodynamiki w ujęciu entropii:** w układzie izolowanym

$$\Delta S \ge 0.$$

Równość zachodzi tylko dla procesów odwracalnych. Entropia ciała może zmaleć (chłodzenie), ale wtedy entropia otoczenia rośnie co najmniej o tyle samo. Dla ciepła $Q$ płynącego z $T_H$ do $T_C$:

$$\Delta S = -\frac{Q}{T_H} + \frac{Q}{T_C} > 0 \quad\Leftrightarrow\quad T_H > T_C.$$

To jest sformułowanie Clausiusa. Z $\Delta S \ge 0$ dla silnika ($-Q_H/T_H + Q_C/T_C \ge 0$) wynika $\eta \le 1 - T_C/T_H$, czyli twierdzenie Carnota.

**Interpretacja statystyczna (Boltzmann).** Makrostan (np. „gaz wypełnia cały pojemnik”) można zrealizować na $\Omega$ sposobów (mikrostanów):

$$S = k\ln\Omega.$$

Układ samorzutnie zmierza do makrostanu o największej liczbie mikrostanów, bo jest on przytłaczająco najbardziej prawdopodobny. Przykład: szansa, że wszystkie $N$ cząsteczek zbierze się w połowie pojemnika, wynosi $2^{-N}$. Dla $N = 100$ to $10^{-30}$, dla mola gazu w praktyce zero. Gdy $N$ cząsteczek dostaje dwa razy więcej miejsca, $\Omega$ rośnie $2^N$ razy, więc $\Delta S = Nk\ln2$. Dla mola to $R\ln2$, zgodnie ze wzorem Clausiusa.

**Trzecia zasada:** entropia kryształu doskonałego dąży do zera, gdy $T \to 0$. Zera bezwzględnego nie da się osiągnąć w skończonej liczbie kroków.

## Wzory i założenia

| Wzór | Znaczenie | Kiedy obowiązuje |
|---|---|---|
| $\Delta S = \int dQ_{\text{odwr}}/T$ | definicja entropii | droga odwracalna |
| $\Delta S = mc\ln(T_2/T_1)$ | ogrzewanie | $c$ stałe |
| $\Delta S = mL/T$ | przemiana fazowa | stała $T$ |
| $\Delta S = nC_V\ln\frac{T_2}{T_1} + nR\ln\frac{V_2}{V_1}$ | gaz doskonały | dowolna przemiana |
| $\Delta S_{\text{izol}} \ge 0$ | II zasada termodynamiki | układ izolowany |
| $S = k\ln\Omega$ | entropia statystyczna | — |

## Przykład rozwiązany

**Zadanie 1.** Wymieszano 1 kg wody o temperaturze 80°C z 1 kg wody o temperaturze 20°C. Temperatura końcowa wynosi 50°C. Oblicz zmianę entropii.

Każdą część ogrzewamy lub chłodzimy w myśli odwracalnie:

$$\Delta S = 4190\left(\ln\frac{323}{353} + \ln\frac{323}{293}\right) = 4190(-0{,}0888 + 0{,}0975) \approx +36\ \mathrm{J/K}.$$

Gorąca woda traci entropię, ale zimna zyskuje więcej. Wynik jest dodatni, więc proces jest nieodwracalny.

**Zadanie 2.** Kostka lodu o masie 1 kg topnieje w pokoju o temperaturze 20°C. Oblicz zmianę entropii lodu, pokoju i całości.

Lód: $+334\,000/273{,}15 \approx +1223\ \mathrm{J/K}$. Pokój: $-334\,000/293{,}15 \approx -1139\ \mathrm{J/K}$. Razem ok. $+83\ \mathrm{J/K} > 0$. Pomijamy tu dalsze ogrzewanie wody z lodu.

### Wersja z rachunkiem różniczkowym i całkowym

**Zadanie.** Jeden mol gazu doskonałego rozpręża się swobodnie do próżni, podwajając objętość. Oblicz zmianę entropii, choć $Q = 0$, i wyjaśnij, dlaczego nie wynosi zero.

Rozprężanie swobodne jest nieodwracalne, ale stan końcowy jest taki sam jak po izotermicznym rozprężeniu odwracalnym ($T$ się nie zmienia, bo $W = 0$ i $Q = 0$, więc $\Delta U = 0$). Po tej drodze:

$$\Delta S = \int\frac{dQ}{T} = \int_V^{2V}\frac{p\,dV'}{T} = nR\ln2 \approx 5{,}76\ \mathrm{J/K}.$$

Wzór $\Delta S = \int dQ/T$ wolno stosować tylko po drodze odwracalnej. W samym rozprężaniu swobodnym $\int dQ/T = 0 < \Delta S$, co jest przykładem **nierówności Clausiusa**.

## Typowe pułapki

- **Entropia zawsze rośnie.** Rośnie entropia układu **izolowanego**. Entropia lodówki czy żywego organizmu może maleć kosztem otoczenia.
- **$\Delta S = Q/T$ dla każdego procesu.** Tylko dla odwracalnego w stałej temperaturze. Przy zmiennej $T$ trzeba całkować.
- **Przy rozprężaniu swobodnym $\Delta S = 0$, bo $Q = 0$.** Entropia to funkcja stanu, więc trzeba ją liczyć po drodze odwracalnej.
- **Entropia = nieporządek.** To potoczna metafora. Ściśle entropia to logarytm liczby mikrostanów. „Porządek” bywa mylący (np. kryształy rosnące w roztworze).
- **Temperatura w stopniach Celsjusza w $Q/T$.** Trzeba używać kelwinów.

## Doświadczenie / symulacja

**Mieszanie barwnika.** Kropla atramentu w szklance wody rozpływa się samorzutnie i nigdy się z powrotem nie skupia. Sfilmuj to i puść film od tyłu: od razu widać, który kierunek jest „fizyczny”. To ilustracja strzałki czasu.

**Model urnowy Ehrenfestów (Python).** $N$ cząsteczek w dwóch połówkach pojemnika. W każdym kroku losowa cząsteczka przeskakuje na drugą stronę. Startujemy ze wszystkimi po lewej. Entropia $S/k = \ln\binom{N}{n}$ rośnie do maksimum i dalej tylko się wokół niego waha, tym mniej, im większe $N$.

```python
import numpy as np
import matplotlib.pyplot as plt
from scipy.special import gammaln

rng = np.random.default_rng(1)
def ehrenfest(N, kroki):
    lewa = N; hist = [lewa]
    for _ in range(kroki):
        lewa += -1 if rng.random() < lewa/N else 1   # losowa cząsteczka zmienia stronę
        hist.append(lewa)
    return np.array(hist)

for N in (20, 200, 2000):
    n = ehrenfest(N, 6*N)
    S = gammaln(N + 1) - gammaln(n + 1) - gammaln(N - n + 1)      # ln C(N, n)
    plt.plot(np.arange(n.size)/N, S/(N*np.log(2)), label=f"N = {N}")
    print(f"N = {N:4d}: końcowy ułamek po lewej {n[-1]/N:.3f}, S/S_max = {S[-1]/(N*np.log(2)):.3f}")

c = 4190
print(f"mieszanie wody 80 + 20 °C: ΔS = {c*(np.log(323.15/353.15) + np.log(323.15/293.15)):.1f} J/K")
print(f"topnienie 1 kg lodu w 20 °C: ΔS = {334e3/273.15 - 334e3/293.15:.0f} J/K")
plt.xlabel("kroki / N"); plt.ylabel("S / (N k ln 2)"); plt.grid(True); plt.legend(); plt.show()
```

## Zadania

### A. Poziom maturalny _(opcjonalnie — rozgrzewka)_

1. Ciepło 1000 J przepływa z ciała o temperaturze 400 K do ciała o temperaturze 300 K. Oblicz zmianę entropii każdego ciała i całości.

<details>
<summary>Odpowiedź</summary>

$-2{,}50\ \mathrm{J/K}$ i $+3{,}33\ \mathrm{J/K}$, razem $+0{,}83\ \mathrm{J/K}$.
</details>

2. Rzucamy 100 monetami. Ile wynosi prawdopodobieństwo, że wypadną same orły? Co to mówi o samorzutnym zebraniu się powietrza w jednej połowie pokoju?

<details>
<summary>Odpowiedź</summary>

$2^{-100} \approx 8\cdot10^{-31}$. Dla $10^{27}$ cząsteczek w pokoju prawdopodobieństwo $2^{-10^{27}}$ jest praktycznie zerowe.
</details>

### B. Poziom akademicki

1. Oblicz zmianę entropii 1 kg wody ogrzanej od 20°C do 80°C. Porównaj z (błędnym) $Q/T_{\text{śr}}$.

<details>
<summary>Odpowiedź</summary>

$\Delta S = 4190\ln(353/293) \approx 781\ \mathrm{J/K}$. Wzór $Q/T_{\text{śr}} = 251\,400/323 \approx 778\ \mathrm{J/K}$ daje wynik bliski, ale tylko przybliżony.
</details>

2. Samochód o masie 1500 kg hamuje z 72 km/h do zera. Energia zamienia się w ciepło w otoczeniu o temperaturze 300 K. Oblicz przyrost entropii.

<details>
<summary>Odpowiedź</summary>

$Q = \tfrac12\cdot1500\cdot20^2 = 300\ \mathrm{kJ}$, $\Delta S = Q/T = 1000\ \mathrm{J/K}$.
</details>

3. Wykaż z II zasady, że sprawność dowolnego silnika pracującego między $T_H$ i $T_C$ nie przekracza $1 - T_C/T_H$.

<details>
<summary>Odpowiedź</summary>

W cyklu entropia silnika się nie zmienia. Zbiorniki zmieniają entropię o $-Q_H/T_H + Q_C/T_C \ge 0$, więc $Q_C/Q_H \ge T_C/T_H$ i $\eta = 1 - Q_C/Q_H \le 1 - T_C/T_H$.
</details>

4. Pokaż, że w przemianie adiabatycznej odwracalnej gazu doskonałego $\Delta S = 0$, korzystając z ogólnego wzoru na $\Delta S$ i równania $TV^{\gamma - 1} = \text{const}$.

<details>
<summary>Odpowiedź</summary>

$\Delta S = nC_V\ln\dfrac{T_2}{T_1} + nR\ln\dfrac{V_2}{V_1} = nC_V(1 - \gamma)\ln\dfrac{V_2}{V_1} + nR\ln\dfrac{V_2}{V_1} = 0$, bo $C_V(\gamma - 1) = R$.
</details>

5. Ziemia otrzymuje energię ze Słońca w postaci promieniowania o temperaturze ok. 5800 K i wypromieniowuje ją w ok. 255 K. Ile entropii na każdy dżul eksportuje Ziemia? Dlaczego to ważne dla życia?

<details>
<summary>Odpowiedź</summary>

W przybliżeniu $1/255 - 1/5800 \approx 3{,}7\cdot10^{-3}\ \mathrm{J/K}$ na dżul (dokładnie dla promieniowania jest czynnik 4/3). Ten strumień entropii na zewnątrz pozwala lokalnie tworzyć uporządkowane struktury, takie jak organizmy, bez łamania II zasady.
</details>

## Źródła

- OpenStax, *Fizyka dla szkół wyższych*, t. 2, rozdz. 4 — §4.6 (entropia) i §4.7 (entropia w skali mikroskopowej).
- Halliday, Resnick, Walker, *Podstawy fizyki* — wyd. 2015: t. 2, §20.1, §20.4; wyd. 1: t. 2, §21.1–21.3, §21.7.
