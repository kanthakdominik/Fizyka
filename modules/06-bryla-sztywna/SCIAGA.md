# 06 — ściąga: Bryła sztywna, statyka i sprężystość

Wszystkie tabele **Wzory i założenia** z tematów modułu na jednej stronie — do powtórki i do sprawdzenia, czy pamiętasz, **kiedy** wolno użyć wzoru. Wyprowadzenia, przykłady i zadania są w tematach.

[← spis modułu](README.md)

## [06.01 — Kinematyka ruchu obrotowego](01-kinematyka-obrotow.md)

| Wzór | Znaczenie | Kiedy obowiązuje |
|---|---|---|
| $\omega = d\theta/dt$, $\ \varepsilon = d\omega/dt$ | definicje | $\theta$ w radianach |
| $\omega = \omega_0 + \varepsilon t$ | prędkość kątowa | $\varepsilon = \text{const}$ |
| $\theta = \omega_0t + \tfrac12\varepsilon t^2$ | kąt obrotu | $\varepsilon = \text{const}$ |
| $\omega^2 = \omega_0^2 + 2\varepsilon\theta$ | bez czasu | $\varepsilon = \text{const}$ |
| $v = \omega r$, $\ a_t = \varepsilon r$, $\ a_n = \omega^2r$ | wielkości liniowe punktu | bryła sztywna, oś stała |

## [06.02 — Moment bezwładności i twierdzenie Steinera](02-moment-bezwladnosci.md)

| Wzór | Znaczenie | Kiedy obowiązuje |
|---|---|---|
| $I = \sum m_ir_i^2 = \int r_\perp^2\,dm$ | moment bezwładności | $r_\perp$ — odległość od osi |
| $E_k = \tfrac12I\omega^2$ | energia ruchu obrotowego | obrót wokół stałej osi |
| $I = I_{\mathrm{SM}} + Md^2$ | twierdzenie Steinera | osie równoległe |
| $I_z = I_x + I_y$ | twierdzenie o osiach prostopadłych | tylko płaskie płytki |
| $I = Mk^2$ | promień bezwładności $k$ | definicja |

## [06.03 — Moment siły i dynamika ruchu obrotowego](03-moment-sily.md)

| Wzór | Znaczenie | Kiedy obowiązuje |
|---|---|---|
| $\tau = rF\sin\theta = Fd$ | moment siły | $d$ — ramię siły |
| $\sum\tau = I\varepsilon$ | II zasada dla obrotu | stała oś, $I$ względem tej osi |
| $W = \tau\theta$, $\ P = \tau\omega$ | praca i moc | stały moment |
| $a = \dfrac{(m_1 - m_2)g}{m_1 + m_2 + I/R^2}$ | maszyna Atwooda z bloczkiem | nić się nie ślizga |
| $a = \dfrac{mg}{m + I/R^2}$ | ciężarek na nici nawiniętej na walec | oś walca nieruchoma |

## [06.04 — Toczenie bez poślizgu](04-toczenie.md)

| Wzór | Znaczenie | Kiedy obowiązuje |
|---|---|---|
| $v_{\mathrm{SM}} = \omega R$ | warunek toczenia | brak poślizgu |
| $E_k = \tfrac12Mv^2(1 + \beta)$ | energia toczenia | $\beta = I_{\mathrm{SM}}/(MR^2)$ |
| $a = g\sin\alpha/(1 + \beta)$ | przyspieszenie na równi | toczenie bez poślizgu |
| $T = \dfrac{\beta}{1 + \beta}Mg\sin\alpha$ | potrzebne tarcie statyczne | j.w. |
| $\mu_s \ge \dfrac{\beta}{1 + \beta}\tan\alpha$ | warunek toczenia bez poślizgu | j.w. |

## [06.05 — Moment pędu i zasada jego zachowania](05-moment-pedu.md)

| Wzór | Znaczenie | Kiedy obowiązuje |
|---|---|---|
| $\vec{L} = \vec{r}\times m\vec{v}$, $\ L = mvd$ | moment pędu punktu | względem wybranego punktu |
| $L = I\omega$ | moment pędu bryły | obrót wokół osi symetrii |
| $\sum\vec{\tau} = d\vec{L}/dt$ | zasada dynamiki | momenty względem tego samego punktu |
| $I_1\omega_1 = I_2\omega_2$ | zachowanie momentu pędu | $\sum\tau_{\text{zewn}} = 0$ |
| $E_k = \dfrac{L^2}{2I}$ | energia przy danym $L$ | — |

## [06.06 — Precesja żyroskopu](06-precesja.md)

| Wzór | Znaczenie | Kiedy obowiązuje |
|---|---|---|
| $d\vec{L} = \vec{\tau}\,dt$ | zmiana momentu pędu | — |
| $\Omega = \dfrac{\tau}{L} = \dfrac{Mgd}{I\omega}$ | prędkość kątowa precesji | $\omega \gg \Omega$, oś pozioma |
| $\Omega = \dfrac{Mgd}{I\omega}$ (niezależnie od kąta) | bąk nachylony pod kątem do pionu | ten sam wynik — kąt się skraca |
| $T_p = 2\pi/\Omega$ | okres precesji | — |

## [06.07 — Równowaga statyczna, naprężenia i prawo Hooke'a](07-rownowaga-i-sprezystosc.md)

| Wzór | Znaczenie | Kiedy obowiązuje |
|---|---|---|
| $\sum\vec{F} = 0$, $\ \sum\vec{\tau} = 0$ | równowaga bryły | momenty względem dowolnego punktu |
| $\sigma = F/S$, $\ \varepsilon = \Delta L/L_0$ | naprężenie, odkształcenie | rozciąganie lub ściskanie |
| $\sigma = E\varepsilon \Rightarrow \Delta L = \dfrac{FL_0}{ES}$ | prawo Hooke'a | poniżej granicy sprężystości |
| $k = \dfrac{ES}{L_0}$ | „współczynnik sprężystości” pręta | j.w. |
| $W = \tfrac12F\Delta L$ | energia sprężystości pręta | j.w. |
