# 02.05 — Rzut poziomy i ukośny

> **Moduł:** [02 — Kinematyka](README.md) · **Poziom:** 🟢 matura R · **Status:** ✅ pełny
>
> **Czytaj:**
>
> - OpenStax, *Fizyka dla szkół wyższych*, t. 1, rozdz. 4: [§4.3](https://openstax.org/books/fizyka-dla-szk%C3%B3%C5%82-wy%C5%BCszych-tom-1/pages/4-3-rzuty) · [wstęp do rozdziału](https://openstax.org/books/fizyka-dla-szk%C3%B3%C5%82-wy%C5%BCszych-tom-1/pages/4-wstep)
> - Halliday, Resnick, Walker, *Podstawy fizyki*, wyd. 2015, t. 1: §4.4 (s. 87)
> - Halliday, Resnick, Walker, *Podstawy fizyki*, wyd. 1 (2003), t. 1: [§4.5–4.6, s. 65](https://home.agh.edu.pl/~czapli/Resnick_1.pdf#page=77) — PDF z serwera AGH

← [Wektory położenia, prędkości i przyspieszenia w 2D i 3D](04-ruch-w-2d-i-3d.md) · [spis modułu](README.md) · [Ruch po okręgu: jednostajny i niejednostajny](06-ruch-po-okregu.md) →

## Po co to jest

Rzut poziomy i ukośny pojawiają się na maturze rozszerzonej praktycznie co roku. To pierwszy ruch, w którym trzeba połączyć dwa niezależne ruchy w jeden: jednostajny w poziomie i jednostajnie zmienny w pionie. Ta sama metoda działa dla elektronu w polu elektrycznym kondensatora (moduł 12) i dla strumienia wody z węża.

## Teoria w pigułce

**Model.** Pomijamy opór powietrza, przyspieszenie $\vec{g}$ jest stałe i skierowane w dół. Oś $x$ poziomo, oś $y$ w górę, start w punkcie $(0,\ h)$ z prędkością $v_0$ pod kątem $\alpha$ do poziomu.

**Rozkład prędkości początkowej:** $v_{0x} = v_0\cos\alpha$, $v_{0y} = v_0\sin\alpha$.

**Równania ruchu** — dwa niezależne ruchy:

$$x = v_0\cos\alpha\cdot t, \qquad y = h + v_0\sin\alpha\cdot t - \tfrac12gt^2,$$

$$v_x = v_0\cos\alpha = \text{const}, \qquad v_y = v_0\sin\alpha - gt.$$

**Tor** otrzymujemy, eliminując czas: $t = x/(v_0\cos\alpha)$, więc

$$y = h + x\tan\alpha - \frac{g}{2v_0^2\cos^2\alpha}\,x^2$$

— parabola z ramionami w dół.

**Rzut poziomy** to przypadek $\alpha = 0$: ciało spada tak samo jak puszczone swobodnie, a jednocześnie przesuwa się w poziomie. Czas lotu z wysokości $h$ nie zależy od prędkości poziomej: $t = \sqrt{2h/g}$.

**Rzut ukośny z poziomu ziemi** ($h = 0$):
- czas lotu $t_c = \dfrac{2v_0\sin\alpha}{g}$,
- największa wysokość $h_{\max} = \dfrac{v_0^2\sin^2\alpha}{2g}$ (gdy $v_y = 0$),
- zasięg $z = \dfrac{v_0^2\sin2\alpha}{g}$ — największy dla $\alpha = 45^\circ$; kąty $\alpha$ i $90^\circ - \alpha$ dają ten sam zasięg.

**Prędkość w dowolnym punkcie** to suma wektorowa składowych: $v = \sqrt{v_x^2 + v_y^2}$, kierunek $\tan\beta = v_y/v_x$ — zawsze styczny do toru.

## Wzory i założenia

| Wzór | Znaczenie | Kiedy obowiązuje |
|---|---|---|
| $t = \sqrt{2h/g}$, $\ z = v_0\sqrt{2h/g}$ | rzut poziomy z wysokości $h$ | bez oporu |
| $t_c = 2v_0\sin\alpha/g$ | czas lotu | start i lądowanie na tej samej wysokości |
| $h_{\max} = v_0^2\sin^2\alpha/(2g)$ | wysokość maksymalna | względem punktu startu |
| $z = v_0^2\sin2\alpha/g$ | zasięg | start i lądowanie na tej samej wysokości |
| $y = x\tan\alpha - \dfrac{gx^2}{2v_0^2\cos^2\alpha}$ | równanie toru | start z $(0,\ 0)$ |
| $v^2 = v_0^2 - 2g(y - y_0)$ | szybkość na wysokości $y$ | z zasady zachowania energii lub z ruchu w pionie |

## Przykład rozwiązany

**Zadanie 1.** Piłkarz kopie piłkę z prędkością 20 m/s pod kątem $30^\circ$ do poziomu. Oblicz czas lotu, zasięg i największą wysokość.

- $v_{0x} = 20\cos30^\circ \approx 17{,}3\ \mathrm{m/s}$, $v_{0y} = 20\sin30^\circ = 10\ \mathrm{m/s}$.
- Czas lotu: $t_c = 2\cdot10/9{,}81 \approx 2{,}04\ \mathrm{s}$.
- Zasięg: $z = 17{,}3\cdot2{,}04 \approx 35{,}3\ \mathrm{m}$ (ze wzoru: $400\sin60^\circ/9{,}81$ — to samo).
- Wysokość maksymalna: $h_{\max} = 10^2/(2\cdot9{,}81) \approx 5{,}1\ \mathrm{m}$.

**Zadanie 2.** Kulka stacza się ze stołu o wysokości 1,25 m i upada 2,0 m od jego krawędzi. Z jaką prędkością opuściła stół?

Czas spadku: $t = \sqrt{2\cdot1{,}25/9{,}81} \approx 0{,}505\ \mathrm{s}$. Prędkość pozioma: $v_0 = 2{,}0/0{,}505 \approx 3{,}96\ \mathrm{m/s}$.

To prosta metoda pomiaru prędkości — wystarczą linijka i taśma.

## Typowe pułapki

- **Wzór na zasięg przy różnych wysokościach.** $z = v_0^2\sin2\alpha/g$ działa tylko, gdy ciało ląduje na wysokości startu. Przy rzucie z dachu trzeba rozwiązać równanie $y(t) = 0$.
- **Prędkość w najwyższym punkcie.** Nie jest zerowa — zostaje składowa pozioma $v_0\cos\alpha$.
- **Mylenie $\sin$ i $\cos$ przy rozkładzie.** Kąt mierzony od poziomu: $v_x = v_0\cos\alpha$. Jeśli kąt jest mierzony od pionu, funkcje się zamieniają.
- **Czas lotu w rzucie poziomym zależy od $v_0$.** Nie zależy — tylko od wysokości.
- **45° zawsze daje największy zasięg.** Tylko bez oporu powietrza i przy starcie z poziomu ziemi. Przy starcie z wysokości optymalny kąt jest mniejszy, a opór powietrza też go zmniejsza.

## Doświadczenie / symulacja

**Symulacja PhET:** *Ruch pocisku* (*Projectile Motion*, [phet.colorado.edu/pl](https://phet.colorado.edu/pl/)). Sprawdź, że kąty $30^\circ$ i $60^\circ$ dają ten sam zasięg, a potem włącz opór powietrza i znajdź kąt największego zasięgu.

**Doświadczenie.** Wyznacz prędkość kulki staczającej się z równi ustawionej na stole metodą z przykładu 2: zmierz wysokość stołu i odległość upadku (połóż kartkę z kalką). Powtórz 5 razy i oblicz niepewność.

**Python:** tor z oporem powietrza i bez. Opór kwadratowy $F = \tfrac12C\rho Av^2$ dla piłki nożnej; równanie ruchu rozwiązujemy numerycznie.

```python
import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp

g, m = 9.81, 0.43                       # piłka nożna: masa [kg]
C, rho, A = 0.25, 1.2, np.pi*0.11**2     # współczynnik oporu, gęstość powietrza, przekrój
k = 0.5 * C * rho * A / m

def rhs(t, s):
    x, y, vx, vy = s
    v = np.hypot(vx, vy)
    return [vx, vy, -k*v*vx, -g - k*v*vy]

def hit_ground(t, s): return s[1]
hit_ground.terminal, hit_ground.direction = True, -1

v0 = 25.0
for deg in (30, 40, 45, 50):
    a = np.radians(deg)
    sol = solve_ivp(rhs, (0, 10), [0, 0, v0*np.cos(a), v0*np.sin(a)], events=hit_ground, max_step=0.01)
    z_vac = v0**2 * np.sin(2*a) / g
    print(f"{deg}°: zasięg z oporem {sol.y[0, -1]:5.1f} m, w próżni {z_vac:5.1f} m")
    plt.plot(sol.y[0], sol.y[1], label=f"{deg}° z oporem")

a = np.radians(45); x = np.linspace(0, v0**2/g, 200)
plt.plot(x, x*np.tan(a) - g*x**2/(2*v0**2*np.cos(a)**2), "k--", label="45° w próżni")
plt.xlabel("x [m]"); plt.ylabel("y [m]"); plt.ylim(bottom=0); plt.grid(True); plt.legend(); plt.show()
```

## Zadania

### A. Poziom maturalny

1. Z wysokości 45 m wyrzucono poziomo kamień z prędkością 10 m/s. Oblicz czas lotu, zasięg i prędkość uderzenia w ziemię.

<details>
<summary>Odpowiedź</summary>

$t \approx 3{,}03\ \mathrm{s}$; $z \approx 30{,}3\ \mathrm{m}$; $v = \sqrt{10^2 + 2\cdot9{,}81\cdot45} \approx 31{,}4\ \mathrm{m/s}$.
</details>

2. Pod jakimi kątami trzeba wyrzucić piłkę z prędkością 20 m/s, żeby upadła 30 m dalej (na tym samym poziomie)?

<details>
<summary>Odpowiedź</summary>

$\sin2\alpha = 30\cdot9{,}81/400 \approx 0{,}736$; $\alpha \approx 23{,}7^\circ$ lub $66{,}3^\circ$.
</details>

3. Pokaż, że dla rzutu pod kątem $45^\circ$ zasięg jest cztery razy większy od wysokości maksymalnej.

<details>
<summary>Odpowiedź</summary>

$z = v_0^2/g$, $h_{\max} = v_0^2/(4g)$.
</details>

4. W najwyższym punkcie toru piłka ma prędkość 12 m/s, a wcześniej wzniosła się na 5 m. Z jaką prędkością i pod jakim kątem ją wyrzucono?

<details>
<summary>Odpowiedź</summary>

$v_{0x} = 12\ \mathrm{m/s}$, $v_{0y} = \sqrt{2\cdot9{,}81\cdot5} \approx 9{,}9\ \mathrm{m/s}$; $v_0 \approx 15{,}6\ \mathrm{m/s}$, $\alpha \approx 39{,}5^\circ$.
</details>

5. Dwie kulki spadają z tej samej wysokości: jedna puszczona swobodnie, druga wyrzucona poziomo. Która uderzy w ziemię pierwsza?

<details>
<summary>Odpowiedź</summary>

Jednocześnie — ruch w pionie jest taki sam.
</details>

### B. Poziom akademicki _(opcjonalnie — rozszerzenie z rachunkiem)_

1. Z urwiska o wysokości 20 m wyrzucono kamień z prędkością 15 m/s pod kątem $30^\circ$ w górę. Oblicz czas lotu i odległość upadku od podnóża.

<details>
<summary>Odpowiedź</summary>

$-20 = 7{,}5t - 4{,}905t^2 \Rightarrow t \approx 2{,}92\ \mathrm{s}$; $x = 15\cos30^\circ\cdot2{,}92 \approx 38{,}0\ \mathrm{m}$.
</details>

2. Wyprowadź z równania toru, że zasięg (przy $h = 0$) jest największy dla $\alpha = 45^\circ$, różniczkując $z(\alpha)$.

<details>
<summary>Odpowiedź</summary>

$\dfrac{dz}{d\alpha} = \dfrac{2v_0^2\cos2\alpha}{g} = 0 \Rightarrow \alpha = 45^\circ$.
</details>

3. Przy starcie z wysokości $h$ optymalny kąt spełnia $\tan\alpha = \dfrac{v_0}{\sqrt{v_0^2 + 2gh}}$. Oblicz go dla $v_0 = 10\ \mathrm{m/s}$, $h = 2\ \mathrm{m}$ (pchnięcie kulą) i porównaj zasięg z zasięgiem dla $45^\circ$.

<details>
<summary>Odpowiedź</summary>

$\alpha \approx 40{,}3^\circ$; zasięg ok. $12{,}03\ \mathrm{m}$ wobec $11{,}91\ \mathrm{m}$ dla $45^\circ$.
</details>

4. Z wierzchołka równi nachylonej pod kątem $\beta$ wyrzucono poziomo ciało z prędkością $v_0$. Po jakim czasie upadnie na równię?

<details>
<summary>Odpowiedź</summary>

Warunek $y/x = -\tan\beta$: $\dfrac{gt^2/2}{v_0t} = \tan\beta \Rightarrow t = \dfrac{2v_0\tan\beta}{g}$.
</details>

### C. Zadania z arkuszy maturalnych CKE

Zadania z egzaminów maturalnych (poziom rozszerzony, formuła 2023), w których ten temat jest potrzebny. Rozwiąż je samodzielnie, a potem porównaj z zasadami oceniania. Pełne zestawienie: [matura/README.md](../../matura/README.md).

- Maj 2025, zad. 1.1 — rzut poziomy jako złożenie ruchów ([arkusz](https://www.oke.poznan.pl/files/cms/875/mfap_r0_100_a_2505_arkusz.pdf), [zasady oceniania](https://cke.gov.pl/egzamin-maturalny/egzamin-maturalny-w-formule-2023/arkusze/2025-2/))
- Maj 2025, zad. 1.2 — dwie kulki w polu grawitacyjnym — prędkość początkowa ([arkusz](https://www.oke.poznan.pl/files/cms/875/mfap_r0_100_a_2505_arkusz.pdf), [zasady oceniania](https://cke.gov.pl/egzamin-maturalny/egzamin-maturalny-w-formule-2023/arkusze/2025-2/))

## Źródła

- OpenStax, *Fizyka dla szkół wyższych*, t. 1, rozdz. 4 — §4.3: rzuty, z przykładami i zadaniami.
- Halliday, Resnick, Walker, *Podstawy fizyki* — wyd. 2015: t. 1, §4.4; wyd. 1: t. 1, §4.5–4.6.
- Symulacja PhET *Ruch pocisku*.
