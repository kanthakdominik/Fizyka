# 23.05 — Półprzewodniki, domieszkowanie i złącze p-n

> **Moduł:** [23 — Fizyka ciała stałego](README.md) · **Poziom:** 🔵 studia · **Status:** ✅ pełny
>
> **Czytaj:**
>
> - OpenStax, *Fizyka dla szkół wyższych*, t. 3, rozdz. 9: [§9.6–9.7](https://openstax.org/books/fizyka-dla-szk%C3%B3%C5%82-wy%C5%BCszych-tom-3/pages/9-6-polprzewodniki-i-domieszkowanie) · [wstęp do rozdziału](https://openstax.org/books/fizyka-dla-szk%C3%B3%C5%82-wy%C5%BCszych-tom-3/pages/9-wstep)
> - Halliday, Resnick, Walker, *Podstawy fizyki*, wyd. 2015, t. 5: §41.2–41.3 (s. 143)
> - Halliday, Resnick, Walker, *Podstawy fizyki*, wyd. 1 (2003), t. 5: [§42.6–42.11, s. 114](https://home.agh.edu.pl/~czapli/Resnick_5.pdf#page=130) — PDF z serwera AGH

← [Teoria pasmowa ciał stałych](04-teoria-pasmowa.md) · [spis modułu](README.md) · [Nadprzewodnictwo](06-nadprzewodnictwo.md) →

## Po co to jest

Prawie cała współczesna elektronika opiera się na półprzewodnikach: procesory (miliardy tranzystorów), pamięci, diody LED, lasery półprzewodnikowe, ogniwa słoneczne, czujniki obrazu w aparatach. Właściwości półprzewodnika można zmienić o wiele rzędów wielkości, dodając jeden obcy atom na kilka milionów (domieszkowanie). Złącze p-n to podstawowa „cegiełka”: przewodzi prąd w jedną stronę, świeci, zamienia światło na prąd. Ten temat łączy teorię pasmową (23.04) z obwodami (13).

## Teoria w pigułce

**Półprzewodnik samoistny.** Czysty krzem w 300 K ma ok. $10^{16}$ elektronów przewodnictwa w 1 m³ (i tyle samo dziur), czyli jeden nośnik na ok. 5 bilionów atomów. Przewodzi słabo (opór właściwy rzędu kΩ·m).

**Domieszkowanie.** Krzem ma 4 elektrony walencyjne.
- **Typ n**: domieszka z grupy 15 (P, As) ma 5 elektronów. Piąty jest związany bardzo słabo (ok. 0,045 eV dla P), więc w temperaturze pokojowej prawie każdy atom domieszki oddaje elektron do pasma przewodnictwa (**donor**). Nośniki większościowe to elektrony.
- **Typ p**: domieszka z grupy 13 (B, Al, Ga) ma 3 elektrony i łatwo przyjmuje elektron z pasma walencyjnego, tworząc dziurę (**akceptor**). Nośniki większościowe to dziury.

Poziomy donorów leżą tuż pod pasmem przewodnictwa, a akceptorów tuż nad pasmem walencyjnym. Domieszka $10^{22}\ \mathrm{m^{-3}}$ (jeden atom na 5 milionów) zwiększa koncentrację nośników milion razy. W równowadze obowiązuje **prawo działania mas** $np = n_i^2$, więc liczba nośników mniejszościowych spada.

**Złącze p-n.** Po zetknięciu obszarów p i n elektrony dyfundują do p, a dziury do n, gdzie rekombinują. Przy złączu powstaje **warstwa zubożona** bez swobodnych nośników, z nieskompensowanymi jonami domieszek: dodatnimi po stronie n, ujemnymi po stronie p. Ich pole elektryczne (bariera ok. 0,7 V w krzemie) zatrzymuje dalszą dyfuzję.
- **Polaryzacja w kierunku przewodzenia** (+ do p): bariera maleje i prąd rośnie wykładniczo.
- **W kierunku zaporowym**: bariera rośnie i płynie tylko mały prąd nasycenia $I_0$.

**Równanie diody (Shockleya):**

$$I = I_0\left(e^{eU/kT} - 1\right), \qquad \frac{kT}{e} \approx 25{,}9\ \mathrm{mV}\ (300\ \mathrm K).$$

Prąd rośnie 10 razy co ok. 60 mV, dlatego dioda krzemowa „otwiera się” przy ok. 0,6–0,7 V.

**Przyrządy:**
- **Dioda prostownicza** — prostowanie prądu przemiennego (15.06).
- **LED** — rekombinacja elektronu z dziurą w złączu emituje foton o energii $\approx E_g$. Barwę wybiera się przerwą: GaAs (podczerwień), AlGaInP (czerwona, ok. 1,9 eV), InGaN (niebieska, ok. 2,7 eV). Krzem świeci bardzo słabo, bo ma przerwę skośną (przejście wymaga udziału drgań sieci).
- **Fotodioda i ogniwo słoneczne** — odwrotny proces: foton $hf > E_g$ tworzy parę elektron–dziura, a pole złącza je rozdziela, dając prąd (20.02).
- **Tranzystor** (bipolarny n-p-n, polowy MOSFET) — mały sygnał steruje dużym prądem. MOSFET to kanał, którego przewodnictwo zmienia napięcie bramki. To podstawa układów cyfrowych.

**Efekt Halla** (14.03) pozwala zmierzyć znak i koncentrację nośników: $U_H = IB/(net)$. W półprzewodniku napięcie Halla jest milion razy większe niż w metalu, dlatego czujniki Halla robi się z półprzewodników.

## Wzory i założenia

| Wzór | Znaczenie | Kiedy obowiązuje |
|---|---|---|
| $np = n_i^2$ | prawo działania mas | równowaga termiczna |
| $n \approx N_D$ (typ n), $p \approx N_A$ (typ p) | nośniki większościowe | pełna jonizacja, $N \gg n_i$ |
| $\sigma = e(n\mu_e + p\mu_h)$ | przewodność | $\mu$ — ruchliwości |
| $I = I_0(e^{eU/kT} - 1)$ | charakterystyka diody | dioda idealna |
| $hf \approx E_g$, $\lambda \approx hc/E_g$ | foton z LED | przerwa prosta |
| $U_H = IB/(net)$ | napięcie Halla | jeden typ nośników |

## Przykład rozwiązany

### Wersja z rachunkiem różniczkowym i całkowym

**Zadanie 1.** Krzem ($n_i = 1{,}0\cdot10^{16}\ \mathrm{m^{-3}}$, $\mu_e = 0{,}135$, $\mu_h = 0{,}048\ \mathrm{m^2/(V\cdot s)}$) domieszkowano fosforem: $N_D = 10^{22}\ \mathrm{m^{-3}}$. Oblicz koncentrację dziur i opór właściwy przed domieszkowaniem i po nim.

Przed: $\sigma = n_ie(\mu_e + \mu_h) \approx 2{,}9\cdot10^{-4}\ \mathrm{S/m}$, $\rho \approx 3400\ \Omega\cdot\mathrm m$.

Po: $n \approx 10^{22}$, $p = n_i^2/n = 10^{10}\ \mathrm{m^{-3}}$, $\rho = 1/(ne\mu_e) \approx 0{,}0046\ \Omega\cdot\mathrm m$. Opór zmalał ok. 700 000 razy, a domieszka to tylko $2\cdot10^{-7}$ atomów krzemu.

**Zadanie 2.** Dioda ma $I_0 = 10^{-12}\ \mathrm A$. Oblicz prąd przy 0,5, 0,6 i 0,7 V w 300 K. Oblicz opór dynamiczny $r = dU/dI$ przy 10 mA.

$I(0{,}5) \approx 0{,}25\ \mathrm{mA}$, $I(0{,}6) \approx 12\ \mathrm{mA}$, $I(0{,}7) \approx 0{,}57\ \mathrm A$.

$\dfrac{dI}{dU} = \dfrac{e}{kT}I_0e^{eU/kT} \approx \dfrac{eI}{kT} \Rightarrow r = \dfrac{kT}{eI} = \dfrac{25{,}9\ \mathrm{mV}}{10\ \mathrm{mA}} \approx 2{,}6\ \Omega$.

**Zadanie 3.** Jakie przerwy energetyczne muszą mieć diody świecące na czerwono (650 nm) i niebiesko (460 nm)?

$E = 1239{,}8/\lambda[\mathrm{nm}]$: czerwona 1,91 eV, niebieska 2,70 eV. Napięcie przewodzenia diody jest bliskie $E_g/e$: czerwone ok. 2 V, niebieskie ok. 3 V.

## Typowe pułapki

- **Półprzewodnik typu n jest naładowany ujemnie.** Jest elektrycznie obojętny. Elektrony przewodnictwa równoważą dodatnie jony donorów.
- **Dziury to cząstki dodatnie płynące jak protony.** To brak elektronu w paśmie walencyjnym. Ruch dziury to ruch elektronów walencyjnych w przeciwną stronę.
- **W kierunku zaporowym nie płynie żaden prąd.** Płynie mały prąd $I_0$ (nośniki mniejszościowe). Silnie rośnie z temperaturą i przy dużym napięciu zachodzi przebicie (diody Zenera).
- **Więcej domieszki zawsze lepiej.** Przy bardzo dużym domieszkowaniu maleje ruchliwość, a półprzewodnik staje się zdegenerowany (zachowuje się prawie jak metal).

## Doświadczenie / symulacja

**Charakterystyka diody i LED.** Złóż obwód: zasilacz, opornik 1 kΩ, dioda. Zmierz napięcie i prąd dla kilkunastu punktów. Narysuj $\ln I$ od $U$: nachylenie daje $e/(\eta kT)$, gdzie $\eta$ (1–2) to współczynnik idealności. Dla LED w różnych kolorach zmierz napięcie progowe i porównaj z $hc/(e\lambda)$. Z tego da się wyznaczyć stałą Plancka.

**Symulacja PhET:** *Półprzewodniki* (*Semiconductors*, starsza symulacja Java, wersja angielska) — domieszkowanie i złącze p-n ([phet.colorado.edu/pl](https://phet.colorado.edu/pl/)).

**Python:** przewodność krzemu w funkcji domieszkowania, charakterystyka diody i wyznaczanie $h$ z napięć progowych LED.

```python
import numpy as np
import matplotlib.pyplot as plt

e, k, h, c = 1.602176634e-19, 1.380649e-23, 6.62607015e-34, 2.99792458e8
ni, mue, muh = 1.0e16, 0.135, 0.048
print(f"Si samoistny: ρ = {1/(ni*e*(mue + muh)):.0f} Ω·m")
for ND in (1e18, 1e20, 1e22, 1e24):
    n = ND/2 + np.sqrt((ND/2)**2 + ni**2); p = ni**2/n
    print(f"N_D = {ND:.0e} m⁻³: n = {n:.2e}, p = {p:.2e}, ρ = {1/(e*(n*mue + p*muh)):.2e} Ω·m")

VT = k*300/e; I0 = 1e-12
U = np.linspace(0, 0.75, 400)
I = I0*(np.exp(U/VT) - 1)
for u in (0.5, 0.6, 0.7):
    print(f"U = {u} V: I = {I0*(np.exp(u/VT) - 1):.2e} A")
print(f"opór dynamiczny przy 10 mA: {VT/0.01:.2f} Ω")

lam = np.array([940, 650, 590, 525, 460])*1e-9            # LED: IR, czerwona, żółta, zielona, niebieska
Uprog = np.array([1.25, 1.85, 2.0, 2.3, 2.6])             # przykładowe napięcia progowe [V]
a, b = np.polyfit(c/lam, Uprog, 1)
print(f"h z dopasowania U = (h/e)·f + b: {a*e:.2e} J·s (dokładnie {h:.3e})")
plt.plot(U, I*1e3); plt.ylim(0, 50); plt.xlabel("U [V]"); plt.ylabel("I [mA]"); plt.grid(True); plt.show()
```

## Zadania

### A. Poziom maturalny _(opcjonalnie — rozgrzewka)_

1. Jaką domieszką (bor czy arsen) trzeba domieszkować krzem, żeby uzyskać półprzewodnik typu p?

<details>
<summary>Odpowiedź</summary>

Borem (grupa 13, 3 elektrony walencyjne) — akceptor.
</details>

2. Ogniwo krzemowe ($E_g = 1{,}12\ \mathrm{eV}$). Jaka jest najdłuższa fala, którą może wykorzystać?

<details>
<summary>Odpowiedź</summary>

$\lambda = hc/E_g \approx 1{,}1\ \mu\mathrm m$ (bliska podczerwień).
</details>

3. Dlaczego dioda przewodzi prąd tylko w jedną stronę?

<details>
<summary>Odpowiedź</summary>

W kierunku przewodzenia zewnętrzne napięcie obniża barierę na złączu i nośniki większościowe mogą ją pokonać. W kierunku zaporowym bariera rośnie, a warstwa zubożona się poszerza.
</details>

### B. Poziom akademicki

1. Ile razy wzrośnie prąd diody przy wzroście napięcia o 0,1 V w 300 K?

<details>
<summary>Odpowiedź</summary>

$e^{0{,}1/0{,}02585} \approx 48$ razy.
</details>

2. Prąd nasycenia $I_0 \propto T^3e^{-E_g/kT}$. Ile razy wzrośnie dla krzemu przy ogrzaniu z 300 do 310 K?

<details>
<summary>Odpowiedź</summary>

$(310/300)^3\exp\left[\dfrac{E_g}{k}\left(\dfrac1{300} - \dfrac1{310}\right)\right] \approx 1{,}10\cdot e^{1{,}40} \approx 4{,}5$ razy. Dlatego elektronika musi kompensować zmiany temperatury.
</details>

3. Płytka krzemu typu n ($n = 10^{22}\ \mathrm{m^{-3}}$) o grubości 0,5 mm, prąd 1 mA, pole 0,5 T. Oblicz napięcie Halla i porównaj z miedzią ($n = 8{,}5\cdot10^{28}\ \mathrm{m^{-3}}$).

<details>
<summary>Odpowiedź</summary>

$U_H = \dfrac{IB}{net} = \dfrac{10^{-3}\cdot0{,}5}{10^{22}\cdot1{,}6\cdot10^{-19}\cdot5\cdot10^{-4}} \approx 0{,}62\ \mathrm{mV}$. Miedź: ok. $7\cdot10^{-11}$ V, prawie 10 milionów razy mniej.
</details>

4. Oszacuj energię jonizacji donora w krzemie z modelu atomu wodoru: elektron w ośrodku o $\varepsilon_r = 11{,}7$ z masą efektywną $0{,}26m_e$. Porównaj z $kT$ w 300 K.

<details>
<summary>Odpowiedź</summary>

$E = 13{,}6\ \mathrm{eV}\cdot\dfrac{0{,}26}{11{,}7^2} \approx 0{,}026\ \mathrm{eV}$ (zmierzone dla P: 0,045 eV). To porównywalne z $kT = 0{,}026\ \mathrm{eV}$, więc donory są prawie całkowicie zjonizowane. Promień orbity: $0{,}053\ \mathrm{nm}\cdot11{,}7/0{,}26 \approx 2{,}4\ \mathrm{nm}$, czyli wiele odległości międzyatomowych. To uzasadnia użycie $\varepsilon_r$.
</details>

## Źródła

- OpenStax, *Fizyka dla szkół wyższych*, t. 3, rozdz. 9 — §9.6 (półprzewodniki i domieszkowanie) i §9.7 (przyrządy półprzewodnikowe).
- Halliday, Resnick, Walker, *Podstawy fizyki* — wyd. 2015: t. 5, §41.2–41.3; wyd. 1: t. 5, §42.6–42.11.
- Symulacja PhET *Semiconductors* (materiał dodatkowy, po angielsku).
