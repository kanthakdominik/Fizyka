# 24.01 — Cząstki elementarne i prawa zachowania

> **Moduł:** [24 — Cząstki elementarne i kosmologia](README.md) · **Poziom:** 🔵 studia · **Status:** ✅ pełny
>
> **Czytaj:**
>
> - OpenStax, *Fizyka dla szkół wyższych*, t. 3, rozdz. 11: [§11.1–11.2](https://openstax.org/books/fizyka-dla-szk%C3%B3%C5%82-wy%C5%BCszych-tom-3/pages/11-1-wstep-do-fizyki-czastek-elementarnych) · [wstęp do rozdziału](https://openstax.org/books/fizyka-dla-szk%C3%B3%C5%82-wy%C5%BCszych-tom-3/pages/11-wstep)
> - Halliday, Resnick, Walker, *Podstawy fizyki*, wyd. 2015, t. 5: §44.1–44.2 (s. 235)
> - Halliday, Resnick, Walker, *Podstawy fizyki*, wyd. 1 (2003), t. 5: [§45.1–45.6, s. 199](https://home.agh.edu.pl/~czapli/Resnick_5.pdf#page=215) — PDF z serwera AGH

← (początek modułu) · [spis modułu](README.md) · [Kwarki i Model Standardowy](02-kwarki-i-model-standardowy.md) →

## Po co to jest

Z czego zbudowana jest materia na najgłębszym poziomie i jakie reguły rządzą przemianami cząstek? W zderzeniach w akceleratorach i w promieniowaniu kosmicznym powstają i znikają setki rodzajów cząstek. Mimo tego chaosu pewne wielkości zawsze się zachowują: energia, pęd, ładunek, liczba barionowa, liczby leptonowe. Prawa zachowania pozwalają przewidzieć, które reakcje i rozpady są możliwe, a które zabronione. To podstawowe narzędzie fizyka cząstek, a zarazem zastosowanie relatywistycznej dynamiki (19.05) w czystej postaci.

## Teoria w pigułce

**Antycząstki.** Każda cząstka ma antycząstkę o tej samej masie i przeciwnym ładunku (i innych liczbach kwantowych). Pozyton przewidział Dirac (1928), a odkrył Anderson (1932) w promieniowaniu kosmicznym. Para cząstka–antycząstka może **anihilować**, np. $e^+ + e^- \to 2\gamma$ (po 0,511 MeV, podstawa tomografii PET), a foton o energii powyżej $2m_ec^2 = 1{,}022\ \mathrm{MeV}$ może w pobliżu jądra wytworzyć parę $e^+e^-$.

**Podział cząstek:**
- **fermiony** (spin połówkowy, podlegają zakazowi Pauliego) — budulec materii: leptony i kwarki (oraz bariony);
- **bozony** (spin całkowity) — nośniki oddziaływań (foton, gluony, W, Z), bozon Higgsa, mezony.

| Grupa | Przykłady | Oddziaływanie silne? |
|---|---|---|
| **leptony** | $e^-$, $\mu^-$, $\tau^-$ i trzy neutrina $\nu_e, \nu_\mu, \nu_\tau$ | nie |
| **mezony** (hadrony, kwark + antykwark) | $\pi^\pm, \pi^0$, $K^\pm, K^0$ | tak |
| **bariony** (hadrony, trzy kwarki) | $p$, $n$, $\Lambda^0$, $\Sigma$, $\Omega^-$ | tak |

**Cztery oddziaływania:**

| Oddziaływanie | Nośnik | Względna siła (ok. 1 fm) | Zasięg | Przykład |
|---|---|---|---|---|
| silne | gluony (8) | 1 | ok. 1 fm | wiązanie kwarków i nukleonów |
| elektromagnetyczne | foton | $10^{-2}$ | nieskończony | atomy, światło |
| słabe | $W^\pm$, $Z^0$ | $10^{-6}$ | ok. $10^{-3}$ fm | rozpad β, Słońce (22.06) |
| grawitacyjne | (grawiton?) | $10^{-38}$ | nieskończony | planety, gwiazdy |

**Zasięg a masa nośnika (Yukawa, 1935).** Wymiana cząstki o masie $m$ „pożycza” energię $mc^2$ na czas $\Delta t \sim \hbar/(mc^2)$ (20.05), więc zasięg to $R \approx c\Delta t = \hbar/(mc)$. Z zasięgu sił jądrowych (ok. 1,4 fm) Yukawa przewidział cząstkę o masie ok. 140 MeV/c², czyli pion, odkryty w 1947 r. Ciężkie bozony W i Z (80 i 91 GeV/c²) dają bardzo krótki zasięg oddziaływań słabych.

**Prawa zachowania:**
- **zawsze**: energia (z masą), pęd, moment pędu, ładunek elektryczny;
- **liczba barionowa** $B$: +1 dla barionów, −1 dla antybarionów, 0 dla pozostałych. Dlatego proton jest stabilny (zmierzony czas życia przekracza $10^{34}$ lat);
- **liczby leptonowe** $L_e$, $L_\mu$, $L_\tau$: każda zachowana osobno (z wyjątkiem oscylacji neutrin);
- **dziwność** $S$: zachowana w oddziaływaniach silnych i elektromagnetycznych, łamana w słabych ($|\Delta S| = 1$). Dziwne cząstki powstają parami (szybko, oddziaływanie silne), a rozpadają się powoli (słabo, ok. $10^{-10}$ s).

**Czasy życia** zdradzają oddziaływanie odpowiedzialne za rozpad: silne ok. $10^{-23}$ s, elektromagnetyczne ok. $10^{-16}$–$10^{-20}$ s, słabe od $10^{-13}$ s do 15 minut (neutron).

## Wzory i założenia

| Wzór | Znaczenie | Kiedy obowiązuje |
|---|---|---|
| $R \approx \hbar/(mc)$ | zasięg oddziaływania | wymiana cząstki o masie $m$ |
| $Q = \left(\sum m_{\text{przed}} - \sum m_{\text{po}}\right)c^2$ | energia reakcji (22.04) | — |
| $p^* = \dfrac{M^2 - m_1^2}{2M}c$ (dla $m_2 = 0$) | pęd w rozpadzie na dwie cząstki | układ spoczynkowy $M$ |
| $K_{\text{próg}} = \dfrac{(\sum m_{\text{po}})^2 - (m_a + m_b)^2}{2m_b}c^2$ | energia progowa | wiązka $a$ na tarczę $b$ w spoczynku |
| $\Delta B = 0$, $\Delta L_e = \Delta L_\mu = \Delta L_\tau = 0$, $\Delta Q = 0$ | prawa zachowania | zawsze |

## Przykład rozwiązany

**Zadanie 1.** Czy możliwe są reakcje: (a) $p \to e^+ + \gamma$, (b) $n \to p + e^- + \bar\nu_e$, (c) $\pi^- + p \to K^0 + \Lambda^0$, (d) $\mu^- \to e^- + \gamma$?

(a) Ładunek: +1 → +1 ✔. $B$: 1 → 0 ✘, a także $L_e$: 0 → −1 ✘. Zabroniona (stąd stabilność protonu).

(b) Ładunek 0 → 0 ✔, $B$: 1 → 1 ✔, $L_e$: 0 → +1 − 1 = 0 ✔. Dozwolona (rozpad β).

(c) Ładunek: 0 ✔, $B$: 1 → 1 ✔, dziwność: 0 → +1 + (−1) = 0 ✔. Dozwolona, silna: tak powstaje para dziwnych cząstek.

(d) Ładunek ✔, ale $L_\mu$: 1 → 0 i $L_e$: 0 → 1 ✘. Zabroniona (doświadczalnie: prawdopodobieństwo poniżej $10^{-12}$).

**Zadanie 2.** Spoczywający pion $\pi^+$ (139,57 MeV/c²) rozpada się na $\mu^+$ (105,66 MeV/c²) i neutrino (masa ≈ 0). Oblicz energię kinetyczną mionu.

Z zasady zachowania pędu mion i neutrino mają pędy o tej samej wartości $p$. Z zasady zachowania energii: $M = \sqrt{p^2 + m^2} + p$ (jednostki $c = 1$, energie w MeV), więc

$$p = \frac{M^2 - m^2}{2M} \approx 29{,}8\ \mathrm{MeV}/c, \qquad K_\mu = \sqrt{p^2 + m^2} - m \approx 4{,}1\ \mathrm{MeV}.$$

Neutrino unosi 29,8 MeV, czyli większość energii $Q = 33{,}9\ \mathrm{MeV}$.

### Wersja z rachunkiem różniczkowym i całkowym

**Energia progowa.** Wielkość $E^2 - (pc)^2$ dla całego układu jest niezmiennikiem (taka sama we wszystkich układach odniesienia, 19.05). Próg reakcji to sytuacja, w której produkty w układzie środka masy spoczywają. Dla wiązki $a$ o energii całkowitej $E_a$ na tarczę $b$ w spoczynku:

$$(E_a + m_bc^2)^2 - (p_ac)^2 = \left(\sum m_{\text{po}}c^2\right)^2 \Rightarrow K_{\text{próg}} = \frac{(\sum m_{\text{po}})^2 - (m_a + m_b)^2}{2m_b}c^2.$$

**Antyproton (Bevatron, 1955):** $p + p \to p + p + p + \bar p$. Próg: $K = \dfrac{(4m_p)^2 - (2m_p)^2}{2m_p}c^2 = 6m_pc^2 \approx 5{,}6\ \mathrm{GeV}$, choć masa wytworzonej pary to tylko $2m_pc^2 = 1{,}9\ \mathrm{GeV}$. Dlatego zbudowano akcelerator na 6,2 GeV i właśnie tam odkryto antyproton. Większość energii wiązki idzie na ruch środka masy.

## Typowe pułapki

- **Antymateria ma ujemną masę.** Masa jest taka sama. Przeciwne są ładunki i liczby kwantowe.
- **Neutrino jest cząstką bez masy.** Oscylacje neutrin dowodzą, że masa jest niezerowa, ale bardzo mała (poniżej ok. 1 eV/c²).
- **Mion to „ciężki elektron”, więc ma te same liczby leptonowe.** Ma $L_\mu = 1$, a $L_e = 0$.
- **Energia progowa to suma mas produktów minus suma mas substratów.** To wartość $Q$. Próg na nieruchomej tarczy jest większy, bo trzeba zachować pęd.

## Doświadczenie / symulacja

**Komora mgłowa w domu.** Akwarium lub słoik odwrócony dnem do góry, filc nasączony izopropanolem przy dnie (teraz górze), całość na suchym lodzie w ciemnym pokoju, oświetlona z boku latarką. Po kilku minutach widać ślady cząstek promieniowania kosmicznego: grube, krótkie (cząstki α z radonu), cienkie i proste (miony), kręte (elektrony). Instrukcje podaje CERN w materiałach dla szkół.

**Python:** sprawdzanie praw zachowania dla listy reakcji, kinematyka rozpadu dwuciałowego i energie progowe.

```python
import numpy as np

# ładunek Q, liczba barionowa B, Le, Lmu, dziwność S, masa [MeV/c²]
C = {"p": (1, 1, 0, 0, 0, 938.27), "n": (0, 1, 0, 0, 0, 939.57), "e-": (-1, 0, 1, 0, 0, 0.511),
     "e+": (1, 0, -1, 0, 0, 0.511), "nu_e": (0, 0, 1, 0, 0, 0), "anu_e": (0, 0, -1, 0, 0, 0),
     "mu-": (-1, 0, 0, 1, 0, 105.66), "mu+": (1, 0, 0, -1, 0, 105.66), "nu_mu": (0, 0, 0, 1, 0, 0),
     "anu_mu": (0, 0, 0, -1, 0, 0), "gamma": (0, 0, 0, 0, 0, 0), "pi+": (1, 0, 0, 0, 0, 139.57),
     "pi-": (-1, 0, 0, 0, 0, 139.57), "pi0": (0, 0, 0, 0, 0, 134.98), "K0": (0, 0, 0, 0, 1, 497.61),
     "K+": (1, 0, 0, 0, 1, 493.68), "Lambda": (0, 1, 0, 0, -1, 1115.68), "pbar": (-1, -1, 0, 0, 0, 938.27)}
nazwy = ["Q", "B", "Le", "Lmu", "S"]

def sprawdz(przed, po):
    s = lambda lista: np.sum([C[c][:5] for c in lista], axis=0)
    roznica = s(po) - s(przed)
    zlamane = [nazwy[i] for i in range(4) if roznica[i] != 0]       # Q, B, Le, Lmu: zawsze zachowane
    Qreak = sum(C[c][5] for c in przed) - sum(C[c][5] for c in po)
    if zlamane:
        return "zabroniona (łamie " + ", ".join(zlamane) + ")", Qreak
    if Qreak < 0 and len(przed) == 1:
        return "zabroniona energetycznie", Qreak
    return ("dozwolona tylko słabo (ΔS ≠ 0)" if roznica[4] != 0 else "dozwolona"), Qreak

for przed, po in [(["p"], ["e+", "gamma"]), (["n"], ["p", "e-", "anu_e"]), (["pi-", "p"], ["K0", "Lambda"]),
                  (["mu-"], ["e-", "gamma"]), (["mu-"], ["e-", "anu_e", "nu_mu"]), (["Lambda"], ["p", "pi-"])]:
    stan, Q = sprawdz(przed, po)
    print(f"{' + '.join(przed):10s} → {' + '.join(po):18s}: {stan:32s} Q = {Q:8.2f} MeV")

M, m = C["pi+"][5], C["mu+"][5]
p = (M**2 - m**2)/(2*M)
print(f"π+ → μ+ ν: p = {p:.2f} MeV/c, K_μ = {np.sqrt(p**2 + m**2) - m:.2f} MeV")
prog = lambda ma, mb, po: (sum(po)**2 - (ma + mb)**2)/(2*mb)
mp = C["p"][5]
print(f"próg p + p → p + p + π0: {prog(mp, mp, [mp, mp, C['pi0'][5]]):.1f} MeV")
print(f"próg p + p → p + p + p + p̄: {prog(mp, mp, [mp]*4)/1e3:.2f} GeV")
hbarc = 197.327
for nosnik, mm in [("pion", 139.57), ("W", 80377)]:
    print(f"zasięg wymiany {nosnik}: {hbarc/mm:.2e} fm")
```

## Zadania

### A. Poziom maturalny _(opcjonalnie — rozgrzewka)_

1. Pozyton i elektron w spoczynku anihilują. Ile fotonów powstaje, jakie mają energie i dlaczego nie może powstać jeden foton?

<details>
<summary>Odpowiedź</summary>

Dwa fotony po 0,511 MeV, lecące w przeciwne strony. Jeden foton miałby pęd, a początkowy pęd układu był równy zeru.
</details>

2. Oblicz zasięg oddziaływania przenoszonego przez pion (140 MeV/c²). Użyj $\hbar c = 197\ \mathrm{MeV\cdot fm}$.

<details>
<summary>Odpowiedź</summary>

$R \approx 197/140 \approx 1{,}4\ \mathrm{fm}$, czyli rozmiar nukleonu.
</details>

### B. Poziom akademicki

1. Sprawdź prawa zachowania: (a) $\pi^+ + n \to K^+ + \Lambda^0$, (b) $\pi^+ + n \to K^+ + n$, (c) $\Lambda^0 \to p + \pi^-$.

<details>
<summary>Odpowiedź</summary>

(a) $Q$: 1 → 1, $B$: 1 → 1, $S$: 0 → +1 − 1 = 0. Dozwolona (silna).

(b) $S$: 0 → +1. Łamie dziwność, więc oddziaływanie silne, które dominuje w zderzeniach hadronów, nie może jej wywołać. W praktyce nie obserwuje się jej.

(c) $S$: −1 → 0. Dozwolona tylko w oddziaływaniu słabym, stąd długi czas życia $\Lambda^0$ (ok. $2{,}6\cdot10^{-10}$ s).
</details>

2. Oblicz energię progową reakcji $p + p \to p + p + \pi^0$ dla protonu uderzającego w nieruchomy proton.

<details>
<summary>Odpowiedź</summary>

$K = \dfrac{(2m_p + m_\pi)^2 - (2m_p)^2}{2m_p}c^2 = \left(2m_\pi + \dfrac{m_\pi^2}{2m_p}\right)c^2 \approx 280\ \mathrm{MeV}$.
</details>

3. Rezonans $\Delta^{++}$ ma szerokość $\Gamma = 117\ \mathrm{MeV}$. Oszacuj jego czas życia i drogę, jaką przebywa (przy $\gamma\beta \approx 1$).

<details>
<summary>Odpowiedź</summary>

$\tau = \hbar/\Gamma = 6{,}58\cdot10^{-22}\ \mathrm{MeV\cdot s}/117\ \mathrm{MeV} \approx 5{,}6\cdot10^{-24}\ \mathrm s$. Droga $c\tau \approx 1{,}7\ \mathrm{fm}$, rozmiar protonu. Takiej cząstki nie widać w detektorze — rozpoznaje się ją po rozkładzie energii produktów.
</details>

4. Neutrino mionowe z rozpadu $\pi^+$ w spoczynku. Jaką długość fali de Broglie'a ma neutrino?

<details>
<summary>Odpowiedź</summary>

$p = 29{,}8\ \mathrm{MeV}/c$, $\lambda = h/p = 2\pi\hbar c/(pc) = 2\pi\cdot197{,}3/29{,}8\ \mathrm{fm} \approx 42\ \mathrm{fm}$.
</details>

## Źródła

- OpenStax, *Fizyka dla szkół wyższych*, t. 3, rozdz. 11 — §11.1 (wstęp do fizyki cząstek) i §11.2 (zasady zachowania).
- Halliday, Resnick, Walker, *Podstawy fizyki* — wyd. 2015: t. 5, §44.1–44.2; wyd. 1: t. 5, §45.1–45.6.
- CERN, materiały dla nauczycieli o komorze mgłowej (*Cloud chamber*, materiał dodatkowy, po angielsku).
