# 12.02 — Natężenie pola, linie pola i dipol

> **Moduł:** [12 — Elektrostatyka](README.md) · **Poziom:** 🟢 matura R · **Status:** ✅ pełny
>
> **Czytaj:**
>
> - OpenStax, *Fizyka dla szkół wyższych*, t. 2, rozdz. 5: [§5.4 i §5.6–5.7](https://openstax.org/books/fizyka-dla-szk%C3%B3%C5%82-wy%C5%BCszych-tom-2/pages/5-4-pole-elektryczne) · [wstęp do rozdziału](https://openstax.org/books/fizyka-dla-szk%C3%B3%C5%82-wy%C5%BCszych-tom-2/pages/5-wstep)
> - Halliday, Resnick, Walker, *Podstawy fizyki*, wyd. 2015, t. 3: §22.1–22.3 (s. 29), §22.6–22.7 (s. 48)
> - Halliday, Resnick, Walker, *Podstawy fizyki*, wyd. 1 (2003), t. 3: [§23.1–23.5, s. 19](https://home.agh.edu.pl/~czapli/Resnick_3.pdf#page=29), [§23.8–23.9, s. 33](https://home.agh.edu.pl/~czapli/Resnick_3.pdf#page=43) — PDF z serwera AGH

← [Ładunek elektryczny i prawo Coulomba](01-ladunek-i-prawo-coulomba.md) · [spis modułu](README.md) · [Pole rozkładów ciągłych ładunku](03-pole-rozkladow-ciaglych.md) →

## Po co to jest

Pole elektryczne pozwala opisać oddziaływanie bez pytania, skąd ładunek „wie” o innym ładunku. Każdy ładunek wytwarza wokół siebie pole, a pole działa na ładunki, które się w nim znajdą. To pojęcie okaże się rzeczywistym bytem fizycznym, który niesie energię i rozchodzi się jako fala elektromagnetyczna (16). Na polu elektrycznym działają oscyloskopy i dawne kineskopy, drukarki atramentowe, akceleratory i elektroforeza w laboratoriach. Dipol elektryczny opisuje cząsteczkę wody i działanie kuchenki mikrofalowej.

## Teoria w pigułce

**Natężenie pola elektrycznego** to siła działająca na mały dodatni ładunek próbny, podzielona przez ten ładunek:

$$\vec E = \frac{\vec F}{q_0}, \qquad [E] = \mathrm{N/C} = \mathrm{V/m}.$$

Na ładunek $q$ w polu działa siła $\vec F = q\vec E$. Na ładunek ujemny działa ona przeciwnie do pola.

**Pole ładunku punktowego** jest skierowane radialnie, od ładunku dodatniego i do ujemnego:

$$E = k\frac{\lvert q\rvert}{r^2}.$$

Pole wielu ładunków to suma wektorowa pól od każdego z nich (**superpozycja**).

**Linie pola** to krzywe styczne w każdym punkcie do $\vec E$:
- zaczynają się na ładunkach dodatnich, a kończą na ujemnych lub w nieskończoności;
- nigdy się nie przecinają;
- ich gęstość jest proporcjonalna do $E$.

**Pole jednorodne** ma wszędzie tę samą wartość i kierunek, na przykład między okładkami płaskiego kondensatora (12.06). Ładunek porusza się w nim ze stałym przyspieszeniem $\vec a = q\vec E/m$, czyli jak ciało w rzucie (02.05). Tak odchyla się wiązkę elektronów w oscyloskopie.

**Dipol elektryczny** to dwa ładunki $\pm q$ w odległości $d$. Opisuje go **moment dipolowy** $\vec p = q\vec d$, skierowany od $-q$ do $+q$. Wiele cząsteczek, np. $\mathrm{H_2O}$, to trwałe dipole.
- Pole daleko od dipola maleje jak $1/r^3$. Na osi wynosi $E \approx 2kp/r^3$.
- W polu jednorodnym na dipol działa moment siły $\vec\tau = \vec p\times\vec E$. Ma on energię potencjalną $U = -\vec p\cdot\vec E$ i obraca się zgodnie z polem.
- W polu niejednorodnym działa na niego też siła wypadkowa, wciągająca go w obszar silniejszego pola.

## Wzory i założenia

| Wzór | Znaczenie | Kiedy obowiązuje |
|---|---|---|
| $\vec E = \vec F/q_0$, $\ \vec F = q\vec E$ | definicja natężenia pola | $q_0$ mały, nie zaburza źródeł |
| $E = k\lvert q\rvert/r^2$ | pole ładunku punktowego | — |
| $\vec E = \sum_i\vec E_i$ | superpozycja | — |
| $\vec p = q\vec d$ | moment dipolowy | od $-q$ do $+q$ |
| $E_{\text{oś}} \approx 2kp/r^3$ | pole na osi dipola | $r \gg d$ |
| $\vec\tau = \vec p\times\vec E$, $\ U = -\vec p\cdot\vec E$ | dipol w polu | pole jednorodne |

## Przykład rozwiązany

**Zadanie 1.** Ładunki $+2\ \mu\mathrm C$ i $-2\ \mu\mathrm C$ są odległe o 10 cm. Oblicz natężenie pola (a) w połowie odległości między nimi, (b) w punkcie odległym o 10 cm od środka, na symetralnej.

(a) Oba pola mają zwrot od ładunku dodatniego do ujemnego: $E = 2\cdot k\dfrac{2\cdot10^{-6}}{0{,}05^2} \approx 1{,}44\cdot10^7\ \mathrm{N/C}$.

(b) Odległość od każdego ładunku: $\sqrt{0{,}05^2 + 0{,}1^2} \approx 0{,}112\ \mathrm m$. Składowe pionowe się znoszą, a poziome dodają: $E = 2\cdot\dfrac{kq}{r^2}\cdot\dfrac{0{,}05}{r} \approx 1{,}29\cdot10^6\ \mathrm{N/C}$, równolegle do osi dipola, w stronę ładunku ujemnego.

**Zadanie 2.** Elektron o prędkości $10^7\ \mathrm{m/s}$ wlatuje prostopadle do linii pola między okładki o długości 5 cm. Pole ma natężenie 1000 N/C. O ile odchyli się elektron?

$a = eE/m \approx 1{,}76\cdot10^{14}\ \mathrm{m/s^2}$, czas przelotu $t = 5\cdot10^{-9}\ \mathrm s$, odchylenie $y = \tfrac12at^2 \approx 2{,}2\ \mathrm{mm}$. Ciężar elektronu ($\sim10^{-29}\ \mathrm N$) jest bez znaczenia wobec siły $eE \approx 1{,}6\cdot10^{-16}\ \mathrm N$.

## Typowe pułapki

- **Pole zależy od ładunku próbnego.** Pole wytwarzają źródła. Ładunek próbny tylko je mierzy.
- **Ładunek porusza się wzdłuż linii pola.** Wzdłuż linii skierowana jest siła, czyli przyspieszenie. Tor pokrywa się z linią tylko wtedy, gdy ładunek startuje ze spoczynku na prostej linii pola.
- **Dodawanie wartości pól.** Pola dodaje się wektorowo, często przez rozkład na składowe i wykorzystanie symetrii.
- **Pole ujemnego ładunku.** Pole jest skierowane do ładunku ujemnego, a siła działająca na elektron jest przeciwna do pola.
- **Dipol w polu jednorodnym przesuwa się.** Wypadkowa siła wynosi zero. Działa tylko moment siły.

## Doświadczenie / symulacja

**Linie pola z kaszy manny.** W płaskim naczyniu z olejem rycynowym (lub olejem jadalnym) rozsyp kaszę mannę lub nasiona trawy. Włóż dwie elektrody połączone z elektroforem albo maszyną elektrostatyczną. Ziarna polaryzują się i ustawiają wzdłuż linii pola. Uwaga: wysokie napięcie, tylko pod opieką nauczyciela.

**Symulacja PhET:** *Ładunki i pola* (*Charges and Fields*) — rozmieszczaj ładunki, mierz pole czujnikiem, rysuj linie ekwipotencjalne ([phet.colorado.edu/pl](https://phet.colorado.edu/pl/)).

**Python:** linie pola dipola i pole w wybranym punkcie z superpozycji.

```python
import numpy as np
import matplotlib.pyplot as plt

k = 8.9875e9
ladunki = [(2e-6, (-0.05, 0.0)), (-2e-6, (0.05, 0.0))]

def pole(x, y):
    Ex, Ey = np.zeros_like(x), np.zeros_like(y)
    for q, (x0, y0) in ladunki:
        dx, dy = x - x0, y - y0
        r3 = (dx**2 + dy**2)**1.5
        Ex += k*q*dx/r3; Ey += k*q*dy/r3
    return Ex, Ey

for p in [(0.0, 0.0), (0.0, 0.1)]:
    Ex, Ey = pole(np.array(p[0]), np.array(p[1]))
    print(f"E{p} = ({float(Ex):.3e}, {float(Ey):.3e}) N/C")

x, y = np.meshgrid(np.linspace(-0.2, 0.2, 300), np.linspace(-0.15, 0.15, 300))
Ex, Ey = pole(x, y)
plt.streamplot(x, y, Ex, Ey, density=1.4, color=np.log10(np.hypot(Ex, Ey)), cmap="viridis")
for q, (x0, y0) in ladunki:
    plt.plot(x0, y0, "ro" if q > 0 else "bo", ms=10)
plt.gca().set_aspect("equal"); plt.title("linie pola dipola"); plt.show()
```

## Zadania

### A. Poziom maturalny

1. Oblicz natężenie pola ładunku 1 nC w odległości 10 cm.

<details>
<summary>Odpowiedź</summary>

$E \approx 900\ \mathrm{N/C}$.
</details>

2. Kropla oleju o masie $3{,}8\cdot10^{-15}\ \mathrm{kg}$ niesie jeden ładunek elementarny. Jakie pole elektryczne utrzyma ją w spoczynku (doświadczenie Millikana)?

<details>
<summary>Odpowiedź</summary>

$eE = mg \Rightarrow E \approx 2{,}3\cdot10^5\ \mathrm{N/C}$, skierowane w dół, jeśli ładunek kropli jest ujemny (w górę dla dodatniego).
</details>

3. Ładunki $+q$ i $+4q$ są odległe o 30 cm. W którym punkcie natężenie pola jest równe zeru?

<details>
<summary>Odpowiedź</summary>

Na odcinku między nimi, 10 cm od ładunku $q$ (jak równowaga ładunku w 12.01, zadanie A4).
</details>

4. Narysuj linie pola dla dwóch równych ładunków dodatnich. Czym różni się ten obraz od dipola?

<details>
<summary>Odpowiedź</summary>

Linie wychodzą z obu ładunków i rozbiegają się do nieskończoności. Między ładunkami jest punkt zerowego pola, a linie się tam odpychają. W dipolu linie łączą ładunki.
</details>

### B. Poziom akademicki _(opcjonalnie — rozszerzenie z rachunkiem)_

1. Wyprowadź pole na osi dipola i pokaż, że dla $z \gg d$ wynosi $2kp/z^3$.

<details>
<summary>Odpowiedź</summary>

$E = kq\left[\dfrac{1}{(z - d/2)^2} - \dfrac{1}{(z + d/2)^2}\right] = kq\dfrac{2zd}{(z^2 - d^2/4)^2} \approx \dfrac{2kqd}{z^3}$.
</details>

2. Cząsteczka wody ma moment dipolowy $6{,}2\cdot10^{-30}\ \mathrm{C\cdot m}$. Oblicz największy moment siły w polu $10^6\ \mathrm{N/C}$ oraz energię potrzebną do odwrócenia dipola. Porównaj z $kT$ w 300 K. Co z tego wynika?

<details>
<summary>Odpowiedź</summary>

$\tau_{\max} = pE = 6{,}2\cdot10^{-24}\ \mathrm{N\cdot m}$, $\Delta U = 2pE \approx 1{,}2\cdot10^{-23}\ \mathrm J$, a $kT \approx 4{,}1\cdot10^{-21}\ \mathrm J$. Ruchy cieplne są 300 razy silniejsze, więc pole porządkuje dipole tylko w niewielkim stopniu.
</details>

3. Dipol o momencie $p$ i momencie bezwładności $I$ wychylono o mały kąt w polu $E$. Pokaż, że wykonuje drgania harmoniczne, i podaj okres.

<details>
<summary>Odpowiedź</summary>

$I\ddot\theta = -pE\sin\theta \approx -pE\theta$, więc $T = 2\pi\sqrt{I/(pE)}$, jak wahadło (09.03).
</details>

### C. Zadania z arkuszy maturalnych CKE

Zadania z egzaminów maturalnych (poziom rozszerzony, formuła 2023), w których ten temat jest potrzebny. Rozwiąż je samodzielnie, a potem porównaj z zasadami oceniania. Pełne zestawienie: [matura/README.md](../../matura/README.md).

- Maj 2024, zad. 6 — natężenie pola układu ładunków w środku kwadratu ([arkusz](https://cke.gov.pl/images/_EGZAMIN_MATURALNY_OD_2023/Arkusze_egzaminacyjne/2024/Fizyka/MFAP-R0-100-A-2405-arkusz.pdf), [zasady oceniania](https://cke.gov.pl/egzamin-maturalny/egzamin-maturalny-w-formule-2023/arkusze/2024-2/))
- Maj 2026, zad. 7.2 — natężenie pola układu ładunków w punkcie P ([arkusz](https://oke.wroc.pl/egzamin-maturalny/egzamin-maturalny-2026-arkusze/), [zasady oceniania](https://cke.gov.pl/egzamin-maturalny/egzamin-maturalny-w-formule-2023/arkusze/))

## Źródła

- OpenStax, *Fizyka dla szkół wyższych*, t. 2, rozdz. 5 — §5.4 (pole elektryczne), §5.6 (linie pola), §5.7 (dipole elektryczne).
- Halliday, Resnick, Walker, *Podstawy fizyki* — wyd. 2015: t. 3, §22.1–22.3, §22.6–22.7; wyd. 1: t. 3, §23.1–23.5, §23.8–23.9.
- Symulacja PhET *Ładunki i pola*.
