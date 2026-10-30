# 08.03 — Równanie ciągłości i równanie Bernoulliego

> **Moduł:** [08 — Mechanika płynów](README.md) · **Poziom:** 🔵 studia · **Status:** ✅ pełny
>
> **Czytaj:**
>
> - OpenStax, *Fizyka dla szkół wyższych*, t. 1, rozdz. 14: [§14.5–14.6](https://openstax.org/books/fizyka-dla-szk%C3%B3%C5%82-wy%C5%BCszych-tom-1/pages/14-5-dynamika-plynow) · [wstęp do rozdziału](https://openstax.org/books/fizyka-dla-szk%C3%B3%C5%82-wy%C5%BCszych-tom-1/pages/14-wstep)
> - Halliday, Resnick, Walker, *Podstawy fizyki*, wyd. 2015, t. 2: §14.6–14.7 (s. 94)
> - Halliday, Resnick, Walker, *Podstawy fizyki*, wyd. 1 (2003), t. 2: [§15.8–15.10, s. 75](https://home.agh.edu.pl/~czapli/Resnick_2.pdf#page=91) — PDF z serwera AGH

← [Prawo Archimedesa i pływanie ciał](02-prawo-archimedesa.md) · [spis modułu](README.md) · [Lepkość i turbulencja](04-lepkosc-i-turbulencja.md) →

## Po co to jest

W płynącym płynie ciśnienie zależy od prędkości: tam, gdzie płyn płynie szybciej, ciśnienie jest mniejsze. To na pozór dziwne prawo tłumaczy działanie rozpylacza, gaźnika, zwężki Venturiego, rurki Pitota w samolocie, wypływ wody z otworu w zbiorniku i (częściowo) siłę nośną skrzydła. Równanie Bernoulliego to zasada zachowania energii zapisana dla płynu.

## Teoria w pigułce

**Model płynu doskonałego:** nieściśliwy ($\rho = \text{const}$), nielepki (bez tarcia wewnętrznego), przepływ ustalony (w danym punkcie prędkość się nie zmienia) i bezwirowy. Ruch opisujemy **liniami prądu** — torami cząstek płynu.

**Równanie ciągłości.** Ile płynu wpływa do odcinka rury, tyle z niego wypływa:

$$S_1v_1 = S_2v_2 = Q = \text{const},$$

gdzie $Q$ to **strumień objętości** (natężenie przepływu) w $\mathrm{m^3/s}$. W zwężeniu płyn płynie szybciej.

**Równanie Bernoulliego.** Wzdłuż linii prądu:

$$p + \tfrac12\rho v^2 + \rho gh = \text{const}.$$

Każdy składnik ma wymiar energii na jednostkę objętości: $p$ — praca sił ciśnienia, $\tfrac12\rho v^2$ — energia kinetyczna, $\rho gh$ — energia potencjalna. Gdy płyn spoczywa, równanie przechodzi w prawo hydrostatyki (08.01).

**Zastosowania.**
- **Wzór Torricellego:** prędkość wypływu z otworu na głębokości $h$ pod powierzchnią dużego zbiornika: $v = \sqrt{2gh}$ — jak w swobodnym spadku.
- **Zwężka Venturiego:** różnica ciśnień między szeroką i wąską częścią rury mierzy prędkość przepływu.
- **Rurka Pitota** (prędkościomierz samolotu): mierzy ciśnienie dynamiczne $\tfrac12\rho v^2$.
- **Rozpylacz, gaźnik, pompka wodna:** szybki strumień powietrza obniża ciśnienie i zasysa ciecz.

**Uwaga o skrzydle.** Popularne wyjaśnienie „powietrze nad skrzydłem ma dłuższą drogę, więc płynie szybciej” jest fałszywe. Prawdą jest, że nad skrzydłem powietrze płynie szybciej, a ciśnienie jest mniejsze (Bernoulli), ale przyczyną jest odchylanie strumienia powietrza w dół przez skrzydło (III zasada dynamiki) — oba opisy są równoważne.

## Wzory i założenia

| Wzór | Znaczenie | Kiedy obowiązuje |
|---|---|---|
| $S_1v_1 = S_2v_2$ | równanie ciągłości | płyn nieściśliwy |
| $p + \tfrac12\rho v^2 + \rho gh = \text{const}$ | równanie Bernoulliego | płyn doskonały, wzdłuż linii prądu |
| $v = \sqrt{2gh}$ | wzór Torricellego | otwór mały w porównaniu z powierzchnią zbiornika |
| $v = \sqrt{2\Delta p/\rho}$ | rurka Pitota | $\Delta p$ — ciśnienie dynamiczne |
| $Q = S_1S_2\sqrt{\dfrac{2\Delta p}{\rho(S_1^2 - S_2^2)}}$ | zwężka Venturiego | rura pozioma |

## Przykład rozwiązany

### Wersja z rachunkiem różniczkowym i całkowym

**Zadanie 1 — zwężenie rury.** Woda płynie poziomą rurą o średnicy 4 cm z prędkością 2 m/s; rura zwęża się do 2 cm. Oblicz prędkość w zwężeniu i różnicę ciśnień.

Z równania ciągłości (pole maleje 4 razy): $v_2 = 8\ \mathrm{m/s}$. Z Bernoulliego (bez zmiany wysokości):

$$\Delta p = \tfrac12\rho(v_2^2 - v_1^2) = \tfrac12\cdot1000\cdot(64 - 4) = 30\ \mathrm{kPa}.$$

W zwężeniu ciśnienie jest o 30 kPa **mniejsze**. Gdyby spadło poniżej ciśnienia pary wodnej, woda zaczęłaby wrzeć (kawitacja) — tak niszczą się śruby okrętowe.

**Zadanie 2 — opróżnianie zbiornika.** Cylindryczny zbiornik o polu przekroju $S = 1\ \mathrm{m^2}$ jest wypełniony wodą do wysokości $H = 1\ \mathrm{m}$. W dnie jest otwór o polu $s = 1\ \mathrm{cm^2}$. Po jakim czasie zbiornik się opróżni?

Prędkość wypływu (Torricelli) $\sqrt{2gh}$, a ubytek wody: $S\,\dfrac{dh}{dt} = -s\sqrt{2gh}$. Rozdzielając zmienne:

$$\int_H^0\frac{dh}{\sqrt h} = -\frac{s}{S}\sqrt{2g}\,t \Rightarrow t = \frac{S}{s}\sqrt{\frac{2H}{g}} = 10^4\cdot\sqrt{\frac{2}{9{,}81}} \approx 4500\ \mathrm{s} \approx 75\ \mathrm{min}.$$

Poziom opada coraz wolniej: pierwsza połowa wody (od $H$ do $H/2$) wypływa w ok. 29% całkowitego czasu, druga — w pozostałych 71%. (W rzeczywistości strumień się przewęża i czas jest dłuższy o ok. 40%.)

## Typowe pułapki

- **„Szybszy płyn = większe ciśnienie”.** Odwrotnie — w szybszym strumieniu ciśnienie statyczne jest mniejsze.
- **Bernoulli dla lepkich płynów w długich rurach.** Lepkość powoduje spadek ciśnienia wzdłuż rury (08.04), którego równanie Bernoulliego nie uwzględnia.
- **Bernoulli między różnymi liniami prądu.** Formalnie tylko wzdłuż jednej linii (dla przepływu bezwirowego — wszędzie).
- **Średnica zamiast pola.** Dwukrotnie mniejsza średnica to czterokrotnie mniejsze pole i czterokrotnie większa prędkość.
- **Gaz jako płyn nieściśliwy.** Dla powietrza w porządku do ok. 100 m/s (ok. 0,3 prędkości dźwięku).

## Doświadczenie / symulacja

**Wzór Torricellego z butelką.** Zrób w plastikowej butelce kilka otworów na różnych wysokościach, napełnij wodą i zmierz zasięg strumieni. Strumień z otworu na głębokości $h$ pod powierzchnią wylatuje poziomo z prędkością $\sqrt{2gh}$ i spada z wysokości $y$ — zasięg $2\sqrt{hy}$. Sprawdź, który otwór daje największy zasięg.

**Dwie kartki.** Dmuchnij między dwie zwisające kartki papieru — zbliżą się, a nie rozsuną.

**Symulacja PhET:** *Ciśnienie cieczy i przepływ* (*Fluid Pressure and Flow*, [phet.colorado.edu/pl](https://phet.colorado.edu/pl/)).

**Python:** opróżnianie zbiornika — rozwiązanie numeryczne równania $S\dot{h} = -s\sqrt{2gh}$ i porównanie z rozwiązaniem dokładnym.

```python
import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp

g, S, s, H = 9.81, 1.0, 1e-4, 1.0

def empty(t, y): return y[0] - 1e-6
empty.terminal = True

sol = solve_ivp(lambda t, y: [-s/S*np.sqrt(2*g*max(y[0], 0))], (0, 10000), [H], events=empty, max_step=5)
t = np.linspace(0, sol.t[-1], 200)
h_exact = (np.sqrt(H) - s/S*np.sqrt(g/2)*t)**2
print(f"czas opróżniania: numerycznie {sol.t[-1]:.0f} s, wzór {S/s*np.sqrt(2*H/g):.0f} s")
print(f"połowa wody wypływa po {S/s*np.sqrt(2/g)*(np.sqrt(H) - np.sqrt(H/2)):.0f} s")
plt.plot(sol.t/60, sol.y[0], label="numerycznie"); plt.plot(t/60, h_exact, "--", label="dokładnie")
plt.xlabel("t [min]"); plt.ylabel("h [m]"); plt.grid(True); plt.legend(); plt.show()
```

## Zadania

### A. Poziom maturalny _(opcjonalnie — rozgrzewka)_

1. Z otworu w beczce, 5 m pod powierzchnią wody, wypływa strumień. Z jaką prędkością?

<details>
<summary>Odpowiedź</summary>

$v = \sqrt{2gh} \approx 9{,}9\ \mathrm{m/s}$.
</details>

2. Dlaczego zatykając palcem część wylotu węża ogrodowego, zwiększamy zasięg strumienia?

<details>
<summary>Odpowiedź</summary>

Z równania ciągłości: mniejsze pole wylotu przy (w przybliżeniu) tym samym strumieniu objętości daje większą prędkość.
</details>

### B. Poziom akademicki

1. Rurka Pitota w samolocie pokazuje ciśnienie dynamiczne 600 Pa. Jaka jest prędkość samolotu względem powietrza ($\rho = 1{,}2\ \mathrm{kg/m^3}$)?

<details>
<summary>Odpowiedź</summary>

$v = \sqrt{2\cdot600/1{,}2} \approx 31{,}6\ \mathrm{m/s}$.
</details>

2. Nad skrzydłem samolotu o polu $20\ \mathrm{m^2}$ powietrze płynie z prędkością 70 m/s, pod skrzydłem — 60 m/s. Oszacuj siłę nośną.

<details>
<summary>Odpowiedź</summary>

$\Delta p = \tfrac12\cdot1{,}2(4900 - 3600) = 780\ \mathrm{Pa}$, $F \approx 15{,}6\ \mathrm{kN}$.
</details>

3. Woda płynie zwężką Venturiego: pole przekroju $S_1 = 20\ \mathrm{cm^2}$, w zwężeniu $S_2 = 5\ \mathrm{cm^2}$, różnica ciśnień 12 kPa. Oblicz strumień objętości.

<details>
<summary>Odpowiedź</summary>

$v_2^2 - v_1^2 = 24$, $v_2 = 4v_1$ ⇒ $15v_1^2 = 24$, $v_1 \approx 1{,}26\ \mathrm{m/s}$; $Q \approx 2{,}5\cdot10^{-3}\ \mathrm{m^3/s} = 2{,}5\ \mathrm{L/s}$.
</details>

4. Strumień wody z kranu (średnica 1 cm przy wylocie, prędkość 1 m/s) zwęża się, spadając. Jaką średnicę ma 20 cm niżej?

<details>
<summary>Odpowiedź</summary>

$v = \sqrt{1 + 2\cdot9{,}81\cdot0{,}2} \approx 2{,}22\ \mathrm{m/s}$; $d = 1\ \mathrm{cm}\cdot\sqrt{1/2{,}22} \approx 0{,}67\ \mathrm{cm}$.
</details>

## Źródła

- OpenStax, *Fizyka dla szkół wyższych*, t. 1, rozdz. 14 — §14.5 (dynamika płynów, równanie ciągłości) i §14.6 (równanie Bernoulliego).
- Halliday, Resnick, Walker, *Podstawy fizyki* — wyd. 2015: t. 2, §14.6–14.7; wyd. 1: t. 2, §15.8–15.10.
- Symulacja PhET *Ciśnienie cieczy i przepływ*.
