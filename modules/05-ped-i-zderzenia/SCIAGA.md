# 05 — ściąga: Pęd, środek masy i zderzenia

Wszystkie tabele **Wzory i założenia** z tematów modułu na jednej stronie — do powtórki i do sprawdzenia, czy pamiętasz, **kiedy** wolno użyć wzoru. Wyprowadzenia, przykłady i zadania są w tematach.

[← spis modułu](README.md)

## [05.01 — Pęd i popęd siły](01-ped-i-poped.md)

| Wzór | Znaczenie | Kiedy obowiązuje |
|---|---|---|
| $\vec{p} = m\vec{v}$ | pęd | $v \ll c$ |
| $\vec{F} = d\vec{p}/dt$ | II zasada dynamiki | układ inercjalny |
| $\vec{J} = \int\vec{F}\,dt = \Delta\vec{p}$ | popęd siły | — |
| $\bar{F} = \Delta p/\Delta t$ | średnia siła w czasie zderzenia | — |
| $E_k = p^2/(2m)$ | związek energii i pędu | $v \ll c$ |
| $F = \mu v$ | siła strumienia masy zatrzymywanej na przeszkodzie | $\mu$ — masa na sekundę, $v$ — prędkość strumienia |

## [05.02 — Zasada zachowania pędu](02-zasada-zachowania-pedu.md)

| Wzór | Znaczenie | Kiedy obowiązuje |
|---|---|---|
| $\sum m_i\vec{v}_i = \sum m_i\vec{v}_i\,'$ | zachowanie pędu | brak (lub pomijalne) siły zewnętrzne |
| $m_1v_1 = m_2v_2$ | odrzut z układu w spoczynku | wartości prędkości, zwroty przeciwne |
| $d\vec{P}/dt = \sum\vec{F}_{\text{zewn}}$ | II zasada dla układu | zawsze |
| $P_x = \text{const}$ | zachowanie składowej | $\sum F_{\text{zewn},x} = 0$ |

## [05.03 — Zderzenia sprężyste i niesprężyste w 1D i 2D](03-zderzenia.md)

| Wzór | Znaczenie | Kiedy obowiązuje |
|---|---|---|
| $\sum m\vec{v} = \sum m\vec{v}\,'$ | zachowanie pędu | każde zderzenie (krótkie, siły wewnętrzne dominują) |
| $\sum\tfrac12mv^2 = \sum\tfrac12mv'^2$ | zachowanie energii kinetycznej | tylko zderzenie sprężyste |
| $V = \dfrac{m_1v_1 + m_2v_2}{m_1 + m_2}$ | doskonale niesprężyste | ciała po zderzeniu razem |
| $v_1' = \dfrac{m_1 - m_2}{m_1 + m_2}v_1$, $\ v_2' = \dfrac{2m_1}{m_1 + m_2}v_1$ | sprężyste, ciało 2 spoczywa | czołowe (1D) |
| $v_1 - v_2 = -(v_1' - v_2')$ | sprężyste: prędkość względna zmienia znak | 1D |
| $v = \dfrac{m + M}{m}\sqrt{2gh}$ | wahadło balistyczne | pocisk $m$ grzęźnie w klocku $M$ |

## [05.04 — Środek masy układu i bryły](04-srodek-masy.md)

| Wzór | Znaczenie | Kiedy obowiązuje |
|---|---|---|
| $x_{\mathrm{SM}} = \sum m_ix_i/\sum m_i$ | środek masy punktów | — |
| $\vec{r}_{\mathrm{SM}} = \frac1M\int\vec{r}\,dm$ | środek masy ciała ciągłego | $dm = \lambda\,dl$, $\sigma\,dA$ lub $\rho\,dV$ |
| $M\vec{a}_{\mathrm{SM}} = \sum\vec{F}_{\text{zewn}}$ | ruch środka masy | — |
| $\vec{P} = M\vec{v}_{\mathrm{SM}}$ | pęd układu | — |
| $y_{\mathrm{SM}} = \dfrac{4R}{3\pi}$ | półkole (płytka) | od średnicy |
| $y_{\mathrm{SM}} = \dfrac{h}{4}$ | stożek pełny | od podstawy |

## [05.05 — Układy o zmiennej masie — rakieta](05-zmienna-masa-rakieta.md)

| Wzór | Znaczenie | Kiedy obowiązuje |
|---|---|---|
| $F_{\text{ciągu}} = u\lvert dm/dt\rvert$ | siła ciągu | $u$ — prędkość gazów względem rakiety |
| $\Delta v = u\ln(m_0/m_k)$ | wzór Ciołkowskiego | brak sił zewnętrznych |
| $v(t) = u\ln\dfrac{m_0}{m(t)} - gt$ | start pionowy | $g$ stałe, bez oporu powietrza |
| $F = v\,dm/dt$ | siła potrzebna do ładowania masy na taśmę | masa dołączana z prędkością zerową |
