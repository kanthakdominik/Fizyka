# 15 — ściąga: Indukcja elektromagnetyczna i prąd przemienny

Wszystkie tabele **Wzory i założenia** z tematów modułu na jednej stronie — do powtórki i do sprawdzenia, czy pamiętasz, **kiedy** wolno użyć wzoru. Wyprowadzenia, przykłady i zadania są w tematach.

[← spis modułu](README.md)

## [15.01 — Prawo Faradaya i reguła Lenza](01-prawo-faradaya-i-lenza.md)

| Wzór | Znaczenie | Kiedy obowiązuje |
|---|---|---|
| $\Phi_B = BA\cos\theta$ | strumień magnetyczny | pole jednorodne, płaska pętla |
| $\varepsilon = -N\,d\Phi_B/dt$ | prawo Faradaya | zawsze |
| $\lvert\varepsilon\rvert = N\Delta\Phi/\Delta t$ | średnia SEM | zmiana w czasie $\Delta t$ |
| $q = N\Delta\Phi/R$ | ładunek indukowany | obwód zamknięty o oporze $R$ |

## [15.02 — SEM ruchu i indukowane pole elektryczne](02-sem-ruchu-i-pole-indukowane.md)

| Wzór | Znaczenie | Kiedy obowiązuje |
|---|---|---|
| $\varepsilon = BLv$ | SEM ruchu | $\vec L$, $\vec v$, $\vec B$ wzajemnie prostopadłe |
| $F = B^2L^2v/R$ | siła hamująca pręt | obwód o oporze $R$ |
| $\oint\vec E\cdot d\vec l = -d\Phi_B/dt$ | prawo Faradaya (postać całkowa) | zawsze |
| $E = \dfrac r2\dfrac{dB}{dt}$ | pole indukowane w solenoidzie | $r < R$, symetria osiowa |

## [15.03 — Prądy wirowe, prądnice i SEM wsteczna](03-pradnice-i-prady-wirowe.md)

| Wzór | Znaczenie | Kiedy obowiązuje |
|---|---|---|
| $\varepsilon = NBA\omega\sin\omega t$ | SEM prądnicy | stała prędkość, pole jednorodne |
| $\varepsilon_0 = NBA\omega$ | amplituda SEM | — |
| $I = (U - \varepsilon_w)/R$ | prąd silnika | silnik prądu stałego |
| $P_{\text{wir}} \propto B^2f^2d^2$ | straty na prądy wirowe | $d$ — grubość blachy |

## [15.04 — Indukcyjność własna i wzajemna, energia pola magnetycznego](04-indukcyjnosc.md)

| Wzór | Znaczenie | Kiedy obowiązuje |
|---|---|---|
| $\varepsilon_2 = -M\,dI_1/dt$ | indukcja wzajemna | — |
| $\varepsilon_L = -L\,dI/dt$ | samoindukcja | — |
| $L = N\Phi/I$ | definicja indukcyjności | — |
| $L = \mu_0N^2A/l$ | solenoid | $l \gg$ średnica, bez rdzenia |
| $W = \tfrac12LI^2$ | energia cewki | — |
| $w = B^2/(2\mu_0)$ | gęstość energii pola | próżnia |

## [15.05 — Obwody RL, LC i RLC — drgania elektromagnetyczne](05-obwody-rl-lc-rlc.md)

| Wzór | Znaczenie | Kiedy obowiązuje |
|---|---|---|
| $\tau = L/R$ | stała czasowa RL | — |
| $I = (\varepsilon/R)(1 - e^{-t/\tau})$ | narastanie prądu | włączenie źródła |
| $\omega_0 = 1/\sqrt{LC}$, $f_0 = 1/(2\pi\sqrt{LC})$ | częstość własna LC | bez strat |
| $\beta = R/(2L)$, $\omega_d = \sqrt{\omega_0^2 - \beta^2}$ | RLC | słabe tłumienie |
| $R_{\text{kr}} = 2\sqrt{L/C}$ | tłumienie krytyczne | — |
| $Q = \omega_0L/R$ | dobroć | — |

## [15.06 — Prąd przemienny: wartości skuteczne, impedancja, rezonans, moc](06-prad-przemienny.md)

| Wzór | Znaczenie | Kiedy obowiązuje |
|---|---|---|
| $U_{\text{sk}} = U_0/\sqrt2$ | wartość skuteczna | przebieg sinusoidalny |
| $X_L = \omega L$, $X_C = 1/(\omega C)$ | reaktancje | — |
| $Z = \sqrt{R^2 + (X_L - X_C)^2}$ | impedancja RLC szeregowego | — |
| $\tan\varphi = (X_L - X_C)/R$ | przesunięcie fazy | — |
| $\omega_0 = 1/\sqrt{LC}$ | rezonans | — |
| $P = U_{\text{sk}}I_{\text{sk}}\cos\varphi$ | moc czynna | — |

## [15.07 — Transformator i przesył energii](07-transformator.md)

| Wzór | Znaczenie | Kiedy obowiązuje |
|---|---|---|
| $U_2/U_1 = N_2/N_1$ | przekładnia napięciowa | brak rozproszenia strumienia |
| $I_2/I_1 = N_1/N_2$ | przekładnia prądowa | transformator idealny, obciążony |
| $U_1I_1 = U_2I_2$ | zachowanie mocy | bez strat |
| $\eta = P_2/P_1$ | sprawność | rzeczywisty transformator |
