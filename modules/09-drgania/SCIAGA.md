# 09 — ściąga: Drgania

Wszystkie tabele **Wzory i założenia** z tematów modułu na jednej stronie — do powtórki i do sprawdzenia, czy pamiętasz, **kiedy** wolno użyć wzoru. Wyprowadzenia, przykłady i zadania są w tematach.

[← spis modułu](README.md)

## [09.01 — Ruch harmoniczny prosty i jego równanie](01-ruch-harmoniczny.md)

| Wzór | Znaczenie | Kiedy obowiązuje |
|---|---|---|
| $x = A\cos(\omega t + \varphi)$ | równanie ruchu | siła $F = -kx$ |
| $\omega = \sqrt{k/m}$, $\ T = 2\pi\sqrt{m/k}$ | częstość i okres ciężarka na sprężynie | sprężyna nieważka, prawo Hooke'a |
| $v_{\max} = A\omega$, $\ a_{\max} = A\omega^2$ | wartości maksymalne | — |
| $a = -\omega^2x$ | warunek ruchu harmonicznego | — |
| $A = \sqrt{x_0^2 + (v_0/\omega)^2}$ | amplituda z warunków początkowych | — |
| $k_{\text{rów}} = k_1 + k_2$; $\ \dfrac{1}{k_{\text{szer}}} = \dfrac{1}{k_1} + \dfrac{1}{k_2}$ | sprężyny równolegle i szeregowo | — |

## [09.02 — Energia w ruchu harmonicznym](02-energia-w-ruchu-harmonicznym.md)

| Wzór | Znaczenie | Kiedy obowiązuje |
|---|---|---|
| $E = \tfrac12kA^2 = \tfrac12m\omega^2A^2$ | energia drgań | brak tłumienia |
| $E_p = \tfrac12kx^2$, $\ E_k = E - E_p$ | podział energii | — |
| $v(x) = \omega\sqrt{A^2 - x^2}$ | prędkość w położeniu $x$ | — |
| $\overline{E_k} = \overline{E_p} = E/2$ | średnie w okresie | — |
| $E_k = E_p$ dla $x = \pm A/\sqrt2$ | punkt równego podziału | — |

## [09.03 — Wahadło matematyczne, fizyczne i torsyjne](03-wahadla.md)

| Wzór | Znaczenie | Kiedy obowiązuje |
|---|---|---|
| $T = 2\pi\sqrt{l/g}$ | wahadło matematyczne | małe kąty ($\lesssim 10^\circ$–$15^\circ$) |
| $T = 2\pi\sqrt{I/(mgd)}$ | wahadło fizyczne | małe kąty; $I$ względem osi obrotu |
| $T = 2\pi\sqrt{I/\kappa}$ | wahadło torsyjne | prawo Hooke'a dla skręcania |
| $T \approx T_0(1 + \theta_0^2/16)$ | poprawka na amplitudę | $\theta_0$ w radianach, umiarkowane kąty |
| $T = 2\pi\sqrt{l/g_{\text{ef}}}$ | wahadło w układzie przyspieszającym | $\vec g_{\text{ef}} = \vec g - \vec A$ (03.06) |

## [09.04 — Drgania tłumione](04-drgania-tlumione.md)

| Wzór | Znaczenie | Kiedy obowiązuje |
|---|---|---|
| $\ddot x + 2\beta\dot x + \omega_0^2x = 0$ | równanie oscylatora tłumionego | opór $\propto v$ |
| $x = A_0e^{-\beta t}\cos(\omega_dt + \varphi)$ | słabe tłumienie | $\beta < \omega_0$ |
| $\omega_d = \sqrt{\omega_0^2 - \beta^2}$ | częstość drgań tłumionych | j.w. |
| $b_{\text{kr}} = 2\sqrt{km}$ | tłumienie krytyczne | $\beta = \omega_0$ |
| $E(t) = E_0e^{-2\beta t}$ | zanik energii | słabe tłumienie |
| $\delta = \beta T_d$, $\ Q = \omega_0/(2\beta) \approx \pi/\delta$ | dekrement, dobroć | $Q \gg 1$ |

## [09.05 — Drgania wymuszone i rezonans](05-drgania-wymuszone-i-rezonans.md)

| Wzór | Znaczenie | Kiedy obowiązuje |
|---|---|---|
| $A(\omega) = \dfrac{F_0/m}{\sqrt{(\omega_0^2 - \omega^2)^2 + 4\beta^2\omega^2}}$ | amplituda drgań wymuszonych | stan ustalony |
| $\tan\delta = \dfrac{2\beta\omega}{\omega_0^2 - \omega^2}$ | przesunięcie fazy | j.w. |
| $\omega_{\text{rez}} = \sqrt{\omega_0^2 - 2\beta^2}$ | częstość największej amplitudy | $\beta < \omega_0/\sqrt2$ |
| $A_{\max} \approx QF_0/k$ | amplituda w rezonansie | $Q \gg 1$ |
| $\Delta\omega \approx 2\beta = \omega_0/Q$ | szerokość rezonansu | j.w. |

## [09.06 — Składanie drgań: dudnienia i krzywe Lissajous](06-skladanie-drgan.md)

| Wzór | Znaczenie | Kiedy obowiązuje |
|---|---|---|
| $A = \sqrt{A_1^2 + A_2^2 + 2A_1A_2\cos\Delta\varphi}$ | amplituda sumy | ta sama częstość i kierunek |
| $\tan\varphi = \dfrac{A_1\sin\varphi_1 + A_2\sin\varphi_2}{A_1\cos\varphi_1 + A_2\cos\varphi_2}$ | faza sumy | j.w. |
| $f_{\text{d}} = \lvert f_1 - f_2\rvert$ | częstotliwość dudnień | $f_1 \approx f_2$ |
| $\cos a + \cos b = 2\cos\frac{a - b}{2}\cos\frac{a + b}{2}$ | tożsamość | — |
| $f_x : f_y = n_y : n_x$ | krzywe Lissajous | $n$ — liczba styczności z bokami prostokąta |
