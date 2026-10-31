# 12.05 — Potencjał, energia potencjalna i związek E z V

> **Moduł:** [12 — Elektrostatyka](README.md) · **Poziom:** 🟢🔵 matura R + studia · **Status:** ✅ pełny
>
> **Czytaj:**
>
> - OpenStax, *Fizyka dla szkół wyższych*, t. 2, rozdz. 7: [§7.1–7.6](https://openstax.org/books/fizyka-dla-szk%C3%B3%C5%82-wy%C5%BCszych-tom-2/pages/7-1-elektryczna-energia-potencjalna) · [wstęp do rozdziału](https://openstax.org/books/fizyka-dla-szk%C3%B3%C5%82-wy%C5%BCszych-tom-2/pages/7-wstep)
> - Halliday, Resnick, Walker, *Podstawy fizyki*, wyd. 2015, t. 3: §24.1–24.8 (s. 102)
> - Halliday, Resnick, Walker, *Podstawy fizyki*, wyd. 1 (2003), t. 3: [§25.1–25.11, s. 73](https://home.agh.edu.pl/~czapli/Resnick_3.pdf#page=83) — PDF z serwera AGH

← [Strumień pola i prawo Gaussa](04-prawo-gaussa.md) · [spis modułu](README.md) · [Kondensatory: pojemność, łączenie, energia](06-kondensatory.md) →

## Po co to jest

Napięcie, mierzone w woltach, jest na każdej baterii, gniazdku i zasilaczu. To różnica potencjałów elektrycznych. Potencjał jest wielkością skalarną, więc liczy się go łatwiej niż wektorowe pole. Opis energetyczny daje od razu prędkość elektronu w lampie rentgenowskiej, energię jonu w akceleratorze i pracę potrzebną do zbudowania układu ładunków. Elektronowolt, jednostka energii z fizyki atomowej i jądrowej, wynika wprost z tej definicji.

## Teoria w pigułce

**Energia potencjalna elektryczna.** Siła Coulomba jest zachowawcza (04.04), więc można zdefiniować energię potencjalną: $\Delta U = -W_{\text{pola}}$. Dla dwóch ładunków punktowych:

$$U = k\frac{q_1q_2}{r} \qquad (U = 0 \text{ w nieskończoności}).$$

Dla ładunków jednoimiennych $U > 0$ (trzeba wykonać pracę, by je zbliżyć). Dla różnoimiennych $U < 0$ (układ związany).

**Potencjał** to energia potencjalna na jednostkę ładunku: $V = U/q$, w woltach ($1\ \mathrm V = 1\ \mathrm{J/C}$). **Napięcie** to różnica potencjałów: $U_{AB} = V_A - V_B$. Ładunek przechodzący przez różnicę potencjałów $\Delta V$ zmienia energię o $q\Delta V$:

$$qU = \Delta E_k \quad\Rightarrow\quad v = \sqrt{\frac{2qU}{m}} \quad\text{(start ze spoczynku)}.$$

**Elektronowolt:** $1\ \mathrm{eV} = 1{,}602\cdot10^{-19}\ \mathrm J$ to energia, którą elektron zyskuje przy przejściu przez napięcie 1 V.

**Potencjał ładunku punktowego** i superpozycja (suma skalarna, ze znakami):

$$V = k\frac qr, \qquad V = \sum_ik\frac{q_i}{r_i}.$$

**Związek pola z potencjałem:**

$$V_B - V_A = -\int_A^B\vec E\cdot d\vec l, \qquad E_x = -\frac{\partial V}{\partial x}, \qquad \vec E = -\nabla V.$$

- Pole wskazuje kierunek najszybszego spadku potencjału.
- W polu jednorodnym $U = Ed$, stąd jednostka V/m.
- **Powierzchnie ekwipotencjalne** (stałego $V$) są prostopadłe do linii pola. Przesuwanie ładunku po nich nie wymaga pracy.
- Przewodnik w równowadze ma we wszystkich punktach ten sam potencjał.

## Wzory i założenia

| Wzór | Znaczenie | Kiedy obowiązuje |
|---|---|---|
| $U = kq_1q_2/r$ | energia potencjalna pary ładunków | $U(\infty) = 0$ |
| $V = kq/r$, $\ V = \sum kq_i/r_i$ | potencjał ładunku punktowego, superpozycja | — |
| $W_{A\to B} = q(V_A - V_B)$ | praca pola | — |
| $qU = \Delta E_k$ | przyspieszanie ładunku | bez innych sił |
| $U = Ed$ | napięcie w polu jednorodnym | — |
| $\vec E = -\nabla V$, $\ \Delta V = -\int\vec E\cdot d\vec l$ | związek pola i potencjału | — |

## Przykład rozwiązany

**Zadanie 1.** Elektron przyspieszono ze spoczynku napięciem 1000 V. Oblicz jego energię w eV i J oraz prędkość.

$E_k = 1000\ \mathrm{eV} = 1{,}6\cdot10^{-16}\ \mathrm J$. $v = \sqrt{2\cdot1{,}602\cdot10^{-19}\cdot1000/9{,}11\cdot10^{-31}} \approx 1{,}9\cdot10^7\ \mathrm{m/s}$, ok. 6% prędkości światła, więc wynik nierelatywistyczny jest dobry.

**Zadanie 2.** W wierzchołkach kwadratu o boku 10 cm umieszczono ładunki po $1\ \mu\mathrm C$. Ile pracy trzeba było wykonać, żeby zbudować ten układ, sprowadzając ładunki z nieskończoności?

Energia układu to suma po wszystkich 6 parach: 4 boki i 2 przekątne.

$W = kq^2\left(\dfrac{4}{a} + \dfrac{2}{a\sqrt2}\right) = 8{,}99\cdot10^{-3}(40 + 14{,}1) \approx 0{,}49\ \mathrm J$.

### Wersja z rachunkiem różniczkowym i całkowym

**Zadanie.** (a) Oblicz potencjał naładowanej metalowej kuli o promieniu $R$ jako całkę z pola. (b) Potencjał na osi pierścienia wynosi $V = kQ/\sqrt{z^2 + R^2}$. Wyprowadź z niego pole.

(a) Na zewnątrz $E = kQ/r^2$: $V(r) = -\displaystyle\int_\infty^r\frac{kQ}{r'^2}dr' = \frac{kQ}{r}$. Wewnątrz $E = 0$, więc $V = kQ/R$ jest stały. Generator Van de Graaffa o promieniu kuli 20 cm osiąga przy polu przebicia $3\cdot10^6\ \mathrm{V/m}$ potencjał $V = ER = 600\ \mathrm{kV}$.

(b) $E_z = -\dfrac{dV}{dz} = \dfrac{kQz}{(z^2 + R^2)^{3/2}}$. To ten sam wynik co w 12.03, otrzymany bez całkowania wektorów: potencjał jest skalarem, więc sumuje się go łatwiej.

## Typowe pułapki

- **Potencjał jako wektor.** Potencjały dodaje się algebraicznie, ze znakami ładunków. Bez rozkładania na składowe.
- **$V = kq/r^2$.** Potencjał maleje jak $1/r$, pole jak $1/r^2$.
- **Zero pola = zero potencjału.** W środku kuli przewodzącej $E = 0$, ale $V = kQ/R$. W połowie odległości między $+q$ i $-q$ jest odwrotnie: $V = 0$, $E \ne 0$.
- **Znak pracy.** Ładunek dodatni samorzutnie przesuwa się do niższego potencjału, a elektron do wyższego.
- **eV jako jednostka napięcia.** eV to jednostka energii, a V napięcia.

## Doświadczenie / symulacja

**Mapa ekwipotencjalna na papierze.** Na arkuszu papieru przewodzącego (lub na tackę z wodą z kranu) połóż dwie elektrody podłączone do baterii 9 V. Woltomierzem z sondą znajdź punkty o tym samym napięciu względem jednej elektrody i narysuj linie ekwipotencjalne. Linie pola dorysuj prostopadle.

**Symulacja PhET:** *Ładunki i pola* (*Charges and Fields*) — narzędzie do rysowania linii ekwipotencjalnych i woltomierz.

**Python:** mapa potencjału dipola i pole jako gradient potencjału.

```python
import numpy as np
import matplotlib.pyplot as plt

k = 8.9875e9
ladunki = [(1e-9, (-0.05, 0.0)), (-1e-9, (0.05, 0.0))]
x, y = np.meshgrid(np.linspace(-0.2, 0.2, 401), np.linspace(-0.15, 0.15, 301))
V = sum(k*q/np.hypot(x - x0, y - y0) for q, (x0, y0) in ladunki)

dy, dx = y[1, 0] - y[0, 0], x[0, 1] - x[0, 0]
Ey, Ex = np.gradient(-V, dy, dx)                    # E = −∇V
i, j = 150, 200                                     # punkt (0, 0)
print(f"V(0,0) = {V[i, j]:.2f} V, Ex(0,0) = {Ex[i, j]:.0f} V/m (wzór: {2*k*1e-9/0.05**2:.0f})")
q, m = 1.602e-19, 9.109e-31
print(f"elektron po 1000 V: v = {np.sqrt(2*q*1000/m):.3e} m/s")

plt.contour(x, y, np.clip(V, -300, 300), levels=np.linspace(-300, 300, 25), cmap="coolwarm")
plt.streamplot(x, y, Ex, Ey, color="k", density=0.8, linewidth=0.5)
plt.gca().set_aspect("equal"); plt.title("linie ekwipotencjalne i linie pola"); plt.show()
```

## Zadania

### A. Poziom maturalny

1. Oblicz potencjał w odległości 10 cm od ładunku $1\ \mu\mathrm C$ i pracę potrzebną do przeniesienia ładunku $1\ \mathrm{nC}$ z nieskończoności do tego punktu.

<details>
<summary>Odpowiedź</summary>

$V \approx 89{,}9\ \mathrm{kV}$, $W = qV \approx 9\cdot10^{-5}\ \mathrm J$.
</details>

2. Okładki kondensatora są odległe o 1 cm, a napięcie wynosi 100 V. Oblicz natężenie pola i siłę działającą na elektron.

<details>
<summary>Odpowiedź</summary>

$E = 10^4\ \mathrm{V/m}$, $F = eE \approx 1{,}6\cdot10^{-15}\ \mathrm N$.
</details>

3. Proton przyspieszono ze spoczynku napięciem 1 MV. Oblicz jego energię w MeV i prędkość.

<details>
<summary>Odpowiedź</summary>

1 MeV, $v \approx 1{,}4\cdot10^7\ \mathrm{m/s}$.
</details>

4. Gdzie na odcinku łączącym ładunki $+q$ i $-q$ potencjał jest równy zeru? Czy pole też jest tam zerowe?

<details>
<summary>Odpowiedź</summary>

W środku (i na całej płaszczyźnie symetralnej). Pole nie jest zerowe; jest największe na odcinku właśnie w środku.
</details>

### B. Poziom akademicki

1. Potencjał w pewnym obszarze wynosi $V = 3x^2y - 2z$ (SI). Oblicz wektor natężenia pola w punkcie $(1, 2, 0)$.

<details>
<summary>Odpowiedź</summary>

$\vec E = -\nabla V = (-6xy, -3x^2, 2) = (-12, -3, 2)\ \mathrm{V/m}$.
</details>

2. Pokaż, że energia elektronu w atomie wodoru (model z orbitą kołową o promieniu $r$) wynosi $E = -\dfrac{ke^2}{2r}$. Oblicz ją w eV dla $r = 5{,}29\cdot10^{-11}\ \mathrm m$.

<details>
<summary>Odpowiedź</summary>

Z $mv^2/r = ke^2/r^2$: $E_k = ke^2/(2r)$, $U = -ke^2/r$, razem $-ke^2/(2r) \approx -13{,}6\ \mathrm{eV}$, czyli energia jonizacji wodoru.
</details>

3. Oblicz potencjał w środku pierścienia o ładunku $Q$ i promieniu $R$ oraz pracę potrzebną do przeniesienia ładunku $q$ z nieskończoności do środka. Dlaczego nie potrzeba do tego wektorów?

<details>
<summary>Odpowiedź</summary>

Wszystkie elementy są w odległości $R$: $V = kQ/R$, $W = kqQ/R$. Potencjał to skalar, więc wystarczy zsumować $k\,dq/R$.
</details>

4. Ile energii trzeba, żeby naładować kulę przewodzącą o promieniu $R$ do ładunku $Q$, dokładając kolejne porcje $dq$ z nieskończoności?

<details>
<summary>Odpowiedź</summary>

$W = \displaystyle\int_0^Q\frac{kq}{R}dq = \frac{kQ^2}{2R}$. Dla Van de Graaffa (13 μC, 0,2 m) to ok. 4 J.
</details>

### C. Zadania z arkuszy maturalnych CKE

Zadania z egzaminów maturalnych (poziom rozszerzony, formuła 2023), w których ten temat jest potrzebny. Rozwiąż je samodzielnie, a potem porównaj z zasadami oceniania. Pełne zestawienie: [matura/README.md](../../matura/README.md).

- Maj 2023, zad. 10.3 — napięcie przyspieszające elektron (temat pomocniczy) ([arkusz](https://cke.gov.pl/images/_EGZAMIN_MATURALNY_OD_2023/Arkusze_egzaminacyjne/2023/Fizyka/MFAP-R0-100-2305.pdf), [zasady oceniania](https://cke.gov.pl/images/_EGZAMIN_MATURALNY_OD_2023/Arkusze_egzaminacyjne/2023/Fizyka/MFAP-R0-100-2305-zasady.pdf))
- Maj 2024, zad. 10.2 — napięcie przyspieszające elektron (relatywistycznie) (temat pomocniczy) ([arkusz](https://cke.gov.pl/images/_EGZAMIN_MATURALNY_OD_2023/Arkusze_egzaminacyjne/2024/Fizyka/MFAP-R0-100-A-2405-arkusz.pdf), [zasady oceniania](https://cke.gov.pl/egzamin-maturalny/egzamin-maturalny-w-formule-2023/arkusze/2024-2/))

## Źródła

- OpenStax, *Fizyka dla szkół wyższych*, t. 2, rozdz. 7 — §7.1–7.6: elektryczna energia potencjalna, potencjał i różnica potencjałów, potencjał rozkładów ładunku, wyznaczanie pola z potencjału, powierzchnie ekwipotencjalne, zastosowania.
- Halliday, Resnick, Walker, *Podstawy fizyki* — wyd. 2015: t. 3, §24.1–24.8; wyd. 1: t. 3, §25.1–25.11.
- Symulacja PhET *Ładunki i pola*.
