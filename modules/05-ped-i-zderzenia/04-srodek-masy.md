# 05.04 — Środek masy układu i bryły

> **Moduł:** [05 — Pęd, środek masy i zderzenia](README.md) · **Poziom:** 🟢🔵 matura R + studia · **Status:** ✅ pełny
>
> **Czytaj:**
>
> - OpenStax, *Fizyka dla szkół wyższych*, t. 1, rozdz. 9: [§9.6](https://openstax.org/books/fizyka-dla-szk%C3%B3%C5%82-wy%C5%BCszych-tom-1/pages/9-6-srodek-masy) · [wstęp do rozdziału](https://openstax.org/books/fizyka-dla-szk%C3%B3%C5%82-wy%C5%BCszych-tom-1/pages/9-wstep)
> - Halliday, Resnick, Walker, *Podstawy fizyki*, wyd. 2015, t. 1: §9.1–9.2 (s. 271)
> - Halliday, Resnick, Walker, *Podstawy fizyki*, wyd. 1 (2003), t. 1: [§9.1–9.3, s. 204](https://home.agh.edu.pl/~czapli/Resnick_1.pdf#page=216) — PDF z serwera AGH

← [Zderzenia sprężyste i niesprężyste w 1D i 2D](03-zderzenia.md) · [spis modułu](README.md) · [Układy o zmiennej masie — rakieta](05-zmienna-masa-rakieta.md) →

## Po co to jest

Ruch ciała rozciągłego lub układu ciał może być bardzo skomplikowany — młot obraca się w locie, gimnastyczka wykonuje salto, pocisk rozpada się na kawałki. Ale jeden punkt, **środek masy**, porusza się tak, jakby cała masa była w nim skupiona, a wszystkie siły zewnętrzne do niego przyłożone. Dzięki temu zasady dynamiki punktu stosują się do ciał rozciągłych; środek masy wraca też w równowadze brył (06.07) i w ruchu planet wokół wspólnego środka masy (07).

## Teoria w pigułce

**Środek masy układu punktów** to średnia ważona masami:

$$\vec{r}_{\mathrm{SM}} = \frac{\sum m_i\vec{r}_i}{\sum m_i}, \qquad x_{\mathrm{SM}} = \frac{m_1x_1 + m_2x_2 + \dots}{m_1 + m_2 + \dots}.$$

Dla dwóch ciał leży na odcinku je łączącym, bliżej cięższego, w odległościach odwrotnie proporcjonalnych do mas: $m_1d_1 = m_2d_2$.

**Ciało ciągłe.** Sumę zastępujemy całką (00.07):

$$\vec{r}_{\mathrm{SM}} = \frac{1}{M}\int\vec{r}\,dm.$$

Dla jednorodnych ciał symetrycznych środek masy leży w środku symetrii; może leżeć poza ciałem (pierścień, bumerang, litera L).

**Ruch środka masy.** Dla układu o całkowitej masie $M$:

$$M\vec{a}_{\mathrm{SM}} = \sum\vec{F}_{\text{zewn}}, \qquad \vec{P} = M\vec{v}_{\mathrm{SM}}.$$

Siły wewnętrzne nie zmieniają ruchu środka masy. Wnioski:
- pocisk rozpadający się w locie — środek masy odłamków porusza się dalej po paraboli (05.02);
- skoczek wzwyż w stylu Fosbury'ego przenosi środek masy pod poprzeczką, choć ciało przechodzi nad nią;
- gdy siły zewnętrzne są zerowe, środek masy porusza się jednostajnie — albo spoczywa (człowiek w łódce, 05.02).

**Środek ciężkości** pokrywa się ze środkiem masy, gdy pole grawitacyjne jest jednorodne — w praktyce dla wszystkich ciał na Ziemi z wyjątkiem bardzo wysokich budowli.

## Wzory i założenia

| Wzór | Znaczenie | Kiedy obowiązuje |
|---|---|---|
| $x_{\mathrm{SM}} = \sum m_ix_i/\sum m_i$ | środek masy punktów | — |
| $\vec{r}_{\mathrm{SM}} = \frac1M\int\vec{r}\,dm$ | środek masy ciała ciągłego | $dm = \lambda\,dl$, $\sigma\,dA$ lub $\rho\,dV$ |
| $M\vec{a}_{\mathrm{SM}} = \sum\vec{F}_{\text{zewn}}$ | ruch środka masy | — |
| $\vec{P} = M\vec{v}_{\mathrm{SM}}$ | pęd układu | — |
| $y_{\mathrm{SM}} = \dfrac{4R}{3\pi}$ | półkole (płytka) | od średnicy |
| $y_{\mathrm{SM}} = \dfrac{h}{4}$ | stożek pełny | od podstawy |

## Przykład rozwiązany

**Zadanie (poziom maturalny).** Gdzie leży środek masy układu Ziemia–Księżyc? Masy: $5{,}97\cdot10^{24}\ \mathrm{kg}$ i $7{,}35\cdot10^{22}\ \mathrm{kg}$, odległość $3{,}84\cdot10^8\ \mathrm{m}$.

Początek układu w środku Ziemi: $x = \dfrac{7{,}35\cdot10^{22}\cdot3{,}84\cdot10^8}{5{,}97\cdot10^{24} + 7{,}35\cdot10^{22}} \approx 4{,}67\cdot10^6\ \mathrm{m}$.

To mniej niż promień Ziemi (6370 km) — środek masy leży wewnątrz Ziemi, ok. 1700 km pod powierzchnią. Wokół tego punktu obiegają się oba ciała; Ziemia „chybocze” się raz w miesiącu.

### Wersja z rachunkiem różniczkowym i całkowym

**Zadanie.** Wyznacz środek masy jednorodnej płytki w kształcie półkola o promieniu $R$.

Z symetrii $x_{\mathrm{SM}} = 0$. Dzielimy płytkę na poziome paski o grubości $dy$ na wysokości $y$; pasek ma długość $2\sqrt{R^2 - y^2}$ i masę $dm = \sigma\cdot2\sqrt{R^2 - y^2}\,dy$:

$$y_{\mathrm{SM}} = \frac{1}{M}\int_0^Ry\,\sigma\,2\sqrt{R^2 - y^2}\,dy = \frac{2\sigma}{M}\cdot\frac{R^3}{3} = \frac{2}{\pi R^2/2}\cdot\frac{R^3}{3} = \frac{4R}{3\pi} \approx 0{,}42R.$$

(Całka: podstawienie $u = R^2 - y^2$ daje $\int_0^Ry\sqrt{R^2 - y^2}\,dy = R^3/3$.)

## Typowe pułapki

- **Środek masy w środku geometrycznym.** Tylko dla ciał jednorodnych i symetrycznych.
- **Środek masy musi leżeć w ciele.** Nie musi — pierścień, podkowa, układ dwóch gwiazd.
- **Siły wewnętrzne zmieniają ruch środka masy.** Nie zmieniają; skoczek w powietrzu nie zmieni toru swojego środka masy, machając rękami.
- **Zapomniany znak współrzędnej.** Przy obiektach po obu stronach początku układu współrzędne mają różne znaki.

## Doświadczenie / symulacja

**Wyznaczanie środka masy.** Wytnij z tektury nieregularny kształt. Zawieś go kolejno w trzech punktach na szpilce, za każdym razem rysując pion (nitka z ciężarkiem). Pionowe linie przecinają się w środku masy. Sprawdź, że w tym punkcie kształt balansuje na czubku ołówka.

**Symulacja PhET:** *Prawo dźwigni* (*Balancing Act*, [phet.colorado.edu/pl](https://phet.colorado.edu/pl/)) — równoważenie mas na desce.

**Python:** środek masy płytki o dowolnym kształcie liczony z siatki punktów (metoda przydatna, gdy całki są trudne).

```python
import numpy as np

R = 1.0
x, y = np.meshgrid(np.linspace(-R, R, 801), np.linspace(-R, R, 801))
dA = (x[0, 1] - x[0, 0]) * (y[1, 0] - y[0, 0])

# Półkole y ≥ 0
inside = (x**2 + y**2 <= R**2) & (y >= 0)
print(f"półkole: y_SM = {y[inside].mean():.4f} R (wzór 4/(3π) = {4/(3*np.pi):.4f})")

# Koło z wyciętym otworem o promieniu R/2 o środku w (R/2, 0)
plate = (x**2 + y**2 <= R**2) & ~((x - R/2)**2 + y**2 <= (R/2)**2)
print(f"koło z otworem: x_SM = {x[plate].mean():.4f} R (wzór −1/6 = {-1/6:.4f})")
print(f"pole płytki ≈ {plate.sum()*dA:.4f} (dokładnie 3π/4 = {3*np.pi/4:.4f})")
```

## Zadania

### A. Poziom maturalny

1. Ciała o masach 2 kg i 3 kg leżą na osi $x$ w punktach $x = 0$ i $x = 5\ \mathrm{m}$. Gdzie jest środek masy?

<details>
<summary>Odpowiedź</summary>

$x = 15/5 = 3\ \mathrm{m}$.
</details>

2. Trzy ciała: 1 kg w $(0,\ 0)$, 2 kg w $(2,\ 0)$, 3 kg w $(0,\ 3)$ (w metrach). Wyznacz środek masy.

<details>
<summary>Odpowiedź</summary>

$x = 4/6 \approx 0{,}67\ \mathrm{m}$, $y = 9/6 = 1{,}5\ \mathrm{m}$.
</details>

3. Dwaj łyżwiarze o masach 80 kg i 50 kg stoją na lodzie 13 m od siebie i ciągną za linę. Gdzie się spotkają?

<details>
<summary>Odpowiedź</summary>

W środku masy, który się nie porusza: $50\ \mathrm{kg}\cdot13\ \mathrm{m}/130\ \mathrm{kg} = 5\ \mathrm{m}$ od cięższego.
</details>

4. Pocisk wystrzelony ukośnie wybucha w locie na kilka odłamków. Jaki tor zakreśla środek masy odłamków (do chwili, gdy któryś uderzy w ziemię)? Dlaczego?

<details>
<summary>Odpowiedź</summary>

Tę samą parabolę co pocisk bez wybuchu — siły wybuchu są wewnętrzne, a jedyna siła zewnętrzna (ciężar) się nie zmieniła.
</details>

### B. Poziom akademicki

1. Wyznacz środek masy jednorodnego stożka o wysokości $h$ (odległość od podstawy).

<details>
<summary>Odpowiedź</summary>

Plaster na wysokości $z$ ma promień $R(1 - z/h)$; $z_{\mathrm{SM}} = \dfrac{\int_0^hz(1 - z/h)^2dz}{\int_0^h(1 - z/h)^2dz} = \dfrac{h^2/12}{h/3} = \dfrac{h}{4}$.
</details>

2. Z jednorodnej okrągłej płytki o promieniu $R$ wycięto otwór o promieniu $R/2$, którego środek leży w odległości $R/2$ od środka płytki. Gdzie jest środek masy pozostałej części?

<details>
<summary>Odpowiedź</summary>

Traktujemy otwór jak masę ujemną: $x = \dfrac{0\cdot M - \tfrac{M}{4}\cdot\tfrac{R}{2}}{M - \tfrac{M}{4}} = -\dfrac{R}{6}$.
</details>

3. Pręt o długości $L$ ma gęstość liniową $\lambda(x) = \lambda_0x^2/L^2$. Gdzie jest jego środek masy?

<details>
<summary>Odpowiedź</summary>

$x_{\mathrm{SM}} = \dfrac{\int_0^Lx^3dx}{\int_0^Lx^2dx} = \dfrac{3L}{4}$.
</details>

4. Pokaż, że $M\vec{a}_{\mathrm{SM}} = \sum\vec{F}_{\text{zewn}}$, sumując II zasadę dla wszystkich cząstek układu i korzystając z III zasady.

<details>
<summary>Odpowiedź</summary>

$\sum m_i\vec{a}_i = \sum\vec{F}_{\text{zewn},i} + \sum_{i\ne j}\vec{F}_{ij}$; siły wewnętrzne znoszą się parami ($\vec{F}_{ij} = -\vec{F}_{ji}$), a $\sum m_i\vec{a}_i = M\vec{a}_{\mathrm{SM}}$.
</details>

### C. Zadania z arkuszy maturalnych CKE

Zadania z egzaminów maturalnych (poziom rozszerzony, formuła 2023), w których ten temat jest potrzebny. Rozwiąż je samodzielnie, a potem porównaj z zasadami oceniania. Pełne zestawienie: [matura/README.md](../../matura/README.md).

- Maj 2024, zad. 5.1 — siły grawitacji Ziemia–Księżyc, środek masy układu (temat pomocniczy) ([arkusz](https://cke.gov.pl/images/_EGZAMIN_MATURALNY_OD_2023/Arkusze_egzaminacyjne/2024/Fizyka/MFAP-R0-100-A-2405-arkusz.pdf), [zasady oceniania](https://cke.gov.pl/egzamin-maturalny/egzamin-maturalny-w-formule-2023/arkusze/2024-2/))

## Źródła

- OpenStax, *Fizyka dla szkół wyższych*, t. 1, rozdz. 9 — §9.6: środek masy punktów i ciał ciągłych.
- Halliday, Resnick, Walker, *Podstawy fizyki* — wyd. 2015: t. 1, §9.1–9.2; wyd. 1: t. 1, §9.1–9.3.
- Symulacja PhET *Prawo dźwigni*.
