# 17.05 — Soczewki cienkie i równanie soczewki

> **Moduł:** [17 — Optyka geometryczna](README.md) · **Poziom:** 🟢 matura R · **Status:** ✅ pełny
>
> **Czytaj:**
>
> - OpenStax, *Fizyka dla szkół wyższych*, t. 3, rozdz. 2: [§2.3–2.4](https://openstax.org/books/fizyka-dla-szk%C3%B3%C5%82-wy%C5%BCszych-tom-3/pages/2-3-obrazy-tworzone-przez-zalamanie-promieni-swiatla) · [wstęp do rozdziału](https://openstax.org/books/fizyka-dla-szk%C3%B3%C5%82-wy%C5%BCszych-tom-3/pages/2-wstep)
> - Halliday, Resnick, Walker, *Podstawy fizyki*, wyd. 2015, t. 4: §34.3–34.4 (s. 62), §34.6 (s. 80)
> - Halliday, Resnick, Walker, *Podstawy fizyki*, wyd. 1 (2003), t. 4: [§35.5–35.6, s. 51](https://home.agh.edu.pl/~czapli/Resnick_4.pdf#page=66), [§35.8, s. 64](https://home.agh.edu.pl/~czapli/Resnick_4.pdf#page=79) — PDF z serwera AGH

← [Zwierciadła płaskie i sferyczne](04-zwierciadla.md) · [spis modułu](README.md) · [Oko, aparat, lupa, mikroskop i luneta](06-przyrzady-optyczne.md) →

## Po co to jest

Soczewki tworzą obraz w oku, okularach, aparacie fotograficznym, projektorze, mikroskopie i lunecie. Z dwóch wzorów, równania soczewki i wzoru szlifierzy, można obliczyć, gdzie powstanie obraz, jak duży będzie i jaką moc (w dioptriach) muszą mieć okulary. To najczęstszy temat optyki na maturze rozszerzonej.

## Teoria w pigułce

**Soczewka cienka** to soczewka, której grubość jest mała w porównaniu z promieniami krzywizny i odległościami przedmiotu i obrazu.
- **Skupiająca** (grubsza w środku, w powietrzu) skupia promienie równoległe w ognisku rzeczywistym. Ma $f > 0$.
- **Rozpraszająca** (cieńsza w środku) rozprasza je tak, jakby wychodziły z ogniska pozornego. Ma $f < 0$.

**Wzór szlifierzy soczewek** (soczewka o współczynniku $n$ w powietrzu):

$$\frac1f = (n - 1)\left(\frac1{R_1} - \frac1{R_2}\right).$$

$R > 0$ dla powierzchni wypukłej od strony padającego światła, $R < 0$ dla wklęsłej. Dla soczewki dwuwypukłej $R_1 > 0$ i $R_2 < 0$. W wodzie ogniskowa soczewki rośnie, bo zamiast $n - 1$ jest $n/n_{\text{ośr}} - 1$.

**Zdolność skupiająca** w dioptriach: $Z = 1/f$ (f w metrach). Soczewki stykające się dodają zdolności skupiające: $Z = Z_1 + Z_2$.

**Równanie soczewki** i powiększenie (ta sama postać co dla zwierciadła, 17.04):

$$\frac1f = \frac1x + \frac1y, \qquad m = -\frac yx.$$

Tutaj $y > 0$ oznacza obraz rzeczywisty **po drugiej stronie** soczewki, a $y < 0$ obraz pozorny po tej samej stronie co przedmiot.

**Promienie konstrukcyjne:**
1. równoległy do osi po przejściu przez soczewkę biegnie przez ognisko po drugiej stronie;
2. przechodzący przez środek soczewki nie zmienia kierunku;
3. przechodzący przez ognisko przed soczewką wychodzi równolegle do osi.

**Obrazy w soczewce skupiającej** przypominają te w zwierciadle wklęsłym:
- $x > 2f$: obraz rzeczywisty, pomniejszony (aparat, oko);
- $f < x < 2f$: rzeczywisty, powiększony (projektor);
- $x < f$: pozorny, prosty, powiększony (lupa).

Soczewka rozpraszająca daje zawsze obraz pozorny, prosty i pomniejszony.

**Wady soczewek:** aberracja sferyczna (17.04), chromatyczna (17.03), astygmatyzm i dystorsja. Obiektywy składa się z wielu soczewek, żeby je skorygować.

## Wzory i założenia

| Wzór | Znaczenie | Kiedy obowiązuje |
|---|---|---|
| $1/f = (n - 1)(1/R_1 - 1/R_2)$ | wzór szlifierzy | soczewka cienka w powietrzu |
| $1/f = 1/x + 1/y$ | równanie soczewki | promienie przyosiowe |
| $m = -y/x$ | powiększenie poprzeczne | — |
| $Z = 1/f$ [D] | zdolność skupiająca | $f$ w metrach |
| $Z = Z_1 + Z_2$ | soczewki stykające się | cienkie |

## Przykład rozwiązany

**Zadanie 1.** Soczewka dwuwypukła ze szkła $n = 1{,}5$ ma promienie krzywizny po 20 cm. Oblicz ogniskową i zdolność skupiającą.

$\dfrac1f = 0{,}5\left(\dfrac1{0{,}2} + \dfrac1{0{,}2}\right) = 5\ \mathrm D$, więc $f = 20\ \mathrm{cm}$.

**Zadanie 2.** Przedmiot stoi przed soczewką skupiającą o ogniskowej 10 cm w odległości 30 cm, 15 cm i 5 cm. Opisz obrazy.

| $x$ | $y$ | $m$ | Obraz |
|---|---|---|---|
| 30 cm | 15 cm | $-0{,}5$ | rzeczywisty, odwrócony, pomniejszony |
| 15 cm | 30 cm | $-2$ | rzeczywisty, odwrócony, powiększony |
| 5 cm | $-10$ cm | $+2$ | pozorny, prosty, powiększony (lupa) |

## Typowe pułapki

- **Soczewka dwuwypukła zawsze skupia.** W ośrodku o większym współczynniku załamania niż szkło (np. pęcherzyk powietrza w wodzie ma kształt dwuwypukły, a rozprasza) działa odwrotnie.
- **Znaki $R_1$ i $R_2$.** Ustal konwencję i sprawdzaj wynik: dla soczewki dwuwypukłej obie powierzchnie zwiększają zdolność skupiającą.
- **Zasłonięcie połowy soczewki zabiera pół obrazu.** Obraz jest cały, tylko ciemniejszy. Każdy fragment soczewki tworzy cały obraz.
- **Dioptrie i ogniskowa w centymetrach.** $Z = 1/f$ wymaga metrów: $f = 25\ \mathrm{cm}$ to 4 D.
- **Obraz pozorny w soczewce po drugiej stronie.** Obraz pozorny jest po tej samej stronie co przedmiot.

## Doświadczenie / symulacja

**Ogniskowa i równanie soczewki.** Lupa lub soczewka z okularów do czytania, świeczka (albo latarka z kartką z narysowaną strzałką) i ekran z kartonu. Dla kilku odległości przedmiotu znajdź ostry obraz i zmierz $y$. Narysuj $1/y$ od $1/x$: punkty powinny leżeć na prostej $1/y = 1/f - 1/x$. Z przecięcia z osią wyznacz $f$.

**Soczewka z kropli wody.** Kropla wody na folii nad tekstem działa jak lupa. Mniejsza kropla ma mniejszy promień krzywizny i silniej powiększa. Tak budował mikroskopy Leeuwenhoek.

**Symulacja PhET:** *Optyka geometryczna* (*Geometric Optics*) — zmieniaj krzywiznę, współczynnik załamania i średnicę soczewki.

**Python:** śledzenie promieni przez soczewkę cienką (macierze ABCD) i porównanie z równaniem soczewki.

```python
import numpy as np

def przelot(d):        # swobodny bieg o odległość d
    return np.array([[1, d], [0, 1]])

def soczewka(f):       # soczewka cienka
    return np.array([[1, 0], [-1/f, 1]])

f, x = 10.0, 15.0
y = 1/(1/f - 1/x)
M = przelot(y) @ soczewka(f) @ przelot(x)
print(f"x = {x} cm → y = {y:.1f} cm, m = {-y/x:.2f}")
print(f"macierz układu przedmiot→obraz:\n{np.round(M, 6)}  (B = 0 ⇒ obraz ostry, A = m)")
for kat in (-0.1, 0.0, 0.1):                    # trzy promienie z wierzchołka przedmiotu (h = 1 cm)
    out = M @ np.array([1.0, kat])
    print(f"promień o kącie {kat:+.1f} rad trafia w h' = {out[0]:.3f} cm")

n, R1, R2 = 1.5, 0.2, -0.2
print(f"wzór szlifierzy: f = {1/((n - 1)*(1/R1 - 1/R2))*100:.1f} cm")
```

## Zadania

### A. Poziom maturalny

1. Soczewka ma zdolność skupiającą +2,5 D. Jaka jest jej ogniskowa? Jaki obraz da dla przedmiotu w odległości 1 m?

<details>
<summary>Odpowiedź</summary>

$f = 40\ \mathrm{cm}$. $y = 1/(2{,}5 - 1) \approx 0{,}67\ \mathrm m$, $m \approx -0{,}67$: rzeczywisty, odwrócony, pomniejszony.
</details>

2. Projektor ma obiektyw o ogniskowej 10 cm, a ekran stoi 5 m od niego. Gdzie musi być slajd i jakie jest powiększenie?

<details>
<summary>Odpowiedź</summary>

$1/x = 1/0{,}1 - 1/5 \Rightarrow x \approx 10{,}2\ \mathrm{cm}$, $m = -5/0{,}102 \approx -49$. Slajd wkłada się do góry nogami.
</details>

3. Soczewka rozpraszająca ma ogniskową $-20\ \mathrm{cm}$. Przedmiot stoi 20 cm przed nią. Opisz obraz.

<details>
<summary>Odpowiedź</summary>

$1/y = -1/20 - 1/20 \Rightarrow y = -10\ \mathrm{cm}$, $m = 0{,}5$: pozorny, prosty, pomniejszony.
</details>

4. Dwie soczewki +3 D i −1 D przyłożono do siebie. Jaka jest ogniskowa układu?

<details>
<summary>Odpowiedź</summary>

$Z = 2\ \mathrm D$, $f = 50\ \mathrm{cm}$.
</details>

### B. Poziom akademicki _(opcjonalnie — rozszerzenie z rachunkiem)_

1. Szklana soczewka ($n = 1{,}5$) ma w powietrzu ogniskową 20 cm. Jaką ma ogniskową w wodzie ($n = 1{,}33$)?

<details>
<summary>Odpowiedź</summary>

$\dfrac{f_w}{f_p} = \dfrac{n - 1}{n/n_w - 1} = \dfrac{0{,}5}{0{,}128} \approx 3{,}9$, więc $f_w \approx 78\ \mathrm{cm}$. Dlatego pod wodą bez maski widzimy nieostro: rogówka prawie traci zdolność skupiającą.
</details>

2. Pokaż, że najmniejsza odległość między przedmiotem a jego rzeczywistym obrazem w soczewce skupiającej wynosi $4f$.

<details>
<summary>Odpowiedź</summary>

$D = x + y = x + \dfrac{xf}{x - f}$. $dD/dx = 1 - \dfrac{f^2}{(x - f)^2} = 0 \Rightarrow x = 2f$, $D_{\min} = 4f$.
</details>

3. Metoda Bessela: przedmiot i ekran są odległe o $D > 4f$. Ostry obraz uzyskuje się dla dwóch położeń soczewki odległych o $d$. Pokaż, że $f = \dfrac{D^2 - d^2}{4D}$.

<details>
<summary>Odpowiedź</summary>

$x + y = D$ i $1/x + 1/y = 1/f$ dają $x^2 - Dx + Df = 0$, z pierwiastkami $x_{1,2} = \dfrac{D \pm\sqrt{D^2 - 4Df}}{2}$. Różnica $d = \sqrt{D^2 - 4Df}$, stąd $f = (D^2 - d^2)/(4D)$. Metoda nie wymaga znajomości położenia środka soczewki.
</details>

### C. Zadania z arkuszy maturalnych CKE

Zadania z egzaminów maturalnych (poziom rozszerzony, formuła 2023), w których ten temat jest potrzebny. Rozwiąż je samodzielnie, a potem porównaj z zasadami oceniania. Pełne zestawienie: [matura/README.md](../../matura/README.md).

- Maj 2024, zad. 9.1 — szerokość wiązki po przejściu przez układ dwóch soczewek ([arkusz](https://cke.gov.pl/images/_EGZAMIN_MATURALNY_OD_2023/Arkusze_egzaminacyjne/2024/Fizyka/MFAP-R0-100-A-2405-arkusz.pdf), [zasady oceniania](https://cke.gov.pl/egzamin-maturalny/egzamin-maturalny-w-formule-2023/arkusze/2024-2/))
- Maj 2024, zad. 9.2 — położenie soczewki skupiającej i bieg promieni w układzie soczewek ([arkusz](https://cke.gov.pl/images/_EGZAMIN_MATURALNY_OD_2023/Arkusze_egzaminacyjne/2024/Fizyka/MFAP-R0-100-A-2405-arkusz.pdf), [zasady oceniania](https://cke.gov.pl/egzamin-maturalny/egzamin-maturalny-w-formule-2023/arkusze/2024-2/))
- Maj 2025, zad. 7.1 — soczewki: równanie soczewki, ogniskowa ([arkusz](https://www.oke.poznan.pl/files/cms/875/mfap_r0_100_a_2505_arkusz.pdf), [zasady oceniania](https://cke.gov.pl/egzamin-maturalny/egzamin-maturalny-w-formule-2023/arkusze/2025-2/))
- Maj 2025, zad. 7.2 — konstrukcja obrazu w soczewce, obliczenia ([arkusz](https://www.oke.poznan.pl/files/cms/875/mfap_r0_100_a_2505_arkusz.pdf), [zasady oceniania](https://cke.gov.pl/egzamin-maturalny/egzamin-maturalny-w-formule-2023/arkusze/2025-2/))

## Źródła

- OpenStax, *Fizyka dla szkół wyższych*, t. 3, rozdz. 2 — §2.3 (załamanie na powierzchni sferycznej) i §2.4 (soczewki cienkie).
- Halliday, Resnick, Walker, *Podstawy fizyki* — wyd. 2015: t. 4, §34.3–34.4, §34.6; wyd. 1: t. 4, §35.5–35.6, §35.8.
- Symulacja PhET *Optyka geometryczna*.
