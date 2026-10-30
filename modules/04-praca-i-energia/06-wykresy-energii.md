# 04.06 — Wykresy energii potencjalnej i stabilność równowagi

> **Moduł:** [04 — Praca, energia i moc](README.md) · **Poziom:** 🔵 studia · **Status:** ✅ pełny
>
> **Czytaj:**
>
> - OpenStax, *Fizyka dla szkół wyższych*, t. 1, rozdz. 8: [§8.4](https://openstax.org/books/fizyka-dla-szk%C3%B3%C5%82-wy%C5%BCszych-tom-1/pages/8-4-wykresy-energii-potencjalnej) · [wstęp do rozdziału](https://openstax.org/books/fizyka-dla-szk%C3%B3%C5%82-wy%C5%BCszych-tom-1/pages/8-wstep)
> - Halliday, Resnick, Walker, *Podstawy fizyki*, wyd. 2015, t. 1: §8.3 (s. 236)
> - Halliday, Resnick, Walker, *Podstawy fizyki*, wyd. 1 (2003), t. 1: [§8.5, s. 180](https://home.agh.edu.pl/~czapli/Resnick_1.pdf#page=192) — PDF z serwera AGH

← [Zasada zachowania energii mechanicznej i całkowitej](05-zasada-zachowania-energii.md) · [spis modułu](README.md) · (koniec modułu) →

## Po co to jest

Wykres energii potencjalnej $U(x)$ pokazuje cały ruch ciała w jednym rysunku: gdzie ciało może się znaleźć, gdzie zawraca, gdzie jest w równowadze i czy ta równowaga jest trwała. Fizycy używają tego narzędzia wszędzie — od wiązań chemicznych i drgań cząsteczek (23) po studnie potencjału w mechanice kwantowej (20) i stabilność orbit (07).

## Teoria w pigułce

**Ruch na wykresie.** Rysujemy $U(x)$ i poziomą linię całkowitej energii $E$. Ponieważ $E_k = E - U \ge 0$:
- ciało może przebywać tylko tam, gdzie $U(x) \le E$ (**obszar dozwolony**);
- w punktach, gdzie $U(x) = E$, prędkość jest zerowa — to **punkty zwrotu**;
- prędkość w dowolnym punkcie: $v(x) = \sqrt{2(E - U(x))/m}$.

**Siła z nachylenia.** $F = -dU/dx$: na stromym zboczu siła jest duża, siła wskazuje w dół zbocza.

**Położenia równowagi** to punkty, gdzie $dU/dx = 0$ (siła zerowa):
- **trwała** w minimum $U$ ($U'' > 0$): po małym wychyleniu siła wraca ciało;
- **nietrwała** w maksimum $U$ ($U'' < 0$): małe wychylenie rośnie;
- **obojętna** tam, gdzie $U$ jest stałe.

**Małe drgania wokół minimum.** Blisko minimum $x_0$ energię przybliżamy parabolą (00.06):

$$U(x) \approx U(x_0) + \tfrac12U''(x_0)(x - x_0)^2,$$

czyli ciało zachowuje się jak na sprężynie o $k = U''(x_0)$ i drga z częstością $\omega = \sqrt{U''(x_0)/m}$. Dlatego drgania harmoniczne (09) są tak powszechne.

**Ruch ograniczony i nieograniczony.** Jeśli obszar dozwolony jest zamknięty z obu stron, ciało drga między punktami zwrotu (związany elektron, planeta na orbicie eliptycznej). Jeśli z jednej strony jest otwarty, ciało może uciec do nieskończoności (prędkość ucieczki, jonizacja).

## Wzory i założenia

| Wzór | Znaczenie | Kiedy obowiązuje |
|---|---|---|
| $E_k = E - U(x) \ge 0$ | obszar dozwolony | tylko siły zachowawcze |
| $U(x_z) = E$ | punkt zwrotu | — |
| $U'(x_0) = 0$ | położenie równowagi | — |
| $U''(x_0) > 0$ / $< 0$ | równowaga trwała / nietrwała | — |
| $\omega = \sqrt{U''(x_0)/m}$ | częstość małych drgań | małe wychylenia od minimum |
| $U_{LJ} = 4\varepsilon\left[\left(\tfrac{\sigma}{r}\right)^{12} - \left(\tfrac{\sigma}{r}\right)^6\right]$ | potencjał Lennarda-Jonesa | oddziaływanie obojętnych atomów |

## Przykład rozwiązany

### Wersja z rachunkiem różniczkowym i całkowym

**Zadanie.** Cząstka o masie 0,5 kg porusza się wzdłuż osi $x$ w polu o energii potencjalnej $U(x) = x^3 - 3x$ (J, m).

a) Znajdź położenia równowagi i określ ich rodzaj.

$U'(x) = 3x^2 - 3 = 0 \Rightarrow x = \pm1$. $U''(x) = 6x$: dla $x = 1$ — $U'' = 6 > 0$, minimum, równowaga **trwała** ($U = -2\ \mathrm{J}$); dla $x = -1$ — $U'' = -6 < 0$, maksimum, równowaga **nietrwała** ($U = 2\ \mathrm{J}$).

b) Cząstka ma energię $E = 0$ i znajduje się w pobliżu $x = 1$. Między jakimi punktami się porusza?

$x^3 - 3x \le 0$ w okolicy minimum dla $0 \le x \le \sqrt3$. Punkty zwrotu: $x = 0$ i $x = \sqrt3 \approx 1{,}73\ \mathrm{m}$.

c) Jaka jest największa prędkość?

W minimum $E_k = 0 - (-2) = 2\ \mathrm{J}$, $v_{\max} = \sqrt{2\cdot2/0{,}5} \approx 2{,}83\ \mathrm{m/s}$.

d) Jaka jest częstość małych drgań wokół $x = 1$?

$\omega = \sqrt{6/0{,}5} \approx 3{,}46\ \mathrm{rad/s}$, okres $T \approx 1{,}81\ \mathrm{s}$.

e) Jaką energię musiałaby mieć cząstka, żeby uciec do $x \to -\infty$?

Musi przejść przez maksimum w $x = -1$: $E > 2\ \mathrm{J}$.

## Typowe pułapki

- **Ciało stoi tam, gdzie $U$ jest najmniejsze.** Ciało przechodzi przez minimum z największą prędkością; stoi (chwilowo) w punktach zwrotu.
- **Równowaga = $U = 0$.** Równowaga to $U' = 0$; wartość $U$ może być dowolna.
- **Punkt zwrotu = równowaga.** W punkcie zwrotu $v = 0$, ale siła zwykle nie jest zerowa.
- **Małe drgania zawsze harmoniczne.** Tylko w przybliżeniu parabolicznym; dla dużych amplitud okres zależy od amplitudy.

## Doświadczenie / symulacja

**Kulka w misce.** Kulka w kulistej misce (równowaga trwała) i na odwróconej misce (nietrwała) to dosłowny wykres $U(x) = mgh(x)$. Zmierz okres małych drgań kulki stalowej w misce o promieniu krzywizny $R$ i porównaj z $2\pi\sqrt{R/g}$ (dla kulki toczącej się będzie dłuższy — temat 06.04).

**Python:** wykres energii, punkty zwrotu i porównanie okresu dokładnego z przybliżeniem harmonicznym w zależności od energii.

```python
import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import quad
from scipy.optimize import brentq

m = 0.5
U = lambda x: x**3 - 3*x

def period(E):
    """Okres ruchu w studni wokół x = 1 dla energii E (-2 < E < 2)."""
    x1 = brentq(lambda x: U(x) - E, -1, 1)          # lewy punkt zwrotu
    x2 = brentq(lambda x: U(x) - E, 1, 2.5)         # prawy punkt zwrotu
    f = lambda x: 1/np.sqrt(2*(E - U(x))/m)
    return 2*quad(f, x1, x2, limit=200)[0], x1, x2

T_harm = 2*np.pi/np.sqrt(6/m)
for E in (-1.9, -1.0, 0.0, 1.5):
    T, x1, x2 = period(E)
    print(f"E = {E:+.1f} J: zwroty {x1:+.3f} i {x2:.3f} m, T = {T:.3f} s (harmonicznie {T_harm:.3f} s)")

x = np.linspace(-2.2, 2.2, 400)
plt.plot(x, U(x)); plt.axhline(0, ls="--", color="gray", label="E = 0")
plt.ylim(-3, 4); plt.xlabel("x [m]"); plt.ylabel("U [J]"); plt.grid(True); plt.legend(); plt.show()
```

## Zadania

### A. Poziom maturalny _(opcjonalnie — rozgrzewka)_

1. Kulka toczy się bez tarcia po torze w kształcie litery W: dwa dołki na wysokości 0, garb między nimi na wysokości 0,5 m. Startuje z prędkością zerową z wysokości 0,4 m w lewym dołku. Czy przedostanie się do prawego? A gdyby startowała z 0,6 m?

<details>
<summary>Odpowiedź</summary>

Z 0,4 m — nie (za mało energii, żeby pokonać garb); z 0,6 m — tak.
</details>

2. Wskaż na przykładach z życia równowagę trwałą, nietrwałą i obojętną.

<details>
<summary>Odpowiedź</summary>

Trwała: kulka w misce, wahadło w najniższym punkcie. Nietrwała: ołówek postawiony na czubku, kulka na szczycie kopuły. Obojętna: kula na poziomym stole.
</details>

### B. Poziom akademicki

1. Wyznacz odległość równowagi i głębokość studni potencjału Lennarda-Jonesa oraz „sztywność” wiązania $k = U''(r_0)$.

<details>
<summary>Odpowiedź</summary>

$r_0 = 2^{1/6}\sigma$, $U(r_0) = -\varepsilon$, $k = \dfrac{72\varepsilon}{2^{1/3}\sigma^2} \approx 57{,}1\,\dfrac{\varepsilon}{\sigma^2}$.
</details>

2. $U(x) = x^4 - 2x^2$ (J, m), $m = 1\ \mathrm{kg}$. Znajdź położenia równowagi i ich rodzaj. Opisz ruch cząstki o energii $E = -0{,}5\ \mathrm{J}$ i $E = +0{,}5\ \mathrm{J}$.

<details>
<summary>Odpowiedź</summary>

$x = 0$ — nietrwała ($U = 0$), $x = \pm1$ — trwałe ($U = -1$). Dla $E = -0{,}5$ cząstka drga w jednym z dołków; dla $E = 0{,}5$ drga między punktami $x = \pm\sqrt{1 + \sqrt{1{,}5}} \approx \pm1{,}49\ \mathrm{m}$, przechodząc nad garbem.
</details>

3. Dla wahadła $U(\theta) = mgL(1 - \cos\theta)$. Wyznacz częstość małych drgań metodą $\omega = \sqrt{U''/I}$, gdzie dla współrzędnej kątowej rolę masy pełni $I = mL^2$.

<details>
<summary>Odpowiedź</summary>

$U''(0) = mgL$, $\omega = \sqrt{mgL/(mL^2)} = \sqrt{g/L}$.
</details>

4. Cząstka o masie $m$ w polu $U(x) = U_0\left(\dfrac{x}{a}\right)^2$ ma energię $E$. Wyznacz punkty zwrotu i prędkość w punkcie $x = 0$.

<details>
<summary>Odpowiedź</summary>

$x = \pm a\sqrt{E/U_0}$; $v = \sqrt{2E/m}$.
</details>

## Źródła

- OpenStax, *Fizyka dla szkół wyższych*, t. 1, rozdz. 8 — §8.4: wykresy energii potencjalnej i stabilność.
- Halliday, Resnick, Walker, *Podstawy fizyki* — wyd. 2015: t. 1, §8.3; wyd. 1: t. 1, §8.5.
