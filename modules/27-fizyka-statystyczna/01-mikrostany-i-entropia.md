# 27.01 — Mikrostany, makrostany i entropia Boltzmanna

> **Moduł:** [27 — Fizyka statystyczna](README.md) · **Poziom:** 🔵 studia · **Status:** ✅ pełny
>
> **Czytaj:**
>
> - OpenStax, *Fizyka dla szkół wyższych*, t. 2, rozdz. 4: [§4.7](https://openstax.org/books/fizyka-dla-szk%C3%B3%C5%82-wy%C5%BCszych-tom-2/pages/4-7-entropia-w-skali-mikroskopowej) · [wstęp do rozdziału](https://openstax.org/books/fizyka-dla-szk%C3%B3%C5%82-wy%C5%BCszych-tom-2/pages/4-wstep)
> - Halliday, Resnick, Walker, *Podstawy fizyki*, wyd. 2015, t. 2: §20.4 (s. 352)
> - Halliday, Resnick, Walker, *Podstawy fizyki*, wyd. 1 (2003), t. 2: [§21.7, s. 276](https://home.agh.edu.pl/~czapli/Resnick_2.pdf#page=292) — PDF z serwera AGH

← (początek modułu) · [spis modułu](README.md) · [Rozkład Boltzmanna i suma statystyczna](02-rozklad-boltzmanna.md) →

## Po co to jest

Termodynamika (11) mówi, **że** entropia układu izolowanego rośnie, ale nie mówi **dlaczego**. Odpowiedź Boltzmanna jest zaskakująco prosta: układ przechodzi do stanów, które można zrealizować na najwięcej sposobów, bo jest ich przytłaczająco więcej. Entropia to logarytm liczby takich sposobów. Ten pomysł tłumaczy nieodwracalność (gaz nigdy sam nie zbierze się w połowie pojemnika), definiuje temperaturę od podstaw i jest punktem wyjścia całej fizyki statystycznej, teorii informacji i współczesnej fizyki materiałów.

## Teoria w pigułce

**Mikrostan i makrostan.** **Makrostan** to opis „z zewnątrz”: energia, objętość, liczba cząstek, ciśnienie. **Mikrostan** to pełny opis wszystkich cząstek (położenia, pędy albo stany kwantowe). Jednemu makrostanowi odpowiada ogromnie wiele mikrostanów. Ich liczbę $\Omega$ nazywamy **wagą statystyczną** makrostanu.

**Przykład: rzut monetami.** Przy $N$ monetach makrostan „$n$ orłów” można zrealizować na $\Omega(n) = \binom Nn$ sposobów. Dla $N = 100$ układ 50 orłów ma $10^{29}$ realizacji, a 100 orłów — jedną.

**Podstawowe założenie fizyki statystycznej.** W układzie izolowanym w równowadze **każdy dostępny mikrostan jest jednakowo prawdopodobny**. Wtedy prawdopodobieństwo makrostanu jest proporcjonalne do $\Omega$. Dla dużych $N$ rozkład jest tak ostry, że praktycznie zawsze obserwujemy makrostan o największym $\Omega$ — to jest **stan równowagi**.

**Entropia Boltzmanna:**

$$S = k\ln\Omega.$$

Logarytm sprawia, że entropia jest addytywna: dla dwóch niezależnych układów $\Omega = \Omega_1\Omega_2$, więc $S = S_1 + S_2$.

**II zasada termodynamiki** (11.07) w tym języku: układ izolowany przechodzi do makrostanów o większym $\Omega$, bo jest ich nieporównanie więcej. Spadek entropii nie jest zabroniony, tylko skrajnie nieprawdopodobny. Szansa, że $N$ cząsteczek gazu zbierze się w jednej połowie pojemnika, to $2^{-N}$: dla 100 cząsteczek $8\cdot10^{-31}$, dla mola — $10^{-1{,}8\cdot10^{23}}$.

**Rozprężanie swobodne.** Gaz z $N$ cząsteczkami rozpręża się do dwa razy większej objętości. Każda cząsteczka ma dwa razy więcej miejsc, więc $\Omega$ rośnie $2^N$ razy, a $\Delta S = Nk\ln2$. Dla mola $\Delta S = R\ln2 = 5{,}76\ \mathrm{J/K}$ — dokładnie tyle, ile daje termodynamika ($\Delta S = nR\ln(V_2/V_1)$, 11.07).

**Temperatura z entropii.** Dwa układy wymieniające energię osiągają równowagę, gdy całkowite $\Omega_A\Omega_B$ (czyli $S_A + S_B$) jest największe. Warunek maksimum przy stałej całkowitej energii: $\dfrac{\partial S_A}{\partial U_A} = \dfrac{\partial S_B}{\partial U_B}$. Ta wspólna wielkość to odwrotność temperatury:

$$\frac1T = \frac{\partial S}{\partial U}.$$

Ciepło płynie od układu, którego entropia mniej rośnie przy dodaniu energii (gorącego), do tego, którego rośnie bardziej (zimnego), bo wtedy łączna entropia rośnie.

**Model kryształu Einsteina.** $N$ oscylatorów kwantowych (20.06), z których każdy może mieć $0, 1, 2, \dots$ kwantów energii $\hbar\omega$. Liczba sposobów rozdzielenia $q$ kwantów między $N$ oscylatorów:

$$\Omega(N, q) = \binom{q + N - 1}{q}.$$

To prosty model ciała stałego, na którym można policzyć wszystko dokładnie.

## Wzory i założenia

| Wzór | Znaczenie | Kiedy obowiązuje |
|---|---|---|
| $S = k\ln\Omega$ | entropia Boltzmanna | układ izolowany, mikrostany jednakowo prawdopodobne |
| $\Omega = \binom Nn = \dfrac{N!}{n!(N - n)!}$ | układy dwustanowe (monety, spiny) | — |
| $\Omega = \binom{q + N - 1}{q}$ | kryształ Einsteina | $q$ kwantów na $N$ oscylatorach |
| $\Delta S = Nk\ln(V_2/V_1)$ | rozprężanie gazu doskonałego | stała energia |
| $1/T = \partial S/\partial U$ | definicja temperatury | stałe $V$ i $N$ |
| $\ln N! \approx N\ln N - N$ | wzór Stirlinga | $N \gg 1$ |

## Przykład rozwiązany

**Zadanie 1.** W pojemniku jest 4 cząsteczki. Wypisz makrostany (liczba cząsteczek w lewej połowie) i ich wagi. Jakie jest prawdopodobieństwo, że wszystkie są w lewej połowie?

$\Omega(0..4) = 1, 4, 6, 4, 1$, łącznie $2^4 = 16$. $P(4) = 1/16$. Najbardziej prawdopodobny jest podział 2:2 (6/16).

**Zadanie 2.** Dwa kryształy Einsteina, A ($N_A = 300$) i B ($N_B = 200$), dzielą $q = 100$ kwantów energii. Jaki podział jest najbardziej prawdopodobny?

Liczba mikrostanów układu przy $q_A$ kwantach w A: $\Omega_A(q_A)\Omega_B(100 - q_A)$. Maksimum (rachunek w Pythonie poniżej) przypada na $q_A = 60$, czyli energia dzieli się proporcjonalnie do liczby oscylatorów. Odchylenie standardowe to ok. 5 kwantów — przy $10^{23}$ oscylatorach względne fluktuacje są rzędu $10^{-11}$, czyli niezauważalne.

### Wersja z rachunkiem różniczkowym i całkowym

**Temperatura kryształu Einsteina.** Dla $q, N \gg 1$ ze wzoru Stirlinga:

$$S = k\ln\binom{q + N}{q} \approx k\left[(q + N)\ln(q + N) - q\ln q - N\ln N\right].$$

Energia $U = q\hbar\omega$, więc

$$\frac1T = \frac{\partial S}{\partial U} = \frac{k}{\hbar\omega}\ln\frac{q + N}{q} \Rightarrow \frac UN = \frac{\hbar\omega}{e^{\hbar\omega/kT} - 1}.$$

To średnia energia oscylatora kwantowego, którą Planck wprowadził przy promieniowaniu ciała doskonale czarnego (20.01). W wysokiej temperaturze ($kT \gg \hbar\omega$) daje $U/N \approx kT$ (ekwipartycja, 27.03).

**Rozprężanie gazu.** Liczba mikrostanów gazu doskonałego jest proporcjonalna do $V^N$ (każda cząsteczka niezależnie zajmuje objętość). $S = Nk\ln V + \text{const}$, więc $\left(\dfrac{\partial S}{\partial V}\right)_U = \dfrac{Nk}{V}$. Z termodynamiki $dS = \dfrac{dU + p\,dV}{T}$, czyli $\dfrac pT = \dfrac{Nk}V$ — równanie stanu gazu doskonałego $pV = NkT$ wynika z samego liczenia mikrostanów.

## Typowe pułapki

- **Entropia to „nieporządek”.** To mylące uproszczenie. Entropia to miara liczby mikrostanów zgodnych z makrostanem. Np. kryształy tworzą się samorzutnie, bo przy krystalizacji wydziela się ciepło i entropia otoczenia rośnie bardziej, niż maleje entropia kryształu.
- **II zasada jest absolutnym zakazem.** Jest prawem statystycznym. Dla kilku cząsteczek spadki entropii zdarzają się często, dla makroskopowych układów — nigdy w praktyce.
- **Wszystkie makrostany są jednakowo prawdopodobne.** Jednakowo prawdopodobne są mikrostany. Makrostany różnią się wagami o wiele rzędów wielkości.
- **$\Omega$ i $S$ zależą od tego, jak policzymy stany.** Stała addytywna w $S$ zależy od umowy, ale zmiany entropii (to, co mierzymy) — nie.

## Doświadczenie / symulacja

**Monety.** Rzuć 10 monetami 50 razy i zapisz liczbę orłów. Porównaj histogram z rozkładem $\binom{10}n/2^{10}$. Jak często wypadło 10 orłów (oczekiwanie: raz na 1024 rzuty)?

**Symulacja PhET:** *Właściwości gazu* — zamknij gaz w jednej części pojemnika i otwórz przegrodę. Obserwuj, czy cząsteczki kiedykolwiek wracają wszystkie na jedną stronę ([phet.colorado.edu/pl](https://phet.colorado.edu/pl/)).

**Python:** wagi statystyczne dwóch kryształów Einsteina wymieniających energię, ostrość rozkładu w funkcji liczby oscylatorów, temperatura z $1/T = \partial S/\partial U$ i entropia rozprężania.

```python
import numpy as np
import matplotlib.pyplot as plt
from scipy.special import gammaln

lnOmega = lambda q, N: gammaln(q + N) - gammaln(q + 1) - gammaln(N)       # ln C(q+N-1, q)

for skala in (1, 10, 100, 1000):
    NA, NB, q = 300*skala, 200*skala, 100*skala
    qa = np.arange(q + 1)
    lnW = lnOmega(qa, NA) + lnOmega(q - qa, NB)
    p = np.exp(lnW - lnW.max()); p /= p.sum()
    sr = (p*qa).sum(); sd = np.sqrt((p*qa**2).sum() - sr**2)
    print(f"N_A = {NA:6d}, N_B = {NB:6d}, q = {q:6d}: najbardziej prawdopodobne q_A = {qa[np.argmax(p)]}, "
          f"względna szerokość σ/q_A = {sd/sr:.4f}")
    if skala == 1:
        plt.plot(qa, p, "o-", ms=3, label="N_A = 300, N_B = 200, q = 100")

# temperatura z entropii: kT/ħω = 1 / (dS/dq) dla kryształu Einsteina N = 1000
N, q = 1000, np.arange(1, 5000)
S = lnOmega(q, N)                                  # S/k
kT = 1/np.gradient(S, q)                           # w jednostkach ħω
U_teoria = 1/np.expm1(1/kT)                        # średnia energia oscylatora (Planck)
print(f"sprawdzenie U/N = 1/(e^(ħω/kT) − 1): maks. różnica {np.max(np.abs(q/N - U_teoria)[10:]):.4f}")
print(f"rozprężanie 1 mola do 2V: ΔS = R ln 2 = {8.314462618*np.log(2):.3f} J/K; P(N = 100 w jednej połowie) = {2.0**-100:.1e}")

plt.xlabel("q_A (kwanty w krysztale A)"); plt.ylabel("prawdopodobieństwo"); plt.legend(); plt.grid(True); plt.show()
```

## Zadania

### A. Poziom maturalny _(opcjonalnie — rozgrzewka)_

1. Rzucamy 6 monetami. Ile mikrostanów ma makrostan „3 orły”, a ile „6 orłów”? Które jest bardziej prawdopodobne i ile razy?

<details>
<summary>Odpowiedź</summary>

$\binom63 = 20$ i $\binom66 = 1$. Trzy orły są 20 razy bardziej prawdopodobne.
</details>

2. Dlaczego zapach perfum rozchodzi się po pokoju, ale nigdy sam nie wraca do flakonu?

<details>
<summary>Odpowiedź</summary>

Stanów, w których cząsteczki są rozproszone w całym pokoju, jest nieporównanie więcej niż stanów z cząsteczkami we flakonie. Powrót nie jest zabroniony, ale jego prawdopodobieństwo jest praktycznie zerowe.
</details>

### B. Poziom akademicki

1. Oblicz zmianę entropii przy rozprężeniu swobodnym 2 moli gazu doskonałego od 10 do 30 litrów: (a) termodynamicznie, (b) z liczenia mikrostanów.

<details>
<summary>Odpowiedź</summary>

(a) $\Delta S = nR\ln3 = 2\cdot8{,}31\cdot1{,}099 \approx 18{,}3\ \mathrm{J/K}$. (b) $\Omega$ rośnie $3^N$ razy, $\Delta S = Nk\ln3 = nR\ln3$ — ten sam wynik.
</details>

2. Pokaż ze wzoru Stirlinga, że dla $N$ monet $\ln\binom{N}{N/2} \approx N\ln2$. Ile razy więcej mikrostanów ma makrostan 50:50 niż 100:0 dla $N = 100$ (dokładnie i z przybliżenia)?

<details>
<summary>Odpowiedź</summary>

$\ln\dfrac{N!}{((N/2)!)^2} \approx N\ln N - N - 2\left(\dfrac N2\ln\dfrac N2 - \dfrac N2\right) = N\ln2$. Dokładnie $\binom{100}{50} \approx 1{,}01\cdot10^{29}$, przybliżenie $2^{100} \approx 1{,}27\cdot10^{30}$ (różnica o czynnik ok. $\sqrt{\pi N/2}$, pominięty w prostym wzorze Stirlinga).
</details>

3. Uruchom kod. Jak względna szerokość rozkładu zależy od liczby oscylatorów? Oszacuj ją dla $10^{23}$ oscylatorów.

<details>
<summary>Odpowiedź</summary>

Maleje jak $1/\sqrt N$ (ok. 0,089 dla $N = 500$, ok. 0,0028 dla $N = 500\,000$). Dla $10^{23}$: rzędu $10^{-11}$ — fluktuacje energii są niemierzalne.
</details>

4. Układ ma $N$ spinów, każdy w stanie o energii $0$ lub $\varepsilon$. Z $S = k\ln\binom Nn$ wyprowadź temperaturę jako funkcję liczby wzbudzonych spinów $n$. Co się dzieje dla $n > N/2$?

<details>
<summary>Odpowiedź</summary>

$\dfrac1T = \dfrac{1}{\varepsilon}\dfrac{dS}{dn} = \dfrac k\varepsilon\ln\dfrac{N - n}{n}$. Dla $n > N/2$ logarytm jest ujemny, więc $T < 0$ — **temperatura ujemna** (inwersja obsadzeń, jak w laserze, 21.06). Taki układ jest „gorętszy” od każdego układu o dodatniej temperaturze.
</details>

## Źródła

- OpenStax, *Fizyka dla szkół wyższych*, t. 2, rozdz. 4 — §4.7: entropia w skali mikroskopowej.
- Halliday, Resnick, Walker, *Podstawy fizyki* — wyd. 2015: t. 2, §20.4 (statystyczne spojrzenie na entropię); wyd. 1: t. 2, §21.7.
- F. Reif, *Fizyka statystyczna* (Kurs Fizyki Berkeley, t. 5), PWN — klasyczny podręcznik na poziomie pierwszych lat studiów.
- K. Huang, *Podstawy fizyki statystycznej*, PWN — wykład akademicki.
- Moduł 11.07 (entropia i II zasada termodynamiki).
- Symulacja PhET *Właściwości gazu*.
