# 23 — ściąga: Fizyka ciała stałego

Wszystkie tabele **Wzory i założenia** z tematów modułu na jednej stronie — do powtórki i do sprawdzenia, czy pamiętasz, **kiedy** wolno użyć wzoru. Wyprowadzenia, przykłady i zadania są w tematach.

[← spis modułu](README.md)

## [23.01 — Wiązania chemiczne i widma cząsteczkowe](01-wiazania-i-czasteczki.md)

| Wzór | Znaczenie | Kiedy obowiązuje |
|---|---|---|
| $U = -ke^2/r + U_{\text{odp}}$ | energia pary jonów | — |
| $\mu = m_1m_2/(m_1 + m_2)$, $I = \mu r^2$ | masa zredukowana, moment bezwładności | cząsteczka dwuatomowa |
| $E_l = \dfrac{\hbar^2}{2I}l(l + 1)$ | poziomy rotacyjne | sztywny rotator |
| $\Delta E_{l\to l+1} = \dfrac{\hbar^2}{I}(l + 1)$ | linie rotacyjne | $\Delta l = \pm1$ |
| $E_n = (n + \tfrac12)\hbar\omega$, $\omega = \sqrt{k/\mu}$ | poziomy oscylacyjne | oscylator harmoniczny |

## [23.02 — Struktura krystaliczna ciał stałych](02-krysztaly.md)

| Wzór | Znaczenie | Kiedy obowiązuje |
|---|---|---|
| $\rho = nM/(N_Aa^3)$ | gęstość z sieci | sieć regularna |
| $n$ = 1 (sc), 2 (bcc), 4 (fcc), 8 (diament) | atomy na komórkę | — |
| odległość sąsiadów: $a$ (sc), $a\sqrt3/2$ (bcc), $a/\sqrt2$ (fcc) | — | — |
| $U = -\alpha ke^2(1 - 1/n)/r_0$ | energia sieci jonowej | na parę jonów |
| $2d\sin\theta = m\lambda$ | dyfrakcja Bragga | pomiar $a$ (18.07) |

## [23.03 — Model elektronów swobodnych w metalach](03-elektrony-swobodne.md)

| Wzór | Znaczenie | Kiedy obowiązuje |
|---|---|---|
| $E_F = \dfrac{\hbar^2}{2m}(3\pi^2n)^{2/3}$ | energia Fermiego | gaz elektronów swobodnych |
| $v_F = \sqrt{2E_F/m}$, $T_F = E_F/k$ | prędkość i temperatura Fermiego | — |
| $g(E) \propto\sqrt E$ | gęstość stanów | 3D, elektrony swobodne |
| $f(E) = 1/(e^{(E - E_F)/kT} + 1)$ | rozkład Fermiego–Diraca | fermiony w równowadze |
| $\bar E = \tfrac35E_F$ | średnia energia elektronu | $T = 0$ |

## [23.04 — Teoria pasmowa ciał stałych](04-teoria-pasmowa.md)

| Wzór | Znaczenie | Kiedy obowiązuje |
|---|---|---|
| $N$ atomów → $N$ poziomów w paśmie | powstawanie pasm | — |
| $n_i \propto T^{3/2}e^{-E_g/(2kT)}$ | koncentracja nośników samoistnych | półprzewodnik niedomieszkowany |
| $\lambda_{\text{gr}} = hc/E_g$ | krawędź absorpcji | przejście przez przerwę |
| $\sigma = ne\mu_e + pe\mu_h$ | przewodność | $\mu$ — ruchliwości nośników |

## [23.05 — Półprzewodniki, domieszkowanie i złącze p-n](05-polprzewodniki.md)

| Wzór | Znaczenie | Kiedy obowiązuje |
|---|---|---|
| $np = n_i^2$ | prawo działania mas | równowaga termiczna |
| $n \approx N_D$ (typ n), $p \approx N_A$ (typ p) | nośniki większościowe | pełna jonizacja, $N \gg n_i$ |
| $\sigma = e(n\mu_e + p\mu_h)$ | przewodność | $\mu$ — ruchliwości |
| $I = I_0(e^{eU/kT} - 1)$ | charakterystyka diody | dioda idealna |
| $hf \approx E_g$, $\lambda \approx hc/E_g$ | foton z LED | przerwa prosta |
| $U_H = IB/(net)$ | napięcie Halla | jeden typ nośników |

## [23.06 — Nadprzewodnictwo](06-nadprzewodnictwo.md)

| Wzór | Znaczenie | Kiedy obowiązuje |
|---|---|---|
| $R = 0$ dla $T < T_c$ | brak oporu | prąd i pole poniżej krytycznych |
| $B_c(T) \approx B_c(0)[1 - (T/T_c)^2]$ | pole krytyczne | przybliżenie empiryczne |
| $\Delta \approx 1{,}76kT_c$ | przerwa nadprzewodząca w 0 K | teoria BCS, słabe sprzężenie |
| $\Phi = n\Phi_0$, $\Phi_0 = h/(2e)$ | kwantowanie strumienia | pierścień nadprzewodzący |
| $f = 2eU/h$ | efekt Josephsona (zmiennoprądowy) | złącze Josephsona |
| $T_c \propto M^{-1/2}$ | efekt izotopowy | nadprzewodniki konwencjonalne |
