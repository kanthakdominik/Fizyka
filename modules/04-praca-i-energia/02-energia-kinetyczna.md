# 04.02 — Energia kinetyczna i twierdzenie o pracy i energii

> **Moduł:** [04 — Praca, energia i moc](README.md) · **Poziom:** 🟢 matura R · **Status:** ✅ pełny
>
> **Czytaj:**
>
> - OpenStax, *Fizyka dla szkół wyższych*, t. 1, rozdz. 7: [§7.2–7.3](https://openstax.org/books/fizyka-dla-szk%C3%B3%C5%82-wy%C5%BCszych-tom-1/pages/7-2-energia-kinetyczna) · [wstęp do rozdziału](https://openstax.org/books/fizyka-dla-szk%C3%B3%C5%82-wy%C5%BCszych-tom-1/pages/7-wstep)
> - Halliday, Resnick, Walker, *Podstawy fizyki*, wyd. 2015, t. 1: §7.1–7.2 (s. 187)
> - Halliday, Resnick, Walker, *Podstawy fizyki*, wyd. 1 (2003), t. 1: [§7.1, s. 141](https://home.agh.edu.pl/~czapli/Resnick_1.pdf#page=153), [§7.3, s. 143](https://home.agh.edu.pl/~czapli/Resnick_1.pdf#page=155) — PDF z serwera AGH

← [Praca siły stałej i zmiennej](01-praca.md) · [spis modułu](README.md) · [Moc i sprawność](03-moc-i-sprawnosc.md) →

## Po co to jest

Energia kinetyczna mówi, ile pracy trzeba wykonać, żeby rozpędzić ciało — albo ile pracy ciało wykona, zanim się zatrzyma. Twierdzenie o pracy i energii pozwala rozwiązać wiele zadań z dynamiki bez liczenia przyspieszenia i czasu: drogę hamowania, siłę uderzenia, prędkość po przejściu odcinka. Na nim zbudowana jest zasada zachowania energii (04.05).

## Teoria w pigułce

**Energia kinetyczna** ciała o masie $m$ poruszającego się z prędkością $v$:

$$E_k = \tfrac12mv^2.$$

Jest skalarem, zawsze nieujemna, zależy od kwadratu prędkości: dwa razy szybszy samochód ma cztery razy większą energię.

**Twierdzenie o pracy i energii.** Praca wypadkowej wszystkich sił działających na ciało równa się zmianie jego energii kinetycznej:

$$W_{\text{wyp}} = \Delta E_k = \tfrac12mv_2^2 - \tfrac12mv_1^2.$$

Siły wykonujące pracę dodatnią rozpędzają ciało, ujemną — hamują.

**Skąd ten wzór.** Dla stałej siły: $F = ma$ oraz $v_2^2 = v_1^2 + 2as$ (02.02). Mnożąc drugie równanie przez $m/2$: $\tfrac12mv_2^2 - \tfrac12mv_1^2 = mas = Fs$.

**Kiedy go używać.** Gdy pytanie dotyczy prędkości i drogi, a nie czasu. Gdy siła zależy od położenia (sprężyna) — wtedy kinematyka jest trudna, a praca łatwa.

## Wzory i założenia

| Wzór | Znaczenie | Kiedy obowiązuje |
|---|---|---|
| $E_k = \tfrac12mv^2$ | energia kinetyczna | $v \ll c$ (dla prędkości bliskich $c$ — moduł 19) |
| $W_{\text{wyp}} = \Delta E_k$ | twierdzenie o pracy i energii | punkt materialny, układ inercjalny |
| $s = \dfrac{v^2}{2\mu g}$ | droga hamowania na poziomej drodze | stałe tarcie, brak innych sił poziomych |
| $\bar{F} = \dfrac{\Delta E_k}{s}$ | średnia siła na drodze $s$ | średnia względem drogi |

## Przykład rozwiązany

**Zadanie 1.** Samochód o masie 1000 kg przyspiesza od 20 m/s do 30 m/s. Jaką pracę wykonała siła wypadkowa?

$W = \tfrac12\cdot1000\cdot(30^2 - 20^2) = 250\ \mathrm{kJ}$.

Rozpędzenie od 0 do 20 m/s kosztuje tylko 200 kJ — przyrost energii o te same 10 m/s jest droższy przy większej prędkości.

**Zadanie 2.** Pocisk o masie 10 g lecący z prędkością 400 m/s wbija się w deskę na głębokość 10 cm. Oblicz średnią siłę oporu deski.

Energia kinetyczna: $E_k = \tfrac12\cdot0{,}01\cdot400^2 = 800\ \mathrm{J}$. Cała zostaje zamieniona na pracę oporu: $\bar{F}\cdot0{,}1 = 800$, $\bar{F} = 8\ \mathrm{kN}$ — ponad 80 000 razy więcej niż ciężar pocisku.

### Wersja z rachunkiem różniczkowym i całkowym

**Wyprowadzenie dla dowolnej siły.** Z II zasady i reguły łańcuchowej $a = \dfrac{dv}{dt} = \dfrac{dv}{dx}\dfrac{dx}{dt} = v\dfrac{dv}{dx}$:

$$W = \int_{x_1}^{x_2}F\,dx = \int_{x_1}^{x_2}mv\frac{dv}{dx}\,dx = \int_{v_1}^{v_2}mv\,dv = \tfrac12mv_2^2 - \tfrac12mv_1^2.$$

**Zadanie.** Na spoczywające ciało o masie $m$ działa siła malejąca liniowo z drogą: $F(x) = F_0(1 - x/L)$ dla $0 \le x \le L$. Jaką prędkość ma ciało w punkcie $x = L$?

$W = \int_0^LF_0(1 - x/L)\,dx = \tfrac12F_0L$, więc $v = \sqrt{F_0L/m}$.

## Typowe pułapki

- **Energia kinetyczna proporcjonalna do prędkości.** Do kwadratu — stąd czterokrotnie dłuższa droga hamowania przy dwukrotnie większej prędkości.
- **Praca jednej siły zamiast wypadkowej.** Twierdzenie dotyczy sumy prac wszystkich sił.
- **Energia kinetyczna jako wektor.** To skalar; nie ma kierunku.
- **Gramy we wzorze.** $\tfrac12mv^2$ z masą w gramach daje wynik 1000 razy za duży.

## Doświadczenie / symulacja

**Droga hamowania wózka.** Rozpędź wózek lub samochodzik zabawkowy na tę samą równię z dwóch różnych wysokości (np. 10 cm i 40 cm) i zmierz, jak daleko się toczy po poziomym dywanie. Sprawdź, że droga jest proporcjonalna do wysokości startu, czyli do energii kinetycznej na dole.

**Python:** droga hamowania samochodu z prędkości od 30 do 150 km/h na różnych nawierzchniach.

```python
import numpy as np
import matplotlib.pyplot as plt

g = 9.81
v = np.linspace(30, 150, 121) / 3.6
for mu, lab in [(0.8, "sucha"), (0.5, "mokra"), (0.1, "lód")]:
    plt.plot(v*3.6, v**2/(2*mu*g), label=f"{lab}, μ = {mu}")
for vk in (50, 100):
    print(f"{vk} km/h, sucha: {(vk/3.6)**2/(2*0.8*g):.1f} m")
plt.yscale("log"); plt.xlabel("prędkość [km/h]"); plt.ylabel("droga hamowania [m]"); plt.grid(True, which="both"); plt.legend()
plt.show()
```

## Zadania

### A. Poziom maturalny

1. Co ma większą energię kinetyczną: ciężarówka o masie 10 t jadąca z prędkością 10 m/s czy samochód o masie 1 t jadący 30 m/s?

<details>
<summary>Odpowiedź</summary>

Ciężarówka: 500 kJ wobec 450 kJ.
</details>

2. Prędkość samochodu wzrosła z 50 do 100 km/h. Ile razy wzrosła jego energia kinetyczna i droga hamowania?

<details>
<summary>Odpowiedź</summary>

4 razy (obie).
</details>

3. Młotek o masie 0,5 kg uderza w gwóźdź z prędkością 8 m/s i wbija go na głębokość 1 cm. Oblicz średnią siłę oporu drewna.

<details>
<summary>Odpowiedź</summary>

$\bar{F} = 16\ \mathrm{J}/0{,}01\ \mathrm{m} = 1600\ \mathrm{N}$.
</details>

4. Sanki z przykładu w temacie 01 (praca wypadkowa 720 J, masa 10 kg) ruszyły z miejsca. Jaką mają prędkość po 20 m?

<details>
<summary>Odpowiedź</summary>

$v = \sqrt{2\cdot720/10} = 12\ \mathrm{m/s}$.
</details>

5. Kulka o masie 0,1 kg spada swobodnie z wysokości 5 m. Oblicz jej energię kinetyczną i prędkość tuż przed uderzeniem.

<details>
<summary>Odpowiedź</summary>

$E_k = mgh \approx 4{,}9\ \mathrm{J}$, $v \approx 9{,}9\ \mathrm{m/s}$.
</details>

### B. Poziom akademicki _(opcjonalnie — rozszerzenie z rachunkiem)_

1. Ciało o masie 2 kg porusza się zgodnie z $x(t) = t^3$ (m, s). Oblicz pracę wypadkowej siły w przedziale od 0 do 2 s dwiema metodami: z energii kinetycznej i z całki $\int Fv\,dt$.

<details>
<summary>Odpowiedź</summary>

$v = 3t^2$, $E_k(2) = \tfrac12\cdot2\cdot144 = 144\ \mathrm{J}$. $F = m\ddot{x} = 12t$, $\int_0^212t\cdot3t^2\,dt = 9t^4\big|_0^2 = 144\ \mathrm{J}$.
</details>

2. Klocek o masie 0,5 kg uderza z prędkością 2 m/s w poziomą sprężynę ($k = 200\ \mathrm{N/m}$). O ile maksymalnie ją ściśnie (bez tarcia)?

<details>
<summary>Odpowiedź</summary>

$\tfrac12kx^2 = \tfrac12mv^2 \Rightarrow x = v\sqrt{m/k} = 0{,}1\ \mathrm{m}$.
</details>

3. Pokaż, że dla siły zależnej od czasu $\Delta E_k = \displaystyle\int\vec{F}\cdot\vec{v}\,dt$.

<details>
<summary>Odpowiedź</summary>

$\dfrac{d}{dt}\left(\tfrac12m\vec{v}\cdot\vec{v}\right) = m\vec{v}\cdot\dfrac{d\vec{v}}{dt} = \vec{F}\cdot\vec{v}$; całkujemy po czasie.
</details>

## Źródła

- OpenStax, *Fizyka dla szkół wyższych*, t. 1, rozdz. 7 — §7.2 (energia kinetyczna) i §7.3 (twierdzenie o pracy i energii).
- Halliday, Resnick, Walker, *Podstawy fizyki* — wyd. 2015: t. 1, §7.1–7.2; wyd. 1: t. 1, §7.1 i §7.3.
