# 03.05 — Opór ośrodka i prędkość graniczna — równanie ruchu

> **Moduł:** [03 — Dynamika punktu materialnego](README.md) · **Poziom:** 🔵 studia · **Status:** ✅ pełny
>
> **Czytaj:**
>
> - OpenStax, *Fizyka dla szkół wyższych*, t. 1, rozdz. 6: [§6.4](https://openstax.org/books/fizyka-dla-szk%C3%B3%C5%82-wy%C5%BCszych-tom-1/pages/6-4-sila-oporu-i-predkosc-graniczna) · [wstęp do rozdziału](https://openstax.org/books/fizyka-dla-szk%C3%B3%C5%82-wy%C5%BCszych-tom-1/pages/6-wstep)
> - Halliday, Resnick, Walker, *Podstawy fizyki*, wyd. 2015, t. 1: §6.2 (s. 164)
> - Halliday, Resnick, Walker, *Podstawy fizyki*, wyd. 1 (2003), t. 1: [§6.3, s. 124](https://home.agh.edu.pl/~czapli/Resnick_1.pdf#page=136) — PDF z serwera AGH

← [Dynamika ruchu po okręgu](04-dynamika-ruchu-po-okregu.md) · [spis modułu](README.md) · [Układy nieinercjalne i siły bezwładności](06-uklady-nieinercjalne.md) →

## Po co to jest

Opór powietrza i wody decyduje o zużyciu paliwa przez samochód, o prędkości spadochroniarza, o tym, jak szybko opadają kropelki mgły i ziarenka pyłu. Na maturze zwykle się go pomija; na studiach jest pierwszym przykładem siły zależnej od prędkości i pierwszym równaniem ruchu, które trzeba rozwiązać jako równanie różniczkowe. Ten sam model (opór liniowy) opisuje tłumienie drgań (09.04) i obwody RC (13.06).

## Teoria w pigułce

**Dwa reżimy oporu.**

- **Opór liniowy** — dla małych, powolnych ciał w lepkim ośrodku (kropelki mgły, pyłki, kulka w oleju). Dla kuli o promieniu $r$ obowiązuje **prawo Stokesa**:
  $$F = 6\pi\eta rv,$$
  gdzie $\eta$ to lepkość ośrodka (dla powietrza ok. $1{,}8\cdot10^{-5}\ \mathrm{Pa\cdot s}$, dla wody ok. $10^{-3}\ \mathrm{Pa\cdot s}$).
- **Opór kwadratowy** — dla większych i szybszych ciał (piłka, samochód, człowiek):
  $$F = \tfrac12C\rho Av^2,$$
  gdzie $\rho$ — gęstość ośrodka, $A$ — pole przekroju poprzecznego, $C$ — bezwymiarowy współczynnik oporu zależny od kształtu (kula ok. 0,5; samochód 0,25–0,35; człowiek w pozycji płaskiej ok. 1).

Który reżim obowiązuje, mówi **liczba Reynoldsa** $\mathrm{Re} = \rho vd/\eta$: dla $\mathrm{Re} \lesssim 1$ opór jest liniowy, dla $\mathrm{Re} \gtrsim 10^3$ — kwadratowy.

**Prędkość graniczna.** Spadające ciało przyspiesza, opór rośnie, aż zrówna się z ciężarem (pomniejszonym o wypór). Od tej chwili ciało spada ze stałą **prędkością graniczną**:

$$v_g = \frac{mg}{b}\ \ \text{(opór } bv\text{)}, \qquad v_g = \sqrt{\frac{2mg}{C\rho A}}\ \ \text{(opór kwadratowy)}.$$

**Równanie ruchu** (oś w dół, bez wyporu):

$$m\frac{dv}{dt} = mg - F(v).$$

Dla oporu liniowego rozwiązanie to $v = v_g(1 - e^{-t/\tau})$, $\tau = m/b$ (00.05). Dla kwadratowego: $v = v_g\tanh(gt/v_g)$.

## Wzory i założenia

| Wzór | Znaczenie | Kiedy obowiązuje |
|---|---|---|
| $F = 6\pi\eta rv$ | prawo Stokesa | kula, $\mathrm{Re} \lesssim 1$ |
| $F = \tfrac12C\rho Av^2$ | opór kwadratowy | $\mathrm{Re} \gtrsim 10^3$ |
| $v_g = \dfrac{2r^2(\rho_k - \rho_c)g}{9\eta}$ | prędkość graniczna kulki w cieczy | Stokes + wypór |
| $v_g = \sqrt{2mg/(C\rho A)}$ | prędkość graniczna, opór kwadratowy | bez wyporu (powietrze) |
| $v = v_g(1 - e^{-t/\tau})$, $\tau = m/b$ | rozpędzanie z oporem liniowym | start z $v = 0$ |
| $v = v_g\tanh(gt/v_g)$ | rozpędzanie z oporem kwadratowym | start z $v = 0$ |

## Przykład rozwiązany

### Wersja z rachunkiem różniczkowym i całkowym

**Zadanie 1 — spadochroniarz.** Skoczek o masie 80 kg spada w pozycji płaskiej: $C = 1{,}0$, $A = 0{,}7\ \mathrm{m^2}$, $\rho = 1{,}2\ \mathrm{kg/m^3}$. Oblicz prędkość graniczną i czas, po którym osiągnie 90% tej prędkości.

$$v_g = \sqrt{\frac{2\cdot80\cdot9{,}81}{1{,}0\cdot1{,}2\cdot0{,}7}} \approx 43\ \mathrm{m/s} \approx 156\ \mathrm{km/h}.$$

Równanie ruchu $\dot{v} = g\left(1 - v^2/v_g^2\right)$ rozwiązujemy przez rozdzielenie zmiennych:

$$\int_0^v\frac{dv'}{1 - v'^2/v_g^2} = gt \Rightarrow v_g\operatorname{artgh}\frac{v}{v_g} = gt \Rightarrow v = v_g\tanh\frac{gt}{v_g}.$$

90% prędkości granicznej: $t = \dfrac{v_g}{g}\operatorname{artgh}0{,}9 \approx \dfrac{43{,}2}{9{,}81}\cdot1{,}47 \approx 6{,}5\ \mathrm{s}$.

**Zadanie 2 — kulka w glicerynie.** Stalowa kulka ($r = 1\ \mathrm{mm}$, $\rho_k = 7800\ \mathrm{kg/m^3}$) opada w glicerynie ($\rho_c = 1260\ \mathrm{kg/m^3}$, $\eta = 1{,}41\ \mathrm{Pa\cdot s}$). Oblicz prędkość graniczną i sprawdź, czy prawo Stokesa obowiązuje.

Ciężar minus wypór równoważy opór: $\tfrac43\pi r^3(\rho_k - \rho_c)g = 6\pi\eta rv_g$, więc

$$v_g = \frac{2r^2(\rho_k - \rho_c)g}{9\eta} \approx 1{,}0\ \mathrm{cm/s}.$$

$\mathrm{Re} = \rho_cv_g\cdot2r/\eta \approx 0{,}02 \ll 1$ — prawo Stokesa obowiązuje. Ten układ (wiskozymetr Stokesa) służy do pomiaru lepkości.

## Typowe pułapki

- **Opór liniowy dla samochodu albo kwadratowy dla kropli mgły.** Sprawdź liczbę Reynoldsa.
- **Masa nie ma znaczenia.** W ośrodku z oporem cięższe ciało o tym samym kształcie spada szybciej: $v_g \propto \sqrt{m}$ (opór kwadratowy).
- **Pominięty wypór w cieczy.** W powietrzu zwykle pomijalny, w cieczy — nie.
- **Prędkość graniczna osiągana „po chwili”.** Formalnie dopiero dla $t \to \infty$; w praktyce po kilku stałych czasowych.
- **Wzory rzutu ukośnego z oporem.** Opór psuje niezależność ruchów w poziomie i pionie — trzeba liczyć numerycznie.

## Doświadczenie / symulacja

**Wiskozymetr kuchenny.** Wrzucaj stalowe kulki z łożyska (lub ołowiane śruciny) do wysokiego słoika z olejem roślinnym albo miodem. Zmierz czas przejścia między dwiema kreskami na słoiku (najlepiej nagranie wideo). Z prędkości granicznej i wzoru Stokesa wyznacz lepkość cieczy i sprawdź liczbę Reynoldsa.

**Python:** spadek skoczka — rozwiązanie numeryczne, porównanie z $\tanh$ i ze spadkiem w próżni.

```python
import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp

m, g, C, rho, A = 80.0, 9.81, 1.0, 1.2, 0.7
k = 0.5 * C * rho * A
vg = np.sqrt(m * g / k)

sol = solve_ivp(lambda t, s: [s[1], g - k*s[1]**2/m], (0, 20), [0, 0], dense_output=True, rtol=1e-9)
t = np.linspace(0, 20, 400)
x, v = sol.sol(t)
print(f"v_g = {vg:.1f} m/s; 90% po {vg/g*np.arctanh(0.9):.2f} s")
print(f"droga po 20 s: {x[-1]:.0f} m (w próżni byłoby {0.5*g*20**2:.0f} m)")

plt.plot(t, v, label="numerycznie")
plt.plot(t, vg*np.tanh(g*t/vg), "--", label="v_g·tanh(gt/v_g)")
plt.plot(t, g*t, ":", label="bez oporu")
plt.ylim(0, 60); plt.xlabel("t [s]"); plt.ylabel("v [m/s]"); plt.grid(True); plt.legend(); plt.show()
```

## Zadania

### A. Poziom maturalny _(opcjonalnie — rozgrzewka)_

1. Z jaką prędkością kropla deszczu uderzyłaby w ziemię, spadając z wysokości 1 km bez oporu powietrza? Rzeczywista prędkość dużych kropel to ok. 9 m/s. Co z tego wynika?

<details>
<summary>Odpowiedź</summary>

$\sqrt{2gh} \approx 140\ \mathrm{m/s}$. Opór powietrza ogranicza prędkość ok. 15-krotnie — inaczej deszcz byłby niebezpieczny.
</details>

2. Dwie piłki o tej samej średnicy, jedna dwa razy cięższa, spadają z dużej wysokości. Ile razy większą prędkość graniczną ma cięższa (opór kwadratowy)?

<details>
<summary>Odpowiedź</summary>

$\sqrt2 \approx 1{,}41$ razy.
</details>

### B. Poziom akademicki

1. Dla oporu liniowego $v = v_g(1 - e^{-t/\tau})$. Wyznacz drogę $x(t)$ i pokaż, że dla dużych $t$ ciało „traci” względem ruchu z prędkością graniczną odcinek $v_g\tau$.

<details>
<summary>Odpowiedź</summary>

$x = v_gt - v_g\tau(1 - e^{-t/\tau}) \to v_gt - v_g\tau$.
</details>

2. Sprawdź przez podstawienie, że $v = v_g\tanh(gt/v_g)$ spełnia równanie $\dot{v} = g(1 - v^2/v_g^2)$. (Wskazówka: $(\tanh u)' = 1 - \tanh^2u$.)

<details>
<summary>Odpowiedź</summary>

$\dot{v} = v_g\cdot\dfrac{g}{v_g}(1 - \tanh^2) = g(1 - v^2/v_g^2)$.
</details>

3. Kulka stalowa o promieniu 1 mm opada w cieczy ($\rho_c = 1260\ \mathrm{kg/m^3}$) z prędkością graniczną 1,0 cm/s. Oblicz lepkość cieczy.

<details>
<summary>Odpowiedź</summary>

$\eta = \dfrac{2r^2(\rho_k - \rho_c)g}{9v_g} \approx 1{,}43\ \mathrm{Pa\cdot s}$ (gliceryna).
</details>

4. Jaką drogę przebędzie skoczek z przykładu, zanim osiągnie 95% prędkości granicznej? (Wskazówka: $v\dfrac{dv}{dx} = g(1 - v^2/v_g^2)$.)

<details>
<summary>Odpowiedź</summary>

$x = \dfrac{v_g^2}{2g}\ln\dfrac{1}{1 - (v/v_g)^2}$; dla $0{,}95$: $\approx 222\ \mathrm{m}$.
</details>

5. Piłkę wyrzucono pionowo w górę w powietrzu z oporem. Czy wznosi się dłużej, czy krócej niż opada? Uzasadnij bez rachunków.

<details>
<summary>Odpowiedź</summary>

Krócej. W drodze w górę opór i ciężar działają w tę samą stronę (większe opóźnienie), w drodze w dół — przeciwnie (mniejsze przyspieszenie); na tej samej wysokości piłka w dół porusza się wolniej niż w górę.
</details>

### C. Zadania z arkuszy maturalnych CKE

Zadania z egzaminów maturalnych (poziom rozszerzony, formuła 2023), w których ten temat jest potrzebny. Rozwiąż je samodzielnie, a potem porównaj z zasadami oceniania. Pełne zestawienie: [matura/README.md](../../matura/README.md).

- Maj 2024, zad. 1.1 — zmiana przyspieszenia spadającej kropli (siła wypadkowa) ([arkusz](https://cke.gov.pl/images/_EGZAMIN_MATURALNY_OD_2023/Arkusze_egzaminacyjne/2024/Fizyka/MFAP-R0-100-A-2405-arkusz.pdf), [zasady oceniania](https://cke.gov.pl/egzamin-maturalny/egzamin-maturalny-w-formule-2023/arkusze/2024-2/))
- Maj 2024, zad. 1.2 — siły oporu i ciężkości działające na kroplę w dwóch chwilach ([arkusz](https://cke.gov.pl/images/_EGZAMIN_MATURALNY_OD_2023/Arkusze_egzaminacyjne/2024/Fizyka/MFAP-R0-100-A-2405-arkusz.pdf), [zasady oceniania](https://cke.gov.pl/egzamin-maturalny/egzamin-maturalny-w-formule-2023/arkusze/2024-2/))
- Maj 2024, zad. 1.3 — wzór na prędkość graniczną kropli ([arkusz](https://cke.gov.pl/images/_EGZAMIN_MATURALNY_OD_2023/Arkusze_egzaminacyjne/2024/Fizyka/MFAP-R0-100-A-2405-arkusz.pdf), [zasady oceniania](https://cke.gov.pl/egzamin-maturalny/egzamin-maturalny-w-formule-2023/arkusze/2024-2/))

## Źródła

- OpenStax, *Fizyka dla szkół wyższych*, t. 1, rozdz. 6 — §6.4: siła oporu i prędkość graniczna, prawo Stokesa.
- Halliday, Resnick, Walker, *Podstawy fizyki* — wyd. 2015: t. 1, §6.2; wyd. 1: t. 1, §6.3.
