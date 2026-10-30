# 16.03 — Energia, wektor Poyntinga i ciśnienie promieniowania

> **Moduł:** [16 — Równania Maxwella i fale elektromagnetyczne](README.md) · **Poziom:** 🔵 studia · **Status:** ✅ pełny
>
> **Czytaj:**
>
> - OpenStax, *Fizyka dla szkół wyższych*, t. 2, rozdz. 16: [§16.3–16.4](https://openstax.org/books/fizyka-dla-szk%C3%B3%C5%82-wy%C5%BCszych-tom-2/pages/16-3-energia-niesiona-przez-fale-elektromagnetyczne) · [wstęp do rozdziału](https://openstax.org/books/fizyka-dla-szk%C3%B3%C5%82-wy%C5%BCszych-tom-2/pages/16-wstep)
> - Halliday, Resnick, Walker, *Podstawy fizyki*, wyd. 2015, t. 4: §33.2–33.3 (s. 11)
> - Halliday, Resnick, Walker, *Podstawy fizyki*, wyd. 1 (2003), t. 4: [§34.4–34.5, s. 11](https://home.agh.edu.pl/~czapli/Resnick_4.pdf#page=26) — PDF z serwera AGH

← [Płaska fala elektromagnetyczna](02-fala-elektromagnetyczna.md) · [spis modułu](README.md) · [Widmo fal elektromagnetycznych](04-widmo-fal-em.md) →

## Po co to jest

Fala elektromagnetyczna niesie energię: Słońce ogrzewa Ziemię i zasila panele fotowoltaiczne, a mikrofalówka grzeje jedzenie. Niesie też pęd, więc wywiera ciśnienie na oświetlane powierzchnie. Ciśnienie promieniowania odpycha ogony komet od Słońca, napędza żagle słoneczne i pozwala laserowym „pęsetom optycznym” przesuwać pojedyncze komórki (Nagroda Nobla 2018). Natężenie fali decyduje o normach bezpieczeństwa dla anten i telefonów.

## Teoria w pigułce

**Gęstość energii.** Pole elektryczne i magnetyczne mają gęstości energii $\tfrac12\varepsilon_0E^2$ (12.06) i $B^2/(2\mu_0)$ (15.04). W fali $B = E/c$, więc obie części są **równe**:

$$w = \frac12\varepsilon_0E^2 + \frac{B^2}{2\mu_0} = \varepsilon_0E^2.$$

**Wektor Poyntinga** opisuje strumień energii (moc na jednostkę powierzchni) i wskazuje kierunek jej przepływu:

$$\vec S = \frac1{\mu_0}\vec E\times\vec B, \qquad S = \frac{EB}{\mu_0} = \frac{E^2}{\mu_0c}.$$

**Natężenie** to średnia wartość $S$. Dla fali sinusoidalnej $\overline{\sin^2} = \tfrac12$:

$$I = \frac{E_0^2}{2\mu_0c} = \frac{c\varepsilon_0E_0^2}{2} = c\,\bar w.$$

Źródło punktowe o mocy $P$ daje $I = P/(4\pi r^2)$ (jak dźwięk, 10.05).

**Pęd i ciśnienie promieniowania.** Fala o energii $U$ niesie pęd $p = U/c$. Wynika to z równań Maxwella, a w języku fotonów z $p = E/c$ (20). Ciśnienie promieniowania padającego prostopadle:

$$p_{\text{rad}} = \frac Ic \ \text{(pochłanianie)}, \qquad p_{\text{rad}} = \frac{2I}{c} \ \text{(odbicie)}.$$

Dla światła słonecznego to zaledwie mikropaskale, ale w kosmosie, bez tarcia, takie ciśnienie potrafi rozpędzić żagiel. W gwiazdach ciśnienie promieniowania podtrzymuje warstwy zewnętrzne przed zapadnięciem.

## Wzory i założenia

| Wzór | Znaczenie | Kiedy obowiązuje |
|---|---|---|
| $w = \varepsilon_0E^2 = B^2/\mu_0$ | gęstość energii fali | fala w próżni |
| $\vec S = \vec E\times\vec B/\mu_0$ | wektor Poyntinga | — |
| $I = E_0^2/(2\mu_0c) = \tfrac12c\varepsilon_0E_0^2$ | natężenie | fala sinusoidalna |
| $I = P/(4\pi r^2)$ | źródło izotropowe | — |
| $p_{\text{rad}} = I/c$ / $2I/c$ | ciśnienie promieniowania | pochłanianie / odbicie, padanie prostopadłe |

## Przykład rozwiązany

**Zadanie.** Natężenie promieniowania słonecznego nad atmosferą wynosi 1361 W/m² (stała słoneczna). Oblicz amplitudy pól $E_0$ i $B_0$, ciśnienie promieniowania na powierzchnię czarną i lustrzaną oraz siłę na żagiel słoneczny o wymiarach 100 m × 100 m (lustro).

$E_0 = \sqrt{2\mu_0cI} \approx 1010\ \mathrm{V/m}$, $B_0 = E_0/c \approx 3{,}4\ \mu\mathrm T$.

$p = I/c \approx 4{,}5\ \mu\mathrm{Pa}$ (czarna), $9{,}1\ \mu\mathrm{Pa}$ (lustro).

Siła na żagiel: $9{,}1\cdot10^{-6}\cdot10^4 \approx 0{,}09\ \mathrm N$. Mało, ale działa bez przerwy i bez paliwa. Lekki żagiel (np. 100 kg) uzyska przyspieszenie ok. $10^{-3}\ \mathrm{m/s^2}$, czyli prędkość ok. 80 m/s po dobie.

### Wersja z rachunkiem różniczkowym i całkowym

**Zadanie.** Telefon emituje moc 1 W (w przybliżeniu izotropowo). Oblicz natężenie i skuteczne pole elektryczne w odległości 1 m. Następnie pokaż, że średnia gęstość energii fali sinusoidalnej wynosi $\tfrac12\varepsilon_0E_0^2$.

$I = \dfrac{1}{4\pi\cdot1^2} \approx 0{,}08\ \mathrm{W/m^2}$. $E_{\text{sk}} = \sqrt{\mu_0cI} \approx 5{,}5\ \mathrm{V/m}$. W bezpośrednim sąsiedztwie (głowa) model źródła punktowego przestaje działać, ale rząd wielkości pozostaje.

Średnia gęstość energii:

$$\bar w = \frac1T\int_0^T\varepsilon_0E_0^2\sin^2(kx - \omega t)\,dt = \frac12\varepsilon_0E_0^2,$$

a $I = c\bar w$, bo energia płynie z prędkością $c$.

## Typowe pułapki

- **Energia pola magnetycznego w fali jest pomijalna.** Jest dokładnie równa energii pola elektrycznego.
- **Natężenie $E_0^2/(\mu_0c)$.** To wartość chwilowa w maksimum. Średnia dla sinusoidy ma czynnik $\tfrac12$.
- **Ciśnienie światła lustra $= I/c$.** Odbicie zmienia pęd dwukrotnie: $2I/c$.
- **Światło nie ma pędu, bo nie ma masy.** Fala elektromagnetyczna (foton) ma pęd $E/c$ mimo zerowej masy spoczynkowej.

## Doświadczenie / symulacja

**Natężenie światła i panel.** Luksomierz w telefonie (phyphox, *Light*) i mały panel fotowoltaiczny z miernikiem. Zmierz natężenie oświetlenia słonecznego (luksy) i moc panelu (napięcie na znanym oporniku). Przyjmując ok. 110 lm/W dla światła słonecznego, przelicz luksy na W/m² i oszacuj sprawność panelu.

**Radiometr Crookesa** (obracający się wiatraczek w bańce) obraca się w świetle, ale w przeciwną stronę, niż przewiduje ciśnienie promieniowania. Za ruch odpowiadają efekty termiczne resztek gazu. Dobry przykład, jak łatwo pomylić zjawiska.

**Python:** pola, ciśnienie i przyspieszenie żagla słonecznego, a także zasięg sygnału.

```python
import numpy as np

mu0, eps0 = 4e-7*np.pi, 8.8541878128e-12
c = 1/np.sqrt(mu0*eps0)
I = 1361.0
E0 = np.sqrt(2*mu0*c*I)
print(f"Słońce: E0 = {E0:.0f} V/m, B0 = {E0/c*1e6:.2f} µT, w = {I/c*1e6:.2f} µJ/m³")
print(f"ciśnienie: czarna {I/c*1e6:.2f} µPa, lustro {2*I/c*1e6:.2f} µPa")
A, m = 1e4, 100.0
a = 2*I/c*A/m
print(f"żagiel 100×100 m, 100 kg: F = {2*I/c*A:.3f} N, a = {a:.2e} m/s², v po dobie = {a*86400:.0f} m/s")
for P, r in [(1, 1), (1, 100), (50e3, 10e3)]:
    Iv = P/(4*np.pi*r**2)
    print(f"P = {P:g} W, r = {r:g} m: I = {Iv:.2e} W/m², E_sk = {np.sqrt(mu0*c*Iv):.3g} V/m")
```

## Zadania

### A. Poziom maturalny _(opcjonalnie — rozgrzewka)_

1. Wskaźnik laserowy o mocy 1 mW daje plamkę o średnicy 1 mm. Oblicz natężenie i porównaj ze światłem słonecznym.

<details>
<summary>Odpowiedź</summary>

$I = 10^{-3}/(\pi\cdot0{,}0005^2) \approx 1270\ \mathrm{W/m^2}$, mniej więcej tyle co Słońce. Dlatego nie wolno patrzeć w wiązkę: soczewka oka skupia ją w maleńki punkt na siatkówce.
</details>

2. Jak zmienia się natężenie fali, gdy amplituda pola elektrycznego wzrośnie dwukrotnie?

<details>
<summary>Odpowiedź</summary>

Czterokrotnie ($I \propto E_0^2$).
</details>

### B. Poziom akademicki

1. Oblicz siłę ciśnienia promieniowania Słońca na Ziemię (pochłanianie, przekrój $\pi R_Z^2$) i porównaj z siłą grawitacji Słońca.

<details>
<summary>Odpowiedź</summary>

$F = \dfrac Ic\pi R_Z^2 \approx 5{,}8\cdot10^8\ \mathrm N$. Grawitacja to ok. $3{,}5\cdot10^{22}\ \mathrm N$, czyli $10^{14}$ razy więcej. Dla ciała stosunek rośnie, gdy maleje rozmiar ($\propto 1/r$), dlatego pył o rozmiarach mikrometrów jest wydmuchiwany z Układu Słonecznego.
</details>

2. Pokaż, że dla fali biegnącej w próżni wektor Poyntinga ma kierunek ruchu fali i wartość $S = cw$.

<details>
<summary>Odpowiedź</summary>

$\vec E\times\vec B$ wskazuje kierunek propagacji (16.02). $S = EB/\mu_0 = E^2/(\mu_0c) = \varepsilon_0cE^2 = cw$, bo $1/(\mu_0c) = \varepsilon_0c$.
</details>

3. Kulka o promieniu $r$ i gęstości $\rho$ w odległości Ziemi od Słońca pochłania światło. Przy jakim promieniu siła ciśnienia promieniowania równa się sile grawitacji Słońca? Przyjmij $\rho = 2000\ \mathrm{kg/m^3}$.

<details>
<summary>Odpowiedź</summary>

$\dfrac Ic\pi r^2 = \dfrac{GM_S}{d^2}\cdot\dfrac43\pi r^3\rho \Rightarrow r = \dfrac{3Id^2}{4cGM_S\rho}$. Ponieważ $I \propto 1/d^2$, wynik nie zależy od odległości: $r \approx 0{,}3\ \mu\mathrm m$.
</details>

## Źródła

- OpenStax, *Fizyka dla szkół wyższych*, t. 2, rozdz. 16 — §16.3 (energia niesiona przez fale elektromagnetyczne) i §16.4 (pęd i ciśnienie promieniowania).
- Halliday, Resnick, Walker, *Podstawy fizyki* — wyd. 2015: t. 4, §33.2–33.3; wyd. 1: t. 4, §34.4–34.5.
