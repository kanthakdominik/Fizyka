# 04 — ściąga: Praca, energia i moc

Wszystkie tabele **Wzory i założenia** z tematów modułu na jednej stronie — do powtórki i do sprawdzenia, czy pamiętasz, **kiedy** wolno użyć wzoru. Wyprowadzenia, przykłady i zadania są w tematach.

[← spis modułu](README.md)

## [04.01 — Praca siły stałej i zmiennej](01-praca.md)

| Wzór | Znaczenie | Kiedy obowiązuje |
|---|---|---|
| $W = Fs\cos\alpha$ | praca stałej siły | prostoliniowe przemieszczenie |
| $W = \int\vec{F}\cdot d\vec{r}$ | praca siły zmiennej | dowolny tor |
| $W = \int_{x_1}^{x_2}F\,dx$ | praca w 1D | pole pod $F(x)$ |
| $W_g = mg(h_1 - h_2)$ | praca siły ciężkości | $g = \text{const}$; nie zależy od drogi |
| $W_s = \tfrac12k(x_1^2 - x_2^2)$ | praca siły sprężystości | prawo Hooke'a; nie zależy od drogi |
| $W_T = -\mu_kNs$ | praca tarcia kinetycznego | stała siła nacisku; zawsze ujemna |

## [04.02 — Energia kinetyczna i twierdzenie o pracy i energii](02-energia-kinetyczna.md)

| Wzór | Znaczenie | Kiedy obowiązuje |
|---|---|---|
| $E_k = \tfrac12mv^2$ | energia kinetyczna | $v \ll c$ (dla prędkości bliskich $c$ — moduł 19) |
| $W_{\text{wyp}} = \Delta E_k$ | twierdzenie o pracy i energii | punkt materialny, układ inercjalny |
| $s = \dfrac{v^2}{2\mu g}$ | droga hamowania na poziomej drodze | stałe tarcie, brak innych sił poziomych |
| $\bar{F} = \dfrac{\Delta E_k}{s}$ | średnia siła na drodze $s$ | średnia względem drogi |

## [04.03 — Moc i sprawność](03-moc-i-sprawnosc.md)

| Wzór | Znaczenie | Kiedy obowiązuje |
|---|---|---|
| $\bar{P} = W/\Delta t$ | moc średnia | — |
| $P = dW/dt = \vec{F}\cdot\vec{v}$ | moc chwilowa | — |
| $W = \int P\,dt$ | praca przy zmiennej mocy | — |
| $\eta = P_{\text{uż}}/P_{\text{pob}}$ | sprawność | — |
| $P = mgv$ | moc podnoszenia ze stałą prędkością | pionowo, bez oporów |
| $1\ \mathrm{kWh} = 3{,}6\cdot10^6\ \mathrm{J}$ | przelicznik | — |

## [04.04 — Siły zachowawcze i energia potencjalna](04-energia-potencjalna.md)

| Wzór | Znaczenie | Kiedy obowiązuje |
|---|---|---|
| $\Delta U = -W_{\text{zach}}$ | definicja energii potencjalnej | tylko dla sił zachowawczych |
| $U = mgh$ | grawitacyjna przy Ziemi | $h \ll R_Z$, $g = \text{const}$ |
| $U = \tfrac12kx^2$ | sprężystości | prawo Hooke'a |
| $U(x) = -\int_{x_0}^{x}F(x')\,dx'$ | energia z siły | $U(x_0) = 0$ |
| $F = -dU/dx$ | siła z energii | 1D |
| $\oint\vec{F}\cdot d\vec{r} = 0$ | test zachowawczości | każda droga zamknięta |

## [04.05 — Zasada zachowania energii mechanicznej i całkowitej](05-zasada-zachowania-energii.md)

| Wzór | Znaczenie | Kiedy obowiązuje |
|---|---|---|
| $\tfrac12mv_1^2 + U_1 = \tfrac12mv_2^2 + U_2$ | zachowanie energii mechanicznej | tylko siły zachowawcze wykonują pracę |
| $\Delta E_{\text{mech}} = W_{\text{niezach}}$ | bilans z tarciem | ogólnie |
| $v = \sqrt{2g\Delta h}$ | prędkość po obniżeniu o $\Delta h$ | start z $v = 0$, bez tarcia; niezależnie od kształtu toru |
| $v_{\text{dół}} = \sqrt{2gL(1 - \cos\theta_0)}$ | wahadło | wychylenie $\theta_0$, puszczone bez prędkości |
| $h_{\min} = \tfrac52R$ | najmniejsza wysokość startu do pętli | bez tarcia, ciało ślizga się (nie toczy) |

## [04.06 — Wykresy energii potencjalnej i stabilność równowagi](06-wykresy-energii.md)

| Wzór | Znaczenie | Kiedy obowiązuje |
|---|---|---|
| $E_k = E - U(x) \ge 0$ | obszar dozwolony | tylko siły zachowawcze |
| $U(x_z) = E$ | punkt zwrotu | — |
| $U'(x_0) = 0$ | położenie równowagi | — |
| $U''(x_0) > 0$ / $< 0$ | równowaga trwała / nietrwała | — |
| $\omega = \sqrt{U''(x_0)/m}$ | częstość małych drgań | małe wychylenia od minimum |
| $U_{LJ} = 4\varepsilon\left[\left(\tfrac{\sigma}{r}\right)^{12} - \left(\tfrac{\sigma}{r}\right)^6\right]$ | potencjał Lennarda-Jonesa | oddziaływanie obojętnych atomów |
