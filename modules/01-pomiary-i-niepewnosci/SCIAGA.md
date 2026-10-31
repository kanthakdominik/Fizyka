# 01 — ściąga: Pomiar, jednostki i niepewności

Wszystkie tabele **Wzory i założenia** z tematów modułu na jednej stronie — do powtórki i do sprawdzenia, czy pamiętasz, **kiedy** wolno użyć wzoru. Wyprowadzenia, przykłady i zadania są w tematach.

[← spis modułu](README.md)

## [01.01 — Układ SI i stałe definicyjne](01-uklad-si.md)

| Reguła | Przykład | Uwagi |
|---|---|---|
| zamiana przez mnożenie przez „jedynkę” | $72\ \dfrac{\mathrm{km}}{\mathrm{h}}\cdot\dfrac{1000\ \mathrm{m}}{1\ \mathrm{km}}\cdot\dfrac{1\ \mathrm{h}}{3600\ \mathrm{s}} = 20\ \mathrm{m/s}$ | jednostki skracają się jak liczby |
| przedrostek przy jednostce w potędze | $1\ \mathrm{cm^2} = (10^{-2}\ \mathrm{m})^2 = 10^{-4}\ \mathrm{m^2}$ | potęga obejmuje też przedrostek |
| kilowatogodzina | $1\ \mathrm{kWh} = 3{,}6\cdot10^{6}\ \mathrm{J}$ | jednostka energii, nie mocy |
| temperatura | $T[\mathrm{K}] = t[^\circ\mathrm{C}] + 273{,}15$ | różnica 1 K = różnica $1\ ^\circ\mathrm{C}$ |
| obie strony równania mają tę samą jednostkę | $[x] = [v_0t] = [\tfrac12at^2] = \mathrm{m}$ | dodawać można tylko wielkości tej samej jednostki |

## [01.02 — Analiza wymiarowa i szacowanie rzędu wielkości](02-analiza-wymiarowa-i-szacowanie.md)

| Wielkość | Wymiar | Wielkość | Wymiar |
|---|---|---|---|
| prędkość | $\mathsf{L\,T^{-1}}$ | energia, praca | $\mathsf{M\,L^2\,T^{-2}}$ |
| przyspieszenie | $\mathsf{L\,T^{-2}}$ | moc | $\mathsf{M\,L^2\,T^{-3}}$ |
| siła | $\mathsf{M\,L\,T^{-2}}$ | ciśnienie | $\mathsf{M\,L^{-1}\,T^{-2}}$ |
| pęd | $\mathsf{M\,L\,T^{-1}}$ | gęstość | $\mathsf{M\,L^{-3}}$ |
| częstotliwość, $\omega$ | $\mathsf{T^{-1}}$ | kąt, liczba | bezwymiarowe |

| Wartość do szacunków | Rząd wielkości |
|---|---|
| rok | $3\cdot10^7\ \mathrm{s}$ |
| promień Ziemi | $6\cdot10^6\ \mathrm{m}$ |
| masa człowieka | $70\ \mathrm{kg} \sim 10^2\ \mathrm{kg}$ |
| liczba Polaków | $4\cdot10^7$ |
| gęstość wody, skał | $10^3$, $3\cdot10^3\ \mathrm{kg/m^3}$ |

## [01.03 — Niepewności pomiarowe: typ A, typ B, niepewność złożona](03-niepewnosci-pomiarowe.md)

| Wzór | Znaczenie | Kiedy obowiązuje |
|---|---|---|
| $u_A = s/\sqrt{n}$ | niepewność średniej z $n$ pomiarów | wyniki niezależne, rozrzut przypadkowy; $n \gtrsim 5$ |
| $u_B = \Delta/\sqrt3$ | niepewność z dokładności przyrządu | znamy tylko granice $\pm\Delta$ |
| $u = \sqrt{u_A^2 + u_B^2}$ | łączenie obu typów | źródła niezależne |
| $u(x \pm y) = \sqrt{u_x^2 + u_y^2}$ | suma i różnica — niepewności **bezwzględne** | $x, y$ niezależne |
| $\dfrac{u(xy)}{xy} = \sqrt{\left(\tfrac{u_x}{x}\right)^2 + \left(\tfrac{u_y}{y}\right)^2}$ | iloczyn i iloraz — niepewności **względne** | to samo dla $x/y$ |
| $\dfrac{u(x^n)}{x^n} = \lvert n\rvert\dfrac{u_x}{x}$ | potęga | wykładnik mnoży niepewność względną |
| $\lvert x - x_{\text{ref}}\rvert \le 2u$ | wynik zgodny z odniesieniem | poziom ufności ok. 95% |

## [01.04 — Wykresy, linearyzacja i dopasowanie prostej](04-wykresy-i-dopasowanie.md)

Oznaczenie: $D = n\sum x_i^2 - \left(\sum x_i\right)^2$.

| Wzór | Znaczenie | Uwagi |
|---|---|---|
| $a = \dfrac{n\sum x_iy_i - \sum x_i\sum y_i}{D}$ | nachylenie | |
| $b = \dfrac{\sum y_i - a\sum x_i}{n}$ | wyraz wolny | prosta przechodzi przez punkt $(\bar{x}, \bar{y})$ |
| $s_y = \sqrt{\dfrac{\sum(y_i - ax_i - b)^2}{n - 2}}$ | rozrzut punktów wokół prostej | $n - 2$, bo wyznaczyliśmy dwa parametry |
| $u(a) = s_y\sqrt{\dfrac{n}{D}}$, $\ u(b) = s_y\sqrt{\dfrac{\sum x_i^2}{D}}$ | niepewności parametrów | gdy niepewności $y_i$ są podobne |
| $u(a) \approx \dfrac{a_{\max} - a_{\min}}{2}$ | z prostych skrajnych | metoda graficzna |

## [01.05 — Planowanie doświadczenia i raport z pomiarów](05-doswiadczenie-i-raport.md)

| Zasada | Uzasadnienie |
|---|---|
| szeroki zakres zmiennej niezależnej | nachylenie prostej jest wtedy wyznaczone pewniej |
| pomiar wielu okresów / wielu kartek / wielu obrotów naraz | niepewność odczytu dzieli się przez ich liczbę |
| powtórzenia pomiaru | pozwalają oszacować niepewność typu A i wykryć pomyłki |
| zmiana tylko jednej zmiennej naraz | inaczej nie wiadomo, co spowodowało efekt |
| wynik jako $(x \pm u)$ jednostka, niepewność 1–2 cyfry znaczące | standard zapisu |
| zgodność: $\lvert x - x_{\text{ref}}\rvert \le 2u$ | poziom ufności ok. 95% |
