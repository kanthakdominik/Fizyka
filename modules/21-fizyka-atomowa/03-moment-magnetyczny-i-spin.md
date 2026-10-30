# 21.03 — Orbitalny moment magnetyczny i spin elektronu

> **Moduł:** [21 — Fizyka atomowa](README.md) · **Poziom:** 🔵 studia · **Status:** ✅ pełny
>
> **Czytaj:**
>
> - OpenStax, *Fizyka dla szkół wyższych*, t. 3, rozdz. 8: [§8.2–8.3](https://openstax.org/books/fizyka-dla-szk%C3%B3%C5%82-wy%C5%BCszych-tom-3/pages/8-2-orbitalny-magnetyczny-moment-dipolowy-elektronu) · [wstęp do rozdziału](https://openstax.org/books/fizyka-dla-szk%C3%B3%C5%82-wy%C5%BCszych-tom-3/pages/8-wstep)
> - Halliday, Resnick, Walker, *Podstawy fizyki*, wyd. 2015, t. 5: §40.1–40.3 (s. 87)
> - Halliday, Resnick, Walker, *Podstawy fizyki*, wyd. 1 (2003), t. 5: [§41.3–41.6, s. 70](https://home.agh.edu.pl/~czapli/Resnick_5.pdf#page=86) — PDF z serwera AGH

← [Atom wodoru w mechanice kwantowej, liczby kwantowe](02-atom-wodoru-kwantowo.md) · [spis modułu](README.md) · [Zakaz Pauliego i układ okresowy](04-zakaz-pauliego.md) →

## Po co to jest

Elektron w atomie to maleńki magnes, i to z dwóch powodów: z ruchu orbitalnego i z własnego, wewnętrznego momentu pędu, czyli spinu. Spin nie ma klasycznego odpowiednika, a jednak decyduje o ferromagnetyzmie (14.07), strukturze układu okresowego (zakaz Pauliego, 21.04), rozszczepieniu linii widmowych w polu magnetycznym, działaniu rezonansu magnetycznego w medycynie i chemii oraz o pamięciach spintronicznych w dyskach twardych. Doświadczenie Sterna–Gerlacha jest też najprostszym pokazem pomiaru kwantowego.

## Teoria w pigułce

**Orbitalny moment magnetyczny.** Krążący elektron to pętla z prądem (14.02), więc jego moment magnetyczny jest proporcjonalny do momentu pędu:

$$\vec\mu_L = -\frac{e}{2m_e}\vec L, \qquad \mu_{L,z} = -m_l\mu_B, \qquad \mu_B = \frac{e\hbar}{2m_e} \approx 9{,}27\cdot10^{-24}\ \mathrm{J/T}.$$

$\mu_B$ to **magneton Bohra** (14.07). Minus oznacza, że dla elektronu moment magnetyczny jest przeciwny do momentu pędu.

**Efekt Zeemana.** W polu $B$ energia stanu przesuwa się o $\Delta E = m_l\mu_BB$. Poziom o danym $l$ rozszczepia się na $2l + 1$ podpoziomów, a linie widmowe na kilka składowych. Przy $B = 1\ \mathrm T$ przesunięcie wynosi ok. $5{,}8\cdot10^{-5}\ \mathrm{eV}$. Z rozszczepienia linii w widmie Słońca mierzy się pole magnetyczne plam słonecznych.

**Doświadczenie Sterna–Gerlacha (1922).** Wiązka atomów srebra przechodzi przez niejednorodne pole magnetyczne, które odchyla magnesy zależnie od orientacji ich momentu. Klasycznie powinna rozmyć się w ciągłą smugę. Okazało się, że rozdziela się na **dwie** plamki. Atomy srebra mają $l = 0$, więc za to odpowiada coś innego niż ruch orbitalny.

**Spin.** Elektron ma wewnętrzny moment pędu (spin) o liczbie kwantowej $s = \tfrac12$:

$$S = \sqrt{s(s + 1)}\hbar = \frac{\sqrt3}{2}\hbar, \qquad S_z = m_s\hbar, \qquad m_s = \pm\tfrac12.$$

Spinowy moment magnetyczny jest prawie dwa razy większy, niż sugeruje stosunek orbitalny ($g \approx 2{,}0023$): $\mu_{s,z} \approx \mp\mu_B$. Spin nie oznacza dosłownie obrotu kulki. Elektron, o ile wiadomo, jest punktowy, a „obracająca się kula” musiałaby mieć powierzchnię szybszą od światła.

**Pełny opis stanu elektronu w atomie** to cztery liczby kwantowe: $n$, $l$, $m_l$, $m_s$.

**Rezonans magnetyczny.** W polu $B$ dwa stany spinu mają różną energię $\Delta E = g\mu B$. Foton o częstotliwości $f = \Delta E/h$ powoduje przejścia.
- Elektrony (EPR/ESR): ok. 28 GHz na tesla.
- Protony (NMR, MRI): moment magnetyczny protonu jest ok. 660 razy mniejszy, a częstotliwość wynosi 42,58 MHz na tesla, czyli 64 MHz w tomografie 1,5 T. Obraz MRI to mapa sygnału protonów (głównie z wody) w tkankach.

## Wzory i założenia

| Wzór | Znaczenie | Kiedy obowiązuje |
|---|---|---|
| $\mu_B = e\hbar/(2m_e) = 9{,}27\cdot10^{-24}\ \mathrm{J/T}$ | magneton Bohra | — |
| $\mu_{L,z} = -m_l\mu_B$ | orbitalny moment magnetyczny | — |
| $\Delta E = m_l\mu_BB$ | normalny efekt Zeemana | słabe pole, bez spinu |
| $S_z = \pm\hbar/2$, $\mu_{s,z} \approx \mp\mu_B$ | spin elektronu | $g \approx 2$ |
| $hf = g\mu_BB$ | rezonans spinowy elektronu | — |
| $f = 42{,}58\ \mathrm{MHz/T}\cdot B$ | NMR protonów | — |

## Przykład rozwiązany

**Zadanie 1.** Oblicz rozszczepienie zeemanowskie poziomu $l = 1$ w polu 1 T. O ile zmienia się długość fali linii 656 nm dla przejścia z $\Delta m_l = 1$?

Podpoziomy: $m_l = -1, 0, +1$, odstęp $\mu_BB \approx 5{,}8\cdot10^{-5}\ \mathrm{eV}$.

$\Delta\lambda = \lambda\Delta E/E = 656\ \mathrm{nm}\cdot5{,}8\cdot10^{-5}/1{,}89 \approx 0{,}02\ \mathrm{nm}$. Do pomiaru potrzebny jest spektrometr o dużej rozdzielczości (siatka z $R \sim 10^5$, 18.03).

**Zadanie 2.** Jakiej częstotliwości trzeba użyć w spektrometrze EPR przy polu 0,336 T? A w tomografie MRI 3 T?

EPR: $f = 2\mu_BB/h \approx 9{,}4\ \mathrm{GHz}$ (mikrofale, pasmo X). MRI: $42{,}58\cdot3 \approx 128\ \mathrm{MHz}$ (fale radiowe).

### Wersja z rachunkiem różniczkowym i całkowym

**Siła na moment magnetyczny w polu niejednorodnym.** Energia $U = -\mu_zB_z$, więc siła $F_z = -\dfrac{dU}{dz} = \mu_z\dfrac{dB_z}{dz}$. Atom srebra ($\mu_z = \pm\mu_B$) w polu o gradiencie 1000 T/m doznaje siły $\pm9{,}3\cdot10^{-21}\ \mathrm N$. Atom ma masę $1{,}8\cdot10^{-25}\ \mathrm{kg}$ i prędkość ok. 500 m/s. Na drodze 3,5 cm (czas 70 μs) odchyli się o

$$z = \frac12\frac Fmt^2 \approx \frac12\cdot5{,}2\cdot10^4\cdot(7\cdot10^{-5})^2 \approx 0{,}13\ \mathrm{mm}.$$

Dwie plamki są odległe o ok. 0,25 mm, co Stern i Gerlach zobaczyli pod mikroskopem.

## Typowe pułapki

- **Spin to obrót elektronu.** To wewnętrzna, kwantowa własność, bez klasycznego odpowiednika.
- **$S = \hbar/2$.** Wartość spinu to $\tfrac{\sqrt3}{2}\hbar$. $\hbar/2$ to rzut na oś.
- **Moment magnetyczny elektronu równoległy do spinu.** Ładunek elektronu jest ujemny, więc moment jest przeciwny do spinu.
- **Rezonans MRI dotyczy elektronów.** MRI wykorzystuje spin jąder wodoru (protonów).

## Doświadczenie / symulacja

**Symulacja doświadczenia Sterna–Gerlacha.** Interaktywne symulacje (np. *Stern-Gerlach* z projektu QuVis, Uniwersytet St Andrews) pozwalają ustawić kilka magnesów pod różnymi kątami i zobaczyć, jak pomiar spinu w jednym kierunku „kasuje” informację o innym.

**Magnetometr protonowy.** W niektórych pracowniach jest prosty spektrometr NMR w polu ziemskim (ok. 2 kHz). Sygnał można usłyszeć przez wzmacniacz.

**Python:** rozszczepienie zeemanowskie i częstotliwości rezonansowe w funkcji pola.

```python
import numpy as np
import matplotlib.pyplot as plt

h, e, me = 6.62607015e-34, 1.602176634e-19, 9.1093837e-31
hbar = h/(2*np.pi)
muB = e*hbar/(2*me)
B = np.linspace(0, 2, 100)
for ml in (-1, 0, 1):
    plt.plot(B, ml*muB*B/e*1e6, label=f"m_l = {ml:+d}")
print(f"μ_B = {muB:.4e} J/T, rozszczepienie przy 1 T: {muB/e*1e6:.1f} µeV")
print(f"przesunięcie Hα przy 1 T: {656.3*muB/(1.89*e):.4f} nm")
print(f"EPR przy 0,336 T: {2.0023*muB*0.336/h/1e9:.2f} GHz; MRI 1,5 T: {42.577*1.5:.1f} MHz; 3 T: {42.577*3:.1f} MHz")
m_ag, v, L, grad = 1.79e-25, 500.0, 0.035, 1000.0
t = L/v
print(f"Stern–Gerlach: odchylenie {0.5*muB*grad/m_ag*t**2*1e3:.3f} mm")
plt.xlabel("B [T]"); plt.ylabel("ΔE [µeV]"); plt.legend(); plt.grid(True); plt.show()
```

## Zadania

### A. Poziom maturalny _(opcjonalnie — rozgrzewka)_

1. Na ile podpoziomów rozszczepia się w polu magnetycznym poziom $l = 2$ (bez spinu)?

<details>
<summary>Odpowiedź</summary>

$2l + 1 = 5$.
</details>

2. Jakie wartości przyjmuje rzut spinu elektronu na oś $z$?

<details>
<summary>Odpowiedź</summary>

$+\hbar/2$ i $-\hbar/2$.
</details>

### B. Poziom akademicki

1. Pokaż, że dla elektronu krążącego po orbicie kołowej $\mu = \dfrac{e}{2m}L$ (14.07, zadanie B2), i oblicz $\mu$ dla $L = \hbar$.

<details>
<summary>Odpowiedź</summary>

$I = ev/(2\pi r)$, $\mu = I\pi r^2 = evr/2 = eL/(2m)$. Dla $L = \hbar$: $\mu = \mu_B$.
</details>

2. Wiązka atomów wodoru w stanie podstawowym ($l = 0$) przechodzi przez magnes Sterna–Gerlacha. Na ile wiązek się rozdzieli? A wiązka atomów w stanie 2p, gdyby nie było spinu?

<details>
<summary>Odpowiedź</summary>

W stanie podstawowym na 2 (spin). Bez spinu stan 2p dałby 3 wiązki ($m_l = -1, 0, 1$). Ze spinem rozkład jest bardziej złożony (struktura subtelna).
</details>

3. Gdyby elektron był kulką o promieniu $10^{-18}\ \mathrm m$ (górna granica z doświadczeń) i masie jednorodnie rozłożonej, z jaką prędkością musiałby się obracać jego równik, żeby moment pędu wynosił $\hbar/2$?

<details>
<summary>Odpowiedź</summary>

$\tfrac25mr^2\omega = \hbar/2 \Rightarrow v = \omega r = \dfrac{5\hbar}{4mr} \approx 1{,}4\cdot10^{17}\ \mathrm{m/s}$, setki milionów razy szybciej niż światło. Spin nie jest obrotem w sensie klasycznym.
</details>

## Źródła

- OpenStax, *Fizyka dla szkół wyższych*, t. 3, rozdz. 8 — §8.2 (orbitalny moment magnetyczny) i §8.3 (spin elektronu).
- Halliday, Resnick, Walker, *Podstawy fizyki* — wyd. 2015: t. 5, §40.1–40.3; wyd. 1: t. 5, §41.3–41.6.
