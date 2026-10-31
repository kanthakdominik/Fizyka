# 20 — ściąga: Podstawy fizyki kwantowej

Wszystkie tabele **Wzory i założenia** z tematów modułu na jednej stronie — do powtórki i do sprawdzenia, czy pamiętasz, **kiedy** wolno użyć wzoru. Wyprowadzenia, przykłady i zadania są w tematach.

[← spis modułu](README.md)

## [20.01 — Promieniowanie ciała doskonale czarnego](01-cialo-doskonale-czarne.md)

| Wzór | Znaczenie | Kiedy obowiązuje |
|---|---|---|
| $E = hf = hc/\lambda$ | kwant energii (foton) | — |
| $B_\lambda = \dfrac{2hc^2}{\lambda^5}\dfrac{1}{e^{hc/\lambda kT} - 1}$ | prawo Plancka | ciało doskonale czarne |
| $\lambda_{\max}T = 2{,}898\cdot10^{-3}\ \mathrm{m\cdot K}$ | prawo Wiena | j.w. |
| $P/A = \sigma T^4$ | prawo Stefana–Boltzmanna | j.w. |
| $B_\lambda \approx 2ckT/\lambda^4$ | Rayleigh–Jeans | $hc/\lambda \ll kT$ |

## [20.02 — Efekt fotoelektryczny](02-efekt-fotoelektryczny.md)

| Wzór | Znaczenie | Kiedy obowiązuje |
|---|---|---|
| $E = hf = hc/\lambda$ | energia fotonu | $hc \approx 1240\ \mathrm{eV\cdot nm}$ |
| $hf = W + E_{k,\max}$ | równanie Einsteina | jeden foton — jeden elektron |
| $eU_h = E_{k,\max}$ | napięcie hamowania | — |
| $f_0 = W/h$, $\lambda_0 = hc/W$ | próg fotoefektu | — |
| $N = P\lambda/(hc)$ | liczba fotonów na sekundę | wiązka monochromatyczna |

## [20.03 — Efekt Comptona](03-efekt-comptona.md)

| Wzór | Znaczenie | Kiedy obowiązuje |
|---|---|---|
| $p = h/\lambda = E/c$ | pęd fotonu | — |
| $\Delta\lambda = \lambda_C(1 - \cos\theta)$ | wzór Comptona | elektron swobodny, spoczywający |
| $\lambda_C = h/(m_ec) = 2{,}43\ \mathrm{pm}$ | komptonowska długość fali | — |
| $E_{k,e} = hc/\lambda - hc/\lambda'$ | energia odrzutu elektronu | — |

## [20.04 — Fale materii de Broglie'a i dualizm korpuskularno-falowy](04-fale-materii.md)

| Wzór | Znaczenie | Kiedy obowiązuje |
|---|---|---|
| $\lambda = h/p$ | długość fali de Broglie'a | każda cząstka |
| $\lambda = h/\sqrt{2mE_k}$ | z energii kinetycznej | $E_k \ll mc^2$ |
| $\lambda = h/\sqrt{2meU}$ | cząstka przyspieszona napięciem | j.w. |
| $pc = \sqrt{E_k^2 + 2E_kmc^2}$ | pęd relatywistyczny | dowolne $E_k$ |

## [20.05 — Funkcja falowa i zasada nieoznaczoności](05-funkcja-falowa-i-nieoznaczonosc.md)

| Wzór | Znaczenie | Kiedy obowiązuje |
|---|---|---|
| $\lvert\psi\rvert^2$ | gęstość prawdopodobieństwa | — |
| $\int\lvert\psi\rvert^2dx = 1$ | normalizacja | — |
| $\langle x\rangle = \int x\lvert\psi\rvert^2dx$ | wartość oczekiwana położenia | — |
| $\Delta x\Delta p \ge \hbar/2$ | zasada nieoznaczoności | równość dla paczki gaussowskiej |
| $\Delta E\Delta t \gtrsim \hbar/2$ | nieoznaczoność energia–czas | $\Delta t$ — czas życia, czas pomiaru |

## [20.06 — Równanie Schrödingera: studnia potencjału i oscylator](06-rownanie-schrodingera.md)

| Wzór | Znaczenie | Kiedy obowiązuje |
|---|---|---|
| $-\frac{\hbar^2}{2m}\psi'' + U\psi = E\psi$ | równanie Schrödingera (1D) | stany stacjonarne |
| $E_n = n^2h^2/(8mL^2)$ | nieskończona studnia | $n = 1, 2, \dots$ |
| $\psi_n = \sqrt{2/L}\sin(n\pi x/L)$ | funkcje własne studni | $0 \le x \le L$ |
| $E_n = (n + \tfrac12)\hbar\omega$ | oscylator harmoniczny | $n = 0, 1, \dots$ |
| $hf = E_n - E_m$ | foton przy przejściu | — |

## [20.07 — Tunelowanie przez barierę potencjału](07-tunelowanie.md)

| Wzór | Znaczenie | Kiedy obowiązuje |
|---|---|---|
| $\kappa = \sqrt{2m(U - E)}/\hbar$ | stała zaniku w barierze | $E < U$ |
| $\psi \propto e^{-\kappa x}$ | zanik w barierze | — |
| $T \approx e^{-2\kappa L}$ | współczynnik przejścia | $\kappa L \gg 1$ |
| $T \approx 16\frac EU(1 - \frac EU)e^{-2\kappa L}$ | dokładniejszy | bariera prostokątna |
| $T \approx \exp\left(-\frac2\hbar\int\sqrt{2m(U(x) - E)}dx\right)$ | bariera dowolnego kształtu (WKB) | wolno zmienne $U$ |
