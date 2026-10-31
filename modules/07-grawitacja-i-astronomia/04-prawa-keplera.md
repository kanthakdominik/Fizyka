# 07.04 — Prawa Keplera

> **Moduł:** [07 — Grawitacja i elementy astronomii](README.md) · **Poziom:** 🟢🔵 matura R + studia · **Status:** ✅ pełny
>
> **Czytaj:**
>
> - OpenStax, *Fizyka dla szkół wyższych*, t. 1, rozdz. 13: [§13.5](https://openstax.org/books/fizyka-dla-szk%C3%B3%C5%82-wy%C5%BCszych-tom-1/pages/13-5-prawa-keplera) · [wstęp do rozdziału](https://openstax.org/books/fizyka-dla-szk%C3%B3%C5%82-wy%C5%BCszych-tom-1/pages/13-wstep)
> - Halliday, Resnick, Walker, *Podstawy fizyki*, wyd. 2015, t. 2: §13.6 (s. 55)
> - Halliday, Resnick, Walker, *Podstawy fizyki*, wyd. 1 (2003), t. 2: [§14.7, s. 42](https://home.agh.edu.pl/~czapli/Resnick_2.pdf#page=58) — PDF z serwera AGH

← [Orbity, satelity i prędkości kosmiczne](03-orbity-i-predkosci-kosmiczne.md) · [spis modułu](README.md) · [Pole rozkładu masy i siły pływowe](05-pole-rozkladu-masy-i-plywy.md) →

## Po co to jest

Prawa Keplera to trzy reguły odczytane na początku XVII wieku z obserwacji Marsa, zanim ktokolwiek wiedział, czym jest grawitacja. Newton pokazał, że wszystkie wynikają z prawa $1/r^2$ i zasad dynamiki — to był triumf fizyki matematycznej. Dziś tymi samymi prawami wyznacza się masy planet z ruchu ich księżyców, masy gwiazd w układach podwójnych i masę czarnej dziury w centrum Galaktyki.

## Teoria w pigułce

**I prawo — elipsy.** Planety poruszają się po elipsach, a Słońce znajduje się w jednym z ognisk.

Elipsa: półoś wielka $a$, mimośród $e$ ($0 \le e < 1$; okrąg to $e = 0$). Najbliższy punkt orbity (**peryhelium**) $r_p = a(1 - e)$, najdalszy (**aphelium**) $r_a = a(1 + e)$. Orbity planet są prawie kołowe (Ziemia $e \approx 0{,}017$), komet — bardzo wydłużone.

**II prawo — pola.** Promień wodzący planety zakreśla równe pola w równych odstępach czasu. Planeta porusza się najszybciej w peryhelium, najwolniej w aphelium:

$$v_pr_p = v_ar_a.$$

To zasada zachowania momentu pędu (06.05): grawitacja jest siłą centralną i nie daje momentu względem Słońca.

**III prawo — okresy.** Kwadraty okresów obiegu są proporcjonalne do sześcianów półosi wielkich:

$$\frac{T^2}{a^3} = \frac{4\pi^2}{GM} = \text{const dla danego ciała centralnego}.$$

Dla orbity kołowej wynika wprost z 07.03. W jednostkach „lata ziemskie i jednostki astronomiczne” dla Układu Słonecznego: $T^2 = a^3$.

**Wyznaczanie mas.** Z III prawa: $M = \dfrac{4\pi^2a^3}{GT^2}$. Masę Słońca dostajemy z orbity Ziemi, masę Jowisza — z orbit jego księżyców, masę Ziemi — z orbity Księżyca. (Dokładniej, gdy masy są porównywalne, w mianowniku występuje $G(M + m)$.)

## Wzory i założenia

| Wzór | Znaczenie | Kiedy obowiązuje |
|---|---|---|
| $r_p = a(1 - e)$, $\ r_a = a(1 + e)$ | peryhelium i aphelium | orbita eliptyczna |
| $v_pr_p = v_ar_a$ | II prawo (zachowanie $L$) | siła centralna |
| $dA/dt = L/(2m) = \text{const}$ | prędkość polowa | j.w. |
| $T^2 = \dfrac{4\pi^2}{GM}a^3$ | III prawo | $m \ll M$ |
| $v^2 = GM\left(\dfrac2r - \dfrac1a\right)$ | wzór vis-viva (prędkość w dowolnym punkcie) | orbita eliptyczna |
| $E = -\dfrac{GMm}{2a}$ | energia na orbicie eliptycznej | zależy tylko od $a$ |

## Przykład rozwiązany

**Zadanie 1.** Półoś wielka orbity Marsa wynosi 1,524 j.a. Oblicz okres obiegu Marsa.

$T = a^{3/2} = 1{,}524^{1{,}5} \approx 1{,}88$ roku (w jednostkach Ziemi).

**Zadanie 2.** Księżyc Jowisza Io obiega planetę po orbicie o promieniu $4{,}217\cdot10^8\ \mathrm{m}$ w ciągu 1,769 doby. Oblicz masę Jowisza.

$M = \dfrac{4\pi^2a^3}{GT^2} = \dfrac{4\pi^2(4{,}217\cdot10^8)^3}{6{,}674\cdot10^{-11}\cdot(1{,}528\cdot10^5)^2} \approx 1{,}90\cdot10^{27}\ \mathrm{kg}$ — ok. 318 mas Ziemi.

### Wersja z rachunkiem różniczkowym i całkowym

**Zadanie — kometa Halleya.** Półoś wielka orbity wynosi 17,8 j.a., mimośród 0,967. Oblicz odległości w peryhelium i aphelium, okres obiegu i prędkość w peryhelium ($GM_\odot = 1{,}327\cdot10^{20}\ \mathrm{m^3/s^2}$, 1 j.a. $= 1{,}496\cdot10^{11}\ \mathrm{m}$).

- $r_p = 17{,}8\cdot0{,}033 \approx 0{,}59$ j.a. (bliżej Słońca niż Wenus), $r_a \approx 35{,}0$ j.a. (dalej niż Neptun).
- $T = 17{,}8^{1{,}5} \approx 75$ lat.
- Prędkość w peryhelium ze wzoru vis-viva:
  $$v_p = \sqrt{GM\left(\frac{2}{r_p} - \frac{1}{a}\right)} \approx 54{,}5\ \mathrm{km/s},$$
  a w aphelium $v_a = v_pr_p/r_a \approx 0{,}9\ \mathrm{km/s}$.

**Skąd wzór vis-viva.** Z zachowania energii i momentu pędu dla punktów $r_p$ i $r_a$ (gdzie prędkość jest prostopadła do promienia) dostajemy $E = -\dfrac{GMm}{r_p + r_a} = -\dfrac{GMm}{2a}$, a stąd $\tfrac12mv^2 - \dfrac{GMm}{r} = -\dfrac{GMm}{2a}$.

## Typowe pułapki

- **Słońce w środku elipsy.** Jest w ognisku.
- **III prawo dla różnych ciał centralnych.** Stała $T^2/a^3$ jest ta sama tylko dla ciał krążących wokół tego samego ciała.
- **Promień zamiast półosi wielkiej.** Dla orbity eliptycznej w III prawie występuje $a$, a nie chwilowa odległość.
- **Stała prędkość planety.** Planeta przyspiesza, zbliżając się do Słońca (II prawo).
- **Ziemia najbliżej Słońca latem.** Peryhelium Ziemi wypada na początku stycznia; pory roku wynikają z nachylenia osi, nie z odległości.

## Doświadczenie / symulacja

**Symulacja PhET:** *Prawa Keplera* (*Kepler's Laws*, [phet.colorado.edu/pl](https://phet.colorado.edu/pl/)) — narysuj orbitę eliptyczną, włącz pola zakreślane w równych czasach i sprawdź III prawo dla kilku orbit.

**Księżyce Jowisza przez lornetkę.** Przez lornetkę (na statywie) widać do czterech księżyców Jowisza. Notuj ich położenie przez kilka nocy (albo użyj [Stellarium](https://stellarium.org/)) i oszacuj okres i promień orbity Io lub Europy; wyznacz masę Jowisza.

**Python:** numeryczne całkowanie orbity eliptycznej — sprawdzenie II prawa (stała prędkość polowa) i III prawa.

```python
import numpy as np
from scipy.integrate import solve_ivp

GM = 4*np.pi**2                        # jednostki: j.a., lata — wtedy T² = a³

def rhs(t, s):
    x, y, vx, vy = s
    r3 = (x*x + y*y)**1.5
    return [vx, vy, -GM*x/r3, -GM*y/r3]

for a, e in [(1.0, 0.0167), (1.524, 0.093), (17.8, 0.967)]:
    rp = a*(1 - e); vp = np.sqrt(GM*(2/rp - 1/a))
    T_kepler = a**1.5
    sol = solve_ivp(rhs, (0, 1.2*T_kepler), [rp, 0, 0, vp], rtol=1e-10, atol=1e-12, dense_output=True)
    t = np.linspace(0, 1.2*T_kepler, 20000)
    x, y, vx, vy = sol.sol(t)
    areal = 0.5*(x*vy - y*vx)                 # prędkość polowa dA/dt
    crossings = t[1:][(y[:-1] < 0) & (y[1:] >= 0)]
    print(f"a = {a:5.2f} j.a.: T z symulacji = {crossings[0]:.3f} lat, T = a^1,5 = {T_kepler:.3f}, "
          f"rozrzut dA/dt = {np.ptp(areal)/areal.mean():.1e}")
```

## Zadania

### A. Poziom maturalny

1. Planeta krąży wokół Słońca z okresem 8 lat. Jaka jest półoś wielka jej orbity?

<details>
<summary>Odpowiedź</summary>

$a = 8^{2/3} = 4$ j.a.
</details>

2. Odległość Ziemi od Słońca w peryhelium wynosi 0,983 j.a., a w aphelium 1,017 j.a. Ile razy prędkość Ziemi w peryhelium jest większa niż w aphelium?

<details>
<summary>Odpowiedź</summary>

$v_p/v_a = r_a/r_p \approx 1{,}035$.
</details>

3. Oblicz masę Słońca z okresu obiegu Ziemi (1 rok) i jej odległości od Słońca ($1{,}496\cdot10^{11}\ \mathrm{m}$).

<details>
<summary>Odpowiedź</summary>

$M = 4\pi^2a^3/(GT^2) \approx 2{,}0\cdot10^{30}\ \mathrm{kg}$.
</details>

4. Wyjaśnij, dlaczego II prawo Keplera wynika z zasady zachowania momentu pędu.

<details>
<summary>Odpowiedź</summary>

Grawitacja Słońca działa wzdłuż promienia, więc nie daje momentu siły względem Słońca. Moment pędu $L = mr^2\omega$ jest stały, a prędkość polowa $\tfrac12r^2\omega = L/(2m)$ — też.
</details>

### B. Poziom akademicki

1. Oblicz prędkość komety Halleya w aphelium dwiema metodami: z II prawa Keplera i ze wzoru vis-viva.

<details>
<summary>Odpowiedź</summary>

$v_a = v_pr_p/r_a \approx 54{,}5\cdot0{,}587/35{,}0 \approx 0{,}91\ \mathrm{km/s}$; vis-viva daje ten sam wynik.
</details>

2. Wyprowadź z zachowania energii i momentu pędu, że energia całkowita na orbicie eliptycznej wynosi $-GMm/(2a)$.

<details>
<summary>Odpowiedź</summary>

$\tfrac12mv_p^2 - \tfrac{GMm}{r_p} = \tfrac12mv_a^2 - \tfrac{GMm}{r_a}$, $v_pr_p = v_ar_a$. Eliminując $v_a$: $v_p^2 = \dfrac{2GMr_a}{r_p(r_p + r_a)}$, skąd $E = -\dfrac{GMm}{r_p + r_a} = -\dfrac{GMm}{2a}$.
</details>

3. Gwiazda S2 obiega centrum Drogi Mlecznej z okresem ok. 16 lat po orbicie o półosi wielkiej ok. 1000 j.a. Oszacuj masę centralnej czarnej dziury w masach Słońca.

<details>
<summary>Odpowiedź</summary>

$M/M_\odot = a^3/T^2 = 10^9/256 \approx 4\cdot10^6$ mas Słońca.
</details>

### C. Zadania z arkuszy maturalnych CKE

Zadania z egzaminów maturalnych (poziom rozszerzony, formuła 2023), w których ten temat jest potrzebny. Rozwiąż je samodzielnie, a potem porównaj z zasadami oceniania. Pełne zestawienie: [matura/README.md](../../matura/README.md).

- Maj 2023, zad. 5.2 — stosunek prędkości w peryhelium i aphelium (II prawo Keplera) ([arkusz](https://cke.gov.pl/images/_EGZAMIN_MATURALNY_OD_2023/Arkusze_egzaminacyjne/2023/Fizyka/MFAP-R0-100-2305.pdf), [zasady oceniania](https://cke.gov.pl/images/_EGZAMIN_MATURALNY_OD_2023/Arkusze_egzaminacyjne/2023/Fizyka/MFAP-R0-100-2305-zasady.pdf))
- Maj 2023, zad. 5.3 — masa Sgr A* z III prawa Keplera ([arkusz](https://cke.gov.pl/images/_EGZAMIN_MATURALNY_OD_2023/Arkusze_egzaminacyjne/2023/Fizyka/MFAP-R0-100-2305.pdf), [zasady oceniania](https://cke.gov.pl/images/_EGZAMIN_MATURALNY_OD_2023/Arkusze_egzaminacyjne/2023/Fizyka/MFAP-R0-100-2305-zasady.pdf))
- Maj 2025, zad. 5.1 — ruch planet po elipsach a prawo powszechnego ciążenia ([arkusz](https://www.oke.poznan.pl/files/cms/875/mfap_r0_100_a_2505_arkusz.pdf), [zasady oceniania](https://cke.gov.pl/egzamin-maturalny/egzamin-maturalny-w-formule-2023/arkusze/2025-2/))
- Maj 2025, zad. 5.2 — II prawo Keplera jako zasada zachowania momentu pędu ([arkusz](https://www.oke.poznan.pl/files/cms/875/mfap_r0_100_a_2505_arkusz.pdf), [zasady oceniania](https://cke.gov.pl/egzamin-maturalny/egzamin-maturalny-w-formule-2023/arkusze/2025-2/))
- Maj 2025, zad. 5.3 — III prawo Keplera dla orbit kołowych i eliptycznych ([arkusz](https://www.oke.poznan.pl/files/cms/875/mfap_r0_100_a_2505_arkusz.pdf), [zasady oceniania](https://cke.gov.pl/egzamin-maturalny/egzamin-maturalny-w-formule-2023/arkusze/2025-2/))
- Maj 2026, zad. 5.2 — okres obiegu planetoidy (III prawo Keplera) ([arkusz](https://oke.wroc.pl/egzamin-maturalny/egzamin-maturalny-2026-arkusze/), [zasady oceniania](https://cke.gov.pl/egzamin-maturalny/egzamin-maturalny-w-formule-2023/arkusze/))
- Maj 2026, zad. 5.4 — prędkość planetoidy w aphelium ([arkusz](https://oke.wroc.pl/egzamin-maturalny/egzamin-maturalny-2026-arkusze/), [zasady oceniania](https://cke.gov.pl/egzamin-maturalny/egzamin-maturalny-w-formule-2023/arkusze/))

## Źródła

- OpenStax, *Fizyka dla szkół wyższych*, t. 1, rozdz. 13 — §13.5: prawa Keplera, orbity eliptyczne, wyznaczanie mas.
- Halliday, Resnick, Walker, *Podstawy fizyki* — wyd. 2015: t. 2, §13.6; wyd. 1: t. 2, §14.7.
- Symulacja PhET *Prawa Keplera*.
