# 25.05 — Pola i potencjały na siatce — równanie Laplace'a

> **Moduł:** [25 — Fizyka obliczeniowa w Pythonie](README.md) · **Poziom:** 🔵 studia · **Status:** ✅ pełny
>
> **Czytaj:**
>
> - _Podręczniki główne nie mają osobnego paragrafu na ten temat — materiały są w sekcji „Źródła”._

← [Dopasowanie modeli do danych pomiarowych](04-dopasowanie-modeli.md) · [spis modułu](README.md) · [Metody Monte Carlo: rozpad, błądzenie losowe, całkowanie](06-monte-carlo.md) →

## Po co to jest

Prawo Gaussa i symetria wystarczają do policzenia pola kuli, walca i płaskiego kondensatora (12.04). Prawdziwe elektrody mają jednak krawędzie, otwory i dziwne kształty: soczewki elektronowe, czujniki pojemnościowe w ekranie dotykowym, izolatory linii wysokiego napięcia. To samo równanie, **równanie Laplace'a**, opisuje ustalony rozkład temperatury w płycie, przepływ cieczy idealnej i dyfuzję w stanie ustalonym. Rozwiązuje się je na siatce prostą regułą: potencjał w każdym punkcie to średnia z sąsiadów. To pierwsze spotkanie z równaniami różniczkowymi cząstkowymi i metodą różnic skończonych — podstawą programów inżynierskich (metoda elementów skończonych działa podobnie).

## Teoria w pigułce

**Równanie Laplace'a i Poissona.** W obszarze bez ładunków potencjał elektryczny spełnia

$$\nabla^2V = \frac{\partial^2V}{\partial x^2} + \frac{\partial^2V}{\partial y^2} = 0,$$

a w obecności ładunku o gęstości $\rho$ — równanie Poissona $\nabla^2V = -\rho/\varepsilon_0$. Wynika to z prawa Gaussa w postaci różniczkowej i z $\vec E = -\nabla V$ (12.05, 16.01). Rozwiązanie wyznaczają **warunki brzegowe**: znane potencjały elektrod i ścianek.

**Dyskretyzacja.** Na siatce o kroku $h$ drugą pochodną zastępujemy ilorazem różnicowym:

$$\frac{\partial^2V}{\partial x^2} \approx \frac{V_{i+1,j} - 2V_{i,j} + V_{i-1,j}}{h^2}.$$

Równanie Laplace'a przyjmuje postać

$$V_{i,j} = \tfrac14\left(V_{i+1,j} + V_{i-1,j} + V_{i,j+1} + V_{i,j-1}\right),$$

czyli **potencjał w każdym węźle jest średnią z czterech sąsiadów**.

**Metody iteracyjne:**
- **Jacobi**: wszystkie węzły naraz zastępujemy średnią z poprzedniej iteracji. Prosta (łatwo wektoryzowana w NumPy), ale wolna — liczba iteracji rośnie jak $N^2$.
- **Gauss–Seidel**: korzysta od razu z już poprawionych sąsiadów, ok. 2 razy szybsza.
- **Nadrelaksacja (SOR)**: poprawkę Gaussa–Seidela mnożymy przez $\omega \in (1, 2)$. Przy optymalnym $\omega \approx 2/(1 + \pi/N)$ liczba iteracji rośnie tylko jak $N$ — dla siatki 100×100 kilkaset zamiast kilkunastu tysięcy.

Na koniec pole liczymy z gradientu: $\vec E = -\nabla V$ (`np.gradient`). Linie ekwipotencjalne rysuje `plt.contour`, linie pola — `plt.streamplot`.

**Właściwość wartości średniej.** Ponieważ rozwiązanie w każdym punkcie jest średnią z otoczenia, potencjał nie ma maksimów ani minimów wewnątrz obszaru bez ładunków. Wniosek fizyczny (**twierdzenie Earnshawa**): ładunku nie da się utrzymać w stabilnej równowadze samymi polami elektrostatycznymi. Pułapki jonowe używają pól zmiennych.

## Wzory i założenia

| Wzór | Znaczenie | Kiedy obowiązuje |
|---|---|---|
| $\nabla^2V = 0$ | równanie Laplace'a | obszar bez ładunków; też temperatura w stanie ustalonym |
| $\nabla^2V = -\rho/\varepsilon_0$ | równanie Poissona | z ładunkiem |
| $V_{i,j} = \tfrac14(V_{i\pm1,j} + V_{i,j\pm1}) + \tfrac{h^2\rho_{i,j}}{4\varepsilon_0}$ | schemat pięciopunktowy | siatka kwadratowa, błąd $\sim h^2$ |
| $V \leftarrow V + \omega(\bar V_{\text{sąsiadów}} - V)$, $\omega_{\text{opt}} \approx \dfrac{2}{1 + \sin(\pi/N)}$ | nadrelaksacja | — |
| $\vec E = -\nabla V$ | pole z potencjału | — |

## Przykład rozwiązany

**Zadanie.** Kwadratowe pudło: górna ścianka ma potencjał 1 V, pozostałe 0 V. Ile wynosi potencjał w środku?

Z zasady superpozycji: gdyby wszystkie cztery ścianki miały 1 V, potencjał wewnątrz byłby wszędzie równy 1 V. Z symetrii każda ścianka daje w środku ten sam wkład, więc $V_{\text{środek}} = \tfrac14\ \mathrm V$ — dokładnie, bez rachunków.

Rozwiązanie analityczne (szereg Fouriera) w dowolnym punkcie:

$$V(x, y) = \sum_{n\ \text{nieparz.}}\frac{4}{n\pi}\sin(n\pi x)\frac{\sinh(n\pi y)}{\sinh(n\pi)}.$$

Daje ono np. $V(0{,}5;\ 0{,}75) \approx 0{,}540\ \mathrm V$. Siatka 41×41 z metodą Jacobiego: 0,2500 i 0,5403 V.

### Wersja z rachunkiem różniczkowym i całkowym

**Skąd schemat pięciopunktowy i jaki ma błąd.** Z rozwinięcia Taylora:

$$V(x \pm h) = V \pm hV' + \frac{h^2}2V'' \pm \frac{h^3}6V''' + \frac{h^4}{24}V^{(4)} + \dots$$

Po dodaniu nieparzyste potęgi się znoszą:

$$\frac{V(x + h) - 2V(x) + V(x - h)}{h^2} = V'' + \frac{h^2}{12}V^{(4)} + \dots,$$

więc błąd jest rzędu $h^2$: dwukrotne zagęszczenie siatki zmniejsza go ok. 4 razy.

**Właściwość wartości średniej** w wersji ciągłej: dla $\nabla^2V = 0$ średnia po okręgu o promieniu $R$ wokół punktu, $\bar V(R) = \frac1{2\pi}\oint V\,d\varphi$, spełnia $\dfrac{d\bar V}{dR} = \dfrac{1}{2\pi R}\oint\nabla V\cdot d\vec n = \dfrac{1}{2\pi R}\iint\nabla^2V\,dS = 0$ (twierdzenie Gaussa). Średnia nie zależy od $R$ i równa się wartości w środku.

## Typowe pułapki

- **Mała zmiana między iteracjami oznacza zbieżność.** W metodzie Jacobiego na dużej siatce zmiana w jednej iteracji może wynosić $10^{-7}$, a błąd rozwiązania $10^{-4}$, bo zbieżność jest bardzo wolna. Sprawdzaj wynik na przypadku znanym i przy różnych tolerancjach.
- **Nadpisywanie tablicy w metodzie Jacobiego.** Wektorowe przypisanie `V[1:-1, 1:-1] = 0.25*(...)` liczy prawą stronę ze starej tablicy — to Jacobi. W pętli po węzłach z aktualizacją w miejscu powstaje Gauss–Seidel. Oba działają, ale trzeba wiedzieć, który się ma.
- **Elektrody nie mogą się zmieniać.** Węzły elektrod i brzegów (warunki brzegowe) trzeba pominąć przy aktualizacji (maska).
- **Indeksy a osie.** W tablicy `V[i, j]` pierwszy indeks to wiersz (oś $y$), drugi kolumna (oś $x$). Przy `np.gradient` i `plt.contour` łatwo zamienić składowe.
- **Zbyt rzadka siatka przy ostrych krawędziach.** Pole przy krawędziach i ostrzach jest bardzo silne (efekt ostrza) i wymaga gęstszej siatki lokalnie.

## Doświadczenie / symulacja

**Ekwipotencjale na papierze przewodzącym.** Na papierze grafitowym (lub kartce zamalowanej miękkim ołówkiem) narysuj elektrody farbą przewodzącą, podłącz baterię 9 V i woltomierzem znajdź punkty o równym potencjale. Porównaj mapę z symulacją dla tego samego kształtu elektrod.

**Symulacja PhET:** *Ładunki i pola* (*Charges and Fields*) — linie ekwipotencjalne układów ładunków ([phet.colorado.edu/pl](https://phet.colorado.edu/pl/)).

**Python:** (1) pudło z jedną ścianką pod napięciem — Jacobi kontra rozwiązanie analityczne, (2) kondensator o skończonych okładkach w uziemionym pudle — nadrelaksacja, ekwipotencjale, linie pola i pole brzegowe.

```python
import numpy as np
import matplotlib.pyplot as plt

def szereg(x, y, nmax=401):                                 # rozwiązanie analityczne, ścianka y = 1 pod napięciem 1 V
    n = np.arange(1, nmax, 2)
    return np.sum(4/(n*np.pi)*np.sin(n*np.pi*x)*np.exp(n*np.pi*(y - 1))*(1 - np.exp(-2*n*np.pi*y))/(1 - np.exp(-2*n*np.pi)))

for N in (21, 41, 81):
    V = np.zeros((N, N)); V[-1, 1:-1] = 1.0                 # wiersz = y, kolumna = x
    for it in range(1, 200001):
        stare = V[1:-1, 1:-1].copy()
        V[1:-1, 1:-1] = 0.25*(V[2:, 1:-1] + V[:-2, 1:-1] + V[1:-1, 2:] + V[1:-1, :-2])
        if np.abs(V[1:-1, 1:-1] - stare).max() < 1e-8:
            break
    c = (N - 1)//2
    print(f"Jacobi N = {N}: {it:6d} iteracji, V(0,5; 0,5) = {V[c, c]:.5f}, V(0,5; 0,75) = {V[3*(N - 1)//4, c]:.5f}"
          f" (dokładnie {szereg(0.5, 0.5):.5f} i {szereg(0.5, 0.75):.5f})")

# kondensator: okładki ±1 V w uziemionym pudle, nadrelaksacja czerwono-czarna (wektorowo)
N = 101; h = 1/(N - 1)
V = np.zeros((N, N)); stale = np.zeros((N, N), bool)
stale[0, :] = stale[-1, :] = stale[:, 0] = stale[:, -1] = True
V[40, 30:71], V[60, 30:71] = -1.0, 1.0; stale[40, 30:71] = stale[60, 30:71] = True
I, J = np.indices(V.shape)
omega = 2/(1 + np.sin(np.pi/(N - 1)))
for it in range(1, 20001):
    zmiana = 0.0
    for kolor in (0, 1):
        maska = ((I + J) % 2 == kolor) & ~stale
        srednia = np.zeros_like(V)
        srednia[1:-1, 1:-1] = 0.25*(V[2:, 1:-1] + V[:-2, 1:-1] + V[1:-1, 2:] + V[1:-1, :-2])
        r = np.where(maska, srednia - V, 0.0)
        V += omega*r; zmiana = max(zmiana, np.abs(r).max())
    if zmiana < 1e-9:
        break
Ey, Ex = np.gradient(-V, h)
print(f"SOR: {it} iteracji; pole w środku kondensatora {abs(Ey[50, 50]):.2f} V/jedn. (U/d = {2/(20*h):.1f}),"
      f" przy krawędzi okładki {abs(Ey[50, 70]):.2f}, poza kondensatorem {abs(Ey[50, 85]):.2f}")
x = np.linspace(0, 1, N)
plt.contour(x, x, V, levels=np.linspace(-0.9, 0.9, 19), cmap="viridis")
plt.streamplot(x, x, Ex, Ey, color="gray", density=1.2, linewidth=0.6)
plt.gca().set_aspect("equal"); plt.title("ekwipotencjale i linie pola"); plt.show()
```

## Zadania

### A. Poziom maturalny _(opcjonalnie — rozgrzewka)_

1. Ścianki kwadratowego pudła mają potencjały 10, 20, 30 i 40 V. Ile wynosi potencjał w środku?

<details>
<summary>Odpowiedź</summary>

Z superpozycji i symetrii każda ścianka daje ¼ swojego potencjału: $(10 + 20 + 30 + 40)/4 = 25\ \mathrm V$.
</details>

2. Na siatce potencjały czterech sąsiadów węzła to 2, 4, 5 i 9 V. Jaki potencjał ma węzeł w rozwiązaniu równania Laplace'a?

<details>
<summary>Odpowiedź</summary>

Średnia: $(2 + 4 + 5 + 9)/4 = 5\ \mathrm V$.
</details>

### B. Poziom akademicki

1. Uruchom kod dla $N = 21, 41, 81$. Jak rośnie liczba iteracji Jacobiego? A błąd wartości w punkcie (0,5; 0,75)?

<details>
<summary>Odpowiedź</summary>

Liczba iteracji rośnie ok. 3,5–4 razy przy podwojeniu $N$ (jak $N^2$). Błąd dyskretyzacji maleje ok. 4 razy (jak $h^2$), o ile kryterium zatrzymania jest wystarczająco ostre — przy zbyt łagodnym błąd iteracji dominuje na dużych siatkach.
</details>

2. Pokaż, że twierdzenie Earnshawa wynika z właściwości wartości średniej: dodatni ładunek próbny nie może mieć stabilnej równowagi w polu ładunków zewnętrznych.

<details>
<summary>Odpowiedź</summary>

Stabilna równowaga wymaga minimum energii $qV$, czyli minimum $V$ w punkcie bez ładunków (poza ładunkiem próbnym). Ale $V$ jest tam średnią z otoczenia, więc nie może być mniejsze od wszystkich sąsiednich wartości. Minimum mogłoby istnieć tylko na brzegu lub przy innym ładunku.
</details>

3. Zmodyfikuj program do równania Poissona: w środku uziemionego pudła umieść „ładunek” w jednym węźle ($\rho h^2/\varepsilon_0 = 1$). Sprawdź, że w pobliżu potencjał zachowuje się jak $-\tfrac{1}{2\pi}\ln r$ (ładunek liniowy w 2D).

<details>
<summary>Odpowiedź</summary>

Krok aktualizacji: `V = 0.25*(sąsiedzi) + 0.25*src`. Wykres $V$ od $\ln r$ w pobliżu środka jest prostą o nachyleniu ok. $-1/(2\pi) \approx -0{,}16$ (w jednostkach siatki). Daleko od środka wpływ uziemionych ścianek zakrzywia zależność.
</details>

4. Ten sam program rozwiązuje zagadnienie cieplne. Płyta metalowa ma krawędzie w 0°C, oprócz jednej w 100°C. Jaka temperatura ustali się w środku? Ile ciepła płynie przez zimne krawędzie względem gorącej?

<details>
<summary>Odpowiedź</summary>

25°C (to samo zagadnienie co pudło z jedną ścianką pod napięciem). W stanie ustalonym ciepło wpływające przez gorącą krawędź równa się sumie ciepła wypływającego przez trzy zimne (bilans energii, 11.03).
</details>

## Źródła

- OpenStax, *Fizyka dla szkół wyższych*, t. 2 — §7.4 (obliczanie natężenia na podstawie potencjału) i §7.5 (powierzchnie ekwipotencjalne i przewodniki).
- Halliday, Resnick, Walker, *Podstawy fizyki*, wyd. 2015, t. 3 — §24.2 (powierzchnie ekwipotencjalne) i §24.6 (natężenie pola z potencjału).
- B. Zglinicki, *Programowanie i metody numeryczne* (Wydział Fizyki UW) — [zestaw 14: równania różniczkowe cząstkowe](https://www.fuw.edu.pl/~bzglinicki/teaching/pmn/cwiczenia/14), po polsku.
- Moduły 12.05 (potencjał) i 11.03 (transport ciepła).
- Symulacja PhET *Ładunki i pola*.
