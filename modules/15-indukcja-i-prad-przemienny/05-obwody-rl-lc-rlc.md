# 15.05 — Obwody RL, LC i RLC — drgania elektromagnetyczne

> **Moduł:** [15 — Indukcja elektromagnetyczna i prąd przemienny](README.md) · **Poziom:** 🔵 studia · **Status:** ✅ pełny
>
> **Czytaj:**
>
> - OpenStax, *Fizyka dla szkół wyższych*, t. 2, rozdz. 14: [§14.4–14.6](https://openstax.org/books/fizyka-dla-szk%C3%B3%C5%82-wy%C5%BCszych-tom-2/pages/14-4-obwody-rl) · [wstęp do rozdziału](https://openstax.org/books/fizyka-dla-szk%C3%B3%C5%82-wy%C5%BCszych-tom-2/pages/14-wstep)
> - Halliday, Resnick, Walker, *Podstawy fizyki*, wyd. 2015, t. 3: §30.6 (s. 352), §31.1–31.2 (s. 378)
> - Halliday, Resnick, Walker, *Podstawy fizyki*, wyd. 1 (2003), t. 3: §31.9, s. 267, §33.1–33.5, s. 320 (skan t. 3 na serwerze AGH kończy się na s. 127 — dalsze strony tylko w wydaniu papierowym)

← [Indukcyjność własna i wzajemna, energia pola magnetycznego](04-indukcyjnosc.md) · [spis modułu](README.md) · [Prąd przemienny: wartości skuteczne, impedancja, rezonans, moc](06-prad-przemienny.md) →

## Po co to jest

Cewka z kondensatorem tworzy elektryczne wahadło: energia przelewa się między polem elektrycznym a magnetycznym, a prąd drga z częstotliwością $1/(2\pi\sqrt{LC})$. Taki obwód LC dostraja radio do stacji, wytwarza sygnał zegarowy w nadajnikach i jest podstawą filtrów. Obwód RL opisuje opóźnienie narastania prądu w cewkach, przekaźnikach i silnikach. Wszystkie trzy obwody opisuje to samo równanie co oscylator mechaniczny z modułu 09, więc wiedza o drganiach przenosi się tu bez zmian.

## Teoria w pigułce

**Obwód RL.** Po włączeniu źródła $\varepsilon$ prąd nie skacze od razu do $\varepsilon/R$, bo cewka sprzeciwia się zmianie:

$$\varepsilon - L\frac{dI}{dt} - IR = 0 \Rightarrow I(t) = \frac\varepsilon R\left(1 - e^{-t/\tau}\right), \qquad \tau = \frac LR.$$

Po odłączeniu źródła (i zwarciu cewki przez opornik) prąd zanika jak $I_0e^{-t/\tau}$. To lustrzane odbicie obwodu RC (13.06): tam napięcie na kondensatorze nie może skoczyć, tu prąd w cewce.

**Obwód LC.** Naładowany kondensator połączony z cewką:

$$L\frac{d^2q}{dt^2} + \frac qC = 0 \Rightarrow q = Q_0\cos(\omega_0t + \varphi), \qquad \omega_0 = \frac{1}{\sqrt{LC}}.$$

Energia przelewa się między kondensatorem ($q^2/2C$) a cewką ($\tfrac12LI^2$), a suma jest stała.

**Analogia z drganiami mechanicznymi (09):**

| Mechanika | Obwód |
|---|---|
| wychylenie $x$ | ładunek $q$ |
| prędkość $v$ | prąd $I$ |
| masa $m$ | indukcyjność $L$ |
| sztywność $k$ | $1/C$ |
| tłumienie $b$ | opór $R$ |
| $\tfrac12mv^2$, $\tfrac12kx^2$ | $\tfrac12LI^2$, $q^2/(2C)$ |

**Obwód RLC** to oscylator tłumiony (09.04):

$$L\ddot q + R\dot q + \frac qC = 0, \qquad \beta = \frac{R}{2L}, \qquad \omega_d = \sqrt{\omega_0^2 - \beta^2}.$$

Tłumienie słabe daje gasnące drgania, krytyczne zachodzi dla $R = 2\sqrt{L/C}$. Dobroć: $Q = \dfrac{\omega_0L}{R} = \dfrac1R\sqrt{\dfrac LC}$.

## Wzory i założenia

| Wzór | Znaczenie | Kiedy obowiązuje |
|---|---|---|
| $\tau = L/R$ | stała czasowa RL | — |
| $I = (\varepsilon/R)(1 - e^{-t/\tau})$ | narastanie prądu | włączenie źródła |
| $\omega_0 = 1/\sqrt{LC}$, $f_0 = 1/(2\pi\sqrt{LC})$ | częstość własna LC | bez strat |
| $\beta = R/(2L)$, $\omega_d = \sqrt{\omega_0^2 - \beta^2}$ | RLC | słabe tłumienie |
| $R_{\text{kr}} = 2\sqrt{L/C}$ | tłumienie krytyczne | — |
| $Q = \omega_0L/R$ | dobroć | — |

## Przykład rozwiązany

### Wersja z rachunkiem różniczkowym i całkowym

**Zadanie.** Obwód zawiera cewkę 10 mH, kondensator 1 μF i opornik 10 Ω.
1. Oblicz stałą czasową RL (sama cewka z opornikiem).
2. Oblicz częstotliwość drgań LC.
3. Oblicz współczynnik tłumienia, dobroć i opór krytyczny.
4. Kondensator naładowano do 10 V. Oblicz największy prąd i czas, po którym amplituda spadnie o połowę.

1. $\tau = L/R = 1\ \mathrm{ms}$.
2. $\omega_0 = 1/\sqrt{10^{-2}\cdot10^{-6}} = 10^4\ \mathrm{rad/s}$, $f_0 \approx 1590\ \mathrm{Hz}$.
3. $\beta = R/(2L) = 500\ \mathrm{s^{-1}}$, $Q = \omega_0L/R = 10$, $R_{\text{kr}} = 2\sqrt{L/C} = 200\ \Omega$.
4. Bez strat z bilansu energii: $\tfrac12CU_0^2 = \tfrac12LI_{\max}^2 \Rightarrow I_{\max} = U_0\sqrt{C/L} = 0{,}1\ \mathrm A$. Z tłumieniem nieco mniej. Amplituda maleje jak $e^{-\beta t}$, połowa po $\ln2/\beta \approx 1{,}4\ \mathrm{ms}$, czyli ok. 2 okresach.

**Dostrajanie radia.** Odbiornik UKF ma cewkę 1 μH. Jaka pojemność dostroi go do 100 MHz? $C = \dfrac{1}{4\pi^2f^2L} \approx 2{,}5\ \mathrm{pF}$. Dla fal średnich (1 MHz) i cewki 100 μH: ok. 250 pF, typowy kondensator obrotowy dawnych radioodbiorników.

## Typowe pułapki

- **Cewka w chwili włączenia jak zwarcie.** Odwrotnie: cewka w chwili włączenia jest jak przerwa ($I = 0$), a po długim czasie jak zwarcie. Kondensator na odwrót.
- **Stała czasowa $LR$.** $\tau = L/R$, w odróżnieniu od $RC$.
- **Częstotliwość $1/\sqrt{LC}$.** To częstość kołowa $\omega_0$. Częstotliwość w hercach to $\omega_0/(2\pi)$.
- **Okres drgań energii = okres prądu.** Energia w kondensatorze ma maksimum dwa razy w okresie prądu.
- **Duży opór = szybsze drgania.** Opór tłumi drgania i nieco **zmniejsza** ich częstotliwość.

## Doświadczenie / symulacja

**Drgania LC na oscyloskopie.** Kondensator 1 μF i cewka ok. 10–100 mH (np. uzwojenie przekaźnika lub dławik). Naładuj kondensator z baterii, przełącz na cewkę i rejestruj napięcie oscyloskopem albo kartą dźwiękową (ostrożnie: wejście mikrofonowe przyjmuje tylko ułamki wolta, potrzebny dzielnik). Zmierz częstotliwość i tempo zaniku, wyznacz $L$ i $R$ cewki.

**Symulacja PhET:** *Zestaw do budowy obwodów AC* (*Circuit Construction Kit: AC*) — obwód LC z przełącznikiem i wykres prądu.

**Python:** obwód RLC numerycznie — porównanie ze wzorem i z oscylatorem mechanicznym.

```python
import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp

L, C, U0 = 10e-3, 1e-6, 10.0
w0 = 1/np.sqrt(L*C)
t = np.linspace(0, 6e-3, 3000)
for R in (10.0, 100.0, 200.0):
    sol = solve_ivp(lambda t, s: [s[1], -(R*s[1] + s[0]/C)/L], (0, t[-1]), [C*U0, 0], t_eval=t, max_step=1e-6)
    plt.plot(t*1e3, sol.y[0]/C, label=f"R = {R:.0f} Ω, Q = {w0*L/R:.1f}")
    print(f"R = {R:5.0f} Ω: |I|max = {np.abs(sol.y[1]).max()*1e3:.1f} mA")
beta = 10/(2*L)
print(f"f0 = {w0/(2*np.pi):.1f} Hz, β = {beta:.0f} 1/s, połowa amplitudy po {np.log(2)/beta*1e3:.2f} ms")
print(f"radio UKF: C = {1/(4*np.pi**2*100e6**2*1e-6)*1e12:.2f} pF")
plt.xlabel("t [ms]"); plt.ylabel("U_C [V]"); plt.grid(True); plt.legend(); plt.show()
```

## Zadania

### A. Poziom maturalny _(opcjonalnie — rozgrzewka)_

1. Oblicz częstotliwość drgań obwodu LC o $L = 2\ \mathrm{mH}$ i $C = 50\ \mathrm{nF}$.

<details>
<summary>Odpowiedź</summary>

$f = 1/(2\pi\sqrt{10^{-10}}) \approx 15{,}9\ \mathrm{kHz}$.
</details>

2. Jak zmieni się częstotliwość obwodu LC, gdy pojemność wzrośnie czterokrotnie?

<details>
<summary>Odpowiedź</summary>

Zmaleje dwukrotnie.
</details>

### B. Poziom akademicki

1. Pokaż, że w obwodzie LC energia całkowita $\dfrac{q^2}{2C} + \dfrac12LI^2$ jest stała, i oblicz $I_{\max}$ dla kondensatora 1 μF naładowanego do 10 V i cewki 10 mH.

<details>
<summary>Odpowiedź</summary>

$\dfrac{d}{dt}\left(\dfrac{q^2}{2C} + \dfrac12L\dot q^2\right) = \dot q\left(\dfrac qC + L\ddot q\right) = 0$. $I_{\max} = U_0\sqrt{C/L} = 0{,}1\ \mathrm A$.
</details>

2. Cewka 2 H o oporze 4 Ω jest podłączona do 12 V. Po jakim czasie prąd osiągnie 2 A? Ile energii zgromadzi cewka w stanie ustalonym?

<details>
<summary>Odpowiedź</summary>

$I_\infty = 3\ \mathrm A$, $\tau = 0{,}5\ \mathrm s$. $2 = 3(1 - e^{-t/\tau}) \Rightarrow t = \tau\ln3 \approx 0{,}55\ \mathrm s$. $W = \tfrac12\cdot2\cdot9 = 9\ \mathrm J$.
</details>

3. Wyprowadź równanie RLC z praw Kirchhoffa i wskaż odpowiedniki $m$, $b$, $k$. Dla jakiego $R$ obwód z przykładu jest tłumiony krytycznie i ile wynosi wtedy stała czasowa powrotu do zera?

<details>
<summary>Odpowiedź</summary>

$-L\ddot q - R\dot q - q/C = 0$; $m \to L$, $b \to R$, $k \to 1/C$. $R_{\text{kr}} = 2\sqrt{L/C} = 200\ \Omega$, $\beta = \omega_0 = 10^4\ \mathrm{s^{-1}}$, $q = (C_1 + C_2t)e^{-\beta t}$, czas charakterystyczny 0,1 ms.
</details>

4. Przez cewkę płynie prąd $I_0$. Źródło odłączono, a cewkę zwarto przez opornik $R$. Oblicz całkowite ciepło wydzielone w oporniku i pokaż, że jest równe energii cewki.

<details>
<summary>Odpowiedź</summary>

$I = I_0e^{-t/\tau}$, $Q = \displaystyle\int_0^\infty I_0^2e^{-2t/\tau}R\,dt = I_0^2R\frac\tau2 = \frac12LI_0^2$, bo $R\tau = L$.
</details>

## Źródła

- OpenStax, *Fizyka dla szkół wyższych*, t. 2, rozdz. 14 — §14.4 (obwody RL), §14.5 (drgania w obwodzie LC), §14.6 (obwody RLC).
- Halliday, Resnick, Walker, *Podstawy fizyki* — wyd. 2015: t. 3, §30.6, §31.1–31.2; wyd. 1: t. 3, §31.9, §33.1–33.5.
- Symulacja PhET *Zestaw do budowy obwodów AC*.
