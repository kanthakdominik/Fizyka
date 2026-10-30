# 25.04 — Dopasowanie modeli do danych pomiarowych

> **Moduł:** [25 — Fizyka obliczeniowa w Pythonie](README.md) · **Poziom:** 🟢🔵 matura R + studia · **Status:** ✅ pełny
>
> **Czytaj:**
>
> - _Podręczniki główne nie mają osobnego paragrafu na ten temat — materiały są w sekcji „Źródła”._

← [Rzut z oporem, wahadło nieliniowe, orbity planet](03-symulacje-mechaniki.md) · [spis modułu](README.md) · [Pola i potencjały na siatce — równanie Laplace'a](05-pola-na-siatce.md) →

## Po co to jest

Pomiar daje punkty z niepewnościami, a fizyka — model z parametrami: $g$ z okresu wahadła, stałą tłumienia z drgań, czas połowicznego zaniku z liczby zliczeń, $H_0$ z prędkości galaktyk. Dopasowanie modelu odpowiada na trzy pytania: jakie wartości parametrów najlepiej pasują do danych, z jaką niepewnością je znamy i czy model w ogóle opisuje dane. Prostą przez punkty opisuje temat 01.04. Tutaj przechodzimy do modeli nieliniowych, dopasowania ważonego, testu $\chi^2$ i typowych błędów, które dają ładny wykres i zły wynik. To umiejętność potrzebna w każdym sprawozdaniu z pracowni i na maturze (linearyzacja, odczyt nachylenia).

## Teoria w pigułce

**Metoda najmniejszych kwadratów (ważona).** Dla punktów $(x_i, y_i)$ z niepewnościami $u_i$ i modelu $f(x; \vec p)$ szukamy parametrów minimalizujących

$$\chi^2(\vec p) = \sum_{i=1}^n\left(\frac{y_i - f(x_i; \vec p)}{u_i}\right)^2.$$

Punkty pewniejsze mają większą wagę. Gdy niepewności nie są znane, przyjmuje się je równe (zwykła metoda najmniejszych kwadratów).

**Model liniowy w parametrach** (prosta, wielomian) ma rozwiązanie jawne (01.04, `np.polyfit`). **Model nieliniowy** (np. $Ae^{-\gamma t}\cos(\omega t + \varphi)$) wymaga minimalizacji iteracyjnej od wartości startowych: `scipy.optimize.curve_fit` (metoda Levenberga–Marquardta).

**Niepewności parametrów** daje macierz kowariancji $C$: $u(p_k) = \sqrt{C_{kk}}$. Elementy pozadiagonalne mówią o **korelacji** parametrów (np. amplituda i tłumienie są skorelowane — większa amplituda początkowa „kompensuje się” szybszym tłumieniem). W `curve_fit` przy znanych niepewnościach trzeba podać `sigma=u, absolute_sigma=True`. Bez tego niepewności parametrów są skalowane przez rozrzut danych.

**Czy model pasuje? Test $\chi^2$.** Liczba stopni swobody $\nu = n - (\text{liczba parametrów})$. Jeśli model jest dobry, a niepewności poprawne:
- $\chi^2/\nu \approx 1$ — dobrze;
- $\chi^2/\nu \gg 1$ — model nie pasuje albo niepewności są niedoszacowane;
- $\chi^2/\nu \ll 1$ — niepewności są przeszacowane (lub dane „poprawiane”).

Prawdopodobieństwo $p$ (`1 - scipy.stats.chi2.cdf(chi2, nu)`) mówi, jak często przy poprawnym modelu dostalibyśmy $\chi^2$ jeszcze większe. Wartości $p < 0{,}01$ sugerują odrzucenie modelu.

**Reszty** $r_i = (y_i - f(x_i))/u_i$ powinny być losowo rozrzucone wokół 0, w większości w przedziale $\pm2$. Systematyczny wzór (łuk, fala) oznacza zły model — to najczulszy test.

**Linearyzacja** (matura): zależność nieliniową przekształca się do prostej, np. $T = 2\pi\sqrt{l/g} \Rightarrow T^2 = \dfrac{4\pi^2}{g}l$, albo $N = N_0e^{-\lambda t} \Rightarrow \ln N = \ln N_0 - \lambda t$. Trzeba pamiętać, że przekształcenie zmienia niepewności: $u(\ln N) = u(N)/N$, więc punkty o małym $N$ są znacznie mniej pewne i powinny mieć mniejszą wagę.

## Wzory i założenia

| Wzór | Znaczenie | Kiedy obowiązuje |
|---|---|---|
| $\chi^2 = \sum\left(\dfrac{y_i - f(x_i)}{u_i}\right)^2$ | miara zgodności | niezależne pomiary, błędy normalne |
| $\nu = n - m$, oczekiwane $\chi^2 \approx \nu \pm \sqrt{2\nu}$ | stopnie swobody | $m$ parametrów |
| $u(p_k) = \sqrt{C_{kk}}$, $\rho_{kl} = \dfrac{C_{kl}}{\sqrt{C_{kk}C_{ll}}}$ | niepewność i korelacja | z macierzy kowariancji |
| $C = (J^TWJ)^{-1}$, $J_{ik} = \partial f(x_i)/\partial p_k$, $W = \mathrm{diag}(1/u_i^2)$ | kowariancja parametrów | przybliżenie liniowe wokół minimum |
| $u(\ln y) = u(y)/y$ | niepewność po linearyzacji | $u(y) \ll y$ |
| $u(N) = \sqrt N$ | niepewność liczby zliczeń | rozkład Poissona (22.03) |

## Przykład rozwiązany

**Zadanie (poziom maturalny).** Zmierzono okres wahadła dla różnych długości:

| $l$ [m] | 0,20 | 0,40 | 0,60 | 0,80 | 1,00 |
|---|---|---|---|---|---|
| $T$ [s] | 0,90 | 1,27 | 1,55 | 1,80 | 2,01 |

Zlinearyzuj zależność i wyznacz $g$.

$T^2$ [s²]: 0,810; 1,613; 2,403; 3,240; 4,040. Wykres $T^2(l)$ to prosta przez początek układu o nachyleniu $a = 4\pi^2/g$.

Dopasowanie: $a \approx 4{,}04\ \mathrm{s^2/m}$ (wyraz wolny $-0{,}005$, zgodny z zerem), więc $g = 4\pi^2/a \approx 9{,}76\ \mathrm{m/s^2}$.

### Wersja z rachunkiem różniczkowym i całkowym

**Skąd się bierze macierz kowariancji.** Rozwińmy model wokół minimum: $f(x_i; \vec p + \delta\vec p) \approx f_i + \sum_kJ_{ik}\delta p_k$. Wtedy $\chi^2$ jest funkcją kwadratową $\delta\vec p$:

$$\chi^2(\delta\vec p) = \sum_i\frac{(r_i - \sum_kJ_{ik}\delta p_k)^2}{u_i^2}, \qquad \frac{\partial\chi^2}{\partial\delta p_k} = 0 \Rightarrow (J^TWJ)\,\delta\vec p = J^TW\vec r.$$

To krok metody **Gaussa–Newtona**: powtarza się go aż do zbieżności (Levenberg–Marquardt dodaje tłumienie kroku, żeby iteracje nie „uciekały”). Niepewności pomiarów przenoszą się na parametry jak przy prawie przenoszenia niepewności: $C = (J^TWJ)^{-1}$.

**Dla prostej** $f = ax + b$: $J = [x_i, 1]$ i wychodzą znane wzory

$$u(a) = \sqrt{\frac{S}{\Delta}}, \quad u(b) = \sqrt{\frac{S_{xx}}{\Delta}}, \qquad S = \sum\frac1{u_i^2},\ S_x = \sum\frac{x_i}{u_i^2},\ S_{xx} = \sum\frac{x_i^2}{u_i^2},\ \Delta = SS_{xx} - S_x^2.$$

**Interpretacja geometryczna:** $\chi^2$ rośnie o 1, gdy parametr odsunie się o jedno odchylenie standardowe od minimum (przy optymalizacji pozostałych). Stąd graficzna metoda wyznaczania niepewności: przedział, w którym $\chi^2 \le \chi^2_{\min} + 1$.

## Typowe pułapki

- **Dopasowanie bez niepewności.** Bez $u_i$ nie ma testu $\chi^2$, a niepewności parametrów są tylko oszacowaniem z rozrzutu.
- **Linearyzacja bez wag.** Dopasowanie prostej do $\ln N$ z jednakowymi wagami przecenia punkty o małej liczbie zliczeń. Trzeba wag $w_i = 1/u(\ln N_i)^2 = N_i$ albo dopasowania nieliniowego do $N$.
- **Złe wartości startowe.** Dopasowanie nieliniowe może utknąć w minimum lokalnym albo znaleźć rozwiązanie równoważne (np. $A < 0$ i faza przesunięta o $\pi$ — ten sam wykres). Wartości startowe odczytaj z wykresu albo z transformaty Fouriera (częstość).
- **„$R^2 = 0{,}99$, więc model jest dobry”.** $R^2$ jest bliskie 1 także dla wyraźnie złego modelu, gdy zmienność danych jest duża. Patrz na reszty i $\chi^2$.
- **Za wiele parametrów.** Każdy dodatkowy parametr zmniejsza $\chi^2$, ale może opisywać szum. Porównując modele, uwzględnij liczbę stopni swobody.

## Doświadczenie / symulacja

**Drgania tłumione z phyphox.** Zawieś telefon na sprężynie lub gumce, nagraj przyspieszenie (*Akcelerometr bez g*), wyeksportuj CSV i dopasuj $a(t) = Ae^{-\gamma t}\cos(\omega t + \varphi) + c$. Wyznacz dobroć $Q = \omega/(2\gamma)$. Niepewność pojedynczego punktu oszacuj z odchylenia standardowego sygnału, gdy telefon leży nieruchomo.

**Python:** dopasowanie drgań tłumionych (`curve_fit`, macierz kowariancji, $\chi^2$, reszty) i porównanie trzech sposobów wyznaczania stałej rozpadu z danych licznikowych.

```python
import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
from scipy import stats

rng = np.random.default_rng(3)
t = np.linspace(0, 10, 201); u = 0.05                      # s, niepewność punktu
model = lambda t, A, g, w, f: A*np.exp(-g*t)*np.cos(w*t + f)
y = model(t, 2.0, 0.25, 3.0, 0.4) + rng.normal(0, u, t.size)
p, C = curve_fit(model, t, y, p0=[1.5, 0.2, 2.9, 0.0], sigma=np.full(t.size, u), absolute_sigma=True)
r = (y - model(t, *p))/u
chi2, nu = np.sum(r**2), t.size - len(p)
for nazwa, wart, niep in zip(["A", "γ", "ω", "φ"], p, np.sqrt(np.diag(C))):
    print(f"{nazwa} = {wart:.4f} ± {niep:.4f}")
print(f"χ² = {chi2:.1f}, ν = {nu}, χ²/ν = {chi2/nu:.2f}, p = {1 - stats.chi2.cdf(chi2, nu):.2f}")
print(f"korelacja A–γ: {C[0, 1]/np.sqrt(C[0, 0]*C[1, 1]):.2f}, dobroć Q = ω/(2γ) = {p[2]/(2*p[1]):.2f}")

# rozpad: liczby zliczeń w kolejnych odcinkach czasu, λ = 0,1 1/s
t2 = np.arange(0, 60, 5.0)
n = rng.poisson(1000*np.exp(-0.1*t2))
a1 = np.polyfit(t2, np.log(n), 1)[0]                        # ln N bez wag
a2 = np.polyfit(t2, np.log(n), 1, w=np.sqrt(n))[0]          # ln N z wagami 1/u(ln N) = √N
p3, C3 = curve_fit(lambda t, N0, lam: N0*np.exp(-lam*t), t2, n, p0=[900, 0.08], sigma=np.sqrt(n), absolute_sigma=True)
print(f"λ (prawdziwe 0,1): ln N bez wag {-a1:.4f}, z wagami {-a2:.4f}, nieliniowo {p3[1]:.4f} ± {np.sqrt(C3[1, 1]):.4f} 1/s")

fig, (ax1, ax2) = plt.subplots(2, 1, sharex=True, figsize=(8, 6), gridspec_kw={"height_ratios": [3, 1]})
ax1.errorbar(t, y, yerr=u, fmt=".", ms=3, label="dane"); ax1.plot(t, model(t, *p), label="dopasowanie"); ax1.legend()
ax2.plot(t, r, "."); ax2.axhline(0, color="gray"); ax2.set_ylabel("reszty / u"); ax2.set_xlabel("t [s]")
plt.show()
```

## Zadania

### A. Poziom maturalny

1. Jak zlinearyzować zależność $s = \tfrac12at^2$ (droga od czasu przy ruchu jednostajnie przyspieszonym), żeby z nachylenia odczytać $a$?

<details>
<summary>Odpowiedź</summary>

Wykres $s$ od $t^2$: prosta o nachyleniu $a/2$. Albo $\sqrt s$ od $t$: nachylenie $\sqrt{a/2}$.
</details>

2. Z danych wahadła w przykładzie wyznacz $g$, prowadząc prostą przez początek układu i pierwszy oraz ostatni punkt tabeli. Porównaj z wynikiem dopasowania.

<details>
<summary>Odpowiedź</summary>

Nachylenie z ostatniego punktu: $4{,}04/1{,}00 = 4{,}04\ \mathrm{s^2/m}$, $g \approx 9{,}77\ \mathrm{m/s^2}$; z pierwszego: $0{,}810/0{,}20 = 4{,}05$, $g \approx 9{,}75$. Zgodne z dopasowaniem (9,76) w granicach ok. 0,1%.
</details>

3. Aktywność próbki zmierzono w kilku chwilach. Jak z wykresu $\ln A(t)$ wyznaczyć czas połowicznego zaniku?

<details>
<summary>Odpowiedź</summary>

Wykres jest prostą o nachyleniu $-\lambda$. $T_{1/2} = \ln2/\lambda$.
</details>

### B. Poziom akademicki

1. Wyprowadź wzory na nachylenie prostej przechodzącej przez początek układu ($y = ax$) metodą najmniejszych kwadratów z jednakowymi niepewnościami $u$. Ile wynosi $u(a)$?

<details>
<summary>Odpowiedź</summary>

$\dfrac{d}{da}\sum(y_i - ax_i)^2 = 0 \Rightarrow a = \dfrac{\sum x_iy_i}{\sum x_i^2}$, $u(a) = \dfrac{u}{\sqrt{\sum x_i^2}}$. Dla danych wahadła $a = 4{,}037\ \mathrm{s^2/m}$, $g = 9{,}78\ \mathrm{m/s^2}$.
</details>

2. Dopasowanie dało $\chi^2 = 45$ przy $\nu = 20$. Co to oznacza? Co zrobić?

<details>
<summary>Odpowiedź</summary>

$\chi^2/\nu = 2{,}25$, $p \approx 0{,}001$. Model nie pasuje albo niepewności są niedoszacowane ok. 1,5 raza. Obejrzyj reszty: wzór w resztach wskazuje na zły model (np. pominięty człon), losowy duży rozrzut — na niedoszacowane niepewności.
</details>

3. Dlaczego dla danych licznikowych $u(\ln N) = 1/\sqrt N$? Ile razy mniejszą wagę ma punkt z $N = 10$ niż z $N = 1000$?

<details>
<summary>Odpowiedź</summary>

$u(N) = \sqrt N$, więc $u(\ln N) = u(N)/N = 1/\sqrt N$. Waga $1/u^2 = N$: punkt z $N = 10$ ma 100 razy mniejszą wagę.
</details>

4. Zmodyfikuj kod z sekcji symulacji: powtórz 1000 razy generowanie danych rozpadu i dopasowanie. Porównaj średnią i rozrzut $\lambda$ z trzech metod. Która jest obciążona?

<details>
<summary>Odpowiedź</summary>

Przykładowy wynik (1000 powtórzeń, zera zastąpione jedynką): bez wag $0{,}102 \pm 0{,}006$, z wagami $0{,}0995 \pm 0{,}002$, nieliniowo $0{,}101 \pm 0{,}002$. Linearyzacja bez wag ma prawie 3 razy większy rozrzut i jest obciążona w górę, bo punkty z małą liczbą zliczeń (duży względny szum) mają w niej zbyt duży wpływ. Pozostałe dwie metody mają małe obciążenie (ok. 1%), bo wagi liczy się z zaobserwowanego $N$, a nie z prawdziwego. Najlepsza jest metoda największej wiarygodności z rozkładem Poissona.
</details>

## Źródła

- Moduł 01.03 (niepewności pomiarowe) i 01.04 (wykresy i dopasowanie prostej) — podstawy.
- Z. Fortuna, B. Macukow, J. Wąsowski, *Metody numeryczne*, WNT/PWN — rozdział o aproksymacji średniokwadratowej.
- Dokumentacja SciPy: [`scipy.optimize.curve_fit`](https://docs.scipy.org/doc/scipy/reference/generated/scipy.optimize.curve_fit.html) (materiał dodatkowy, po angielsku).
