# 22.05 — Rozszczepienie jąder i reaktor

> **Moduł:** [22 — Fizyka jądrowa](README.md) · **Poziom:** 🟢 matura R · **Status:** ✅ pełny
>
> **Czytaj:**
>
> - OpenStax, *Fizyka dla szkół wyższych*, t. 3, rozdz. 10: [§10.5](https://openstax.org/books/fizyka-dla-szk%C3%B3%C5%82-wy%C5%BCszych-tom-3/pages/10-5-rozszczepienie-jadra-atomowego) · [wstęp do rozdziału](https://openstax.org/books/fizyka-dla-szk%C3%B3%C5%82-wy%C5%BCszych-tom-3/pages/10-wstep)
> - Halliday, Resnick, Walker, *Podstawy fizyki*, wyd. 2015, t. 5: §43.1–43.3 (s. 203)
> - Halliday, Resnick, Walker, *Podstawy fizyki*, wyd. 1 (2003), t. 5: [§44.1–44.5, s. 170](https://home.agh.edu.pl/~czapli/Resnick_5.pdf#page=186) — PDF z serwera AGH

← [Reakcje jądrowe i zasady zachowania](04-reakcje-jadrowe.md) · [spis modułu](README.md) · [Synteza termojądrowa i energia gwiazd](06-synteza.md) →

## Po co to jest

Rozszczepienie jądra uranu uwalnia ok. 200 MeV, czyli kilkadziesiąt milionów razy więcej niż spalenie jednej cząsteczki węgla. Elektrownie jądrowe dają ok. 10% światowej energii elektrycznej przy bardzo małej emisji CO₂, a Polska buduje pierwszą elektrownię jądrową. Fizyka rozszczepienia tłumaczy, jak działa reaktor, dlaczego potrzebny jest moderator i pręty sterujące, skąd biorą się odpady i jak działa broń jądrowa. Ta wiedza jest potrzebna, żeby rzeczowo dyskutować o energetyce.

## Teoria w pigułce

**Rozszczepienie.** Jądro ²³⁵U pochłania neutron, staje się wzbudzonym ²³⁶U, odkształca się jak kropla (model kroplowy, 22.02) i rozpada na dwa fragmenty o masach ok. 90–100 i 135–145, emitując 2–3 neutrony. Przykład:

$$^{235}\mathrm U + n \to {}^{141}\mathrm{Ba} + {}^{92}\mathrm{Kr} + 3n + \text{ok. }170\ \mathrm{MeV}.$$

Wraz z późniejszymi rozpadami β fragmentów i energią neutrin daje to ok. 200 MeV na rozszczepienie. Większość energii unoszą fragmenty jako energię kinetyczną, która zamienia się w ciepło w paliwie.

**Skąd energia.** Ciężkie jądra mają mniejszą energię wiązania na nukleon (7,6 MeV) niż średnie (ok. 8,5 MeV). Różnica, ok. 0,9 MeV na nukleon, daje ok. 200 MeV (22.02).

**Reakcja łańcuchowa.** Neutrony z jednego rozszczepienia wywołują kolejne. **Współczynnik mnożenia** $k$ to średnia liczba neutronów z jednego rozszczepienia, które wywołają następne:
- $k < 1$: reakcja wygasa (stan podkrytyczny);
- $k = 1$: stała moc (stan krytyczny, praca reaktora);
- $k > 1$: lawinowy wzrost (nadkrytyczny, broń).

**Reaktor jądrowy (lekkowodny):**
- **paliwo**: uran wzbogacony do 3–5% ²³⁵U (naturalny ma 0,72%, reszta to ²³⁸U, który rozszczepia się tylko szybkimi neutronami);
- **moderator** (woda): spowalnia szybkie neutrony (ok. 2 MeV) do termicznych (0,025 eV), które dużo chętniej rozszczepiają ²³⁵U;
- **pręty sterujące** (bor, kadm): pochłaniają neutrony i regulują $k$;
- **chłodziwo** odbiera ciepło i napędza turbinę (cykl parowy, sprawność ok. 33%, 11.06).

Sterowanie jest możliwe dzięki **neutronom opóźnionym**: ok. 0,65% neutronów pojawia się dopiero po sekundach, z rozpadów fragmentów. To spowalnia odpowiedź reaktora z mikrosekund do sekund.

**Odpady.** Fragmenty rozszczepienia są silnie promieniotwórcze. Większość szybko się rozpada, ale niektóre (np. ¹³⁷Cs, ⁹⁰Sr, ok. 30 lat) i transuranowce (pluton, ameryk) wymagają składowania przez tysiące lat. Objętość jest mała: ok. 25–30 t wypalonego paliwa rocznie z reaktora 1 GW.

## Wzory i założenia

| Wzór | Znaczenie | Kiedy obowiązuje |
|---|---|---|
| $Q \approx 200\ \mathrm{MeV}$ | energia rozszczepienia ²³⁵U | łącznie z rozpadami fragmentów |
| $Q = (m_U + m_n - \sum m_{\text{prod}})c^2$ | energia z mas | — |
| $N(t) \approx N_0k^{t/t_g}$ | wzrost liczby neutronów | $t_g$ — czas pokolenia |
| $P = R\cdot Q$ | moc reaktora | $R$ — rozszczepienia na sekundę |

## Przykład rozwiązany

**Zadanie 1.** Oblicz $Q$ reakcji $^{235}\mathrm U + n \to {}^{141}\mathrm{Ba} + {}^{92}\mathrm{Kr} + 3n$. Masy: ²³⁵U 235,043930 u, ¹⁴¹Ba 140,914411 u, ⁹²Kr 91,926156 u, n 1,008665 u.

$\Delta m = 235{,}043930 + 1{,}008665 - 140{,}914411 - 91{,}926156 - 3\cdot1{,}008665 \approx 0{,}1860\ \mathrm u$, czyli $Q \approx 173\ \mathrm{MeV}$.

**Zadanie 2.** Ile energii daje rozszczepienie 1 kg ²³⁵U? Ile ton węgla (29 MJ/kg) trzeba spalić, żeby uzyskać tyle samo?

$N = \dfrac{1000}{235}N_A \approx 2{,}56\cdot10^{24}$, $E = N\cdot200\ \mathrm{MeV} \approx 8{,}2\cdot10^{13}\ \mathrm J$. Równowartość ok. 2800 t węgla.

**Zadanie 3.** Reaktor ma moc cieplną 3 GW. Ile rozszczepień na sekundę zachodzi i ile ²³⁵U zużywa na dobę?

$R = 3\cdot10^9/(200\cdot1{,}6\cdot10^{-13}) \approx 9{,}4\cdot10^{19}\ \mathrm{s^{-1}}$. Na dobę ok. 3,2 kg ²³⁵U.

## Typowe pułapki

- **W elektrowni jądrowej może dojść do wybuchu jak w bombie.** Paliwo z 3–5% ²³⁵U nie może osiągnąć szybkiej reakcji nadkrytycznej. Broń wymaga ok. 90%. Awarie (Czarnobyl, Fukushima) to przegrzanie, pożary i wybuchy wodoru lub pary, a nie wybuch jądrowy.
- **Moderator pochłania neutrony.** Moderator je spowalnia. Pochłaniają pręty sterujące.
- **Każdy izotop uranu się rozszczepia.** ²³⁸U neutronami termicznymi nie, za to wychwytuje je i po dwóch rozpadach β tworzy pluton-239.
- **Większość energii unoszą neutrony.** Ok. 80% mają fragmenty rozszczepienia.

## Doświadczenie / symulacja

**Symulacja PhET:** *Rozszczepienie jądra* (*Nuclear Fission*) — pojedyncze rozszczepienie, reakcja łańcuchowa, reaktor z prętami sterującymi ([phet.colorado.edu/pl](https://phet.colorado.edu/pl/)).

**Model z pułapkami na myszy.** Klasyczny pokaz: pułapki na myszy z piłeczkami pingpongowymi w zamkniętym pudle. Jedna wrzucona piłka wywołuje lawinę. To dobra ilustracja $k > 1$.

**Python:** bilans energii rozszczepienia, porównanie paliw i model reakcji łańcuchowej dla różnych $k$.

```python
import numpy as np
import matplotlib.pyplot as plt

uc2, NA, e = 931.494, 6.02214076e23, 1.602176634e-19
Q = (235.043930 + 1.008665 - 140.914411 - 91.926156 - 3*1.008665)*uc2
print(f"Q(Ba + Kr + 3n) = {Q:.1f} MeV (z rozpadami fragmentów ok. 200 MeV)")
E1kg = 1000/235*NA*200e6*e
print(f"1 kg U-235: {E1kg:.2e} J = {E1kg/29e6/1e3:.0f} t węgla = {E1kg/3.6e12:.1f} GWh ciepła")
R = 3e9/(200e6*e)
print(f"reaktor 3 GW: {R:.2e} rozszczepień/s, {R*86400*235/NA/1e3:.2f} kg U-235 na dobę")

tg = 1e-4                                          # czas pokolenia neutronów (s), z neutronami opóźnionymi znacznie dłuższy
t = np.linspace(0, 0.05, 300)
for k in (0.999, 1.0, 1.001, 1.01):
    plt.plot(t*1e3, k**(t/tg), label=f"k = {k}")
plt.yscale("log"); plt.xlabel("t [ms]"); plt.ylabel("N / N0"); plt.legend(); plt.grid(True, which="both"); plt.show()
```

## Zadania

### A. Poziom maturalny

1. Uzupełnij reakcję: $^{235}_{92}\mathrm U + {}^1_0n \to {}^{140}_{54}\mathrm{Xe} + {}^{94}_{?}\mathrm{Sr} + ?\,{}^1_0n$.

<details>
<summary>Odpowiedź</summary>

Sr ma $Z = 38$. Nukleony: $236 = 140 + 94 + x$, więc $x = 2$ neutrony.
</details>

2. Do czego służy w reaktorze moderator, a do czego pręty sterujące?

<details>
<summary>Odpowiedź</summary>

Moderator spowalnia neutrony, zwiększając prawdopodobieństwo rozszczepienia ²³⁵U. Pręty pochłaniają neutrony i regulują współczynnik mnożenia.
</details>

3. Elektrownia o mocy elektrycznej 1 GW ma sprawność 33%. Ile uranu-235 zużywa w ciągu roku?

<details>
<summary>Odpowiedź</summary>

Moc cieplna 3 GW, czyli ok. 3,2 kg na dobę, ok. 1,15 t rocznie (w ok. 25–30 t paliwa wzbogaconego).
</details>

### B. Poziom akademicki _(opcjonalnie — rozszerzenie z rachunkiem)_

1. Czas pokolenia neutronów w reaktorze bez neutronów opóźnionych to ok. $10^{-4}$ s. Ile razy wzrośnie moc w ciągu 1 s przy $k = 1{,}001$? A z neutronami opóźnionymi (efektywny czas pokolenia ok. 0,1 s)?

<details>
<summary>Odpowiedź</summary>

Bez opóźnionych: $1{,}001^{10^4} \approx e^{10} \approx 2{,}2\cdot10^4$ razy. Z opóźnionymi: $1{,}001^{10} \approx 1{,}01$, czyli o 1%. Dzięki temu reaktor da się sterować mechanicznie.
</details>

2. Neutron o energii 2 MeV zderza się sprężyście czołowo z protonem (wodór w wodzie) i z jądrem węgla-12 (grafit). Jaką część energii traci w jednym zderzeniu? Ile czołowych zderzeń z węglem trzeba, żeby zejść do 0,025 eV?

<details>
<summary>Odpowiedź</summary>

W zderzeniu czołowym zostaje ułamek $\left(\dfrac{A - 1}{A + 1}\right)^2$ energii (05.03). Dla wodoru 0 (całą energię traci), dla węgla $(11/13)^2 \approx 0{,}716$. Zderzeń: $\dfrac{\ln(2\cdot10^6/0{,}025)}{\ln(1/0{,}716)} \approx 55$ czołowych. Uśredniając po kątach, w praktyce ok. 115 zderzeń.
</details>

## Źródła

- OpenStax, *Fizyka dla szkół wyższych*, t. 3, rozdz. 10 — §10.5: rozszczepienie jądra.
- Halliday, Resnick, Walker, *Podstawy fizyki* — wyd. 2015: t. 5, §43.1–43.3; wyd. 1: t. 5, §44.1–44.5.
- Symulacja PhET *Rozszczepienie jądra*.
