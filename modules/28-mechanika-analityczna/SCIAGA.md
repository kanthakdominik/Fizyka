# 28 — ściąga: Mechanika analityczna (wstęp)

Wszystkie tabele **Wzory i założenia** z tematów modułu na jednej stronie — do powtórki i do sprawdzenia, czy pamiętasz, **kiedy** wolno użyć wzoru. Wyprowadzenia, przykłady i zadania są w tematach.

[← spis modułu](README.md)

## [28.01 — Rachunek wariacyjny i zasada najmniejszego działania](01-zasada-najmniejszego-dzialania.md)

| Wzór | Znaczenie | Kiedy obowiązuje |
|---|---|---|
| $J[y] = \int F(y, y', x)\,dx$ | funkcjonał | ustalone końce $y(x_1)$, $y(x_2)$ |
| $\dfrac{d}{dx}\dfrac{\partial F}{\partial y'} - \dfrac{\partial F}{\partial y} = 0$ | równanie Eulera–Lagrange'a | warunek ekstremum |
| $F - y'\dfrac{\partial F}{\partial y'} = \text{const}$ | całka pierwsza (tożsamość Beltramiego) | $F$ nie zależy jawnie od $x$ |
| $L = E_k - E_p$ | lagranżjan | siły zachowawcze |
| $S = \int L\,dt$, $\delta S = 0$ | zasada Hamiltona | ustalone położenia w $t_1$ i $t_2$ |
| $x = R(\varphi - \sin\varphi)$, $y = -R(1 - \cos\varphi)$ | cykloida (brachistochrona) | start z zerową prędkością |

## [28.02 — Więzy, współrzędne uogólnione i równania Lagrange'a](02-rownania-lagrangea.md)

| Wzór | Znaczenie | Kiedy obowiązuje |
|---|---|---|
| $n = 3N - k$ | liczba stopni swobody | $N$ punktów, $k$ więzów holonomicznych |
| $L(q, \dot q, t) = E_k - E_p$ | lagranżjan | siły zachowawcze |
| $\dfrac{d}{dt}\dfrac{\partial L}{\partial\dot q_i} - \dfrac{\partial L}{\partial q_i} = Q_i$ | równania Lagrange'a | $Q_i$ — siły niezachowawcze (0, gdy ich brak) |
| $E_k = \tfrac12\sum m_j\dot{\vec r}_j^2$, $\vec r_j = \vec r_j(q_1, \dots, q_n, t)$ | energia kinetyczna przez $q_i$ | — |
| $\cos\theta_0 = g/(\omega^2R)$ | położenie koralika na okręgu | $\omega^2 > g/R$ |

## [28.03 — Symetrie i prawa zachowania — twierdzenie Noether](03-symetrie-i-prawa-zachowania.md)

| Wzór | Znaczenie | Kiedy obowiązuje |
|---|---|---|
| $p_i = \partial L/\partial\dot q_i$ | pęd uogólniony | — |
| $\partial L/\partial q_i = 0 \Rightarrow p_i = \text{const}$ | współrzędna cykliczna | — |
| $h = \sum\dot q_i\,\partial L/\partial\dot q_i - L = \text{const}$ | całka Jacobiego (energia) | $L$ nie zależy jawnie od $t$ |
| $h = E_k + E_p$ | — | $E_k$ kwadratowa w $\dot q$, więzy niezależne od czasu |
| $V_{\text{ef}}(r) = V(r) + p_\varphi^2/(2mr^2)$ | potencjał efektywny | pole centralne |
| $\dfrac{dA}{dt} = \dfrac{p_\varphi}{2m}$ | prędkość polowa | II prawo Keplera |

## [28.04 — Funkcja Hamiltona, równania Hamiltona i przestrzeń fazowa](04-rownania-hamiltona.md)

| Wzór | Znaczenie | Kiedy obowiązuje |
|---|---|---|
| $p_i = \partial L/\partial\dot q_i$ | pęd kanoniczny | — |
| $H = \sum p_i\dot q_i - L$ | hamiltonian | wyrażony przez $q$, $p$ |
| $\dot q_i = \partial H/\partial p_i$, $\dot p_i = -\partial H/\partial q_i$ | równania Hamiltona | — |
| $dH/dt = \partial H/\partial t$ | zachowanie $H$ | $H = \text{const}$, gdy nie zależy jawnie od $t$ |
| $H = \dfrac{p^2}{2m} + V(x)$ | cząstka w potencjale | — |
| $\oint p\,dq = 2\pi E/\omega$ | pole elipsy fazowej oscylatora | oscylator harmoniczny |

## [28.05 — Małe drgania i drgania sprzężone — mody normalne](05-mody-normalne.md)

| Wzór | Znaczenie | Kiedy obowiązuje |
|---|---|---|
| $M\ddot{\vec x} = -K\vec x$ | równania małych drgań | rozwinięcie wokół minimum energii |
| $\det(K - \omega^2M) = 0$ | równanie na częstości własne | — |
| $\omega_1 = \sqrt{g/l}$, $\omega_2 = \sqrt{g/l + 2\kappa/m}$ | wahadła sprzężone | małe wychylenia |
| $T_{\text{przek}} = \pi/(\omega_2 - \omega_1)$ | czas przekazania energii | jedno wahadło wychylone na starcie |
| $\omega_n = 2\sqrt{k/m}\sin\dfrac{n\pi}{2(N + 1)}$ | łańcuch $N$ mas | końce zamocowane |
| $\omega(q) = 2\sqrt{k/m}\lvert\sin(qa/2)\rvert$ | związek dyspersyjny łańcucha | łańcuch nieskończony, $a$ — odstęp mas |
