# 17.04 — Zwierciadła płaskie i sferyczne

> **Moduł:** [17 — Optyka geometryczna](README.md) · **Poziom:** 🟢 matura R · **Status:** ✅ pełny
>
> **Czytaj:**
>
> - OpenStax, *Fizyka dla szkół wyższych*, t. 3, rozdz. 2: [§2.1–2.2](https://openstax.org/books/fizyka-dla-szk%C3%B3%C5%82-wy%C5%BCszych-tom-3/pages/2-1-obrazy-tworzone-przez-zwierciadla-plaskie) · [wstęp do rozdziału](https://openstax.org/books/fizyka-dla-szk%C3%B3%C5%82-wy%C5%BCszych-tom-3/pages/2-wstep)
> - Halliday, Resnick, Walker, *Podstawy fizyki*, wyd. 2015, t. 4: §34.1–34.2 (s. 49)
> - Halliday, Resnick, Walker, *Podstawy fizyki*, wyd. 1 (2003), t. 4: [§35.1–35.4, s. 41](https://home.agh.edu.pl/~czapli/Resnick_4.pdf#page=56) — PDF z serwera AGH

← [Rozszczepienie światła i pryzmat](03-dyspersja.md) · [spis modułu](README.md) · [Soczewki cienkie i równanie soczewki](05-soczewki.md) →

## Po co to jest

Zwierciadła kuliste skupiają lub rozpraszają światło. Wklęsłe stosuje się w reflektorach samochodów, latarkach, lusterkach kosmetycznych, piekarnikach słonecznych i największych teleskopach świata. Wypukłe stoją na skrzyżowaniach i w lusterkach bocznych samochodów („obiekty w lusterku są bliżej, niż się wydaje”). Równanie zwierciadła ma tę samą postać co równanie soczewki (17.05), więc metoda konstrukcji obrazów przyda się w całym module.

## Teoria w pigułce

**Zwierciadło kuliste** to fragment sfery o promieniu $R$. Promienie równoległe do osi i bliskie niej (**przyosiowe**) po odbiciu przechodzą przez **ognisko** $F$ w odległości

$$f = \frac R2.$$

W zwierciadle wklęsłym ognisko jest rzeczywiste (przed lustrem), a w wypukłym pozorne (za lustrem). Wtedy przyjmujemy $f < 0$.

**Promienie konstrukcyjne:**
1. równoległy do osi po odbiciu przechodzi przez ognisko (lub jego przedłużenie, w wypukłym);
2. przechodzący przez ognisko po odbiciu biegnie równolegle do osi;
3. padający na wierzchołek odbija się symetrycznie względem osi;
4. przechodzący przez środek krzywizny wraca po tej samej drodze.

**Równanie zwierciadła** i powiększenie:

$$\frac1f = \frac1x + \frac1y, \qquad m = \frac{h'}{h} = -\frac yx.$$

- $x$ to odległość przedmiotu, $y$ odległość obrazu.
- $y > 0$ oznacza obraz rzeczywisty (przed lustrem), $y < 0$ pozorny (za lustrem).
- $m < 0$ oznacza obraz odwrócony, $\lvert m\rvert > 1$ powiększony.

**Obrazy w zwierciadle wklęsłym:**

| Położenie przedmiotu | Obraz |
|---|---|
| $x > 2f$ | rzeczywisty, odwrócony, pomniejszony |
| $x = 2f$ | rzeczywisty, odwrócony, tej samej wielkości |
| $f < x < 2f$ | rzeczywisty, odwrócony, powiększony |
| $x = f$ | brak obrazu (promienie równoległe), tak działa reflektor |
| $x < f$ | pozorny, prosty, powiększony (lusterko kosmetyczne) |

Zwierciadło wypukłe zawsze daje obraz pozorny, prosty i pomniejszony, ale ma szerokie pole widzenia.

**Aberracja sferyczna.** Promienie dalekie od osi skupiają się bliżej lustra niż przyosiowe. Zwierciadło **paraboliczne** skupia wszystkie promienie równoległe w jednym punkcie, dlatego anteny satelitarne i teleskopy mają kształt paraboloidy.

## Wzory i założenia

| Wzór | Znaczenie | Kiedy obowiązuje |
|---|---|---|
| $f = R/2$ | ogniskowa | promienie przyosiowe |
| $1/f = 1/x + 1/y$ | równanie zwierciadła | $f < 0$ dla wypukłego, $y < 0$ dla obrazu pozornego |
| $m = -y/x$ | powiększenie | — |

## Przykład rozwiązany

**Zadanie 1.** Przedmiot stoi 30 cm przed zwierciadłem wklęsłym o promieniu 40 cm. Gdzie powstaje obraz i jaki jest?

$f = 20\ \mathrm{cm}$, $\dfrac1y = \dfrac1{20} - \dfrac1{30} \Rightarrow y = 60\ \mathrm{cm}$, $m = -2$. Obraz jest rzeczywisty, odwrócony, dwukrotnie powiększony, 60 cm przed lustrem.

**Zadanie 2.** Lusterko boczne samochodu jest wypukłe, $f = -0{,}5\ \mathrm m$. Samochód jest 10 m za nim. Gdzie widać obraz i jak duży?

$\dfrac1y = -2 - 0{,}1 \Rightarrow y \approx -0{,}48\ \mathrm m$, $m \approx 0{,}048$. Obraz jest pozorny, prosty, ponad 20 razy pomniejszony. Mózg ocenia odległość po wielkości, więc auto wydaje się dalej, niż jest.

## Typowe pułapki

- **Znaki.** Trzymaj się jednej konwencji: $f < 0$ dla wypukłego, $y < 0$ dla obrazu pozornego.
- **Ogniskowa = promień.** $f = R/2$.
- **Obraz pozorny można zobaczyć na ekranie.** Na ekranie można uzyskać tylko obraz rzeczywisty.
- **Zwierciadło wypukłe powiększa.** Zawsze pomniejsza.
- **Wzory dla dużych zwierciadeł szerokokątnych.** Wzór $1/f = 1/x + 1/y$ dotyczy promieni przyosiowych.

## Doświadczenie / symulacja

**Ogniskowa łyżki.** Wypolerowana łyżka to zwierciadło wklęsłe (od wewnątrz) i wypukłe (od zewnątrz). Sprawdź, że z bliska w wewnętrznej stronie twarz jest prosta i powiększona, a z daleka odwrócona.

**Ogniskowa lusterka kosmetycznego.** Skieruj lusterko na Słońce (lub na odległe okno) i znajdź na kartce odległość, w której obraz jest najostrzejszy. To ogniskowa. Uwaga: skupione światło słoneczne może zapalić papier.

**Symulacja PhET:** *Optyka geometryczna* (*Geometric Optics*) — soczewki i zwierciadła, promienie konstrukcyjne ([phet.colorado.edu/pl](https://phet.colorado.edu/pl/)).

**Python:** położenie i powiększenie obrazu w funkcji odległości przedmiotu oraz aberracja sferyczna.

```python
import numpy as np
import matplotlib.pyplot as plt

def obraz(f, x):
    y = 1/(1/f - 1/x)
    return y, -y/x

for f, x in [(20, 30), (20, 10), (20, 60), (-50, 1000)]:
    y, m = obraz(f, x)
    print(f"f = {f:4} cm, x = {x:4} cm: y = {y:7.1f} cm, m = {m:+.3f}, "
          f"{'rzeczywisty' if y > 0 else 'pozorny'}, {'odwrócony' if m < 0 else 'prosty'}")

R = 40.0                                         # aberracja sferyczna: gdzie promień na wysokości h przecina oś
h = np.linspace(0.1, 15, 100)
th = np.arcsin(h/R)
F_h = R - R/(2*np.cos(th))                       # odległość przecięcia od wierzchołka
print(f"przyosiowo F = {F_h[0]:.2f} cm, dla h = 15 cm F = {F_h[-1]:.2f} cm")
plt.plot(h, F_h); plt.axhline(R/2, ls="--", color="gray")
plt.xlabel("wysokość promienia h [cm]"); plt.ylabel("punkt przecięcia osi [cm]"); plt.grid(True); plt.show()
```

## Zadania

### A. Poziom maturalny

1. Przedmiot stoi 10 cm przed zwierciadłem wklęsłym o ogniskowej 20 cm. Opisz obraz.

<details>
<summary>Odpowiedź</summary>

$y = -20\ \mathrm{cm}$, $m = 2$: pozorny, prosty, dwukrotnie powiększony.
</details>

2. Gdzie umieścić żarówkę w reflektorze, żeby wiązka była równoległa?

<details>
<summary>Odpowiedź</summary>

W ognisku zwierciadła.
</details>

3. Zwierciadło wklęsłe daje rzeczywisty obraz trzykrotnie powiększony w odległości 60 cm. Oblicz odległość przedmiotu i ogniskową.

<details>
<summary>Odpowiedź</summary>

$x = y/3 = 20\ \mathrm{cm}$, $1/f = 1/20 + 1/60 \Rightarrow f = 15\ \mathrm{cm}$.
</details>

### B. Poziom akademicki _(opcjonalnie — rozszerzenie z rachunkiem)_

1. Wyprowadź z geometrii, że promień równoległy do osi na wysokości $h$ przecina oś w odległości $R - \dfrac{R}{2\cos\theta}$ od wierzchołka, gdzie $\sin\theta = h/R$. Pokaż, że dla małych $h$ daje to $R/2$.

<details>
<summary>Odpowiedź</summary>

Promień pada pod kątem $\theta$ do promienia sfery i odbija się symetrycznie. Trójkąt środek–punkt odbicia–przecięcie z osią jest równoramienny, więc odległość środka od przecięcia wynosi $R/(2\cos\theta)$. Dla małych $\theta$: $\cos\theta \approx 1$, odległość od wierzchołka $R/2$.
</details>

2. Pokaż, że parabola $y = x^2/(4f)$ skupia wszystkie promienie równoległe do osi w punkcie $(0, f)$.

<details>
<summary>Odpowiedź</summary>

Odległość punktu paraboli od ogniska równa się odległości od kierownicy $y = -f$, więc droga każdego promienia od czoła fali do ogniska jest taka sama i wszystkie docierają w fazie. Rachunek: nachylenie stycznej $x/(2f)$ daje kąt padania, a odbity promień przechodzi przez $(0, f)$.
</details>

3. Przedmiot zbliża się do zwierciadła wklęsłego ($f = 20\ \mathrm{cm}$) ze stałą prędkością 1 cm/s. Z jaką prędkością porusza się obraz, gdy $x = 30\ \mathrm{cm}$?

<details>
<summary>Odpowiedź</summary>

Różniczkując $1/x + 1/y = 1/f$: $\dot y = -\dfrac{y^2}{x^2}\dot x = -4\dot x$. Obraz oddala się z prędkością 4 cm/s.
</details>

## Źródła

- OpenStax, *Fizyka dla szkół wyższych*, t. 3, rozdz. 2 — §2.1 (obrazy w zwierciadłach płaskich) i §2.2 (zwierciadła kuliste).
- Halliday, Resnick, Walker, *Podstawy fizyki* — wyd. 2015: t. 4, §34.1–34.2; wyd. 1: t. 4, §35.1–35.4.
- Symulacja PhET *Optyka geometryczna*.
