# 13.01 — Natężenie i gęstość prądu, model przewodnictwa

> **Moduł:** [13 — Prąd stały](README.md) · **Poziom:** 🟢🔵 matura R + studia · **Status:** ✅ pełny
>
> **Czytaj:**
>
> - OpenStax, *Fizyka dla szkół wyższych*, t. 2, rozdz. 9: [§9.1–9.2](https://openstax.org/books/fizyka-dla-szk%C3%B3%C5%82-wy%C5%BCszych-tom-2/pages/9-1-prad-elektryczny) · [wstęp do rozdziału](https://openstax.org/books/fizyka-dla-szk%C3%B3%C5%82-wy%C5%BCszych-tom-2/pages/9-wstep)
> - Halliday, Resnick, Walker, *Podstawy fizyki*, wyd. 2015, t. 3: §26.1–26.2 (s. 178)
> - Halliday, Resnick, Walker, *Podstawy fizyki*, wyd. 1 (2003), t. 3: §27.1–27.3, s. 129 (skan t. 3 na serwerze AGH kończy się na s. 127 — dalsze strony tylko w wydaniu papierowym)

← (początek modułu) · [spis modułu](README.md) · [Opór, opór właściwy i prawo Ohma](02-opor-i-prawo-ohma.md) →

## Po co to jest

Prąd elektryczny to uporządkowany ruch ładunków. Zasila wszystko od latarki po sieć energetyczną. Model mikroskopowy pokazuje rzecz zaskakującą: elektrony w przewodzie płyną wolniej niż ślimak, a mimo to światło zapala się natychmiast. Ten sam model wyjaśnia, skąd bierze się opór i prawo Ohma (13.02), dlaczego metale grzeją się przy przepływie prądu i czym różnią się przewodniki od półprzewodników (23). Pojemność akumulatora w mAh to po prostu ładunek.

## Teoria w pigułce

**Natężenie prądu** to ładunek przepływający przez przekrój przewodnika w jednostce czasu:

$$I = \frac{dq}{dt}, \qquad I = \frac{\Delta q}{\Delta t}\ \text{(prąd stały)}, \qquad 1\ \mathrm A = 1\ \mathrm{C/s}.$$

Umowny kierunek prądu to kierunek ruchu ładunków dodatnich. W metalach elektrony płyną przeciwnie. Ładunek przepływający w czasie $t$ to $q = \int I\,dt$, czyli pole pod wykresem $I(t)$. Pojemność akumulatora 2000 mAh oznacza $2\ \mathrm A\cdot3600\ \mathrm s = 7200\ \mathrm C$.

**Gęstość prądu** $\vec J$ to prąd na jednostkę pola przekroju: $I = \int\vec J\cdot d\vec A$, dla jednorodnego przepływu $J = I/A$.

**Prędkość dryfu.** Elektrony w metalu poruszają się chaotycznie z ogromnymi prędkościami (ok. $10^6\ \mathrm{m/s}$). Pole elektryczne dodaje do tego powolny, uporządkowany dryf z prędkością $v_d$. Jeśli w jednostce objętości jest $n$ nośników o ładunku $q$:

$$I = nqv_dA, \qquad \vec J = nq\vec v_d.$$

W miedzi $n \approx 8{,}5\cdot10^{28}\ \mathrm{m^{-3}}$ (jeden elektron swobodny na atom).

**Dlaczego światło zapala się natychmiast?** Po włączeniu pole elektryczne rozchodzi się wzdłuż przewodu z prędkością bliską prędkości światła. Elektrony w całym obwodzie zaczynają dryfować prawie jednocześnie, jak woda w wypełnionym wężu ogrodowym.

**Model Drudego.** Elektron przyspiesza w polu $E$ przez średni czas $\tau$ między zderzeniami z jonami sieci. Potem „zapomina” prędkość. Średnia prędkość dryfu wynosi $v_d = \dfrac{eE}{m}\tau$, stąd

$$\vec J = \sigma\vec E, \qquad \sigma = \frac{ne^2\tau}{m}, \qquad \rho = \frac1\sigma.$$

$\sigma$ to przewodność właściwa, a $\rho$ opór właściwy. Gęstość prądu jest proporcjonalna do pola, co jest mikroskopową postacią prawa Ohma. Model daje dobre rzędy wielkości, ale pełny opis wymaga mechaniki kwantowej (23).

## Wzory i założenia

| Wzór | Znaczenie | Kiedy obowiązuje |
|---|---|---|
| $I = dq/dt$, $\ q = \int I\,dt$ | natężenie prądu, przepływający ładunek | — |
| $J = I/A$ | gęstość prądu | przepływ jednorodny |
| $I = nqv_dA$ | prąd a prędkość dryfu | — |
| $\vec J = \sigma\vec E$ | mikroskopowe prawo Ohma | przewodnik omowy |
| $\sigma = ne^2\tau/m$ | przewodność w modelu Drudego | metale, model klasyczny |

## Przykład rozwiązany

**Zadanie.** Miedziany przewód o przekroju 1 mm² przewodzi prąd 1 A. Oblicz prędkość dryfu elektronów i czas, w jakim elektron przesuwa się o 1 m.

$v_d = \dfrac{I}{neA} = \dfrac{1}{8{,}49\cdot10^{28}\cdot1{,}602\cdot10^{-19}\cdot10^{-6}} \approx 7{,}4\cdot10^{-5}\ \mathrm{m/s}$, czyli ok. 0,07 mm/s.

Przesunięcie o 1 m zajmuje ok. $1{,}4\cdot10^4\ \mathrm s \approx 3{,}8\ \mathrm h$.

### Wersja z rachunkiem różniczkowym i całkowym

**Zadanie.** Prąd rozładowania kondensatora maleje jak $I(t) = I_0e^{-t/\tau}$, gdzie $I_0 = 2\ \mathrm A$ i $\tau = 0{,}5\ \mathrm s$. Jaki ładunek przepłynie w ciągu pierwszej sekundy, a jaki łącznie? Oszacuj też $\tau$ dla miedzi w modelu Drudego ($\rho = 1{,}68\cdot10^{-8}\ \Omega\cdot\mathrm m$).

$$q(1\ \mathrm s) = \int_0^1I_0e^{-t/\tau}dt = I_0\tau(1 - e^{-2}) \approx 0{,}86\ \mathrm C, \qquad q_{\text{całk}} = I_0\tau = 1\ \mathrm C.$$

Model Drudego: $\tau = \dfrac{m}{ne^2\rho} = \dfrac{9{,}11\cdot10^{-31}}{8{,}49\cdot10^{28}\cdot(1{,}602\cdot10^{-19})^2\cdot1{,}68\cdot10^{-8}} \approx 2{,}5\cdot10^{-14}\ \mathrm s$. Przy prędkości elektronów ok. $1{,}6\cdot10^6\ \mathrm{m/s}$ daje to drogę między zderzeniami ok. 40 nm, czyli ok. 150 odległości między atomami. Klasycznie nie da się tego wyjaśnić. Elektrony rozpraszają się nie na samych jonach, lecz na drganiach sieci i defektach (23).

## Typowe pułapki

- **Elektrony płyną z prędkością światła.** Z prędkością bliską światłu rozchodzi się pole (sygnał). Same elektrony dryfują z prędkością ułamków milimetra na sekundę.
- **Kierunek prądu = kierunek ruchu elektronów.** Kierunek umowny jest przeciwny do ruchu elektronów.
- **Prąd „zużywa się” w żarówce.** Natężenie prądu na wejściu i wyjściu odbiornika jest takie samo. Zużywa się energia (13.03).
- **mAh to jednostka energii.** To jednostka ładunku. Energię daje dopiero pomnożenie przez napięcie (mAh × V = mWh).
- **Gęstość prądu a natężenie.** W cieńszym odcinku przewodu natężenie jest takie samo, a gęstość prądu i prędkość dryfu są większe.

## Doświadczenie / symulacja

**Ile ładunku ma powerbank?** Odczytaj z obudowy pojemność w mAh i napięcie ogniwa. Przelicz na kulomby, liczbę elektronów i energię w Wh oraz dżulach. Porównaj z energią do podniesienia siebie na wysokość piętra.

**Symulacja PhET:** *Zestaw do budowy obwodów DC* (*Circuit Construction Kit: DC*) — w widoku elektronów widać ich ruch w przewodach, w żarówce i w baterii ([phet.colorado.edu/pl](https://phet.colorado.edu/pl/)).

**Python:** prędkość dryfu w przewodach o różnych przekrojach i model Drudego.

```python
import numpy as np

e, me = 1.602e-19, 9.109e-31
n_cu, rho_cu = 8.49e28, 1.68e-8
for A_mm2, I in [(0.5, 1), (1.5, 10), (2.5, 16), (50, 200)]:
    vd = I/(n_cu*e*A_mm2*1e-6)
    print(f"przekrój {A_mm2:5.1f} mm², I = {I:4d} A: J = {I/A_mm2:5.1f} A/mm², v_d = {vd*1e3:.3f} mm/s")

tau = me/(n_cu*e**2*rho_cu)
print(f"czas między zderzeniami τ = {tau:.2e} s, droga swobodna (v_F = 1,57e6 m/s) = {tau*1.57e6*1e9:.0f} nm")
q = 2*0.5*(1 - np.exp(-2))
print(f"ładunek w 1 s rozładowania: {q:.3f} C")
print(f"powerbank 10 000 mAh: {10*3600:.0f} C = {10*3600/e:.2e} elektronów, przy 3,7 V {10*3.7:.0f} Wh")
```

## Zadania

### A. Poziom maturalny

1. Akumulator telefonu ma pojemność 4000 mAh. Ile to kulombów? Ile elektronów przepływa przy pełnym rozładowaniu?

<details>
<summary>Odpowiedź</summary>

$q = 4\ \mathrm A\cdot3600\ \mathrm s = 14\,400\ \mathrm C$, $N = q/e \approx 9\cdot10^{22}$.
</details>

2. Przez żarówkę płynie prąd 0,25 A. Ile ładunku przepłynie przez nią w ciągu godziny?

<details>
<summary>Odpowiedź</summary>

900 C.
</details>

3. Przewód miedziany zwęża się z przekroju 2 mm² do 1 mm². Co dzieje się z natężeniem prądu, gęstością prądu i prędkością dryfu w węższej części?

<details>
<summary>Odpowiedź</summary>

Natężenie się nie zmienia. Gęstość prądu i prędkość dryfu rosną dwukrotnie.
</details>

### B. Poziom akademicki

1. Ładunek przepływający przez przewodnik zmienia się jak $q(t) = 4t^2 - t\ (\mathrm{C})$. Oblicz natężenie prądu w chwili $t = 2\ \mathrm s$.

<details>
<summary>Odpowiedź</summary>

$I = dq/dt = 8t - 1 = 15\ \mathrm A$.
</details>

2. Gęstość prądu w przewodzie o promieniu $R$ rośnie od osi: $J(r) = J_0r/R$. Oblicz całkowite natężenie prądu.

<details>
<summary>Odpowiedź</summary>

$I = \displaystyle\int_0^RJ_0\frac rR2\pi r\,dr = \frac23\pi R^2J_0$.
</details>

3. Aluminium ma 3 elektrony swobodne na atom, gęstość $2700\ \mathrm{kg/m^3}$, masę molową 27 g/mol i opór właściwy $2{,}65\cdot10^{-8}\ \Omega\cdot\mathrm m$. Oblicz $n$ i czas $\tau$ z modelu Drudego.

<details>
<summary>Odpowiedź</summary>

$n = 3\cdot\dfrac{2700}{0{,}027}\cdot6{,}02\cdot10^{23} \approx 1{,}8\cdot10^{29}\ \mathrm{m^{-3}}$, $\tau = m/(ne^2\rho) \approx 7\cdot10^{-15}\ \mathrm s$.
</details>

## Źródła

- OpenStax, *Fizyka dla szkół wyższych*, t. 2, rozdz. 9 — §9.1 (prąd elektryczny) i §9.2 (model przewodnictwa w metalach).
- Halliday, Resnick, Walker, *Podstawy fizyki* — wyd. 2015: t. 3, §26.1–26.2; wyd. 1: t. 3, §27.1–27.3.
- Symulacja PhET *Zestaw do budowy obwodów DC*.
