# 00.01 — Wektory: składowe, iloczyn skalarny i wektorowy

> **Moduł:** [00 — Narzędzia matematyczne fizyka](README.md) · **Poziom:** 🟢🔵 matura R + studia · **Status:** ✅ pełny
>
> **Czytaj:**
>
> - OpenStax, *Fizyka dla szkół wyższych*, t. 1, rozdz. 2: [§2.1–2.4](https://openstax.org/books/fizyka-dla-szk%C3%B3%C5%82-wy%C5%BCszych-tom-1/pages/2-1-skalary-i-wektory) · [wstęp do rozdziału](https://openstax.org/books/fizyka-dla-szk%C3%B3%C5%82-wy%C5%BCszych-tom-1/pages/2-wstep)
> - Halliday, Resnick, Walker, *Podstawy fizyki*, wyd. 2015, t. 1: §3.1–3.3 (s. 52)
> - Halliday, Resnick, Walker, *Podstawy fizyki*, wyd. 1 (2003): [t. 1, rozdz. 3](https://home.agh.edu.pl/~czapli/Resnick_1.pdf) — PDF z serwera AGH

← (początek modułu) · [spis modułu](README.md) · [Funkcje i wykresy w fizyce, linearyzacja](02-funkcje-i-wykresy.md) →

## Po co to jest

Prędkość, przyspieszenie, siła, pęd, natężenie pola — większość wielkości w fizyce ma kierunek. Bez sprawnego rozkładania wektorów na składowe nie rozwiążesz rzutu ukośnego (02), równi pochyłej (03) ani układu ładunków (12). Iloczyn skalarny wraca w pracy i strumieniu pola, iloczyn wektorowy — w momencie siły, momencie pędu i sile Lorentza.

## Teoria w pigułce

**Skalar** to liczba z jednostką (masa, temperatura, energia). **Wektor** ma długość (wartość), kierunek i zwrot. Wektor zapisujemy jako $\vec{a}$, a jego długość jako $a$ albo $\lvert\vec{a}\rvert$.

**Składowe.** W układzie współrzędnych z wersorami $\hat{\imath}, \hat{\jmath}, \hat{k}$ (wektory o długości 1 wzdłuż osi $x, y, z$):

$$\vec{a} = a_x\hat{\imath} + a_y\hat{\jmath} + a_z\hat{k}.$$

Składowa to rzut wektora na oś — liczba ze znakiem. Na płaszczyźnie wektor o długości $a$ tworzący kąt $\theta$ z osią $x$ ma składowe $a_x = a\cos\theta$, $a_y = a\sin\theta$.

**Dodawanie** wektorów to dodawanie składowych. Geometrycznie: reguła równoległoboku albo „ogon do grotu”. Odejmowanie $\vec{a} - \vec{b}$ to dodanie wektora przeciwnego $-\vec{b}$.

**Iloczyn skalarny** daje liczbę i mierzy, „jak bardzo” wektory są równoległe:

$$\vec{a}\cdot\vec{b} = ab\cos\varphi = a_xb_x + a_yb_y + a_zb_z.$$

Gdy wektory są prostopadłe, $\vec{a}\cdot\vec{b} = 0$. Przykład fizyczny: praca $W = \vec{F}\cdot\Delta\vec{r}$ — liczy się tylko składowa siły wzdłuż przemieszczenia.

**Iloczyn wektorowy** daje wektor prostopadły do obu czynników, o długości równej polu równoległoboku rozpiętego na $\vec{a}$ i $\vec{b}$:

$$\lvert\vec{a}\times\vec{b}\rvert = ab\sin\varphi.$$

Zwrot wyznacza **reguła prawej dłoni**: palce od $\vec{a}$ do $\vec{b}$ (krótszą drogą), kciuk wskazuje $\vec{a}\times\vec{b}$. Iloczyn wektorowy jest antyprzemienny: $\vec{b}\times\vec{a} = -\vec{a}\times\vec{b}$. Przykład fizyczny: moment siły $\vec{\tau} = \vec{r}\times\vec{F}$.

## Wzory i założenia

| Wzór | Znaczenie | Kiedy obowiązuje |
|---|---|---|
| $a = \sqrt{a_x^2 + a_y^2 + a_z^2}$ | długość wektora | układ prostokątny (kartezjański) |
| $a_x = a\cos\theta,\ a_y = a\sin\theta$ | składowe na płaszczyźnie | $\theta$ mierzony od dodatniej osi $x$ przeciwnie do ruchu wskazówek zegara |
| $\theta = \operatorname{atan2}(a_y, a_x)$ | kierunek wektora | sam $\arctan(a_y/a_x)$ myli ćwiartki II i III — sprawdzaj znaki składowych |
| $\vec{a}\cdot\vec{b} = ab\cos\varphi = a_xb_x + a_yb_y + a_zb_z$ | iloczyn skalarny | $\varphi$ — kąt między wektorami, $0 \le \varphi \le 180^\circ$ |
| $\cos\varphi = \dfrac{\vec{a}\cdot\vec{b}}{ab}$ | kąt między wektorami | $a, b \neq 0$ |
| $\vec{a}\times\vec{b} = (a_yb_z - a_zb_y)\hat{\imath} + (a_zb_x - a_xb_z)\hat{\jmath} + (a_xb_y - a_yb_x)\hat{k}$ | iloczyn wektorowy | układ prawoskrętny ($\hat{\imath}\times\hat{\jmath} = \hat{k}$) |
| $\lvert\vec{a}\times\vec{b}\rvert = ab\sin\varphi$ | pole równoległoboku | — |
| $\lvert\vec{a}+\vec{b}\rvert^2 = a^2 + b^2 + 2ab\cos\varphi$ | długość sumy (twierdzenie cosinusów) | $\varphi$ — kąt **między wektorami**, nie kąt w trójkącie |

## Przykład rozwiązany

**Zadanie.** Samolot leci z prędkością $v_s = 250\ \mathrm{km/h}$ względem powietrza, kursem na północ. Wiatr wieje ze wschodu na zachód z prędkością $v_w = 60\ \mathrm{km/h}$. Jaka jest prędkość samolotu względem ziemi i o jaki kąt odchyla się od północy?

**Model.** Prędkość względem ziemi to suma wektorów: $\vec{v} = \vec{v}_s + \vec{v}_w$. Oś $x$ — na wschód, oś $y$ — na północ.

**Składowe.** $\vec{v}_s = (0,\ 250)\ \mathrm{km/h}$, wiatr wieje *na zachód*, więc $\vec{v}_w = (-60,\ 0)\ \mathrm{km/h}$.

$$\vec{v} = (-60,\ 250)\ \mathrm{km/h}, \qquad v = \sqrt{60^2 + 250^2} \approx 257\ \mathrm{km/h}.$$

**Kierunek.** Odchylenie od północy: $\tan\alpha = 60/250$, więc $\alpha \approx 13{,}5^\circ$ na zachód.

**Sprawdzenie.** Wynik jest nieco większy niż 250 km/h (wiatr prostopadły zawsze zwiększa wartość prędkości), a gdy $v_w \to 0$, odchylenie dąży do zera. Zgadza się.

### Wersja z rachunkiem różniczkowym i całkowym

**Zadanie.** Punkt porusza się po okręgu: $\vec{r}(t) = R\cos(\omega t)\,\hat{\imath} + R\sin(\omega t)\,\hat{\jmath}$. Pokaż, że prędkość jest zawsze prostopadła do promienia, a przyspieszenie skierowane do środka.

Wektor różniczkujemy składowa po składowej (wersory w układzie kartezjańskim są stałe):

$$\vec{v} = \frac{d\vec{r}}{dt} = -R\omega\sin(\omega t)\,\hat{\imath} + R\omega\cos(\omega t)\,\hat{\jmath},$$

$$\vec{r}\cdot\vec{v} = -R^2\omega\sin\omega t\cos\omega t + R^2\omega\sin\omega t\cos\omega t = 0.$$

Iloczyn skalarny jest zerowy, więc $\vec{v} \perp \vec{r}$. Dalej

$$\vec{a} = \frac{d\vec{v}}{dt} = -R\omega^2\cos(\omega t)\,\hat{\imath} - R\omega^2\sin(\omega t)\,\hat{\jmath} = -\omega^2\vec{r},$$

czyli przyspieszenie ma wartość $\omega^2R$ i zwrot przeciwny do $\vec{r}$ — do środka okręgu. To jest wzór na przyspieszenie dośrodkowe z modułu 02, wyprowadzony w trzech linijkach.

## Typowe pułapki

- **Mylenie kąta.** Kąt w iloczynie skalarnym i w twierdzeniu cosinusów to kąt *między wektorami* (zaczepionymi w jednym punkcie), a nie kąt wewnętrzny trójkąta z reguły „ogon do grotu”. Różnią się o $180^\circ$, a cosinus zmienia znak.
- **Kalkulator w stopniach albo radianach.** Sprawdź tryb przed liczeniem $\sin$ i $\cos$. W Pythonie `np.sin` przyjmuje radiany.
- **$\arctan$ zamiast atan2.** Dla $\vec{a} = (-3, -4)$ wzór $\arctan(a_y/a_x)$ daje $53^\circ$, a wektor wskazuje w III ćwiartce ($233^\circ$).
- **Kolejność w iloczynie wektorowym.** $\vec{r}\times\vec{F}$ i $\vec{F}\times\vec{r}$ mają przeciwne zwroty — moment siły „kręci” w złą stronę.
- **Dodawanie długości.** $\lvert\vec{a}+\vec{b}\rvert = a + b$ tylko wtedy, gdy wektory są równoległe i zgodnie skierowane.

## Doświadczenie / symulacja

**Symulacja PhET:** *Dodawanie wektorów* ([phet.colorado.edu/pl](https://phet.colorado.edu/pl/)). Ustaw dwa wektory o długościach 3 i 4 i zmieniaj kąt między nimi od $0^\circ$ do $180^\circ$. Zapisz długość sumy dla pięciu kątów i porównaj z $\sqrt{a^2 + b^2 + 2ab\cos\varphi}$.

**Python:** iloczyny i kąt między wektorami — ten sam rachunek, którym sprawdzisz zadania B.

```python
import numpy as np
import matplotlib.pyplot as plt

a = np.array([1.0, 2.0, -1.0])
b = np.array([2.0, 0.0, 3.0])

dot = a @ b
cross = np.cross(a, b)
phi = np.degrees(np.arccos(dot / (np.linalg.norm(a) * np.linalg.norm(b))))
print(f"a·b = {dot:.3f}, a×b = {cross}, kąt = {phi:.1f}°")
assert abs(cross @ a) < 1e-12 and abs(cross @ b) < 1e-12   # a×b ⟂ a i b

# Dodawanie wektorów na płaszczyźnie: reguła „ogon do grotu”
u, w = np.array([3.0, 1.0]), np.array([1.0, 2.5])
fig, ax = plt.subplots(figsize=(4, 4))
ax.quiver(0, 0, *u, angles="xy", scale_units="xy", scale=1, color="C0", label="u")
ax.quiver(*u, *w, angles="xy", scale_units="xy", scale=1, color="C1", label="w")
ax.quiver(0, 0, *(u + w), angles="xy", scale_units="xy", scale=1, color="C2", label="u + w")
ax.set_xlim(-0.5, 5); ax.set_ylim(-0.5, 4.5); ax.set_aspect("equal"); ax.grid(True); ax.legend()
plt.show()
```

## Zadania

### A. Poziom maturalny

1. Wektor $\vec{a} = (3,\ 4)$. Oblicz jego długość i kąt z dodatnią osią $x$.

<details>
<summary>Odpowiedź</summary>

$a = 5$, $\theta = \arctan(4/3) \approx 53{,}1^\circ$.
</details>

2. Na ciało działają dwie siły: $F_1 = 30\ \mathrm{N}$ i $F_2 = 40\ \mathrm{N}$. Oblicz wartość siły wypadkowej, gdy kąt między siłami wynosi a) $90^\circ$, b) $60^\circ$, c) $180^\circ$.

<details>
<summary>Odpowiedź</summary>

a) $50\ \mathrm{N}$; b) $\sqrt{900 + 1600 + 2\cdot30\cdot40\cdot\tfrac12} = \sqrt{3700} \approx 60{,}8\ \mathrm{N}$; c) $10\ \mathrm{N}$ (zwrot siły $F_2$).
</details>

3. Skrzynię przesunięto po poziomej podłodze o $5\ \mathrm{m}$, ciągnąc ją siłą $20\ \mathrm{N}$ skierowaną pod kątem $30^\circ$ do poziomu. Oblicz pracę tej siły.

<details>
<summary>Odpowiedź</summary>

$W = Fs\cos 30^\circ = 20\cdot5\cdot0{,}866 \approx 86{,}6\ \mathrm{J}$.
</details>

4. Łódź płynie prostopadle do brzegu z prędkością $3\ \mathrm{m/s}$ względem wody. Prąd rzeki ma prędkość $4\ \mathrm{m/s}$. Jaka jest prędkość łodzi względem brzegu i jaki kąt tworzy z kierunkiem prostopadłym do brzegu?

<details>
<summary>Odpowiedź</summary>

$5\ \mathrm{m/s}$; kąt $\arctan(4/3) \approx 53{,}1^\circ$ w kierunku prądu.
</details>

### B. Poziom akademicki

1. Dla $\vec{a} = (1,\ 2,\ -1)$ i $\vec{b} = (2,\ 0,\ 3)$ oblicz $\vec{a}\cdot\vec{b}$, $\vec{a}\times\vec{b}$ i kąt między wektorami.

<details>
<summary>Odpowiedź</summary>

$\vec{a}\cdot\vec{b} = -1$, $\vec{a}\times\vec{b} = (6,\ -5,\ -4)$, $\cos\varphi = -1/\sqrt{78}$, $\varphi \approx 96{,}5^\circ$.
</details>

2. Oblicz pole trójkąta o wierzchołkach $A(0,0,0)$, $B(1,2,0)$, $C(3,1,2)$.

<details>
<summary>Odpowiedź</summary>

$\overrightarrow{AB}\times\overrightarrow{AC} = (4,\ -2,\ -5)$, pole $= \tfrac12\sqrt{45} \approx 3{,}35$.
</details>

3. Siła $\vec{F} = (3,\ 0,\ 4)\ \mathrm{N}$ działa w punkcie $\vec{r} = (0,\ 2,\ 0)\ \mathrm{m}$. Oblicz moment siły względem początku układu i jego wartość.

<details>
<summary>Odpowiedź</summary>

$\vec{\tau} = \vec{r}\times\vec{F} = (8,\ 0,\ -6)\ \mathrm{N\cdot m}$, $\tau = 10\ \mathrm{N\cdot m}$.
</details>

4. Udowodnij, że jeśli $\lvert\vec{a}+\vec{b}\rvert = \lvert\vec{a}-\vec{b}\rvert$, to $\vec{a}\perp\vec{b}$.

<details>
<summary>Odpowiedź</summary>

$\lvert\vec{a}+\vec{b}\rvert^2 - \lvert\vec{a}-\vec{b}\rvert^2 = 4\,\vec{a}\cdot\vec{b}$. Równość długości oznacza $\vec{a}\cdot\vec{b} = 0$.
</details>

5. Wektor $\vec{u}(t)$ ma stałą długość. Pokaż, że $\vec{u}\cdot\dfrac{d\vec{u}}{dt} = 0$. Co to oznacza dla prędkości w ruchu po okręgu?

<details>
<summary>Odpowiedź</summary>

$\dfrac{d}{dt}(\vec{u}\cdot\vec{u}) = 2\,\vec{u}\cdot\dfrac{d\vec{u}}{dt} = \dfrac{d}{dt}(u^2) = 0$. Dla $\vec{u} = \vec{r}$ w ruchu po okręgu: prędkość jest prostopadła do promienia.
</details>

## Źródła

- OpenStax, *Fizyka dla szkół wyższych*, t. 1, rozdz. 2 — cały rozdział, szczególnie §2.4 (iloczyny wektorów) i zadania z końca rozdziału.
- Halliday, Resnick, Walker, *Podstawy fizyki*, wyd. 2015, t. 1, rozdz. 3 — §3.3 o mnożeniu wektorów zawiera dobre przykłady z regułą prawej dłoni.
- Symulacja PhET *Dodawanie wektorów* (wersja polska).
