# 09.04 — Drgania tłumione

> **Moduł:** [09 — Drgania](README.md) · **Poziom:** 🔵 studia · **Status:** ✅ pełny
>
> **Czytaj:**
>
> - OpenStax, *Fizyka dla szkół wyższych*, t. 1, rozdz. 15: [§15.5](https://openstax.org/books/fizyka-dla-szk%C3%B3%C5%82-wy%C5%BCszych-tom-1/pages/15-5-drgania-tlumione) · [wstęp do rozdziału](https://openstax.org/books/fizyka-dla-szk%C3%B3%C5%82-wy%C5%BCszych-tom-1/pages/15-wstep)
> - Halliday, Resnick, Walker, *Podstawy fizyki*, wyd. 2015, t. 2: §15.5 (s. 137)
> - Halliday, Resnick, Walker, *Podstawy fizyki*, wyd. 1 (2003), t. 2: [§16.8, s. 110](https://home.agh.edu.pl/~czapli/Resnick_2.pdf#page=126) — PDF z serwera AGH

← [Wahadło matematyczne, fizyczne i torsyjne](03-wahadla.md) · [spis modułu](README.md) · [Drgania wymuszone i rezonans](05-drgania-wymuszone-i-rezonans.md) →

## Po co to jest

Prawdziwe drgania zanikają: huśtawka bez popychania się zatrzymuje, struna gitary cichnie. Tłumienie decyduje o tym, jak szybko — i jest celowo dobierane w amortyzatorach samochodów, wskazówkach mierników, budynkach w strefach sejsmicznych i głośnikach. Równanie oscylatora tłumionego to najważniejsze równanie różniczkowe drugiego rzędu w fizyce i technice: ma identyczną postać jak równanie obwodu RLC (15.05) i układu regulacji.

## Teoria w pigułce

**Model.** Na ciężarek na sprężynie działa dodatkowo siła oporu proporcjonalna do prędkości, $F = -b\dot x$ (opór lepki, 03.05):

$$m\ddot x + b\dot x + kx = 0 \quad\Rightarrow\quad \ddot x + 2\beta\dot x + \omega_0^2x = 0,$$

gdzie $\omega_0 = \sqrt{k/m}$ — częstość drgań nietłumionych, $\beta = b/(2m)$ — **współczynnik tłumienia**.

**Trzy przypadki** (szukamy rozwiązań $e^{\lambda t}$: $\lambda^2 + 2\beta\lambda + \omega_0^2 = 0$, $\lambda = -\beta \pm\sqrt{\beta^2 - \omega_0^2}$):

1. **Tłumienie słabe** ($\beta < \omega_0$) — drgania o malejącej amplitudzie:
   $$x(t) = A_0e^{-\beta t}\cos(\omega_dt + \varphi), \qquad \omega_d = \sqrt{\omega_0^2 - \beta^2}.$$
2. **Tłumienie krytyczne** ($\beta = \omega_0$) — najszybszy powrót do równowagi bez przeskoczenia: $x = (C_1 + C_2t)e^{-\beta t}$. Tak projektuje się amortyzatory i wskazówki mierników.
3. **Tłumienie nadkrytyczne** ($\beta > \omega_0$) — powolne pełzanie do równowagi bez drgań (drzwi z mocnym samozamykaczem).

**Miary tłumienia.**
- Amplituda maleje $e$-krotnie po czasie $\tau = 1/\beta$; energia — po czasie $1/(2\beta)$ (bo $E \propto A^2$).
- **Dekrement logarytmiczny** $\delta = \ln\dfrac{A_n}{A_{n+1}} = \beta T_d$ — logarytm stosunku kolejnych amplitud.
- **Dobroć** $Q = \dfrac{\omega_0}{2\beta}$ — ok. $2\pi$ razy energia zgromadzona przez energię traconą w jednym okresie; w przybliżeniu liczba drgań (razy $\pi$) do zaniku amplitudy $e$-krotnie. Kamerton: $Q \sim 10^3$–$10^4$; kwarc w zegarku: $Q \sim 10^5$; amortyzator samochodu: $Q \approx 0{,}5$.

## Wzory i założenia

| Wzór | Znaczenie | Kiedy obowiązuje |
|---|---|---|
| $\ddot x + 2\beta\dot x + \omega_0^2x = 0$ | równanie oscylatora tłumionego | opór $\propto v$ |
| $x = A_0e^{-\beta t}\cos(\omega_dt + \varphi)$ | słabe tłumienie | $\beta < \omega_0$ |
| $\omega_d = \sqrt{\omega_0^2 - \beta^2}$ | częstość drgań tłumionych | j.w. |
| $b_{\text{kr}} = 2\sqrt{km}$ | tłumienie krytyczne | $\beta = \omega_0$ |
| $E(t) = E_0e^{-2\beta t}$ | zanik energii | słabe tłumienie |
| $\delta = \beta T_d$, $\ Q = \omega_0/(2\beta) \approx \pi/\delta$ | dekrement, dobroć | $Q \gg 1$ |

## Przykład rozwiązany

### Wersja z rachunkiem różniczkowym i całkowym

**Zadanie.** Ciężarek o masie 0,5 kg na sprężynie o współczynniku 200 N/m jest tłumiony siłą $-b\dot x$, $b = 0{,}5\ \mathrm{kg/s}$. Oblicz $\omega_0$, $\beta$, $\omega_d$, czas, po którym amplituda zmaleje o połowę, oraz dobroć.

- $\omega_0 = 20\ \mathrm{rad/s}$, $\beta = 0{,}5/(2\cdot0{,}5) = 0{,}5\ \mathrm{s^{-1}}$ — tłumienie słabe.
- $\omega_d = \sqrt{400 - 0{,}25} \approx 19{,}994\ \mathrm{rad/s}$ — praktycznie bez zmian.
- Połowa amplitudy: $e^{-\beta t} = \tfrac12 \Rightarrow t = \ln2/\beta \approx 1{,}39\ \mathrm{s}$ (ok. 4,4 okresu).
- $Q = 20/(2\cdot0{,}5) = 20$.

**Sprawdzenie rozwiązania.** Wstawiając $x = e^{\lambda t}$: $\lambda^2 + \lambda + 400 = 0$, $\lambda = -0{,}5 \pm i\,19{,}994$ — część rzeczywista daje zanik, urojona — drgania.

**Jakie $b$ daje tłumienie krytyczne?** $b_{\text{kr}} = 2\sqrt{km} = 2\sqrt{100} = 20\ \mathrm{kg/s}$ — 40 razy więcej.

## Typowe pułapki

- **Częstość drgań tłumionych równa $\omega_0$.** Jest mniejsza: $\omega_d < \omega_0$ (przy słabym tłumieniu różnica jest minimalna).
- **Energia maleje tak jak amplituda.** Energia maleje dwa razy szybciej w wykładniku ($E \propto A^2$).
- **Krytyczne tłumienie = najwolniejszy powrót.** Odwrotnie — najszybszy bez przeskoczenia; nadkrytyczne jest wolniejsze.
- **Amplituda maleje liniowo.** Przy oporze lepkim — wykładniczo. (Przy tarciu suchym maleje liniowo — inny model.)

## Doświadczenie / symulacja

**Zanik drgań wahadła.** Zawieś telefon na sznurku i zmierz w phyphox (żyroskop) prędkość kątową przez kilka minut. Odczytaj kolejne maksima, narysuj $\ln\omega_{\max}$ od czasu — nachylenie to $-\beta$. Powtórz z przyczepioną do telefonu kartką papieru (większy opór powietrza) i porównaj dobroć.

**Python:** trzy rodzaje tłumienia i wyznaczenie $\beta$ z dopasowania obwiedni.

```python
import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp

m, k = 0.5, 200.0
w0 = np.sqrt(k/m)
t = np.linspace(0, 3, 3000)
for b, lab in [(0.5, "słabe (b = 0,5)"), (20.0, "krytyczne (b = 20)"), (60.0, "nadkrytyczne (b = 60)")]:
    sol = solve_ivp(lambda t, s: [s[1], -(b*s[1] + k*s[0])/m], (0, 3), [0.05, 0], t_eval=t, rtol=1e-9)
    plt.plot(t, sol.y[0]*100, label=lab)
    if b == 0.5:
        x = sol.y[0]
        i = np.where((x[1:-1] > x[:-2]) & (x[1:-1] > x[2:]))[0] + 1     # maksima
        beta_fit = -np.polyfit(t[i], np.log(x[i]), 1)[0]
        print(f"β z dopasowania = {beta_fit:.3f} 1/s (teoria b/2m = {b/(2*m):.3f}), Q = {w0/(2*beta_fit):.1f}")
plt.xlabel("t [s]"); plt.ylabel("x [cm]"); plt.grid(True); plt.legend(); plt.show()
```

## Zadania

### A. Poziom maturalny _(opcjonalnie — rozgrzewka)_

1. Do czego służą amortyzatory w samochodzie? Co by się działo bez nich?

<details>
<summary>Odpowiedź</summary>

Tłumią drgania nadwozia na sprężynach zawieszenia. Bez nich samochód po każdej nierówności długo by się kołysał, a koła traciłyby kontakt z drogą.
</details>

2. Amplituda drgań huśtawki maleje o 10% w każdym okresie. Jaka część amplitudy zostanie po 10 okresach?

<details>
<summary>Odpowiedź</summary>

$0{,}9^{10} \approx 0{,}35$ — ok. 35%.
</details>

### B. Poziom akademicki

1. Amplituda maleje o 10% na okres. Oblicz dekrement logarytmiczny i dobroć.

<details>
<summary>Odpowiedź</summary>

$\delta = \ln(1/0{,}9) \approx 0{,}105$; $Q \approx \pi/\delta \approx 30$.
</details>

2. Samochód z przykładu 09.01 ($m = 1500\ \mathrm{kg}$, $k = 98\,100\ \mathrm{N/m}$) ma amortyzatory dające tłumienie krytyczne. Jaki jest łączny współczynnik $b$?

<details>
<summary>Odpowiedź</summary>

$b = 2\sqrt{km} \approx 2{,}4\cdot10^4\ \mathrm{kg/s}$.
</details>

3. Amplituda wahadła maleje o połowę po 50 wahnięciach. Oblicz dobroć.

<details>
<summary>Odpowiedź</summary>

$e^{-\beta\cdot50T} = \tfrac12 \Rightarrow \beta T = \ln2/50$; $Q = \pi/(\beta T) \approx 227$.
</details>

4. Pokaż, że dla $\beta = \omega_0$ funkcja $x = te^{-\beta t}$ spełnia równanie oscylatora tłumionego.

<details>
<summary>Odpowiedź</summary>

$\dot x = (1 - \beta t)e^{-\beta t}$, $\ddot x = (\beta^2t - 2\beta)e^{-\beta t}$; $\ddot x + 2\beta\dot x + \beta^2x = (\beta^2t - 2\beta + 2\beta - 2\beta^2t + \beta^2t)e^{-\beta t} = 0$.
</details>

5. Pokaż, że moc tracona na tłumienie wynosi $b\dot x^2$, i oblicz jej średnią wartość w okresie przy słabym tłumieniu, wyrażając ją przez energię. Co to mówi o $Q$?

<details>
<summary>Odpowiedź</summary>

$\dfrac{dE}{dt} = \dot x(m\ddot x + kx) = -b\dot x^2$; średnio $b\overline{\dot x^2} = b\cdot E/m = 2\beta E$. Energia tracona w okresie $2\beta ET$, więc $\dfrac{E}{\Delta E} = \dfrac{1}{2\beta T} = \dfrac{Q}{2\pi}$.
</details>

## Źródła

- OpenStax, *Fizyka dla szkół wyższych*, t. 1, rozdz. 15 — §15.5: drgania tłumione.
- Halliday, Resnick, Walker, *Podstawy fizyki* — wyd. 2015: t. 2, §15.5; wyd. 1: t. 2, §16.8.
