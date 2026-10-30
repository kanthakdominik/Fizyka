# 04.03 — Moc i sprawność

> **Moduł:** [04 — Praca, energia i moc](README.md) · **Poziom:** 🟢 matura R · **Status:** ✅ pełny
>
> **Czytaj:**
>
> - OpenStax, *Fizyka dla szkół wyższych*, t. 1, rozdz. 7: [§7.4](https://openstax.org/books/fizyka-dla-szk%C3%B3%C5%82-wy%C5%BCszych-tom-1/pages/7-4-moc) · [wstęp do rozdziału](https://openstax.org/books/fizyka-dla-szk%C3%B3%C5%82-wy%C5%BCszych-tom-1/pages/7-wstep)
> - Halliday, Resnick, Walker, *Podstawy fizyki*, wyd. 2015, t. 1: §7.6 (s. 209)
> - Halliday, Resnick, Walker, *Podstawy fizyki*, wyd. 1 (2003), t. 1: [§7.7, s. 158](https://home.agh.edu.pl/~czapli/Resnick_1.pdf#page=170) — PDF z serwera AGH

← [Energia kinetyczna i twierdzenie o pracy i energii](02-energia-kinetyczna.md) · [spis modułu](README.md) · [Siły zachowawcze i energia potencjalna](04-energia-potencjalna.md) →

## Po co to jest

Ta sama praca może być wykonana szybko albo wolno — o tym mówi moc. Moc silnika, grzałki czy żarówki decyduje, jak szybko coś się rozpędzi, podgrzeje albo ile zapłacimy za prąd. Sprawność mówi, jaka część pobranej energii jest wykorzystana. Oba pojęcia są na każdej maturze i wracają przy termodynamice (silniki cieplne, 11) i prądzie elektrycznym (13).

## Teoria w pigułce

**Moc średnia** to praca wykonana w jednostce czasu:

$$\bar{P} = \frac{W}{\Delta t}, \qquad \text{moc chwilowa: } P = \frac{dW}{dt}.$$

Jednostka: wat, $1\ \mathrm{W} = 1\ \mathrm{J/s}$. Dawna jednostka koń mechaniczny: $1\ \mathrm{KM} \approx 736\ \mathrm{W}$.

**Moc a prędkość.** Dla siły działającej na ciało poruszające się z prędkością $\vec{v}$:

$$P = \vec{F}\cdot\vec{v} = Fv\cos\alpha.$$

Samochód jadący ze stałą prędkością musi pokonywać opory; moc silnika to iloczyn siły oporu i prędkości. Przy oporze powietrza $F \propto v^2$ moc rośnie jak $v^3$ — dlatego szybka jazda tak bardzo zwiększa zużycie paliwa.

**Energia a moc.** $W = P\cdot t$. Stąd jednostka energii elektrycznej: kilowatogodzina, $1\ \mathrm{kWh} = 3{,}6\ \mathrm{MJ}$ — energia, którą urządzenie o mocy 1 kW pobiera w ciągu godziny.

**Sprawność** urządzenia:

$$\eta = \frac{W_{\text{użyteczna}}}{W_{\text{pobrana}}} = \frac{P_{\text{użyteczna}}}{P_{\text{pobrana}}} < 1.$$

Reszta energii zamienia się zwykle w ciepło (tarcie, opór elektryczny). Typowe wartości: silnik elektryczny 85–95%, silnik spalinowy 25–40%, człowiek przy pracy mięśni ok. 20–25%.

## Wzory i założenia

| Wzór | Znaczenie | Kiedy obowiązuje |
|---|---|---|
| $\bar{P} = W/\Delta t$ | moc średnia | — |
| $P = dW/dt = \vec{F}\cdot\vec{v}$ | moc chwilowa | — |
| $W = \int P\,dt$ | praca przy zmiennej mocy | — |
| $\eta = P_{\text{uż}}/P_{\text{pob}}$ | sprawność | — |
| $P = mgv$ | moc podnoszenia ze stałą prędkością | pionowo, bez oporów |
| $1\ \mathrm{kWh} = 3{,}6\cdot10^6\ \mathrm{J}$ | przelicznik | — |

## Przykład rozwiązany

**Zadanie 1.** Samochód jedzie ze stałą prędkością 108 km/h. Opór powietrza wynosi 600 N, opór toczenia 200 N. Jaką moc musi dostarczać silnik do kół?

$P = Fv = (600 + 200)\cdot30 = 24\ \mathrm{kW}$ (ok. 33 KM).

**Zadanie 2.** Winda o masie 800 kg (z pasażerami) jedzie w górę ze stałą prędkością 1,5 m/s. Silnik ma sprawność 80%. Jaką moc pobiera z sieci?

Moc użyteczna: $P_{\text{uż}} = mgv = 800\cdot9{,}81\cdot1{,}5 \approx 11{,}8\ \mathrm{kW}$. Moc pobrana: $P = 11{,}8/0{,}8 \approx 14{,}7\ \mathrm{kW}$.

## Typowe pułapki

- **kW a kWh.** Kilowat to moc, kilowatogodzina — energia.
- **Sprawność większa od 1.** Niemożliwa; jeśli tak wychodzi, zamieniono energię użyteczną z pobraną.
- **$P = Fv$ z prędkością średnią.** Przy zmiennej prędkości tak liczona moc jest mocą chwilową w danej chwili, a nie średnią.
- **Moc stała przy rozpędzaniu.** Przy stałej sile moc rośnie z prędkością; przy stałej mocy siła maleje.

## Doświadczenie / symulacja

**Twoja moc.** Zmierz czas wbiegania po schodach na znaną wysokość (policz stopnie i zmierz jeden). Oblicz moc $mgh/t$. Porównaj z mocą czajnika elektrycznego i oszacuj, ile musiałbyś biegać, żeby zagotować 1 L wody (ok. 0,34 MJ).

**Pomiar sprawności czajnika.** Wlej 1 L wody o znanej temperaturze, zmierz czas do zagotowania i odczytaj moc z tabliczki. Sprawność $\eta = \dfrac{mc\Delta T}{Pt}$, gdzie $c = 4190\ \mathrm{J/(kg\cdot K)}$ (moduł 11).

**Python:** moc potrzebna do jazdy ze stałą prędkością (opór toczenia + opór powietrza).

```python
import numpy as np
import matplotlib.pyplot as plt

m, g, Cr = 1300, 9.81, 0.012            # masa [kg], współczynnik oporu toczenia
C, rho, A = 0.30, 1.2, 2.2              # opór powietrza
v = np.linspace(0, 160, 161) / 3.6
P_roll = Cr*m*g*v
P_air = 0.5*C*rho*A*v**3
for vk in (50, 90, 130):
    vv = vk/3.6
    print(f"{vk} km/h: {(Cr*m*g*vv + 0.5*C*rho*A*vv**3)/1000:.1f} kW")
plt.stackplot(v*3.6, P_roll/1000, P_air/1000, labels=["opór toczenia", "opór powietrza"])
plt.xlabel("prędkość [km/h]"); plt.ylabel("moc [kW]"); plt.grid(True); plt.legend(loc="upper left"); plt.show()
```

## Zadania

### A. Poziom maturalny

1. Dźwig podnosi ładunek o masie 500 kg na wysokość 12 m w ciągu 20 s. Jaka jest moc użyteczna dźwigu?

<details>
<summary>Odpowiedź</summary>

$P = mgh/t \approx 2{,}9\ \mathrm{kW}$.
</details>

2. Pompa o sprawności 60% przepompowuje 1000 L wody na wysokość 10 m w ciągu 5 min. Jaką moc pobiera?

<details>
<summary>Odpowiedź</summary>

$W_{\text{uż}} = 98{,}1\ \mathrm{kJ}$, $P_{\text{uż}} = 327\ \mathrm{W}$, $P_{\text{pob}} = 545\ \mathrm{W}$.
</details>

3. Czajnik o mocy 2 kW i sprawności 90% podgrzewa 1 L wody od $20\ ^\circ\mathrm{C}$ do $100\ ^\circ\mathrm{C}$ ($c = 4190\ \mathrm{J/(kg\cdot K)}$). Ile to trwa?

<details>
<summary>Odpowiedź</summary>

$Q = 335\ \mathrm{kJ}$, $t = 335\,200/(0{,}9\cdot2000) \approx 186\ \mathrm{s}$.
</details>

4. Rowerzysta jedzie ze stałą prędkością, rozwijając moc 200 W przeciwko łącznym oporom 25 N. Z jaką prędkością jedzie?

<details>
<summary>Odpowiedź</summary>

$v = P/F = 8\ \mathrm{m/s} \approx 29\ \mathrm{km/h}$.
</details>

5. Człowiek o masie 70 kg wbiega na piętro (3 m) w 5 s. Jaką średnią moc rozwija?

<details>
<summary>Odpowiedź</summary>

$P \approx 412\ \mathrm{W}$.
</details>

### B. Poziom akademicki _(opcjonalnie — rozszerzenie z rachunkiem)_

1. Samochód o masie 1200 kg rusza z miejsca, a silnik dostarcza stałą moc 60 kW do kół (pomiń opory). Jaką prędkość osiągnie po 5 s? Dlaczego ten model zawodzi dla $t \to 0$?

<details>
<summary>Odpowiedź</summary>

$\tfrac12mv^2 = Pt \Rightarrow v = \sqrt{2Pt/m} \approx 22{,}4\ \mathrm{m/s}$. Dla $t \to 0$ siła $F = P/v \to \infty$ — w rzeczywistości ogranicza ją tarcie opon.
</details>

2. Przy prędkości 90 km/h samochód potrzebuje 15 kW na pokonanie oporu powietrza. Ile przy 130 km/h?

<details>
<summary>Odpowiedź</summary>

$P \propto v^3$: $15\cdot(130/90)^3 \approx 45\ \mathrm{kW}$.
</details>

3. Na ciało o masie 2 kg, spoczywające w chwili $t = 0$, działa siła $F = 6t$ (N, s). Oblicz moc chwilową w $t = 2\ \mathrm{s}$ i moc średnią w przedziale od 0 do 2 s.

<details>
<summary>Odpowiedź</summary>

$v = 1{,}5t^2$, $P = Fv = 9t^3$, $P(2) = 72\ \mathrm{W}$. $W = \int_0^29t^3\,dt = 36\ \mathrm{J}$, $\bar{P} = 18\ \mathrm{W}$.
</details>

## Źródła

- OpenStax, *Fizyka dla szkół wyższych*, t. 1, rozdz. 7 — §7.4: moc.
- Halliday, Resnick, Walker, *Podstawy fizyki* — wyd. 2015: t. 1, §7.6; wyd. 1: t. 1, §7.7.
