# 01.01 — Układ SI i stałe definicyjne

> **Moduł:** [01 — Pomiar, jednostki i niepewności](README.md) · **Poziom:** 🟢🔵 matura R + studia · **Status:** ✅ pełny
>
> **Czytaj:**
>
> - OpenStax, *Fizyka dla szkół wyższych*, t. 1, rozdz. 1: [§1.1–1.3](https://openstax.org/books/fizyka-dla-szk%C3%B3%C5%82-wy%C5%BCszych-tom-1/pages/1-1-zakres-stosowalnosci-praw-fizyki) · [wstęp do rozdziału](https://openstax.org/books/fizyka-dla-szk%C3%B3%C5%82-wy%C5%BCszych-tom-1/pages/1-wstep)
> - Halliday, Resnick, Walker, *Podstawy fizyki*, wyd. 2015, t. 1: §1.1–1.3 (s. 1)
> - Halliday, Resnick, Walker, *Podstawy fizyki*, wyd. 1 (2003): [t. 1, rozdz. 1](https://home.agh.edu.pl/~czapli/Resnick_1.pdf) — PDF z serwera AGH

← (początek modułu) · [spis modułu](README.md) · [Analiza wymiarowa i szacowanie rzędu wielkości](02-analiza-wymiarowa-i-szacowanie.md) →

## Po co to jest

Wynik bez jednostki nie ma znaczenia, a wynik w złej jednostce bywa groźny — sonda Mars Climate Orbiter rozbiła się w 1999 roku, bo jeden zespół liczył w funtach-siłach, a drugi w niutonach. Sprawne przeliczanie jednostek i przedrostków to podstawa każdego zadania maturalnego, a sprawdzanie jednostek wyniku to najtańszy sposób wyłapania błędu w rachunkach.

## Teoria w pigułce

**Układ SI** ma siedem jednostek podstawowych:

| Wielkość | Jednostka | Symbol |
|---|---|---|
| czas | sekunda | s |
| długość | metr | m |
| masa | kilogram | kg |
| natężenie prądu | amper | A |
| temperatura termodynamiczna | kelwin | K |
| liczność materii | mol | mol |
| światłość | kandela | cd |

**Definicje od 2019 roku.** Wszystkie jednostki SI są zdefiniowane przez ustalenie dokładnych wartości siedmiu stałych przyrody — m.in. prędkości światła $c = 299\,792\,458\ \mathrm{m/s}$, stałej Plancka $h = 6{,}626\,070\,15\cdot10^{-34}\ \mathrm{J\cdot s}$, ładunku elementarnego $e = 1{,}602\,176\,634\cdot10^{-19}\ \mathrm{C}$, stałej Boltzmanna $k = 1{,}380\,649\cdot10^{-23}\ \mathrm{J/K}$ i stałej Avogadra $N_A = 6{,}022\,140\,76\cdot10^{23}\ \mathrm{mol^{-1}}$. Sekundę wyznacza częstotliwość przejścia w atomie cezu, metr — droga światła w próżni w ustalonym czasie, kilogram — stała Plancka. Wcześniej kilogram był wzorcem — walcem przechowywanym pod Paryżem.

**Jednostki pochodne** powstają z podstawowych przez mnożenie i dzielenie. Każdą można rozpisać na jednostki podstawowe, co przydaje się do sprawdzania wzorów:

| Jednostka | Wielkość | W jednostkach podstawowych |
|---|---|---|
| N (niuton) | siła | $\mathrm{kg\cdot m\cdot s^{-2}}$ |
| J (dżul) | energia, praca | $\mathrm{N\cdot m} = \mathrm{kg\cdot m^2\cdot s^{-2}}$ |
| W (wat) | moc | $\mathrm{J/s} = \mathrm{kg\cdot m^2\cdot s^{-3}}$ |
| Pa (paskal) | ciśnienie | $\mathrm{N/m^2} = \mathrm{kg\cdot m^{-1}\cdot s^{-2}}$ |
| C (kulomb) | ładunek | $\mathrm{A\cdot s}$ |
| V (wolt) | napięcie | $\mathrm{W/A} = \mathrm{kg\cdot m^2\cdot s^{-3}\cdot A^{-1}}$ |
| Ω (om) | opór | $\mathrm{V/A}$ |
| Hz (herc) | częstotliwość | $\mathrm{s^{-1}}$ |

**Przedrostki** zmieniają jednostkę o potęgę dziesięciu:

| Przedrostek | Symbol | Mnożnik | | Przedrostek | Symbol | Mnożnik |
|---|---|---|---|---|---|---|
| giga | G | $10^{9}$ | | mili | m | $10^{-3}$ |
| mega | M | $10^{6}$ | | mikro | μ | $10^{-6}$ |
| kilo | k | $10^{3}$ | | nano | n | $10^{-9}$ |
| centy | c | $10^{-2}$ | | piko | p | $10^{-12}$ |

**Zapis naukowy:** liczba w postaci $a\cdot10^n$ z $1 \le a < 10$. Ułatwia rachunki i od razu pokazuje rząd wielkości.

## Wzory i założenia

| Reguła | Przykład | Uwagi |
|---|---|---|
| zamiana przez mnożenie przez „jedynkę” | $72\ \dfrac{\mathrm{km}}{\mathrm{h}}\cdot\dfrac{1000\ \mathrm{m}}{1\ \mathrm{km}}\cdot\dfrac{1\ \mathrm{h}}{3600\ \mathrm{s}} = 20\ \mathrm{m/s}$ | jednostki skracają się jak liczby |
| przedrostek przy jednostce w potędze | $1\ \mathrm{cm^2} = (10^{-2}\ \mathrm{m})^2 = 10^{-4}\ \mathrm{m^2}$ | potęga obejmuje też przedrostek |
| kilowatogodzina | $1\ \mathrm{kWh} = 3{,}6\cdot10^{6}\ \mathrm{J}$ | jednostka energii, nie mocy |
| temperatura | $T[\mathrm{K}] = t[^\circ\mathrm{C}] + 273{,}15$ | różnica 1 K = różnica $1\ ^\circ\mathrm{C}$ |
| obie strony równania mają tę samą jednostkę | $[x] = [v_0t] = [\tfrac12at^2] = \mathrm{m}$ | dodawać można tylko wielkości tej samej jednostki |

## Przykład rozwiązany

**Zadanie.** Pociąg jedzie z prędkością $144\ \mathrm{km/h}$. Hamuje z opóźnieniem $0{,}8\ \mathrm{m/s^2}$. Jaką drogę przejedzie do zatrzymania? Wynik podaj w metrach i kilometrach.

**Jednostki.** $144\ \mathrm{km/h} = 144/3{,}6\ \mathrm{m/s} = 40\ \mathrm{m/s}$.

**Rachunek.** $s = \dfrac{v^2}{2a} = \dfrac{40^2}{2\cdot0{,}8}\ \mathrm{m} = 1000\ \mathrm{m} = 1\ \mathrm{km}$.

**Sprawdzenie jednostek.** $\dfrac{(\mathrm{m/s})^2}{\mathrm{m/s^2}} = \dfrac{\mathrm{m^2/s^2}}{\mathrm{m/s^2}} = \mathrm{m}$. Gdyby wstawić prędkość w km/h, wyszłoby $12\,960$ jednostek bez sensu — błąd byłby widoczny w jednostce.

### Wersja z rachunkiem różniczkowym i całkowym

Pochodna i całka też mają jednostki: $\left[\dfrac{dx}{dt}\right] = \dfrac{[x]}{[t]}$, $\left[\int F\,dx\right] = [F]\cdot[x]$. Z tego wynika jednostka każdej stałej we wzorze.

**Zadanie.** W równaniu $m\dot{v} = mg - bv$ (spadek z oporem) jaką jednostkę ma $b$? A stała $\tau = m/b$?

$[m\dot{v}] = \mathrm{kg\cdot m/s^2} = \mathrm{N}$, więc $[bv] = \mathrm{N}$ i $[b] = \dfrac{\mathrm{N}}{\mathrm{m/s}} = \mathrm{kg/s}$. Wtedy $[\tau] = \dfrac{\mathrm{kg}}{\mathrm{kg/s}} = \mathrm{s}$ — stała czasowa ma jednostkę czasu, jak powinna.

## Typowe pułapki

- **Przedrostek w potędze.** $1\ \mathrm{mm^3} = 10^{-9}\ \mathrm{m^3}$, a nie $10^{-3}\ \mathrm{m^3}$.
- **Gram zamiast kilograma.** We wzorach SI masa jest w kilogramach. Energia kinetyczna kulki 5 g przy 2 m/s to 0,01 J, a nie 10 J.
- **kW a kWh.** Kilowat to moc, kilowatogodzina — energia.
- **Stopnie Celsjusza w prawach gazowych.** We wzorze $pV = nRT$ temperatura musi być w kelwinach.
- **Mylenie m (metr) i m (mili-).** $1\ \mathrm{ms}$ to milisekunda, a nie „metr razy sekunda” (to pisze się $\mathrm{m\cdot s}$).

## Doświadczenie / symulacja

**Grubość kartki.** Zmierz linijką grubość ryzy papieru (500 kartek) albo grubej książki i policz grubość jednej kartki. Wynik podaj w milimetrach, mikrometrach i metrach w zapisie naukowym. Dlaczego pomiar wielu kartek naraz jest dokładniejszy niż pomiar jednej? (Odpowiedź w temacie 03.)

**Python:** wartości stałych definicyjnych SI są dostępne w `scipy.constants`. Sprawdźmy przy okazji kilka przeliczeń.

```python
from scipy import constants as c

print(f"c   = {c.c} m/s")
print(f"h   = {c.h} J·s")
print(f"e   = {c.e} C")
print(f"k   = {c.k} J/K")
print(f"N_A = {c.N_A} 1/mol")

print("144 km/h =", 144 * c.kilo / c.hour, "m/s")
print("1 kWh    =", c.kilo * c.hour, "J")
print("1 rok świetlny =", f"{c.light_year:.4e}", "m")
# długość Comptona elektronu ħ/(m_e c) — sprawdzenie, że to długość
print("ħ/(m_e c) =", f"{c.hbar / (c.m_e * c.c):.4e}", "m")
```

## Zadania

### A. Poziom maturalny

1. Zamień $108\ \mathrm{km/h}$ na m/s oraz $15\ \mathrm{m/s}$ na km/h.

<details>
<summary>Odpowiedź</summary>

$30\ \mathrm{m/s}$; $54\ \mathrm{km/h}$.
</details>

2. Przekrój przewodu wynosi $2{,}5\ \mathrm{mm^2}$. Wyraź go w $\mathrm{m^2}$.

<details>
<summary>Odpowiedź</summary>

$2{,}5\cdot10^{-6}\ \mathrm{m^2}$.
</details>

3. Czajnik o mocy $2\ \mathrm{kW}$ pracuje przez 3 minuty. Ile energii pobiera — w dżulach i w kWh?

<details>
<summary>Odpowiedź</summary>

$2000\cdot180 = 3{,}6\cdot10^{5}\ \mathrm{J} = 0{,}1\ \mathrm{kWh}$.
</details>

4. Wyraź wolt w jednostkach podstawowych SI.

<details>
<summary>Odpowiedź</summary>

$\mathrm{V} = \mathrm{W/A} = \mathrm{kg\cdot m^2\cdot s^{-3}\cdot A^{-1}}$.
</details>

5. Gęstość wody wynosi $1\ \mathrm{g/cm^3}$. Ile to w $\mathrm{kg/m^3}$? Jaka jest masa $1\ \mathrm{L}$ wody?

<details>
<summary>Odpowiedź</summary>

$1000\ \mathrm{kg/m^3}$; $1\ \mathrm{kg}$ ($1\ \mathrm{L} = 10^{-3}\ \mathrm{m^3}$).
</details>

### B. Poziom akademicki

1. Z prawa grawitacji $F = G\dfrac{m_1m_2}{r^2}$ wyznacz jednostkę $G$ w jednostkach podstawowych.

<details>
<summary>Odpowiedź</summary>

$\mathrm{N\cdot m^2/kg^2} = \mathrm{m^3\cdot kg^{-1}\cdot s^{-2}}$.
</details>

2. Z prawa Coulomba $F = \dfrac{1}{4\pi\varepsilon_0}\dfrac{q^2}{r^2}$ wyznacz jednostkę $\varepsilon_0$ w jednostkach podstawowych.

<details>
<summary>Odpowiedź</summary>

$\mathrm{C^2/(N\cdot m^2)} = \mathrm{A^2\cdot s^4\cdot kg^{-1}\cdot m^{-3}}$.
</details>

3. Wychylenie tłumionego oscylatora opisuje $x(t) = Ae^{-\beta t}\sin(\omega t)$, gdzie $x$ jest w metrach. Jakie jednostki mają $A$, $\beta$ i $\omega$? Dlaczego?

<details>
<summary>Odpowiedź</summary>

$A$ — metr; $\beta$ i $\omega$ — $\mathrm{s^{-1}}$ (ω zwykle jako rad/s), bo argumenty funkcji wykładniczej i sinusa muszą być bezwymiarowe.
</details>

4. Pokaż, że $\hbar/(mc)$ ma wymiar długości, i oblicz tę wielkość dla elektronu ($\hbar = 1{,}055\cdot10^{-34}\ \mathrm{J\cdot s}$, $m_e = 9{,}11\cdot10^{-31}\ \mathrm{kg}$).

<details>
<summary>Odpowiedź</summary>

$\dfrac{\mathrm{kg\cdot m^2\cdot s^{-1}}}{\mathrm{kg\cdot m\cdot s^{-1}}} = \mathrm{m}$; $\approx 3{,}86\cdot10^{-13}\ \mathrm{m}$ (zredukowana długość fali Comptona).
</details>

5. Ile metrów ma rok świetlny? Przyjmij rok $= 365{,}25$ doby.

<details>
<summary>Odpowiedź</summary>

$c\cdot365{,}25\cdot86\,400\ \mathrm{s} \approx 9{,}46\cdot10^{15}\ \mathrm{m}$.
</details>

## Źródła

- OpenStax, *Fizyka dla szkół wyższych*, t. 1, rozdz. 1 — §1.2 (układy jednostek) i §1.3 (przeliczanie jednostek), z tabelami przedrostków.
- Halliday, Resnick, Walker, *Podstawy fizyki*, wyd. 2015, t. 1, rozdz. 1 — §1.1–1.3: pomiar długości, czasu i masy; dodatki A i D (układ SI, przeliczniki jednostek).
- [NIST — Fundamental Physical Constants](https://physics.nist.gov/cuu/Constants/) _(po angielsku)_ — aktualne wartości stałych.
