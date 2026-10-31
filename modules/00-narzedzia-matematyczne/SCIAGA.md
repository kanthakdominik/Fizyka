# 00 — ściąga: Narzędzia matematyczne fizyka

Wszystkie tabele **Wzory i założenia** z tematów modułu na jednej stronie — do powtórki i do sprawdzenia, czy pamiętasz, **kiedy** wolno użyć wzoru. Wyprowadzenia, przykłady i zadania są w tematach.

[← spis modułu](README.md)

## [00.01 — Wektory: składowe, iloczyn skalarny i wektorowy](01-wektory.md)

| Wzór | Znaczenie | Kiedy obowiązuje |
|---|---|---|
| $a = \sqrt{a_x^2 + a_y^2 + a_z^2}$ | długość wektora | układ prostokątny (kartezjański) |
| $a_x = a\cos\theta,\ a_y = a\sin\theta$ | składowe na płaszczyźnie | $\theta$ mierzony od dodatniej osi $x$ przeciwnie do ruchu wskazówek zegara |
| $\theta = \operatorname{atan2}(a_y, a_x)$ | kierunek wektora | sam $\arctan(a_y/a_x)$ myli ćwiartki II i III — sprawdzaj znaki składowych |
| $\vec{a}\cdot\vec{b} = ab\cos\varphi = a_xb_x + a_yb_y + a_zb_z$ | iloczyn skalarny | $\varphi$ — kąt między wektorami, $0 \le \varphi \le 180^\circ$ |
| $\cos\varphi = \dfrac{\vec{a}\cdot\vec{b}}{ab}$ | kąt między wektorami | $a, b \neq 0$ |
| $\vec{a}\times\vec{b} = (a_yb_z - a_zb_y)\hat{\imath} + (a_zb_x - a_xb_z)\hat{\jmath} + (a_xb_y - a_yb_x)\hat{k}$ | iloczyn wektorowy | układ prawoskrętny ($\hat{\imath}\times\hat{\jmath} = \hat{k}$) |
| $\lvert\vec{a}\times\vec{b}\rvert = ab\sin\varphi$ | pole równoległoboku | — |
| $\lvert\vec{a}+\vec{b}\rvert^2 = a^2 + b^2 + 2ab\cos\varphi$ | długość sumy (twierdzenie cosinusów) | $\varphi$ — kąt **między wektorami**, nie kąt w trójkącie |

## [00.02 — Funkcje i wykresy w fizyce, linearyzacja](02-funkcje-i-wykresy.md)

| Wzór | Znaczenie | Kiedy obowiązuje |
|---|---|---|
| $a = \dfrac{y_2 - y_1}{x_2 - x_1}$ | nachylenie prostej | punkty bierz **z narysowanej prostej**, daleko od siebie, a nie z tabeli pomiarów |
| $\ln(e^x) = x$, $\ln(ab) = \ln a + \ln b$, $\ln(a^n) = n\ln a$ | własności logarytmu | $a, b > 0$ |
| $e^{-\lambda T_{1/2}} = \tfrac12 \Rightarrow T_{1/2} = \dfrac{\ln 2}{\lambda}$ | czas połowicznego zaniku | zanik wykładniczy |
| $L = 10\log_{10}\dfrac{I}{I_0}\ \mathrm{dB}$ | poziom natężenia dźwięku | $I_0 = 10^{-12}\ \mathrm{W/m^2}$ |

## [00.03 — Pochodna jako szybkość zmian](03-pochodna.md)

| Wzór | Uwagi |
|---|---|
| $(c)' = 0$, $(x^n)' = nx^{n-1}$ | $n$ dowolne rzeczywiste, np. $(\sqrt{x})' = \tfrac{1}{2\sqrt{x}}$, $(1/x)' = -1/x^2$ |
| $(cf)' = cf'$, $(f + g)' = f' + g'$ | liniowość |
| $(fg)' = f'g + fg'$ | iloczyn |
| $\left(\dfrac{f}{g}\right)' = \dfrac{f'g - fg'}{g^2}$ | iloraz, $g \neq 0$ |
| $\dfrac{d}{dt}f(g(t)) = f'(g(t))\cdot g'(t)$ | pochodna złożenia (reguła łańcuchowa) |
| $(\sin x)' = \cos x$, $(\cos x)' = -\sin x$ | $x$ w **radianach** |
| $(e^{x})' = e^{x}$, $(e^{kx})' = ke^{kx}$, $(\ln x)' = 1/x$ | $x > 0$ dla logarytmu |
| $\dfrac{d}{dt}\sin(\omega t) = \omega\cos(\omega t)$ | reguła łańcuchowa w drganiach |

## [00.04 — Całka jako suma: pole pod wykresem, praca, średnia](04-calka.md)

| Całka nieoznaczona | Uwagi |
|---|---|
| $\int x^n\,dx = \dfrac{x^{n+1}}{n+1} + C$ | $n \neq -1$ |
| $\int \dfrac{dx}{x} = \ln\lvert x\rvert + C$ | $x \neq 0$ |
| $\int e^{kx}\,dx = \dfrac{1}{k}e^{kx} + C$ | $k \neq 0$ |
| $\int \sin(\omega t)\,dt = -\dfrac{1}{\omega}\cos(\omega t) + C$ | radiany |
| $\int \cos(\omega t)\,dt = \dfrac{1}{\omega}\sin(\omega t) + C$ | radiany |
| $\int (af + bg)\,dx = a\int f\,dx + b\int g\,dx$ | liniowość |
| $\int f(g(x))\,g'(x)\,dx = \int f(u)\,du$ | podstawienie $u = g(x)$ |
| $\int_a^b f\,dx = -\int_b^a f\,dx$ | zmiana kierunku całkowania zmienia znak |

## [00.05 — Proste równania różniczkowe w fizyce](05-rownania-rozniczkowe.md)

| Równanie | Rozwiązanie | Przykłady |
|---|---|---|
| $\dot{y} = -y/\tau$ | $y = y_0e^{-t/\tau}$ | rozpad ($\tau = 1/\lambda$), rozładowanie $RC$ ($\tau = RC$) |
| $\dot{y} = (y_\infty - y)/\tau$ | $y = y_\infty + (y_0 - y_\infty)e^{-t/\tau}$ | ładowanie $RC$, stygnięcie (prawo Newtona), spadek z oporem liniowym |
| $\ddot{x} = -\omega^2x$ | $x = A\cos(\omega t + \varphi)$, $T = 2\pi/\omega$ | sprężyna ($\omega^2 = k/m$), wahadło dla małych kątów, obwód $LC$ |
| $T_{1/2} = \tau\ln2$ | czas połowicznego zaniku | tylko dla zaniku wykładniczego |
| $A = \sqrt{x_0^2 + (v_0/\omega)^2}$ | amplituda z warunków początkowych | oscylator harmoniczny |

## [00.06 — Przybliżenia i szeregi (małe kąty, dwumian, Taylor)](06-przyblizenia-i-szeregi.md)

| Zastosowanie | Przybliżenie | Warunek |
|---|---|---|
| wahadło | $\sin\theta \approx \theta \Rightarrow T = 2\pi\sqrt{l/g}$ | $\theta_0 \lesssim 10^\circ$–$15^\circ$ (błąd okresu poniżej 0,5%) |
| ciążenie na wysokości $h$ | $g(h) \approx g_0\left(1 - \dfrac{2h}{R}\right)$ | $h \ll R$ |
| energia kinetyczna | $(\gamma - 1)mc^2 \approx \tfrac12mv^2$ | $v \ll c$ |
| interferencja | $\sin\theta \approx \tan\theta \approx y/L$ | $y \ll L$ |
| małe drgania wokół minimum $U$ | $k = U''(x_0)$, $\omega = \sqrt{U''(x_0)/m}$ | małe wychylenie |

## [00.07 — Współrzędne biegunowe, walcowe, sferyczne i całki wielokrotne](07-wspolrzedne-i-calki-wielokrotne.md)

| Wielkość | Wzór | Uwagi |
|---|---|---|
| masa | $m = \int\rho\,dV$ | $\rho$ może zależeć od położenia |
| środek masy | $\vec{r}_{\mathrm{SM}} = \dfrac{1}{m}\int\vec{r}\,dm$ | dla ciał symetrycznych leży na osi symetrii |
| moment bezwładności | $I = \int r_\perp^2\,dm$ | $r_\perp$ — odległość od **osi obrotu**, nie od początku układu |
| element powierzchni | $dA = dx\,dy = r\,dr\,d\varphi$ | nie zapomnij czynnika $r$ |
| element objętości | $dV = r\,dr\,d\varphi\,dz = r^2\sin\theta\,dr\,d\theta\,d\varphi$ | walcowe / sferyczne |
| pole koła, objętość kuli | $\int_0^R2\pi r\,dr = \pi R^2$, $\int_0^R4\pi r^2\,dr = \tfrac43\pi R^3$ | sprawdzian poprawności elementu |
