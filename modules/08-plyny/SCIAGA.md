# 08 — ściąga: Mechanika płynów

Wszystkie tabele **Wzory i założenia** z tematów modułu na jednej stronie — do powtórki i do sprawdzenia, czy pamiętasz, **kiedy** wolno użyć wzoru. Wyprowadzenia, przykłady i zadania są w tematach.

[← spis modułu](README.md)

## [08.01 — Ciśnienie, prawo Pascala, ciśnienie hydrostatyczne](01-cisnienie-i-prawo-pascala.md)

| Wzór | Znaczenie | Kiedy obowiązuje |
|---|---|---|
| $p = F/S$ | ciśnienie | siła prostopadła do powierzchni |
| $p = p_0 + \rho gh$ | ciśnienie hydrostatyczne | ciecz nieściśliwa, $g$ stałe |
| $F_2/F_1 = S_2/S_1$ | prasa hydrauliczna | prawo Pascala, ciecz w spoczynku |
| $\rho_1h_1 = \rho_2h_2$ | dwie ciecze w rurce U | ciecze się nie mieszają, poziomy od granicy cieczy |
| $p = p_0e^{-h/H}$, $\ H = RT/(Mg)$ | wzór barometryczny | atmosfera izotermiczna |

## [08.02 — Prawo Archimedesa i pływanie ciał](02-prawo-archimedesa.md)

| Wzór | Znaczenie | Kiedy obowiązuje |
|---|---|---|
| $F_w = \rho_pgV_{\text{zan}}$ | siła wyporu | płyn w spoczynku, $g$ stałe |
| $V_{\text{zan}}/V = \rho_c/\rho_p$ | część zanurzona | ciało pływające |
| $Q' = (\rho_c - \rho_p)gV$ | ciężar pozorny | ciało całkowicie zanurzone |
| $\rho_c = \rho_p\dfrac{Q}{Q - Q'}$ | gęstość z ważenia w powietrzu i cieczy | $Q$ — ciężar w powietrzu, $Q'$ — w cieczy |
| $F_{\text{nośna}} = (\rho_{\text{pow}} - \rho_{\text{gazu}})gV$ | siła nośna balonu | bez masy powłoki |

## [08.03 — Równanie ciągłości i równanie Bernoulliego](03-rownanie-bernoulliego.md)

| Wzór | Znaczenie | Kiedy obowiązuje |
|---|---|---|
| $S_1v_1 = S_2v_2$ | równanie ciągłości | płyn nieściśliwy |
| $p + \tfrac12\rho v^2 + \rho gh = \text{const}$ | równanie Bernoulliego | płyn doskonały, wzdłuż linii prądu |
| $v = \sqrt{2gh}$ | wzór Torricellego | otwór mały w porównaniu z powierzchnią zbiornika |
| $v = \sqrt{2\Delta p/\rho}$ | rurka Pitota | $\Delta p$ — ciśnienie dynamiczne |
| $Q = S_1S_2\sqrt{\dfrac{2\Delta p}{\rho(S_1^2 - S_2^2)}}$ | zwężka Venturiego | rura pozioma |

## [08.04 — Lepkość i turbulencja](04-lepkosc-i-turbulencja.md)

| Wzór | Znaczenie | Kiedy obowiązuje |
|---|---|---|
| $\tau = \eta\,dv/dy$ | prawo lepkości Newtona | płyny newtonowskie (woda, olej, powietrze) |
| $v(r) = \dfrac{\Delta p}{4\eta L}(R^2 - r^2)$ | profil prędkości | przepływ laminarny w rurze |
| $Q = \dfrac{\pi R^4\Delta p}{8\eta L}$ | prawo Poiseuille'a | j.w. |
| $\bar{v} = Q/(\pi R^2) = v_{\max}/2$ | prędkość średnia | j.w. |
| $\mathrm{Re} = \rho vd/\eta$ | liczba Reynoldsa | $\mathrm{Re} < 2000$ — laminarny (rura) |
| $F = 6\pi\eta rv$ | prawo Stokesa | kula, $\mathrm{Re} \lesssim 1$ (03.05) |
