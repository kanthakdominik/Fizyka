# 07 — ściąga: Grawitacja i elementy astronomii

Wszystkie tabele **Wzory i założenia** z tematów modułu na jednej stronie — do powtórki i do sprawdzenia, czy pamiętasz, **kiedy** wolno użyć wzoru. Wyprowadzenia, przykłady i zadania są w tematach.

[← spis modułu](README.md)

## [07.01 — Prawo powszechnego ciążenia](01-prawo-grawitacji.md)

| Wzór | Znaczenie | Kiedy obowiązuje |
|---|---|---|
| $F = Gm_1m_2/r^2$ | prawo ciążenia | masy punktowe lub kule o symetrii sferycznej |
| $\vec{F}_{12} = -G\dfrac{m_1m_2}{r^2}\hat{r}_{12}$ | postać wektorowa | $\hat{r}_{12}$ — wersor od 1 do 2 (siła na 2) |
| $g = GM/R^2$ | przyspieszenie na powierzchni | pomijamy obrót planety |
| $g(h) = g_0R^2/(R + h)^2$ | przyspieszenie na wysokości $h$ | nad powierzchnią |
| $M = gR^2/G$ | masa planety z $g$ i $R$ | — |

## [07.02 — Natężenie pola, potencjał i energia grawitacyjna](02-pole-i-potencjal-grawitacyjny.md)

| Wzór | Znaczenie | Kiedy obowiązuje |
|---|---|---|
| $\gamma = GM/r^2$ | natężenie pola | na zewnątrz kuli o symetrii sferycznej |
| $U = -GMm/r$ | energia potencjalna | $U(\infty) = 0$ |
| $V = -GM/r$ | potencjał | j.w. |
| $\gamma_r = -dV/dr$ | związek pola z potencjałem | 1D/radialnie |
| $\Delta U = GMm\left(\dfrac{1}{r_1} - \dfrac{1}{r_2}\right)$ | praca przy oddaleniu z $r_1$ do $r_2$ | — |
| $v_{II} = \sqrt{2GM/R}$ | prędkość ucieczki | bez oporu atmosfery i innych ciał |
| $\gamma(r) = GMr/R^3$ | pole wewnątrz jednorodnej kuli | $r < R$ |

## [07.03 — Orbity, satelity i prędkości kosmiczne](03-orbity-i-predkosci-kosmiczne.md)

| Wzór | Znaczenie | Kiedy obowiązuje |
|---|---|---|
| $v = \sqrt{GM/r}$ | prędkość na orbicie kołowej | $m \ll M$ |
| $T = 2\pi\sqrt{r^3/GM}$ | okres obiegu | orbita kołowa |
| $v_I = \sqrt{gR} \approx 7{,}9\ \mathrm{km/s}$ | I prędkość kosmiczna | Ziemia, bez atmosfery |
| $v_{II} = \sqrt{2gR} \approx 11{,}2\ \mathrm{km/s}$ | II prędkość kosmiczna | j.w. |
| $E = -GMm/(2r)$ | energia na orbicie kołowej | $U(\infty) = 0$ |
| $r_{\text{geo}} = \sqrt[3]{GMT^2/(4\pi^2)}$ | orbita geostacjonarna | $T$ — doba gwiazdowa |

## [07.04 — Prawa Keplera](04-prawa-keplera.md)

| Wzór | Znaczenie | Kiedy obowiązuje |
|---|---|---|
| $r_p = a(1 - e)$, $\ r_a = a(1 + e)$ | peryhelium i aphelium | orbita eliptyczna |
| $v_pr_p = v_ar_a$ | II prawo (zachowanie $L$) | siła centralna |
| $dA/dt = L/(2m) = \text{const}$ | prędkość polowa | j.w. |
| $T^2 = \dfrac{4\pi^2}{GM}a^3$ | III prawo | $m \ll M$ |
| $v^2 = GM\left(\dfrac2r - \dfrac1a\right)$ | wzór vis-viva (prędkość w dowolnym punkcie) | orbita eliptyczna |
| $E = -\dfrac{GMm}{2a}$ | energia na orbicie eliptycznej | zależy tylko od $a$ |

## [07.05 — Pole rozkładu masy i siły pływowe](05-pole-rozkladu-masy-i-plywy.md)

| Wzór | Znaczenie | Kiedy obowiązuje |
|---|---|---|
| $\vec{\gamma} = -G\int\dfrac{dm}{r^2}\hat{r}$ | pole rozkładu masy | superpozycja |
| $\gamma = GM/r^2$ | na zewnątrz kuli | symetria sferyczna |
| $\gamma = 0$ | wewnątrz jednorodnej powłoki | — |
| $\gamma = \dfrac{GMz}{(z^2 + R^2)^{3/2}}$ | na osi pierścienia | odległość $z$ od środka pierścienia |
| $\Delta a = \dfrac{2GM}{r^3}\Delta r$ | przyspieszenie pływowe | $\Delta r \ll r$ |

## [07.06 — Elementy astronomii: odległości, gwiazdy, galaktyki](06-elementy-astronomii.md)

| Wzór | Znaczenie | Kiedy obowiązuje |
|---|---|---|
| $d\ [\mathrm{pc}] = 1/p\ [\text{″}]$ | odległość z paralaksy | małe kąty, gwiazdy bliskie (do kilku kpc) |
| $\lambda_{\max}T = 2{,}898\cdot10^{-3}\ \mathrm{m\cdot K}$ | prawo Wiena | ciało doskonale czarne |
| $L = 4\pi R^2\sigma T^4$ | jasność gwiazdy | j.w. |
| $I = L/(4\pi d^2)$ | natężenie w odległości $d$ | brak pochłaniania |
| $v = H_0d$, $\ v \approx cz$ | prawo Hubble'a | $z \ll 1$, galaktyki dalsze niż kilka Mpc |
