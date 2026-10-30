# 22.06 — Synteza termojądrowa i energia gwiazd

> **Moduł:** [22 — Fizyka jądrowa](README.md) · **Poziom:** 🟢 matura R · **Status:** ✅ pełny
>
> **Czytaj:**
>
> - OpenStax, *Fizyka dla szkół wyższych*, t. 3, rozdz. 10: [§10.6](https://openstax.org/books/fizyka-dla-szk%C3%B3%C5%82-wy%C5%BCszych-tom-3/pages/10-6-fuzja-jadrowa) · [wstęp do rozdziału](https://openstax.org/books/fizyka-dla-szk%C3%B3%C5%82-wy%C5%BCszych-tom-3/pages/10-wstep)
> - Halliday, Resnick, Walker, *Podstawy fizyki*, wyd. 2015, t. 5: §43.4–43.6 (s. 219)
> - Halliday, Resnick, Walker, *Podstawy fizyki*, wyd. 1 (2003), t. 5: [§44.6–44.8, s. 183](https://home.agh.edu.pl/~czapli/Resnick_5.pdf#page=199) — PDF z serwera AGH

← [Rozszczepienie jąder i reaktor](05-rozszczepienie.md) · [spis modułu](README.md) · [Oddziaływanie promieniowania z materią, dawki i ochrona](07-promieniowanie-i-dawki.md) →

## Po co to jest

Słońce i inne gwiazdy świecą dzięki syntezie (fuzji) lekkich jąder w cięższe. W nich też powstały wszystkie pierwiastki od węgla do żelaza, z których jesteśmy zbudowani. Opanowanie kontrolowanej syntezy na Ziemi (ITER we Francji, tokamaki, lasery w National Ignition Facility) dałoby praktycznie niewyczerpane źródło energii z wody, bez długożyciowych odpadów. Fizyka syntezy wyjaśnia też, dlaczego jest to tak trudne.

## Teoria w pigułce

**Energia syntezy.** Lekkie jądra mają małą energię wiązania na nukleon (22.02). Ich połączenie daje jądro silniej związane i wydziela energię. Najważniejsze reakcje:

| Reakcja | $Q$ |
|---|---|
| $\mathrm D + \mathrm T \to {}^4\mathrm{He} + n$ | 17,6 MeV |
| $\mathrm D + \mathrm D \to {}^3\mathrm{He} + n$ | 3,3 MeV |
| $\mathrm D + \mathrm D \to \mathrm T + p$ | 4,0 MeV |
| cykl pp w Słońcu: $4p \to {}^4\mathrm{He} + 2e^+ + 2\nu$ | 26,7 MeV (z anihilacją pozytonów) |

Na kilogram paliwa synteza D–T daje ok. $3{,}4\cdot10^{14}\ \mathrm J$, czterokrotnie więcej niż rozszczepienie uranu i ok. 10 mln razy więcej niż węgiel.

**Bariera kulombowska.** Jądra są dodatnie i odpychają się. Żeby oddziaływanie silne zadziałało, muszą się zbliżyć na ok. 3 fm. Bariera wynosi wtedy $ke^2/r \approx 0{,}5\ \mathrm{MeV}$. Średnia energia cząstek w temperaturze $T$ to $\tfrac32kT$, więc klasycznie potrzeba ok. $4\cdot10^9\ \mathrm K$.

Synteza zachodzi w niższych temperaturach dzięki:
- **tunelowaniu** przez barierę (20.07);
- **ogonowi rozkładu Maxwella** (11.04): najszybsze cząstki mają energie wielokrotnie większe od średniej.

Wnętrze Słońca ma ok. $1{,}5\cdot10^7\ \mathrm K$ ($kT \approx 1{,}3\ \mathrm{keV}$), a reakcja pp zachodzi tak wolno, że Słońce świeci ok. 10 mld lat. W reaktorach D–T potrzeba ok. $10^8\ \mathrm K$, bo plazma ma dużo mniejszą gęstość niż wnętrze Słońca.

**Warunki zapłonu (kryterium Lawsona).** Plazma musi być jednocześnie dość gorąca, gęsta i utrzymana dość długo, żeby energia z syntezy przewyższyła straty:

$$n\tau_ET \gtrsim 3\cdot10^{21}\ \mathrm{keV\cdot s/m^3} \quad\text{(dla D–T)}.$$

**Sposoby utrzymania plazmy:**
- **magnetyczne** (tokamak, stellarator): plazma o temperaturze 100–150 mln K jest uwięziona w polu magnetycznym, bo naładowane cząstki krążą wokół linii pola (14.01). ITER ma uzyskać 10 razy więcej mocy z syntezy, niż dostarcza grzanie plazmy.
- **inercyjne**: kapsułka D–T jest ściskana laserami w nanosekundach. NIF w 2022 r. po raz pierwszy uzyskał więcej energii z syntezy niż energia wiązki laserowej dostarczonej do celu.

## Wzory i założenia

| Wzór | Znaczenie | Kiedy obowiązuje |
|---|---|---|
| $Q = (\sum m_{\text{przed}} - \sum m_{\text{po}})c^2$ | energia syntezy | — |
| $U_C = kZ_1Z_2e^2/r$ | bariera kulombowska | $r$ — suma promieni jąder |
| $\bar E = \tfrac32kT$ | średnia energia cząstek | plazma w równowadze |
| $n\tau_ET \gtrsim 3\cdot10^{21}\ \mathrm{keV\,s/m^3}$ | kryterium Lawsona (D–T) | — |

## Przykład rozwiązany

**Zadanie 1.** Oblicz $Q$ reakcji D + T → ⁴He + n. Masy: ²H 2,014102 u, ³H 3,016049 u, ⁴He 4,002603 u, n 1,008665 u. Jak dzieli się energia między produkty?

$Q = (2{,}014102 + 3{,}016049 - 4{,}002603 - 1{,}008665)\cdot931{,}5 \approx 17{,}6\ \mathrm{MeV}$.

Pędy produktów są równe i przeciwne, więc energie dzielą się odwrotnie do mas: neutron unosi $\tfrac45$, czyli 14,1 MeV, a cząstka alfa 3,5 MeV. Neutrony uciekają z plazmy i grzeją ścianki (płaszcz), a cząstki alfa podgrzewają plazmę.

**Zadanie 2.** Słońce emituje $3{,}83\cdot10^{26}\ \mathrm W$. Ile reakcji cyklu pp zachodzi na sekundę i ile wodoru Słońce „spala”?

$N = 3{,}83\cdot10^{26}/(26{,}7\cdot1{,}6\cdot10^{-13}) \approx 9\cdot10^{37}\ \mathrm{s^{-1}}$. Wodoru: $4N\cdot m_p \approx 6\cdot10^{11}\ \mathrm{kg/s}$, czyli ok. 600 mln ton na sekundę. Ubytek masy to ok. 4 mln ton na sekundę (19.05).

## Typowe pułapki

- **Synteza wymaga temperatury bariery kulombowskiej.** Dzięki tunelowaniu i ogonowi rozkładu Maxwella zachodzi w temperaturze ok. 100 razy niższej.
- **Wodór w Słońcu łączy się bezpośrednio w hel.** To łańcuch kilku reakcji. Pierwsza ($p + p \to d + e^+ + \nu$) wymaga oddziaływania słabego i jest bardzo powolna.
- **Synteza nie daje promieniotwórczości.** Neutrony 14 MeV aktywują materiały konstrukcyjne reaktora, a tryt jest promieniotwórczy, ale odpady są krótko żyjące w porównaniu z rozszczepieniem.
- **Energia syntezy na reakcję jest większa niż rozszczepienia.** Na reakcję mniejsza (17,6 vs 200 MeV). Na kilogram paliwa większa.

## Doświadczenie / symulacja

**Ogon rozkładu Maxwella.** Policz w Pythonie (kod niżej), jaki ułamek jąder w plazmie ma energię większą od 10, 20, 50 razy $kT$. Zobacz, jak szybko maleje.

**Python:** energia reakcji, bariera kulombowska i ułamek cząstek o energii powyżej progu.

```python
import numpy as np
from scipy.special import gammaincc

uc2, e, k, kC = 931.494, 1.602176634e-19, 1.380649e-23, 8.98755e9
Q = (2.014102 + 3.016049 - 4.002603 - 1.008665)*uc2
print(f"D + T: Q = {Q:.2f} MeV, neutron {Q*4.002603/(4.002603 + 1.008665):.1f} MeV, alfa {Q*1.008665/(4.002603 + 1.008665):.1f} MeV")
Uc = kC*e**2/3e-15/e/1e6
print(f"bariera kulombowska (3 fm): {Uc:.2f} MeV, odpowiada T = {2/3*Uc*1e6*e/k:.1e} K")
for T in (1.5e7, 1e8):
    kT = k*T/e/1e3
    print(f"T = {T:.1e} K: kT = {kT:.2f} keV")
for x in (10, 20, 50):                            # ułamek cząstek z E > x·kT (rozkład Maxwella: Γ(3/2, x)/Γ(3/2))
    print(f"E > {x} kT: ułamek {gammaincc(1.5, x):.2e}")
print(f"Słońce: {3.83e26/(26.7e6*e):.2e} reakcji pp/s, spala {4*3.83e26/(26.7e6*e)*1.6726e-27:.2e} kg H/s")
print(f"energia D–T na kg paliwa: {Q*1e6*e/(5.03*1.66054e-27):.2e} J/kg")
```

## Zadania

### A. Poziom maturalny

1. Uzupełnij reakcję: $^2_1\mathrm H + {}^2_1\mathrm H \to {}^3_2\mathrm{He} + ?$

<details>
<summary>Odpowiedź</summary>

Neutron $^1_0n$.
</details>

2. Dlaczego synteza jądrowa wymaga ogromnych temperatur, a rozszczepienie nie?

<details>
<summary>Odpowiedź</summary>

Łączące się jądra są dodatnie i trzeba pokonać ich odpychanie. Rozszczepienie wywołują neutrony, które nie są odpychane.
</details>

3. Oblicz, ile energii daje synteza 1 g mieszaniny D–T (5 u na reakcję) i porównaj z 1 g ²³⁵U.

<details>
<summary>Odpowiedź</summary>

D–T: ok. $3{,}4\cdot10^{11}\ \mathrm J$. U-235: ok. $8{,}2\cdot10^{10}\ \mathrm J$. Synteza daje ok. 4 razy więcej na gram.
</details>

### B. Poziom akademicki _(opcjonalnie — rozszerzenie z rachunkiem)_

1. Pokaż, że w rozpadzie na dwa ciała (np. produkty syntezy D–T przy pomijalnym pędzie początkowym) energie kinetyczne dzielą się odwrotnie proporcjonalnie do mas.

<details>
<summary>Odpowiedź</summary>

$p_1 = p_2 = p$, $E_i = p^2/(2m_i)$, więc $E_1/E_2 = m_2/m_1$ i $E_1 = Q\dfrac{m_2}{m_1 + m_2}$.
</details>

2. Ile deuteru jest w 1 litrze wody (D/H ≈ 1/6420)? Ile energii dałaby jego synteza w reakcji D + D (średnio ok. 3,65 MeV)? Porównaj z 1 litrem benzyny (34 MJ).

<details>
<summary>Odpowiedź</summary>

1 L wody to 55,5 mola, czyli $6{,}7\cdot10^{25}$ atomów H, z czego ok. $1{,}0\cdot10^{22}$ D. Reakcji $5{,}2\cdot10^{21}$, energia $5{,}2\cdot10^{21}\cdot3{,}65\ \mathrm{MeV} \approx 3\cdot10^9\ \mathrm J$, ok. 90 razy więcej niż litr benzyny. (Przy pełnym spaleniu deuteru z dalszymi reakcjami T i ³He jeszcze więcej.)
</details>

## Źródła

- OpenStax, *Fizyka dla szkół wyższych*, t. 3, rozdz. 10 — §10.6: synteza jądrowa.
- Halliday, Resnick, Walker, *Podstawy fizyki* — wyd. 2015: t. 5, §43.4–43.6; wyd. 1: t. 5, §44.6–44.8.
