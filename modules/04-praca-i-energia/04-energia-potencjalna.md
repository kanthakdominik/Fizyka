# 04.04 — Siły zachowawcze i energia potencjalna

> **Moduł:** [04 — Praca, energia i moc](README.md) · **Poziom:** 🟢🔵 matura R + studia · **Status:** ✅ pełny
>
> **Czytaj:**
>
> - OpenStax, *Fizyka dla szkół wyższych*, t. 1, rozdz. 8: [§8.1–8.2](https://openstax.org/books/fizyka-dla-szk%C3%B3%C5%82-wy%C5%BCszych-tom-1/pages/8-1-energia-potencjalna-ukladu) · [wstęp do rozdziału](https://openstax.org/books/fizyka-dla-szk%C3%B3%C5%82-wy%C5%BCszych-tom-1/pages/8-wstep)
> - Halliday, Resnick, Walker, *Podstawy fizyki*, wyd. 2015, t. 1: §8.1 (s. 224)
> - Halliday, Resnick, Walker, *Podstawy fizyki*, wyd. 1 (2003), t. 1: [§8.1–8.3, s. 169](https://home.agh.edu.pl/~czapli/Resnick_1.pdf#page=181) — PDF z serwera AGH

← [Moc i sprawność](03-moc-i-sprawnosc.md) · [spis modułu](README.md) · [Zasada zachowania energii mechanicznej i całkowitej](05-zasada-zachowania-energii.md) →

## Po co to jest

Energia potencjalna to energia „zmagazynowana” w położeniu ciała względem innych ciał: w podniesionym ciężarze, ściśniętej sprężynie, rozsuniętych ładunkach. Można ją zdefiniować tylko dla sił szczególnego rodzaju — zachowawczych. Z tego pojęcia wyrastają zasada zachowania energii (04.05), potencjał grawitacyjny (07) i elektryczny (12), a na studiach — cała mechanika kwantowa, w której ruch opisuje się przez energię potencjalną, a nie siły.

## Teoria w pigułce

**Siła zachowawcza** to taka, której praca przy przejściu z punktu A do B **nie zależy od drogi**, a tylko od położeń A i B. Równoważnie: praca po dowolnej drodze zamkniętej jest zerowa. Zachowawcze są: grawitacja, siła sprężystości, siła elektrostatyczna. **Niezachowawcze** (dyssypatywne) są: tarcie, opór ośrodka — ich praca zależy od długości drogi i zawsze zmniejsza energię mechaniczną.

**Energia potencjalna** $U$ jest zdefiniowana tak, że praca siły zachowawczej równa się jej ubytkowi:

$$W_{A\to B} = -\Delta U = U_A - U_B.$$

Liczy się tylko **zmiana** energii potencjalnej; poziom zerowy wybieramy dowolnie (np. podłoga, stół, nieskończoność).

**Najważniejsze energie potencjalne.**

| Siła | Energia potencjalna | Poziom zerowy |
|---|---|---|
| ciężar przy powierzchni Ziemi, $mg$ | $U = mgh$ | dowolna wysokość $h = 0$ |
| sprężystość, $F = -kx$ | $U = \tfrac12kx^2$ | sprężyna nieodkształcona |
| grawitacja Newtona, $F = GMm/r^2$ | $U = -\dfrac{GMm}{r}$ | nieskończoność (07) |
| siła Coulomba | $U = \dfrac{kq_1q_2}{r}$ | nieskończoność (12) |

**Siła z energii potencjalnej.** Ponieważ $dW = F\,dx = -dU$:

$$F_x = -\frac{dU}{dx}, \qquad \text{w 3D: } \vec{F} = -\nabla U = -\left(\frac{\partial U}{\partial x}, \frac{\partial U}{\partial y}, \frac{\partial U}{\partial z}\right).$$

Siła wskazuje w stronę **malejącej** energii potencjalnej — kulka toczy się w dół zbocza.

## Wzory i założenia

| Wzór | Znaczenie | Kiedy obowiązuje |
|---|---|---|
| $\Delta U = -W_{\text{zach}}$ | definicja energii potencjalnej | tylko dla sił zachowawczych |
| $U = mgh$ | grawitacyjna przy Ziemi | $h \ll R_Z$, $g = \text{const}$ |
| $U = \tfrac12kx^2$ | sprężystości | prawo Hooke'a |
| $U(x) = -\int_{x_0}^{x}F(x')\,dx'$ | energia z siły | $U(x_0) = 0$ |
| $F = -dU/dx$ | siła z energii | 1D |
| $\oint\vec{F}\cdot d\vec{r} = 0$ | test zachowawczości | każda droga zamknięta |

## Przykład rozwiązany

**Zadanie (poziom maturalny).** Książkę o masie 1 kg przeniesiono z podłogi na półkę na wysokości 2 m, a potem na stół o wysokości 0,8 m. Oblicz zmianę energii potencjalnej w obu etapach i łącznie. Czy wynik zależy od wyboru poziomu zerowego?

- Podłoga → półka: $\Delta U = 1\cdot9{,}81\cdot2 \approx 19{,}6\ \mathrm{J}$.
- Półka → stół: $\Delta U = 1\cdot9{,}81\cdot(0{,}8 - 2) \approx -11{,}8\ \mathrm{J}$.
- Łącznie: $+7{,}8\ \mathrm{J} = mg\cdot0{,}8\ \mathrm{m}$ — tyle samo, co przy przeniesieniu wprost na stół.

Gdyby poziom zerowy był na stole, wartości $U$ zmieniłyby się o stałą, ale różnice — nie.

### Wersja z rachunkiem różniczkowym i całkowym

**Zadanie 1 — energia z siły.** Sprężyna „twardnieje” przy dużych wydłużeniach: $F(x) = -kx - \beta x^3$. Wyznacz energię potencjalną.

$$U(x) = -\int_0^x(-kx' - \beta x'^3)\,dx' = \tfrac12kx^2 + \tfrac14\beta x^4.$$

**Zadanie 2 — siła z energii.** Energia potencjalna cząstki: $U(x) = 3x^2 - x^3$ (J, m). Oblicz siłę w punktach $x = 1\ \mathrm{m}$ i $x = 3\ \mathrm{m}$.

$F = -\dfrac{dU}{dx} = -6x + 3x^2$; $F(1) = -3\ \mathrm{N}$ (do zera), $F(3) = 9\ \mathrm{N}$ (od zera).

**Zadanie 3 — test zachowawczości.** Czy siła $\vec{F} = (y,\ x)$ jest zachowawcza? Szukamy $U$ takiego, że $-\partial U/\partial x = y$, $-\partial U/\partial y = x$. Funkcja $U = -xy$ spełnia oba warunki, więc tak. Dla siły $(2y,\ x)$ z tematu 01 takiej funkcji nie ma (warunek $\partial F_x/\partial y = \partial F_y/\partial x$ nie jest spełniony: $2 \neq 1$).

## Typowe pułapki

- **Energia potencjalna tarcia.** Nie istnieje — tarcie nie jest zachowawcze.
- **Wartość bezwzględna $U$ ma sens fizyczny.** Ma go tylko zmiana; wartość zależy od wyboru zera.
- **Energia potencjalna „ciała”.** Formalnie należy do układu ciał (książka + Ziemia), nie do samego ciała.
- **Znak w $F = -dU/dx$.** Bez minusa siła wypycha ciało w górę zbocza.
- **$U = mgh$ dla satelity.** Dla dużych wysokości trzeba użyć $-GMm/r$ (07).

## Doświadczenie / symulacja

**Symulacja PhET:** *Energia na rampie dla deskorolkarza* (*Energy Skate Park*, [phet.colorado.edu/pl](https://phet.colorado.edu/pl/)). Zmieniaj poziom zerowy energii potencjalnej i obserwuj, że zmieniają się wartości $U$, ale nie przebieg ruchu.

**Python:** siła jako minus pochodna energii — numerycznie dla $U(x) = 3x^2 - x^3$.

```python
import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(-1, 3.5, 451)
U = 3*x**2 - x**3
F = -np.gradient(U, x)                      # F = −dU/dx numerycznie
print("F(1) =", round(np.interp(1, x, F), 3), "N;  F(3) =", round(np.interp(3, x, F), 3), "N")

fig, ax = plt.subplots(2, 1, figsize=(6, 6), sharex=True)
ax[0].plot(x, U); ax[0].set_ylabel("U [J]"); ax[0].grid(True)
ax[1].plot(x, F); ax[1].axhline(0, color="gray"); ax[1].set_ylabel("F [N]"); ax[1].set_xlabel("x [m]"); ax[1].grid(True)
plt.tight_layout(); plt.show()
```

## Zadania

### A. Poziom maturalny

1. Sprężynę o współczynniku $500\ \mathrm{N/m}$ ściśnięto o 4 cm. Ile energii zgromadzono?

<details>
<summary>Odpowiedź</summary>

$U = \tfrac12\cdot500\cdot0{,}04^2 = 0{,}4\ \mathrm{J}$.
</details>

2. Turysta o masie 70 kg wszedł z doliny na szczyt położony 1000 m wyżej. O ile wzrosła jego energia potencjalna? Wyraź ją w kWh.

<details>
<summary>Odpowiedź</summary>

$\Delta U \approx 687\ \mathrm{kJ} \approx 0{,}19\ \mathrm{kWh}$.
</details>

3. Które z sił są zachowawcze: ciężar, siła sprężystości, tarcie, opór powietrza, siła elektrostatyczna?

<details>
<summary>Odpowiedź</summary>

Ciężar, siła sprężystości, siła elektrostatyczna. Tarcie i opór powietrza — nie.
</details>

4. Klocek przesunięto po stole po linii prostej z punktu A do B (1 m), a drugi raz — po półokręgu z A do B. W którym przypadku praca tarcia jest większa (co do wartości)? A praca ciężaru?

<details>
<summary>Odpowiedź</summary>

Tarcia — po półokręgu (droga $\pi/2 \approx 1{,}57\ \mathrm{m}$). Ciężaru — w obu przypadkach zero.
</details>

### B. Poziom akademicki

1. Siła działająca na cząstkę: $F(x) = -k/x^2$ (dla $x > 0$). Wyznacz energię potencjalną, przyjmując $U(\infty) = 0$.

<details>
<summary>Odpowiedź</summary>

$U(x) = -\displaystyle\int_\infty^x\left(-\frac{k}{x'^2}\right)dx' = -\frac{k}{x}$.
</details>

2. Energia potencjalna: $U(x, y) = 2x^2 + 3xy$. Oblicz wektor siły w punkcie $(1,\ 1)$.

<details>
<summary>Odpowiedź</summary>

$\vec{F} = -(4x + 3y,\ 3x) = (-7,\ -3)\ \mathrm{N}$.
</details>

3. Sprawdź, czy siła $\vec{F} = (2xy,\ x^2)$ jest zachowawcza. Jeśli tak, znajdź energię potencjalną.

<details>
<summary>Odpowiedź</summary>

$\partial F_x/\partial y = 2x = \partial F_y/\partial x$ — tak. $U = -x^2y$.
</details>

4. Klocek przesuwamy po stole tam i z powrotem na odcinku 1 m ($\mu_k = 0{,}3$, $m = 1\ \mathrm{kg}$). Oblicz pracę tarcia po tej drodze zamkniętej. Co to mówi o tarciu?

<details>
<summary>Odpowiedź</summary>

$W = -2\cdot0{,}3\cdot9{,}81\cdot1 \approx -5{,}9\ \mathrm{J} \neq 0$ — tarcie nie jest zachowawcze.
</details>

## Źródła

- OpenStax, *Fizyka dla szkół wyższych*, t. 1, rozdz. 8 — §8.1 (energia potencjalna układu) i §8.2 (siły zachowawcze i niezachowawcze).
- Halliday, Resnick, Walker, *Podstawy fizyki* — wyd. 2015: t. 1, §8.1; wyd. 1: t. 1, §8.1–8.3.
- Symulacja PhET *Energia na rampie dla deskorolkarza*.
