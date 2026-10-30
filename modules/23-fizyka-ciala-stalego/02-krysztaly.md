# 23.02 — Struktura krystaliczna ciał stałych

> **Moduł:** [23 — Fizyka ciała stałego](README.md) · **Poziom:** 🔵 studia · **Status:** ✅ pełny
>
> **Czytaj:**
>
> - OpenStax, *Fizyka dla szkół wyższych*, t. 3, rozdz. 9: [§9.3](https://openstax.org/books/fizyka-dla-szk%C3%B3%C5%82-wy%C5%BCszych-tom-3/pages/9-3-wiazania-w-cialach-stalych) · [wstęp do rozdziału](https://openstax.org/books/fizyka-dla-szk%C3%B3%C5%82-wy%C5%BCszych-tom-3/pages/9-wstep)
> - Halliday, Resnick, Walker, *Podstawy fizyki*, wyd. 2015, t. 5: §41.1 (s. 130)
> - Halliday, Resnick, Walker, *Podstawy fizyki*, wyd. 1 (2003), t. 5: [§42.1–42.3, s. 104](https://home.agh.edu.pl/~czapli/Resnick_5.pdf#page=120) — PDF z serwera AGH

← [Wiązania chemiczne i widma cząsteczkowe](01-wiazania-i-czasteczki.md) · [spis modułu](README.md) · [Model elektronów swobodnych w metalach](03-elektrony-swobodne.md) →

## Po co to jest

W ciałach krystalicznych atomy układają się w regularną, powtarzającą się sieć. Od jej typu zależą gęstość, twardość, kowalność, sposób pękania i przewodnictwo metali i półprzewodników. Krystalografia rentgenowska (18.07) odczytuje tę strukturę bezpośrednio. Znajomość podstawowych sieci (regularna prosta, przestrzennie i ściennie centrowana, heksagonalna) pozwala obliczać gęstość z odległości międzyatomowych, energię sieci i rozumieć, czym różnią się stal, krzem i sól.

## Teoria w pigułce

**Sieć krystaliczna** to regularny układ punktów w przestrzeni. **Komórka elementarna** to najmniejszy fragment, którego powtarzanie odtwarza kryształ. Ma krawędź (stałą sieci) $a$.

**Podstawowe sieci regularne (sześcienne):**

| Sieć | Atomy na komórkę | Liczba najbliższych sąsiadów | Wypełnienie przestrzeni | Przykłady |
|---|---|---|---|---|
| prosta (sc) | 1 | 6 | 52% | polon |
| przestrzennie centrowana (bcc) | 2 | 8 | 68% | żelazo α, sód, wolfram |
| ściennie centrowana (fcc) | 4 | 12 | 74% | miedź, aluminium, złoto |

Atomy w narożach liczą się po $1/8$ (każdy należy do 8 komórek), na ścianach po $1/2$, w środku w całości. Sieć **heksagonalna gęsto upakowana** (magnez, cynk, tytan) też ma wypełnienie 74%. Metale fcc są zwykle bardziej plastyczne niż bcc.

**Gęstość z budowy sieci:**

$$\rho = \frac{nM}{N_Aa^3},$$

gdzie $n$ to liczba atomów (lub jednostek wzoru) w komórce, $M$ masa molowa.

**Kryształy jonowe.** NaCl to dwie przenikające się sieci fcc (Na⁺ i Cl⁻). Każdy jon ma 6 najbliższych sąsiadów przeciwnego znaku, a komórka zawiera 4 pary NaCl. Energia sieci (na parę jonów) uwzględnia przyciąganie i odpychanie ze wszystkimi jonami w krysztale:

$$U = -\alpha\frac{ke^2}{r_0}\left(1 - \frac1n\right),$$

gdzie $\alpha$ to **stała Madelunga** (dla NaCl 1,7476) zawierająca sumę po wszystkich jonach, a $n$ wykładnik odpychania (ok. 9).

**Kryształy kowalencyjne.** Diament i krzem tworzą sieć diamentu: każdy atom ma 4 sąsiadów w narożach czworościanu (wiązania sp³). Są twarde i mają wysoką temperaturę topnienia.

**Defekty** (wakanse, atomy międzywęzłowe, domieszki, dyslokacje, granice ziaren) w dużym stopniu decydują o właściwościach. Dyslokacje umożliwiają plastyczność metali, a domieszki sterują przewodnictwem półprzewodników (23.05).

**Ciała bezpostaciowe** (szkło, wiele polimerów) nie mają uporządkowania dalekiego zasięgu. Miękną stopniowo, zamiast topnieć w określonej temperaturze.

## Wzory i założenia

| Wzór | Znaczenie | Kiedy obowiązuje |
|---|---|---|
| $\rho = nM/(N_Aa^3)$ | gęstość z sieci | sieć regularna |
| $n$ = 1 (sc), 2 (bcc), 4 (fcc), 8 (diament) | atomy na komórkę | — |
| odległość sąsiadów: $a$ (sc), $a\sqrt3/2$ (bcc), $a/\sqrt2$ (fcc) | — | — |
| $U = -\alpha ke^2(1 - 1/n)/r_0$ | energia sieci jonowej | na parę jonów |
| $2d\sin\theta = m\lambda$ | dyfrakcja Bragga | pomiar $a$ (18.07) |

## Przykład rozwiązany

### Wersja z rachunkiem różniczkowym i całkowym

**Zadanie 1.** Oblicz gęstość NaCl ($a = 0{,}564\ \mathrm{nm}$, 4 pary na komórkę, $M = 58{,}44\ \mathrm{g/mol}$) i miedzi (fcc, $a = 0{,}3615\ \mathrm{nm}$, $M = 63{,}55\ \mathrm{g/mol}$).

NaCl: $\rho = \dfrac{4\cdot0{,}05844}{6{,}022\cdot10^{23}\cdot(0{,}564\cdot10^{-9})^3} \approx 2160\ \mathrm{kg/m^3}$ (tablice: 2165).

Cu: $\rho \approx 8940\ \mathrm{kg/m^3}$ (tablice: 8960).

**Zadanie 2.** Oblicz energię sieci NaCl ($r_0 = 0{,}282\ \mathrm{nm}$, $\alpha = 1{,}7476$, $n = 9$) w eV na parę i kJ/mol.

$U = 1{,}7476\cdot\dfrac{1{,}44\ \mathrm{eV\cdot nm}}{0{,}282\ \mathrm{nm}}\cdot\dfrac89 \approx 7{,}9\ \mathrm{eV}$ na parę, czyli ok. 765 kJ/mol (zmierzone: 787 kJ/mol).

**Stała Madelunga jako suma.** Dla łańcucha jonów na prostej ($+-+-\dots$) co odległość $r_0$:

$$\alpha = 2\left(1 - \frac12 + \frac13 - \frac14 + \dots\right) = 2\ln2 \approx 1{,}386.$$

W trzech wymiarach szereg jest warunkowo zbieżny i trzeba go sumować sprytnie (metoda Ewalda), co daje 1,7476.

## Typowe pułapki

- **Każdy atom w narożu należy do komórki w całości.** Narożny liczy się jako 1/8, ścienny jako 1/2.
- **Stała sieci = odległość najbliższych sąsiadów.** Tylko w sieci prostej. W fcc najbliżsi sąsiedzi są w odległości $a/\sqrt2$.
- **Energia sieci jonowej $ke^2/r_0$.** Trzeba uwzględnić oddziaływania ze wszystkimi jonami (stała Madelunga) i odpychanie.
- **Szkło to ciecz, która płynie przez wieki.** Szkło jest ciałem stałym bezpostaciowym. Grubsze dolne części starych szyb to efekt produkcji, a nie spływania.

## Doświadczenie / symulacja

**Model fcc z kulek.** Ułóż kulki (plastelina, piłeczki) w warstwy o upakowaniu heksagonalnym. Kolejne warstwy w układzie ABCABC dają fcc, a ABAB heksagonalną gęsto upakowaną. Policz sąsiadów kulki w środku.

**Kryształy z roztworu.** Wyhoduj kryształy soli kuchennej, ałunu lub cukru z przesyconego roztworu. Porównaj kształty: sześciany, ośmiościany, słupki.

**Python:** gęstość z parametrów sieci i stała Madelunga dla łańcucha jonów oraz sieci NaCl (sumowanie po rosnących sześcianach).

```python
import numpy as np

NA = 6.02214076e23
for nazwa, n, M, a in [("NaCl", 4, 58.44, 0.564), ("Cu (fcc)", 4, 63.55, 0.3615),
                       ("Fe (bcc)", 2, 55.845, 0.2866), ("Si (diament)", 8, 28.086, 0.5431)]:
    print(f"{nazwa:12s}: ρ = {n*M*1e-3/(NA*(a*1e-9)**3):7.0f} kg/m³")

N = np.arange(1, 200001)
print(f"łańcuch jonów: α = {2*np.sum((-1)**(N + 1)/N):.4f} (2 ln 2 = {2*np.log(2):.4f})")

def madelung_NaCl(L):                                # sumowanie Evjena: ładunki brzegowe z wagami 1/2, 1/4, 1/8
    s = 0.0
    r = np.arange(-L, L + 1)
    i, j, k = np.meshgrid(r, r, r, indexing="ij")
    d = np.sqrt(i**2 + j**2 + k**2)
    w = np.ones_like(d, dtype=float)
    for ax in (i, j, k):
        w = w*np.where(np.abs(ax) == L, 0.5, 1.0)
    mask = d > 0
    return -np.sum(w[mask]*(-1.0)**(i + j + k)[mask]/d[mask])
for L in (2, 4, 8):
    print(f"NaCl, sześcian ±{L}: α = {madelung_NaCl(L):.4f} (dokładnie 1,7476)")
U = 1.7476*1.43996/0.282*(1 - 1/9)
print(f"energia sieci NaCl: {U:.2f} eV na parę = {U*1.602e-19*NA/1e3:.0f} kJ/mol")
```

## Zadania

### A. Poziom maturalny _(opcjonalnie — rozgrzewka)_

1. Ile atomów przypada na komórkę elementarną sieci bcc i fcc?

<details>
<summary>Odpowiedź</summary>

bcc: $8\cdot\tfrac18 + 1 = 2$. fcc: $8\cdot\tfrac18 + 6\cdot\tfrac12 = 4$.
</details>

2. Dlaczego kryształy soli kuchennej mają kształt sześcianów?

<details>
<summary>Odpowiedź</summary>

Sieć NaCl jest regularna (sześcienna), a kryształ rośnie, zachowując symetrię sieci.
</details>

### B. Poziom akademicki

1. Oblicz wypełnienie przestrzeni w sieci bcc, przyjmując, że atomy stykają się wzdłuż przekątnej sześcianu.

<details>
<summary>Odpowiedź</summary>

$4R = a\sqrt3$. Objętość 2 atomów: $2\cdot\tfrac43\pi R^3 = \tfrac{\pi\sqrt3}{8}a^3$, czyli $\pi\sqrt3/8 \approx 0{,}68$.
</details>

2. Żelazo ma sieć bcc o stałej 0,2866 nm. Oblicz gęstość i odległość najbliższych sąsiadów.

<details>
<summary>Odpowiedź</summary>

$\rho \approx 7880\ \mathrm{kg/m^3}$ (tablice: 7874). Odległość sąsiadów $a\sqrt3/2 \approx 0{,}248\ \mathrm{nm}$.
</details>

3. Krzem ma sieć diamentu (8 atomów w komórce), $a = 0{,}5431\ \mathrm{nm}$. Oblicz liczbę atomów w 1 m³ i gęstość.

<details>
<summary>Odpowiedź</summary>

$8/a^3 \approx 5{,}0\cdot10^{28}\ \mathrm{m^{-3}}$, $\rho \approx 2330\ \mathrm{kg/m^3}$.
</details>

## Źródła

- OpenStax, *Fizyka dla szkół wyższych*, t. 3, rozdz. 9 — §9.3: wiązania w kryształach.
- Halliday, Resnick, Walker, *Podstawy fizyki* — wyd. 2015: t. 5, §41.1; wyd. 1: t. 5, §42.1–42.3.
