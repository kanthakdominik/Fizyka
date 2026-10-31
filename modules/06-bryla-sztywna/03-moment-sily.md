# 06.03 — Moment siły i dynamika ruchu obrotowego

> **Moduł:** [06 — Bryła sztywna, statyka i sprężystość](README.md) · **Poziom:** 🟢 matura R · **Status:** ✅ pełny
>
> **Czytaj:**
>
> - OpenStax, *Fizyka dla szkół wyższych*, t. 1, rozdz. 10: [§10.6–10.8](https://openstax.org/books/fizyka-dla-szk%C3%B3%C5%82-wy%C5%BCszych-tom-1/pages/10-6-moment-sily) · [wstęp do rozdziału](https://openstax.org/books/fizyka-dla-szk%C3%B3%C5%82-wy%C5%BCszych-tom-1/pages/10-wstep)
> - Halliday, Resnick, Walker, *Podstawy fizyki*, wyd. 2015, t. 1: §10.6–10.8 (s. 350)
> - Halliday, Resnick, Walker, *Podstawy fizyki*, wyd. 1 (2003), t. 1: [§11.8–11.10, s. 276](https://home.agh.edu.pl/~czapli/Resnick_1.pdf#page=288) — PDF z serwera AGH

← [Moment bezwładności i twierdzenie Steinera](02-moment-bezwladnosci.md) · [spis modułu](README.md) · [Toczenie bez poślizgu](04-toczenie.md) →

## Po co to jest

Żeby otworzyć drzwi, pchamy je przy klamce, a nie przy zawiasach; żeby odkręcić zapieczoną śrubę, bierzemy dłuższy klucz. O skutku obrotowym siły decyduje nie tylko jej wartość, ale i ramię — to jest moment siły. II zasada dynamiki dla ruchu obrotowego $\tau = I\varepsilon$ pozwala liczyć bloczki z masą, wały, koła zamachowe i silniki, a moment siły jest też kluczem do równowagi (06.07) i momentu pędu (06.05).

## Teoria w pigułce

**Moment siły** względem osi (punktu O):

$$\vec{\tau} = \vec{r}\times\vec{F}, \qquad \tau = rF\sin\theta = F\cdot d,$$

gdzie $\vec{r}$ to wektor od osi do punktu przyłożenia siły, $\theta$ — kąt między $\vec{r}$ a $\vec{F}$, a $d = r\sin\theta$ — **ramię siły** (odległość osi od prostej, wzdłuż której działa siła). Jednostka: $\mathrm{N\cdot m}$ (nie dżul, choć wymiar ten sam).

Siła skierowana wzdłuż $\vec{r}$ (przez oś) nie daje momentu. Znak: przyjmujemy np. „przeciwnie do ruchu wskazówek zegara” jako dodatni.

**II zasada dynamiki dla ruchu obrotowego** (oś stała):

$$\sum\tau = I\varepsilon.$$

Analogia: siła ↔ moment siły, masa ↔ moment bezwładności, przyspieszenie ↔ przyspieszenie kątowe.

**Praca i moc w ruchu obrotowym.**

$$W = \int\tau\,d\theta \ (= \tau\theta\ \text{dla stałego } \tau), \qquad P = \tau\omega, \qquad W = \Delta\left(\tfrac12I\omega^2\right).$$

Moc silnika to iloczyn momentu obrotowego wału i jego prędkości kątowej — dlatego w danych technicznych samochodu podaje się moment obrotowy (N·m) i obroty.

**Bloczek z masą.** Gdy bloczek ma moment bezwładności $I$, naciągi nici po obu stronach są **różne** — ich różnica rozkręca bloczek: $(T_1 - T_2)R = I\varepsilon$, a przy braku poślizgu $a = \varepsilon R$.

## Wzory i założenia

| Wzór | Znaczenie | Kiedy obowiązuje |
|---|---|---|
| $\tau = rF\sin\theta = Fd$ | moment siły | $d$ — ramię siły |
| $\sum\tau = I\varepsilon$ | II zasada dla obrotu | stała oś, $I$ względem tej osi |
| $W = \tau\theta$, $\ P = \tau\omega$ | praca i moc | stały moment |
| $a = \dfrac{(m_1 - m_2)g}{m_1 + m_2 + I/R^2}$ | maszyna Atwooda z bloczkiem | nić się nie ślizga |
| $a = \dfrac{mg}{m + I/R^2}$ | ciężarek na nici nawiniętej na walec | oś walca nieruchoma |

## Przykład rozwiązany

**Zadanie 1.** Na koło o momencie bezwładności $0{,}5\ \mathrm{kg\cdot m^2}$ i promieniu 0,2 m nawinięto linkę, którą ciągniemy stycznie siłą 10 N. Oblicz przyspieszenie kątowe.

$\tau = 10\cdot0{,}2 = 2\ \mathrm{N\cdot m}$, $\varepsilon = 2/0{,}5 = 4\ \mathrm{rad/s^2}$.

**Zadanie 2 — Atwood z ciężkim bloczkiem.** Ciężarki 3 kg i 2 kg wiszą na nici przerzuconej przez bloczek w kształcie tarczy o masie 2 kg. Oblicz przyspieszenie i naciągi.

Trzy równania (oś ruchu: cięższy w dół):
- $m_1$: $m_1g - T_1 = m_1a$,
- $m_2$: $T_2 - m_2g = m_2a$,
- bloczek: $(T_1 - T_2)R = \tfrac12MR^2\cdot\dfrac{a}{R} \Rightarrow T_1 - T_2 = \tfrac12Ma$.

Dodając: $(m_1 - m_2)g = (m_1 + m_2 + \tfrac12M)a \Rightarrow a = \dfrac{g}{6} \approx 1{,}64\ \mathrm{m/s^2}$.

$T_1 = 3(9{,}81 - 1{,}64) \approx 24{,}5\ \mathrm{N}$, $T_2 = 2(9{,}81 + 1{,}64) \approx 22{,}9\ \mathrm{N}$. Przy nieważkim bloczku $a = g/5$, a naciągi byłyby równe.

### Wersja z rachunkiem różniczkowym i całkowym

**Zadanie.** Na koło zamachowe ($I = 0{,}5\ \mathrm{kg\cdot m^2}$, początkowo w spoczynku) działa moment siły rosnący liniowo: $\tau = 2t$ (N·m, s). Oblicz prędkość kątową i kąt obrotu po 3 s oraz wykonaną pracę.

$\varepsilon = \tau/I = 4t$, $\omega = 2t^2$, $\theta = \tfrac23t^3$. Po 3 s: $\omega = 18\ \mathrm{rad/s}$, $\theta = 18\ \mathrm{rad}$.

Praca: $W = \tfrac12I\omega^2 = 81\ \mathrm{J}$; sprawdzenie: $\displaystyle\int\tau\,d\theta = \int_0^3\tau\omega\,dt = \int_0^34t^3dt = 81\ \mathrm{J}$.

## Typowe pułapki

- **Ramię = odległość punktu przyłożenia.** Ramię to odległość osi od **linii działania** siły; równa się $r$ tylko dla siły prostopadłej do $\vec{r}$.
- **Równe naciągi po obu stronach bloczka z masą.** Są różne, gdy bloczek przyspiesza.
- **Moment bezwładności względem złej osi.** $\tau$ i $I$ muszą być liczone względem tej samej osi.
- **N·m = J.** Wymiarowo tak, ale moment siły to nie energia; nie zapisuj momentu w dżulach.

## Doświadczenie / symulacja

**Wahadło z linki i szpuli.** Nawiń linkę na szpulę (lub puszkę) osadzoną na ołówku jako osi i zawieś na lince ciężarek. Zmierz czas opadania ciężarka na znanej wysokości, oblicz $a$ i wyznacz moment bezwładności szpuli ze wzoru $a = mg/(m + I/R^2)$. Porównaj z $\tfrac12MR^2$.

**Symulacja PhET:** *Prawo dźwigni* — moment siły jako iloczyn siły i ramienia.

**Python:** Atwood z bloczkiem — jak masa bloczka zmienia przyspieszenie i naciągi.

```python
import numpy as np
import matplotlib.pyplot as plt

g, m1, m2 = 9.81, 3.0, 2.0
M = np.linspace(0, 10, 101)                  # masa bloczka-tarczy [kg]
a = (m1 - m2)*g/(m1 + m2 + M/2)
T1, T2 = m1*(g - a), m2*(g + a)
print(f"M = 0: a = {a[0]:.3f} m/s²;  M = 2 kg: a = {(m1-m2)*g/(m1+m2+1):.3f} m/s²")

plt.plot(M, a, label="a [m/s²]"); plt.plot(M, T1 - T2, label="T1 − T2 [N]")
plt.xlabel("masa bloczka [kg]"); plt.grid(True); plt.legend(); plt.show()
```

## Zadania

### A. Poziom maturalny

1. Klucz o długości 25 cm. Siła 80 N działa na koniec klucza a) prostopadle, b) pod kątem $30^\circ$ do klucza. Oblicz moment siły.

<details>
<summary>Odpowiedź</summary>

a) $20\ \mathrm{N\cdot m}$; b) $80\cdot0{,}25\cdot\sin30^\circ = 10\ \mathrm{N\cdot m}$.
</details>

2. Dlaczego klamkę umieszcza się daleko od zawiasów drzwi?

<details>
<summary>Odpowiedź</summary>

Większe ramię — ten sam moment siły uzyskujemy mniejszą siłą.
</details>

3. Na pełny walec o masie 4 kg i promieniu 10 cm (oś pozioma, nieruchoma) nawinięto nić, na której wisi ciężarek 1 kg. Oblicz przyspieszenie ciężarka i naciąg nici.

<details>
<summary>Odpowiedź</summary>

$a = \dfrac{mg}{m + M/2} = \dfrac{g}{3} \approx 3{,}27\ \mathrm{m/s^2}$; $T = m(g - a) \approx 6{,}54\ \mathrm{N}$.
</details>

4. Silnik rozwija moment obrotowy 200 N·m przy 3000 obr/min. Jaka jest jego moc?

<details>
<summary>Odpowiedź</summary>

$P = \tau\omega \approx 200\cdot314 \approx 62{,}8\ \mathrm{kW}$ (ok. 85 KM).
</details>

5. Huśtawka-ważka: dziecko o masie 30 kg siedzi 2 m od osi. Jaki moment siły wywiera jego ciężar?

<details>
<summary>Odpowiedź</summary>

$\tau = 30\cdot9{,}81\cdot2 \approx 589\ \mathrm{N\cdot m}$.
</details>

### B. Poziom akademicki _(opcjonalnie — rozszerzenie z rachunkiem)_

1. Jednorodny pręt o długości $L$ obraca się wokół osi przez jeden koniec. Puszczono go z położenia poziomego. Oblicz początkowe przyspieszenie kątowe i przyspieszenie wolnego końca. Porównaj z $g$.

<details>
<summary>Odpowiedź</summary>

$\varepsilon = \dfrac{mgL/2}{mL^2/3} = \dfrac{3g}{2L}$; koniec: $a = \tfrac32g$ — szybciej niż swobodny spadek.
</details>

2. Pręt z zadania 1 ($L = 1\ \mathrm{m}$) przechodzi przez położenie pionowe. Jaką ma prędkość kątową?

<details>
<summary>Odpowiedź</summary>

$mg\dfrac L2 = \tfrac12\cdot\tfrac13mL^2\omega^2 \Rightarrow \omega = \sqrt{3g/L} \approx 5{,}42\ \mathrm{rad/s}$.
</details>

3. Tarcza szlifierki ($I = 0{,}02\ \mathrm{kg\cdot m^2}$) obraca się z prędkością 300 rad/s. Po wyłączeniu silnika zatrzymuje się w ciągu 60 s ze stałym momentem tarcia. Oblicz ten moment i pracę tarcia.

<details>
<summary>Odpowiedź</summary>

$\tau = I\omega_0/t = 0{,}1\ \mathrm{N\cdot m}$; $W = -\tfrac12I\omega_0^2 = -900\ \mathrm{J}$.
</details>

### C. Zadania z arkuszy maturalnych CKE

Zadania z egzaminów maturalnych (poziom rozszerzony, formuła 2023), w których ten temat jest potrzebny. Rozwiąż je samodzielnie, a potem porównaj z zasadami oceniania. Pełne zestawienie: [matura/README.md](../../matura/README.md).

- Maj 2023, zad. 3.2 — przyspieszenie ciężarka na lince nawiniętej na walec ([arkusz](https://cke.gov.pl/images/_EGZAMIN_MATURALNY_OD_2023/Arkusze_egzaminacyjne/2023/Fizyka/MFAP-R0-100-2305.pdf), [zasady oceniania](https://cke.gov.pl/images/_EGZAMIN_MATURALNY_OD_2023/Arkusze_egzaminacyjne/2023/Fizyka/MFAP-R0-100-2305-zasady.pdf))
- Maj 2024, zad. 2.2 — przyspieszenie środka masy toczącego się walca (temat pomocniczy) ([arkusz](https://cke.gov.pl/images/_EGZAMIN_MATURALNY_OD_2023/Arkusze_egzaminacyjne/2024/Fizyka/MFAP-R0-100-A-2405-arkusz.pdf), [zasady oceniania](https://cke.gov.pl/egzamin-maturalny/egzamin-maturalny-w-formule-2023/arkusze/2024-2/))
- Maj 2025, zad. 2.2 — przyspieszenie walca toczącego się po równi (temat pomocniczy) ([arkusz](https://www.oke.poznan.pl/files/cms/875/mfap_r0_100_a_2505_arkusz.pdf), [zasady oceniania](https://cke.gov.pl/egzamin-maturalny/egzamin-maturalny-w-formule-2023/arkusze/2025-2/))
- Maj 2026, zad. 3.2 — siła przy ruchu ciężarka z przyspieszeniem g/2 (bloczek o masie) ([arkusz](https://oke.wroc.pl/egzamin-maturalny/egzamin-maturalny-2026-arkusze/), [zasady oceniania](https://cke.gov.pl/egzamin-maturalny/egzamin-maturalny-w-formule-2023/arkusze/))

## Źródła

- OpenStax, *Fizyka dla szkół wyższych*, t. 1, rozdz. 10 — §10.6 (moment siły), §10.7 (II zasada dynamiki dla ruchu obrotowego), §10.8 (praca i moc w ruchu obrotowym).
- Halliday, Resnick, Walker, *Podstawy fizyki* — wyd. 2015: t. 1, §10.6–10.8; wyd. 1: t. 1, §11.8–11.10.
- Symulacja PhET *Prawo dźwigni*.
