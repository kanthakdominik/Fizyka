# 13 — ściąga: Prąd stały

Wszystkie tabele **Wzory i założenia** z tematów modułu na jednej stronie — do powtórki i do sprawdzenia, czy pamiętasz, **kiedy** wolno użyć wzoru. Wyprowadzenia, przykłady i zadania są w tematach.

[← spis modułu](README.md)

## [13.01 — Natężenie i gęstość prądu, model przewodnictwa](01-prad-i-model-przewodnictwa.md)

| Wzór | Znaczenie | Kiedy obowiązuje |
|---|---|---|
| $I = dq/dt$, $\ q = \int I\,dt$ | natężenie prądu, przepływający ładunek | — |
| $J = I/A$ | gęstość prądu | przepływ jednorodny |
| $I = nqv_dA$ | prąd a prędkość dryfu | — |
| $\vec J = \sigma\vec E$ | mikroskopowe prawo Ohma | przewodnik omowy |
| $\sigma = ne^2\tau/m$ | przewodność w modelu Drudego | metale, model klasyczny |

## [13.02 — Opór, opór właściwy i prawo Ohma](02-opor-i-prawo-ohma.md)

| Wzór | Znaczenie | Kiedy obowiązuje |
|---|---|---|
| $R = U/I$ | definicja oporu | — |
| $I = U/R$, $R$ = const | prawo Ohma | elementy omowe, stała temperatura |
| $R = \rho L/A$ | opór przewodnika | jednorodny, stały przekrój |
| $\rho = \rho_0[1 + \alpha\Delta T]$ | zależność od temperatury | metale, umiarkowane $\Delta T$ |
| $R = \int\rho\,dl/A(l)$ | przekrój zmienny | prąd wzdłuż osi |

## [13.03 — Praca i moc prądu](03-praca-i-moc-pradu.md)

| Wzór | Znaczenie | Kiedy obowiązuje |
|---|---|---|
| $P = UI$ | moc prądu | każdy odbiornik |
| $P = I^2R = U^2/R$ | moc cieplna | opornik |
| $W = Pt = UIt$ | energia | moc stała w czasie |
| $W = \int P\,dt$ | energia | moc zmienna |
| $1\ \mathrm{kWh} = 3{,}6\cdot10^6\ \mathrm J$ | jednostka rozliczeniowa | — |
| $P_{\text{strat}} = (P/U)^2R_l$ | straty przesyłu | — |

## [13.04 — SEM, opór wewnętrzny, łączenie oporników](04-sem-i-laczenie-opornikow.md)

| Wzór | Znaczenie | Kiedy obowiązuje |
|---|---|---|
| $U = \varepsilon - Ir$ | napięcie na zaciskach | źródło rozładowywane |
| $I = \varepsilon/(R + r)$ | prąd w obwodzie z jednym źródłem | — |
| $P_{\max} = \varepsilon^2/(4r)$ dla $R = r$ | dopasowanie mocy | — |
| $R = R_1 + R_2 + \dots$ | połączenie szeregowe | — |
| $1/R = 1/R_1 + 1/R_2 + \dots$ | połączenie równoległe | — |
| $U_1 = UR_1/(R_1 + R_2)$ | dzielnik napięcia | bez obciążenia wyjścia |

## [13.05 — Prawa Kirchhoffa i mierniki](05-prawa-kirchhoffa.md)

| Wzór | Znaczenie | Kiedy obowiązuje |
|---|---|---|
| $\sum I_{\text{wpł}} = \sum I_{\text{wypł}}$ | I prawo Kirchhoffa | każdy węzeł, stan ustalony |
| $\sum\varepsilon - \sum IR = 0$ | II prawo Kirchhoffa | każde oczko |
| $R_b = \dfrac{I_gR_g}{I - I_g}$ | bocznik amperomierza | zakres $I$, galwanometr $I_g$, $R_g$ |
| $R_s = U/I_g - R_g$ | posobnik woltomierza | zakres $U$ |
| $R_1/R_2 = R_3/R_4$ | równowaga mostka | brak prądu w przekątnej |

## [13.06 — Obwody RC — ładowanie i rozładowanie](06-obwody-rc.md)

| Wzór | Znaczenie | Kiedy obowiązuje |
|---|---|---|
| $\tau = RC$ | stała czasowa | — |
| $q = C\varepsilon(1 - e^{-t/\tau})$, $\ I = (\varepsilon/R)e^{-t/\tau}$ | ładowanie | $q(0) = 0$ |
| $q = Q_0e^{-t/\tau}$ | rozładowanie | — |
| $t_{1/2} = \tau\ln2$ | czas połowicznego rozładowania | — |
| $W_{\text{źr}} = C\varepsilon^2$, $W_C = W_R = \tfrac12C\varepsilon^2$ | bilans energii ładowania | pełne naładowanie |
