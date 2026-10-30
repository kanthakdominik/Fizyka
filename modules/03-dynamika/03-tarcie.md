# 03.03 — Tarcie statyczne i kinetyczne

> **Moduł:** [03 — Dynamika punktu materialnego](README.md) · **Poziom:** 🟢 matura R · **Status:** ✅ pełny
>
> **Czytaj:**
>
> - OpenStax, *Fizyka dla szkół wyższych*, t. 1, rozdz. 6: [§6.2](https://openstax.org/books/fizyka-dla-szk%C3%B3%C5%82-wy%C5%BCszych-tom-1/pages/6-2-tarcie) · [wstęp do rozdziału](https://openstax.org/books/fizyka-dla-szk%C3%B3%C5%82-wy%C5%BCszych-tom-1/pages/6-wstep)
> - Halliday, Resnick, Walker, *Podstawy fizyki*, wyd. 2015, t. 1: §6.1 (s. 156)
> - Halliday, Resnick, Walker, *Podstawy fizyki*, wyd. 1 (2003), t. 1: [§6.1–6.2, s. 118](https://home.agh.edu.pl/~czapli/Resnick_1.pdf#page=130) — PDF z serwera AGH

← [Diagramy sił i układy ciał (równia, bloczki, więzy)](02-uklady-cial.md) · [spis modułu](README.md) · [Dynamika ruchu po okręgu](04-dynamika-ruchu-po-okregu.md) →

## Po co to jest

Bez tarcia nie dałoby się chodzić, hamować ani trzymać czegokolwiek w ręce, a z jego powodu maszyny się nagrzewają i zużywają. W zadaniach tarcie jest najczęstszym źródłem błędów, bo jego wartość nie jest dana z góry: tarcie statyczne przyjmuje taką wartość, jaka jest potrzebna, żeby ciało się nie poruszało — ale tylko do pewnej granicy.

## Teoria w pigułce

**Tarcie statyczne** działa, gdy powierzchnie się nie przesuwają względem siebie. Jego wartość dopasowuje się do sytuacji, aż do wartości maksymalnej:

$$T_s \le \mu_sN.$$

**Tarcie kinetyczne** (poślizgowe) działa podczas przesuwania się powierzchni. W prostym modelu ma stałą wartość, niezależną od prędkości i od pola powierzchni styku:

$$T_k = \mu_kN, \qquad \mu_k < \mu_s.$$

Siła tarcia jest skierowana wzdłuż powierzchni, **przeciwnie do ruchu względnego** (kinetyczne) albo przeciwnie do kierunku, w którym ciało by się zaczęło przesuwać (statyczne).

**Jak rozwiązywać.** Najpierw załóż, że ciało spoczywa, i oblicz, jakiego tarcia potrzeba. Jeśli wychodzi więcej niż $\mu_sN$, ciało się porusza i trzeba przyjąć tarcie kinetyczne $\mu_kN$.

**Skąd tarcie.** Powierzchnie stykają się tylko w mikroskopijnych wierzchołkach nierówności, gdzie atomy tworzą wiązania. Rzeczywiste pole styku jest proporcjonalne do siły nacisku — stąd $T \propto N$ i brak zależności od pola pozornej powierzchni.

**Kąt tarcia.** Klocek na równi zaczyna się zsuwać, gdy $mg\sin\alpha > \mu_smg\cos\alpha$, czyli

$$\tan\alpha_{\text{gr}} = \mu_s.$$

To prosta metoda pomiaru współczynnika tarcia.

**Typowe wartości** (orientacyjne): opona na suchym asfalcie $\mu \approx 0{,}7$–$1{,}0$, na mokrym $0{,}4$–$0{,}6$, na lodzie $0{,}1$; drewno po drewnie $0{,}25$–$0{,}5$; stal po stali (sucha) $0{,}6$–$0{,}7$, (smarowana) $0{,}05$–$0{,}1$; teflon po teflonie $0{,}04$.

## Wzory i założenia

| Wzór | Znaczenie | Kiedy obowiązuje |
|---|---|---|
| $T_s \le \mu_sN$ | tarcie statyczne | brak poślizgu; wartość z równań równowagi |
| $T_k = \mu_kN$ | tarcie kinetyczne | poślizg; model przybliżony |
| $\tan\alpha_{\text{gr}} = \mu_s$ | kąt, przy którym klocek rusza | równia, brak innych sił |
| $a = g(\sin\alpha - \mu_k\cos\alpha)$ | zsuwanie się z równi | $\tan\alpha > \mu_s$ |
| $s = \dfrac{v^2}{2\mu g}$ | droga hamowania | koła zablokowane ($\mu_k$) lub ABS (bliżej $\mu_s$) |

## Przykład rozwiązany

**Zadanie 1.** Skrzynia o masie 5 kg leży na poziomej podłodze; $\mu_s = 0{,}5$, $\mu_k = 0{,}3$. Popychamy ją poziomo siłą a) 20 N, b) 30 N. Jaka jest siła tarcia i przyspieszenie?

Maksymalne tarcie statyczne: $\mu_smg = 0{,}5\cdot5\cdot9{,}81 \approx 24{,}5\ \mathrm{N}$.

a) $20\ \mathrm{N} < 24{,}5\ \mathrm{N}$ — skrzynia stoi, tarcie ma wartość **20 N** (a nie 24,5 N!), $a = 0$.

b) $30\ \mathrm{N} > 24{,}5\ \mathrm{N}$ — skrzynia rusza. Tarcie kinetyczne $0{,}3\cdot49{,}05 \approx 14{,}7\ \mathrm{N}$, $a = (30 - 14{,}7)/5 \approx 3{,}06\ \mathrm{m/s^2}$.

**Zadanie 2.** Klocek zsuwa się z równi o kącie $30^\circ$, $\mu_k = 0{,}2$. Oblicz przyspieszenie.

$a = g(\sin30^\circ - 0{,}2\cos30^\circ) = 9{,}81(0{,}5 - 0{,}173) \approx 3{,}2\ \mathrm{m/s^2}$.

## Typowe pułapki

- **$T = \mu_sN$, gdy ciało stoi.** To wartość maksymalna; rzeczywista wynika z równowagi sił.
- **$N = mg$ zawsze.** Gdy siła ciągnąca jest skierowana ukośnie albo ciało leży na równi, nacisk jest inny — tarcie też.
- **Zły zwrot tarcia.** Tarcie przeciwdziała ruchowi względnemu powierzchni, a nie „ruchowi w ogóle”. Napędzane koło samochodu działa na jezdnię do tyłu, a jezdnia na koło — do przodu; to tarcie statyczne napędza samochód.
- **Tarcie zależy od pola powierzchni.** W prostym modelu nie zależy.
- **Ciało na równi musi się zsuwać.** Jeśli $\tan\alpha \le \mu_s$, zostaje w spoczynku.

## Doświadczenie / symulacja

**Pomiar współczynnika tarcia.** Połóż telefon (albo pudełko z telefonem) na książce i powoli ją unoś. Eksperyment *Inclination* w phyphox pokazuje kąt nachylenia. Odczytaj kąt, przy którym telefon rusza: $\mu_s = \tan\alpha$. Powtórz 10 razy, policz średnią i niepewność. Potem zmierz $\mu_k$: ustaw większy kąt, nagraj przyspieszenie zsuwania i skorzystaj ze wzoru $a = g(\sin\alpha - \mu_k\cos\alpha)$.

**Symulacja PhET:** *Siły i ruch: podstawy* — zakładka *Tarcie*.

**Python:** siła tarcia w funkcji przyłożonej siły — charakterystyczny „skok” przy ruszaniu.

```python
import numpy as np
import matplotlib.pyplot as plt

m, g, mu_s, mu_k = 5.0, 9.81, 0.5, 0.3
N = m * g
F = np.linspace(0, 40, 401)
T = np.where(F <= mu_s*N, F, mu_k*N)          # tarcie statyczne = F, potem kinetyczne
a = np.where(F <= mu_s*N, 0.0, (F - mu_k*N)/m)

print(f"tarcie statyczne max = {mu_s*N:.1f} N, kinetyczne = {mu_k*N:.1f} N")
print(f"F = 30 N: a = {(30 - mu_k*N)/m:.2f} m/s²")

fig, ax = plt.subplots(1, 2, figsize=(9, 3.5))
ax[0].plot(F, T); ax[0].set_xlabel("F [N]"); ax[0].set_ylabel("tarcie [N]"); ax[0].grid(True)
ax[1].plot(F, a); ax[1].set_xlabel("F [N]"); ax[1].set_ylabel("a [m/s²]"); ax[1].grid(True)
plt.tight_layout(); plt.show()
```

## Zadania

### A. Poziom maturalny

1. Skrzynię o masie 20 kg pchamy po podłodze ze stałą prędkością; $\mu_k = 0{,}25$. Jaką siłą?

<details>
<summary>Odpowiedź</summary>

$F = \mu_kmg \approx 49\ \mathrm{N}$.
</details>

2. Oblicz drogę hamowania samochodu jadącego z prędkością 72 km/h na suchej ($\mu = 0{,}7$) i mokrej ($\mu = 0{,}4$) nawierzchni.

<details>
<summary>Odpowiedź</summary>

$29\ \mathrm{m}$ i $51\ \mathrm{m}$.
</details>

3. Klocek na powoli unoszonej desce zaczął się zsuwać przy kącie $25^\circ$. Ile wynosi współczynnik tarcia statycznego?

<details>
<summary>Odpowiedź</summary>

$\mu_s = \tan25^\circ \approx 0{,}47$.
</details>

4. Klocek o masie 2 kg ciągniemy siłą 10 N skierowaną pod kątem $30^\circ$ nad poziomem; $\mu_k = 0{,}3$. Oblicz siłę nacisku, tarcie i przyspieszenie.

<details>
<summary>Odpowiedź</summary>

$N = mg - F\sin30^\circ \approx 14{,}6\ \mathrm{N}$; $T \approx 4{,}39\ \mathrm{N}$; $a = (8{,}66 - 4{,}39)/2 \approx 2{,}14\ \mathrm{m/s^2}$.
</details>

5. Jakie jest największe możliwe przyspieszenie samochodu z napędem na cztery koła, jeśli $\mu_s = 0{,}8$? W jakim najkrótszym czasie może rozpędzić się do 100 km/h?

<details>
<summary>Odpowiedź</summary>

$a = \mu_sg \approx 7{,}85\ \mathrm{m/s^2}$; $t \approx 3{,}5\ \mathrm{s}$.
</details>

### B. Poziom akademicki _(opcjonalnie — rozszerzenie z rachunkiem)_

1. Pod jakim kątem do poziomu należy ciągnąć skrzynię, żeby przesuwać ją ze stałą prędkością najmniejszą siłą? Ile wynosi ta siła?

<details>
<summary>Odpowiedź</summary>

$F(\theta) = \dfrac{\mu mg}{\cos\theta + \mu\sin\theta}$; minimum dla $\tan\theta = \mu$, $F_{\min} = \dfrac{\mu mg}{\sqrt{1 + \mu^2}}$.
</details>

2. Klocek wepchnięto w górę równi o kącie $30^\circ$ z prędkością 10 m/s; $\mu_k = \mu_s = 0{,}3$. Jak wysoko (wzdłuż równi) dojedzie? Czy wróci, a jeśli tak, z jaką prędkością?

<details>
<summary>Odpowiedź</summary>

W górę: $a = g(\sin\alpha + \mu\cos\alpha) \approx 7{,}45\ \mathrm{m/s^2}$, droga $\approx 6{,}7\ \mathrm{m}$. Wróci, bo $\tan30^\circ > 0{,}3$; w dół $a \approx 2{,}36\ \mathrm{m/s^2}$, prędkość na dole $\approx 5{,}6\ \mathrm{m/s}$.
</details>

3. Lina owinięta wokół słupka: dla krótkiego odcinka liny o kącie opasania $d\theta$ różnica naciągów to $dT = \mu T\,d\theta$. Pokaż, że $T_2 = T_1e^{\mu\theta}$, i oblicz, ile razy większą siłę może utrzymać marynarz, owijając linę trzy razy wokół pachołka ($\mu = 0{,}3$).

<details>
<summary>Odpowiedź</summary>

$\displaystyle\int\frac{dT}{T} = \mu\int d\theta$; dla $\theta = 6\pi$: $e^{0{,}3\cdot6\pi} \approx 286$ razy.
</details>

## Źródła

- OpenStax, *Fizyka dla szkół wyższych*, t. 1, rozdz. 6 — §6.2: tarcie, z tabelą współczynników i przykładami.
- Halliday, Resnick, Walker, *Podstawy fizyki* — wyd. 2015: t. 1, §6.1; wyd. 1: t. 1, §6.1–6.2.
