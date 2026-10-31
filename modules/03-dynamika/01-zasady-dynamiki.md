# 03.01 — Zasady dynamiki Newtona i rodzaje sił

> **Moduł:** [03 — Dynamika punktu materialnego](README.md) · **Poziom:** 🟢 matura R · **Status:** ✅ pełny
>
> **Czytaj:**
>
> - OpenStax, *Fizyka dla szkół wyższych*, t. 1, rozdz. 5: [§5.1–5.6](https://openstax.org/books/fizyka-dla-szk%C3%B3%C5%82-wy%C5%BCszych-tom-1/pages/5-1-pojecie-sily) · [wstęp do rozdziału](https://openstax.org/books/fizyka-dla-szk%C3%B3%C5%82-wy%C5%BCszych-tom-1/pages/5-wstep)
> - Halliday, Resnick, Walker, *Podstawy fizyki*, wyd. 2015, t. 1: §5.1–5.2 (s. 119)
> - Halliday, Resnick, Walker, *Podstawy fizyki*, wyd. 1 (2003), t. 1: [§5.1–5.7, s. 87](https://home.agh.edu.pl/~czapli/Resnick_1.pdf#page=99) — PDF z serwera AGH

← (początek modułu) · [spis modułu](README.md) · [Diagramy sił i układy ciał (równia, bloczki, więzy)](02-uklady-cial.md) →

## Po co to jest

Kinematyka opisuje, jak ciało się porusza; dynamika wyjaśnia dlaczego. Trzy zasady Newtona wystarczają, żeby z sił działających na ciało przewidzieć jego ruch — od klocka na stole po orbitę planety. To najważniejszy temat mechaniki: na nim stoją energia (04), pęd (05), ruch obrotowy (06) i grawitacja (07).

## Teoria w pigułce

**Siła** to miara oddziaływania między ciałami — wektor, jednostka niuton ($1\ \mathrm{N} = 1\ \mathrm{kg\cdot m/s^2}$). Na ciało może działać wiele sił; liczy się ich suma wektorowa, czyli **siła wypadkowa** $\vec{F}_{\text{wyp}} = \sum\vec{F}_i$.

**I zasada (bezwładności).** Jeśli na ciało nie działają siły albo się równoważą, ciało pozostaje w spoczynku lub porusza się ruchem jednostajnym prostoliniowym. Zasada ta definiuje **układy inercjalne** — takie, w których obowiązuje. Ziemia jest w przybliżeniu układem inercjalnym.

**II zasada.** Przyspieszenie ciała jest proporcjonalne do siły wypadkowej i odwrotnie proporcjonalne do masy:

$$\vec{a} = \frac{\vec{F}_{\text{wyp}}}{m}, \qquad \text{ogólniej: } \vec{F}_{\text{wyp}} = \frac{d\vec{p}}{dt},\ \ \vec{p} = m\vec{v}.$$

Masa jest miarą bezwładności — tego, jak trudno zmienić prędkość ciała.

**III zasada (akcji i reakcji).** Jeśli ciało A działa na B siłą $\vec{F}_{AB}$, to B działa na A siłą $\vec{F}_{BA} = -\vec{F}_{AB}$. Te siły działają na **różne ciała**, więc nigdy się nie równoważą.

**Najczęstsze siły.**

| Siła | Wzór | Kierunek |
|---|---|---|
| ciężar (grawitacja przy Ziemi) | $\vec{Q} = m\vec{g}$ | pionowo w dół |
| siła reakcji podłoża (nacisku) $\vec{N}$ | z równań ruchu | prostopadle do powierzchni |
| naciąg nici $\vec{T}$ | z równań ruchu | wzdłuż nici, od ciała |
| sprężystość (prawo Hooke'a) | $F = -kx$ | przeciwnie do odkształcenia |
| tarcie | $T \le \mu N$ | wzdłuż powierzchni (03.03) |

**Masa a ciężar.** Masa (kg) jest własnością ciała. Ciężar (N) to siła, z jaką przyciąga je planeta: na Księżycu ten sam człowiek waży sześć razy mniej, ale ma tę samą masę. Waga łazienkowa mierzy siłę nacisku, a nie masę — dlatego w windzie „kłamie”.

## Wzory i założenia

| Wzór | Znaczenie | Kiedy obowiązuje |
|---|---|---|
| $\sum\vec{F} = m\vec{a}$ | II zasada dynamiki | układ inercjalny, $m = \text{const}$, $v \ll c$ |
| $\vec{F} = d\vec{p}/dt$ | II zasada w postaci ogólnej | także dla zmiennej masy układu (05.05) |
| $\vec{F}_{AB} = -\vec{F}_{BA}$ | III zasada | siły działają na różne ciała |
| $Q = mg$ | ciężar | $g \approx 9{,}81\ \mathrm{m/s^2}$ przy powierzchni Ziemi |
| $F = kx$ | siła sprężystości | małe odkształcenia (granica sprężystości) |

## Przykład rozwiązany

**Zadanie.** Człowiek o masie 70 kg stoi na wadze w windzie, która rusza w górę z przyspieszeniem $2\ \mathrm{m/s^2}$. Co pokazuje waga?

**Siły na człowieka:** ciężar $mg$ w dół, siła nacisku wagi $N$ w górę.

**II zasada** (oś w górę): $N - mg = ma \Rightarrow N = m(g + a) = 70\cdot11{,}81 \approx 827\ \mathrm{N}$.

Waga wyskalowana w kilogramach dzieli siłę przez $g$, więc pokaże ok. **84 kg**. Przy hamowaniu windy jadącej w górę (przyspieszenie w dół) pokaże mniej niż 70 kg, a w swobodnie spadającej windzie — zero (stan nieważkości).

**Sprawdzenie.** Dla $a = 0$ waga pokazuje 70 kg — zgodnie z I zasadą.

### Wersja z rachunkiem różniczkowym i całkowym

**Zadanie.** Na spoczywające ciało o masie 2 kg zaczyna działać siła rosnąca liniowo, $F(t) = 6t$ (N, s). Wyznacz prędkość i położenie po 2 s.

$$a = \frac{F}{m} = 3t, \qquad v(t) = \int_0^t3t'\,dt' = 1{,}5t^2, \qquad x(t) = \int_0^t1{,}5t'^2\,dt' = 0{,}5t^3.$$

$v(2) = 6\ \mathrm{m/s}$, $x(2) = 4\ \mathrm{m}$. Zmiana pędu $mv = 12\ \mathrm{kg\cdot m/s}$ równa się polu pod wykresem $F(t)$: $\tfrac12\cdot2\cdot12 = 12\ \mathrm{N\cdot s}$ — to popęd siły (05.01).

## Typowe pułapki

- **Siła „potrzebna do ruchu”.** Ruch jednostajny nie wymaga siły wypadkowej; siła jest potrzebna do **zmiany** prędkości.
- **Akcja i reakcja się równoważą.** Nie — działają na różne ciała. Na książkę leżącą na stole działają ciężar i reakcja stołu; równoważą się z powodu I zasady, a nie III. Para z III zasady dla ciężaru książki to siła, z jaką książka przyciąga Ziemię.
- **$N = mg$ zawsze.** Tylko na poziomej powierzchni bez przyspieszenia pionowego i bez innych sił pionowych.
- **Mylenie masy i ciężaru.** Masa w kg, ciężar w N.
- **Pominięta siła.** Zawsze rysuj diagram sił i sprawdź, czy każda siła ma źródło (ciało, które ją wywiera).

## Doświadczenie / symulacja

**Winda z telefonem.** Połóż telefon płasko na podłodze windy i uruchom w phyphox eksperyment *Elevator* (albo *Acceleration with g*). Przejedź kilka pięter. Odczytaj przyspieszenie przy ruszaniu i hamowaniu i oblicz, co pokazałaby waga dla osoby o masie 70 kg. Barometr w telefonie pozwala przy okazji obliczyć wysokość piętra.

**Symulacja PhET:** *Siły i ruch: podstawy* (*Forces and Motion: Basics*, [phet.colorado.edu/pl](https://phet.colorado.edu/pl/)) — przeciąganie liny i wózek: sprawdź, że przy równych siłach wózek nie zmienia prędkości.

**Python:** ruch pod działaniem siły zależnej od czasu, rozwiązany numerycznie.

```python
import numpy as np
from scipy.integrate import solve_ivp

m = 2.0
F = lambda t: 6*t                      # siła rosnąca liniowo [N]

sol = solve_ivp(lambda t, s: [s[1], F(t)/m], (0, 2), [0.0, 0.0], rtol=1e-10)
x, v = sol.y[:, -1]
print(f"numerycznie: x(2) = {x:.4f} m, v(2) = {v:.4f} m/s")
print("dokładnie:   x(2) = 4 m,      v(2) = 6 m/s")
```

## Zadania

### A. Poziom maturalny

1. Samochód o masie 1200 kg rozpędza się od zera do 100 km/h w 10 s. Jaka średnia siła wypadkowa na niego działa?

<details>
<summary>Odpowiedź</summary>

$a = 2{,}78\ \mathrm{m/s^2}$, $F \approx 3{,}3\ \mathrm{kN}$.
</details>

2. Osoba o masie 60 kg stoi w windzie na wadze, która pokazuje 540 N. Jakie jest przyspieszenie windy? Czy można stwierdzić, w którą stronę winda jedzie?

<details>
<summary>Odpowiedź</summary>

$a = 540/60 - 9{,}81 \approx -0{,}81\ \mathrm{m/s^2}$ (w dół). Nie: winda może jechać w dół i przyspieszać albo jechać w górę i hamować.
</details>

3. „Koń ciągnie wóz, a wóz ciągnie konia z tą samą siłą (III zasada), więc nie mogą ruszyć.” Gdzie jest błąd?

<details>
<summary>Odpowiedź</summary>

Siły z III zasady działają na różne ciała. O ruchu wozu decyduje wypadkowa sił działających na wóz (koń i tarcie), a o ruchu konia — siły na konia, w tym siła, z jaką ziemia odpycha jego kopyta do przodu.
</details>

4. Astronauta ma masę 70 kg. Ile wynosi jego ciężar na Ziemi i na Księżycu ($g_K = 1{,}62\ \mathrm{m/s^2}$)? Jaką ma masę na Księżycu?

<details>
<summary>Odpowiedź</summary>

$687\ \mathrm{N}$ i $113\ \mathrm{N}$; masa nadal 70 kg.
</details>

5. Na sprężynie o współczynniku $200\ \mathrm{N/m}$ zawieszono ciężarek 0,5 kg. O ile wydłużyła się sprężyna?

<details>
<summary>Odpowiedź</summary>

$x = mg/k \approx 2{,}45\ \mathrm{cm}$.
</details>

### B. Poziom akademicki _(opcjonalnie — rozszerzenie z rachunkiem)_

1. Na ciało o masie $m$ spoczywające na gładkiej powierzchni działa siła $F(t) = F_0e^{-t/\tau}$. Do jakiej prędkości dąży ciało?

<details>
<summary>Odpowiedź</summary>

$v(t) = \dfrac{F_0\tau}{m}(1 - e^{-t/\tau}) \to \dfrac{F_0\tau}{m}$.
</details>

2. Na spoczywające ciało działa siła $F(t) = F_0\cos(\omega t)$. Wyznacz $x(t)$. Czy ciało oddala się od punktu startu?

<details>
<summary>Odpowiedź</summary>

$x = \dfrac{F_0}{m\omega^2}(1 - \cos\omega t)$ — ciało oscyluje między $0$ a $2F_0/(m\omega^2)$, nie oddala się.
</details>

3. Pokaż, że $\vec{F} = d\vec{p}/dt$ sprowadza się do $\vec{F} = m\vec{a}$ tylko wtedy, gdy masa jest stała. Jaki dodatkowy wyraz pojawia się, gdy masa się zmienia?

<details>
<summary>Odpowiedź</summary>

$\dfrac{d(m\vec{v})}{dt} = m\dfrac{d\vec{v}}{dt} + \vec{v}\dfrac{dm}{dt}$. Wyraz $\vec{v}\,dm/dt$ ma jednak sens fizyczny dopiero po uwzględnieniu prędkości dołączanej lub odrzucanej masy — patrz rakieta (05.05).
</details>

### C. Zadania z arkuszy maturalnych CKE

Zadania z egzaminów maturalnych (poziom rozszerzony, formuła 2023), w których ten temat jest potrzebny. Rozwiąż je samodzielnie, a potem porównaj z zasadami oceniania. Pełne zestawienie: [matura/README.md](../../matura/README.md).

- Maj 2023, zad. 2.1 — siły wzajemnego oddziaływania przy zderzeniu krążków (III zasada dynamiki) ([arkusz](https://cke.gov.pl/images/_EGZAMIN_MATURALNY_OD_2023/Arkusze_egzaminacyjne/2023/Fizyka/MFAP-R0-100-2305.pdf), [zasady oceniania](https://cke.gov.pl/images/_EGZAMIN_MATURALNY_OD_2023/Arkusze_egzaminacyjne/2023/Fizyka/MFAP-R0-100-2305-zasady.pdf))
- Maj 2024, zad. 1.1 — zmiana przyspieszenia spadającej kropli (siła wypadkowa) (temat pomocniczy) ([arkusz](https://cke.gov.pl/images/_EGZAMIN_MATURALNY_OD_2023/Arkusze_egzaminacyjne/2024/Fizyka/MFAP-R0-100-A-2405-arkusz.pdf), [zasady oceniania](https://cke.gov.pl/egzamin-maturalny/egzamin-maturalny-w-formule-2023/arkusze/2024-2/))

## Źródła

- OpenStax, *Fizyka dla szkół wyższych*, t. 1, rozdz. 5 — §5.1–5.6: zasady dynamiki, masa i ciężar, rodzaje sił.
- Halliday, Resnick, Walker, *Podstawy fizyki* — wyd. 2015: t. 1, §5.1–5.2; wyd. 1: t. 1, §5.1–5.7.
- Symulacja PhET *Siły i ruch: podstawy*.
