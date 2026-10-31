# 02 — ściąga: Kinematyka

Wszystkie tabele **Wzory i założenia** z tematów modułu na jednej stronie — do powtórki i do sprawdzenia, czy pamiętasz, **kiedy** wolno użyć wzoru. Wyprowadzenia, przykłady i zadania są w tematach.

[← spis modułu](README.md)

## [02.01 — Ruch prostoliniowy: położenie, prędkość, przyspieszenie](01-ruch-prostoliniowy.md)

| Wzór | Znaczenie | Kiedy obowiązuje |
|---|---|---|
| $\Delta x = x_2 - x_1$ | przemieszczenie | zawsze; znak zależy od zwrotu osi |
| $\bar{v} = \Delta x/\Delta t$ | prędkość średnia | zawsze |
| $\bar{v}_s = s/\Delta t$ | szybkość średnia | zawsze; $\bar{v}_s \ge \lvert\bar{v}\rvert$ |
| $v = dx/dt$ | prędkość chwilowa | nachylenie stycznej do $x(t)$ |
| $a = dv/dt$ | przyspieszenie chwilowe | nachylenie stycznej do $v(t)$ |
| $\Delta x = \int v\,dt$ | przemieszczenie z prędkości | pole pod $v(t)$ ze znakiem |
| $1\ \mathrm{m/s} = 3{,}6\ \mathrm{km/h}$ | przelicznik | — |

## [02.02 — Ruch jednostajnie zmienny i spadek swobodny](02-ruch-jednostajnie-zmienny.md)

| Wzór | Brakująca wielkość | Kiedy obowiązuje |
|---|---|---|
| $v = v_0 + at$ | położenie | $a = \text{const}$ |
| $x = x_0 + v_0t + \tfrac12at^2$ | prędkość końcowa | $a = \text{const}$ |
| $v^2 = v_0^2 + 2a(x - x_0)$ | czas | $a = \text{const}$ |
| $x - x_0 = \tfrac12(v_0 + v)t$ | przyspieszenie | $a = \text{const}$ |
| $h_{\max} = \dfrac{v_0^2}{2g}$, $t_{\text{wzn}} = \dfrac{v_0}{g}$ | rzut pionowy w górę | bez oporu powietrza |
| $t = \sqrt{2h/g}$, $v = \sqrt{2gh}$ | spadek swobodny z wysokości $h$ | start z $v_0 = 0$, bez oporu |

## [02.03 — Ruch o zmiennym przyspieszeniu — całkowanie a(t)](03-zmienne-przyspieszenie.md)

| Dane | Metoda | Wynik |
|---|---|---|
| $a(t)$ | całkuj po czasie | $v(t) = v_0 + \int a\,dt$, $\ x(t) = x_0 + \int v\,dt$ |
| $a(v)$ | rozdziel zmienne | $t = \int dv/a(v)$, $\ \Delta x = \int v\,dv/a(v)$ |
| $a(x)$ | $a = v\,dv/dx$ | $v^2 = v_0^2 + 2\int a\,dx$ |
| $a = -kv$ | — | $v = v_0e^{-kt}$, $\ x = \dfrac{v_0}{k}(1 - e^{-kt})$, droga do zatrzymania $v_0/k$ |
| $a = -kv^2$ | — | $v = \dfrac{v_0}{1 + kv_0t}$, $\ v(x) = v_0e^{-kx}$ |

## [02.04 — Wektory położenia, prędkości i przyspieszenia w 2D i 3D](04-ruch-w-2d-i-3d.md)

| Wzór | Znaczenie | Uwagi |
|---|---|---|
| $\Delta\vec{r} = \vec{r}_2 - \vec{r}_1$ | przemieszczenie | długość $\lvert\Delta\vec{r}\rvert \le$ droga |
| $\vec{v} = d\vec{r}/dt$, $\ \vec{a} = d\vec{v}/dt$ | prędkość, przyspieszenie | różniczkujemy każdą składową |
| $v = \sqrt{v_x^2 + v_y^2 + v_z^2}$ | szybkość | — |
| $a_t = \dfrac{\vec{v}\cdot\vec{a}}{v}$ | przyspieszenie styczne | rzut $\vec{a}$ na kierunek $\vec{v}$ |
| $a_n = \sqrt{a^2 - a_t^2} = \dfrac{v^2}{R}$ | przyspieszenie normalne | $R$ — promień krzywizny toru |
| $\vec{r}(t) = \vec{r}_0 + \vec{v}_0t + \tfrac12\vec{a}t^2$ | ruch ze stałym $\vec{a}$ | wektorowa wersja wzorów z 02.02 |

## [02.05 — Rzut poziomy i ukośny](05-rzuty.md)

| Wzór | Znaczenie | Kiedy obowiązuje |
|---|---|---|
| $t = \sqrt{2h/g}$, $\ z = v_0\sqrt{2h/g}$ | rzut poziomy z wysokości $h$ | bez oporu |
| $t_c = 2v_0\sin\alpha/g$ | czas lotu | start i lądowanie na tej samej wysokości |
| $h_{\max} = v_0^2\sin^2\alpha/(2g)$ | wysokość maksymalna | względem punktu startu |
| $z = v_0^2\sin2\alpha/g$ | zasięg | start i lądowanie na tej samej wysokości |
| $y = x\tan\alpha - \dfrac{gx^2}{2v_0^2\cos^2\alpha}$ | równanie toru | start z $(0,\ 0)$ |
| $v^2 = v_0^2 - 2g(y - y_0)$ | szybkość na wysokości $y$ | z zasady zachowania energii lub z ruchu w pionie |

## [02.06 — Ruch po okręgu: jednostajny i niejednostajny](06-ruch-po-okregu.md)

| Wzór | Znaczenie | Kiedy obowiązuje |
|---|---|---|
| $\omega = 2\pi/T = 2\pi f$ | prędkość kątowa | ruch jednostajny po okręgu |
| $v = \omega R = 2\pi R/T$ | prędkość liniowa | $\omega$ w rad/s |
| $a_d = v^2/R = \omega^2R$ | przyspieszenie dośrodkowe | zawsze (także w ruchu niejednostajnym) |
| $a_t = dv/dt = \varepsilon R$ | przyspieszenie styczne | ruch niejednostajny |
| $a = \sqrt{a_t^2 + a_d^2}$ | przyspieszenie całkowite | składowe prostopadłe |
| $1\ \mathrm{obr/min} = \dfrac{2\pi}{60}\ \mathrm{rad/s}$ | przelicznik | — |

## [02.07 — Ruch względny i transformacja Galileusza](07-ruch-wzgledny.md)

| Wzór | Znaczenie | Kiedy obowiązuje |
|---|---|---|
| $\vec{r} = \vec{r}\,' + \vec{V}t$, $\ t = t'$ | transformacja Galileusza | $\vec{V} = \text{const}$, $V \ll c$ |
| $\vec{v} = \vec{v}\,' + \vec{V}$ | składanie prędkości | j.w. |
| $\vec{v}_{A/B} = \vec{v}_A - \vec{v}_B$ | prędkość względna | — |
| $\vec{a} = \vec{a}\,'$ | przyspieszenie niezmiennicze | układy inercjalne |
