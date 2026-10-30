# 17.03 — Rozszczepienie światła i pryzmat

> **Moduł:** [17 — Optyka geometryczna](README.md) · **Poziom:** 🟢 matura R · **Status:** ✅ pełny
>
> **Czytaj:**
>
> - OpenStax, *Fizyka dla szkół wyższych*, t. 3, rozdz. 1: [§1.5](https://openstax.org/books/fizyka-dla-szk%C3%B3%C5%82-wy%C5%BCszych-tom-3/pages/1-5-rozszczepienie) · [wstęp do rozdziału](https://openstax.org/books/fizyka-dla-szk%C3%B3%C5%82-wy%C5%BCszych-tom-3/pages/1-wstep)
> - Halliday, Resnick, Walker, *Podstawy fizyki*, wyd. 2015, t. 4: §33.5 (s. 23)
> - Halliday, Resnick, Walker, *Podstawy fizyki*, wyd. 1 (2003), t. 4: [§34.7, s. 21](https://home.agh.edu.pl/~czapli/Resnick_4.pdf#page=36) — PDF z serwera AGH

← [Załamanie światła i całkowite wewnętrzne odbicie](02-zalamanie-i-calkowite-odbicie.md) · [spis modułu](README.md) · [Zwierciadła płaskie i sferyczne](04-zwierciadla.md) →

## Po co to jest

Pryzmat rozszczepia białe światło na tęczę barw, bo współczynnik załamania zależy od długości fali. To zjawisko odkrył Newton i dzięki niemu wiemy, że światło białe jest mieszaniną kolorów. Dyspersja tworzy tęczę i błyski diamentu, a w optyce jest kłopotem: soczewki rozmazują kolory (aberracja chromatyczna), a impulsy w światłowodach się rozciągają. Wykorzystuje się ją w spektroskopach, które rozpoznają skład chemiczny gwiazd (21).

## Teoria w pigułce

**Dyspersja** to zależność współczynnika załamania od długości fali, $n(\lambda)$. W przezroczystych materiałach w zakresie widzialnym $n$ rośnie, gdy maleje długość fali (**dyspersja normalna**). Fiolet załamuje się mocniej niż czerwień. Dla szkła typu crown $n$ wynosi ok. 1,513 dla czerwieni i 1,532 dla fioletu.

**Pryzmat** o kącie łamiącym $A$ odchyla promień o kąt $\delta$. Kąt odchylenia jest najmniejszy, gdy promień biegnie symetrycznie przez pryzmat:

$$n = \frac{\sin\frac{A + \delta_{\min}}{2}}{\sin\frac A2}.$$

Ten wzór służy do dokładnego pomiaru $n$. Różne barwy mają różne $\delta$, więc białe światło rozszczepia się na widmo.

**Tęcza.** Światło słoneczne wpada do kulistej kropli wody, załamuje się, odbija od tylnej ścianki i załamuje ponownie przy wyjściu. Kąt między promieniem wychodzącym a kierunkiem przeciwnym do Słońca ma maksimum ok. $42^\circ$ dla czerwieni i ok. $40{,}6^\circ$ dla fioletu. W pobliżu tego kąta skupia się dużo światła. Dlatego tęczę widać jako łuk o promieniu kątowym ok. $42^\circ$ wokół punktu przeciwsłonecznego (cień głowy obserwatora), z czerwienią na zewnątrz. Tęcza wtórna (dwa odbicia w kropli) ma ok. $51^\circ$ i odwróconą kolejność barw.

**Rozpraszanie** to inne zjawisko niż dyspersja, ale też zależy od długości fali. Małe cząsteczki powietrza rozpraszają światło z natężeniem $\propto 1/\lambda^4$ (rozpraszanie Rayleigha). Niebieskie rozprasza się kilka razy silniej niż czerwone, stąd niebieskie niebo i czerwone zachody Słońca.

**Aberracja chromatyczna.** Soczewka ma dla każdej barwy inną ogniskową (17.05). Koryguje się ją achromatami, czyli parami soczewek z dwóch szkieł o różnej dyspersji.

## Wzory i założenia

| Wzór | Znaczenie | Kiedy obowiązuje |
|---|---|---|
| $n = n(\lambda)$, $dn/d\lambda < 0$ | dyspersja normalna | materiały przezroczyste w danym zakresie |
| $n = \sin\frac{A + \delta_{\min}}{2}/\sin\frac A2$ | minimum odchylenia w pryzmacie | przejście symetryczne |
| $\delta \approx (n - 1)A$ | odchylenie w cienkim pryzmacie | małe $A$ i małe kąty padania |
| $I_{\text{rozpr}} \propto 1/\lambda^4$ | rozpraszanie Rayleigha | cząstki $\ll\lambda$ |

## Przykład rozwiązany

**Zadanie.** Pryzmat o kącie $60^\circ$ ze szkła crown ma $n = 1{,}513$ dla czerwieni i $1{,}532$ dla fioletu. Oblicz minimalne kąty odchylenia i szerokość kątową widma.

Z wzoru na minimum odchylenia: $\delta_{\min} = 2\arcsin\left(n\sin30^\circ\right) - 60^\circ$.

Czerwień: $\delta \approx 38{,}3^\circ$. Fiolet: $\delta \approx 40{,}0^\circ$. Widmo ma szerokość ok. $1{,}7^\circ$.

## Typowe pułapki

- **Czerwień załamuje się najmocniej.** Najmocniej załamuje się fiolet, który ma największe $n$.
- **Pryzmat barwi światło.** Pryzmat tylko rozdziela barwy, które już są w świetle białym (doświadczenie Newtona z drugim pryzmatem).
- **Tęcza jest w określonym miejscu nieba.** Każdy obserwator widzi własną tęczę, zawsze $42^\circ$ od swojego punktu przeciwsłonecznego.
- **Dyspersja wyjaśnia niebieskie niebo.** Kolor nieba bierze się z rozpraszania Rayleigha, a nie z dyspersji.

## Doświadczenie / symulacja

**Tęcza z węża ogrodowego.** Stań tyłem do niskiego Słońca i rozpylaj wodę przed sobą. Zmierz kątowy promień łuku (np. ramieniem wyciągniętym w stronę cienia głowy i kątomierzem) i porównaj z $42^\circ$.

**Widmo z płyty CD** to inne zjawisko (siatka dyfrakcyjna, 18), ale warto porównać kolejność barw z widmem z pryzmatu lub szklanki wody.

**Symulacja PhET:** *Załamanie światła* (*Bending Light*), zakładka *Pryzmaty* — włącz białe światło.

**Python:** kąt tęczy z minimum odchylenia w kropli i rozszczepienie w pryzmacie.

```python
import numpy as np
import matplotlib.pyplot as plt

def kat_teczy(n):
    i = np.linspace(1e-4, np.pi/2 - 1e-4, 200000)
    r = np.arcsin(np.sin(i)/n)
    D = np.pi + 2*i - 4*r                                # odchylenie po jednym odbiciu w kropli
    return 180 - np.degrees(D.min())

for kolor, n in [("czerwony 700 nm", 1.331), ("fioletowy 400 nm", 1.343)]:
    print(f"tęcza, {kolor}: {kat_teczy(n):.1f}°")

for kolor, n in [("czerwony", 1.513), ("fioletowy", 1.532)]:
    d = 2*np.degrees(np.arcsin(n*np.sin(np.radians(30)))) - 60
    print(f"pryzmat 60°, {kolor}: δ_min = {d:.2f}°")

lam = np.linspace(400, 700, 100)
plt.plot(lam, (550/lam)**4)
plt.xlabel("λ [nm]"); plt.ylabel("rozpraszanie względem 550 nm"); plt.title("rozpraszanie Rayleigha ~ 1/λ⁴"); plt.grid(True); plt.show()
```

## Zadania

### A. Poziom maturalny

1. Białe światło pada ukośnie na płytkę szklaną o równoległych ściankach. Czy wychodzące światło jest rozszczepione?

<details>
<summary>Odpowiedź</summary>

Wiązki poszczególnych barw wychodzą równolegle do wejściowej (17.02), tylko nieco przesunięte. Przy szerokiej wiązce nakładają się z powrotem i widać światło białe, z kolorowymi brzegami.
</details>

2. Dlaczego tęczę widać tylko wtedy, gdy Słońce jest za plecami i nisko nad horyzontem?

<details>
<summary>Odpowiedź</summary>

Tęcza jest $42^\circ$ od punktu przeciwsłonecznego. Gdy Słońce jest wyżej niż $42^\circ$, punkt przeciwsłoneczny jest tak nisko pod horyzontem, że cały łuk tęczy też jest pod horyzontem.
</details>

3. Ile razy silniej rozpraszane jest światło niebieskie (450 nm) niż czerwone (700 nm)?

<details>
<summary>Odpowiedź</summary>

$(700/450)^4 \approx 5{,}9$ razy.
</details>

### B. Poziom akademicki _(opcjonalnie — rozszerzenie z rachunkiem)_

1. Kąt odchylenia promienia po jednym odbiciu w kropli to $D(i) = 180^\circ + 2i - 4r$, gdzie $\sin i = n\sin r$. Pokaż, że minimum $D$ występuje dla $\cos^2i = \dfrac{n^2 - 1}{3}$, i oblicz kąt tęczy dla $n = 1{,}333$.

<details>
<summary>Odpowiedź</summary>

$dD/di = 2 - 4\,dr/di = 0$, a $dr/di = \dfrac{\cos i}{n\cos r}$. Stąd $n\cos r = 2\cos i$, czyli $n^2(1 - \sin^2i/n^2) = 4\cos^2i$, co daje $\cos^2i = (n^2 - 1)/3$. Dla $n = 1{,}333$: $i \approx 59{,}4^\circ$, $r \approx 40{,}2^\circ$, kąt tęczy $180^\circ - D \approx 42{,}1^\circ$.
</details>

2. Cienki pryzmat ($A = 5^\circ$) ze szkła o $n = 1{,}5$ odchyla promień o ok. $(n - 1)A$. Oblicz odchylenie. Ile wynosi różnica odchyleń czerwieni i fioletu ($\Delta n = 0{,}02$)?

<details>
<summary>Odpowiedź</summary>

$\delta \approx 2{,}5^\circ$, $\Delta\delta \approx 0{,}1^\circ$.
</details>

## Źródła

- OpenStax, *Fizyka dla szkół wyższych*, t. 3, rozdz. 1 — §1.5: rozszczepienie (dyspersja) światła.
- Halliday, Resnick, Walker, *Podstawy fizyki* — wyd. 2015: t. 4, §33.5; wyd. 1: t. 4, §34.7.
- Symulacja PhET *Załamanie światła*.
