# 12 — ściąga: Elektrostatyka

Wszystkie tabele **Wzory i założenia** z tematów modułu na jednej stronie — do powtórki i do sprawdzenia, czy pamiętasz, **kiedy** wolno użyć wzoru. Wyprowadzenia, przykłady i zadania są w tematach.

[← spis modułu](README.md)

## [12.01 — Ładunek elektryczny i prawo Coulomba](01-ladunek-i-prawo-coulomba.md)

| Wzór | Znaczenie | Kiedy obowiązuje |
|---|---|---|
| $q = Ne$ | kwantyzacja ładunku | $e = 1{,}602\cdot10^{-19}\ \mathrm C$ |
| $F = k\lvert q_1q_2\rvert/r^2$ | prawo Coulomba | ładunki punktowe (lub kule), spoczywające |
| $k = 1/(4\pi\varepsilon_0) \approx 9\cdot10^9\ \mathrm{N\,m^2/C^2}$ | stała elektryczna | próżnia (powietrze w przybliżeniu) |
| $\vec F = \sum_i\vec F_i$ | superpozycja | — |

## [12.02 — Natężenie pola, linie pola i dipol](02-pole-elektryczne.md)

| Wzór | Znaczenie | Kiedy obowiązuje |
|---|---|---|
| $\vec E = \vec F/q_0$, $\ \vec F = q\vec E$ | definicja natężenia pola | $q_0$ mały, nie zaburza źródeł |
| $E = k\lvert q\rvert/r^2$ | pole ładunku punktowego | — |
| $\vec E = \sum_i\vec E_i$ | superpozycja | — |
| $\vec p = q\vec d$ | moment dipolowy | od $-q$ do $+q$ |
| $E_{\text{oś}} \approx 2kp/r^3$ | pole na osi dipola | $r \gg d$ |
| $\vec\tau = \vec p\times\vec E$, $\ U = -\vec p\cdot\vec E$ | dipol w polu | pole jednorodne |

## [12.03 — Pole rozkładów ciągłych ładunku](03-pole-rozkladow-ciaglych.md)

| Wzór | Znaczenie | Kiedy obowiązuje |
|---|---|---|
| $d\vec E = k\,dq\,\hat r/r^2$ | przyczynek elementu | — |
| $dq = \lambda\,dl = \sigma\,dA = \rho\,dV$ | element ładunku | — |
| $E = \lambda/(2\pi\varepsilon_0r)$ | nieskończona nić | $r \ll$ długość nici |
| $E = kQz/(z^2 + R^2)^{3/2}$ | pierścień, na osi | — |
| $E = \sigma/(2\varepsilon_0)$ | nieskończona płaszczyzna | $z \ll$ rozmiar płaszczyzny |

## [12.04 — Strumień pola i prawo Gaussa](04-prawo-gaussa.md)

| Wzór | Znaczenie | Kiedy obowiązuje |
|---|---|---|
| $\Phi_E = \int\vec E\cdot d\vec A$ | strumień pola | — |
| $\oint\vec E\cdot d\vec A = Q_{\text{wewn}}/\varepsilon_0$ | prawo Gaussa | zawsze; do liczenia $E$ — przy symetrii |
| $E = kQ/r^2$ (na zewnątrz), $kQr/R^3$ (wewnątrz) | kula jednorodna | symetria kulista |
| $E = \sigma/\varepsilon_0$ | tuż przy powierzchni przewodnika | równowaga elektrostatyczna |
| $E = 0$ | wnętrze przewodnika | j.w. |

## [12.05 — Potencjał, energia potencjalna i związek E z V](05-potencjal.md)

| Wzór | Znaczenie | Kiedy obowiązuje |
|---|---|---|
| $U = kq_1q_2/r$ | energia potencjalna pary ładunków | $U(\infty) = 0$ |
| $V = kq/r$, $\ V = \sum kq_i/r_i$ | potencjał ładunku punktowego, superpozycja | — |
| $W_{A\to B} = q(V_A - V_B)$ | praca pola | — |
| $qU = \Delta E_k$ | przyspieszanie ładunku | bez innych sił |
| $U = Ed$ | napięcie w polu jednorodnym | — |
| $\vec E = -\nabla V$, $\ \Delta V = -\int\vec E\cdot d\vec l$ | związek pola i potencjału | — |

## [12.06 — Kondensatory: pojemność, łączenie, energia](06-kondensatory.md)

| Wzór | Znaczenie | Kiedy obowiązuje |
|---|---|---|
| $C = Q/U$ | definicja pojemności | — |
| $C = \varepsilon_0A/d$ | kondensator płaski | $d \ll$ rozmiar okładek, próżnia |
| $C = C_1 + C_2$ | łączenie równoległe | — |
| $1/C = 1/C_1 + 1/C_2$ | łączenie szeregowe | — |
| $W = \tfrac12CU^2 = Q^2/(2C)$ | energia kondensatora | — |
| $w = \tfrac12\varepsilon_0E^2$ | gęstość energii pola | próżnia |

## [12.07 — Dielektryki w polu elektrycznym](07-dielektryki.md)

| Wzór | Znaczenie | Kiedy obowiązuje |
|---|---|---|
| $C = \varepsilon_rC_0$ | kondensator wypełniony dielektrykiem | dielektryk wypełnia całą przestrzeń |
| $E = E_0/\varepsilon_r$ | osłabienie pola | stały ładunek swobodny |
| $\sigma_b = \sigma(1 - 1/\varepsilon_r)$ | ładunek związany | dielektryk liniowy |
| $w = \tfrac12\varepsilon_r\varepsilon_0E^2$ | gęstość energii | — |
| $\oint\vec D\cdot d\vec A = Q_{\text{swob}}$, $\ \vec D = \varepsilon_r\varepsilon_0\vec E$ | prawo Gaussa w dielektryku | dielektryk liniowy, izotropowy |
