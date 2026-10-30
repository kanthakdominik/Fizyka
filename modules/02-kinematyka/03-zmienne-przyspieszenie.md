# 02.03 — Ruch o zmiennym przyspieszeniu — całkowanie a(t)

> **Moduł:** [02 — Kinematyka](README.md) · **Poziom:** 🔵 studia · **Status:** ✅ pełny
>
> **Czytaj:**
>
> - OpenStax, *Fizyka dla szkół wyższych*, t. 1, rozdz. 3: [§3.6](https://openstax.org/books/fizyka-dla-szk%C3%B3%C5%82-wy%C5%BCszych-tom-1/pages/3-6-wyznaczanie-rownan-ruchu-metoda-calkowania) · [wstęp do rozdziału](https://openstax.org/books/fizyka-dla-szk%C3%B3%C5%82-wy%C5%BCszych-tom-1/pages/3-wstep)
> - Halliday, Resnick, Walker, *Podstawy fizyki*, wyd. 2015, t. 1: §2.6 (s. 36)
> - Halliday, Resnick, Walker, *Podstawy fizyki*, wyd. 1 (2003), t. 1: [§2.7, s. 26](https://home.agh.edu.pl/~czapli/Resnick_1.pdf#page=38) — PDF z serwera AGH

← [Ruch jednostajnie zmienny i spadek swobodny](02-ruch-jednostajnie-zmienny.md) · [spis modułu](README.md) · [Wektory położenia, prędkości i przyspieszenia w 2D i 3D](04-ruch-w-2d-i-3d.md) →

## Po co to jest

W rzeczywistości przyspieszenie rzadko jest stałe: samochód rusza z przyspieszeniem malejącym wraz z prędkością, łódź po wyłączeniu silnika hamuje coraz słabiej, rakieta przyspiesza coraz mocniej, bo traci masę. Wzorów z tematu 02 nie da się wtedy użyć. Ten temat pokazuje ogólną metodę — całkowanie — i trzy typowe przypadki: przyspieszenie zależne od czasu, od prędkości i od położenia. To podstawa każdego równania ruchu na studiach.

## Teoria w pigułce

**Zależność od czasu: $a = a(t)$.** Całkujemy dwa razy, za każdym razem dodając warunek początkowy:

$$v(t) = v_0 + \int_0^t a(t')\,dt', \qquad x(t) = x_0 + \int_0^t v(t')\,dt'.$$

**Zależność od prędkości: $a = a(v)$** (np. opór ośrodka). Rozdzielamy zmienne:

$$\frac{dv}{dt} = a(v) \ \Rightarrow\ t = \int_{v_0}^{v}\frac{dv'}{a(v')}.$$

Z tego dostajemy $v(t)$, a potem $x(t)$ przez całkowanie. Jeśli interesuje nas droga, a nie czas, wygodniej użyć $a = v\,\dfrac{dv}{dx}$:

$$x - x_0 = \int_{v_0}^{v}\frac{v'\,dv'}{a(v')}.$$

**Zależność od położenia: $a = a(x)$** (np. siła sprężystości, grawitacja). Z $a = v\,\dfrac{dv}{dx}$:

$$\tfrac12v^2 - \tfrac12v_0^2 = \int_{x_0}^{x}a(x')\,dx'.$$

To jest twierdzenie o pracy i energii (moduł 04) w przebraniu kinematycznym: dostajemy prędkość jako funkcję położenia bez rozwiązywania równania ruchu.

**Graficznie.** Pole pod wykresem $a(t)$ to zmiana prędkości, pole pod $v(t)$ — przemieszczenie. Gdy wykres składa się z odcinków, całkowanie to dodawanie pól trapezów i prostokątów.

## Wzory i założenia

| Dane | Metoda | Wynik |
|---|---|---|
| $a(t)$ | całkuj po czasie | $v(t) = v_0 + \int a\,dt$, $\ x(t) = x_0 + \int v\,dt$ |
| $a(v)$ | rozdziel zmienne | $t = \int dv/a(v)$, $\ \Delta x = \int v\,dv/a(v)$ |
| $a(x)$ | $a = v\,dv/dx$ | $v^2 = v_0^2 + 2\int a\,dx$ |
| $a = -kv$ | — | $v = v_0e^{-kt}$, $\ x = \dfrac{v_0}{k}(1 - e^{-kt})$, droga do zatrzymania $v_0/k$ |
| $a = -kv^2$ | — | $v = \dfrac{v_0}{1 + kv_0t}$, $\ v(x) = v_0e^{-kx}$ |

## Przykład rozwiązany

### Wersja z rachunkiem różniczkowym i całkowym

**Zadanie 1 — $a(t)$.** Wózek rusza z miejsca, a jego przyspieszenie maleje liniowo: $a(t) = 2 - 0{,}5t$ (m/s², s). Wyznacz $v(t)$ i $x(t)$, największą prędkość i miejsce zatrzymania.

$$v(t) = \int_0^t(2 - 0{,}5t')\,dt' = 2t - 0{,}25t^2, \qquad x(t) = \int_0^t v\,dt' = t^2 - \frac{t^3}{12}.$$

- Prędkość jest największa, gdy $a = 0$: $t = 4\ \mathrm{s}$, $v_{\max} = 8 - 4 = 4\ \mathrm{m/s}$.
- Wózek zatrzymuje się, gdy $v = 0$: $t = 8\ \mathrm{s}$, $x(8) = 64 - \tfrac{512}{12} \approx 21{,}3\ \mathrm{m}$.

**Zadanie 2 — $a(v)$.** Motorówka płynie z prędkością $v_0 = 10\ \mathrm{m/s}$; po wyłączeniu silnika woda hamuje ją tak, że $a = -kv$, $k = 0{,}5\ \mathrm{s^{-1}}$. Jak daleko dopłynie? Po jakim czasie prędkość spadnie do 1 m/s?

$$\frac{dv}{v} = -k\,dt \Rightarrow v = v_0e^{-kt}, \qquad x(t) = \int_0^tv_0e^{-kt'}dt' = \frac{v_0}{k}\left(1 - e^{-kt}\right).$$

- Droga do zatrzymania (dla $t \to \infty$): $v_0/k = 20\ \mathrm{m}$ — skończona, choć czas nieskończony.
- $v = 1\ \mathrm{m/s}$ po $t = \dfrac{\ln10}{k} \approx 4{,}6\ \mathrm{s}$.

**Sprawdzenie.** Jednostka $v_0/k$: $\dfrac{\mathrm{m/s}}{\mathrm{1/s}} = \mathrm{m}$. Dla małych $t$: $x \approx v_0t$ — na początku łódź płynie prawie jednostajnie. Zgadza się.

## Typowe pułapki

- **$x = \tfrac12at^2$ przy zmiennym $a$.** Ten wzór obowiązuje tylko dla stałego przyspieszenia.
- **Zgubione warunki początkowe.** Każde całkowanie wprowadza stałą; wyznacz ją z $v_0$ i $x_0$.
- **Całkowanie po złej zmiennej.** Gdy $a$ zależy od $v$, nie wolno pisać $v = \int a(v)\,dt$ tak, jakby $a$ było funkcją czasu — trzeba rozdzielić zmienne.
- **Mylenie maksimum prędkości i zatrzymania.** Największa prędkość jest tam, gdzie $a = 0$; zatrzymanie — gdzie $v = 0$.

## Doświadczenie / symulacja

**Pomiar.** Nagraj w phyphox (*Acceleration (without g)*) przyspieszenie telefonu, który pchasz po stole i puszczasz — tak, żeby hamował na tarciu. Scałkuj dane numerycznie i sprawdź, czy prędkość po zatrzymaniu wraca do zera (projekt modułu 00).

**Python:** całkowanie numeryczne równania ruchu dla przyspieszenia zależnego od prędkości i porównanie z rozwiązaniem dokładnym.

```python
import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp

k, v0 = 0.5, 10.0

def rhs(t, y):                      # y = [x, v]
    x, v = y
    return [v, -k * v]

sol = solve_ivp(rhs, (0, 12), [0.0, v0], dense_output=True, rtol=1e-8)
t = np.linspace(0, 12, 200)
x, v = sol.sol(t)
print(f"x(12 s) = {x[-1]:.3f} m (granica v0/k = {v0/k} m)")
print(f"v = 1 m/s po t = {np.log(10)/k:.2f} s; numerycznie v(4,6 s) = {sol.sol(4.605)[1]:.3f} m/s")

fig, ax = plt.subplots(1, 2, figsize=(9, 3.5))
ax[0].plot(t, v); ax[0].set_xlabel("t [s]"); ax[0].set_ylabel("v [m/s]"); ax[0].grid(True)
ax[1].plot(t, x); ax[1].axhline(v0/k, ls="--", color="gray")
ax[1].set_xlabel("t [s]"); ax[1].set_ylabel("x [m]"); ax[1].grid(True)
plt.tight_layout(); plt.show()
```

## Zadania

### A. Poziom maturalny _(opcjonalnie — rozgrzewka)_

1. Ciało rusza z miejsca. Przez pierwsze 3 s ma przyspieszenie $2\ \mathrm{m/s^2}$, przez kolejne 2 s porusza się bez przyspieszenia, a potem hamuje z opóźnieniem $3\ \mathrm{m/s^2}$ aż do zatrzymania. Narysuj wykres $v(t)$ i oblicz całą drogę.

<details>
<summary>Odpowiedź</summary>

$v_{\max} = 6\ \mathrm{m/s}$; hamowanie trwa 2 s. Droga $= 9 + 12 + 6 = 27\ \mathrm{m}$.
</details>

2. Wykres $a(t)$ to trójkąt: przyspieszenie rośnie liniowo od 0 do $4\ \mathrm{m/s^2}$ w ciągu 2 s, a potem maleje liniowo do zera w ciągu kolejnych 2 s. Ciało startuje z miejsca. Jaką ma prędkość po 4 s?

<details>
<summary>Odpowiedź</summary>

Pole pod $a(t)$: $\tfrac12\cdot4\cdot4 = 8\ \mathrm{m/s}$.
</details>

### B. Poziom akademicki

1. $a(t) = 6t - 4$ (m/s², s), $v_0 = 2\ \mathrm{m/s}$, $x_0 = 1\ \mathrm{m}$. Wyznacz $v(t)$, $x(t)$ i ich wartości dla $t = 2\ \mathrm{s}$.

<details>
<summary>Odpowiedź</summary>

$v = 3t^2 - 4t + 2$, $x = t^3 - 2t^2 + 2t + 1$; $v(2) = 6\ \mathrm{m/s}$, $x(2) = 5\ \mathrm{m}$.
</details>

2. Ciało startuje z miejsca z przyspieszeniem $a(t) = A\sin(\omega t)$. Wyznacz $v(t)$ i $x(t)$. Czy ciało drga wokół punktu startu?

<details>
<summary>Odpowiedź</summary>

$v = \dfrac{A}{\omega}(1 - \cos\omega t) \ge 0$, $x = \dfrac{A}{\omega}t - \dfrac{A}{\omega^2}\sin\omega t$. Nie — ciało „pulsuje”, ale dryfuje do przodu ze średnią prędkością $A/\omega$.
</details>

3. Dla motorówki z przykładu ($v_0 = 10\ \mathrm{m/s}$, $a = -kv$, $k = 0{,}5\ \mathrm{s^{-1}}$) oblicz drogę przebytą do chwili, gdy prędkość spadnie do 1 m/s.

<details>
<summary>Odpowiedź</summary>

$\Delta x = (v_0 - v)/k = 18\ \mathrm{m}$.
</details>

4. Łódź hamuje z oporem kwadratowym: $a = -kv^2$, $k = 0{,}02\ \mathrm{m^{-1}}$, $v_0 = 20\ \mathrm{m/s}$. Jaką drogę przebędzie, zanim zwolni do 5 m/s?

<details>
<summary>Odpowiedź</summary>

$v\,\dfrac{dv}{dx} = -kv^2 \Rightarrow v = v_0e^{-kx}$; $x = \dfrac{\ln4}{0{,}02} \approx 69{,}3\ \mathrm{m}$.
</details>

5. Przyspieszenie maleje wykładniczo: $a(t) = a_0e^{-t/\tau}$, ciało startuje z miejsca. Do jakiej prędkości dąży?

<details>
<summary>Odpowiedź</summary>

$v(t) = a_0\tau(1 - e^{-t/\tau}) \to a_0\tau$.
</details>

6. Ciało porusza się wzdłuż osi $x$ z przyspieszeniem $a(x) = -4x$ (m/s², m). W punkcie $x = 0$ ma prędkość 6 m/s. Jak daleko od początku się oddali?

<details>
<summary>Odpowiedź</summary>

$v^2 = 36 - 4x^2$; $v = 0$ dla $x = 3\ \mathrm{m}$ (to ruch harmoniczny o amplitudzie 3 m).
</details>

## Źródła

- OpenStax, *Fizyka dla szkół wyższych*, t. 1, rozdz. 3 — §3.6: wyznaczanie równań ruchu metodą całkowania.
- Halliday, Resnick, Walker, *Podstawy fizyki* — wyd. 2015: t. 1, §2.6 (całkowanie graficzne); wyd. 1: t. 1, §2.7.
