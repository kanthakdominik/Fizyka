# 25.03 — Rzut z oporem, wahadło nieliniowe, orbity planet

> **Moduł:** [25 — Fizyka obliczeniowa w Pythonie](README.md) · **Poziom:** 🔵 studia · **Status:** ✅ pełny
>
> **Czytaj:**
>
> - _Podręczniki główne nie mają osobnego paragrafu na ten temat — materiały są w sekcji „Źródła”._

← [Całkowanie równań ruchu: Euler, Euler–Cromer, Verlet, RK4](02-calkowanie-rownan-ruchu.md) · [spis modułu](README.md) · [Dopasowanie modeli do danych pomiarowych](04-dopasowanie-modeli.md) →

## Po co to jest

W szkole rzut ukośny liczy się bez oporu powietrza, wahadło tylko dla małych wychyleń, a orbity jako okręgi. Prawdziwa piłka baseballowa leci o połowę bliżej niż w próżni. Wahadło wychylone o 90° ma okres dłuższy o 18%. Orbita komety jest silnie wydłużoną elipsą. Symulacja pozwala usunąć te uproszczenia i sprawdzić, kiedy wzory szkolne wystarczają. To pierwszy krok do prawdziwej fizyki obliczeniowej: model → równania ruchu → program → test → wnioski.

## Teoria w pigułce

**1. Rzut z oporem kwadratowym** (03.05). Dla piłek, ludzi i samochodów w powietrzu opór jest proporcjonalny do kwadratu prędkości i skierowany przeciwnie do niej:

$$\vec F_{\text{op}} = -\tfrac12\rho C_xAv\,\vec v \Rightarrow \ddot{\vec r} = \vec g - k\lvert\vec v\rvert\vec v, \qquad k = \frac{\rho C_xA}{2m}.$$

Ruch w poziomie i pionie jest sprzężony (przez $\lvert\vec v\rvert$), więc nie da się go rozwiązać analitycznie. Skutki: mniejszy zasięg i wysokość, tor niesymetryczny (opadanie bardziej strome), kąt optymalny mniejszy od 45°, prędkość graniczna $v_{gr} = \sqrt{g/k}$.

**2. Wahadło nieliniowe** (09.03). Pełne równanie

$$\ddot\theta = -\frac gl\sin\theta$$

dla małych kątów ($\sin\theta \approx \theta$) daje drgania harmoniczne z okresem $T_0 = 2\pi\sqrt{l/g}$. Dla dużych amplitud okres rośnie. Dokładny wynik wyraża się przez całkę eliptyczną:

$$T = \frac{2T_0}{\pi}K\!\left(\sin^2\frac{\theta_0}{2}\right) \approx T_0\left(1 + \frac{\theta_0^2}{16} + \dots\right).$$

Przy 90° okres jest dłuższy o 18%, przy 170° — prawie 2,5 raza. Dodanie tłumienia i siły wymuszającej prowadzi do **chaosu**: ruch jest deterministyczny, ale nieprzewidywalny na dłuższą metę, bo nieskończenie małe różnice warunków początkowych rosną wykładniczo.

**3. Orbity** (07.03–07.04). Ruch planety w polu Słońca:

$$\ddot{\vec r} = -\frac{GM}{r^3}\vec r.$$

Wygodne jednostki: AU, rok, wtedy $GM_\odot = 4\pi^2\ \mathrm{AU^3/rok^2}$. Symulacja metodą Verleta (25.02) odtwarza wszystkie trzy prawa Keplera, a test poprawności to zachowanie energii i momentu pędu. Łatwo dodać kolejne ciała (Jowisz zaburzający orbitę Ziemi lub komety, problem trzech ciał) — wtedy rozwiązanie analityczne nie istnieje.

**Schemat pracy:**
1. Zapisz siły i równania ruchu, dobierz jednostki.
2. Wybierz metodę (`solve_ivp` lub Verlet) i krok.
3. **Przetestuj** na przypadku znanym (bez oporu, małe kąty, orbita kołowa).
4. Sprawdź zbieżność: połowa kroku nie może zmieniać wyniku.
5. Dopiero wtedy wyciągaj wnioski.

## Wzory i założenia

| Wzór | Znaczenie | Kiedy obowiązuje |
|---|---|---|
| $\ddot{\vec r} = \vec g - k\lvert\vec v\rvert\vec v$, $k = \rho C_xA/(2m)$ | rzut z oporem | $\mathrm{Re} \gtrsim 1000$ |
| $v_{gr} = \sqrt{g/k}$ | prędkość graniczna | spadek pionowy |
| $\ddot\theta = -(g/l)\sin\theta$ | wahadło matematyczne | bez tarcia |
| $T = \dfrac{2T_0}{\pi}K(\sin^2\tfrac{\theta_0}{2})$, $T \approx T_0(1 + \theta_0^2/16)$ | okres przy dużej amplitudzie | $K(m)$ — pełna całka eliptyczna |
| $\ddot{\vec r} = -GM\vec r/r^3$, $GM_\odot = 4\pi^2\ \mathrm{AU^3/rok^2}$ | ruch orbitalny | dwa ciała, $M \gg m$ |
| $E = \tfrac12v^2 - GM/r$, $L = \lvert\vec r\times\vec v\rvert$ | zachowane (na jednostkę masy) | test symulacji |

## Przykład rozwiązany

**Zadanie 1.** Piłka baseballowa ($m = 0{,}145\ \mathrm{kg}$, $d = 7{,}4\ \mathrm{cm}$, $C_x = 0{,}35$) wybita z prędkością 45 m/s pod kątem 45°. Porównaj zasięg z oporem i bez ($\rho = 1{,}2\ \mathrm{kg/m^3}$).

$k = \dfrac{1{,}2\cdot0{,}35\cdot\pi\cdot0{,}037^2}{2\cdot0{,}145} \approx 0{,}0062\ \mathrm{m^{-1}}$, $v_{gr} \approx 40\ \mathrm{m/s}$.

Bez oporu: $z = v_0^2/g \approx 206\ \mathrm m$. Z oporem (symulacja): ok. 110 m, maksymalna wysokość 35 m, czas lotu 5,3 s. Najdalej piłka leci przy kącie ok. 40° (111 m).

**Zadanie 2.** Ile razy okres wahadła wychylonego o 10°, 30°, 60°, 90° i 170° jest dłuższy od $T_0$?

Z całki eliptycznej: 1,002; 1,017; 1,073; 1,180; 2,44. Przybliżenie $1 + \theta_0^2/16$ daje dla 90° wartość 1,154 — błąd 2%.

### Wersja z rachunkiem różniczkowym i całkowym

**Okres wahadła z zasady zachowania energii.** Z $\tfrac12l^2\dot\theta^2 = gl(\cos\theta - \cos\theta_0)$:

$$T = 4\int_0^{\theta_0}\frac{d\theta}{\dot\theta} = 4\sqrt{\frac lg}\int_0^{\theta_0}\frac{d\theta}{\sqrt{2(\cos\theta - \cos\theta_0)}}.$$

Całka ma osobliwość na końcu przedziału (prędkość równa zeru), co utrudnia całkowanie numeryczne. Podstawienie $\sin\tfrac\theta2 = \sin\tfrac{\theta_0}2\sin\varphi$ usuwa osobliwość i daje

$$T = 4\sqrt{\frac lg}\int_0^{\pi/2}\frac{d\varphi}{\sqrt{1 - m\sin^2\varphi}} = 4\sqrt{\frac lg}K(m), \qquad m = \sin^2\frac{\theta_0}{2}.$$

Rozwinięcie $K(m) \approx \tfrac\pi2(1 + \tfrac m4)$ i $m \approx \theta_0^2/4$ daje $T \approx T_0(1 + \theta_0^2/16)$.

## Typowe pułapki

- **Opór liniowy zamiast kwadratowego.** Opór $\propto v$ dotyczy bardzo małych prędkości lub cząstek (kropelki mgły). Dla piłek $F \propto v^2$. Sprawdź liczbę Reynoldsa (08).
- **Liczenie oporu osobno dla składowych** jako $-kv_x^2$ i $-kv_y^2$. Poprawnie: $-k\lvert\vec v\rvert v_x$ i $-k\lvert\vec v\rvert v_y$ (i znak przeciwny do składowej prędkości).
- **Koniec lotu w kroku czasowym.** Piłka „przelatuje” pod ziemię w ostatnim kroku. Trzeba interpolować moment upadku albo użyć zdarzeń (`events`) w `solve_ivp`.
- **Orbita nie zamyka się** — to zwykle za duży krok przy peryhelium, gdzie prędkość jest największa, albo metoda niesymplektyczna. Zmniejsz krok lub użyj kroku zmiennego.
- **Chaos to błąd numeryczny.** W układach chaotycznych rozbieżność torów jest cechą fizyki, nie programu. Sprawdza się ją, zmniejszając tolerancję obliczeń: tor do pewnej chwili się nie zmienia, rozbieżność pojawia się tylko później.

## Doświadczenie / symulacja

**Wahadło z telefonem.** Zawieś telefon na dwóch sznurkach (wahadło bifilarne, bez obrotów) i zmierz okres w phyphox (*Wahadło*, żyroskop) dla amplitud 10°, 30°, 60°, 80°. Porównaj z $T(\theta_0)$ z symulacji. Wahadło o dużej amplitudzie wymaga sztywnego pręta zamiast sznurka.

**Rzut piłką.** Nagraj telefonem lot piłki (np. lekkiej piłki plażowej, na którą opór działa silnie) i odczytaj położenia w programie Tracker. Porównaj z symulacjami bez oporu i z oporem.

**Python:** trzy symulacje — rzut z oporem (`solve_ivp` ze zdarzeniem upadku), okres wahadła w funkcji amplitudy (symulacja vs całka eliptyczna) i orbita eliptyczna metodą Verleta z kontrolą energii i III prawa Keplera.

```python
import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp
from scipy.special import ellipk

g = 9.81
k = 0.5*1.2*0.35*np.pi*0.037**2/0.145                      # baseball [1/m]
def rzut(kat, v0=45, k=k):
    f = lambda t, y: [y[2], y[3], -k*np.hypot(y[2], y[3])*y[2], -g - k*np.hypot(y[2], y[3])*y[3]]
    upadek = lambda t, y: y[1]; upadek.terminal = True; upadek.direction = -1
    th = np.radians(kat)
    return solve_ivp(f, [0, 20], [0, 0, v0*np.cos(th), v0*np.sin(th)], events=upadek, max_step=0.01, rtol=1e-8)
fig, ax = plt.subplots(1, 3, figsize=(14, 4))
for kk, opis in [(0, "bez oporu"), (k, "z oporem")]:
    s = rzut(45, k=kk)
    ax[0].plot(s.y[0], s.y[1], label=opis)
    print(f"{opis:10s}: zasięg {s.y_events[0][0][0]:6.1f} m, h_max {s.y[1].max():5.1f} m, czas {s.t_events[0][0]:.2f} s")
katy = np.arange(25, 51, 1)
zasiegi = [rzut(a).y_events[0][0][0] for a in katy]
print(f"najlepszy kąt z oporem: {katy[np.argmax(zasiegi)]}°, zasięg {max(zasiegi):.1f} m")
ax[0].set_xlabel("x [m]"); ax[0].set_ylabel("y [m]"); ax[0].legend(); ax[0].set_aspect("equal")

def okres(theta0):                                          # wahadło l = g (T0 = 2π), czas między przejściami przez zero
    f = lambda t, y: [y[1], -np.sin(y[0])]
    przejscie = lambda t, y: y[0]; przejscie.direction = -1
    s = solve_ivp(f, [0, 60], [theta0, 0], events=przejscie, rtol=1e-10, atol=1e-12)
    return np.mean(np.diff(s.t_events[0]))/(2*np.pi)
amp = np.radians([10, 30, 60, 90, 120, 150, 170])
sym = [okres(a) for a in amp]
dok = 2/np.pi*ellipk(np.sin(amp/2)**2)
for a, s_, d_ in zip(np.degrees(amp), sym, dok):
    print(f"θ0 = {a:5.0f}°: T/T0 symulacja {s_:.4f}, całka eliptyczna {d_:.4f}, przybliżenie {1 + np.radians(a)**2/16:.4f}")
ax[1].plot(np.degrees(amp), dok, "o-"); ax[1].set_xlabel("amplituda [°]"); ax[1].set_ylabel("T / T0")

GM, h = 4*np.pi**2, 1e-3                                     # AU, rok
r, v = np.array([0.5, 0.0]), np.array([0.0, np.sqrt(GM*(2/0.5 - 1/1.0))])   # peryhelium orbity a = 1 AU, e = 0,5
acc = lambda r: -GM*r/np.linalg.norm(r)**3
tor, E, przejscia, a_n = [r], [], [], acc(r)
for n in range(3000):                                        # 3 lata
    r_nowe = r + h*v + 0.5*h*h*a_n
    a_nowe = acc(r_nowe); v = v + 0.5*h*(a_n + a_nowe)
    if r[1] < 0 <= r_nowe[1]: przejscia.append((n + 1)*h)    # przejście przez peryhelium
    r, a_n = r_nowe, a_nowe
    tor.append(r); E.append(0.5*v @ v - GM/np.linalg.norm(r))
tor = np.array(tor)
print(f"orbita: okres {np.mean(np.diff(przejscia)):.4f} roku (Kepler: a^1,5 = 1), afelium {np.abs(tor[:, 0]).max():.4f} AU,"
      f" względna zmiana energii {np.ptp(E)/abs(np.mean(E)):.1e}")
ax[2].plot(tor[:, 0], tor[:, 1]); ax[2].plot(0, 0, "y*", ms=15); ax[2].set_aspect("equal"); ax[2].set_xlabel("x [AU]")
plt.tight_layout(); plt.show()
```

## Zadania

### A. Poziom maturalny _(opcjonalnie — rozgrzewka)_

1. Dlaczego przy oporze powietrza najdalej leci się pod kątem mniejszym niż 45°?

<details>
<summary>Odpowiedź</summary>

Przy wyższym torze piłka dłużej przebywa w powietrzu i opór dłużej hamuje jej ruch poziomy. Bardziej płaski tor skraca czas lotu i straty.
</details>

2. Oblicz prędkość graniczną piłki baseballowej z $k = 0{,}0062\ \mathrm{m^{-1}}$. Czy uderzona z prędkością 45 m/s piłka może lecieć szybciej, gdy spada?

<details>
<summary>Odpowiedź</summary>

$v_{gr} = \sqrt{g/k} \approx 40\ \mathrm{m/s}$. Opadając, piłka nie przekroczy tej prędkości (zbliża się do niej od dołu). Na początku lotu jest szybsza (45 m/s), ale tylko dzięki wybiciu.
</details>

### B. Poziom akademicki

1. Zmodyfikuj symulację rzutu dla piłki pingpongowej ($m = 2{,}7\ \mathrm g$, $d = 40\ \mathrm{mm}$, $C_x = 0{,}5$, $v_0 = 20\ \mathrm{m/s}$, 45°). Ile wynosi prędkość graniczna i zasięg?

<details>
<summary>Odpowiedź</summary>

$k \approx 0{,}14\ \mathrm{m^{-1}}$, $v_{gr} \approx 8{,}4\ \mathrm{m/s}$. Zasięg ok. 9,6 m zamiast 41 m w próżni. Tor jest wyraźnie niesymetryczny — piłka spada stromo, pod kątem ok. 70° do poziomu.
</details>

2. Wahadło tłumione i wymuszane: $\ddot\theta = -\sin\theta - 0{,}5\dot\theta + 1{,}2\cos(\tfrac23t)$. Rozwiąż je dla $\theta_0 = 0{,}2$ i $0{,}2 + 10^{-6}$ (prędkość początkowa 0). Kiedy różnica kątów przekroczy 0,5 rad? Co się dzieje dla amplitudy wymuszenia 0,9?

<details>
<summary>Odpowiedź</summary>

Przy amplitudzie 1,2 ruch jest chaotyczny: różnica rośnie wykładniczo i przekracza 0,5 rad po ok. 100 jednostkach czasu (zależnie od tolerancji obliczeń). Przy 0,9 ruch jest okresowy i różnica zanika ($10^{-14}$ po 100 jednostkach).
</details>

3. Dodaj do symulacji orbity Jowisza ($a = 5{,}2\ \mathrm{AU}$, masa $10^{-3}M_\odot$, orbita kołowa, nieruchome Słońce) i kometę na orbicie z $a = 3\ \mathrm{AU}$, $e = 0{,}6$. Czy po 50 latach okres komety się zmienił?

<details>
<summary>Odpowiedź</summary>

Wynik zależy od fazy przelotu w pobliżu Jowisza. Zwykle okres zmienia się o ułamki procenta do kilku procent. Przy bliskim przejściu orbita może zmienić się całkowicie. Tak Jowisz „przechwytuje” komety krótkookresowe.
</details>

4. Sprawdź III prawo Keplera numerycznie: dla orbit o $a = 0{,}5;\ 1;\ 2;\ 4\ \mathrm{AU}$ (dowolne $e$) zmierz okresy i dopasuj prostą do $\log T$ od $\log a$.

<details>
<summary>Odpowiedź</summary>

Nachylenie 1,500 (z dokładnością zależną od kroku), czyli $T \propto a^{3/2}$; okres 1 rok dla $a = 1\ \mathrm{AU}$ niezależnie od mimośrodu.
</details>

## Źródła

- OpenStax, *Fizyka dla szkół wyższych*, t. 1 — §6.4 (siła oporu i prędkość graniczna), §13.5 (prawa Keplera), §15.4 (wahadła).
- Halliday, Resnick, Walker, *Podstawy fizyki*, wyd. 2015, t. 1 — §6.2 (opór); t. 2 — §13.6 (Kepler) i §15.3–15.4 (wahadła).
- Moduły 03.05 (opór ośrodka), 07.04 (prawa Keplera), 09.03 (wahadła).
- M. Newman, *Computational Physics*, rozdz. 8 — przykłady z wahadłem i orbitami (materiał dodatkowy, po angielsku).
