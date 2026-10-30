# 23.04 — Teoria pasmowa ciał stałych

> **Moduł:** [23 — Fizyka ciała stałego](README.md) · **Poziom:** 🔵 studia · **Status:** ✅ pełny
>
> **Czytaj:**
>
> - OpenStax, *Fizyka dla szkół wyższych*, t. 3, rozdz. 9: [§9.5](https://openstax.org/books/fizyka-dla-szk%C3%B3%C5%82-wy%C5%BCszych-tom-3/pages/9-5-teoria-pasmowa-cial-stalych) · [wstęp do rozdziału](https://openstax.org/books/fizyka-dla-szk%C3%B3%C5%82-wy%C5%BCszych-tom-3/pages/9-wstep)
> - Halliday, Resnick, Walker, *Podstawy fizyki*, wyd. 2015, t. 5: §41.1 (s. 130)
> - Halliday, Resnick, Walker, *Podstawy fizyki*, wyd. 1 (2003), t. 5: [§42.3–42.5, s. 105](https://home.agh.edu.pl/~czapli/Resnick_5.pdf#page=121) — PDF z serwera AGH

← [Model elektronów swobodnych w metalach](03-elektrony-swobodne.md) · [spis modułu](README.md) · [Półprzewodniki, domieszkowanie i złącze p-n](05-polprzewodniki.md) →

## Po co to jest

Dlaczego miedź przewodzi prąd $10^{20}$ razy lepiej niż szkło, choć oba materiały mają podobną liczbę elektronów? Odpowiada na to teoria pasmowa. W krysztale poziomy energii atomów rozmywają się w pasma przedzielone przerwami. O tym, czy materiał jest przewodnikiem, izolatorem czy półprzewodnikiem, decyduje to, czy najwyższe obsadzone pasmo jest zapełnione i jak szeroka jest przerwa nad nim. Teoria pasmowa wyjaśnia też, dlaczego szkło i diament są przezroczyste, a krzem nieprzezroczysty, i jakiej barwy będzie dioda LED (23.05).

## Teoria w pigułce

**Od poziomów do pasm.** Gdy dwa jednakowe atomy się zbliżają, każdy ich poziom energii rozszczepia się na dwa (jak w cząsteczce H₂, 23.01). W krysztale z $N \sim 10^{23}$ atomów każdy poziom rozszczepia się na $N$ bardzo bliskich poziomów, tworząc praktycznie ciągłe **pasmo**. Między pasmami są **przerwy energetyczne** (pasma wzbronione), w których elektrony nie mogą mieć energii.

**Inny obraz: elektron w sieci periodycznej.** Fala elektronu odbija się od rzędów jonów jak promieniowanie rentgenowskie (warunek Bragga, 18.07). Dla pewnych długości fali odbite fale tworzą fale stojące i przy tych energiach pojawiają się przerwy.

**Pasmo walencyjne** to najwyższe pasmo zapełnione w 0 K, a **pasmo przewodnictwa** najbliższe wyższe. Prąd mogą przewodzić tylko elektrony, które mają wolne stany w pobliżu, czyli w paśmie częściowo zapełnionym.

| Rodzaj | Struktura pasm | Przerwa $E_g$ | Przykłady |
|---|---|---|---|
| **przewodnik (metal)** | pasmo częściowo zapełnione albo pasma nachodzące | brak | Cu, Al, Na |
| **izolator** | pasmo walencyjne pełne, przewodnictwa puste | duża (> ok. 4 eV) | diament 5,5 eV, SiO₂ ok. 9 eV |
| **półprzewodnik** | jak izolator, ale przerwa mała | 0,1–3 eV | Si 1,12 eV, Ge 0,66 eV, GaAs 1,42 eV |

**Przewodnictwo półprzewodników samoistnych.** Ruchy cieplne przenoszą część elektronów przez przerwę. W paśmie walencyjnym zostają **dziury**, które zachowują się jak nośniki dodatnie. Koncentracja nośników rośnie bardzo silnie z temperaturą:

$$n_i \propto T^{3/2}e^{-E_g/(2kT)}.$$

Dlatego opór półprzewodnika maleje z temperaturą, odwrotnie niż metalu (13.02). Na tym działają termistory NTC.

**Własności optyczne.** Foton o energii $hf > E_g$ może przenieść elektron przez przerwę i zostać pochłonięty. Fotony o mniejszej energii przechodzą.
- Diament ($E_g = 5{,}5\ \mathrm{eV}$, próg 225 nm) i szkło przepuszczają całe światło widzialne (1,6–3,3 eV), więc są przezroczyste.
- Krzem ($E_g = 1{,}12\ \mathrm{eV}$, próg 1,1 μm) pochłania całe światło widzialne, ale jest przezroczysty dla podczerwieni powyżej 1,1 μm. Stąd soczewki krzemowe w kamerach termowizyjnych.
- Metale silnie odbijają światło, bo ich swobodne elektrony drgają razem z polem fali.

## Wzory i założenia

| Wzór | Znaczenie | Kiedy obowiązuje |
|---|---|---|
| $N$ atomów → $N$ poziomów w paśmie | powstawanie pasm | — |
| $n_i \propto T^{3/2}e^{-E_g/(2kT)}$ | koncentracja nośników samoistnych | półprzewodnik niedomieszkowany |
| $\lambda_{\text{gr}} = hc/E_g$ | krawędź absorpcji | przejście przez przerwę |
| $\sigma = ne\mu_e + pe\mu_h$ | przewodność | $\mu$ — ruchliwości nośników |

## Przykład rozwiązany

### Wersja z rachunkiem różniczkowym i całkowym

**Zadanie 1.** Oblicz krawędź absorpcji dla Si, Ge, GaAs i diamentu. Które z nich są przezroczyste dla światła widzialnego?

Si: 1107 nm. Ge: 1880 nm. GaAs: 873 nm. Diament: 225 nm. Przezroczysty jest tylko diament. Pozostałe pochłaniają światło widzialne i wydają się szare lub czarne z metalicznym połyskiem.

**Zadanie 2.** Porównaj czynnik $e^{-E_g/(2kT)}$ dla krzemu i diamentu w 300 K. Jak zmienia się koncentracja nośników w krzemie przy ogrzaniu od 300 do 350 K?

Si: $e^{-1{,}12/0{,}0517} \approx 3{,}9\cdot10^{-10}$. Diament: $\approx 6\cdot10^{-47}$. Stosunek to ok. $10^{37}$: diament jest doskonałym izolatorem.

Przy ogrzaniu: $\dfrac{n_i(350)}{n_i(300)} = \left(\dfrac{350}{300}\right)^{3/2}\exp\left[\dfrac{E_g}{2k}\left(\dfrac1{300} - \dfrac1{350}\right)\right] \approx 1{,}26\cdot e^{3{,}1} \approx 28$ razy.

**Pochodna logarytmiczna** (czułość termistora): $\dfrac{d\ln n_i}{dT} = \dfrac{3}{2T} + \dfrac{E_g}{2kT^2} \approx 0{,}005 + 0{,}072\ \mathrm{K^{-1}}$ dla Si w 300 K, czyli ok. 7–8% na kelwin. Dla metalu opór zmienia się tylko o ok. 0,4% na kelwin.

## Typowe pułapki

- **Izolator nie ma elektronów, które mogłyby się poruszać.** Ma ich mnóstwo, ale pasmo walencyjne jest pełne i nie ma wolnych stanów, do których mogłyby przejść.
- **Dziura to brak atomu.** Dziura to brak elektronu w paśmie walencyjnym, zachowujący się jak nośnik dodatni.
- **Granica izolator–półprzewodnik jest ostra.** Jest umowna (ok. 3–4 eV). Diament i GaN mogą być półprzewodnikami po domieszkowaniu.
- **Przezroczystość zależy od gęstości materiału.** Zależy od przerwy energetycznej (i od struktury, np. rozpraszania na granicach ziaren).

## Doświadczenie / symulacja

**Opór termistora i opornika.** Zmierz opór termistora NTC i zwykłego opornika metalowego w wodzie z lodem, w temperaturze pokojowej i w gorącej wodzie. Narysuj $\ln R$ termistora od $1/T$: nachylenie daje $E_g/(2k)$, czyli efektywną przerwę materiału termistora.

**Symulacja PhET:** *Band Structure* (starsza symulacja Java, wersja angielska) — studnie potencjału ułożone w szereg tworzą pasma ([phet.colorado.edu/pl](https://phet.colorado.edu/pl/)).

**Python:** model Kroniga–Penneya — powstawanie pasm dla elektronu w okresowym potencjale.

```python
import numpy as np
import matplotlib.pyplot as plt

hbar, me, e = 1.054571817e-34, 9.1093837e-31, 1.602176634e-19
a, b, U0 = 0.4e-9, 0.1e-9, 10.0                      # studnia, bariera [m], wysokość bariery [eV]
E = np.linspace(0.01, 25, 6000)
alpha = np.sqrt(2*me*E*e)/hbar
F = np.empty_like(E)
for i, (Ei, al) in enumerate(zip(E, alpha)):
    if Ei < U0:
        be = np.sqrt(2*me*(U0 - Ei)*e)/hbar
        F[i] = (be**2 - al**2)/(2*al*be)*np.sinh(be*b)*np.sin(al*a) + np.cosh(be*b)*np.cos(al*a)
    else:
        q = np.sqrt(2*me*(Ei - U0)*e)/hbar
        F[i] = -(q**2 + al**2)/(2*al*q)*np.sin(q*b)*np.sin(al*a) + np.cos(q*b)*np.cos(al*a)
dozw = np.abs(F) <= 1                                 # stany dozwolone: |cos(k(a + b))| ≤ 1
krawedzie = E[np.where(np.diff(dozw.astype(int)) != 0)[0]]
print("granice pasm [eV]:", np.round(krawedzie, 2))
for Eg, nazwa in [(1.12, "Si"), (0.66, "Ge"), (5.5, "diament")]:
    print(f"{nazwa}: krawędź absorpcji {1239.84/Eg:.0f} nm, czynnik exp(−Eg/2kT) = {np.exp(-Eg*e/(2*1.380649e-23*300)):.1e}")
plt.plot(E, F); plt.fill_between(E, -1, 1, where=dozw, alpha=0.2, label="pasma dozwolone")
plt.ylim(-4, 4); plt.xlabel("E [eV]"); plt.ylabel("F(E)"); plt.legend(); plt.grid(True); plt.show()
```

## Zadania

### A. Poziom maturalny _(opcjonalnie — rozgrzewka)_

1. Dlaczego opór półprzewodnika maleje ze wzrostem temperatury, a metalu rośnie?

<details>
<summary>Odpowiedź</summary>

W półprzewodniku ciepło wytwarza nowe nośniki (elektrony przechodzą przez przerwę), a ich liczba rośnie wykładniczo. W metalu liczba nośników jest stała, a rośnie rozpraszanie na drganiach sieci.
</details>

2. Dlaczego szkło jest przezroczyste?

<details>
<summary>Odpowiedź</summary>

Przerwa energetyczna szkła (ok. 9 eV) jest większa od energii fotonów światła widzialnego, więc nie mogą one wzbudzić elektronów i nie są pochłaniane.
</details>

### B. Poziom akademicki

1. Kryształ zawiera $N$ atomów sodu. Każdy ma jeden elektron 3s. Ile stanów jest w paśmie 3s (ze spinem) i w jakiej części jest ono zapełnione? Dlaczego sód jest metalem?

<details>
<summary>Odpowiedź</summary>

$2N$ stanów i $N$ elektronów, czyli pasmo zapełnione w połowie. Elektrony mają wolne stany tuż nad sobą i mogą przyspieszać w polu.
</details>

2. Magnez ma dwa elektrony 3s, więc pasmo 3s jest pełne. Dlaczego mimo to jest metalem?

<details>
<summary>Odpowiedź</summary>

Pasmo 3s nachodzi na pasmo 3p, więc elektrony mają wolne stany w nachodzącym paśmie.
</details>

3. Opór termistora wynosi 10 kΩ w 25°C i 3,6 kΩ w 50°C. Oblicz efektywną przerwę z $R \propto e^{E_g/(2kT)}$ (pomiń czynnik $T^{3/2}$).

<details>
<summary>Odpowiedź</summary>

$\ln(10/3{,}6) = \dfrac{E_g}{2k}\left(\dfrac{1}{298} - \dfrac{1}{323}\right) \Rightarrow E_g \approx 2k\cdot\dfrac{1{,}02}{2{,}6\cdot10^{-4}} \approx 0{,}68\ \mathrm{eV}$.
</details>

## Źródła

- OpenStax, *Fizyka dla szkół wyższych*, t. 3, rozdz. 9 — §9.5: teoria pasmowa ciał stałych.
- Halliday, Resnick, Walker, *Podstawy fizyki* — wyd. 2015: t. 5, §41.1; wyd. 1: t. 5, §42.3–42.5.
- Symulacja PhET *Band Structure* (materiał dodatkowy, po angielsku).
