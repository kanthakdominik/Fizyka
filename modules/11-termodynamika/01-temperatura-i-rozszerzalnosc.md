# 11.01 — Temperatura i rozszerzalność cieplna

> **Moduł:** [11 — Termodynamika i teoria kinetyczna](README.md) · **Poziom:** 🟢 matura R · **Status:** ✅ pełny
>
> **Czytaj:**
>
> - OpenStax, *Fizyka dla szkół wyższych*, t. 2, rozdz. 1: [§1.1–1.3](https://openstax.org/books/fizyka-dla-szk%C3%B3%C5%82-wy%C5%BCszych-tom-2/pages/1-1-temperatura-i-rownowaga-termiczna) · [wstęp do rozdziału](https://openstax.org/books/fizyka-dla-szk%C3%B3%C5%82-wy%C5%BCszych-tom-2/pages/1-wstep)
> - Halliday, Resnick, Walker, *Podstawy fizyki*, wyd. 2015, t. 2: §18.1–18.3 (s. 244)
> - Halliday, Resnick, Walker, *Podstawy fizyki*, wyd. 1 (2003), t. 2: [§19.1–19.5, s. 188](https://home.agh.edu.pl/~czapli/Resnick_2.pdf#page=204) — PDF z serwera AGH

← (początek modułu) · [spis modułu](README.md) · [Ciepło, ciepło właściwe, przemiany fazowe, kalorymetria](02-cieplo-i-przemiany-fazowe.md) →

## Po co to jest

Temperatura to wielkość, którą mierzymy codziennie, a jej fizyczny sens ujawnia się dopiero w teorii kinetycznej (11.04): to miara średniej energii ruchu cząsteczek. Rozszerzalność cieplna zmusza inżynierów do zostawiania szczelin w torach i mostach, stosowania kompensatorów w rurociągach i doboru materiałów w zębach (wypełnienia) i elektronice. Na niej działają termometry cieczowe i termostaty bimetaliczne. Anomalia wody sprawia, że jeziora zamarzają od góry i ryby mogą przezimować.

## Teoria w pigułce

**Równowaga termiczna i zerowa zasada termodynamiki.** Dwa ciała w kontakcie termicznym wymieniają energię, aż osiągną równowagę. Jeśli ciała A i B są w równowadze z ciałem C, to są w równowadze ze sobą. Temperatura to wielkość, która jest wtedy równa, a termometr to ciało C.

**Skale temperatury:**
- Kelwin (skala bezwzględna, jednostka SI): $T = t_C + 273{,}15$; zero bezwzględne to $0\ \mathrm K$.
- Celsjusz: woda zamarza w 0°C i wrze w 100°C pod ciśnieniem normalnym.
- Fahrenheit: $t_F = \tfrac95t_C + 32$.

Różnica 1 K jest równa różnicy 1°C. Punkt potrójny wody to dokładnie 273,16 K. Od 2019 r. kelwin jest zdefiniowany przez stałą Boltzmanna (01.01).

**Rozszerzalność liniowa** ciał stałych przy niewielkich zmianach temperatury:

$$\Delta L = \alpha L_0\,\Delta T.$$

$\alpha$ to współczynnik rozszerzalności liniowej, rzędu $10^{-5}\ \mathrm{K^{-1}}$: stal ok. $12\cdot10^{-6}$, aluminium $23\cdot10^{-6}$, szkło kwarcowe zaledwie $0{,}5\cdot10^{-6}\ \mathrm{K^{-1}}$.

**Rozszerzalność objętościowa:** $\Delta V = \beta V_0\,\Delta T$. Dla ciał stałych izotropowych $\beta \approx 3\alpha$. Ciecze rozszerzają się zwykle mocniej (benzyna ok. $10^{-3}\ \mathrm{K^{-1}}$). Ciało ogrzane rozszerza się jak powiększenie fotograficzne, więc otwór w płytce też się powiększa.

**Anomalia wody.** Między 0°C a 4°C woda kurczy się przy ogrzewaniu, a największą gęstość ma w 4°C. Zimą woda o temperaturze 4°C opada na dno, a lód powstaje na powierzchni i izoluje resztę jeziora.

**Naprężenia termiczne.** Pręt, którego końce są unieruchomione, nie może się wydłużyć. Powstaje w nim naprężenie, jakby ściśnięto go o $\alpha L\Delta T$ (06.07):

$$\sigma = E\alpha\,\Delta T.$$

## Wzory i założenia

| Wzór | Znaczenie | Kiedy obowiązuje |
|---|---|---|
| $T[\mathrm K] = t[^\circ\mathrm C] + 273{,}15$ | przeliczenie skal | — |
| $t_F = \tfrac95t_C + 32$ | skala Fahrenheita | — |
| $\Delta L = \alpha L_0\Delta T$ | rozszerzalność liniowa | $\alpha\Delta T \ll 1$ |
| $\Delta V = \beta V_0\Delta T$, $\ \beta \approx 3\alpha$ | rozszerzalność objętościowa | ciało izotropowe |
| $\sigma = E\alpha\Delta T$ | naprężenie termiczne | końce unieruchomione, zakres sprężysty |

## Przykład rozwiązany

**Zadanie.** Stalowa szyna ma długość 25 m w temperaturze −10°C. (a) Jaką szczelinę trzeba zostawić między szynami, by w 40°C się zetknęły? (b) Jakie naprężenie powstałoby w szynie bez szczeliny ($\alpha = 12\cdot10^{-6}\ \mathrm{K^{-1}}$, $E = 200\ \mathrm{GPa}$)?

(a) $\Delta L = 12\cdot10^{-6}\cdot25\cdot50 = 0{,}015\ \mathrm m = 15\ \mathrm{mm}$.

(b) $\sigma = 200\cdot10^9\cdot12\cdot10^{-6}\cdot50 = 1{,}2\cdot10^8\ \mathrm{Pa} = 120\ \mathrm{MPa}$. To ok. połowa granicy plastyczności zwykłej stali, a siła ściskająca szynę o przekroju $75\ \mathrm{cm^2}$ wynosi ok. 900 kN. Szyna mogłaby się wyboczyć. Współczesne tory bezstykowe są spawane w dobranej temperaturze neutralnej i mocno przytwierdzone do podkładów, żeby przenosiły te naprężenia.

## Typowe pułapki

- **Kelwiny a stopnie przy różnicach.** Różnica temperatur w K i °C jest taka sama. Przy stosunkach (prawa gazowe, sprawność) trzeba używać kelwinów.
- **Otwór się zmniejsza.** Otwór w ogrzanej płytce się **powiększa**, tak jakby był z tego samego materiału.
- **$\beta = \alpha$.** Dla ciała stałego $\beta \approx 3\alpha$.
- **Woda zawsze rozszerza się przy ogrzewaniu.** Nie w zakresie 0–4°C.
- **Termometr wskazuje temperaturę ciała od razu.** Wskazuje własną temperaturę, więc potrzebuje czasu na osiągnięcie równowagi.

## Doświadczenie / symulacja

**Kulka i pierścień w kuchni.** Zakręcony słoik, którego nie da się otworzyć: polej pokrywkę gorącą wodą. Metalowa pokrywka rozszerza się bardziej niż szkło i puszcza.

**Pomiar rozszerzalności.** Długi drut lub rurka aluminiowa (ok. 1 m) oparta jednym końcem o przeszkodę, drugim o igłę z przyklejoną wskazówką ze słomki. Polewanie gorącą wodą obraca wskazówkę. Z kąta obrotu i promienia igły oblicz $\Delta L$ i wyznacz $\alpha$.

**Python:** gęstość wody w pobliżu 4°C (przybliżenie wielomianowe) i rozszerzalność szyny.

```python
import numpy as np
import matplotlib.pyplot as plt

t = np.linspace(0, 20, 200)
# przybliżenie gęstości wody (kg/m³) w zakresie 0–20 °C
rho = 999.84 + 0.0679*t - 0.00908*t**2 + 1.0e-4*t**3
print(f"maksimum gęstości w t = {t[np.argmax(rho)]:.1f} °C")

alpha, L0, E = 12e-6, 25.0, 200e9
for dT in (20, 50):
    print(f"ΔT = {dT} K: ΔL = {alpha*L0*dT*1000:.1f} mm, σ = {E*alpha*dT/1e6:.0f} MPa")
plt.plot(t, rho); plt.xlabel("t [°C]"); plt.ylabel("ρ [kg/m³]"); plt.title("anomalia wody"); plt.grid(True); plt.show()
```

## Zadania

### A. Poziom maturalny

1. Przelicz 37°C na kelwiny i stopnie Fahrenheita. W jakiej temperaturze skale Celsjusza i Fahrenheita wskazują tę samą liczbę?

<details>
<summary>Odpowiedź</summary>

310,15 K i 98,6°F. Liczby są równe w −40°.
</details>

2. Aluminiowy pręt ma 2 m długości w 20°C. O ile wydłuży się po ogrzaniu do 120°C ($\alpha = 23\cdot10^{-6}\ \mathrm{K^{-1}}$)?

<details>
<summary>Odpowiedź</summary>

$\Delta L = 23\cdot10^{-6}\cdot2\cdot100 = 4{,}6\ \mathrm{mm}$.
</details>

3. Bak samochodu o pojemności 50 L zatankowano do pełna zimną benzyną. O ile wzrośnie objętość benzyny, gdy ogrzeje się o 20 K ($\beta = 9{,}5\cdot10^{-4}\ \mathrm{K^{-1}}$)? Pomiń rozszerzalność baku.

<details>
<summary>Odpowiedź</summary>

$\Delta V \approx 0{,}95\ \mathrm L$, czyli prawie litr może się wylać.
</details>

4. Stalowy pierścień ma otwór o średnicy 2,000 cm. O ile zwiększy się średnica otworu po ogrzaniu o 100 K?

<details>
<summary>Odpowiedź</summary>

$\Delta d = \alpha d\Delta T = 12\cdot10^{-6}\cdot2\cdot100 = 0{,}0024\ \mathrm{cm}$, czyli o 24 μm (otwór się powiększa).
</details>

### B. Poziom akademicki _(opcjonalnie — rozszerzenie z rachunkiem)_

1. Zegar wahadłowy z prętem stalowym ($\alpha = 12\cdot10^{-6}\ \mathrm{K^{-1}}$) chodzi dokładnie w 20°C. Ile sekund na dobę spóźnia się w 30°C? Użyj różniczki: $\dfrac{dT}{T} = \dfrac12\dfrac{dL}{L}$.

<details>
<summary>Odpowiedź</summary>

$\dfrac{\Delta T}{T} = \dfrac12\alpha\Delta t = 6\cdot10^{-5}$, czyli $6\cdot10^{-5}\cdot86\,400 \approx 5{,}2\ \mathrm s$ na dobę.
</details>

2. Pokaż, że dla sześcianu $\beta \approx 3\alpha$, rozwijając $(1 + \alpha\Delta T)^3$.

<details>
<summary>Odpowiedź</summary>

$V = L_0^3(1 + \alpha\Delta T)^3 = V_0(1 + 3\alpha\Delta T + 3\alpha^2\Delta T^2 + \dots)$. Wyrazy z $\alpha^2$ są pomijalne, bo $\alpha\Delta T \sim 10^{-3}$.
</details>

3. Współczynnik rozszerzalności zależy od temperatury: $\alpha(T)$. Zapisz długość pręta jako całkę i pokaż, że dla stałego $\alpha$ wynosi ona $L_0e^{\alpha\Delta T} \approx L_0(1 + \alpha\Delta T)$.

<details>
<summary>Odpowiedź</summary>

$\dfrac{dL}{L} = \alpha(T)\,dT \Rightarrow L = L_0\exp\int_{T_0}^{T}\alpha\,dT$. Dla stałego $\alpha$ wychodzi $L_0e^{\alpha\Delta T}$, a rozwinięcie $e^x \approx 1 + x$ daje wzór liniowy.
</details>

## Źródła

- OpenStax, *Fizyka dla szkół wyższych*, t. 2, rozdz. 1 — §1.1 (temperatura i równowaga termiczna), §1.2 (termometry i skale), §1.3 (rozszerzalność cieplna).
- Halliday, Resnick, Walker, *Podstawy fizyki* — wyd. 2015: t. 2, §18.1–18.3; wyd. 1: t. 2, §19.1–19.5.
