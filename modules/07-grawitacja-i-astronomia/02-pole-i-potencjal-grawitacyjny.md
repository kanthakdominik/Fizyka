# 07.02 — Natężenie pola, potencjał i energia grawitacyjna

> **Moduł:** [07 — Grawitacja i elementy astronomii](README.md) · **Poziom:** 🟢🔵 matura R + studia · **Status:** ✅ pełny
>
> **Czytaj:**
>
> - OpenStax, *Fizyka dla szkół wyższych*, t. 1, rozdz. 13: [§13.3](https://openstax.org/books/fizyka-dla-szk%C3%B3%C5%82-wy%C5%BCszych-tom-1/pages/13-3-energia-potencjalna-i-calkowita-pola-grawitacyjnego) · [wstęp do rozdziału](https://openstax.org/books/fizyka-dla-szk%C3%B3%C5%82-wy%C5%BCszych-tom-1/pages/13-wstep)
> - Halliday, Resnick, Walker, *Podstawy fizyki*, wyd. 2015, t. 2: §13.5 (s. 49)
> - Halliday, Resnick, Walker, *Podstawy fizyki*, wyd. 1 (2003), t. 2: [§14.6, s. 37](https://home.agh.edu.pl/~czapli/Resnick_2.pdf#page=53) — PDF z serwera AGH

← [Prawo powszechnego ciążenia](01-prawo-grawitacji.md) · [spis modułu](README.md) · [Orbity, satelity i prędkości kosmiczne](03-orbity-i-predkosci-kosmiczne.md) →

## Po co to jest

Pojęcie **pola** pozwala opisać grawitację bez pytania, kto kogo przyciąga: masa wytwarza wokół siebie pole, a pole działa na inne masy. Ten sam język (natężenie, potencjał, energia potencjalna, linie pola, powierzchnie ekwipotencjalne) przeniesiemy niemal słowo w słowo do elektrostatyki (12). Z energii potencjalnej $-GMm/r$ wynika też prędkość ucieczki i energia potrzebna do wyniesienia satelity.

## Teoria w pigułce

**Natężenie pola grawitacyjnego** w danym punkcie to siła działająca na jednostkową masę próbną:

$$\vec{\gamma} = \frac{\vec{F}}{m}, \qquad \gamma = \frac{GM}{r^2}\ \text{(od masy punktowej, skierowane do niej)}.$$

Jednostka $\mathrm{N/kg} = \mathrm{m/s^2}$ — natężenie pola to po prostu przyspieszenie grawitacyjne. Przy powierzchni Ziemi pole jest w przybliżeniu jednorodne ($\gamma = g$); w dużej skali — **centralne**.

**Energia potencjalna** dwóch mas. Praca siły grawitacji przy przejściu od $r_1$ do $r_2$ zależy tylko od $r_1$ i $r_2$, więc siła jest zachowawcza. Przyjmując $U(\infty) = 0$:

$$U(r) = -\frac{GMm}{r}.$$

Energia jest **ujemna**: ciała związane grawitacyjnie mają mniej energii niż rozsunięte do nieskończoności. Blisko powierzchni $\Delta U \approx mgh$ (z rozwinięcia, 00.06).

**Potencjał grawitacyjny** to energia potencjalna na jednostkę masy:

$$V(r) = \frac{U}{m} = -\frac{GM}{r}, \qquad [V] = \mathrm{J/kg}.$$

Praca przy przeniesieniu masy $m$ między punktami: $W = -m\Delta V$. Natężenie pola to „spadek” potencjału: $\gamma_r = -dV/dr$.

**Powierzchnie ekwipotencjalne** (stałego potencjału) wokół kuli to sfery; linie pola są do nich prostopadłe.

**Prędkość ucieczki** (druga prędkość kosmiczna) — najmniejsza prędkość, z jaką ciało musi opuścić powierzchnię, żeby nie wróciło (dotrze do nieskończoności z $v = 0$):

$$\tfrac12mv^2 - \frac{GMm}{R} = 0 \Rightarrow v_{II} = \sqrt{\frac{2GM}{R}}.$$

Dla Ziemi 11,2 km/s, dla Księżyca 2,4 km/s.

## Wzory i założenia

| Wzór | Znaczenie | Kiedy obowiązuje |
|---|---|---|
| $\gamma = GM/r^2$ | natężenie pola | na zewnątrz kuli o symetrii sferycznej |
| $U = -GMm/r$ | energia potencjalna | $U(\infty) = 0$ |
| $V = -GM/r$ | potencjał | j.w. |
| $\gamma_r = -dV/dr$ | związek pola z potencjałem | 1D/radialnie |
| $\Delta U = GMm\left(\dfrac{1}{r_1} - \dfrac{1}{r_2}\right)$ | praca przy oddaleniu z $r_1$ do $r_2$ | — |
| $v_{II} = \sqrt{2GM/R}$ | prędkość ucieczki | bez oporu atmosfery i innych ciał |
| $\gamma(r) = GMr/R^3$ | pole wewnątrz jednorodnej kuli | $r < R$ |

## Przykład rozwiązany

**Zadanie.** Ile energii trzeba, żeby podnieść satelitę o masie 1000 kg z powierzchni Ziemi na wysokość 400 km (sama zmiana energii potencjalnej)? Porównaj z wynikiem wzoru $mgh$. ($GM = 3{,}986\cdot10^{14}\ \mathrm{m^3/s^2}$, $R = 6371\ \mathrm{km}$.)

$$\Delta U = GMm\left(\frac1R - \frac1{R + h}\right) = 3{,}986\cdot10^{14}\cdot1000\left(\frac{1}{6{,}371\cdot10^6} - \frac{1}{6{,}771\cdot10^6}\right) \approx 3{,}70\cdot10^9\ \mathrm{J}.$$

Wzór $mgh$ daje $3{,}92\cdot10^9\ \mathrm{J}$ — o 6% za dużo, bo pomija spadek $g$ z wysokością. (Żeby satelita utrzymał się na orbicie, trzeba mu jeszcze nadać energię kinetyczną — ok. $2{,}9\cdot10^{10}\ \mathrm{J}$, prawie 8 razy więcej, 07.03.)

### Wersja z rachunkiem różniczkowym i całkowym

**Wyprowadzenie $U(r)$.** Praca siły grawitacji przy przejściu z $r$ do nieskończoności:

$$W = \int_r^\infty\left(-\frac{GMm}{r'^2}\right)dr' = -\frac{GMm}{r}, \qquad U(r) = U(\infty) - W = -\frac{GMm}{r}.$$

**Tunel przez Ziemię.** Wewnątrz jednorodnej kuli przyciąga tylko masa leżąca bliżej środka (07.05): $M(r) = M\dfrac{r^3}{R^3}$, więc $\gamma = \dfrac{GMr}{R^3}$ — rośnie liniowo z $r$. Ciało puszczone w tunelu przez środek Ziemi ma przyspieszenie $\ddot{r} = -\dfrac{GM}{R^3}r$ — to ruch harmoniczny (00.05) z okresem

$$T = 2\pi\sqrt{\frac{R^3}{GM}} \approx 5060\ \mathrm{s} \approx 84\ \mathrm{min}.$$

Ciekawostka: to dokładnie okres satelity krążącego tuż nad powierzchnią.

## Typowe pułapki

- **Dodatnia energia potencjalna.** Przy zerze w nieskończoności $U < 0$ — ciało zbliżające się do planety „traci” energię potencjalną.
- **$mgh$ dla dużych wysokości.** Działa tylko dla $h \ll R$.
- **Prędkość ucieczki zależy od kierunku.** Nie zależy (pomijając obrót Ziemi i atmosferę) — energia jest skalarem.
- **Natężenie pola wewnątrz planety rośnie, im głębiej.** Dla jednorodnej kuli maleje liniowo do zera w środku.

## Doświadczenie / symulacja

**Symulacja PhET:** *Grawitacja i orbity* (*Gravity and Orbits*, [phet.colorado.edu/pl](https://phet.colorado.edu/pl/)) — wystrzel „pocisk” z różną prędkością i obserwuj przejście od orbity zamkniętej do ucieczki.

**Python:** potencjał i natężenie pola Ziemi wewnątrz i na zewnątrz (model jednorodnej kuli).

```python
import numpy as np
import matplotlib.pyplot as plt

GM, R = 3.986e14, 6.371e6
r = np.linspace(0.01, 4, 400) * R
gamma = np.where(r < R, GM*r/R**3, GM/r**2)
V = np.where(r < R, -GM*(3*R**2 - r**2)/(2*R**3), -GM/r)
print(f"V na powierzchni = {-GM/R:.3e} J/kg, w środku = {-1.5*GM/R:.3e} J/kg")
print(f"prędkość ucieczki = {np.sqrt(2*GM/R)/1000:.2f} km/s; okres tunelu = {2*np.pi*np.sqrt(R**3/GM)/60:.1f} min")

fig, ax = plt.subplots(1, 2, figsize=(9, 3.5))
ax[0].plot(r/R, gamma); ax[0].set_xlabel("r / R"); ax[0].set_ylabel("γ [m/s²]"); ax[0].grid(True)
ax[1].plot(r/R, V/1e6); ax[1].set_xlabel("r / R"); ax[1].set_ylabel("V [MJ/kg]"); ax[1].grid(True)
plt.tight_layout(); plt.show()
```

## Zadania

### A. Poziom maturalny

1. Oblicz prędkość ucieczki z Ziemi i z Księżyca.

<details>
<summary>Odpowiedź</summary>

$11{,}2\ \mathrm{km/s}$ i $2{,}4\ \mathrm{km/s}$.
</details>

2. Ile wynosi potencjał grawitacyjny Ziemi na jej powierzchni? Ile energii potrzeba, żeby 1 kg uciekł z Ziemi?

<details>
<summary>Odpowiedź</summary>

$V = -GM/R \approx -6{,}26\cdot10^7\ \mathrm{J/kg}$; potrzeba $62{,}6\ \mathrm{MJ}$.
</details>

3. Jak zmieni się natężenie pola grawitacyjnego i potencjał, gdy odległość od środka Ziemi wzrośnie dwukrotnie?

<details>
<summary>Odpowiedź</summary>

Natężenie zmaleje 4 razy, potencjał (wartość bezwzględna) — 2 razy.
</details>

4. Rakieta oddala się od Ziemi z wyłączonym silnikiem. Jak zmieniają się jej energia kinetyczna, potencjalna i całkowita?

<details>
<summary>Odpowiedź</summary>

Kinetyczna maleje, potencjalna rośnie (staje się mniej ujemna), całkowita stała.
</details>

### B. Poziom akademicki

1. Wyprowadź okres drgań w tunelu przez środek Ziemi i porównaj z okresem satelity krążącego tuż nad powierzchnią.

<details>
<summary>Odpowiedź</summary>

$\ddot{r} = -\dfrac{GM}{R^3}r \Rightarrow T = 2\pi\sqrt{R^3/GM} \approx 84\ \mathrm{min}$. Satelita: $v^2/R = GM/R^2 \Rightarrow T = 2\pi R/v = 2\pi\sqrt{R^3/GM}$ — ten sam.
</details>

2. Pokaż, że potencjał w środku jednorodnej kuli wynosi $-\dfrac{3GM}{2R}$.

<details>
<summary>Odpowiedź</summary>

$V(0) = V(R) - \displaystyle\int_R^0\gamma\,dr$, z $\gamma$ skierowanym do środka: $V(0) = -\dfrac{GM}{R} - \int_0^R\dfrac{GMr}{R^3}dr = -\dfrac{GM}{R} - \dfrac{GM}{2R}$.
</details>

3. Z jaką prędkością meteoryt uderzy w Ziemię (bez atmosfery), jeśli daleko od niej miał prędkość 5 km/s?

<details>
<summary>Odpowiedź</summary>

$v = \sqrt{v_\infty^2 + v_{II}^2} = \sqrt{25 + 125{,}4} \approx 12{,}3\ \mathrm{km/s}$.
</details>

4. Promień, przy którym prędkość ucieczki równa się prędkości światła, to promień Schwarzschilda $r_s = 2GM/c^2$. Oblicz go dla Słońca i dla Ziemi.

<details>
<summary>Odpowiedź</summary>

Słońce: ok. 3 km; Ziemia: ok. 9 mm. (Poprawny wynik daje dopiero ogólna teoria względności, ale wzór wychodzi ten sam.)
</details>

### C. Zadania z arkuszy maturalnych CKE

Zadania z egzaminów maturalnych (poziom rozszerzony, formuła 2023), w których ten temat jest potrzebny. Rozwiąż je samodzielnie, a potem porównaj z zasadami oceniania. Pełne zestawienie: [matura/README.md](../../matura/README.md).

- Maj 2024, zad. 5.2 — punkt między Ziemią a Księżycem, w którym siły się równoważą (temat pomocniczy) ([arkusz](https://cke.gov.pl/images/_EGZAMIN_MATURALNY_OD_2023/Arkusze_egzaminacyjne/2024/Fizyka/MFAP-R0-100-A-2405-arkusz.pdf), [zasady oceniania](https://cke.gov.pl/egzamin-maturalny/egzamin-maturalny-w-formule-2023/arkusze/2024-2/))

## Źródła

- OpenStax, *Fizyka dla szkół wyższych*, t. 1, rozdz. 13 — §13.3: energia potencjalna i całkowita w polu grawitacyjnym, prędkość ucieczki.
- Halliday, Resnick, Walker, *Podstawy fizyki* — wyd. 2015: t. 2, §13.5; wyd. 1: t. 2, §14.6.
- Symulacja PhET *Grawitacja i orbity*.
