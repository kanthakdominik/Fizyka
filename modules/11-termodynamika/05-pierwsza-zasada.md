# 11.05 — I zasada termodynamiki i przemiany gazowe

> **Moduł:** [11 — Termodynamika i teoria kinetyczna](README.md) · **Poziom:** 🟢🔵 matura R + studia · **Status:** ✅ pełny
>
> **Czytaj:**
>
> - OpenStax, *Fizyka dla szkół wyższych*, t. 2, rozdz. 3: [§3.1–3.6](https://openstax.org/books/fizyka-dla-szk%C3%B3%C5%82-wy%C5%BCszych-tom-2/pages/3-1-uklady-termodynamiczne) · [wstęp do rozdziału](https://openstax.org/books/fizyka-dla-szk%C3%B3%C5%82-wy%C5%BCszych-tom-2/pages/3-wstep)
> - Halliday, Resnick, Walker, *Podstawy fizyki*, wyd. 2015, t. 2: §18.5 (s. 261), §19.7–19.9 (s. 306)
> - Halliday, Resnick, Walker, *Podstawy fizyki*, wyd. 1 (2003), t. 2: [§19.8–19.10, s. 202](https://home.agh.edu.pl/~czapli/Resnick_2.pdf#page=218), [§20.8–20.11, s. 239](https://home.agh.edu.pl/~czapli/Resnick_2.pdf#page=255) — PDF z serwera AGH

← [Gaz doskonały i kinetyczna teoria gazów](04-gaz-doskonaly-i-teoria-kinetyczna.md) · [spis modułu](README.md) · [Silniki cieplne, chłodziarki i cykl Carnota](06-silniki-i-cykl-carnota.md) →

## Po co to jest

Pierwsza zasada termodynamiki to zasada zachowania energii rozszerzona o ciepło. Energię wewnętrzną gazu można zmienić, ogrzewając go albo wykonując nad nim pracę. To podstawa działania silników, sprężarek, pomp ciepła i lodówek (11.06). Wyjaśnia też, dlaczego pompka rowerowa się nagrzewa, aerozol z puszki jest zimny, a powietrze spływające z gór grzeje (halny, fen). Wykresy $p$–$V$ i przemiany gazowe to obowiązkowy materiał maturalny i pierwszy semestr termodynamiki.

## Teoria w pigułce

**Energia wewnętrzna** $U$ to suma energii ruchu i oddziaływań wszystkich cząsteczek. Jest **funkcją stanu**: zależy tylko od stanu ($p$, $V$, $T$), a nie od drogi, którą do niego dotarto. Dla gazu doskonałego zależy tylko od temperatury: $U = \tfrac f2nRT$ (11.04).

**Praca gazu.** Gaz rozprężający się o $dV$ pod ciśnieniem $p$ wykonuje pracę $dW = p\,dV$. Dla skończonej przemiany

$$W = \int_{V_1}^{V_2}p\,dV,$$

czyli pole pod krzywą na wykresie $p$–$V$. Praca zależy od drogi, podobnie jak ciepło.

**Pierwsza zasada termodynamiki.** Używa się dwóch konwencji znaków, więc zawsze trzeba sprawdzić, którą przyjęto:

| Konwencja | Zapis | Znaczenie $W$ | Gdzie używana |
|---|---|---|---|
| inżynierska / OpenStax / Halliday | $\Delta U = Q - W$ | praca **wykonana przez gaz** | podręczniki akademickie |
| „fizyczna” / matura | $\Delta U = Q + W$ | praca **wykonana nad gazem** | polska szkoła, karta wzorów CKE |

W obu przypadkach $Q > 0$ oznacza ciepło dostarczone do gazu. W tym module używamy $\Delta U = Q - W$ z pracą wykonaną przez gaz, zgodnie z OpenStax.

**Przemiany gazu doskonałego** ($n$ moli):

| Przemiana | Warunek | $W$ (przez gaz) | $Q$ | $\Delta U$ |
|---|---|---|---|---|
| izochoryczna | $V$ = const | 0 | $nC_V\Delta T$ | $nC_V\Delta T$ |
| izobaryczna | $p$ = const | $p\Delta V = nR\Delta T$ | $nC_p\Delta T$ | $nC_V\Delta T$ |
| izotermiczna | $T$ = const | $nRT\ln(V_2/V_1)$ | $= W$ | 0 |
| adiabatyczna | $Q = 0$ | $-\Delta U$ | 0 | $nC_V\Delta T$ |

**Ciepła molowe** gazu doskonałego: $C_V = \tfrac f2R$, a z pierwszej zasady dla przemiany izobarycznej wynika **wzór Mayera**:

$$C_p = C_V + R, \qquad \gamma = \frac{C_p}{C_V} = \frac53\ \text{(jednoatomowy)},\ \frac75\ \text{(dwuatomowy)}.$$

**Przemiana adiabatyczna** (szybka albo w izolacji, bez wymiany ciepła):

$$pV^\gamma = \text{const}, \qquad TV^{\gamma - 1} = \text{const}.$$

Na wykresie $p$–$V$ adiabata jest bardziej stroma niż izoterma. Gaz sprężany adiabatycznie się grzeje, a rozprężany się chłodzi.

## Wzory i założenia

| Wzór | Znaczenie | Kiedy obowiązuje |
|---|---|---|
| $\Delta U = Q - W$ | I zasada (W — praca gazu) | zawsze |
| $W = \int p\,dV$ | praca gazu | przemiana kwazistatyczna |
| $\Delta U = nC_V\Delta T$ | zmiana energii wewnętrznej | gaz doskonały, **każda** przemiana |
| $C_p - C_V = R$ | wzór Mayera | gaz doskonały |
| $pV^\gamma$ = const, $\ TV^{\gamma-1}$ = const | adiabata | kwazistatyczna, $Q = 0$ |
| $W_{\text{cykl}} = \oint p\,dV = Q_{\text{netto}}$ | praca w cyklu = pole wewnątrz | cykl ($\Delta U = 0$) |

## Przykład rozwiązany

**Zadanie 1.** Jeden mol gazu jednoatomowego ogrzano izobarycznie o 100 K. Oblicz ciepło, pracę gazu i zmianę energii wewnętrznej.

$\Delta U = \tfrac32R\cdot100 \approx 1247\ \mathrm J$. $W = R\cdot100 \approx 831\ \mathrm J$. $Q = \tfrac52R\cdot100 \approx 2079\ \mathrm J$. Sprawdzenie: $Q - W = \Delta U$. Tylko 60% ciepła podnosi temperaturę, a reszta idzie na pracę rozprężania.

**Zadanie 2.** W silniku Diesla powietrze o temperaturze 300 K jest sprężane adiabatycznie dziesięciokrotnie. Oblicz temperaturę i ciśnienie po sprężeniu (początkowe ciśnienie 1 bar, $\gamma = 1{,}4$).

$T_2 = 300\cdot10^{0{,}4} \approx 754\ \mathrm K$ (ok. 480°C), czyli powyżej temperatury samozapłonu oleju napędowego (ok. 250°C). Dlatego silnik Diesla nie potrzebuje świecy zapłonowej. $p_2 = 10^{1{,}4} \approx 25\ \mathrm{bar}$.

### Wersja z rachunkiem różniczkowym i całkowym

**Zadanie.** (a) Oblicz pracę jednego mola gazu przy izotermicznym podwojeniu objętości w 300 K. (b) Wyprowadź równanie adiabaty.

(a) $W = \displaystyle\int_{V}^{2V}\frac{nRT}{V'}dV' = nRT\ln2 \approx 1729\ \mathrm J$. Gaz pobiera tyle samo ciepła, bo $\Delta U = 0$.

(b) Dla $Q = 0$: $nC_V\,dT = -p\,dV$. Różniczkując $pV = nRT$: $p\,dV + V\,dp = nR\,dT$. Po wyeliminowaniu $dT$:

$$C_V(p\,dV + V\,dp) = -Rp\,dV \Rightarrow C_pp\,dV + C_VV\,dp = 0 \Rightarrow \gamma\frac{dV}{V} + \frac{dp}{p} = 0.$$

Całkując: $\gamma\ln V + \ln p = \text{const}$, czyli $pV^\gamma = \text{const}$.

## Typowe pułapki

- **Konwencja znaków pracy.** To najczęstsze źródło błędów. Ustal, czy $W$ to praca gazu czy nad gazem, i trzymaj się jednej konwencji.
- **$\Delta U = nC_V\Delta T$ tylko dla izochory.** Wzór obowiązuje dla każdej przemiany gazu doskonałego, bo $U$ to funkcja stanu.
- **Przemiana adiabatyczna = izotermiczna.** W adiabatycznej $Q = 0$ i temperatura się zmienia. W izotermicznej $\Delta T = 0$, ale ciepło płynie.
- **Ciepło i praca to funkcje stanu.** Zależą od drogi. Tylko ich różnica $Q - W$ od drogi nie zależy.
- **Rozprężanie swobodne wykonuje pracę.** Gaz rozprężający się do próżni nie wykonuje pracy, a jego temperatura (dla gazu doskonałego) się nie zmienia.

## Doświadczenie / symulacja

**Pompka rowerowa.** Zatkaj wylot pompki palcem i kilka razy szybko sprężaj powietrze. Cylinder się nagrzewa (sprężanie prawie adiabatyczne plus tarcie). Dla porównania wypuść gaz z naboju do syfonu lub z puszki ze sprężonym powietrzem: puszka wyraźnie się chłodzi.

**Chmura w butelce.** Do plastikowej butelki wlej odrobinę ciepłej wody, zakręć i mocno ściśnij, a potem gwałtownie puść (lepiej: pompka z wentylem w korku). Adiabatyczne rozprężenie ochładza powietrze poniżej punktu rosy i pojawia się mgła. Tak powstają chmury w unoszącym się powietrzu.

**Symulacja PhET:** *Właściwości gazu* (*Gas Properties*) — utrzymuj stałą temperaturę lub objętość i obserwuj zmiany pozostałych parametrów.

**Python:** izoterma i adiabata na wykresie $p$–$V$ oraz praca jako całka.

```python
import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import quad

R, n, T0, gam = 8.314, 1.0, 300.0, 1.4
V0 = n*R*T0/1e5                                   # 1 bar
V = np.linspace(V0/10, V0, 300)
p_iso = n*R*T0/V
p_ad = 1e5*(V0/V)**gam
plt.plot(V*1e3, p_iso/1e5, label="izoterma 300 K"); plt.plot(V*1e3, p_ad/1e5, label="adiabata γ = 1,4")

W_iso = quad(lambda v: n*R*T0/v, V0, 2*V0)[0]
print(f"praca izotermy przy podwojeniu V: {W_iso:.0f} J (wzór nRT ln2 = {n*R*T0*np.log(2):.0f} J)")
print(f"sprężanie adiabatyczne 10×: T = {T0*10**(gam - 1):.0f} K, p = {10**gam:.1f} bar")
W_ad = quad(lambda v: 1e5*(V0/v)**gam, V0, V0/10)[0]            # praca gazu (ujemna)
print(f"praca gazu w tym sprężaniu: {W_ad:.0f} J, ΔU = nCvΔT = {n*2.5*R*(T0*10**(gam - 1) - T0):.0f} J")
plt.xlabel("V [L]"); plt.ylabel("p [bar]"); plt.grid(True); plt.legend(); plt.show()
```

## Zadania

### A. Poziom maturalny

1. Gaz pobrał 500 J ciepła i wykonał pracę 200 J. Jak zmieniła się jego energia wewnętrzna? Zapisz wynik w obu konwencjach znaków.

<details>
<summary>Odpowiedź</summary>

Wzrosła o 300 J. $\Delta U = Q - W_{\text{gazu}} = 500 - 200$, albo $\Delta U = Q + W_{\text{nad}} = 500 + (-200)$.
</details>

2. Dwa mole gazu dwuatomowego ogrzano izochorycznie o 50 K. Ile ciepła dostarczono?

<details>
<summary>Odpowiedź</summary>

$Q = n\cdot\tfrac52R\cdot\Delta T \approx 2079\ \mathrm J$.
</details>

3. Gaz przechodzi cykl prostokątny na wykresie $p$–$V$: ciśnienia 1 bar i 2 bar, objętości 1 L i 3 L, w kierunku zgodnym z ruchem wskazówek zegara. Oblicz pracę wykonaną w cyklu i ciepło netto.

<details>
<summary>Odpowiedź</summary>

$W = \Delta p\,\Delta V = 10^5\cdot2\cdot10^{-3} = 200\ \mathrm J$ (pole prostokąta). Ciepło netto też wynosi 200 J, bo $\Delta U = 0$.
</details>

4. Dlaczego pompka rowerowa grzeje się przy pompowaniu?

<details>
<summary>Odpowiedź</summary>

Szybkie sprężanie jest prawie adiabatyczne. Praca wykonana nad gazem zwiększa jego energię wewnętrzną i temperaturę, a gorący gaz ogrzewa cylinder. Dokłada się tarcie tłoka.
</details>

### B. Poziom akademicki

1. Jeden mol gazu jednoatomowego o temperaturze 300 K sprężono adiabatycznie do połowy objętości. Oblicz temperaturę końcową i pracę wykonaną nad gazem.

<details>
<summary>Odpowiedź</summary>

$T_2 = 300\cdot2^{2/3} \approx 476\ \mathrm K$. $W_{\text{nad}} = \Delta U = \tfrac32R(476 - 300) \approx 2{,}2\ \mathrm{kJ}$.
</details>

2. Pokaż, że praca gazu w przemianie adiabatycznej wynosi $W = \dfrac{p_1V_1 - p_2V_2}{\gamma - 1}$.

<details>
<summary>Odpowiedź</summary>

$W = -\Delta U = -nC_V(T_2 - T_1) = \dfrac{C_V}{R}(p_1V_1 - p_2V_2)$, a $C_V/R = 1/(\gamma - 1)$. To samo daje całka $\int p_1V_1^\gamma V^{-\gamma}dV$.
</details>

3. Powietrze spływa po zawietrznej stronie Tatr z wysokości 2500 m do 700 m (halny). Ciśnienie rośnie od ok. 750 do 930 hPa. Oszacuj ogrzanie powietrza, traktując proces jako adiabatyczny. Wyjdź od temperatury 0°C na grani.

<details>
<summary>Odpowiedź</summary>

$T \propto p^{(\gamma-1)/\gamma}$: $273\cdot(930/750)^{0{,}286} \approx 290\ \mathrm K$, czyli ok. 17°C. Ogrzanie wynosi ok. 17 K, czyli ok. 1 K na 100 m (sucho-adiabatyczny gradient).
</details>

4. Uzasadnij, dlaczego adiabata jest bardziej stroma niż izoterma, obliczając $dp/dV$ dla obu w tym samym punkcie.

<details>
<summary>Odpowiedź</summary>

Izoterma: $dp/dV = -p/V$. Adiabata: $dp/dV = -\gamma p/V$. Ponieważ $\gamma > 1$, adiabata jest $\gamma$ razy bardziej stroma.
</details>

## Źródła

- OpenStax, *Fizyka dla szkół wyższych*, t. 2, rozdz. 3 — §3.1–3.6: układy termodynamiczne, praca, ciepło i energia wewnętrzna, I zasada, przemiany termodynamiczne, ciepła molowe gazu doskonałego, przemiany adiabatyczne.
- Halliday, Resnick, Walker, *Podstawy fizyki* — wyd. 2015: t. 2, §18.5, §19.7–19.9; wyd. 1: t. 2, §19.8–19.10, §20.8–20.11.
- Informator i karta wzorów CKE (konwencja $\Delta U = Q + W$).
