# 07.05 — Pole rozkładu masy i siły pływowe

> **Moduł:** [07 — Grawitacja i elementy astronomii](README.md) · **Poziom:** 🔵 studia · **Status:** ✅ pełny
>
> **Czytaj:**
>
> - OpenStax, *Fizyka dla szkół wyższych*, t. 1, rozdz. 13: [§13.6](https://openstax.org/books/fizyka-dla-szk%C3%B3%C5%82-wy%C5%BCszych-tom-1/pages/13-6-sily-plywowe) · [wstęp do rozdziału](https://openstax.org/books/fizyka-dla-szk%C3%B3%C5%82-wy%C5%BCszych-tom-1/pages/13-wstep)
> - Halliday, Resnick, Walker, *Podstawy fizyki*, wyd. 2015, t. 2: §13.4 (s. 47)
> - Halliday, Resnick, Walker, *Podstawy fizyki*, wyd. 1 (2003), t. 2: [§14.3, s. 30](https://home.agh.edu.pl/~czapli/Resnick_2.pdf#page=46), [§14.5, s. 36](https://home.agh.edu.pl/~czapli/Resnick_2.pdf#page=52) — PDF z serwera AGH

← [Prawa Keplera](04-prawa-keplera.md) · [spis modułu](README.md) · [Elementy astronomii: odległości, gwiazdy, galaktyki](06-elementy-astronomii.md) →

## Po co to jest

Wzór $GMm/r^2$ dotyczy mas punktowych. Dlaczego możemy go stosować do Ziemi, która jest wielką kulą? Odpowiedź daje twierdzenie o powłoce Newtona, a metoda — sumowanie (całkowanie) przyczynków od małych kawałków masy — przyda się bez zmian w elektrostatyce (12.03). Ten temat wyjaśnia też pływy morskie: biorą się nie z samej grawitacji Księżyca, ale z tego, że jest ona **różna** po dwóch stronach Ziemi.

## Teoria w pigułce

**Zasada superpozycji.** Pole od ciała rozciągłego to suma (całka) pól od jego elementów:

$$\vec{\gamma} = -G\int\frac{dm}{r^2}\hat{r}.$$

W praktyce całkujemy osobno składowe i korzystamy z symetrii, żeby część z nich się zniosła.

**Twierdzenia o powłoce (Newton).**
1. Jednorodna powłoka kulista przyciąga ciało **na zewnątrz** tak, jakby cała jej masa była skupiona w środku.
2. Wewnątrz powłoki pole grawitacyjne od niej jest **zerowe**.

Wnioski: kula o masie zależnej tylko od odległości od środka przyciąga na zewnątrz jak punkt; wewnątrz jednorodnej kuli na ciało działa tylko masa „pod nim”, więc $\gamma = GMr/R^3$ (07.02). (Najprościej udowodnić to prawem Gaussa dla grawitacji — analogicznie jak w 12.04.)

**Siły pływowe.** Księżyc przyciąga bliższą stronę Ziemi mocniej niż środek, a środek mocniej niż stronę dalszą. Względem środka Ziemi woda po bliższej stronie jest „przyciągana”, a po dalszej — „zostaje w tyle”. Powstają **dwa** wybrzuszenia, stąd dwa przypływy na dobę. Różnica przyspieszeń dla punktów odległych o $\Delta r$ wzdłuż linii do ciała o masie $M$:

$$\Delta a \approx \frac{2GM}{r^3}\Delta r.$$

Zależy od $1/r^3$, a nie $1/r^2$ — dlatego bliski Księżyc wywołuje ok. dwa razy silniejsze pływy niż znacznie masywniejsze, ale dalekie Słońce. Gdy Słońce, Ziemia i Księżyc są w jednej linii (nów, pełnia), pływy się sumują (**syzygijne**); przy kwadrach częściowo się znoszą (**kwadraturowe**).

**Inne skutki pływów:** synchroniczny obrót Księżyca (zawsze ta sama strona do Ziemi), wydłużanie się doby na Ziemi i oddalanie Księżyca (ok. 3,8 cm/rok), granica Roche'a, w której ciało rozrywane jest przez pływy, rozciąganie ciał w pobliżu czarnych dziur.

## Wzory i założenia

| Wzór | Znaczenie | Kiedy obowiązuje |
|---|---|---|
| $\vec{\gamma} = -G\int\dfrac{dm}{r^2}\hat{r}$ | pole rozkładu masy | superpozycja |
| $\gamma = GM/r^2$ | na zewnątrz kuli | symetria sferyczna |
| $\gamma = 0$ | wewnątrz jednorodnej powłoki | — |
| $\gamma = \dfrac{GMz}{(z^2 + R^2)^{3/2}}$ | na osi pierścienia | odległość $z$ od środka pierścienia |
| $\Delta a = \dfrac{2GM}{r^3}\Delta r$ | przyspieszenie pływowe | $\Delta r \ll r$ |

## Przykład rozwiązany

### Wersja z rachunkiem różniczkowym i całkowym

**Zadanie 1 — pierścień.** Wyznacz pole grawitacyjne na osi cienkiego jednorodnego pierścienia o masie $M$ i promieniu $R$ w odległości $z$ od jego środka.

Każdy element $dm$ jest w odległości $\sqrt{z^2 + R^2}$. Składowe prostopadłe do osi znoszą się parami (symetria), zostaje składowa wzdłuż osi z czynnikiem $\cos\theta = z/\sqrt{z^2 + R^2}$:

$$\gamma = \int\frac{G\,dm}{z^2 + R^2}\cdot\frac{z}{\sqrt{z^2 + R^2}} = \frac{GMz}{(z^2 + R^2)^{3/2}}.$$

Sprawdzenie: dla $z \gg R$ dostajemy $GM/z^2$ (jak punkt), dla $z = 0$ — zero (symetria). Pole jest największe dla $z = R/\sqrt2$.

**Zadanie 2 — pływy.** Porównaj przyspieszenia pływowe od Księżyca i od Słońca na powierzchni Ziemi.

Różnica przyspieszeń między środkiem Ziemi a punktem na powierzchni ($\Delta r = R$), z $\dfrac{d}{dr}\left(\dfrac{GM}{r^2}\right) = -\dfrac{2GM}{r^3}$:

- Księżyc: $\Delta a = \dfrac{2\cdot4{,}9\cdot10^{12}\cdot6{,}37\cdot10^6}{(3{,}84\cdot10^8)^3} \approx 1{,}1\cdot10^{-6}\ \mathrm{m/s^2}$,
- Słońce: $\Delta a = \dfrac{2\cdot1{,}33\cdot10^{20}\cdot6{,}37\cdot10^6}{(1{,}50\cdot10^{11})^3} \approx 5{,}1\cdot10^{-7}\ \mathrm{m/s^2}$.

Pływy słoneczne to ok. 46% księżycowych, choć przyciąganie Słońca jest ok. 180 razy silniejsze niż Księżyca. Przyspieszenie pływowe to ok. $10^{-7}g$ — mało, ale działa na cały ocean.

## Typowe pułapki

- **Pływy z „przyciągania wody przez Księżyc”.** To wyjaśnia tylko jedno wybrzuszenie. Dwa powstają z **różnicy** przyciągania.
- **Pole wewnątrz planety równe zero.** Zero jest wewnątrz pustej powłoki; wewnątrz pełnej kuli pole maleje liniowo.
- **Sumowanie wartości zamiast wektorów.** W całce trzeba rzutować na osie — inaczej wynik dla pierścienia byłby $GM/(z^2 + R^2)$, bez czynnika $\cos\theta$.
- **Siła pływowa ∝ $1/r^2$.** Jest proporcjonalna do $1/r^3$.

## Doświadczenie / symulacja

**Tablice pływów.** Pobierz tablice pływów dla dowolnego portu nad oceanem (np. Gdańsk ma pływy rzędu centymetrów — Bałtyk jest prawie zamknięty; dobrym przykładem jest Brest we Francji). Zaznacz na wykresie wysokość wody przez miesiąc i fazy Księżyca: sprawdź, że największe pływy wypadają ok. nowiu i pełni.

**Python:** pole na osi pierścienia — porównanie wzoru z sumowaniem numerycznym po elementach.

```python
import numpy as np
import matplotlib.pyplot as plt

G, M, R = 1.0, 1.0, 1.0                 # jednostki umowne
phi = np.linspace(0, 2*np.pi, 2000, endpoint=False)
dm = M/len(phi)
ring = np.stack([R*np.cos(phi), R*np.sin(phi), np.zeros_like(phi)], axis=1)

z = np.linspace(0.01, 5, 200)
g_num = []
for zz in z:
    d = np.array([0, 0, zz]) - ring                 # od elementów do punktu na osi
    r = np.linalg.norm(d, axis=1)
    g_vec = -(G*dm*d/r[:, None]**3).sum(axis=0)     # pole skierowane do elementów
    g_num.append(-g_vec[2])
g_wz = G*M*z/(z**2 + R**2)**1.5
print(f"maksimum dla z = {z[np.argmax(g_num)]:.3f} R (wzór 1/√2 = {1/np.sqrt(2):.3f})")
plt.plot(z, g_num, "o", ms=3, label="suma numeryczna"); plt.plot(z, g_wz, label="wzór")
plt.plot(z, G*M/z**2, "--", label="masa punktowa"); plt.ylim(0, 1)
plt.xlabel("z / R"); plt.ylabel("γ [jedn. umowne]"); plt.grid(True); plt.legend(); plt.show()
```

## Zadania

### A. Poziom maturalny _(opcjonalnie — rozgrzewka)_

1. Dlaczego przypływy zdarzają się mniej więcej co 12 h 25 min, a nie co 12 h?

<details>
<summary>Odpowiedź</summary>

Księżyc w ciągu doby przesuwa się po orbicie, więc ten sam punkt Ziemi znajduje się naprzeciw niego co ok. 24 h 50 min; dwa wybrzuszenia dają przypływ co ok. 12 h 25 min.
</details>

2. Kiedy pływy są największe: przy nowiu, pierwszej kwadrze, pełni czy ostatniej kwadrze?

<details>
<summary>Odpowiedź</summary>

Przy nowiu i pełni (Słońce, Ziemia i Księżyc w jednej linii).
</details>

### B. Poziom akademicki

1. Dla pola na osi pierścienia znajdź punkt, w którym jest ono największe.

<details>
<summary>Odpowiedź</summary>

$\dfrac{d}{dz}\dfrac{z}{(z^2 + R^2)^{3/2}} = \dfrac{R^2 - 2z^2}{(z^2 + R^2)^{5/2}} = 0 \Rightarrow z = R/\sqrt2$.
</details>

2. Wyznacz pole na osi cienkiego jednorodnego dysku o masie $M$ i promieniu $R$, sumując pierścienie. Sprawdź granicę $z \gg R$.

<details>
<summary>Odpowiedź</summary>

$\gamma = \displaystyle\int_0^R\frac{G\sigma2\pi r\,dr\,z}{(z^2 + r^2)^{3/2}} = 2\pi G\sigma\left(1 - \frac{z}{\sqrt{z^2 + R^2}}\right)$, $\sigma = M/(\pi R^2)$. Dla $z \gg R$: $1 - z/\sqrt{z^2 + R^2} \approx R^2/(2z^2)$, więc $\gamma \approx GM/z^2$.
</details>

3. Człowiek o wzroście 2 m spada stopami w dół w kierunku czarnej dziury o masie 10 mas Słońca. Oblicz różnicę przyspieszeń między głową a stopami w odległości 1000 km od dziury.

<details>
<summary>Odpowiedź</summary>

$\Delta a = 2GM\Delta r/r^3 = 2\cdot1{,}33\cdot10^{21}\cdot2/10^{18} \approx 5\cdot10^3\ \mathrm{m/s^2}$ — ok. 500 $g$: ciało zostałoby rozerwane („spagetyfikacja”).
</details>

4. Pokaż (całkując po pierścieniach powłoki), że pole jednorodnej powłoki kulistej wewnątrz niej jest zerowe. (Wskazówka: dla punktu w odległości $r$ od środka powłoki o promieniu $R$ wygodnie całkować po odległości $s$ od punktu do pierścienia; wynik to $\int_{R-r}^{R+r}(\dots)\,ds$, w którym przyczynki się znoszą.)

<details>
<summary>Odpowiedź</summary>

Potencjał od powłoki: $V = -\dfrac{GM}{2Rr}\displaystyle\int_{R-r}^{R+r}ds = -\dfrac{GM}{R}$ — stały wewnątrz, więc $\gamma = -dV/dr = 0$. (Na zewnątrz granice to $r - R$ i $r + R$, co daje $-GM/r$.)
</details>

## Źródła

- OpenStax, *Fizyka dla szkół wyższych*, t. 1, rozdz. 13 — §13.6: siły pływowe.
- Halliday, Resnick, Walker, *Podstawy fizyki* — wyd. 2015: t. 2, §13.4 (grawitacja wewnątrz Ziemi); wyd. 1: t. 2, §14.3 i §14.5 (superpozycja, grawitacja wewnątrz Ziemi).
