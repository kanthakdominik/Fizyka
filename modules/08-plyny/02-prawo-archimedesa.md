# 08.02 — Prawo Archimedesa i pływanie ciał

> **Moduł:** [08 — Mechanika płynów](README.md) · **Poziom:** 🟢 matura R · **Status:** ✅ pełny
>
> **Czytaj:**
>
> - OpenStax, *Fizyka dla szkół wyższych*, t. 1, rozdz. 14: [§14.4](https://openstax.org/books/fizyka-dla-szk%C3%B3%C5%82-wy%C5%BCszych-tom-1/pages/14-4-prawo-archimedesa-i-sila-wyporu) · [wstęp do rozdziału](https://openstax.org/books/fizyka-dla-szk%C3%B3%C5%82-wy%C5%BCszych-tom-1/pages/14-wstep)
> - Halliday, Resnick, Walker, *Podstawy fizyki*, wyd. 2015, t. 2: §14.5 (s. 90)
> - Halliday, Resnick, Walker, *Podstawy fizyki*, wyd. 1 (2003), t. 2: [§15.7, s. 71](https://home.agh.edu.pl/~czapli/Resnick_2.pdf#page=87) — PDF z serwera AGH

← [Ciśnienie, prawo Pascala, ciśnienie hydrostatyczne](01-cisnienie-i-prawo-pascala.md) · [spis modułu](README.md) · [Równanie ciągłości i równanie Bernoulliego](03-rownanie-bernoulliego.md) →

## Po co to jest

Prawo Archimedesa wyjaśnia, dlaczego stalowy statek pływa, a stalowa kulka tonie, jak działa balon i łódź podwodna, dlaczego góra lodowa wystaje z wody tylko w 10% i jak zbadać, czy korona jest ze szczerego złota. To jeden z najczęstszych tematów zadań maturalnych z hydrostatyki.

## Teoria w pigułce

**Siła wyporu.** Na ciało zanurzone w płynie działa pionowo w górę siła równa ciężarowi wypartego płynu:

$$F_w = \rho_pgV_{\text{zan}},$$

gdzie $\rho_p$ — gęstość **płynu**, $V_{\text{zan}}$ — objętość zanurzonej części ciała.

**Skąd się bierze.** Ciśnienie hydrostatyczne rośnie z głębokością, więc na dolną powierzchnię ciała działa większa siła parcia niż na górną. Wypadkowa sił parcia to siła wyporu. Nie zależy od materiału ciała — tylko od objętości i gęstości płynu.

**Pływanie, zawieszenie, tonięcie** (ciało całkowicie zanurzone, o średniej gęstości $\rho_c$):
- $\rho_c < \rho_p$ — wypływa i pływa częściowo zanurzone,
- $\rho_c = \rho_p$ — pozostaje zawieszone (ryba, łódź podwodna),
- $\rho_c > \rho_p$ — tonie.

**Ciało pływające.** Wypór równoważy ciężar, więc zanurzona część objętości to

$$\frac{V_{\text{zan}}}{V} = \frac{\rho_c}{\rho_p}.$$

Statek ze stali pływa, bo jego **średnia** gęstość (stal + powietrze wewnątrz) jest mniejsza od gęstości wody.

**Ciężar pozorny** ciała zanurzonego: $Q' = mg - F_w$. Z różnicy ciężaru w powietrzu i w wodzie można wyznaczyć objętość, a więc i gęstość ciała — tak (według legendy) Archimedes zbadał koronę króla Hierona.

**Wypór w powietrzu.** Działa także w gazach; na nim latają balony i sterowce. Dokładne ważenie wymaga poprawki na wypór powietrza.

## Wzory i założenia

| Wzór | Znaczenie | Kiedy obowiązuje |
|---|---|---|
| $F_w = \rho_pgV_{\text{zan}}$ | siła wyporu | płyn w spoczynku, $g$ stałe |
| $V_{\text{zan}}/V = \rho_c/\rho_p$ | część zanurzona | ciało pływające |
| $Q' = (\rho_c - \rho_p)gV$ | ciężar pozorny | ciało całkowicie zanurzone |
| $\rho_c = \rho_p\dfrac{Q}{Q - Q'}$ | gęstość z ważenia w powietrzu i cieczy | $Q$ — ciężar w powietrzu, $Q'$ — w cieczy |
| $F_{\text{nośna}} = (\rho_{\text{pow}} - \rho_{\text{gazu}})gV$ | siła nośna balonu | bez masy powłoki |

## Przykład rozwiązany

**Zadanie 1 — góra lodowa.** Jaka część góry lodowej jest pod wodą? (Lód $917\ \mathrm{kg/m^3}$, woda morska $1025\ \mathrm{kg/m^3}$.)

$V_{\text{zan}}/V = 917/1025 \approx 0{,}89$ — nad wodą wystaje tylko ok. 11%.

**Zadanie 2 — korona.** Korona waży w powietrzu 9,81 N, a zanurzona w wodzie — 9,25 N. Czy jest ze szczerego złota ($\rho = 19\,300\ \mathrm{kg/m^3}$)?

Wypór: $F_w = 0{,}56\ \mathrm{N} = 1000\cdot9{,}81\cdot V \Rightarrow V \approx 5{,}71\cdot10^{-5}\ \mathrm{m^3}$. Masa 1 kg, więc $\rho = 1/V \approx 17\,500\ \mathrm{kg/m^3}$ — mniej niż złoto. Korona zawiera domieszkę lżejszego metalu (np. srebra).

### Wersja z rachunkiem różniczkowym i całkowym

**Zadanie — kołyszący się klocek.** Prostopadłościenny klocek o polu podstawy $S$ i masie $m$ pływa w wodzie, zanurzony na głębokość $h_0$. Wciskamy go nieco głębiej i puszczamy. Wykaż, że drga harmonicznie, i oblicz okres.

W równowadze $\rho gSh_0 = mg$. Przy dodatkowym zanurzeniu $x$ wypór rośnie o $\rho gSx$, więc wypadkowa siła to $-\rho gSx$:

$$m\ddot{x} = -\rho gSx \Rightarrow \omega^2 = \frac{\rho gS}{m} = \frac{g}{h_0}, \qquad T = 2\pi\sqrt{\frac{h_0}{g}}.$$

Dla klocka zanurzonego na 10 cm: $T \approx 0{,}63\ \mathrm{s}$ — tak kołysze się boja. (Pomijamy masę wody poruszanej razem z klockiem i tłumienie.)

## Typowe pułapki

- **Gęstość ciała zamiast płynu we wzorze na wypór.** We wzorze jest gęstość **płynu**.
- **Wypór zależy od głębokości.** Dla całkowicie zanurzonego ciała w cieczy nieściśliwej — nie.
- **Wypór zależy od masy ciała.** Zależy od objętości zanurzonej części; ciężkie i lekkie ciało o tej samej objętości mają ten sam wypór.
- **Cała objętość zamiast zanurzonej.** Dla ciała pływającego liczy się tylko część pod powierzchnią.
- **Woda słodka a morska.** Statek wpływający z rzeki do morza wynurza się — woda morska jest gęstsza.

## Doświadczenie / symulacja

**Gęstość przedmiotu wagą kuchenną.** Postaw na wadze naczynie z wodą i wytaruj. Zanurz w wodzie przedmiot (np. pierścionek, kamień) zawieszony na nitce, tak żeby nie dotykał dna: waga pokaże masę wypartej wody, czyli objętość w cm³. Potem zważ sam przedmiot. Oblicz gęstość i porównaj z tablicami.

**Symulacja PhET:** *Siła wyporu* (*Buoyancy*, [phet.colorado.edu/pl](https://phet.colorado.edu/pl/)) — wypór dla bloków o różnej gęstości i w różnych cieczach.

**Python:** drgania pływającego klocka — rozwiązanie numeryczne z tłumieniem i porównanie okresu ze wzorem.

```python
import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp

rho, g, S, h0 = 1000.0, 9.81, 0.01, 0.10      # woda, pole podstawy 10×10 cm, zanurzenie 10 cm
m = rho*S*h0                                   # z warunku równowagi
b = 0.3                                        # tłumienie (umowne)

sol = solve_ivp(lambda t, s: [s[1], (-rho*g*S*s[0] - b*s[1])/m], (0, 5), [0.02, 0], max_step=0.005)
t, x = sol.t, sol.y[0]
peaks = t[1:-1][(x[1:-1] > x[:-2]) & (x[1:-1] > x[2:])]
print(f"okres z symulacji = {np.diff(peaks).mean():.3f} s, wzór 2π√(h0/g) = {2*np.pi*np.sqrt(h0/g):.3f} s")
plt.plot(t, x*100); plt.xlabel("t [s]"); plt.ylabel("wychylenie [cm]"); plt.grid(True); plt.show()
```

## Zadania

### A. Poziom maturalny

1. Balon wypełniony helem ma objętość $1\ \mathrm{m^3}$. Jaką masę może unieść (razem z powłoką)? ($\rho_{\text{pow}} = 1{,}2\ \mathrm{kg/m^3}$, $\rho_{\text{He}} = 0{,}18\ \mathrm{kg/m^3}$.)

<details>
<summary>Odpowiedź</summary>

$(1{,}2 - 0{,}18)\cdot1 = 1{,}02\ \mathrm{kg}$ (siła nośna ok. 10 N).
</details>

2. Drewniany klocek o gęstości $600\ \mathrm{kg/m^3}$ pływa w wodzie. Jaka część jego objętości jest zanurzona? A w oleju o gęstości $900\ \mathrm{kg/m^3}$?

<details>
<summary>Odpowiedź</summary>

60%; ok. 67%.
</details>

3. Kamień waży w powietrzu 30 N, a w wodzie 20 N. Oblicz jego objętość i gęstość.

<details>
<summary>Odpowiedź</summary>

$V = 10/(1000\cdot9{,}81) \approx 1{,}02\cdot10^{-3}\ \mathrm{m^3}$; $\rho = 3000\ \mathrm{kg/m^3}$.
</details>

4. Statek wpływa z rzeki do morza. Zanurza się głębiej czy wynurza? Dlaczego?

<details>
<summary>Odpowiedź</summary>

Wynurza się — woda morska jest gęstsza, więc ta sama siła wyporu wymaga mniejszej objętości zanurzonej.
</details>

5. Kostka lodu pływa w szklance wody. Czy po stopieniu poziom wody się podniesie?

<details>
<summary>Odpowiedź</summary>

Nie — lód wypiera tyle wody, ile sam waży, a po stopieniu zajmuje dokładnie tę objętość.
</details>

### B. Poziom akademicki _(opcjonalnie — rozszerzenie z rachunkiem)_

1. Balon na ogrzane powietrze ma objętość $2500\ \mathrm{m^3}$. Powietrze w środku ma $100\ ^\circ\mathrm{C}$, na zewnątrz $20\ ^\circ\mathrm{C}$ ($\rho = 1{,}2\ \mathrm{kg/m^3}$). Jaką masę (kosz, powłoka, ludzie) może unieść?

<details>
<summary>Odpowiedź</summary>

$\rho_{\text{wewn}} = 1{,}2\cdot293/373 \approx 0{,}94\ \mathrm{kg/m^3}$ (gaz doskonały, to samo ciśnienie); udźwig $(1{,}2 - 0{,}94)\cdot2500 \approx 640\ \mathrm{kg}$.
</details>

2. Wyprowadź prawo Archimedesa dla prostopadłościanu o wysokości $h$ i polu podstawy $S$, całkując siły parcia na jego ścianki.

<details>
<summary>Odpowiedź</summary>

Siły na ścianki boczne się znoszą. Na dolną podstawę: $(p_0 + \rho gy_d)S$ w górę, na górną: $(p_0 + \rho gy_g)S$ w dół. Wypadkowa $\rho g(y_d - y_g)S = \rho ghS = \rho gV$.
</details>

3. Areometr (pływająca rurka o przekroju $S$ i masie $m$) zanurza się w wodzie do głębokości $h_w$. Na jaką głębokość zanurzy się w cieczy o gęstości $\rho$? Jak należy rozmieścić podziałkę?

<details>
<summary>Odpowiedź</summary>

$h = h_w\rho_w/\rho$ — podziałka nieliniowa, gęstsza dla większych gęstości.
</details>

## Źródła

- OpenStax, *Fizyka dla szkół wyższych*, t. 1, rozdz. 14 — §14.4: prawo Archimedesa i siła wyporu.
- Halliday, Resnick, Walker, *Podstawy fizyki* — wyd. 2015: t. 2, §14.5; wyd. 1: t. 2, §15.7.
- Symulacja PhET *Siła wyporu*.
