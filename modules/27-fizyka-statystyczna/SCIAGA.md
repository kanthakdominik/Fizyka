# 27 — ściąga: Fizyka statystyczna

Wszystkie tabele **Wzory i założenia** z tematów modułu na jednej stronie — do powtórki i do sprawdzenia, czy pamiętasz, **kiedy** wolno użyć wzoru. Wyprowadzenia, przykłady i zadania są w tematach.

[← spis modułu](README.md)

## [27.01 — Mikrostany, makrostany i entropia Boltzmanna](01-mikrostany-i-entropia.md)

| Wzór | Znaczenie | Kiedy obowiązuje |
|---|---|---|
| $S = k\ln\Omega$ | entropia Boltzmanna | układ izolowany, mikrostany jednakowo prawdopodobne |
| $\Omega = \binom Nn = \dfrac{N!}{n!(N - n)!}$ | układy dwustanowe (monety, spiny) | — |
| $\Omega = \binom{q + N - 1}{q}$ | kryształ Einsteina | $q$ kwantów na $N$ oscylatorach |
| $\Delta S = Nk\ln(V_2/V_1)$ | rozprężanie gazu doskonałego | stała energia |
| $1/T = \partial S/\partial U$ | definicja temperatury | stałe $V$ i $N$ |
| $\ln N! \approx N\ln N - N$ | wzór Stirlinga | $N \gg 1$ |

## [27.02 — Rozkład Boltzmanna i suma statystyczna](02-rozklad-boltzmanna.md)

| Wzór | Znaczenie | Kiedy obowiązuje |
|---|---|---|
| $P_i = e^{-E_i/kT}/Z$, $Z = \sum e^{-E_i/kT}$ | rozkład Boltzmanna | układ w równowadze z termostatem |
| $N_2/N_1 = (g_2/g_1)e^{-\Delta E/kT}$ | stosunek obsadzeń | dwa poziomy |
| $n(h) = n_0e^{-mgh/kT}$, $H = kT/(mg)$ | wzór barometryczny | atmosfera izotermiczna |
| $f(v_x) \propto e^{-mv_x^2/2kT}$ | rozkład składowej prędkości | gaz klasyczny |
| $\langle E\rangle = -\partial\ln Z/\partial\beta$ | średnia energia | $\beta = 1/kT$ |
| $\langle\sigma\rangle = \tanh(\mu B/kT)$ | polaryzacja spinów ½ | paramagnetyk idealny |
| $k = 1{,}380649\cdot10^{-23}\ \mathrm{J/K}$; $kT \approx 0{,}0259\ \mathrm{eV}$ w 300 K | — | — |

## [27.03 — Ekwipartycja energii i kwantowe zamrażanie stopni swobody](03-ekwipartycja-i-cieplo-wlasciwe.md)

| Wzór | Znaczenie | Kiedy obowiązuje |
|---|---|---|
| $\langle E\rangle = \tfrac12kT$ na stopień swobody | zasada ekwipartycji | kwadratowe stopnie swobody, $kT \gg \Delta E$ |
| $C_V = \tfrac s2R$, $C_p = C_V + R$ | ciepło molowe gazu doskonałego | — |
| $E_{śr} = \tfrac s2kT$ | średnia energia cząsteczki | karta wzorów CKE |
| $C_V = 3R$ | prawo Dulonga–Petita | ciała stałe, $T \gg \theta_E$ |
| $C_V = 3R\dfrac{x^2e^x}{(e^x - 1)^2}$, $x = \theta_E/T$ | model Einsteina | — |
| $\theta = \Delta E/k$ | temperatura charakterystyczna | — |

## [27.04 — Statystyki kwantowe: fermiony, bozony i promieniowanie cieplne](04-statystyki-kwantowe.md)

| Wzór | Znaczenie | Kiedy obowiązuje |
|---|---|---|
| $\bar n_{FD} = 1/(e^{(E - \mu)/kT} + 1)$ | rozkład Fermiego–Diraca | fermiony nierozróżnialne |
| $\bar n_{BE} = 1/(e^{(E - \mu)/kT} - 1)$ | rozkład Bosego–Einsteina | bozony; $\mu \le$ najniższa energia |
| $\bar n_{MB} = e^{-(E - \mu)/kT}$ | granica klasyczna | $E - \mu \gg kT$ |
| $\lambda_{th} = h/\sqrt{2\pi mkT}$ | termiczna długość fali | kryterium: $n\lambda_{th}^3 \sim 1$ |
| $u(f) = \dfrac{8\pi hf^3}{c^3}\dfrac{1}{e^{hf/kT} - 1}$ | prawo Plancka | gaz fotonów, $\mu = 0$ |
| $T_c = \dfrac{2\pi\hbar^2}{mk}\left(\dfrac{n}{2{,}612}\right)^{2/3}$ | temperatura kondensacji BE | gaz idealny bozonów |

## [27.05 — Model Isinga, przejścia fazowe i metoda Metropolisa](05-model-isinga.md)

| Wzór | Znaczenie | Kiedy obowiązuje |
|---|---|---|
| $E = -J\sum_{\langle ij\rangle}s_is_j - h\sum s_i$ | energia modelu Isinga | spiny $\pm1$, oddziaływanie najbliższych sąsiadów |
| $kT_c = 2J/\ln(1 + \sqrt2) \approx 2{,}269J$ | temperatura krytyczna (Onsager) | 2D, siatka kwadratowa, $h = 0$ |
| $m = [1 - \sinh^{-4}(2J/kT)]^{1/8}$ | namagnesowanie spontaniczne | 2D, $T < T_c$ |
| $m = \tanh\dfrac{zJm + h}{kT}$, $kT_c = zJ$ | przybliżenie pola średniego | $z$ — liczba sąsiadów |
| $P_{\text{akcept}} = \min(1, e^{-\Delta E/kT})$ | krok Metropolisa | równowaga, rozkład Boltzmanna |
| $C = \dfrac{\langle E^2\rangle - \langle E\rangle^2}{kT^2}$ | ciepło właściwe z fluktuacji | zespół kanoniczny |
