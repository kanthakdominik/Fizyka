# 06.02 — Moment bezwładności i twierdzenie Steinera

> **Moduł:** [06 — Bryła sztywna, statyka i sprężystość](README.md) · **Poziom:** 🟢🔵 matura R + studia · **Status:** ✅ pełny
>
> **Czytaj:**
>
> - OpenStax, *Fizyka dla szkół wyższych*, t. 1, rozdz. 10: [§10.4–10.5](https://openstax.org/books/fizyka-dla-szk%C3%B3%C5%82-wy%C5%BCszych-tom-1/pages/10-4-moment-bezwladnosci-i-energia-kinetyczna-w-ruchu-obrotowym) · [wstęp do rozdziału](https://openstax.org/books/fizyka-dla-szk%C3%B3%C5%82-wy%C5%BCszych-tom-1/pages/10-wstep)
> - Halliday, Resnick, Walker, *Podstawy fizyki*, wyd. 2015, t. 1: §10.4–10.5 (s. 343)
> - Halliday, Resnick, Walker, *Podstawy fizyki*, wyd. 1 (2003), t. 1: [§11.6–11.7, s. 271](https://home.agh.edu.pl/~czapli/Resnick_1.pdf#page=283) — PDF z serwera AGH

← [Kinematyka ruchu obrotowego](01-kinematyka-obrotow.md) · [spis modułu](README.md) · [Moment siły i dynamika ruchu obrotowego](03-moment-sily.md) →

## Po co to jest

Masa mówi, jak trudno rozpędzić ciało w ruchu postępowym; **moment bezwładności** — jak trudno rozkręcić je w ruchu obrotowym. Zależy nie tylko od masy, ale i od tego, jak daleko od osi jest ona rozłożona. Dlatego koło zamachowe ma masę na obwodzie, łyżwiarka przyspiesza obrót, przyciągając ręce, a pełna puszka toczy się z równi szybciej niż pusta rura (06.04).

## Teoria w pigułce

**Energia kinetyczna ruchu obrotowego.** Punkt w odległości $r_i$ od osi ma prędkość $\omega r_i$, więc

$$E_k = \sum\tfrac12m_i(\omega r_i)^2 = \tfrac12\left(\sum m_ir_i^2\right)\omega^2 = \tfrac12I\omega^2.$$

**Moment bezwładności** względem danej osi:

$$I = \sum m_ir_i^2, \qquad I = \int r_\perp^2\,dm,$$

gdzie $r_\perp$ to odległość od **osi** (nie od środka). Jednostka: $\mathrm{kg\cdot m^2}$. Ta sama bryła ma różne momenty względem różnych osi.

**Najważniejsze momenty bezwładności** (oś przez środek masy, jeśli nie zaznaczono inaczej):

| Bryła | Oś | $I$ |
|---|---|---|
| obręcz, cienka rura | oś symetrii | $MR^2$ |
| walec pełny, tarcza | oś symetrii | $\tfrac12MR^2$ |
| kula pełna | przez środek | $\tfrac25MR^2$ |
| sfera (cienka powłoka) | przez środek | $\tfrac23MR^2$ |
| pręt cienki | prostopadle, przez środek | $\tfrac1{12}ML^2$ |
| pręt cienki | prostopadle, przez koniec | $\tfrac13ML^2$ |
| płytka prostokątna $a\times b$ | prostopadle, przez środek | $\tfrac1{12}M(a^2 + b^2)$ |

**Twierdzenie Steinera.** Moment bezwładności względem osi równoległej do osi przez środek masy, odległej o $d$:

$$I = I_{\mathrm{SM}} + Md^2.$$

Najmniejszy moment bezwładności (dla danego kierunku osi) jest względem osi przez środek masy.

## Wzory i założenia

| Wzór | Znaczenie | Kiedy obowiązuje |
|---|---|---|
| $I = \sum m_ir_i^2 = \int r_\perp^2\,dm$ | moment bezwładności | $r_\perp$ — odległość od osi |
| $E_k = \tfrac12I\omega^2$ | energia ruchu obrotowego | obrót wokół stałej osi |
| $I = I_{\mathrm{SM}} + Md^2$ | twierdzenie Steinera | osie równoległe |
| $I_z = I_x + I_y$ | twierdzenie o osiach prostopadłych | tylko płaskie płytki |
| $I = Mk^2$ | promień bezwładności $k$ | definicja |

## Przykład rozwiązany

**Zadanie 1.** Dwa ciężarki po 1 kg są przymocowane do końców lekkiego pręta o długości 0,6 m. Oblicz moment bezwładności względem osi prostopadłej do pręta przechodzącej a) przez jego środek, b) przez jeden koniec.

a) $I = 2\cdot1\cdot0{,}3^2 = 0{,}18\ \mathrm{kg\cdot m^2}$. b) $I = 1\cdot0 + 1\cdot0{,}6^2 = 0{,}36\ \mathrm{kg\cdot m^2}$ (Steiner: $0{,}18 + 2\cdot0{,}3^2 = 0{,}36$).

**Zadanie 2.** Koło zamachowe w kształcie pełnego walca o masie 10 kg i promieniu 20 cm obraca się z prędkością 3000 obr/min. Ile energii magazynuje?

$I = \tfrac12\cdot10\cdot0{,}04 = 0{,}2\ \mathrm{kg\cdot m^2}$, $\omega \approx 314\ \mathrm{rad/s}$, $E = \tfrac12\cdot0{,}2\cdot314^2 \approx 9{,}9\ \mathrm{kJ}$ — tyle, ile ma samochód jadący 15 km/h.

### Wersja z rachunkiem różniczkowym i całkowym

**Zadanie.** Wyprowadź moment bezwładności jednorodnego pręta o masie $M$ i długości $L$ względem osi prostopadłej przez środek i przez koniec.

Gęstość liniowa $\lambda = M/L$, element $dm = \lambda\,dx$ w odległości $x$ od osi:

$$I_{\mathrm{SM}} = \int_{-L/2}^{L/2}x^2\frac{M}{L}\,dx = \frac{M}{L}\cdot\frac{2}{3}\left(\frac{L}{2}\right)^3 = \frac{ML^2}{12}, \qquad I_{\text{koniec}} = \int_0^Lx^2\frac{M}{L}\,dx = \frac{ML^2}{3}.$$

Sprawdzenie Steinerem: $\tfrac1{12}ML^2 + M\left(\tfrac L2\right)^2 = \tfrac13ML^2$. Momenty tarczy i kuli wyprowadziliśmy w [00.07](../00-narzedzia-matematyczne/07-wspolrzedne-i-calki-wielokrotne.md).

## Typowe pułapki

- **Odległość od środka zamiast od osi.** W kuli punkt na „biegunie” leży na osi i ma $r_\perp = 0$.
- **Steiner od dowolnej osi.** Twierdzenie łączy oś przez **środek masy** z osią równoległą; nie przenosi między dwiema dowolnymi osiami.
- **Moment bezwładności to własność ciała.** To własność ciała **i osi**.
- **Masa skupiona w środku.** Dla ruchu obrotowego nie wolno zastępować bryły punktem w środku masy — dałoby $I = 0$.

## Doświadczenie / symulacja

**Wyścig puszek.** Puść jednocześnie z tej samej równi pełną puszkę (np. konserwę) i pustą rurę lub puszkę bez dna o podobnych wymiarach. Pełna wygrywa — ma mniejszy moment bezwładności w stosunku do $MR^2$ (06.04).

**Python:** moment bezwładności z rozkładu masy — tarcza, obręcz i pręt jako zbiory punktów; sprawdzenie twierdzenia Steinera.

```python
import numpy as np

rng = np.random.default_rng(0)
M, R, N = 2.0, 0.1, 400_000

# Tarcza: punkty rozłożone równomiernie po kole
r = R*np.sqrt(rng.uniform(0, 1, N)); phi = rng.uniform(0, 2*np.pi, N)
x, y = r*np.cos(phi), r*np.sin(phi)
m = M/N
I_center = np.sum(m*(x**2 + y**2))
I_edge = np.sum(m*((x - R)**2 + y**2))          # oś równoległa przez brzeg
print(f"tarcza, środek: {I_center:.5f} (wzór {0.5*M*R**2:.5f})")
print(f"tarcza, brzeg:  {I_edge:.5f} (Steiner {0.5*M*R**2 + M*R**2:.5f})")

# Pręt L = 1 m: oś przez środek i koniec
L = 1.0; xs = rng.uniform(-L/2, L/2, N)
print(f"pręt: środek {np.sum(m*xs**2):.4f} (≈ML²/12 = {M*L**2/12:.4f}), koniec {np.sum(m*(xs+L/2)**2):.4f} (ML²/3 = {M*L**2/3:.4f})")
```

## Zadania

### A. Poziom maturalny

1. Obręcz i tarcza mają tę samą masę i promień. Którą łatwiej rozkręcić? Ile razy różnią się ich momenty bezwładności?

<details>
<summary>Odpowiedź</summary>

Tarczę — ma dwa razy mniejszy moment bezwładności.
</details>

2. Trzy kulki po 0,2 kg leżą w wierzchołkach trójkąta równobocznego o boku 30 cm, połączone lekkimi prętami. Oblicz moment bezwładności względem osi prostopadłej do płaszczyzny trójkąta, przechodzącej przez jeden z wierzchołków.

<details>
<summary>Odpowiedź</summary>

Dwie kulki w odległości 0,3 m: $I = 2\cdot0{,}2\cdot0{,}09 = 0{,}036\ \mathrm{kg\cdot m^2}$.
</details>

3. Tarcza o masie 2 kg i promieniu 10 cm obraca się wokół osi prostopadłej do niej przechodzącej przez punkt na jej brzegu. Oblicz moment bezwładności.

<details>
<summary>Odpowiedź</summary>

$I = \tfrac12MR^2 + MR^2 = 0{,}01 + 0{,}02 = 0{,}03\ \mathrm{kg\cdot m^2}$.
</details>

4. Koło zamachowe ma energię 9,9 kJ przy 3000 obr/min. Jaką będzie miało energię przy 1500 obr/min?

<details>
<summary>Odpowiedź</summary>

Cztery razy mniejszą: ok. 2,5 kJ.
</details>

### B. Poziom akademicki

1. Wyprowadź moment bezwładności cienkiej sfery o masie $M$ i promieniu $R$ względem średnicy. (Wskazówka: pierścienie o promieniu $R\sin\theta$ i masie $dm = \tfrac{M}{2}\sin\theta\,d\theta$.)

<details>
<summary>Odpowiedź</summary>

$I = \displaystyle\int_0^\pi R^2\sin^2\theta\cdot\frac{M}{2}\sin\theta\,d\theta = \frac{MR^2}{2}\cdot\frac43 = \frac23MR^2$.
</details>

2. Korzystając z twierdzenia o osiach prostopadłych, wyznacz moment bezwładności tarczy względem jej średnicy.

<details>
<summary>Odpowiedź</summary>

$I_z = \tfrac12MR^2 = I_x + I_y = 2I_x \Rightarrow I_x = \tfrac14MR^2$.
</details>

3. Płytka prostokątna $a\times b$ o masie $M$: wyprowadź $I = \tfrac1{12}M(a^2 + b^2)$ względem osi prostopadłej przez środek.

<details>
<summary>Odpowiedź</summary>

$I = \sigma\displaystyle\int_{-a/2}^{a/2}\!\int_{-b/2}^{b/2}(x^2 + y^2)\,dy\,dx = \sigma\left(\frac{a^3b}{12} + \frac{ab^3}{12}\right) = \frac{M(a^2 + b^2)}{12}$.
</details>

4. Pręt o długości $L$ ma gęstość rosnącą liniowo od zera na jednym końcu: $\lambda = \lambda_0x/L$. Oblicz jego masę i moment bezwładności względem osi przez lżejszy koniec. Wyraź $I$ przez $M$.

<details>
<summary>Odpowiedź</summary>

$M = \lambda_0L/2$, $I = \displaystyle\int_0^Lx^2\frac{\lambda_0x}{L}dx = \frac{\lambda_0L^3}{4} = \frac{ML^2}{2}$.
</details>

## Źródła

- OpenStax, *Fizyka dla szkół wyższych*, t. 1, rozdz. 10 — §10.4 (moment bezwładności i energia ruchu obrotowego) i §10.5 (obliczanie momentu bezwładności, twierdzenie Steinera).
- Halliday, Resnick, Walker, *Podstawy fizyki* — wyd. 2015: t. 1, §10.4–10.5; wyd. 1: t. 1, §11.6–11.7 (tabela momentów bezwładności).
