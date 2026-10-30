# 06.06 — Precesja żyroskopu

> **Moduł:** [06 — Bryła sztywna, statyka i sprężystość](README.md) · **Poziom:** 🔵 studia · **Status:** ✅ pełny
>
> **Czytaj:**
>
> - OpenStax, *Fizyka dla szkół wyższych*, t. 1, rozdz. 11: [§11.4](https://openstax.org/books/fizyka-dla-szk%C3%B3%C5%82-wy%C5%BCszych-tom-1/pages/11-4-precesja-zyroskopu) · [wstęp do rozdziału](https://openstax.org/books/fizyka-dla-szk%C3%B3%C5%82-wy%C5%BCszych-tom-1/pages/11-wstep)
> - Halliday, Resnick, Walker, *Podstawy fizyki*, wyd. 2015, t. 1: §11.9 (s. 403)

← [Moment pędu i zasada jego zachowania](05-moment-pedu.md) · [spis modułu](README.md) · [Równowaga statyczna, naprężenia i prawo Hooke'a](07-rownowaga-i-sprezystosc.md) →

## Po co to jest

Wirujący bąk nie przewraca się, tylko powoli obraca oś wokół pionu; koło rowerowe trzymane za koniec osi „wisi” w powietrzu. To precesja — skutek wektorowej natury momentu pędu. Wyjaśnia, dlaczego rower stabilizuje się w ruchu, jak działają żyrokompasy i żyroskopy nawigacyjne, dlaczego oś Ziemi zatacza stożek w ciągu 26 tysięcy lat i jak działa rezonans magnetyczny (precesja spinów w polu magnetycznym, 21).

## Teoria w pigułce

**Moment siły zmienia kierunek, a nie tylko wartość $\vec{L}$.** Z $\vec{\tau} = d\vec{L}/dt$ wynika, że zmiana momentu pędu $d\vec{L}$ ma kierunek momentu siły. Gdy $\vec{\tau}$ jest prostopadły do $\vec{L}$, wartość $L$ się nie zmienia, a wektor $\vec{L}$ obraca się — oś bąka „ucieka w bok” zamiast opadać.

**Żyroskop podparty na końcu osi.** Koło o momencie pędu $L = I\omega$ (wzdłuż poziomej osi) jest podparte w punkcie odległym o $d$ od środka masy. Ciężar daje moment $\tau = Mgd$, poziomy i prostopadły do osi. W czasie $dt$ wektor $\vec{L}$ obraca się w poziomie o kąt $d\phi = \tau\,dt/L$. **Prędkość kątowa precesji**:

$$\Omega = \frac{d\phi}{dt} = \frac{\tau}{L} = \frac{Mgd}{I\omega}.$$

Im szybciej wiruje koło, tym wolniejsza precesja. Wzór jest przybliżeniem dla $\omega \gg \Omega$ (tzw. szybki bąk); dokładniej na precesję nakładają się drgania osi (nutacja).

**Precesja osi Ziemi.** Ziemia jest spłaszczona, a jej równik nachylony do płaszczyzny orbity. Przyciąganie Słońca i Księżyca działa na zgrubienie równikowe momentem siły, który próbuje „wyprostować” oś. Skutek: oś Ziemi zatacza stożek z okresem ok. 25 800 lat (precesja punktów równonocy). Za ok. 12 tys. lat gwiazdą polarną będzie Wega.

## Wzory i założenia

| Wzór | Znaczenie | Kiedy obowiązuje |
|---|---|---|
| $d\vec{L} = \vec{\tau}\,dt$ | zmiana momentu pędu | — |
| $\Omega = \dfrac{\tau}{L} = \dfrac{Mgd}{I\omega}$ | prędkość kątowa precesji | $\omega \gg \Omega$, oś pozioma |
| $\Omega = \dfrac{Mgd}{I\omega}$ (niezależnie od kąta) | bąk nachylony pod kątem do pionu | ten sam wynik — kąt się skraca |
| $T_p = 2\pi/\Omega$ | okres precesji | — |

## Przykład rozwiązany

### Wersja z rachunkiem różniczkowym i całkowym

**Zadanie.** Koło rowerowe (obręcz o masie 2 kg i promieniu 0,3 m) wiruje z prędkością 10 obr/s. Trzymamy je za koniec osi w odległości 15 cm od środka koła, oś pozioma, a potem puszczamy jedną ręką — koło zawieszone na sznurku za koniec osi. Oblicz okres precesji.

- $I = MR^2 = 2\cdot0{,}09 = 0{,}18\ \mathrm{kg\cdot m^2}$, $\omega = 20\pi \approx 62{,}8\ \mathrm{rad/s}$, $L = I\omega \approx 11{,}3\ \mathrm{kg\cdot m^2/s}$.
- $\tau = Mgd = 2\cdot9{,}81\cdot0{,}15 \approx 2{,}94\ \mathrm{N\cdot m}$.
- $\Omega = \tau/L \approx 0{,}26\ \mathrm{rad/s}$, $T_p = 2\pi/\Omega \approx 24\ \mathrm{s}$.

**Sprawdzenie założenia.** $\Omega \approx 0{,}26 \ll \omega \approx 63\ \mathrm{rad/s}$ — przybliżenie szybkiego bąka jest uzasadnione. Gdy koło zwolni (tarcie), precesja przyspieszy, aż w końcu koło opadnie.

**Wyprowadzenie.** Wektor $\vec{L}$ o stałej długości obraca się w poziomie: $\vec{L}(t) = L(\cos\Omega t,\ \sin\Omega t,\ 0)$, więc $\dfrac{d\vec{L}}{dt} = L\Omega(-\sin\Omega t,\ \cos\Omega t,\ 0)$ — wektor poziomy, prostopadły do $\vec{L}$, o długości $L\Omega$. Porównując z $\vec{\tau}$ (też poziomy i prostopadły do osi): $L\Omega = \tau$.

## Typowe pułapki

- **„Żyroskop przeczy grawitacji”.** Nie: siła naciągu sznurka równoważy ciężar (środek masy nie spada), a moment ciężaru obraca $\vec{L}$ w poziomie.
- **Precesja szybsza przy szybszym wirowaniu.** Odwrotnie — $\Omega \propto 1/\omega$.
- **Kierunek precesji.** Wyznacz go z $d\vec{L} \parallel \vec{\tau}$ (reguła prawej dłoni), a nie z intuicji.
- **Precesja a nutacja.** Wzór $\Omega = \tau/L$ opisuje średni ruch osi; drgania osi w górę i w dół (nutacja) to osobne zjawisko.

## Doświadczenie / symulacja

**Koło rowerowe i krzesło obrotowe.** Usiądź na obrotowym krześle z rozkręconym kołem rowerowym trzymanym poziomo za oś. Obróć oś koła do pionu — zaczniesz się obracać w przeciwną stronę (zachowanie momentu pędu układu).

**Bąk z telefonem.** Postaw telefon w etui na bąku-podstawce albo przyklej go do dużego bąka (ostrożnie!) i zmierz żyroskopem w phyphox prędkość wirowania i — po składowych — prędkość precesji. Sprawdź, czy ich iloczyn jest w przybliżeniu stały, gdy bąk zwalnia.

**Python:** numeryczne potwierdzenie precesji — obrót wektora $\vec{L}$ pod działaniem momentu prostopadłego.

```python
import numpy as np
import matplotlib.pyplot as plt

M, g, d, I, w = 2.0, 9.81, 0.15, 0.18, 20*np.pi
L = np.array([I*w, 0.0, 0.0])             # oś koła wzdłuż x
dt, T = 1e-3, 30.0
traj = []
for _ in range(int(T/dt)):
    r = d * L / np.linalg.norm(L)          # punkt podparcia → środek masy wzdłuż osi
    tau = np.cross(r, np.array([0, 0, -M*g]))
    L = L + tau*dt
    traj.append(L.copy())
traj = np.array(traj)
phi = np.unwrap(np.arctan2(traj[:, 1], traj[:, 0]))
Omega = phi[-1]/T
print(f"Ω numerycznie = {Omega:.4f} rad/s, wzór τ/L = {M*g*d/(I*w):.4f} rad/s, okres {2*np.pi/abs(Omega):.1f} s")
plt.plot(traj[:, 0], traj[:, 1]); plt.axis("equal"); plt.xlabel("L_x"); plt.ylabel("L_y"); plt.grid(True); plt.show()
```

## Zadania

### A. Poziom maturalny _(opcjonalnie — rozgrzewka)_

1. Dlaczego jadący rower łatwiej utrzymać w równowadze niż stojący? Jaką rolę grają koła?

<details>
<summary>Odpowiedź</summary>

Wirujące koła mają moment pędu; przechylenie roweru daje moment siły, który obraca oś koła (skręca kierownicę) w stronę przechyłu, co pomaga odzyskać równowagę. (W praktyce ważniejsza jest geometria widelca i odruchy rowerzysty, ale efekt żyroskopowy też działa.)
</details>

2. Co stanie się z prędkością precesji bąka, gdy jego wirowanie zwalnia na skutek tarcia?

<details>
<summary>Odpowiedź</summary>

Wzrośnie ($\Omega \propto 1/\omega$), aż bąk się przewróci.
</details>

### B. Poziom akademicki

1. W przykładzie zwiększamy prędkość wirowania koła do 20 obr/s i przesuwamy punkt zawieszenia na 10 cm od środka. Oblicz nowy okres precesji.

<details>
<summary>Odpowiedź</summary>

$\Omega = \dfrac{2\cdot9{,}81\cdot0{,}1}{0{,}18\cdot40\pi} \approx 0{,}087\ \mathrm{rad/s}$, $T_p \approx 72\ \mathrm{s}$.
</details>

2. Precesja osi Ziemi ma okres ok. 25 800 lat. Oszacuj średni moment siły działający na Ziemię, przyjmując $L \approx 5{,}9\cdot10^{33}\ \mathrm{kg\cdot m^2/s}$. (Uwaga: oś jest nachylona pod kątem $23{,}4^\circ$; zaniedbaj ten szczegół.)

<details>
<summary>Odpowiedź</summary>

$\Omega = 2\pi/(25\,800\cdot3{,}16\cdot10^7\ \mathrm{s}) \approx 7{,}7\cdot10^{-12}\ \mathrm{rad/s}$; $\tau \approx \Omega L \approx 4{,}5\cdot10^{22}\ \mathrm{N\cdot m}$.
</details>

3. Pokaż, że prędkość precesji bąka nachylonego pod kątem $\theta$ do pionu nie zależy od $\theta$.

<details>
<summary>Odpowiedź</summary>

Moment ciężaru $\tau = Mgd\sin\theta$; zmienia się tylko pozioma składowa $\vec{L}$, o długości $L\sin\theta$, obracająca się z prędkością $\Omega$: $L\sin\theta\cdot\Omega = Mgd\sin\theta \Rightarrow \Omega = Mgd/L$.
</details>

## Źródła

- OpenStax, *Fizyka dla szkół wyższych*, t. 1, rozdz. 11 — §11.4: precesja żyroskopu, z przykładem precesji Ziemi.
- Halliday, Resnick, Walker, *Podstawy fizyki*, wyd. 2015, t. 1, §11.9 — precesja żyroskopu.
