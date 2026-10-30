# 06.07 — Równowaga statyczna, naprężenia i prawo Hooke'a

> **Moduł:** [06 — Bryła sztywna, statyka i sprężystość](README.md) · **Poziom:** 🟢🔵 matura R + studia · **Status:** ✅ pełny
>
> **Czytaj:**
>
> - OpenStax, *Fizyka dla szkół wyższych*, t. 1, rozdz. 12: [§12.1–12.4](https://openstax.org/books/fizyka-dla-szk%C3%B3%C5%82-wy%C5%BCszych-tom-1/pages/12-1-warunki-rownowagi-statycznej) · [wstęp do rozdziału](https://openstax.org/books/fizyka-dla-szk%C3%B3%C5%82-wy%C5%BCszych-tom-1/pages/12-wstep)
> - Halliday, Resnick, Walker, *Podstawy fizyki*, wyd. 2015, t. 2: §12.1–12.3 (s. 1)
> - Halliday, Resnick, Walker, *Podstawy fizyki*, wyd. 1 (2003), t. 2: [§13.1–13.6, s. 2](https://home.agh.edu.pl/~czapli/Resnick_2.pdf#page=18) — PDF z serwera AGH

← [Precesja żyroskopu](06-precesja.md) · [spis modułu](README.md) · (koniec modułu) →

## Po co to jest

Mosty, belki, drabiny, dźwigi, ludzki kręgosłup — wszystko, co ma stać, musi spełniać warunki równowagi sił **i** momentów sił. A ponieważ żadne ciało nie jest naprawdę sztywne, trzeba też wiedzieć, jak bardzo się odkształci i kiedy pęknie. Ten temat to wstęp do statyki i wytrzymałości materiałów — przedmiotów obecnych na każdym kierunku politechnicznym.

## Teoria w pigułce

**Warunki równowagi bryły sztywnej.** Bryła spoczywa (lub porusza się jednostajnie bez przyspieszenia kątowego), gdy

$$\sum\vec{F} = 0 \quad\text{i}\quad \sum\vec{\tau} = 0.$$

Drugi warunek musi być spełniony względem **dowolnego** punktu — dlatego wybieramy punkt, przez który przechodzą nieznane siły (np. zawias, punkt podparcia), żeby wypadły z równania momentów.

**Ciężar bryły** działa w jej środku ciężkości (dla jednorodnego pola — środku masy, 05.04).

**Procedura.** 1) Rysunek wszystkich sił działających na bryłę, z punktami przyłożenia. 2) Równania sił (składowe $x$ i $y$). 3) Równanie momentów względem sprytnie wybranego punktu. 4) Rozwiązanie i sprawdzenie (np. momenty względem innego punktu).

**Sprężystość.** Pod działaniem siły ciała się odkształcają. Dla małych odkształceń obowiązuje **prawo Hooke'a** w postaci materiałowej:

$$\sigma = E\varepsilon, \qquad \sigma = \frac{F}{S}\ \text{(naprężenie)}, \qquad \varepsilon = \frac{\Delta L}{L_0}\ \text{(odkształcenie względne)},$$

gdzie $E$ to **moduł Younga** — cecha materiału (stal ok. $200\ \mathrm{GPa}$, aluminium $70\ \mathrm{GPa}$, kość $15$–$20\ \mathrm{GPa}$, guma ok. $0{,}01$–$0{,}1\ \mathrm{GPa}$). Analogicznie definiuje się moduł ścinania (zmiana kształtu) i moduł ściśliwości (zmiana objętości pod ciśnieniem).

**Poza zakresem sprężystym.** Powyżej **granicy sprężystości** materiał odkształca się trwale (plastycznie), a po przekroczeniu **wytrzymałości na rozciąganie** pęka. Stal konstrukcyjna: granica plastyczności ok. 250 MPa, wytrzymałość ok. 400–500 MPa.

## Wzory i założenia

| Wzór | Znaczenie | Kiedy obowiązuje |
|---|---|---|
| $\sum\vec{F} = 0$, $\ \sum\vec{\tau} = 0$ | równowaga bryły | momenty względem dowolnego punktu |
| $\sigma = F/S$, $\ \varepsilon = \Delta L/L_0$ | naprężenie, odkształcenie | rozciąganie lub ściskanie |
| $\sigma = E\varepsilon \Rightarrow \Delta L = \dfrac{FL_0}{ES}$ | prawo Hooke'a | poniżej granicy sprężystości |
| $k = \dfrac{ES}{L_0}$ | „współczynnik sprężystości” pręta | j.w. |
| $W = \tfrac12F\Delta L$ | energia sprężystości pręta | j.w. |

## Przykład rozwiązany

**Zadanie 1 — kładka.** Jednorodna deska o długości 4 m i masie 20 kg leży na dwóch podporach na swoich końcach. Człowiek o masie 70 kg stoi 1 m od lewego końca. Oblicz siły nacisku podpór.

Momenty względem lewej podpory (jej siła wypada): $R_P\cdot4 = 20g\cdot2 + 70g\cdot1 \Rightarrow R_P \approx 270\ \mathrm{N}$. Z równowagi sił: $R_L = 90g - R_P \approx 613\ \mathrm{N}$.

**Sprawdzenie** momentami względem prawej podpory: $R_L\cdot4 = 20g\cdot2 + 70g\cdot3 = 2453\ \mathrm{N\cdot m} \Rightarrow R_L \approx 613\ \mathrm{N}$. Zgadza się.

**Zadanie 2 — drabina.** Drabina o długości 5 m i masie 15 kg opiera się o gładką ścianę pod kątem $60^\circ$ do podłogi. Jaki najmniejszy współczynnik tarcia o podłogę zapobiega jej zsunięciu?

Siły: ciężar $mg$ w środku, reakcja podłogi $N$ (pionowo) i tarcie $T$ (poziomo, do ściany), reakcja ściany $N_s$ (poziomo, od ściany — ściana gładka).

- Pionowo: $N = mg$. Poziomo: $T = N_s$.
- Momenty względem dolnego końca: $N_s\cdot L\sin60^\circ = mg\cdot\tfrac L2\cos60^\circ \Rightarrow N_s = \dfrac{mg}{2\tan60^\circ} \approx 42{,}5\ \mathrm{N}$.
- $\mu \ge T/N = \dfrac{1}{2\tan60^\circ} \approx 0{,}29$.

**Zadanie 3 — drut.** Stalowy drut o długości 2 m i średnicy 1 mm obciążono siłą 100 N. O ile się wydłuży ($E = 200\ \mathrm{GPa}$)?

$S = \pi(0{,}5\cdot10^{-3})^2 \approx 7{,}85\cdot10^{-7}\ \mathrm{m^2}$, $\sigma \approx 127\ \mathrm{MPa}$ (poniżej granicy plastyczności), $\varepsilon = \sigma/E \approx 6{,}4\cdot10^{-4}$, $\Delta L \approx 1{,}3\ \mathrm{mm}$.

### Wersja z rachunkiem różniczkowym i całkowym

**Zadanie.** Stalowa lina o długości $L$ zwisa pionowo pod własnym ciężarem. O ile się wydłuży? Jaka jest największa długość liny, która nie zerwie się pod własnym ciężarem?

Odcinek $dx$ w odległości $x$ od dolnego końca jest rozciągany ciężarem liny poniżej: $\sigma(x) = \rho gx$. Jego wydłużenie $d(\Delta L) = \dfrac{\rho gx}{E}dx$:

$$\Delta L = \int_0^L\frac{\rho gx}{E}dx = \frac{\rho gL^2}{2E}.$$

Dla $L = 1\ \mathrm{km}$: $\Delta L = \dfrac{7850\cdot9{,}81\cdot10^6}{2\cdot2\cdot10^{11}} \approx 0{,}19\ \mathrm{m}$. Największe naprężenie jest na górze: $\rho gL$. Lina zerwie się, gdy $\rho gL$ przekroczy wytrzymałość (500 MPa): $L_{\max} = \dfrac{5\cdot10^8}{7850\cdot9{,}81} \approx 6{,}5\ \mathrm{km}$ — tzw. długość zrywająca.

## Typowe pułapki

- **Tylko równowaga sił.** Bez równania momentów deska „obróciłaby się”, a zadanie ma nieskończenie wiele rozwiązań.
- **Zły punkt odniesienia momentów.** Wybieraj punkt, przez który przechodzą nieznane siły.
- **Ramię siły zamiast odległości.** Liczy się odległość osi od linii działania siły.
- **Średnica zamiast promienia w polu przekroju.** $S = \pi d^2/4$.
- **Prawo Hooke'a poza zakresem sprężystym.** Sprawdź, czy naprężenie jest poniżej granicy plastyczności.

## Doświadczenie / symulacja

**Symulacja PhET:** *Prawo dźwigni* (*Balancing Act*) — zrównoważ deskę ciężarkami i sprawdź warunek momentów.

**Dźwignia z linijki.** Połóż linijkę na ołówku jako podporze i zrównoważ monety po obu stronach. Zmierz ramiona i sprawdź $m_1d_1 = m_2d_2$. Wyznacz w ten sposób nieznaną masę.

**Python:** siły w drabinie w zależności od kąta nachylenia — przy jakim kącie drabina zacznie się zsuwać.

```python
import numpy as np
import matplotlib.pyplot as plt

m, g, mu = 15.0, 9.81, 0.4
theta = np.radians(np.linspace(40, 85, 200))
N_wall = m*g/(2*np.tan(theta))
mu_req = N_wall/(m*g)
th_min = np.degrees(np.arctan(1/(2*mu)))
print(f"przy μ = {mu} drabina stoi dla kąta ≥ {th_min:.1f}°")
plt.plot(np.degrees(theta), mu_req, label="potrzebny μ"); plt.axhline(mu, ls="--", color="gray", label="μ podłogi")
plt.xlabel("kąt drabiny do podłogi [°]"); plt.ylabel("μ"); plt.grid(True); plt.legend(); plt.show()
```

## Zadania

### A. Poziom maturalny

1. Na huśtawce-ważce dziecko o masie 30 kg siedzi 2 m od osi. W jakiej odległości od osi powinno usiąść dziecko o masie 40 kg?

<details>
<summary>Odpowiedź</summary>

$1{,}5\ \mathrm{m}$.
</details>

2. Jednorodna belka o masie 50 kg i długości 6 m jest podparta w punktach odległych o 1 m od lewego końca i 1 m od prawego. Na prawym końcu stoi człowiek o masie 80 kg. Oblicz siły podpór.

<details>
<summary>Odpowiedź</summary>

Momenty względem lewej podpory ($x = 1$): $R_P\cdot4 = 50g\cdot2 + 80g\cdot5 \Rightarrow R_P = 125g \approx 1226\ \mathrm{N}$; $R_L = 130g - 125g = 5g \approx 49\ \mathrm{N}$. (Przy cięższym człowieku belka uniosłaby się z lewej podpory.)
</details>

3. Lampa o masie 4 kg wisi na końcu poziomego, lekkiego wysięgnika o długości 1 m, zamocowanego na zawiasie do ściany i podtrzymywanego linką przyczepioną do końca wysięgnika i do ściany 1 m nad zawiasem. Oblicz naciąg linki.

<details>
<summary>Odpowiedź</summary>

Linka pod kątem $45^\circ$; momenty względem zawiasu: $T\sin45^\circ\cdot1 = mg\cdot1 \Rightarrow T \approx 55{,}5\ \mathrm{N}$.
</details>

4. Stalowy drut o długości 2 m i średnicy 1 mm obciążono masą 10 kg. O ile się wydłużył? ($E = 200\ \mathrm{GPa}$)

<details>
<summary>Odpowiedź</summary>

$F \approx 98\ \mathrm{N}$, $\Delta L \approx 1{,}25\ \mathrm{mm}$.
</details>

### B. Poziom akademicki

1. Pokaż, że drabina oparta o gładką ścianę pod kątem $\theta$ do podłogi nie zsunie się, jeśli $\mu \ge \dfrac{1}{2\tan\theta}$. Przy jakim najmniejszym kącie stoi drabina, gdy $\mu = 0{,}4$?

<details>
<summary>Odpowiedź</summary>

Z momentów: $N_s = \dfrac{mg}{2\tan\theta}$, $T = N_s \le \mu mg$. Dla $\mu = 0{,}4$: $\tan\theta \ge 1{,}25$, $\theta \ge 51{,}3^\circ$.
</details>

2. Oblicz energię sprężystości zgromadzoną w drucie z zadania A4.

<details>
<summary>Odpowiedź</summary>

$W = \tfrac12F\Delta L \approx \tfrac12\cdot98\cdot1{,}25\cdot10^{-3} \approx 0{,}061\ \mathrm{J}$.
</details>

3. Stalowa lina zwisa z helikoptera. Jaką największą długość może mieć, jeśli wytrzymałość stali wynosi 500 MPa, a na końcu wisi ładunek wywołujący naprężenie 200 MPa?

<details>
<summary>Odpowiedź</summary>

$\rho gL + 200\ \mathrm{MPa} \le 500\ \mathrm{MPa} \Rightarrow L \le \dfrac{3\cdot10^8}{7850\cdot9{,}81} \approx 3{,}9\ \mathrm{km}$.
</details>

4. Pręt stalowy i aluminiowy o tych samych wymiarach połączono szeregowo i rozciągnięto siłą $F$. Który wydłuży się bardziej i ile razy? A gdy połączymy je równolegle (obie końcówki wspólne) — jak rozłoży się siła?

<details>
<summary>Odpowiedź</summary>

Szeregowo (ta sama siła): aluminiowy ok. $200/70 \approx 2{,}9$ razy bardziej. Równolegle (to samo wydłużenie): siły proporcjonalne do $E$ — stalowy przenosi ok. 74% siły.
</details>

## Źródła

- OpenStax, *Fizyka dla szkół wyższych*, t. 1, rozdz. 12 — §12.1–12.2 (warunki i przykłady równowagi statycznej), §12.3–12.4 (naprężenie, odkształcenie, sprężystość i plastyczność).
- Halliday, Resnick, Walker, *Podstawy fizyki* — wyd. 2015: t. 2, §12.1–12.3; wyd. 1: t. 2, §13.1–13.6.
- Symulacja PhET *Prawo dźwigni*.
