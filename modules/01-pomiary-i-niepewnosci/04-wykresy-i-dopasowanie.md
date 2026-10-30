# 01.04 — Wykresy, linearyzacja i dopasowanie prostej

> **Moduł:** [01 — Pomiar, jednostki i niepewności](README.md) · **Poziom:** 🟢🔵 matura R + studia · **Status:** ✅ pełny
>
> **Czytaj:**
>
> - _Podręczniki główne nie mają osobnego paragrafu na ten temat — materiały są w sekcji „Źródła”._

← [Niepewności pomiarowe: typ A, typ B, niepewność złożona](03-niepewnosci-pomiarowe.md) · [spis modułu](README.md) · [Planowanie doświadczenia i raport z pomiarów](05-doswiadczenie-i-raport.md) →

## Po co to jest

Jeden pomiar daje jedną liczbę; seria pomiarów przy różnych warunkach pozwala sprawdzić **prawo** i wyznaczyć stałą z całej serii naraz. Narzędziem jest wykres z niepewnościami i prosta dopasowana do punktów. Na maturze rozszerzonej to standardowe zadanie doświadczalne: narysuj wykres, poprowadź prostą, wyznacz nachylenie. Na studiach to samo robi się metodą najmniejszych kwadratów, z niepewnością parametrów.

## Teoria w pigułce

**Dobry wykres.**
- Na osi poziomej wielkość, którą ustawiamy (zmienna niezależna), na pionowej — mierzona.
- Każda oś ma opis wielkości i jednostkę: „$F$ [N]”.
- Skala dobrana tak, żeby punkty zajmowały większość wykresu; oś nie musi zaczynać się od zera.
- Punkty pomiarowe zaznaczone wyraźnie, z **odcinkami niepewności** (słupkami błędu) albo prostokątami niepewności.
- Linia trendu to prosta (lub krzywa modelu), a nie łamana łącząca punkty.

**Prosta „na oko” i proste skrajne (poziom maturalny).** Prowadzimy prostą, która przechodzi przez wszystkie prostokąty niepewności lub możliwie blisko nich, z punktami rozłożonymi po obu stronach. Nachylenie liczymy z dwóch odległych punktów **tej prostej**. Niepewność nachylenia można oszacować, prowadząc najbardziej i najmniej stromą prostą, która jeszcze mieści się w prostokątach niepewności: $u(a) \approx (a_{\max} - a_{\min})/2$.

**Metoda najmniejszych kwadratów (regresja liniowa).** Szukamy prostej $y = ax + b$, dla której suma kwadratów odchyleń punktów od prostej jest najmniejsza:

$$S(a, b) = \sum_{i=1}^n\left(y_i - ax_i - b\right)^2 \to \min.$$

Przyrównanie pochodnych $\partial S/\partial a$ i $\partial S/\partial b$ do zera daje wzory w tabeli poniżej. Metoda zakłada, że niepewność ma głównie $y$, a $x$ jest znane dokładnie.

**Reszty.** Różnice $y_i - (ax_i + b)$ to reszty. Jeśli model jest dobry, reszty są losowo rozrzucone wokół zera. Jeśli układają się w łuk — zależność nie jest liniowa i trzeba zmienić model albo zlinearyzować dane (temat 00.02).

## Wzory i założenia

Oznaczenie: $D = n\sum x_i^2 - \left(\sum x_i\right)^2$.

| Wzór | Znaczenie | Uwagi |
|---|---|---|
| $a = \dfrac{n\sum x_iy_i - \sum x_i\sum y_i}{D}$ | nachylenie | |
| $b = \dfrac{\sum y_i - a\sum x_i}{n}$ | wyraz wolny | prosta przechodzi przez punkt $(\bar{x}, \bar{y})$ |
| $s_y = \sqrt{\dfrac{\sum(y_i - ax_i - b)^2}{n - 2}}$ | rozrzut punktów wokół prostej | $n - 2$, bo wyznaczyliśmy dwa parametry |
| $u(a) = s_y\sqrt{\dfrac{n}{D}}$, $\ u(b) = s_y\sqrt{\dfrac{\sum x_i^2}{D}}$ | niepewności parametrów | gdy niepewności $y_i$ są podobne |
| $u(a) \approx \dfrac{a_{\max} - a_{\min}}{2}$ | z prostych skrajnych | metoda graficzna |

## Przykład rozwiązany

**Zadanie.** Na sprężynie wieszano ciężarki i mierzono jej wydłużenie $x$:

| $m$ [kg] | 0,05 | 0,10 | 0,15 | 0,20 | 0,25 | 0,30 |
|---|---|---|---|---|---|---|
| $F = mg$ [N] | 0,49 | 0,98 | 1,47 | 1,96 | 2,45 | 2,94 |
| $x$ [cm] | 2,1 | 4,0 | 6,2 | 7,9 | 10,1 | 12,0 |

Niepewność wydłużenia (linijka) wynosi ok. 1 mm. Wyznacz współczynnik sprężystości $k$ z prawa Hooke'a $F = kx$.

**Model i wykres.** Jeśli prawo Hooke'a działa, wykres $F(x)$ jest prostą przez początek układu o nachyleniu $k$. Odkładamy $x$ (w metrach) na osi poziomej, $F$ na pionowej — wtedy nachylenie to wprost $k$. (Formalnie to $x$ ma tu niepewność, a $F$ jest dokładne; dla tak dobrze ułożonych punktów wynik jest praktycznie ten sam przy odwrotnym wyborze osi.)

**Metoda graficzna.** Prosta poprowadzona przez punkty przechodzi blisko $(0;\ 0)$ i $(0{,}120\ \mathrm{m};\ 2{,}96\ \mathrm{N})$, więc $k \approx 2{,}96/0{,}120 \approx 24{,}7\ \mathrm{N/m}$.

**Metoda najmniejszych kwadratów** (rachunek w Pythonie poniżej):

$$k = (24{,}7 \pm 0{,}3)\ \mathrm{N/m}, \qquad b = (-0{,}02 \pm 0{,}03)\ \mathrm{N}.$$

**Interpretacja.** Wyraz wolny jest zgodny z zerem w granicach niepewności — zgodnie z prawem Hooke'a. Niepewność względna $k$ to ok. 1,4%. Gdyby $b$ wyszło wyraźnie różne od zera, oznaczałoby to np. wstępne napięcie sprężyny albo błąd w odczycie położenia zerowego.

### Wersja z rachunkiem różniczkowym i całkowym

**Wyprowadzenie wzorów.** Warunki minimum $S(a, b)$:

$$\frac{\partial S}{\partial b} = -2\sum(y_i - ax_i - b) = 0, \qquad \frac{\partial S}{\partial a} = -2\sum x_i(y_i - ax_i - b) = 0.$$

To dwa równania liniowe na $a$ i $b$:

$$a\sum x_i + nb = \sum y_i, \qquad a\sum x_i^2 + b\sum x_i = \sum x_iy_i,$$

których rozwiązanie (np. wzorami Cramera) daje wzory z tabeli. Z pierwszego równania od razu widać, że prosta przechodzi przez punkt średnich $(\bar{x}, \bar{y})$.

**Dopasowanie ważone.** Gdy punkty mają różne niepewności $u_i$, minimalizujemy $\chi^2 = \sum\left(\dfrac{y_i - ax_i - b}{u_i}\right)^2$ — punkty pewniejsze mają większą wagę. Wartość $\chi^2/(n-2) \approx 1$ oznacza, że rozrzut punktów jest zgodny z ich niepewnościami.

## Typowe pułapki

- **Nachylenie z dwóch punktów pomiarowych.** Nachylenie bierze się z narysowanej prostej, nie z tabeli.
- **Łączenie punktów łamaną.** Model to prosta (albo krzywa z teorii); łamana nie jest modelem.
- **Wymuszanie przejścia przez zero.** Jeśli nie ma do tego powodu fizycznego i sprawdzenia, że $b \approx 0$, dopasowuj prostą z wyrazem wolnym.
- **Mylenie osi.** Nachylenie wykresu $x(F)$ to $1/k$, a nie $k$.
- **Dopasowanie prostej do krzywej.** Wysokie $R^2$ nie dowodzi liniowości — sprawdź wykres reszt.
- **Jednostki nachylenia.** Nachylenie ma jednostkę „$y$ na $x$”: tu N/m. W centymetrach wyszłoby 0,247 N/cm.

## Doświadczenie / symulacja

**Prawo Hooke'a w domu.** Zawieś na gumce recepturce albo sprężynie z długopisu woreczek, do którego wkładasz kolejno monety (masa 5-złotówki: 6,54 g; 2-złotówki: 5,21 g; 1-złotówki: 5,00 g; 1-groszówki: 1,64 g). Zmierz wydłużenie linijką dla 6–8 obciążeń, narysuj wykres $F(x)$ z prostokątami niepewności i wyznacz $k$ obiema metodami. Czy gumka spełnia prawo Hooke'a w całym zakresie?

**Python:** dopasowanie metodą najmniejszych kwadratów z niepewnościami parametrów i wykresem reszt.

```python
import numpy as np
import matplotlib.pyplot as plt

g = 9.81
m = np.array([0.05, 0.10, 0.15, 0.20, 0.25, 0.30])          # kg
x = np.array([2.1, 4.0, 6.2, 7.9, 10.1, 12.0]) / 100         # m
F = m * g

# Wzory z tabeli
n = x.size
D = n * np.sum(x**2) - np.sum(x)**2
a = (n * np.sum(x*F) - np.sum(x) * np.sum(F)) / D
b = (np.sum(F) - a * np.sum(x)) / n
res = F - (a*x + b)
s_y = np.sqrt(np.sum(res**2) / (n - 2))
ua, ub = s_y * np.sqrt(n / D), s_y * np.sqrt(np.sum(x**2) / D)
print(f"k = {a:.2f} ± {ua:.2f} N/m,  b = {b:.3f} ± {ub:.3f} N")

# To samo funkcją biblioteczną
(a2, b2), cov = np.polyfit(x, F, 1, cov=True)
print(f"polyfit: k = {a2:.2f} ± {np.sqrt(cov[0, 0]):.2f} N/m")

fig, ax = plt.subplots(2, 1, figsize=(6, 6), sharex=True, gridspec_kw={"height_ratios": [3, 1]})
ax[0].errorbar(x*100, F, xerr=0.1, fmt="o", capsize=3, label="pomiary")
xx = np.linspace(0, x.max()*1.05, 50)
ax[0].plot(xx*100, a*xx + b, label=f"F = {a:.1f}·x {b:+.2f}")
ax[0].set_ylabel("F [N]"); ax[0].grid(True); ax[0].legend()
ax[1].axhline(0, color="gray"); ax[1].plot(x*100, res, "o")
ax[1].set_xlabel("x [cm]"); ax[1].set_ylabel("reszty [N]"); ax[1].grid(True)
plt.tight_layout(); plt.show()
```

## Zadania

### A. Poziom maturalny

1. Prosta dopasowana do wykresu $v(t)$ przechodzi przez punkty $(1{,}0\ \mathrm{s};\ 3{,}5\ \mathrm{m/s})$ i $(5{,}0\ \mathrm{s};\ 11{,}5\ \mathrm{m/s})$. Wyznacz przyspieszenie i prędkość początkową.

<details>
<summary>Odpowiedź</summary>

$a = 8/4 = 2{,}0\ \mathrm{m/s^2}$; $v_0 = 3{,}5 - 2{,}0\cdot1{,}0 = 1{,}5\ \mathrm{m/s}$.
</details>

2. Najbardziej stroma prosta mieszcząca się w prostokątach niepewności ma nachylenie $26{,}1\ \mathrm{N/m}$, najmniej stroma — $23{,}5\ \mathrm{N/m}$. Podaj $k$ z niepewnością.

<details>
<summary>Odpowiedź</summary>

$k = (24{,}8 \pm 1{,}3)\ \mathrm{N/m}$.
</details>

3. Dla wahadła zmierzono $T$ dla kilku długości $l$. Jaki wykres narysujesz, żeby wyznaczyć $g$ z nachylenia prostej? Jak obliczysz $g$ z nachylenia $a$?

<details>
<summary>Odpowiedź</summary>

$T^2$ od $l$; $g = 4\pi^2/a$.
</details>

4. Uczeń dopasował prostą do wykresu napięcia od natężenia prądu dla opornika i otrzymał wyraz wolny $0{,}8\ \mathrm{V}$ przy niepewności $0{,}1\ \mathrm{V}$. Co to może oznaczać?

<details>
<summary>Odpowiedź</summary>

Wyraz wolny wyraźnie różny od zera wskazuje na błąd systematyczny (np. przesunięte zero woltomierza) albo na to, że element nie jest zwykłym opornikiem (np. dioda, źródło napięcia w obwodzie).
</details>

### B. Poziom akademicki

1. Dla punktów $(1;\ 2{,}1)$, $(2;\ 3{,}9)$, $(3;\ 6{,}2)$, $(4;\ 7{,}8)$ oblicz ręcznie $a$ i $b$ metodą najmniejszych kwadratów.

<details>
<summary>Odpowiedź</summary>

$\sum x = 10$, $\sum y = 20$, $\sum xy = 59{,}7$, $\sum x^2 = 30$, $D = 20$; $a = (4\cdot59{,}7 - 200)/20 = 1{,}94$; $b = (20 - 19{,}4)/4 = 0{,}15$.
</details>

2. Pokaż, że prosta najmniejszych kwadratów przechodzi przez punkt $(\bar{x}, \bar{y})$.

<details>
<summary>Odpowiedź</summary>

Z $\partial S/\partial b = 0$: $\sum y_i = a\sum x_i + nb$, po podzieleniu przez $n$: $\bar{y} = a\bar{x} + b$.
</details>

3. Dopasowanie prostej przez zero $y = ax$: wyprowadź wzór na $a$, minimalizując $\sum(y_i - ax_i)^2$.

<details>
<summary>Odpowiedź</summary>

$\dfrac{d}{da}\sum(y_i - ax_i)^2 = -2\sum x_i(y_i - ax_i) = 0 \Rightarrow a = \dfrac{\sum x_iy_i}{\sum x_i^2}$.
</details>

4. Rozpad: zmierzono liczbę zliczeń $N$ w kolejnych minutach. Jak dopasować model $N = N_0e^{-\lambda t}$ prostą? Jakie wagi należałoby nadać punktom, jeśli niepewność liczby zliczeń to $\sqrt{N}$?

<details>
<summary>Odpowiedź</summary>

Dopasować $\ln N = \ln N_0 - \lambda t$. Niepewność $\ln N$ to $u(N)/N = 1/\sqrt{N}$, więc waga punktu (odwrotność kwadratu niepewności) to $N$ — punkty z dużą liczbą zliczeń są pewniejsze.
</details>

## Źródła

- OpenStax, *Fizyka dla szkół wyższych*, t. 1, rozdz. 1 — §1.6 (precyzja i dokładność); przykłady odczytu nachylenia w rozdz. 3.
- CKE, [Informator o egzaminie maturalnym z fizyki](https://cke.gov.pl/images/_EGZAMIN_MATURALNY_OD_2023/Informatory/2024/Informator_EM2024_fizyka.pdf) — zadania z rysowaniem wykresu i wyznaczaniem wielkości z nachylenia prostej.
- [NIST/SEMATECH e-Handbook of Statistical Methods](https://www.itl.nist.gov/div898/handbook/) _(po angielsku)_ — rozdział o regresji liniowej i analizie reszt.
