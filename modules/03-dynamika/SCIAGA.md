# 03 — ściąga: Dynamika punktu materialnego

Wszystkie tabele **Wzory i założenia** z tematów modułu na jednej stronie — do powtórki i do sprawdzenia, czy pamiętasz, **kiedy** wolno użyć wzoru. Wyprowadzenia, przykłady i zadania są w tematach.

[← spis modułu](README.md)

## [03.01 — Zasady dynamiki Newtona i rodzaje sił](01-zasady-dynamiki.md)

| Wzór | Znaczenie | Kiedy obowiązuje |
|---|---|---|
| $\sum\vec{F} = m\vec{a}$ | II zasada dynamiki | układ inercjalny, $m = \text{const}$, $v \ll c$ |
| $\vec{F} = d\vec{p}/dt$ | II zasada w postaci ogólnej | także dla zmiennej masy układu (05.05) |
| $\vec{F}_{AB} = -\vec{F}_{BA}$ | III zasada | siły działają na różne ciała |
| $Q = mg$ | ciężar | $g \approx 9{,}81\ \mathrm{m/s^2}$ przy powierzchni Ziemi |
| $F = kx$ | siła sprężystości | małe odkształcenia (granica sprężystości) |

## [03.02 — Diagramy sił i układy ciał (równia, bloczki, więzy)](02-uklady-cial.md)

| Wzór | Znaczenie | Założenia |
|---|---|---|
| $a = g\sin\alpha$, $\ N = mg\cos\alpha$ | równia bez tarcia | jedyne siły: ciężar i reakcja |
| $a = \dfrac{m_1 - m_2}{m_1 + m_2}g$ | maszyna Atwooda | nić nieważka i nierozciągliwa, bloczek nieważki bez tarcia |
| $a = \dfrac{m_2}{m_1 + m_2}g$, $\ T = m_1a$ | klocek $m_1$ na stole, $m_2$ wiszący | stół bez tarcia |
| $a = \dfrac{F}{m_1 + m_2}$, $\ F_{12} = m_2a$ | siła pchająca dwa klocki | siła $F$ przyłożona do $m_1$ |

## [03.03 — Tarcie statyczne i kinetyczne](03-tarcie.md)

| Wzór | Znaczenie | Kiedy obowiązuje |
|---|---|---|
| $T_s \le \mu_sN$ | tarcie statyczne | brak poślizgu; wartość z równań równowagi |
| $T_k = \mu_kN$ | tarcie kinetyczne | poślizg; model przybliżony |
| $\tan\alpha_{\text{gr}} = \mu_s$ | kąt, przy którym klocek rusza | równia, brak innych sił |
| $a = g(\sin\alpha - \mu_k\cos\alpha)$ | zsuwanie się z równi | $\tan\alpha > \mu_s$ |
| $s = \dfrac{v^2}{2\mu g}$ | droga hamowania | koła zablokowane ($\mu_k$) lub ABS (bliżej $\mu_s$) |

## [03.04 — Dynamika ruchu po okręgu](04-dynamika-ruchu-po-okregu.md)

| Wzór | Znaczenie | Kiedy obowiązuje |
|---|---|---|
| $\sum F_r = mv^2/R$ | II zasada w kierunku do środka | ruch po okręgu (także niejednostajny — składowa promieniowa) |
| $v_{\max} = \sqrt{\mu_sgR}$ | płaski zakręt | koła się nie ślizgają |
| $\tan\theta = v^2/(gR)$ | idealne wyprofilowanie | bez tarcia |
| $v_{\min} = \sqrt{gR}$ | górny punkt pętli / okręgu na lince | ciało nie odpada / linka napięta |
| $T = 2\pi\sqrt{\dfrac{L\cos\theta}{g}}$ | okres wahadła stożkowego | długość linki $L$, kąt od pionu $\theta$ |

## [03.05 — Opór ośrodka i prędkość graniczna — równanie ruchu](05-opor-osrodka.md)

| Wzór | Znaczenie | Kiedy obowiązuje |
|---|---|---|
| $F = 6\pi\eta rv$ | prawo Stokesa | kula, $\mathrm{Re} \lesssim 1$ |
| $F = \tfrac12C\rho Av^2$ | opór kwadratowy | $\mathrm{Re} \gtrsim 10^3$ |
| $v_g = \dfrac{2r^2(\rho_k - \rho_c)g}{9\eta}$ | prędkość graniczna kulki w cieczy | Stokes + wypór |
| $v_g = \sqrt{2mg/(C\rho A)}$ | prędkość graniczna, opór kwadratowy | bez wyporu (powietrze) |
| $v = v_g(1 - e^{-t/\tau})$, $\tau = m/b$ | rozpędzanie z oporem liniowym | start z $v = 0$ |
| $v = v_g\tanh(gt/v_g)$ | rozpędzanie z oporem kwadratowym | start z $v = 0$ |

## [03.06 — Układy nieinercjalne i siły bezwładności](06-uklady-nieinercjalne.md)

| Wzór | Znaczenie | Kiedy obowiązuje |
|---|---|---|
| $\vec{F}_b = -m\vec{A}$ | siła bezwładności | układ poruszający się postępowo z przyspieszeniem $\vec{A}$ |
| $\vec{g}_{\text{ef}} = \vec{g} - \vec{A}$ | efektywne przyspieszenie „grawitacyjne” | j.w. |
| $\tan\theta = A/g$ | odchylenie wahadła | przyspieszenie poziome |
| $F_{\text{odśr}} = m\omega^2r$ | siła odśrodkowa | układ obracający się, $r$ — odległość od osi |
| $\vec{F}_C = -2m\vec{\omega}\times\vec{v}\,'$ | siła Coriolisa | $\vec{v}\,'$ — prędkość względem układu obracającego się |
| $T_F = \dfrac{T_{\text{doby gw}}}{\sin\varphi}$ | okres obrotu płaszczyzny wahadła Foucaulta | szerokość geograficzna $\varphi$ |
