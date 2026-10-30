# 25.06 — Metody Monte Carlo: rozpad, błądzenie losowe, całkowanie

> **Moduł:** [25 — Fizyka obliczeniowa w Pythonie](README.md) · **Poziom:** 🔵 studia · **Status:** ✅ pełny
>
> **Czytaj:**
>
> - _Podręczniki główne nie mają osobnego paragrafu na ten temat — materiały są w sekcji „Źródła”._

← [Pola i potencjały na siatce — równanie Laplace'a](05-pola-na-siatce.md) · [spis modułu](README.md) · (koniec modułu) →

## Po co to jest

Wiele zjawisk jest losowych z natury: rozpad pojedynczego jądra, ruchy Browna, droga fotonu ze środka Słońca, zliczenia licznika Geigera. Inne są deterministyczne, ale tak złożone, że łatwiej je „zagrać” losowo, np. całki w wielu wymiarach, transport neutronów w reaktorze, dawka w radioterapii. Metody Monte Carlo (nazwa od kasyna; rozwinięte w Los Alamos w latach 40.) zastępują rachunek wielokrotnym losowaniem. Ich ogromną zaletą jest prostota, a niepewność wyniku maleje jak $1/\sqrt N$ — niezależnie od liczby wymiarów.

## Teoria w pigułce

**Liczby losowe.** Komputer generuje liczby **pseudolosowe** deterministycznym algorytmem, ale o dobrych własnościach statystycznych. W NumPy: `rng = np.random.default_rng(ziarno)`, potem `rng.random(n)` (rozkład jednostajny na [0, 1)), `rng.normal(mu, sigma, n)`, `rng.poisson(lam, n)`, `rng.binomial(n, p)`. Ustalone ziarno daje powtarzalne wyniki.

**1. Rozpad promieniotwórczy** (22.03). Każde jądro w czasie $\Delta t$ rozpada się z prawdopodobieństwem $p = 1 - e^{-\lambda\Delta t} \approx \lambda\Delta t$, niezależnie od innych i od swojego „wieku”. Symulacja: w każdym kroku losujemy, które jądra się rozpadły (albo od razu liczbę rozpadów z rozkładu dwumianowego). Średnio dostajemy $N_0e^{-\lambda t}$, ale z fluktuacjami rzędu $\sqrt N$. Liczba zliczeń w ustalonym czasie ma **rozkład Poissona**: średnia $\mu$, odchylenie standardowe $\sqrt\mu$.

**2. Błądzenie losowe i dyfuzja.** Cząstka wykonuje $N$ kroków długości $l$ w losowych kierunkach. Średnie przesunięcie jest zerowe, ale średni kwadrat przesunięcia rośnie liniowo z liczbą kroków:

$$\langle r^2\rangle = Nl^2 \Rightarrow r_{\text{sk}} = l\sqrt N.$$

Ponieważ $N \propto t$, dostajemy prawo dyfuzji $\langle x^2\rangle = 2Dt$ (w jednym wymiarze). Einstein (1905) połączył współczynnik dyfuzji cząstki Browna z temperaturą: $D = \dfrac{kT}{6\pi\eta r}$. Pomiary Perrina (1908) dały z tego stałą Avogadra i ostatecznie przekonały fizyków o istnieniu atomów. Ten sam model opisuje przewodnictwo ciepła (11.03) i wędrówkę fotonu ze środka Słońca (dziesiątki do setek tysięcy lat zamiast 2 sekund lotu po prostej).

**3. Całkowanie Monte Carlo.** Średnia wartość funkcji w losowych punktach razy objętość obszaru przybliża całkę:

$$\int_Vf\,dV \approx V\cdot\frac1N\sum_{i=1}^Nf(\vec x_i), \qquad u = V\frac{\sigma_f}{\sqrt N}.$$

Wariant „trafień”: losujemy punkty w prostokącie i liczymy ułamek, który trafił pod wykres (lub do koła — szacowanie $\pi$). W jednym wymiarze to metoda gorsza od Simpsona (25.01), ale w 10 wymiarach siatka 10 punktów na oś to już $10^{10}$ punktów, a Monte Carlo wystarcza $10^6$ losowań dla dokładności na poziomie procentów.

## Wzory i założenia

| Wzór | Znaczenie | Kiedy obowiązuje |
|---|---|---|
| $p = 1 - e^{-\lambda\Delta t}$ | prawdopodobieństwo rozpadu w kroku | jądra niezależne |
| $P(k) = \dfrac{\mu^ke^{-\mu}}{k!}$, $\sigma = \sqrt\mu$ | rozkład Poissona | zdarzenia rzadkie i niezależne |
| $\langle r^2\rangle = Nl^2$ | błądzenie losowe | kroki niezależne |
| $\langle x^2\rangle = 2Dt$, $D = \dfrac{kT}{6\pi\eta r}$ | dyfuzja, ruchy Browna | kulka w cieczy |
| $\displaystyle\int_Vf \approx V\langle f\rangle$, $u = V\sigma_f/\sqrt N$ | całkowanie Monte Carlo | dowolny wymiar |

## Przykład rozwiązany

**Zadanie 1.** Ile wynosi typowa odległość od punktu startu po 1000 krokach o długości 1 m w losowych kierunkach?

$r_{\text{sk}} = \sqrt{1000} \approx 32\ \mathrm m$, choć przebyta droga to 1000 m.

**Zadanie 2.** Szacujemy $\pi$, losując $N = 10^6$ punktów w kwadracie $[0, 1]^2$ i licząc ułamek $f$ w ćwiartce koła: $\pi \approx 4f$. Jaka jest niepewność?

Każdy punkt trafia z prawdopodobieństwem $p = \pi/4$. Liczba trafień ma rozkład dwumianowy, więc $u(f) = \sqrt{p(1 - p)/N}$ i $u(\pi) = 4\sqrt{0{,}785\cdot0{,}215/10^6} \approx 0{,}0016$. Trzy poprawne cyfry z miliona losowań — Monte Carlo jest „wolne”, ale proste i odporne.

**Zadanie 3.** Kulka lateksowa o promieniu 0,5 μm w wodzie (20°C, $\eta = 10^{-3}\ \mathrm{Pa\cdot s}$). Oblicz współczynnik dyfuzji i średnie przesunięcie w jednym kierunku po minucie.

$D = \dfrac{kT}{6\pi\eta r} \approx 4{,}3\cdot10^{-13}\ \mathrm{m^2/s}$, $\sqrt{2Dt} \approx 7\ \mu\mathrm m$ — widoczne pod mikroskopem.

### Wersja z rachunkiem różniczkowym i całkowym

**Dlaczego $\langle r^2\rangle = Nl^2$.** Przesunięcie to suma kroków $\vec R = \sum\vec s_i$. Wtedy

$$\langle R^2\rangle = \sum_i\langle s_i^2\rangle + \sum_{i\ne j}\langle\vec s_i\cdot\vec s_j\rangle = Nl^2 + 0,$$

bo kierunki kolejnych kroków są niezależne i średnia iloczynu skalarnego znika.

**Dlaczego błąd Monte Carlo maleje jak $1/\sqrt N$.** Estymator $\hat I = \frac VN\sum f(\vec x_i)$ to średnia $N$ niezależnych zmiennych losowych o wariancji $V^2\sigma_f^2$, gdzie $\sigma_f^2 = \langle f^2\rangle - \langle f\rangle^2$. Wariancja średniej jest $N$ razy mniejsza:

$$\operatorname{Var}\hat I = \frac{V^2\sigma_f^2}{N} \Rightarrow u(\hat I) = \frac{V\sigma_f}{\sqrt N}.$$

Wymiar przestrzeni nie występuje we wzorze. Metoda siatkowa rzędu $h^k$ z $N$ punktami w $d$ wymiarach ma $h \sim N^{-1/d}$ i błąd $\sim N^{-k/d}$, więc dla $d > 2k$ przegrywa z Monte Carlo.

**Przykład:** $\int_0^1e^{-x^2}dx = 0{,}7468$, $\sigma_f^2 = \int_0^1e^{-2x^2}dx - 0{,}7468^2 \approx 0{,}0404$, więc przy $N = 10^4$: $u \approx 0{,}201/100 \approx 0{,}002$.

## Typowe pułapki

- **Ta sama liczba losowa użyta dwa razy** albo stałe ziarno przy porównywaniu „niezależnych” przebiegów. Wyniki są wtedy skorelowane.
- **Mylenie średniej z odchyleniem.** Średnie przesunięcie w błądzeniu losowym wynosi zero. Rośnie średni kwadrat przesunięcia.
- **Za duży krok czasowy w symulacji rozpadu.** Przy $\lambda\Delta t$ rzędu 1 przybliżenie $p \approx \lambda\Delta t$ się psuje (prawdopodobieństwo większe od 1!). Używaj $p = 1 - e^{-\lambda\Delta t}$ i małego kroku.
- **Brak niepewności wyniku.** Wynik Monte Carlo bez $\pm u$ jest bezwartościowy. Liczy się go z rozrzutu wartości albo z kilku niezależnych przebiegów.
- **Pętla po milionie elementów w Pythonie.** Losuj od razu całe tablice (`rng.random((N, d))`), a sumy licz funkcjami NumPy.

## Doświadczenie / symulacja

**Rozpad kostek do gry.** Rzuć 100 kostkami, usuń te, które pokazały „6”, rzucaj pozostałymi dalej. Zapisuj liczbę kostek po każdym rzucie. Okres połowicznego zaniku wynosi $\ln2/\ln(6/5) \approx 3{,}8$ rzutu. Porównaj z symulacją komputerową i zobacz, jak fluktuacje rosną względnie, gdy kostek zostaje mało.

**Statystyka zliczeń licznika Geigera.** Jeśli masz dostęp do licznika (pracownia szkolna lub aplikacja z modułem detektora), zmierz 100 razy liczbę zliczeń tła w 10 s i porównaj histogram z rozkładem Poissona.

**Python:** symulacja rozpadu z fluktuacjami, błądzenie losowe w 2D (sprawdzenie $\langle r^2\rangle = Nl^2$), szacowanie $\pi$ i objętości kuli w 10 wymiarach.

```python
import numpy as np
import matplotlib.pyplot as plt
from scipy.special import gamma

rng = np.random.default_rng(2024)
fig, ax = plt.subplots(1, 3, figsize=(14, 4))

lam, dt, N0 = 0.1, 0.1, 1000                                 # rozpad: λ [1/s], krok [s]
p = 1 - np.exp(-lam*dt)
for proba in range(5):
    N = [N0]
    for _ in range(500):
        N.append(N[-1] - rng.binomial(N[-1], p))
    t = np.arange(len(N))*dt
    ax[0].plot(t, N, lw=0.8)
    if proba == 0:
        print(f"rozpad: N(T1/2) = {N[int(round(np.log(2)/lam/dt))]} (średnio 500 ± {np.sqrt(250):.0f})")
ax[0].plot(t, N0*np.exp(-lam*t), "k--", label="N0·e^(−λt)"); ax[0].set_xlabel("t [s]"); ax[0].legend()

M, kroki = 2000, 1000                                        # błądzenie losowe w 2D, krok l = 1
phi = rng.uniform(0, 2*np.pi, (M, kroki))
x, y = np.cumsum(np.cos(phi), axis=1), np.cumsum(np.sin(phi), axis=1)
r2 = (x**2 + y**2).mean(axis=0)
print(f"błądzenie: <r²> po {kroki} krokach = {r2[-1]:.0f} (teoria {kroki}), r_sk = {np.sqrt(r2[-1]):.1f}")
ax[1].plot(x[0], y[0], lw=0.5); ax[1].plot(x[1], y[1], lw=0.5); ax[1].set_aspect("equal"); ax[1].set_title("dwa błądzenia losowe")

n = 10**6
pkt = rng.random((n, 2))
f = np.mean(np.sum(pkt**2, axis=1) < 1)
print(f"π ≈ {4*f:.4f} ± {4*np.sqrt(f*(1 - f)/n):.4f}")
for d in (2, 3, 5, 10):
    pkt = rng.uniform(-1, 1, (n, d))
    f = np.mean(np.sum(pkt**2, axis=1) < 1)
    Vmc, u = 2**d*f, 2**d*np.sqrt(f*(1 - f)/n)
    print(f"kula w {d:2d} wymiarach: V = {Vmc:.4f} ± {u:.4f} (dokładnie {np.pi**(d/2)/gamma(d/2 + 1):.4f})")

xs = rng.random(10**4)
fx = np.exp(-xs**2)
print(f"∫₀¹ exp(−x²) dx ≈ {fx.mean():.4f} ± {fx.std()/np.sqrt(xs.size):.4f} (dokładnie 0,7468)")
Ns = np.logspace(2, 6, 9).astype(int)
bledy = [abs(4*np.mean(np.sum(rng.random((k, 2))**2, axis=1) < 1) - np.pi) for k in Ns]
ax[2].loglog(Ns, bledy, "o", label="|błąd| szacowania π"); ax[2].loglog(Ns, 1.6/np.sqrt(Ns), "k--", label="1,6/√N")
ax[2].set_xlabel("N"); ax[2].legend()
plt.tight_layout(); plt.show()
```

## Zadania

### A. Poziom maturalny _(opcjonalnie — rozgrzewka)_

1. Rzucamy 100 razy monetą. Ile orłów spodziewamy się średnio i jaki jest typowy rozrzut wyniku?

<details>
<summary>Odpowiedź</summary>

Średnio 50, odchylenie standardowe $\sqrt{100\cdot0{,}5\cdot0{,}5} = 5$. Wyniki 45–55 są typowe, a 30 orłów byłoby bardzo podejrzane.
</details>

2. Licznik zarejestrował 400 zliczeń w ciągu minuty. Jaka jest niepewność tego wyniku? Ile zliczeń trzeba zebrać, żeby niepewność względna wynosiła 1%?

<details>
<summary>Odpowiedź</summary>

$u = \sqrt{400} = 20$ (5%). Dla 1%: $1/\sqrt N = 0{,}01 \Rightarrow N = 10\,000$ zliczeń.
</details>

### B. Poziom akademicki

1. Wyprowadź okres połowicznego zaniku w modelu kostek do gry (usuwamy „szóstki”) i sprawdź go symulacją dla 1000 kostek.

<details>
<summary>Odpowiedź</summary>

Po $n$ rzutach zostaje $N_0(5/6)^n$. Połowa: $n = \ln2/\ln(6/5) \approx 3{,}8$ rzutu. Symulacja: `N -= rng.binomial(N, 1/6)` w pętli.
</details>

2. Oszacuj metodą Monte Carlo objętość kuli jednostkowej w 10 wymiarach, losując $10^6$ punktów w kostce $[-1, 1]^{10}$. Jaka jest niepewność względna i dlaczego jest tak duża?

<details>
<summary>Odpowiedź</summary>

Dokładnie $\pi^5/120 \approx 2{,}550$. Tylko ułamek $2{,}55/1024 \approx 0{,}25\%$ punktów trafia do kuli, więc względna niepewność $\sqrt{(1 - f)/(fN)} \approx 2\%$. W dużych wymiarach prawie cała objętość kostki leży w narożach poza kulą. Lepsze jest losowanie z rozkładu dopasowanego do problemu (*importance sampling*).
</details>

3. Foton w Słońcu przebywa średnio ok. 1 mm między kolejnymi rozproszeniami. Promień Słońca to $7\cdot10^8$ m. Ile kroków i ile czasu potrzeba, żeby dotarł na powierzchnię (zakładając błądzenie losowe w 3D i stałą drogę swobodną)?

<details>
<summary>Odpowiedź</summary>

$N = (R/l)^2 \approx 5\cdot10^{23}$ kroków; czas $Nl/c \approx 5\cdot10^{23}\cdot10^{-3}/3\cdot10^8\ \mathrm s \approx 1{,}6\cdot10^{12}\ \mathrm s \approx 50\,000$ lat. Rzeczywista droga swobodna zmienia się z głębokością i szacunki dają od dziesiątek do setek tysięcy lat.
</details>

4. Napisz symulację, w której 10 000 cząstek startuje z $x = 0$ i co 1 ms wykonuje krok $\pm1\ \mu\mathrm m$. Wyznacz $D$ z wykresu $\langle x^2\rangle(t)$ i porównaj z $D = l^2/(2\Delta t)$.

<details>
<summary>Odpowiedź</summary>

`x = np.cumsum(rng.choice([-1, 1], (10000, n)), axis=1)`; nachylenie $\langle x^2\rangle(t)$ wynosi $2D$, więc $D = l^2/(2\Delta t) = 10^{-12}/(2\cdot10^{-3}) = 5\cdot10^{-10}\ \mathrm{m^2/s}$ (rząd dyfuzji małych cząsteczek w wodzie).
</details>

## Źródła

- OpenStax, *Fizyka dla szkół wyższych*, t. 3 — §10.3 (rozpad promieniotwórczy); t. 2 — §2.4 (rozkład prędkości cząsteczek, losowość ruchu cieplnego).
- B. Zglinicki, *Programowanie i metody numeryczne* (Wydział Fizyki UW) — [ćwiczenia 12: całkowanie Monte Carlo](https://www.fuw.edu.pl/~bzglinicki/teaching/pmn/cwiczenia/12/PMN_Cwiczenia-12.pdf), po polsku.
- Moduły 22.03 (prawo rozpadu), 11.04 (teoria kinetyczna gazów), 01.03 (niepewności).
- M. Newman, *Computational Physics*, rozdz. 10 (procesy losowe i metody Monte Carlo) — materiał dodatkowy, po angielsku.
