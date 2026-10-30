# 02.02 — Ruch jednostajnie zmienny i spadek swobodny

> **Moduł:** [02 — Kinematyka](README.md) · **Poziom:** 🟢 matura R · **Status:** ✅ pełny
>
> **Czytaj:**
>
> - OpenStax, *Fizyka dla szkół wyższych*, t. 1, rozdz. 3: [§3.4–3.5](https://openstax.org/books/fizyka-dla-szk%C3%B3%C5%82-wy%C5%BCszych-tom-1/pages/3-4-ruch-ze-stalym-przyspieszeniem) · [wstęp do rozdziału](https://openstax.org/books/fizyka-dla-szk%C3%B3%C5%82-wy%C5%BCszych-tom-1/pages/3-wstep)
> - Halliday, Resnick, Walker, *Podstawy fizyki*, wyd. 2015, t. 1: §2.4–2.5 (s. 28)
> - Halliday, Resnick, Walker, *Podstawy fizyki*, wyd. 1 (2003), t. 1: [§2.6, s. 23](https://home.agh.edu.pl/~czapli/Resnick_1.pdf#page=35), [§2.8, s. 27](https://home.agh.edu.pl/~czapli/Resnick_1.pdf#page=39) — PDF z serwera AGH

← [Ruch prostoliniowy: położenie, prędkość, przyspieszenie](01-ruch-prostoliniowy.md) · [spis modułu](README.md) · [Ruch o zmiennym przyspieszeniu — całkowanie a(t)](03-zmienne-przyspieszenie.md) →

## Po co to jest

Ruch ze stałym przyspieszeniem to najczęstszy model w zadaniach maturalnych: ruszanie i hamowanie pojazdów, spadek swobodny, rzut pionowy. Cztery wzory z tego tematu trzeba znać na pamięć i umieć dobrać ten, który pasuje do danych. Z nich zbudowane są rzuty (02.05), a w module 03 dowiemy się, kiedy siły dają stałe przyspieszenie.

## Teoria w pigułce

**Ruch jednostajnie zmienny** to ruch po prostej ze stałym przyspieszeniem $a$. Prędkość zmienia się liniowo, a położenie — kwadratowo z czasem:

$$v = v_0 + at, \qquad x = x_0 + v_0t + \tfrac12at^2.$$

Eliminując czas, dostajemy wzór bez $t$ (przydatny, gdy nie znamy czasu):

$$v^2 = v_0^2 + 2a(x - x_0).$$

A z tego, że prędkość średnia to średnia z prędkości początkowej i końcowej:

$$x - x_0 = \frac{v_0 + v}{2}\,t.$$

**Wybór wzoru.** Każdy z czterech wzorów nie zawiera jednej z wielkości $t$, $v$, $x - x_0$, $a$. Wybierz ten, w którym nie ma wielkości, której nie znasz i której nie potrzebujesz.

**Spadek swobodny** to ruch jednostajnie zmienny z przyspieszeniem ziemskim $g \approx 9{,}81\ \mathrm{m/s^2}$ skierowanym w dół, gdy opór powietrza można pominąć. Wszystkie ciała spadają wtedy z tym samym przyspieszeniem, niezależnie od masy. W **rzucie pionowym w górę** ciało hamuje z przyspieszeniem $g$, w najwyższym punkcie ma prędkość zero (ale przyspieszenie nadal $g$!) i wraca z tą samą szybkością, z jaką zostało wyrzucone.

**Wybór osi.** Najwygodniej skierować oś $y$ w górę; wtedy $a = -g$. Wszystkie znaki biorą się wtedy same z równań.

## Wzory i założenia

| Wzór | Brakująca wielkość | Kiedy obowiązuje |
|---|---|---|
| $v = v_0 + at$ | położenie | $a = \text{const}$ |
| $x = x_0 + v_0t + \tfrac12at^2$ | prędkość końcowa | $a = \text{const}$ |
| $v^2 = v_0^2 + 2a(x - x_0)$ | czas | $a = \text{const}$ |
| $x - x_0 = \tfrac12(v_0 + v)t$ | przyspieszenie | $a = \text{const}$ |
| $h_{\max} = \dfrac{v_0^2}{2g}$, $t_{\text{wzn}} = \dfrac{v_0}{g}$ | rzut pionowy w górę | bez oporu powietrza |
| $t = \sqrt{2h/g}$, $v = \sqrt{2gh}$ | spadek swobodny z wysokości $h$ | start z $v_0 = 0$, bez oporu |

## Przykład rozwiązany

**Zadanie 1 — droga zatrzymania.** Kierowca jedzie z prędkością 72 km/h i zauważa przeszkodę. Czas reakcji wynosi 0,8 s, a przy hamowaniu opóźnienie to $6\ \mathrm{m/s^2}$. Jaka jest całkowita droga zatrzymania?

- $v_0 = 72/3{,}6 = 20\ \mathrm{m/s}$.
- **Droga reakcji** (ruch jednostajny): $s_r = 20\cdot0{,}8 = 16\ \mathrm{m}$.
- **Droga hamowania** (wzór bez czasu, $v = 0$): $s_h = \dfrac{v_0^2}{2a} = \dfrac{400}{12} \approx 33{,}3\ \mathrm{m}$.
- **Razem** ok. $49\ \mathrm{m}$.

Przy dwa razy większej prędkości droga reakcji rośnie dwukrotnie, a droga hamowania — czterokrotnie.

**Zadanie 2 — rzut z wysokości.** Z dachu na wysokości 20 m rzucono kamień pionowo w górę z prędkością 15 m/s. Po jakim czasie spadnie na ziemię, na jaką największą wysokość się wzniesie i z jaką prędkością uderzy w ziemię?

Oś $y$ w górę, początek na ziemi: $y_0 = 20\ \mathrm{m}$, $v_0 = 15\ \mathrm{m/s}$, $a = -g$.

- **Upadek** ($y = 0$): $0 = 20 + 15t - 4{,}905t^2$, czyli $t = \dfrac{15 + \sqrt{225 + 392{,}4}}{9{,}81} \approx 4{,}06\ \mathrm{s}$ (drugi pierwiastek jest ujemny i nie ma sensu fizycznego).
- **Największa wysokość:** $y_{\max} = 20 + \dfrac{15^2}{2\cdot9{,}81} \approx 31{,}5\ \mathrm{m}$.
- **Prędkość uderzenia:** $v^2 = 15^2 + 2\cdot9{,}81\cdot20$, $v \approx 24{,}8\ \mathrm{m/s}$ (skierowana w dół).

**Sprawdzenie.** Prędkość uderzenia nie zależy od tego, czy kamień rzucono w górę, czy w dół z tą samą szybkością — wynika to ze wzoru bez czasu.

## Typowe pułapki

- **Znak $g$.** Gdy oś jest w górę, $a = -9{,}81\ \mathrm{m/s^2}$ przez cały lot — także w drodze w górę i w najwyższym punkcie.
- **„W najwyższym punkcie przyspieszenie jest zero”.** Zero jest prędkość; przyspieszenie to nadal $g$.
- **Wzory ruchu jednostajnie zmiennego przy zmiennym przyspieszeniu.** Działają tylko dla $a = \text{const}$ (zmienne przyspieszenie — temat 03).
- **Odrzucanie pierwiastka bez zastanowienia.** Z równania kwadratowego wybierz rozwiązanie, które ma sens fizyczny w danym przedziale czasu.
- **Pomijanie czasu reakcji** w zadaniach o hamowaniu, gdy treść o nim mówi.

## Doświadczenie / symulacja

**Pomiar $g$ ze spadku swobodnego.** Upuść stalową kulkę lub ciężki klucz z kilku wysokości (0,5–2 m) i mierz czas spadku eksperymentem *Acoustic Stopwatch* w phyphox (start — stuknięcie przy puszczeniu, stop — uderzenie w podłogę). Narysuj $h(t^2)$; nachylenie prostej to $g/2$. Pełny plan i opracowanie niepewności są w [module 01, temat 05](../01-pomiary-i-niepewnosci/05-doswiadczenie-i-raport.md).

**Python:** droga zatrzymania w zależności od prędkości — dlaczego ograniczenie prędkości w terenie zabudowanym ma znaczenie.

```python
import numpy as np
import matplotlib.pyplot as plt

v_kmh = np.linspace(20, 140, 121)
v = v_kmh / 3.6
t_r, a = 0.8, 6.0                      # czas reakcji [s], opóźnienie [m/s²]
s_r = v * t_r
s_h = v**2 / (2 * a)

for vk in (30, 50, 70, 90, 140):
    vv = vk / 3.6
    print(f"{vk:3d} km/h: reakcja {vv*t_r:5.1f} m, hamowanie {vv**2/(2*a):5.1f} m, razem {vv*t_r + vv**2/(2*a):5.1f} m")

plt.stackplot(v_kmh, s_r, s_h, labels=["droga reakcji", "droga hamowania"])
plt.xlabel("prędkość [km/h]"); plt.ylabel("droga zatrzymania [m]"); plt.grid(True); plt.legend(loc="upper left")
plt.show()
```

## Zadania

### A. Poziom maturalny

1. Samochód rozpędza się od zera do 100 km/h w 8 s ruchem jednostajnie przyspieszonym. Oblicz przyspieszenie i drogę rozpędzania.

<details>
<summary>Odpowiedź</summary>

$a = 27{,}8/8 \approx 3{,}47\ \mathrm{m/s^2}$; $s = \tfrac12\cdot27{,}8\cdot8 \approx 111\ \mathrm{m}$.
</details>

2. Kamień puszczony swobodnie do studni uderzył w wodę po 2,0 s. Oblicz głębokość studni (do lustra wody) i prędkość uderzenia, pomijając czas biegu dźwięku.

<details>
<summary>Odpowiedź</summary>

$h = \tfrac12\cdot9{,}81\cdot4 \approx 19{,}6\ \mathrm{m}$; $v = 19{,}6\ \mathrm{m/s}$.
</details>

3. Piłkę rzucono pionowo w górę z prędkością 20 m/s. Oblicz największą wysokość i czas, po którym piłka wróci do ręki.

<details>
<summary>Odpowiedź</summary>

$h_{\max} = 400/19{,}62 \approx 20{,}4\ \mathrm{m}$; $t = 2v_0/g \approx 4{,}08\ \mathrm{s}$.
</details>

4. Pociąg jadący z prędkością 30 m/s zatrzymuje się jednostajnie na drodze 450 m. Oblicz opóźnienie i czas hamowania.

<details>
<summary>Odpowiedź</summary>

$a = 900/900 = 1\ \mathrm{m/s^2}$; $t = 30\ \mathrm{s}$.
</details>

5. W chwili, gdy samochód A rusza z miejsca z przyspieszeniem $2\ \mathrm{m/s^2}$, mija go samochód B jadący ze stałą prędkością 20 m/s. Po jakim czasie i w jakiej odległości A dogoni B? Jaką będzie miał wtedy prędkość?

<details>
<summary>Odpowiedź</summary>

$t^2 = 20t \Rightarrow t = 20\ \mathrm{s}$; $x = 400\ \mathrm{m}$; $v_A = 40\ \mathrm{m/s}$.
</details>

### B. Poziom akademicki _(opcjonalnie — rozszerzenie z rachunkiem)_

1. Kamień puszczono do studni i usłyszano plusk po 3,0 s. Prędkość dźwięku wynosi 340 m/s. Oblicz głębokość studni. O ile procent pomylilibyśmy się, pomijając czas biegu dźwięku?

<details>
<summary>Odpowiedź</summary>

$t_1 + \dfrac{gt_1^2}{2\cdot340} = 3{,}0$ daje $t_1 \approx 2{,}88\ \mathrm{s}$, $h \approx 40{,}7\ \mathrm{m}$. Bez dźwięku: $h = 44{,}1\ \mathrm{m}$ — o ok. 8% za dużo.
</details>

2. Wyprowadź wzór $v^2 = v_0^2 + 2a\Delta x$ z zależności $a = v\dfrac{dv}{dx}$ przez całkowanie.

<details>
<summary>Odpowiedź</summary>

$\displaystyle\int_{v_0}^{v}v'\,dv' = \int_{x_0}^{x}a\,dx' \Rightarrow \tfrac12(v^2 - v_0^2) = a(x - x_0)$.
</details>

3. Pokaż, że w spadku swobodnym z zerową prędkością początkową drogi przebywane w kolejnych sekundach mają się do siebie jak kolejne liczby nieparzyste $1 : 3 : 5 : \dots$ (prawo Galileusza).

<details>
<summary>Odpowiedź</summary>

Droga w $n$-tej sekundzie: $\tfrac12gn^2 - \tfrac12g(n-1)^2 = \tfrac12g(2n - 1)$.
</details>

## Źródła

- OpenStax, *Fizyka dla szkół wyższych*, t. 1, rozdz. 3 — §3.4 (ruch ze stałym przyspieszeniem) i §3.5 (spadek swobodny), z wieloma przykładami rozwiązanymi.
- Halliday, Resnick, Walker, *Podstawy fizyki* — wyd. 2015: t. 1, §2.4–2.5; wyd. 1: t. 1, §2.6 i §2.8.
- CKE, [Informator o egzaminie maturalnym z fizyki](https://cke.gov.pl/images/_EGZAMIN_MATURALNY_OD_2023/Informatory/2024/Informator_EM2024_fizyka.pdf) — zadania z kinematyki.
