# 19.03 — Transformacja Lorentza i składanie prędkości

> **Moduł:** [19 — Szczególna teoria względności](README.md) · **Poziom:** 🔵 studia · **Status:** ✅ pełny
>
> **Czytaj:**
>
> - OpenStax, *Fizyka dla szkół wyższych*, t. 3, rozdz. 5: [§5.5–5.6](https://openstax.org/books/fizyka-dla-szk%C3%B3%C5%82-wy%C5%BCszych-tom-3/pages/5-5-transformacja-lorentza) · [wstęp do rozdziału](https://openstax.org/books/fizyka-dla-szk%C3%B3%C5%82-wy%C5%BCszych-tom-3/pages/5-wstep)
> - Halliday, Resnick, Walker, *Podstawy fizyki*, wyd. 2015, t. 4: §37.3–37.4 (s. 204)
> - Halliday, Resnick, Walker, *Podstawy fizyki*, wyd. 1 (2003), t. 4: [§38.7–38.9, s. 160](https://home.agh.edu.pl/~czapli/Resnick_4.pdf#page=175) — PDF z serwera AGH

← [Dylatacja czasu i skrócenie długości](02-dylatacja-i-skrocenie.md) · [spis modułu](README.md) · [Relatywistyczny efekt Dopplera](04-relatywistyczny-doppler.md) →

## Po co to jest

Transformacja Lorentza to „słownik” tłumaczący współrzędne zdarzenia z jednego układu inercjalnego na drugi. Z niej w kilku linijkach wynikają dylatacja czasu, skrócenie długości, względność równoczesności i relatywistyczne dodawanie prędkości, które nie pozwala przekroczyć prędkości światła. Wielkością niezmienną jest interwał czasoprzestrzenny. To wejście do geometrii czasoprzestrzeni Minkowskiego, a dalej do ogólnej teorii względności i fizyki cząstek.

## Teoria w pigułce

**Transformacja Lorentza.** Układ $S'$ porusza się względem $S$ z prędkością $v$ wzdłuż osi $x$, a w chwili $t = t' = 0$ początki się pokrywają:

$$x' = \gamma(x - vt), \qquad t' = \gamma\left(t - \frac{vx}{c^2}\right), \qquad y' = y, \quad z' = z.$$

Transformacja odwrotna ma tę samą postać z $-v$. Dla $v \ll c$ przechodzi w transformację Galileusza $x' = x - vt$, $t' = t$.

**Wnioski:**
- **Względność równoczesności:** zdarzenia równoczesne w $S$ ($\Delta t = 0$) w różnych miejscach mają w $S'$ różnicę czasów $\Delta t' = -\gamma v\Delta x/c^2$.
- **Dylatacja czasu:** zegar w spoczynku w $S'$ ($\Delta x' = 0$): $\Delta t = \gamma\Delta t'$.
- **Skrócenie długości:** końce pręta spoczywającego w $S'$ mierzone w $S$ jednocześnie ($\Delta t = 0$): $\Delta x' = \gamma\Delta x$, czyli $L = L_0/\gamma$.

**Relatywistyczne dodawanie prędkości.** Ciało porusza się w $S'$ z prędkością $u'$ wzdłuż $x$. W układzie $S$:

$$u = \frac{u' + v}{1 + u'v/c^2}.$$

Dla $u' = c$ wychodzi $u = c$ przy dowolnym $v$. Złożenie prędkości mniejszych od $c$ daje zawsze prędkość mniejszą od $c$.

**Interwał czasoprzestrzenny** jest taki sam we wszystkich układach inercjalnych:

$$s^2 = (c\Delta t)^2 - \Delta x^2 - \Delta y^2 - \Delta z^2.$$

- $s^2 > 0$ (**czasowy**): istnieje układ, w którym zdarzenia zachodzą w tym samym miejscu. Kolejność jest absolutna i zdarzenia mogą być przyczynowo powiązane. $s/c$ to czas własny.
- $s^2 < 0$ (**przestrzenny**): żaden sygnał nie zdąży między zdarzeniami. Kolejność zależy od układu.
- $s^2 = 0$ (**zerowy**, świetlny): zdarzenia połączone promieniem światła.

**Diagram Minkowskiego** ($ct$ na osi pionowej, $x$ na poziomej) pokazuje linie świata ciał. Światło biegnie pod kątem $45^\circ$, a stożek świetlny oddziela przyszłość i przeszłość zdarzenia od obszaru „gdzie indziej”.

## Wzory i założenia

| Wzór | Znaczenie | Kiedy obowiązuje |
|---|---|---|
| $x' = \gamma(x - vt)$, $t' = \gamma(t - vx/c^2)$ | transformacja Lorentza | ruch wzdłuż $x$, wspólny początek |
| $u = (u' + v)/(1 + u'v/c^2)$ | dodawanie prędkości | prędkości równoległe |
| $s^2 = c^2\Delta t^2 - \Delta x^2 - \Delta y^2 - \Delta z^2$ | interwał (niezmiennik) | — |
| $\Delta\tau = s/c$ | czas własny | $s^2 > 0$ |

## Przykład rozwiązany

### Wersja z rachunkiem różniczkowym i całkowym

**Zadanie 1.** Dwie rakiety oddalają się od Ziemi w przeciwnych kierunkach, każda z prędkością $0{,}8c$. Z jaką prędkością jedna porusza się względem drugiej?

$u = \dfrac{0{,}8 + 0{,}8}{1 + 0{,}64}c \approx 0{,}976c$ (a nie $1{,}6c$).

**Zadanie 2.** Wyprowadź wzór na dodawanie prędkości z transformacji Lorentza.

Różniczkując odwrotną transformację $x = \gamma(x' + vt')$, $t = \gamma(t' + vx'/c^2)$:

$$u = \frac{dx}{dt} = \frac{\gamma(dx' + v\,dt')}{\gamma(dt' + v\,dx'/c^2)} = \frac{u' + v}{1 + u'v/c^2}.$$

**Zadanie 3.** Zdarzenie A: $(t, x) = (0, 0)$. Zdarzenie B: $t = 2\ \mu\mathrm s$, $x = 900\ \mathrm m$. Oblicz interwał. Czy A może być przyczyną B? Jaki czas własny upływa dla ciała, które przeszło z A do B ze stałą prędkością?

$c\Delta t = 600\ \mathrm m < 900\ \mathrm m$, więc $s^2 = 600^2 - 900^2 < 0$. Interwał jest przestrzenny. Żaden sygnał nie zdąży z A do B, więc A nie może być przyczyną B. Takiego ciała nie ma, bo musiałoby poruszać się szybciej od światła.

## Typowe pułapki

- **Prędkości dodaje się zwyczajnie.** Przy prędkościach bliskich $c$ trzeba użyć wzoru relatywistycznego.
- **W transformacji czasu pomija się wyraz $vx/c^2$.** Ten wyraz odpowiada za względność równoczesności i jest kluczowy.
- **Interwał zależy od układu.** Interwał jest niezmiennikiem, a $\Delta t$ i $\Delta x$ osobno się zmieniają.
- **Prędkość względna dwóch ciał widzianych z Ziemi może przekroczyć $c$.** Odległość między nimi może rosnąć szybciej niż $c$ (np. $1{,}6c$ w zadaniu 1), ale prędkość jednego w układzie drugiego jest mniejsza od $c$.

## Doświadczenie / symulacja

**Diagram Minkowskiego w Pythonie.** Narysuj osie układu $S'$ na diagramie $S$: oś $ct'$ to linia $x = vt$, a oś $x'$ to linia $ct = (v/c)x$. Zaznacz dwa zdarzenia równoczesne w $S$ i sprawdź, że w $S'$ nie są równoczesne (kod niżej).

**Python:** transformacja Lorentza zdarzeń, niezmienniczość interwału i diagram Minkowskiego.

```python
import numpy as np
import matplotlib.pyplot as plt

c = 1.0                                          # jednostki: c = 1 (czas w µs·c, czyli w 300 m)
def lorentz(t, x, v):
    g = 1/np.sqrt(1 - v**2)
    return g*(t - v*x), g*(x - v*t)

v = 0.6
zdarzenia = {"A": (0.0, 0.0), "B": (0.0, 2.0), "C": (3.0, 1.0)}
for nazwa, (t, x) in zdarzenia.items():
    t2, x2 = lorentz(t, x, v)
    print(f"{nazwa}: S (t, x) = ({t:.2f}, {x:.2f}) → S' = ({t2:.2f}, {x2:.2f}), s² = {t**2 - x**2:.2f} = {t2**2 - x2**2:.2f}")
print(f"0,8c ⊕ 0,8c = {(0.8 + 0.8)/(1 + 0.8*0.8):.3f} c")

fig, ax = plt.subplots(figsize=(5, 5))
s = np.linspace(-1, 4, 2)
ax.plot(s, s, "y--", label="światło"); ax.plot(-s, s, "y--")
ax.plot(v*s, s, "r", label="oś ct′"); ax.plot(s, v*s, "b", label="oś x′")
for nazwa, (t, x) in zdarzenia.items():
    ax.plot(x, t, "ko"); ax.annotate(nazwa, (x + 0.05, t + 0.05))
ax.set_xlabel("x"); ax.set_ylabel("ct"); ax.set_aspect("equal"); ax.legend(); ax.grid(True); plt.show()
```

## Zadania

### A. Poziom maturalny _(opcjonalnie — rozgrzewka)_

1. Rakieta lecąca z prędkością $0{,}5c$ wystrzeliwuje do przodu pocisk z prędkością $0{,}5c$ względem siebie. Jaka jest prędkość pocisku względem Ziemi?

<details>
<summary>Odpowiedź</summary>

$0{,}8c$.
</details>

2. Dlaczego żadne ciało nie może osiągnąć prędkości światła, choćby dodawać mu kolejne przyrosty prędkości?

<details>
<summary>Odpowiedź</summary>

Z relatywistycznego wzoru złożenie dowolnych prędkości mniejszych od $c$ daje prędkość mniejszą od $c$. Do tego energia potrzebna do rozpędzenia rośnie do nieskończoności przy $v \to c$ (19.05).
</details>

### B. Poziom akademicki

1. Pokaż, że interwał $c^2t^2 - x^2$ jest niezmienniczy względem transformacji Lorentza.

<details>
<summary>Odpowiedź</summary>

$c^2t'^2 - x'^2 = \gamma^2[(ct - vx/c)^2 - (x - vt)^2] = \gamma^2(c^2t^2 + v^2x^2/c^2 - x^2 - v^2t^2) = \gamma^2(1 - v^2/c^2)(c^2t^2 - x^2) = c^2t^2 - x^2$.
</details>

2. W układzie $S$ dwa zdarzenia zachodzą w odległości 600 m i odstępie 1 μs. Czy istnieje układ, w którym są równoczesne? Jeśli tak, z jaką prędkością się porusza?

<details>
<summary>Odpowiedź</summary>

$c\Delta t = 300\ \mathrm m < 600\ \mathrm m$, interwał przestrzenny, więc taki układ istnieje. $\Delta t' = 0 \Rightarrow v = c^2\Delta t/\Delta x = c\cdot300/600 = 0{,}5c$.
</details>

3. Pokaż, że $\gamma$ można zapisać jako $\cosh\phi$, a $v/c$ jako $\tanh\phi$ (szybkość, rapidity), i że przy składaniu prędkości szybkości się dodają.

<details>
<summary>Odpowiedź</summary>

Z $\tanh(\phi_1 + \phi_2) = \dfrac{\tanh\phi_1 + \tanh\phi_2}{1 + \tanh\phi_1\tanh\phi_2}$, czyli dokładnie wzór na dodawanie prędkości. $\gamma = 1/\sqrt{1 - \tanh^2\phi} = \cosh\phi$. Transformacja Lorentza to „obrót hiperboliczny” o kąt $\phi$.
</details>

## Źródła

- OpenStax, *Fizyka dla szkół wyższych*, t. 3, rozdz. 5 — §5.5 (transformacja Lorentza) i §5.6 (relatywistyczne składanie prędkości).
- Halliday, Resnick, Walker, *Podstawy fizyki* — wyd. 2015: t. 4, §37.3–37.4; wyd. 1: t. 4, §38.7–38.9.
