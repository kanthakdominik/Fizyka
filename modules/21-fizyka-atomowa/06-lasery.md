# 21.06 — Emisja wymuszona i lasery

> **Moduł:** [21 — Fizyka atomowa](README.md) · **Poziom:** 🟢🔵 matura R + studia · **Status:** ✅ pełny
>
> **Czytaj:**
>
> - OpenStax, *Fizyka dla szkół wyższych*, t. 3, rozdz. 8: [§8.6](https://openstax.org/books/fizyka-dla-szk%C3%B3%C5%82-wy%C5%BCszych-tom-3/pages/8-6-lasery) · [wstęp do rozdziału](https://openstax.org/books/fizyka-dla-szk%C3%B3%C5%82-wy%C5%BCszych-tom-3/pages/8-wstep)
> - Halliday, Resnick, Walker, *Podstawy fizyki*, wyd. 2015, t. 5: §40.7 (s. 114)
> - Halliday, Resnick, Walker, *Podstawy fizyki*, wyd. 1 (2003), t. 5: [§41.11–41.12, s. 90](https://home.agh.edu.pl/~czapli/Resnick_5.pdf#page=106) — PDF z serwera AGH

← [Widma atomowe i promieniowanie rentgenowskie](05-widma-i-promieniowanie-x.md) · [spis modułu](README.md) · (koniec modułu) →

## Po co to jest

Laser daje światło niezwykłe: jednobarwne, spójne, skierowane w wąską wiązkę i dające się skupić w maleńki punkt. Stoi za czytnikami kodów kreskowych, światłowodową łącznością internetu, chirurgią oka, cięciem stali, drukarkami, lidarami w samochodach, interferometrem LIGO i pomiarem odległości do Księżyca. Działa dzięki emisji wymuszonej, przewidzianej przez Einsteina w 1917 r. i wykorzystanej w praktyce dopiero w 1960 r.

## Teoria w pigułce

**Trzy procesy** między poziomami $E_1$ i $E_2$ atomu ($E_2 - E_1 = hf$):
1. **Absorpcja**: foton o energii $hf$ przenosi atom z $E_1$ na $E_2$.
2. **Emisja spontaniczna**: atom wzbudzony sam przechodzi na $E_1$ po średnim czasie życia $\tau$ (zwykle ok. 10 ns) i emituje foton w przypadkowym kierunku i fazie. Tak świecą żarówki, LED i lampy.
3. **Emisja wymuszona**: foton o energii $hf$ przechodzący obok wzbudzonego atomu wywołuje emisję drugiego fotonu, **identycznego** (ten sam kierunek, częstotliwość, faza, polaryzacja). Światło jest wzmacniane.

**Inwersja obsadzeń.** W równowadze termicznej stosunek obsadzeń wynosi (rozkład Boltzmanna)

$$\frac{N_2}{N_1} = e^{-(E_2 - E_1)/kT}.$$

Dla przejścia 2 eV w temperaturze pokojowej to ok. $10^{-34}$. Absorpcja zawsze wygrywa z emisją wymuszoną. Żeby wzmacniać, trzeba „przepompować” więcej atomów do stanu wyższego niż niższego: $N_2 > N_1$. Do tego potrzebne są:
- **pompowanie**: wyładowanie elektryczne, lampa błyskowa, inny laser, prąd w złączu półprzewodnikowym;
- **stan metastabilny**: długo żyjący poziom (np. ms zamiast ns), na którym atomy się gromadzą. Dlatego laser wymaga co najmniej trzech poziomów.

**Rezonator.** Ośrodek czynny umieszcza się między dwoma lustrami (jedno częściowo przepuszczalne). Fotony biegnące wzdłuż osi przechodzą tam i z powrotem wiele razy i za każdym razem są wzmacniane. Przetrwają tylko fale stojące, dla których na długości rezonatora mieści się całkowita liczba połówek fali (10.03).

**Przykłady:**
- **laser helowo-neonowy**: 632,8 nm, czerwony. Hel przekazuje energię neonowi w zderzeniach;
- **lasery półprzewodnikowe (diody laserowe)**: wskaźniki, czytniki, łączność 1,3–1,55 μm;
- **Nd:YAG**: 1064 nm, cięcie i spawanie, medycyna;
- **CO₂**: 10,6 μm, cięcie materiałów.

**Właściwości wiązki:**
- **spójność** czasowa (droga spójności od cm do km, 18.01) i przestrzenna;
- **mała rozbieżność**: kąt ograniczony dyfrakcją, $\theta \sim \lambda/D$ (18.05);
- **wysoka jasność i natężenie po skupieniu**: wskaźnik 5 mW na plamce 1 mm daje kilka kW/m², więcej niż Słońce. Dlatego nie wolno patrzeć w wiązkę.

## Wzory i założenia

| Wzór | Znaczenie | Kiedy obowiązuje |
|---|---|---|
| $hf = E_2 - E_1$ | energia fotonu laserowego | — |
| $N_2/N_1 = e^{-\Delta E/kT}$ | obsadzenia w równowadze | równowaga termiczna |
| $N_2 > N_1$ | inwersja obsadzeń | warunek wzmocnienia |
| $L = m\lambda/2$ | mody rezonatora | lustra płaskie |
| $\Delta f = c/(2L)$ | odstęp modów | — |
| $\theta \approx \lambda/D$ | rozbieżność wiązki | ograniczenie dyfrakcyjne |

## Przykład rozwiązany

**Zadanie.** Laser He-Ne ma rezonator o długości 30 cm i wiązkę o średnicy 1 mm, a jego moc wynosi 5 mW.
1. Oblicz odstęp częstotliwości modów rezonatora.
2. Ile modów zmieści się w paśmie wzmocnienia neonu o szerokości 1,5 GHz?
3. Oblicz liczbę fotonów na sekundę i natężenie wiązki.

1. $\Delta f = c/(2L) = 500\ \mathrm{MHz}$.
2. Mieszczą się 3 mody.
3. $N = P\lambda/(hc) \approx 1{,}6\cdot10^{16}\ \mathrm{s^{-1}}$. $I = 5\cdot10^{-3}/(\pi\cdot0{,}5^2\cdot10^{-6}) \approx 6400\ \mathrm{W/m^2}$, prawie pięć razy więcej niż światło słoneczne.

### Wersja z rachunkiem różniczkowym i całkowym

**Wzmocnienie w ośrodku czynnym.** Natężenie wiązki zmienia się wzdłuż ośrodka jak

$$\frac{dI}{dx} = \sigma(N_2 - N_1)I \Rightarrow I(x) = I_0e^{\sigma(N_2 - N_1)x},$$

gdzie $\sigma$ to przekrój czynny na emisję wymuszoną. Dla $N_2 < N_1$ wiązka jest tłumiona (zwykła absorpcja, prawo Beera–Lamberta), a dla $N_2 > N_1$ wzmacniana.

Laser zaczyna pracować, gdy wzmocnienie na drodze tam i z powrotem przewyższa straty na lustrach: $R_1R_2e^{2gL} \ge 1$, gdzie $g = \sigma(N_2 - N_1)$. Przy lustrach 99,9% i 98% oraz $L = 0{,}3\ \mathrm m$ wystarcza $g \ge -\dfrac{\ln(R_1R_2)}{2L} \approx 0{,}035\ \mathrm{m^{-1}}$, czyli zaledwie 3,5% wzmocnienia na metr.

## Typowe pułapki

- **Laser to bardzo jasna żarówka.** Kluczowe są spójność i kierunkowość, wynikające z emisji wymuszonej.
- **Inwersję da się uzyskać grzaniem.** W równowadze termicznej zawsze $N_2 < N_1$, w dowolnej temperaturze.
- **Laser na dwóch poziomach.** Przy pompowaniu optycznym dwóch poziomów nie da się uzyskać trwałej inwersji, bo pompa wymusza też emisję. Potrzebne są trzy lub cztery poziomy.
- **Wiązka laserowa w ogóle się nie rozbiega.** Rozbiega się, choć słabo (dyfrakcja). Wiązka z Ziemi na Księżycu ma kilka kilometrów średnicy.

## Doświadczenie / symulacja

**Spójność lasera a LED.** Wykonaj doświadczenie Younga (18.02) z laserem i z diodą LED tej samej barwy przez wąską szczelinę. Z laserem prążki są wyraźne, z LED prawie znikają.

**Plamka (speckle).** Oświetl laserem matową ścianę i popatrz na ziarnisty, migoczący wzór. To interferencja światła spójnego rozproszonego na nierównościach. Przy ruchu głowy ziarna się przesuwają.

**Symulacja PhET:** *Lasery* (*Lasers*) — pompowanie, inwersja i emisja wymuszona na dwóch i trzech poziomach ([phet.colorado.edu/pl](https://phet.colorado.edu/pl/)).

**Python:** model populacji lasera trójpoziomowego (równania kinetyczne) i próg akcji laserowej.

```python
import numpy as np
from scipy.integrate import solve_ivp
import matplotlib.pyplot as plt

k = 1.380649e-23; e = 1.602176634e-19
print(f"N2/N1 dla 2 eV w 300 K: {np.exp(-2*e/(k*300)):.1e}")

# poziomy 1 (podstawowy), 3 (pompowany, szybko rozpada się do 2), 2 (metastabilny)
W = 400.0                  # tempo pompowania 1→3 [1/s]
t32, t21 = 1e-8, 3e-3       # czasy życia [s]
def rhs(t, N):
    N1, N2, N3 = N
    return [-W*N1 + N2/t21, N3/t32 - N2/t21, W*N1 - N3/t32]
sol = solve_ivp(rhs, (0, 0.03), [1, 0, 0], method="LSODA", max_step=1e-5)
N1, N2, N3 = sol.y[:, -1]
print(f"stan ustalony: N1 = {N1:.3f}, N2 = {N2:.3f}, inwersja: {N2 > N1}")
print(f"próg pompowania (N2 = N1): W = 1/τ21 = {1/t21:.0f} 1/s")
R1, R2, L = 0.999, 0.98, 0.3
print(f"wymagane wzmocnienie g ≥ {-np.log(R1*R2)/(2*L):.4f} 1/m")
plt.plot(sol.t*1e3, sol.y[0], label="N1"); plt.plot(sol.t*1e3, sol.y[1], label="N2 (metastabilny)")
plt.xlabel("t [ms]"); plt.ylabel("obsadzenie"); plt.legend(); plt.grid(True); plt.show()
```

## Zadania

### A. Poziom maturalny _(opcjonalnie — rozgrzewka)_

1. Czym różni się emisja wymuszona od spontanicznej?

<details>
<summary>Odpowiedź</summary>

Emisję wymuszoną wywołuje foton o odpowiedniej energii, a nowy foton jest jego kopią (kierunek, faza, częstotliwość). Emisja spontaniczna zachodzi samorzutnie, w przypadkowym kierunku i fazie.
</details>

2. Jaką energię (w eV) ma foton lasera He-Ne (632,8 nm) i lasera CO₂ (10,6 μm)?

<details>
<summary>Odpowiedź</summary>

1,96 eV i 0,117 eV.
</details>

### B. Poziom akademicki

1. Wiązka lasera o długości fali 532 nm i średnicy 1 m (teleskop) jest skierowana na Księżyc. Oszacuj średnicę plamki na Księżycu z dyfrakcji.

<details>
<summary>Odpowiedź</summary>

$\theta \approx 1{,}22\lambda/D \approx 6{,}5\cdot10^{-7}\ \mathrm{rad}$, średnica ok. $2\theta d \approx 500\ \mathrm m$. W praktyce atmosfera rozmywa wiązkę do kilku kilometrów.
</details>

2. Pokaż, że dla trzypoziomowego lasera w stanie ustalonym (szybkie przejście 3→2) inwersja $N_2 > N_1$ wymaga tempa pompowania $W > 1/\tau_{21}$.

<details>
<summary>Odpowiedź</summary>

W stanie ustalonym $N_3 \approx 0$ i $WN_1 = N_2/\tau_{21}$, czyli $N_2/N_1 = W\tau_{21}$. Inwersja dla $W\tau_{21} > 1$.
</details>

3. W temperaturze, w której $kT$ równa się energii przejścia, ile wynosi $N_2/N_1$? Jaka to temperatura dla 2 eV?

<details>
<summary>Odpowiedź</summary>

$e^{-1} \approx 0{,}37$, wciąż mniej niż 1. $T = 2\ \mathrm{eV}/k \approx 23\,000\ \mathrm K$. Grzaniem nie da się uzyskać inwersji.
</details>

## Źródła

- OpenStax, *Fizyka dla szkół wyższych*, t. 3, rozdz. 8 — §8.6: lasery.
- Halliday, Resnick, Walker, *Podstawy fizyki* — wyd. 2015: t. 5, §40.7; wyd. 1: t. 5, §41.11–41.12.
- Symulacja PhET *Lasery*.
