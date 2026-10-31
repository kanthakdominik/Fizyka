# 17.06 — Oko, aparat, lupa, mikroskop i luneta

> **Moduł:** [17 — Optyka geometryczna](README.md) · **Poziom:** 🟢 matura R · **Status:** ✅ pełny
>
> **Czytaj:**
>
> - OpenStax, *Fizyka dla szkół wyższych*, t. 3, rozdz. 2: [§2.5–2.8](https://openstax.org/books/fizyka-dla-szk%C3%B3%C5%82-wy%C5%BCszych-tom-3/pages/2-5-oko) · [wstęp do rozdziału](https://openstax.org/books/fizyka-dla-szk%C3%B3%C5%82-wy%C5%BCszych-tom-3/pages/2-wstep)
> - Halliday, Resnick, Walker, *Podstawy fizyki*, wyd. 2015, t. 4: §34.5 (s. 75)
> - Halliday, Resnick, Walker, *Podstawy fizyki*, wyd. 1 (2003), t. 4: [§35.7, s. 60](https://home.agh.edu.pl/~czapli/Resnick_4.pdf#page=75) — PDF z serwera AGH

← [Soczewki cienkie i równanie soczewki](05-soczewki.md) · [spis modułu](README.md) · (koniec modułu) →

## Po co to jest

Oko jest najważniejszym przyrządem optycznym, a okulary i soczewki kontaktowe korygują jego wady u większości ludzi. Lupa, mikroskop i luneta zwiększają kąt, pod jakim widzimy przedmiot, i otwierają światy zbyt małe lub zbyt odległe dla gołego oka. Aparat fotograficzny ma tę samą budowę co oko. Znajomość tych układów pozwala zrozumieć recepty okulistyczne, dobór obiektywu, powiększenie lornetki i ograniczenia przyrządów.

## Teoria w pigułce

**Oko.** Rogówka i soczewka (razem ok. +60 D) tworzą na siatkówce rzeczywisty, odwrócony, pomniejszony obraz. **Akomodacja** to zmiana ogniskowej soczewki przez mięśnie rzęskowe. Zdrowe oko ostro widzi od **punktu bliży** (ok. 25 cm, tzw. odległość dobrego widzenia $d = 25\ \mathrm{cm}$) do **punktu dali** (nieskończoność).

**Wady wzroku i korekcja:**
- **Krótkowzroczność**: gałka za długa, obraz dalekich przedmiotów powstaje przed siatkówką, punkt dali jest blisko. Korekcja soczewką rozpraszającą, która daje obraz nieskończoności w punkcie dali: $Z = -1/d_{\text{dali}}$.
- **Nadwzroczność**: obraz bliskich przedmiotów powstaje za siatkówką, punkt bliży jest daleko. Korekcja soczewką skupiającą, która daje obraz przedmiotu z 25 cm w punkcie bliży: $Z = \dfrac1{0{,}25} - \dfrac1{d_{\text{bliży}}}$.
- **Starczowzroczność**: soczewka traci elastyczność i punkt bliży oddala się z wiekiem. Stąd okulary do czytania.
- **Astygmatyzm**: rogówka ma różną krzywiznę w różnych kierunkach. Korekcja soczewką cylindryczną.

**Powiększenie kątowe.** Wielkość przedmiotu, jaką widzimy, zależy od kąta, pod jakim go widać. Przyrządy powiększają ten kąt: $M = \theta'/\theta$.

**Lupa** to soczewka skupiająca o krótkiej ogniskowej. Przedmiot w ognisku daje obraz w nieskończoności (oko nie męczy się akomodacją):

$$M = \frac df, \qquad d = 25\ \mathrm{cm}.$$

**Mikroskop.** Obiektyw (bardzo krótka ogniskowa $f_{ob}$) tworzy powiększony obraz rzeczywisty. Okular działa jak lupa i ogląda ten obraz. Przy długości optycznej tubusu $L$ (odległość między ogniskami, zwykle 160 mm):

$$M \approx \frac{L}{f_{ob}}\cdot\frac{d}{f_{ok}}.$$

Najmniejszy szczegół ogranicza dyfrakcja (18), czyli ok. 0,2 μm dla światła widzialnego. Daje to sens powiększeniom do ok. 1000–1500×.

**Luneta (teleskop soczewkowy Keplera).** Obiektyw o długiej ogniskowej tworzy obraz odległego przedmiotu w swoim ognisku, a okular go ogląda:

$$M = \frac{f_{ob}}{f_{ok}}, \qquad \text{długość} \approx f_{ob} + f_{ok}.$$

Obraz jest odwrócony. Lornetki prostują go pryzmatami. Średnica obiektywu decyduje o ilości zebranego światła ($\propto D^2$) i o zdolności rozdzielczej. Dlatego teleskopy buduje się coraz większe.

**Aparat fotograficzny** to obiektyw i matryca. Liczba przysłony $f/D$ decyduje o jasności obrazu ($\propto (D/f)^2$) i głębi ostrości.

## Wzory i założenia

| Wzór | Znaczenie | Kiedy obowiązuje |
|---|---|---|
| $Z = -1/d_{\text{dali}}$ | korekcja krótkowzroczności | okulary blisko oka |
| $Z = 1/0{,}25 - 1/d_{\text{bliży}}$ | korekcja nadwzroczności | j.w., $d$ w metrach |
| $M = d/f$ | lupa | obraz w nieskończoności, $d = 25\ \mathrm{cm}$ |
| $M \approx (L/f_{ob})(d/f_{ok})$ | mikroskop | $L \gg f_{ob}$, $f_{ok}$ |
| $M = f_{ob}/f_{ok}$ | luneta Keplera | przedmiot w nieskończoności |

## Przykład rozwiązany

**Zadanie 1.** Krótkowidz widzi ostro tylko do 50 cm. Jakie okulary mu pomogą? Dalekowidz ma punkt bliży w odległości 1 m. Jakie okulary pozwolą mu czytać z 25 cm?

Krótkowidz: $Z = -1/0{,}5 = -2\ \mathrm D$.

Dalekowidz: soczewka ma dać obraz przedmiotu z 25 cm w odległości 1 m (pozorny, $y = -1\ \mathrm m$): $Z = \dfrac1{0{,}25} + \dfrac1{-1} = +3\ \mathrm D$.

**Zadanie 2.** Mikroskop ma obiektyw o ogniskowej 4 mm, okular o ogniskowej 25 mm i tubus 160 mm. Oblicz powiększenie. Luneta ma obiektyw 900 mm i okular 10 mm. Pod jakim kątem widać przez nią Księżyc?

Mikroskop: $M = (160/4)\cdot(250/25) = 40\cdot10 = 400\times$.

Luneta: $M = 90\times$. Księżyc ma średnicę kątową ok. $0{,}52^\circ$, a w lunecie ok. $47^\circ$, czyli prawie całe pole widzenia okularu.

## Typowe pułapki

- **Powiększenie lunety to powiększenie wielkości.** To powiększenie **kątowe**. Odległe przedmioty nie dają się „powiększyć” liniowo.
- **Większe powiększenie mikroskopu pokaże więcej szczegółów.** Powyżej ok. 1000–1500× powiększa się tylko rozmycie dyfrakcyjne (powiększenie puste).
- **Krótkowidz potrzebuje soczewek skupiających.** Potrzebuje rozpraszających (minusy), bo jego oko skupia za mocno.
- **Dioptrie w recepcie a ogniskowa w cm.** −2 D to $f = -50\ \mathrm{cm}$.
- **Teleskop powiększa, więc większy teleskop to większe powiększenie.** Średnica obiektywu decyduje o jasności i rozdzielczości. Powiększenie zmienia się wymianą okularu.

## Doświadczenie / symulacja

**Luneta z dwóch soczewek.** Soczewka z okularów do czytania (+2 D, $f = 50\ \mathrm{cm}$) jako obiektyw i lupa ($f \approx 5\ \mathrm{cm}$) jako okular, ustawione w odległości ok. 55 cm (w tubie z kartonu). Powiększenie ok. 10×, obraz odwrócony. Sprawdź powiększenie, porównując widziany przez lunetę i gołym okiem rozmiar odległego okna.

**Punkt bliży.** Przybliżaj tekst do oka, aż przestanie być ostry, i zmierz odległość. Porównaj wyniki osób w różnym wieku.

**Symulacja PhET:** *Optyka geometryczna* (*Geometric Optics*) — złożenie dwóch soczewek.

**Python:** dobór okularów i powiększenia przyrządów, a także obraz w lunecie z równania soczewki dla dwóch soczewek.

```python
import numpy as np

def korekcja(dali=None, blizy=None):
    if dali is not None:
        return -1/dali
    return 1/0.25 - 1/blizy

print(f"krótkowidz (daleko 0,5 m): {korekcja(dali=0.5):+.1f} D")
print(f"dalekowidz (blisko 1 m): {korekcja(blizy=1.0):+.1f} D")
print(f"lupa f = 5 cm: M = {25/5:.0f}×; mikroskop: M = {160/4*250/25:.0f}×; luneta 900/10: M = {900/10:.0f}×")

# luneta krok po kroku: przedmiot bardzo daleko, obiektyw f1, okular f2, odstęp f1 + f2
f1, f2 = 90.0, 1.0                           # cm
x1 = 1e9
y1 = 1/(1/f1 - 1/x1)                         # obraz pośredni ≈ w ognisku obiektywu
x2 = (f1 + f2) - y1
print(f"obraz pośredni {y1:.3f} cm za obiektywem, {x2:.3f} cm przed okularem (= f2: obraz końcowy w ∞)")
ksiezyc = np.degrees(3474/384400)
print(f"Księżyc: {ksiezyc:.2f}° gołym okiem, {ksiezyc*f1/f2:.0f}° w lunecie")
```

## Zadania

### A. Poziom maturalny

1. Osoba ma punkt dali w odległości 2 m. Jakie okulary należy jej przepisać?

<details>
<summary>Odpowiedź</summary>

$-0{,}5\ \mathrm D$.
</details>

2. Lupa ma zdolność skupiającą +10 D. Jakie daje powiększenie (obraz w nieskończoności)?

<details>
<summary>Odpowiedź</summary>

$f = 10\ \mathrm{cm}$, $M = 25/10 = 2{,}5\times$.
</details>

3. Lornetka ma oznaczenie 10×50. Co oznaczają te liczby? Ile razy więcej światła zbiera niż oko o źrenicy 5 mm?

<details>
<summary>Odpowiedź</summary>

Powiększenie 10× i średnica obiektywu 50 mm. Zbiera $(50/5)^2 = 100$ razy więcej światła.
</details>

4. Mikroskop ma obiektyw 40× i okular 10×. Jakie jest powiększenie całkowite?

<details>
<summary>Odpowiedź</summary>

400×.
</details>

### B. Poziom akademicki _(opcjonalnie — rozszerzenie z rachunkiem)_

1. Pokaż, że gdy obraz w lupie powstaje w punkcie bliży (25 cm), a nie w nieskończoności, powiększenie wynosi $M = 1 + d/f$.

<details>
<summary>Odpowiedź</summary>

$y = -d$, więc $x = \dfrac{df}{d + f}$. Kąt widzenia $h/x$ porównany z $h/d$: $M = d/x = 1 + d/f$.
</details>

2. Pokaż z równania soczewki, że przejście od patrzenia w dal do patrzenia z odległości 25 cm wymaga zwiększenia zdolności skupiającej oka o 4 D, niezależnie od budowy oka. Ile wynosi zakres akomodacji, jeśli punkt bliży to 1 m?

<details>
<summary>Odpowiedź</summary>

$Z = 1/x + 1/y$, a odległość siatkówki od soczewki ($y$) się nie zmienia. Dla $x \to \infty$: $Z_\infty = 1/y$, dla $x = 0{,}25\ \mathrm m$: $Z = 4 + 1/y$. Różnica 4 D. Przy punkcie bliży 1 m zakres akomodacji to tylko 1 D, dlatego potrzebne są okulary +3 D do czytania (przykład 1).
</details>

3. Ostatnią soczewkę obiektywu mikroskopu i preparat zanurza się w olejku o $n = 1{,}52$. Apertura numeryczna to $\mathrm{NA} = n\sin\alpha$. Najmniejszy rozróżnialny szczegół to $d \approx 0{,}61\lambda/\mathrm{NA}$. Oblicz $d$ dla $\alpha = 67^\circ$ i $\lambda = 550\ \mathrm{nm}$ z olejkiem i w powietrzu.

<details>
<summary>Odpowiedź</summary>

Z olejkiem $\mathrm{NA} = 1{,}52\cdot0{,}92 = 1{,}40$, $d \approx 240\ \mathrm{nm}$. W powietrzu $\mathrm{NA} = 0{,}92$, $d \approx 365\ \mathrm{nm}$.
</details>

### C. Zadania z arkuszy maturalnych CKE

Zadania z egzaminów maturalnych (poziom rozszerzony, formuła 2023), w których ten temat jest potrzebny. Rozwiąż je samodzielnie, a potem porównaj z zasadami oceniania. Pełne zestawienie: [matura/README.md](../../matura/README.md).

- Maj 2024, zad. 9.1 — szerokość wiązki po przejściu przez układ dwóch soczewek (temat pomocniczy) ([arkusz](https://cke.gov.pl/images/_EGZAMIN_MATURALNY_OD_2023/Arkusze_egzaminacyjne/2024/Fizyka/MFAP-R0-100-A-2405-arkusz.pdf), [zasady oceniania](https://cke.gov.pl/egzamin-maturalny/egzamin-maturalny-w-formule-2023/arkusze/2024-2/))

## Źródła

- OpenStax, *Fizyka dla szkół wyższych*, t. 3, rozdz. 2 — §2.5 (oko), §2.6 (aparat fotograficzny), §2.7 (lupa), §2.8 (mikroskopy i teleskopy).
- Halliday, Resnick, Walker, *Podstawy fizyki* — wyd. 2015: t. 4, §34.5; wyd. 1: t. 4, §35.7.
- Symulacja PhET *Optyka geometryczna*.
