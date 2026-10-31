# 11 — ściąga: Termodynamika i teoria kinetyczna

Wszystkie tabele **Wzory i założenia** z tematów modułu na jednej stronie — do powtórki i do sprawdzenia, czy pamiętasz, **kiedy** wolno użyć wzoru. Wyprowadzenia, przykłady i zadania są w tematach.

[← spis modułu](README.md)

## [11.01 — Temperatura i rozszerzalność cieplna](01-temperatura-i-rozszerzalnosc.md)

| Wzór | Znaczenie | Kiedy obowiązuje |
|---|---|---|
| $T[\mathrm K] = t[^\circ\mathrm C] + 273{,}15$ | przeliczenie skal | — |
| $t_F = \tfrac95t_C + 32$ | skala Fahrenheita | — |
| $\Delta L = \alpha L_0\Delta T$ | rozszerzalność liniowa | $\alpha\Delta T \ll 1$ |
| $\Delta V = \beta V_0\Delta T$, $\ \beta \approx 3\alpha$ | rozszerzalność objętościowa | ciało izotropowe |
| $\sigma = E\alpha\Delta T$ | naprężenie termiczne | końce unieruchomione, zakres sprężysty |

## [11.02 — Ciepło, ciepło właściwe, przemiany fazowe, kalorymetria](02-cieplo-i-przemiany-fazowe.md)

| Wzór | Znaczenie | Kiedy obowiązuje |
|---|---|---|
| $Q = mc\Delta T$ | ogrzewanie bez przemiany fazowej | $c$ stałe w zakresie temperatur |
| $Q = mL$ | przemiana fazowa | stała temperatura i ciśnienie |
| $\sum m_ic_i(T_k - T_i) = 0$ | temperatura końcowa mieszaniny | układ izolowany, bez przemian |
| $Q = \int mc(T)\,dT$ | gdy $c$ zależy od temperatury | — |
| $c_{\text{wody}} = 4190\ \mathrm{J/(kg\cdot K)}$, $L_t = 334\ \mathrm{kJ/kg}$, $L_p = 2256\ \mathrm{kJ/kg}$ | stałe dla wody | — |

## [11.03 — Przewodnictwo, konwekcja i promieniowanie cieplne](03-transport-ciepla.md)

| Wzór | Znaczenie | Kiedy obowiązuje |
|---|---|---|
| $P = kA\Delta T/L$ | przewodzenie przez płytę | stan ustalony |
| $R = L/(kA)$, $\ R_{\text{szer}} = \sum R_i$ | opór cieplny | warstwy szeregowo |
| $P = UA\Delta T$, $\ U = 1/\sum(L_i/k_i)$ | przenikanie przez przegrodę | j.w., na 1 m² |
| $P = hA(T - T_{\text{ot}})$ | prawo stygnięcia Newtona | niewielkie $\Delta T$, konwekcja |
| $P = \varepsilon\sigma AT^4$ | prawo Stefana–Boltzmanna | — |
| $\lambda_{\max}T = 2{,}898\cdot10^{-3}\ \mathrm{m\cdot K}$ | prawo Wiena | ciało doskonale czarne |

## [11.04 — Gaz doskonały i kinetyczna teoria gazów](04-gaz-doskonaly-i-teoria-kinetyczna.md)

| Wzór | Znaczenie | Kiedy obowiązuje |
|---|---|---|
| $pV = nRT = NkT$ | równanie stanu | gaz doskonały, $T$ w kelwinach |
| $p = \tfrac13(N/V)m\overline{v^2}$ | ciśnienie z teorii kinetycznej | j.w. |
| $\overline{E_k} = \tfrac32kT$ | energia ruchu postępowego | każdy gaz doskonały |
| $v_{\text{śr.kw.}} = \sqrt{3RT/M}$ | prędkość średnia kwadratowa | $M$ w kg/mol |
| $U = \tfrac f2nRT$ | energia wewnętrzna | $f$ = 3 (jednoatomowy), 5 (dwuatomowy) |
| $v_p : \bar v : v_{\text{śr.kw.}} = \sqrt2 : \sqrt{8/\pi} : \sqrt3$ | prędkości z rozkładu Maxwella | — |

## [11.05 — I zasada termodynamiki i przemiany gazowe](05-pierwsza-zasada.md)

| Wzór | Znaczenie | Kiedy obowiązuje |
|---|---|---|
| $\Delta U = Q - W$ | I zasada (W — praca gazu) | zawsze |
| $W = \int p\,dV$ | praca gazu | przemiana kwazistatyczna |
| $\Delta U = nC_V\Delta T$ | zmiana energii wewnętrznej | gaz doskonały, **każda** przemiana |
| $C_p - C_V = R$ | wzór Mayera | gaz doskonały |
| $pV^\gamma$ = const, $\ TV^{\gamma-1}$ = const | adiabata | kwazistatyczna, $Q = 0$ |
| $W_{\text{cykl}} = \oint p\,dV = Q_{\text{netto}}$ | praca w cyklu = pole wewnątrz | cykl ($\Delta U = 0$) |

## [11.06 — Silniki cieplne, chłodziarki i cykl Carnota](06-silniki-i-cykl-carnota.md)

| Wzór | Znaczenie | Kiedy obowiązuje |
|---|---|---|
| $W = Q_H - Q_C$ | bilans silnika | cykl, wartości dodatnie |
| $\eta = W/Q_H = 1 - Q_C/Q_H$ | sprawność silnika | — |
| $\eta_C = 1 - T_C/T_H$ | sprawność Carnota (maksymalna) | odwracalny, $T$ w kelwinach |
| $\text{COP}_{\text{chł}} = Q_C/W \le T_C/(T_H - T_C)$ | chłodziarka | — |
| $\text{COP}_{\text{pc}} = Q_H/W \le T_H/(T_H - T_C)$ | pompa ciepła | — |
| $\eta_{\text{Otto}} = 1 - r^{1 - \gamma}$ | cykl Otto | gaz doskonały, cykl idealny |

## [11.07 — Entropia i II zasada termodynamiki](07-entropia-i-druga-zasada.md)

| Wzór | Znaczenie | Kiedy obowiązuje |
|---|---|---|
| $\Delta S = \int dQ_{\text{odwr}}/T$ | definicja entropii | droga odwracalna |
| $\Delta S = mc\ln(T_2/T_1)$ | ogrzewanie | $c$ stałe |
| $\Delta S = mL/T$ | przemiana fazowa | stała $T$ |
| $\Delta S = nC_V\ln\frac{T_2}{T_1} + nR\ln\frac{V_2}{V_1}$ | gaz doskonały | dowolna przemiana |
| $\Delta S_{\text{izol}} \ge 0$ | II zasada termodynamiki | układ izolowany |
| $S = k\ln\Omega$ | entropia statystyczna | — |
