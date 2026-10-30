# 25.02 — Całkowanie równań ruchu: Euler, Euler–Cromer, Verlet, RK4

> **Moduł:** [25 — Fizyka obliczeniowa w Pythonie](README.md) · **Poziom:** 🔵 studia · **Status:** ✅ pełny
>
> **Czytaj:**
>
> - _Podręczniki główne nie mają osobnego paragrafu na ten temat — materiały są w sekcji „Źródła”._

← [Python dla fizyka: NumPy, Matplotlib, SciPy](01-python-dla-fizyka.md) · [spis modułu](README.md) · [Rzut z oporem, wahadło nieliniowe, orbity planet](03-symulacje-mechaniki.md) →

## Po co to jest

Druga zasada dynamiki $m\ddot{\vec r} = \vec F(\vec r, \vec v, t)$ to równanie różniczkowe. Na kartce da się je rozwiązać tylko dla kilku prostych sił (stała, sprężysta, liniowy opór). Komputer rozwiązuje je dla dowolnej siły, krok po kroku: znając położenie i prędkość teraz, oblicza je za chwilę $\Delta t$. Od wyboru metody zależy, czy symulacja Układu Słonecznego zachowa energię przez miliardy lat, czy planety po kilku obiegach odlecą w kosmos. Te same algorytmy działają w grach komputerowych, symulacjach molekularnych i obliczaniu torów sond kosmicznych.

## Teoria w pigułce

Zapisujemy równanie drugiego rzędu jako układ dwóch równań pierwszego rzędu:

$$\frac{dx}{dt} = v, \qquad \frac{dv}{dt} = a(x, v, t) = \frac{F}{m}.$$

Dzielimy czas na kroki $h = \Delta t$ i obliczamy kolejne $x_n$, $v_n$.

**Metoda Eulera** (najprostsza, ale zła):

$$x_{n+1} = x_n + hv_n, \qquad v_{n+1} = v_n + ha_n.$$

Błąd globalny $\sim h$ (metoda 1. rzędu). Dla drgań energia rośnie w każdym kroku i tor spiralnie się rozwija.

**Metoda Eulera–Cromera** (półjawna): najpierw nowa prędkość, potem położenie z **nową** prędkością:

$$v_{n+1} = v_n + ha_n, \qquad x_{n+1} = x_n + hv_{n+1}.$$

Nadal 1. rzędu, ale energia w drganiach i orbitach nie ucieka — tylko oscyluje wokół prawidłowej wartości. Ta drobna zmiana kolejności robi ogromną różnicę.

**Metoda Verleta (prędkościowa)** — standard w symulacjach molekularnych i grawitacyjnych:

$$x_{n+1} = x_n + hv_n + \tfrac12h^2a_n, \qquad v_{n+1} = v_n + \tfrac12h\left(a_n + a_{n+1}\right).$$

Błąd $\sim h^2$, jedno obliczenie siły na krok, odwracalna w czasie i **symplektyczna** (zachowuje objętość w przestrzeni fazowej), więc energia pozostaje ograniczona nawet przez miliony kroków.

**Metoda Rungego–Kutty 4. rzędu (RK4).** W każdym kroku liczymy pochodne w czterech punktach (na początku, dwa razy w środku, na końcu) i bierzemy średnią ważoną. Dla $\dot y = f(t, y)$:

$$k_1 = f(t_n, y_n),\ k_2 = f\!\left(t_n + \tfrac h2, y_n + \tfrac h2k_1\right),\ k_3 = f\!\left(t_n + \tfrac h2, y_n + \tfrac h2k_2\right),\ k_4 = f(t_n + h, y_n + hk_3),$$

$$y_{n+1} = y_n + \frac h6(k_1 + 2k_2 + 2k_3 + k_4).$$

Błąd $\sim h^4$: dwa razy mniejszy krok daje 16 razy mniejszy błąd. Bardzo dokładna na krótkich odcinkach, ale energia powoli dryfuje. Funkcja `scipy.integrate.solve_ivp` używa metod Rungego–Kutty ze zmiennym krokiem (domyślnie RK45) i sama dobiera $h$ do zadanej dokładności.

**Jak wybrać:**
- szybki test, układy z tarciem → RK4 lub `solve_ivp`;
- długie symulacje układów zachowawczych (orbity, molekuły) → Verlet;
- metodę Eulera warto znać tylko po to, żeby rozumieć, dlaczego zawodzi.

## Wzory i założenia

| Metoda | Krok | Rząd (błąd globalny) | Obliczeń siły na krok | Energia w drganiach |
|---|---|---|---|---|
| Euler | $x \mathrel{+}= hv$, $v \mathrel{+}= ha$ (stare wartości) | $h$ | 1 | rośnie wykładniczo |
| Euler–Cromer | $v \mathrel{+}= ha$, potem $x \mathrel{+}= hv$ | $h$ | 1 | oscyluje, ograniczona |
| Verlet prędkościowy | jak wyżej, ze średnią przyspieszeń | $h^2$ | 1 | oscyluje, ograniczona |
| RK4 | 4 próbki pochodnej | $h^4$ | 4 | bardzo wolno maleje |

Warunek stabilności dla drgań harmonicznych (Euler–Cromer, Verlet): $h\omega < 2$. W praktyce dla dobrej dokładności $h \lesssim T/50$.

## Przykład rozwiązany

**Zadanie.** Oscylator $\ddot x = -x$ ($\omega = 1$, $T = 2\pi$), $x(0) = 1$, $v(0) = 0$. Porównaj błąd położenia w chwili $t = 10$ dla $h = 0{,}1;\ 0{,}05;\ 0{,}025$ oraz energię w chwili $t = 100$ dla $h = 0{,}1$.

| Metoda | błąd, $h = 0{,}1$ | $h = 0{,}05$ | $h = 0{,}025$ | $E(t = 100)/E_0$ |
|---|---|---|---|---|
| Euler | 0,57 | 0,24 | 0,11 | **ok. 21 000** |
| Euler–Cromer | $3{,}0\cdot10^{-2}$ | $1{,}4\cdot10^{-2}$ | $7\cdot10^{-3}$ | 1,04 |
| Verlet | $2{,}3\cdot10^{-3}$ | $5{,}7\cdot10^{-4}$ | $1{,}4\cdot10^{-4}$ | 1,00 |
| RK4 | $3{,}9\cdot10^{-6}$ | $2{,}7\cdot10^{-7}$ | $1{,}7\cdot10^{-8}$ | 1,00 |

Połowa kroku zmniejsza błąd ok. 2 razy (Euler, Euler–Cromer), 4 razy (Verlet) i 15 razy (RK4) — zgodnie z rzędem metod. Metoda Eulera po 16 okresach zwiększyła energię 21 tysięcy razy.

### Wersja z rachunkiem różniczkowym i całkowym

**Dlaczego Euler „pompuje” energię.** Dla $\ddot x = -\omega^2x$ krok Eulera w zapisie macierzowym:

$$\begin{pmatrix}x_{n+1}\\ v_{n+1}/\omega\end{pmatrix} = \begin{pmatrix}1 & h\omega\\ -h\omega & 1\end{pmatrix}\begin{pmatrix}x_n\\ v_n/\omega\end{pmatrix}.$$

Ta macierz to obrót pomnożony przez $\sqrt{1 + h^2\omega^2}$, więc $E_{n+1} = (1 + h^2\omega^2)E_n$. Po $N$ krokach: $E_N = (1 + h^2\omega^2)^NE_0$; dla $h = 0{,}1$, $N = 1000$: $1{,}01^{1000} \approx 2{,}1\cdot10^4$.

Euler–Cromer daje macierz $\begin{pmatrix}1 - h^2\omega^2 & h\omega\\ -h\omega & 1\end{pmatrix}$ o wyznaczniku $1 - h^2\omega^2 + h^2\omega^2 = 1$. Pole w przestrzeni fazowej jest zachowane (metoda symplektyczna), a wartości własne leżą na okręgu jednostkowym, gdy $\lvert\operatorname{tr}\rvert = \lvert2 - h^2\omega^2\rvert < 2$, czyli $h\omega < 2$. Wtedy rozwiązanie nie rośnie ani nie maleje — energia tylko oscyluje.

## Typowe pułapki

- **Mały krok naprawi metodę Eulera.** Zmniejszy błąd, ale energia nadal będzie systematycznie rosnąć. Lepiej zmienić metodę.
- **RK4 jest zawsze najlepsza.** Na krótkich odcinkach tak. W symulacjach na miliony okresów (orbity) metody symplektyczne (Verlet) lepiej zachowują energię przy tym samym koszcie.
- **Siła zależna od prędkości w Verlecie.** Wzór na $v_{n+1}$ wymaga $a_{n+1}$, które zależy od $v_{n+1}$. Przy oporze ośrodka używa się wersji przybliżonej lub RK4.
- **Brak testu.** Każdy nowy program sprawdź najpierw na przypadku z rozwiązaniem analitycznym (spadek swobodny, oscylator) i przy dwóch różnych krokach.

## Doświadczenie / symulacja

**Porównaj z pomiarem.** Nagraj w phyphox drgania telefonu zawieszonego na gumce (akcelerometr) i porównaj z symulacją oscylatora tłumionego. Dobierz $\omega$ i współczynnik tłumienia tak, żeby krzywe się pokrywały (dokładne dopasowanie: 25.04).

**Python:** cztery metody na jednym oscylatorze — błąd w funkcji kroku (wykres log–log, nachylenie = rząd metody) i zachowanie energii w długiej symulacji.

```python
import numpy as np
import matplotlib.pyplot as plt

acc = lambda x: -x                                   # oscylator ω = 1

def euler(x, v, h):        return x + h*v, v + h*acc(x)
def euler_cromer(x, v, h): v = v + h*acc(x); return x + h*v, v
def verlet(x, v, h):
    a = acc(x); x = x + h*v + 0.5*h*h*a
    return x, v + 0.5*h*(a + acc(x))
def rk4(x, v, h):
    k1x, k1v = v, acc(x)
    k2x, k2v = v + 0.5*h*k1v, acc(x + 0.5*h*k1x)
    k3x, k3v = v + 0.5*h*k2v, acc(x + 0.5*h*k2x)
    k4x, k4v = v + h*k3v, acc(x + h*k3x)
    return x + h/6*(k1x + 2*k2x + 2*k3x + k4x), v + h/6*(k1v + 2*k2v + 2*k3v + k4v)

metody = {"Euler": euler, "Euler–Cromer": euler_cromer, "Verlet": verlet, "RK4": rk4}

def symuluj(krok, h, T):
    x, v = 1.0, 0.0
    E = []
    for _ in range(int(round(T/h))):
        x, v = krok(x, v, h)
        E.append(0.5*(x*x + v*v))
    return x, np.array(E)

hs = np.array([0.2, 0.1, 0.05, 0.025, 0.0125])
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(11, 4))
for nazwa, krok in metody.items():
    bledy = [abs(symuluj(krok, h, 10)[0] - np.cos(10)) for h in hs]
    rzad = np.polyfit(np.log(hs), np.log(bledy), 1)[0]
    _, E = symuluj(krok, 0.1, 1000)
    print(f"{nazwa:13s}: rząd ≈ {rzad:.2f}, E/E0 po 1000 jednostkach czasu (h = 0,1): min {E.min()/0.5:.4f}, max {E.max()/0.5:.4g}")
    ax1.loglog(hs, bledy, "o-", label=nazwa)
    if nazwa != "Euler":
        ax2.plot(np.arange(1, E.size + 1)*0.1, E/0.5, label=nazwa)
ax1.set_xlabel("krok h"); ax1.set_ylabel("błąd x(10)"); ax1.legend(); ax1.grid(True, which="both")
ax2.set_xlabel("t"); ax2.set_ylabel("E / E0"); ax2.legend(); ax2.grid(True)
plt.tight_layout(); plt.show()
```

## Zadania

### A. Poziom maturalny _(opcjonalnie — rozgrzewka)_

1. Ciało spada swobodnie z prędkością początkową 0. Wykonaj ręcznie trzy kroki metody Eulera z $h = 0{,}1\ \mathrm s$ ($g = 10\ \mathrm{m/s^2}$). Porównaj drogę po 0,3 s z dokładnym wynikiem.

<details>
<summary>Odpowiedź</summary>

$v$: 0 → 1 → 2 → 3 m/s; $s$: 0 → 0 → 0,1 → 0,3 m (Euler używa starej prędkości). Dokładnie $s = gt^2/2 = 0{,}45\ \mathrm m$. Euler–Cromer dałby 0,1 → 0,3 → 0,6 m; średnia obu metod (Verlet) daje dokładnie 0,45 m, bo dla stałego przyspieszenia Verlet jest ścisły.
</details>

2. Dlaczego w symulacji ruchu planety metodą Eulera planeta oddala się od Słońca?

<details>
<summary>Odpowiedź</summary>

Metoda Eulera w każdym kroku nieco zwiększa energię układu (krok wzdłuż stycznej wyprowadza na wyższą orbitę), więc orbita rozwija się w spiralę.
</details>

### B. Poziom akademicki

1. Pokaż, że dla oscylatora krok Eulera zwiększa energię o czynnik $1 + h^2\omega^2$. Po ilu krokach przy $h\omega = 0{,}05$ energia się podwoi?

<details>
<summary>Odpowiedź</summary>

$x_{n+1}^2 + v_{n+1}^2/\omega^2 = (1 + h^2\omega^2)(x_n^2 + v_n^2/\omega^2)$. Podwojenie: $N = \ln2/\ln(1{,}0025) \approx 277$ kroków, czyli ok. 2,2 okresu.
</details>

2. Napisz metodę Verleta dla spadku swobodnego i pokaż, że daje wynik dokładny dla dowolnego $h$.

<details>
<summary>Odpowiedź</summary>

Przy stałym $a$: $x_{n+1} = x_n + hv_n + \tfrac12h^2a$ i $v_{n+1} = v_n + ha$ — to dokładne wzory ruchu jednostajnie przyspieszonego, więc błąd obcięcia jest równy zeru.
</details>

3. Wyznacz numerycznie rząd metody: dla RK4 i oscylatora zmierz błąd w $t = 10$ przy $h = 0{,}2$ i $0{,}1$. Ile wynosi $\log_2$ stosunku błędów?

<details>
<summary>Odpowiedź</summary>

Błędy ok. $5{,}3\cdot10^{-5}$ i $3{,}9\cdot10^{-6}$, stosunek ok. 13,5, $\log_2 \approx 3{,}8$ — blisko 4 (przy mniejszych krokach stosunek dąży do 16). (Uruchom kod z sekcji symulacji — wypisuje rząd z nachylenia prostej).
</details>

4. Rozwiąż `solve_ivp` równanie oscylatora z `rtol=1e-9` i porównaj liczbę obliczeń funkcji (`sol.nfev`) z RK4 o stałym kroku przy tej samej dokładności.

<details>
<summary>Odpowiedź</summary>

`solve_ivp(lambda t, y: [y[1], -y[0]], [0, 10], [1, 0], rtol=1e-9, atol=1e-12)` potrzebuje ok. 1300 obliczeń funkcji i daje błąd ok. $10^{-9}$. RK4 ze stałym krokiem osiąga taki błąd przy ok. 800 krokach ($h \approx 0{,}0125$), czyli ok. 3200 obliczeń. Metoda adaptacyjna dobiera krok sama i zwykle jest tańsza.
</details>

## Źródła

- Z. Fortuna, B. Macukow, J. Wąsowski, *Metody numeryczne*, WNT/PWN — rozdział o równaniach różniczkowych zwyczajnych (metody Eulera i Rungego–Kutty).
- OpenStax, *Fizyka dla szkół wyższych*, t. 1 — §15.1 (ruch harmoniczny) — rozwiązanie analityczne do porównań.
- Moduł 00.05 (proste równania różniczkowe w fizyce) i 09 (drgania).
- M. Newman, *Computational Physics*, rozdz. 8 (równania różniczkowe zwyczajne, metody Rungego–Kutty i Verleta) — materiał dodatkowy, po angielsku.
