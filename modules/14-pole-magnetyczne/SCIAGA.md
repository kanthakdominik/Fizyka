# 14 — ściąga: Pole magnetyczne

Wszystkie tabele **Wzory i założenia** z tematów modułu na jednej stronie — do powtórki i do sprawdzenia, czy pamiętasz, **kiedy** wolno użyć wzoru. Wyprowadzenia, przykłady i zadania są w tematach.

[← spis modułu](README.md)

## [14.01 — Pole magnetyczne, siła Lorentza i ruch ładunku](01-sila-lorentza.md)

| Wzór | Znaczenie | Kiedy obowiązuje |
|---|---|---|
| $\vec F = q\vec v\times\vec B$, $F = \lvert q\rvert vB\sin\alpha$ | siła Lorentza (magnetyczna) | — |
| $\vec F = q(\vec E + \vec v\times\vec B)$ | pełna siła Lorentza | — |
| $r = mv/(\lvert q\rvert B)$ | promień okręgu | $\vec v \perp \vec B$, pole jednorodne |
| $T = 2\pi m/(\lvert q\rvert B)$ | okres obiegu | $v \ll c$ |
| $v = E/B$ | selektor prędkości | $\vec E \perp \vec B \perp \vec v$ |

## [14.02 — Siła elektrodynamiczna i moment sił na ramkę z prądem](02-sila-elektrodynamiczna.md)

| Wzór | Znaczenie | Kiedy obowiązuje |
|---|---|---|
| $\vec F = I\vec L\times\vec B$, $F = BIL\sin\alpha$ | siła na prosty przewodnik | pole jednorodne na długości $L$ |
| $d\vec F = I\,d\vec l\times\vec B$ | siła na element | dowolny kształt i pole |
| $\vec\mu = NI\vec A$ | moment magnetyczny ramki | ramka płaska, $N$ zwojów |
| $\vec\tau = \vec\mu\times\vec B$, $\tau = NIAB\sin\theta$ | moment siły na ramkę | pole jednorodne |
| $U = -\vec\mu\cdot\vec B$ | energia ramki w polu | — |

## [14.03 — Efekt Halla, spektrometr masowy, cyklotron](03-hall-cyklotron-spektrometr.md)

| Wzór | Znaczenie | Kiedy obowiązuje |
|---|---|---|
| $U_H = IB/(nqt)$ | napięcie Halla | jeden rodzaj nośników |
| $r = mv/(qB)$ | promień toru jonu | $\vec v \perp \vec B$ |
| $m = qBr/v$ | masa ze spektrometru | znane $v$ (selektor) |
| $f = qB/(2\pi m)$ | częstotliwość cyklotronu | $v \ll c$ |
| $E_{k,\max} = q^2B^2R^2/(2m)$ | energia końcowa | $v \ll c$ |

## [14.04 — Prawo Biota–Savarta](04-prawo-biota-savarta.md)

| Wzór | Znaczenie | Kiedy obowiązuje |
|---|---|---|
| $d\vec B = \dfrac{\mu_0}{4\pi}\dfrac{I\,d\vec l\times\hat r}{r^2}$ | prawo Biota–Savarta | prąd stały |
| $B = \mu_0I/(2\pi d)$ | nieskończony przewód prostoliniowy | $d \ll$ długość |
| $B = \mu_0I/(2R)$ | środek pętli kołowej | — |
| $B = \mu_0IR^2/[2(z^2 + R^2)^{3/2}]$ | oś pętli | — |
| $B = (4/5)^{3/2}\mu_0NI/R$ | cewki Helmholtza (środek) | odległość cewek $= R$ |

## [14.05 — Oddziaływanie przewodników z prądem](05-oddzialywanie-przewodnikow.md)

| Wzór | Znaczenie | Kiedy obowiązuje |
|---|---|---|
| $F/L = \mu_0I_1I_2/(2\pi d)$ | siła między przewodami równoległymi | długie, cienkie, $d \ll L$ |
| zgodne prądy — przyciąganie | kierunek siły | — |
| $\mu_0/(2\pi) = 2\cdot10^{-7}\ \mathrm{T\cdot m/A}$ | wygodna stała | — |

## [14.06 — Prawo Ampère'a, solenoid i toroid](06-prawo-ampera.md)

| Wzór | Znaczenie | Kiedy obowiązuje |
|---|---|---|
| $\oint\vec B\cdot d\vec l = \mu_0I_{\text{obj}}$ | prawo Ampère'a | prądy stałe (w ogólnym przypadku + prąd przesunięcia, 16) |
| $B = \mu_0nI$ | solenoid | długość $\gg$ średnica, z dala od końców |
| $B = \mu_0NI/(2\pi r)$ | toroid | wewnątrz uzwojenia |
| $B = \mu_0Ir/(2\pi R^2)$ | wnętrze przewodu | prąd jednorodny |

## [14.07 — Magnetyzm materii: dia-, para- i ferromagnetyki](07-magnetyzm-materii.md)

| Wzór | Znaczenie | Kiedy obowiązuje |
|---|---|---|
| $\mu_B = e\hbar/(2m_e) \approx 9{,}27\cdot10^{-24}\ \mathrm{A\cdot m^2}$ | magneton Bohra | — |
| $\vec B = \mu_0(\vec H + \vec M)$ | pole w materiale | — |
| $\vec M = \chi\vec H$, $\mu_r = 1 + \chi$ | materiał liniowy | dia- i paramagnetyki |
| $B = \mu_r\mu_0nI$ | solenoid z rdzeniem | ferromagnetyk poniżej nasycenia |
| $\chi = C/T$ | prawo Curie | paramagnetyki, $\mu B \ll kT$ |
| $M_s = n\mu_{\text{at}}$ | namagnesowanie nasycenia | wszystkie momenty zgodne |
