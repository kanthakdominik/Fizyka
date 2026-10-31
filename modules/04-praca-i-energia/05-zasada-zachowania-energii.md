# 04.05 — Zasada zachowania energii mechanicznej i całkowitej

> **Moduł:** [04 — Praca, energia i moc](README.md) · **Poziom:** 🟢 matura R · **Status:** ✅ pełny
>
> **Czytaj:**
>
> - OpenStax, *Fizyka dla szkół wyższych*, t. 1, rozdz. 8: [§8.3](https://openstax.org/books/fizyka-dla-szk%C3%B3%C5%82-wy%C5%BCszych-tom-1/pages/8-3-zasada-zachowania-energii) · [wstęp do rozdziału](https://openstax.org/books/fizyka-dla-szk%C3%B3%C5%82-wy%C5%BCszych-tom-1/pages/8-wstep)
> - Halliday, Resnick, Walker, *Podstawy fizyki*, wyd. 2015, t. 1: §8.2 (s. 232), §8.4–8.5 (s. 241)
> - Halliday, Resnick, Walker, *Podstawy fizyki*, wyd. 1 (2003), t. 1: [§8.4, s. 176](https://home.agh.edu.pl/~czapli/Resnick_1.pdf#page=188), [§8.6–8.7, s. 183](https://home.agh.edu.pl/~czapli/Resnick_1.pdf#page=195) — PDF z serwera AGH

← [Siły zachowawcze i energia potencjalna](04-energia-potencjalna.md) · [spis modułu](README.md) · [Wykresy energii potencjalnej i stabilność równowagi](06-wykresy-energii.md) →

## Po co to jest

Zasada zachowania energii to jedno z najważniejszych praw fizyki: energia nie powstaje z niczego i nie znika, tylko zmienia formę. W mechanice daje najszybszą drogę do prędkości w zadaniach z rollercoasterem, wahadłem, sprężyną i skokiem na bungee — bez liczenia sił i czasu. W dalszych modułach zasada przybiera postać I zasady termodynamiki (11), bilansu energii w obwodach (13) i równania $E = mc^2$ (19).

## Teoria w pigułce

**Energia mechaniczna** to suma energii kinetycznej i potencjalnej: $E = E_k + U$.

**Zasada zachowania energii mechanicznej.** Jeśli pracę wykonują tylko siły zachowawcze (ciężar, sprężystość), energia mechaniczna jest stała:

$$E_{k1} + U_1 = E_{k2} + U_2.$$

Siły, które nie wykonują pracy (nacisk podłoża prostopadły do ruchu, naciąg nici wahadła), nie przeszkadzają.

**Z siłami niezachowawczymi** (tarcie, opór) energia mechaniczna się zmienia o pracę tych sił:

$$E_2 - E_1 = W_{\text{niezach}}.$$

Tarcie daje $W < 0$ — energia mechaniczna zamienia się w energię wewnętrzną (ciepło) ciał i otoczenia. **Całkowita** energia (mechaniczna + wewnętrzna + inne formy) jest zachowana zawsze.

**Jak rozwiązywać.**
1. Wybierz dwa stany (początkowy i końcowy) i poziom zerowy energii potencjalnej.
2. Wypisz wszystkie formy energii w obu stanach.
3. Sprawdź, czy działają siły niezachowawcze; jeśli tak — dopisz ich pracę.
4. Rozwiąż równanie bilansu.

**Kiedy nie wystarcza.** Zasada zachowania energii nie mówi nic o czasie ani o kierunku ruchu. Jeśli pytanie dotyczy sił (np. naciągu w pętli), trzeba ją połączyć z II zasadą dynamiki (03.04).

## Wzory i założenia

| Wzór | Znaczenie | Kiedy obowiązuje |
|---|---|---|
| $\tfrac12mv_1^2 + U_1 = \tfrac12mv_2^2 + U_2$ | zachowanie energii mechanicznej | tylko siły zachowawcze wykonują pracę |
| $\Delta E_{\text{mech}} = W_{\text{niezach}}$ | bilans z tarciem | ogólnie |
| $v = \sqrt{2g\Delta h}$ | prędkość po obniżeniu o $\Delta h$ | start z $v = 0$, bez tarcia; niezależnie od kształtu toru |
| $v_{\text{dół}} = \sqrt{2gL(1 - \cos\theta_0)}$ | wahadło | wychylenie $\theta_0$, puszczone bez prędkości |
| $h_{\min} = \tfrac52R$ | najmniejsza wysokość startu do pętli | bez tarcia, ciało ślizga się (nie toczy) |

## Przykład rozwiązany

**Zadanie 1.** Wagonik kolejki górskiej startuje z zerową prędkością ze szczytu na wysokości 30 m. Jaką ma prędkość na dole toru i na wzniesieniu o wysokości 12 m? (Pomijamy tarcie.)

Poziom zerowy: dół toru. $mgh_1 = \tfrac12mv^2 + mgh_2$:
- na dole: $v = \sqrt{2\cdot9{,}81\cdot30} \approx 24{,}3\ \mathrm{m/s}$,
- na 12 m: $v = \sqrt{2\cdot9{,}81\cdot18} \approx 18{,}8\ \mathrm{m/s}$.

Masa się skraca, a kształt toru między punktami nie ma znaczenia.

**Zadanie 2.** Sanki o masie 20 kg zjeżdżają z górki o wysokości 10 m i na dole mają prędkość 12 m/s. Ile energii zamieniło się w ciepło?

$E_1 = mgh = 1962\ \mathrm{J}$, $E_2 = \tfrac12mv^2 = 1440\ \mathrm{J}$. Tarcie i opór powietrza zamieniły w ciepło $522\ \mathrm{J}$ (ok. 27% energii).

## Typowe pułapki

- **Zachowanie energii mechanicznej przy tarciu.** Nie obowiązuje; trzeba dopisać pracę tarcia.
- **Pomijanie energii sprężystości.** W zadaniach ze sprężyną energia jest w trzech formach: kinetycznej, grawitacyjnej i sprężystości.
- **Różne poziomy zerowe w jednym równaniu.** Wybierz jeden poziom dla obu stanów.
- **Energia „zużyta”.** Energia nie znika — zamienia się w ciepło, dźwięk, odkształcenie.
- **Pętla: $h = 2R$ wystarcza.** Na szczycie pętli ciało musi mieć prędkość co najmniej $\sqrt{gR}$, więc trzeba startować z $2{,}5R$.

## Doświadczenie / symulacja

**Symulacja PhET:** *Energia na rampie dla deskorolkarza* — narysuj własny tor, włącz wykresy energii i tarcie. Sprawdź, że bez tarcia deskorolkarz wraca na tę samą wysokość, a z tarciem — coraz niżej.

**Wahadło i telefon.** Zawieś telefon na sznurku (ok. 1 m) i odchyl o znany kąt. phyphox (*Pendulum* lub żyroskop) pokaże prędkość kątową w najniższym punkcie, a z niej $v = \omega L$. Porównaj z $\sqrt{2gL(1 - \cos\theta_0)}$.

**Python:** skok na bungee — energia kinetyczna, grawitacyjna i sprężystości liny w trakcie skoku.

```python
import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp

m, g, L0, k = 70.0, 9.81, 20.0, 200.0         # masa, długość liny, sztywność liny

def rhs(t, s):                                 # y — odległość w dół od mostu
    y, v = s
    F_lina = -k*(y - L0) if y > L0 else 0.0
    return [v, g + F_lina/m]

sol = solve_ivp(rhs, (0, 6), [0, 0], max_step=0.005)
y, v = sol.y
Ek = 0.5*m*v**2
Ug = -m*g*y                                     # poziom zerowy na moście
Us = np.where(y > L0, 0.5*k*(y - L0)**2, 0.0)
print(f"największe opadnięcie: {y.max():.2f} m; zmiana energii całkowitej: {np.ptp(Ek + Ug + Us):.2e} J")

plt.plot(sol.t, Ek, label="kinetyczna"); plt.plot(sol.t, Ug, label="grawitacyjna")
plt.plot(sol.t, Us, label="sprężystości"); plt.plot(sol.t, Ek + Ug + Us, "k--", label="suma")
plt.xlabel("t [s]"); plt.ylabel("E [J]"); plt.grid(True); plt.legend(); plt.show()
```

## Zadania

### A. Poziom maturalny

1. Piłka spada swobodnie z wysokości 5 m. Z jaką prędkością uderza w ziemię?

<details>
<summary>Odpowiedź</summary>

$v = \sqrt{2gh} \approx 9{,}9\ \mathrm{m/s}$.
</details>

2. Pistolet sprężynowy ma sprężynę o współczynniku $800\ \mathrm{N/m}$ ściśniętą o 5 cm. Z jaką prędkością wylatuje kulka o masie 20 g i na jaką wysokość się wzniesie przy strzale pionowym?

<details>
<summary>Odpowiedź</summary>

$v = \sqrt{k/m}\,x = 10\ \mathrm{m/s}$; $h = v^2/(2g) \approx 5{,}1\ \mathrm{m}$.
</details>

3. Narciarz o masie 60 kg zjeżdża ze stoku o różnicy wysokości 50 m i na dole ma prędkość 25 m/s. Ile energii zamieniło się w ciepło?

<details>
<summary>Odpowiedź</summary>

$29\,430 - 18\,750 = 10\,680\ \mathrm{J} \approx 10{,}7\ \mathrm{kJ}$.
</details>

4. Wahadło o długości 1 m odchylono o $60^\circ$ i puszczono. Z jaką prędkością przechodzi przez najniższy punkt?

<details>
<summary>Odpowiedź</summary>

$v = \sqrt{2gL(1 - \cos60^\circ)} = \sqrt{gL} \approx 3{,}1\ \mathrm{m/s}$.
</details>

5. Z jakiej najmniejszej wysokości musi zjechać (bez tarcia) wagonik, żeby pokonać pętlę o promieniu $R$?

<details>
<summary>Odpowiedź</summary>

Na szczycie $v^2 \ge gR$: $mgh = mg\cdot2R + \tfrac12mgR \Rightarrow h = 2{,}5R$.
</details>

### B. Poziom akademicki _(opcjonalnie — rozszerzenie z rachunkiem)_

1. Skoczek o masie 70 kg skacze z mostu na linie bungee o długości 20 m i sztywności $200\ \mathrm{N/m}$. Jak nisko spadnie?

<details>
<summary>Odpowiedź</summary>

$mg(L_0 + x) = \tfrac12kx^2 \Rightarrow x \approx 15{,}6\ \mathrm{m}$; łącznie ok. $35{,}6\ \mathrm{m}$ poniżej mostu.
</details>

2. Wyprowadź prędkość ucieczki z powierzchni Ziemi z zasady zachowania energii z $U = -GMm/r$ i oblicz ją ($GM_Z = 3{,}99\cdot10^{14}\ \mathrm{m^3/s^2}$, $R = 6{,}37\cdot10^6\ \mathrm{m}$).

<details>
<summary>Odpowiedź</summary>

$\tfrac12mv^2 - \dfrac{GMm}{R} = 0 \Rightarrow v = \sqrt{2GM/R} \approx 11{,}2\ \mathrm{km/s}$.
</details>

3. Klocek o masie 1 kg uderza z prędkością 3 m/s w sprężynę ($k = 100\ \mathrm{N/m}$) leżącą na poziomym stole; $\mu_k = 0{,}2$. O ile ściśnie sprężynę?

<details>
<summary>Odpowiedź</summary>

$\tfrac12mv^2 = \tfrac12kx^2 + \mu mgx \Rightarrow 50x^2 + 1{,}962x - 4{,}5 = 0$, $x \approx 0{,}281\ \mathrm{m}$.
</details>

4. Wykaż na podstawie II zasady dynamiki, że dla ruchu w 1D w polu siły zachowawczej $\dfrac{d}{dt}\left(\tfrac12mv^2 + U(x)\right) = 0$.

<details>
<summary>Odpowiedź</summary>

$\dfrac{d}{dt}\left(\tfrac12mv^2\right) + \dfrac{dU}{dx}\dfrac{dx}{dt} = mva - Fv = v(ma - F) = 0$.
</details>

### C. Zadania z arkuszy maturalnych CKE

Zadania z egzaminów maturalnych (poziom rozszerzony, formuła 2023), w których ten temat jest potrzebny. Rozwiąż je samodzielnie, a potem porównaj z zasadami oceniania. Pełne zestawienie: [matura/README.md](../../matura/README.md).

- Maj 2026, zad. 2.3 — stosunek największej i najmniejszej siły naciągu nici (temat pomocniczy) ([arkusz](https://oke.wroc.pl/egzamin-maturalny/egzamin-maturalny-2026-arkusze/), [zasady oceniania](https://cke.gov.pl/egzamin-maturalny/egzamin-maturalny-w-formule-2023/arkusze/))

## Źródła

- OpenStax, *Fizyka dla szkół wyższych*, t. 1, rozdz. 8 — §8.3: zasada zachowania energii, z wieloma przykładami.
- Halliday, Resnick, Walker, *Podstawy fizyki* — wyd. 2015: t. 1, §8.2 i §8.4–8.5; wyd. 1: t. 1, §8.4 i §8.6–8.7.
- Symulacja PhET *Energia na rampie dla deskorolkarza*.
