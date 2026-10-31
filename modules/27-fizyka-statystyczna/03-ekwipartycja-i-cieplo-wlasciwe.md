# 27.03 — Ekwipartycja energii i kwantowe zamrażanie stopni swobody

> **Moduł:** [27 — Fizyka statystyczna](README.md) · **Poziom:** 🔵 studia · **Status:** ✅ pełny
>
> **Czytaj:**
>
> - OpenStax, *Fizyka dla szkół wyższych*, t. 2, rozdz. 2: [§2.3](https://openstax.org/books/fizyka-dla-szk%C3%B3%C5%82-wy%C5%BCszych-tom-2/pages/2-3-cieplo-wlasciwe-i-zasada-ekwipartycji-energii) · [wstęp do rozdziału](https://openstax.org/books/fizyka-dla-szk%C3%B3%C5%82-wy%C5%BCszych-tom-2/pages/2-wstep)
> - Halliday, Resnick, Walker, *Podstawy fizyki*, wyd. 2015, t. 2: §19.7–19.8 (s. 306)
> - Halliday, Resnick, Walker, *Podstawy fizyki*, wyd. 1 (2003), t. 2: [§20.8–20.10, s. 239](https://home.agh.edu.pl/~czapli/Resnick_2.pdf#page=255) — PDF z serwera AGH

← [Rozkład Boltzmanna i suma statystyczna](02-rozklad-boltzmanna.md) · [spis modułu](README.md) · [Statystyki kwantowe: fermiony, bozony i promieniowanie cieplne](04-statystyki-kwantowe.md) →

## Po co to jest

Dlaczego ciepło molowe helu wynosi $\tfrac32R$, azotu w temperaturze pokojowej $\tfrac52R$, a prawie wszystkich metali ok. $3R$? Odpowiada na to zasada ekwipartycji energii. Równie ważne jest to, gdzie ona zawodzi: w niskich temperaturach ciepło właściwe ciał stałych spada do zera, a wodór „traci” stopnie swobody rotacji. Fizyka klasyczna nie potrafiła tego wyjaśnić — to był jeden z problemów, które doprowadziły do fizyki kwantowej. Ciepło molowe jest na karcie wzorów maturalnych, a rozumienie stopni swobody pomaga w zadaniach z termodynamiki (11.05).

## Teoria w pigułce

**Zasada ekwipartycji.** W równowadze termicznej każdy wyraz energii zależny od kwadratu położenia lub pędu (**kwadratowy stopień swobody**) ma średnio energię

$$\langle E\rangle = \tfrac12kT.$$

Przykłady stopni swobody:
- ruch postępowy: $\tfrac12mv_x^2$, $\tfrac12mv_y^2$, $\tfrac12mv_z^2$ — 3 stopnie;
- obrót cząsteczki liniowej (dwuatomowej) wokół dwóch osi — 2 stopnie;
- drgania wzdłuż wiązania: energia kinetyczna i potencjalna sprężystości — 2 stopnie;
- atom w krysztale drgający w trzech kierunkach — 6 stopni (3 kinetyczne + 3 potencjalne).

**Ciepło molowe** przy stałej objętości to $C_V = \dfrac s2R$, gdzie $s$ — liczba stopni swobody, $C_p = C_V + R$ (11.05), $\kappa = C_p/C_V$:

| Układ | $s$ | $C_V$ | $\kappa$ |
|---|---|---|---|
| gaz jednoatomowy (He, Ar) | 3 | $\tfrac32R = 12{,}5\ \mathrm{J/(mol\cdot K)}$ | 5/3 |
| gaz dwuatomowy (N₂, O₂), 300 K | 5 | $\tfrac52R = 20{,}8$ | 7/5 |
| gaz dwuatomowy, bardzo wysoka temperatura | 7 | $\tfrac72R$ | 9/7 |
| ciało stałe (prawo Dulonga–Petita) | 6 | $3R = 24{,}9$ | — |

**Gdzie ekwipartycja zawodzi.** Doświadczenie pokazuje, że:
- drgania cząsteczek N₂ i O₂ w temperaturze pokojowej nie wnoszą nic do $C_V$;
- ciepło molowe wodoru spada poniżej ok. 100 K z $\tfrac52R$ do $\tfrac32R$;
- ciepło właściwe ciał stałych w niskich temperaturach dąży do zera (diament już w temperaturze pokojowej ma tylko $0{,}75R$).

**Wyjaśnienie kwantowe.** Energia drgań i obrotów jest skwantowana (20.06, 23.01). Jeśli odstęp poziomów $\Delta E$ jest dużo większy od $kT$, prawie żadna cząsteczka nie jest wzbudzona i stopień swobody jest „zamrożony”. Charakterystyczne temperatury $\theta = \Delta E/k$:

| Ruch | Przykład | $\theta$ |
|---|---|---|
| obrót | H₂ | ok. 88 K |
| obrót | N₂ | ok. 3 K |
| drgania | H₂ | ok. 6300 K |
| drgania | N₂ | ok. 3400 K |
| drgania sieci (temperatura Einsteina) | diament | ok. 1300 K |
| drgania sieci | ołów | ok. 70 K |

Stopień swobody działa w pełni dopiero dla $T \gg \theta$.

**Model Einsteina (1907)** — atomy kryształu jako niezależne oscylatory kwantowe o częstości $\omega$. Ze średniej energii oscylatora (27.02):

$$C_V = 3R\frac{x^2e^x}{(e^x - 1)^2}, \qquad x = \frac{\theta_E}{T} = \frac{\hbar\omega}{kT}.$$

Dla $T \gg \theta_E$ daje $3R$, dla $T \ll \theta_E$ spada wykładniczo. Model Debye'a (drgania sieci jako fale o różnych częstościach) poprawia zachowanie w niskich temperaturach: $C_V \propto T^3$.

## Wzory i założenia

| Wzór | Znaczenie | Kiedy obowiązuje |
|---|---|---|
| $\langle E\rangle = \tfrac12kT$ na stopień swobody | zasada ekwipartycji | kwadratowe stopnie swobody, $kT \gg \Delta E$ |
| $C_V = \tfrac s2R$, $C_p = C_V + R$ | ciepło molowe gazu doskonałego | — |
| $E_{śr} = \tfrac s2kT$ | średnia energia cząsteczki | karta wzorów CKE |
| $C_V = 3R$ | prawo Dulonga–Petita | ciała stałe, $T \gg \theta_E$ |
| $C_V = 3R\dfrac{x^2e^x}{(e^x - 1)^2}$, $x = \theta_E/T$ | model Einsteina | — |
| $\theta = \Delta E/k$ | temperatura charakterystyczna | — |

## Przykład rozwiązany

**Zadanie 1.** Ile ciepła trzeba dostarczyć, żeby ogrzać o 10 K przy stałej objętości 1 mol helu, 1 mol azotu i 1 mol miedzi w temperaturze pokojowej?

He: $\tfrac32R\cdot10 = 125\ \mathrm J$. N₂: $\tfrac52R\cdot10 = 208\ \mathrm J$. Cu: $3R\cdot10 = 249\ \mathrm J$ (zmierzone: 245 J).

**Zadanie 2.** Ciepło właściwe miedzi to $385\ \mathrm{J/(kg\cdot K)}$, a ołowiu $129\ \mathrm{J/(kg\cdot K)}$. Sprawdź prawo Dulonga–Petita ($M_{\mathrm{Cu}} = 63{,}5\ \mathrm{g/mol}$, $M_{\mathrm{Pb}} = 207\ \mathrm{g/mol}$).

Cu: $0{,}0635\cdot385 = 24{,}4\ \mathrm{J/(mol\cdot K)}$. Pb: $0{,}207\cdot129 = 26{,}7$. Oba bliskie $3R = 24{,}9$. Prawo Dulonga–Petita (1819) pozwalało szacować masy atomowe nowych pierwiastków.

### Wersja z rachunkiem różniczkowym i całkowym

**Ekwipartycja z czynnika Boltzmanna.** Dla stopnia swobody o energii $E = aq^2$:

$$\langle E\rangle = \frac{\int aq^2e^{-\beta aq^2}dq}{\int e^{-\beta aq^2}dq} = -\frac{\partial}{\partial\beta}\ln\int e^{-\beta aq^2}dq = -\frac{\partial}{\partial\beta}\ln\sqrt{\frac{\pi}{\beta a}} = \frac{1}{2\beta} = \frac12kT.$$

Wynik nie zależy od $a$ — stąd uniwersalność ekwipartycji.

**Ciepło właściwe Einsteina.** Z $\langle E\rangle = \dfrac{\hbar\omega}{e^{\hbar\omega/kT} - 1}$ dla $3N_A$ oscylatorów:

$$C_V = 3N_A\frac{d\langle E\rangle}{dT} = 3N_Ak\frac{x^2e^x}{(e^x - 1)^2}.$$

Dla $x \to 0$: $e^x \approx 1 + x$, więc $C_V \to 3R$. Dla diamentu ($\theta_E = 1320\ \mathrm K$) w 300 K: $x = 4{,}4$, $C_V \approx 0{,}24\cdot3R$. W 100 K już tylko $0{,}0003\cdot3R$ — model Einsteina zaniża tę wartość, bo pomija niskoczęstotliwościowe drgania sieci (model Debye'a).

## Typowe pułapki

- **Każda cząsteczka dwuatomowa ma 7 stopni swobody, więc $C_V = \tfrac72R$.** W temperaturze pokojowej drgania są zamrożone: $C_V = \tfrac52R$.
- **Obrót atomu wokół własnej osi to dodatkowe stopnie swobody.** Dla atomu (i dla obrotu cząsteczki liniowej wokół jej osi) moment bezwładności jest tak mały, że odstęp poziomów rotacyjnych jest ogromny — te obroty są zamrożone.
- **$\tfrac12kT$ na stopień swobody liczy się na mol.** Na cząsteczkę $\tfrac12kT$, na mol $\tfrac12RT$.
- **Prawo Dulonga–Petita obowiązuje zawsze.** Tylko dla $T \gg \theta_E$. Diament, beryl i bor mają w temperaturze pokojowej znacznie mniejsze ciepło molowe.

## Doświadczenie / symulacja

**Ciepło właściwe metali.** Podgrzej w gorącej wodzie (np. 80°C) jednakowe masy aluminium, żelaza i miedzi (np. ciężarki), wrzuć do kalorymetru z zimną wodą i zmierz temperaturę końcową (11.02). Policz ciepło właściwe i ciepło molowe. Wszystkie wyjdą bliskie $3R = 25\ \mathrm{J/(mol\cdot K)}$, choć ciepła właściwe na kilogram różnią się ponad dwukrotnie.

**Symulacja PhET:** *Właściwości gazu* — porównaj ogrzewanie gazu lekkich i ciężkich cząsteczek przy stałej objętości ([phet.colorado.edu/pl](https://phet.colorado.edu/pl/)).

**Python:** ciepło molowe kryształu Einsteina, model ciepła molowego wodoru z zamrażaniem obrotów i drgań oraz sprawdzenie ekwipartycji przez losowanie z rozkładu Boltzmanna.

```python
import numpy as np
import matplotlib.pyplot as plt

R = 8.314462618
einstein = lambda x: x**2*np.exp(-x)/(-np.expm1(-x))**2      # C/k jednego oscylatora kwantowego (= x²eˣ/(eˣ−1)², postać bez przepełnienia)

T = np.logspace(0, 4, 400)
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 4.5))
for nazwa, th in [("ołów", 70), ("miedź", 240), ("diament", 1320)]:
    ax1.plot(T, einstein(th/T), label=f"{nazwa} (θ_E = {th} K)")
    print(f"{nazwa:8s}: C_V/3R w 300 K = {einstein(th/300):.3f}")
ax1.set_xscale("log"); ax1.set_xlabel("T [K]"); ax1.set_ylabel("C_V / 3R"); ax1.legend(); ax1.set_title("model Einsteina")

def rotacja(T, theta, nmax=40):                               # ciepło molowe rotacji z sumy statystycznej rotatora
    J = np.arange(nmax)[:, None]
    w = (2*J + 1)*np.exp(-J*(J + 1)*theta/T)
    E = (J*(J + 1)*theta*w).sum(0)/w.sum(0)
    return np.gradient(E, T)
Th = np.linspace(10, 10000, 4000)
C_H2 = 1.5 + rotacja(Th, 87.6) + einstein(6330/Th)            # w jednostkach R (bez rozróżnienia orto/para)
ax2.plot(Th, C_H2); ax2.set_xscale("log"); ax2.set_xlabel("T [K]"); ax2.set_ylabel("C_V / R"); ax2.set_title("wodór H₂ (model)")
for t in (20, 300, 3000, 10000):
    print(f"H₂, T = {t:5d} K: C_V ≈ {np.interp(t, Th, C_H2):.2f} R")

rng = np.random.default_rng(0)                                # ekwipartycja: <a q²> = kT/2 niezależnie od a (kT = 1)
for a in (0.1, 1, 25):
    q = rng.normal(0, np.sqrt(1/(2*a)), 10**6)
    print(f"a = {a:5}: <a q²> = {np.mean(a*q**2):.4f} (teoria 0,5)")
plt.tight_layout(); plt.show()
```

## Zadania

### A. Poziom maturalny _(opcjonalnie — rozgrzewka)_

1. Ile wynosi średnia energia kinetyczna ruchu postępowego cząsteczki azotu, a ile całkowita energia (ruch postępowy i obrót) w temperaturze 300 K?

<details>
<summary>Odpowiedź</summary>

Postępowa: $\tfrac32kT = 6{,}2\cdot10^{-21}\ \mathrm J$. Z obrotem: $\tfrac52kT = 1{,}04\cdot10^{-20}\ \mathrm J$.
</details>

2. Oblicz $C_p$ i $\kappa = C_p/C_V$ dla gazu jednoatomowego i dwuatomowego w temperaturze pokojowej.

<details>
<summary>Odpowiedź</summary>

Jednoatomowy: $C_p = \tfrac52R$, $\kappa = 5/3$. Dwuatomowy: $C_p = \tfrac72R$, $\kappa = 7/5$.
</details>

### B. Poziom akademicki

1. Oszacuj temperaturę, powyżej której zaczyna się obrót cząsteczek H₂ ($I = 4{,}6\cdot10^{-48}\ \mathrm{kg\cdot m^2}$), z warunku $kT \approx \hbar^2/I$ (odstęp poziomów $J = 0 \to 1$).

<details>
<summary>Odpowiedź</summary>

$\hbar^2/(Ik) = (1{,}055\cdot10^{-34})^2/(4{,}6\cdot10^{-48}\cdot1{,}38\cdot10^{-23}) \approx 175\ \mathrm K$ ($\theta_{\text{rot}} = \hbar^2/(2Ik) \approx 88\ \mathrm K$).
</details>

2. Pokaż, że dla $x = \theta_E/T \to 0$ wzór Einsteina daje $C_V \to 3R$, a dla $x \to \infty$ — $C_V \approx 3Rx^2e^{-x}$.

<details>
<summary>Odpowiedź</summary>

Dla małych $x$: $e^x - 1 \approx x$, $e^x \approx 1$, więc $\dfrac{x^2e^x}{(e^x - 1)^2} \to 1$. Dla dużych $x$: $(e^x - 1)^2 \approx e^{2x}$, więc wyrażenie $\approx x^2e^{-x}$.
</details>

3. Oblicz średnią energię oscylatora harmonicznego $E = \tfrac12mv^2 + \tfrac12kx^2$ z ekwipartycji i porównaj z kwantowym wynikiem dla drgań cząsteczki N₂ ($\theta = 3400\ \mathrm K$) w 300 K.

<details>
<summary>Odpowiedź</summary>

Klasycznie $kT$. Kwantowo $\dfrac{k\theta}{e^{\theta/T} - 1} = kT\cdot\dfrac{11{,}3}{e^{11{,}3} - 1} \approx 1{,}4\cdot10^{-4}kT$ — drgania praktycznie zamrożone.
</details>

## Źródła

- OpenStax, *Fizyka dla szkół wyższych*, t. 2, rozdz. 2 — §2.3: ciepło właściwe i zasada ekwipartycji energii.
- Halliday, Resnick, Walker, *Podstawy fizyki* — wyd. 2015: t. 2, §19.7–19.8 (ciepła molowe, stopnie swobody); wyd. 1: t. 2, §20.8–20.10.
- F. Reif, *Fizyka statystyczna* (Kurs Fizyki Berkeley, t. 5), PWN.
- Moduły 11.04–11.05 (gaz doskonały, I zasada), 23.01 (widma cząsteczkowe).
- Symulacja PhET *Właściwości gazu*.
