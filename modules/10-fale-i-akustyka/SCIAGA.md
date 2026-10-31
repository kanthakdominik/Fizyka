# 10 — ściąga: Fale mechaniczne i akustyka

Wszystkie tabele **Wzory i założenia** z tematów modułu na jednej stronie — do powtórki i do sprawdzenia, czy pamiętasz, **kiedy** wolno użyć wzoru. Wyprowadzenia, przykłady i zadania są w tematach.

[← spis modułu](README.md)

## [10.01 — Fala biegnąca i jej opis matematyczny](01-fala-biegnaca.md)

| Wzór | Znaczenie | Kiedy obowiązuje |
|---|---|---|
| $v = \lambda f = \omega/k$ | prędkość fali | fala harmoniczna |
| $k = 2\pi/\lambda$, $\ \omega = 2\pi f$ | liczba falowa, częstość | — |
| $y = A\sin(kx \mp \omega t + \varphi)$ | fala biegnąca w prawo / w lewo | fala harmoniczna |
| $v_y = \partial y/\partial t$, $\ v_{y,\max} = A\omega$ | prędkość elementu ośrodka | fala poprzeczna |
| $\dfrac{\partial^2y}{\partial t^2} = v^2\dfrac{\partial^2y}{\partial x^2}$ | równanie falowe | ośrodek liniowy, bez tłumienia (10.02) |

## [10.02 — Prędkość fali, energia i równanie falowe](02-predkosc-i-energia-fali.md)

| Wzór | Znaczenie | Kiedy obowiązuje |
|---|---|---|
| $v = \sqrt{F/\mu}$ | fala na strunie | małe wychylenia, struna jednorodna |
| $v = \sqrt{K/\rho}$, $\ v = \sqrt{\gamma RT/M}$ | dźwięk w płynach, w gazie doskonałym | procesy adiabatyczne |
| $v = \sqrt{E/\rho}$ | fala podłużna w cienkim pręcie | — |
| $\partial_t^2y = v^2\partial_x^2y$ | równanie falowe | ośrodek liniowy, bez strat |
| $\bar P = \tfrac12\mu\omega^2A^2v$ | moc fali na strunie | fala harmoniczna |

## [10.03 — Superpozycja, interferencja i fale stojące](03-interferencja-i-fale-stojace.md)

| Wzór | Znaczenie | Kiedy obowiązuje |
|---|---|---|
| $y = y_1 + y_2$ | zasada superpozycji | ośrodek liniowy |
| $\Delta r = m\lambda$ / $\Delta r = (m + \tfrac12)\lambda$ | wzmocnienie / wygaszenie | źródła spójne, w fazie |
| $y = 2A\sin kx\cos\omega t$ | fala stojąca | dwie jednakowe fale przeciwbieżne |
| odległość węzłów $= \lambda/2$ | — | fala stojąca |
| $f_n = nv/(2L)$ | mody struny | oba końce zamocowane |

## [10.04 — Zasada Huygensa: odbicie, załamanie i dyfrakcja fal](04-huygens-dyfrakcja-zalamanie.md)

| Wzór | Znaczenie | Kiedy obowiązuje |
|---|---|---|
| $\theta_{\text{odb}} = \theta_{\text{pad}}$ | prawo odbicia | gładka powierzchnia (nierówności $\ll\lambda$) |
| $\sin\theta_1/\sin\theta_2 = v_1/v_2$ | prawo załamania | — |
| $\sin\theta_{\text{gr}} = v_1/v_2$ | kąt graniczny | $v_2 > v_1$ |
| $t = 2d/v$ | czas powrotu echa | — |
| $v \approx \sqrt{gh}$ | fale na płytkiej wodzie | $h \ll \lambda$ |
| silna dyfrakcja, gdy $a \lesssim \lambda$ | ugięcie na szczelinie $a$ | — |

## [10.05 — Dźwięk: prędkość, natężenie, poziom w decybelach](05-dzwiek-i-natezenie.md)

| Wzór | Znaczenie | Kiedy obowiązuje |
|---|---|---|
| $\Delta p_m = \rho v\omega s_m$ | amplituda ciśnienia a amplituda wychylenia | fala harmoniczna |
| $I = \Delta p_m^2/(2\rho v)$ | natężenie fali dźwiękowej | j.w. |
| $I = P/(4\pi r^2)$ | źródło punktowe | brak odbić i pochłaniania |
| $L = 10\log(I/I_0)$ | poziom natężenia w dB | $I_0 = 10^{-12}\ \mathrm{W/m^2}$ |
| $L_2 - L_1 = 10\log(I_2/I_1) = 20\log(r_1/r_2)$ | różnica poziomów | źródło punktowe |

## [10.06 — Struny i piszczałki: mody własne, dudnienia](06-struny-rury-dudnienia.md)

| Wzór | Znaczenie | Kiedy obowiązuje |
|---|---|---|
| $f_n = nv/(2L)$, $n = 1, 2, 3, \dots$ | struna; rura otwarta z obu stron | — |
| $f_n = nv/(4L)$, $n = 1, 3, 5, \dots$ | rura zamknięta z jednej strony | — |
| $v = \sqrt{F/\mu}$ / $v \approx 343\ \mathrm{m/s}$ | prędkość fali na strunie / w powietrzu | powietrze w 20°C |
| $\Delta L \approx 0{,}6r$ | poprawka wylotowa | rura o promieniu $r$, koniec otwarty |
| $f_{\text{d}} = \lvert f_1 - f_2\rvert$ | dudnienia | $f_1 \approx f_2$ |

## [10.07 — Efekt Dopplera i fala uderzeniowa](07-efekt-dopplera.md)

| Wzór | Znaczenie | Kiedy obowiązuje |
|---|---|---|
| $f' = f\dfrac{v \pm v_o}{v \mp v_s}$ | efekt Dopplera dla dźwięku | ruch wzdłuż prostej; $v_s < v$; górne znaki — zbliżanie |
| $\lambda' = (v \mp v_s)/f$ | długość fali przed / za źródłem | — |
| $\Delta f \approx 2uf/c$ | radar, odbicie od ruchomego obiektu | $u \ll c$ |
| $\sin\theta = v/v_s$ | kąt stożka Macha | $v_s > v$ |
