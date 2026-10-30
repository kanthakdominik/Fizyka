# 18.03 — Interferencja na wielu szczelinach i siatka dyfrakcyjna

> **Moduł:** [18 — Optyka falowa](README.md) · **Poziom:** 🟢 matura R · **Status:** ✅ pełny
>
> **Czytaj:**
>
> - OpenStax, *Fizyka dla szkół wyższych*, t. 3, rozdz. 3: [§3.3 i §4.4](https://openstax.org/books/fizyka-dla-szk%C3%B3%C5%82-wy%C5%BCszych-tom-3/pages/3-3-interferencja-na-wielu-szczelinach) · [wstęp do rozdziału](https://openstax.org/books/fizyka-dla-szk%C3%B3%C5%82-wy%C5%BCszych-tom-3/pages/3-wstep)
> - Halliday, Resnick, Walker, *Podstawy fizyki*, wyd. 2015, t. 4: §36.5–36.6 (s. 162)
> - Halliday, Resnick, Walker, *Podstawy fizyki*, wyd. 1 (2003), t. 4: [§37.7–37.8, s. 127](https://home.agh.edu.pl/~czapli/Resnick_4.pdf#page=142) — PDF z serwera AGH

← [Doświadczenie Younga](02-doswiadczenie-younga.md) · [spis modułu](README.md) · [Interferencja w cienkich warstwach, interferometr Michelsona](04-cienkie-warstwy-i-michelson.md) →

## Po co to jest

Siatka dyfrakcyjna to tysiące równoległych szczelin lub rys. Rozszczepia światło na widmo dużo dokładniej niż pryzmat. Jest sercem spektrometrów, którymi astronomowie mierzą skład i prędkość gwiazd, chemicy identyfikują substancje, a telekomunikacja rozdziela kanały w światłowodach. Tęczowe barwy płyty CD i DVD, skrzydeł motyli czy hologramów na banknotach to też działanie siatek.

## Teoria w pigułce

**Siatka** ma $N$ szczelin odległych o $d$ (**stała siatki**). Siatka z 600 rysami na milimetr ma $d = 1/600\ \mathrm{mm} \approx 1{,}67\ \mu\mathrm m$. Fale z sąsiednich szczelin wzmacniają się, gdy różnica dróg to całkowita liczba długości fali:

$$d\sin\theta = m\lambda, \qquad m = 0, \pm1, \pm2, \dots$$

Warunek jest ten sam co dla dwóch szczelin (18.02), ale maksima są **bardzo wąskie i jasne**. Już niewielkie odejście od kąta $\theta_m$ sprawia, że fale z wielu szczelin się znoszą. Między maksimami głównymi jest $N - 1$ minimów.

**Rząd widma** $m$ jest ograniczony przez $\sin\theta \le 1$: $m_{\max} = \lfloor d/\lambda\rfloor$.

**Widmo.** Światło białe daje biały prążek zerowy i kolorowe widma po obu stronach. Czerwień jest odchylona najmocniej (odwrotnie niż w pryzmacie, 17.03). Widma wyższych rzędów mogą na siebie zachodzić.

**Zdolność rozdzielcza.** Dwie linie o długościach $\lambda$ i $\lambda + \Delta\lambda$ są rozróżnialne, gdy

$$R = \frac{\lambda}{\Delta\lambda} \le Nm.$$

Więcej oświetlonych rys i wyższy rząd dają lepszą rozdzielczość.

**Siatka odbiciowa** (rysy na lustrze, płyta CD) działa tak samo: w warunku jest odległość między ścieżkami. Na płycie CD wynosi ona 1,6 μm, na DVD 0,74 μm.

## Wzory i założenia

| Wzór | Znaczenie | Kiedy obowiązuje |
|---|---|---|
| $d\sin\theta = m\lambda$ | maksima główne | padanie prostopadłe |
| $m_{\max} = \lfloor d/\lambda\rfloor$ | najwyższy rząd | — |
| $R = \lambda/\Delta\lambda = Nm$ | zdolność rozdzielcza | $N$ — liczba oświetlonych rys |
| $d = 1/(\text{liczba rys na mm})$ | stała siatki | — |

## Przykład rozwiązany

**Zadanie 1.** Siatka ma 600 rys na milimetr. Pod jakimi kątami widać światło zielone 550 nm? Ile rzędów widma jest widocznych? Jak szerokie kątowo jest widmo pierwszego rzędu (400–700 nm)?

$d \approx 1{,}667\ \mu\mathrm m$. $\theta_1 = \arcsin(0{,}33) \approx 19{,}3^\circ$, $\theta_2 \approx 41{,}3^\circ$, $\theta_3 \approx 81{,}9^\circ$, czyli $m_{\max} = 3$.

Widmo pierwszego rzędu: od $\arcsin(0{,}24) \approx 13{,}9^\circ$ do $\arcsin(0{,}42) \approx 24{,}8^\circ$, ok. $11^\circ$. Pryzmat dawał ok. $1{,}7^\circ$ (17.03).

**Zadanie 2.** Ile rys musi być oświetlonych, żeby w pierwszym rzędzie rozdzielić żółty dublet sodu (589,0 nm i 589,6 nm)?

$R = 589{,}0/0{,}6 \approx 980$, więc $N \ge 980$ rys. Siatka 600 rys/mm wymaga oświetlenia ok. 1,6 mm.

## Typowe pułapki

- **$d$ to liczba rys na milimetr.** $d$ to odległość między rysami, odwrotność tej liczby.
- **Siatka rozszczepia jak pryzmat.** W siatce najmocniej odchylana jest czerwień, w pryzmacie fiolet.
- **Rzędów może być dowolnie dużo.** $\sin\theta \le 1$ ogranicza ich liczbę.
- **Więcej rys = szersze widmo.** Szerokość kątowa widma zależy od $d$. Więcej rys daje węższe i jaśniejsze linie, czyli lepszą rozdzielczość.

## Doświadczenie / symulacja

**Spektroskop z płyty CD.** W pudełku po herbacie zrób wąską szczelinę z dwóch żyletek, a po przeciwnej stronie pod kątem ok. $60^\circ$ przyklej kawałek płyty CD (bez etykiety). Oglądaj widma żarówki, świetlówki, lampy LED i nieba. Świetlówka daje jasne linie rtęci, LED ciągłe widmo z niebieskim pikiem.

**Pomiar ścieżek CD.** Skieruj laser prostopadle na płytę CD i zmierz na ekranie odległość plamki pierwszego rzędu od środka. Z $d\sin\theta = \lambda$ oblicz odstęp ścieżek. Powinno wyjść ok. 1,6 μm.

**Symulacja PhET:** *Interferencja fal* — zwiększaj liczbę szczelin (w wersjach z tą opcją) albo użyj symulacji siatki z innych źródeł.

**Python:** natężenie dla siatki z $N$ szczelin — maksima główne węższe wraz z $N$.

```python
import numpy as np
import matplotlib.pyplot as plt

lam, d = 550e-9, 1e-3/600
s = np.linspace(-0.45, 0.45, 20000)                  # sin θ
phi = np.pi*d*s/lam
for N in (2, 5, 20):
    with np.errstate(invalid="ignore", divide="ignore"):
        I = np.where(np.abs(np.sin(phi)) < 1e-9, 1.0, (np.sin(N*phi)/(N*np.sin(phi)))**2)
    plt.plot(s, I, label=f"N = {N}")
for m in (1, 2, 3):
    print(f"rząd {m}: θ = {np.degrees(np.arcsin(m*lam/d)):.1f}°")
print(f"rozdzielenie dubletu sodu wymaga N ≥ {589.0/0.6:.0f} rys")
plt.xlabel("sin θ"); plt.ylabel("I / I_max"); plt.legend(); plt.grid(True); plt.show()
```

## Zadania

### A. Poziom maturalny

1. Siatka ma 300 rys na milimetr. Pod jakim kątem widać pierwszy rząd światła czerwonego (650 nm)?

<details>
<summary>Odpowiedź</summary>

$d = 3{,}33\ \mu\mathrm m$, $\sin\theta = 0{,}195 \Rightarrow \theta \approx 11{,}2^\circ$.
</details>

2. Laser oświetla płytę CD (ścieżki co 1,6 μm). Plamka pierwszego rzędu jest pod kątem $24^\circ$. Jaka jest długość fali lasera?

<details>
<summary>Odpowiedź</summary>

$\lambda = d\sin\theta \approx 650\ \mathrm{nm}$.
</details>

3. Ile maksimów (łącznie z zerowym) da siatka o 500 rysach na milimetr dla światła 600 nm?

<details>
<summary>Odpowiedź</summary>

$d/\lambda = 3{,}33$, więc $m_{\max} = 3$ i maksimów jest $2\cdot3 + 1 = 7$.
</details>

### B. Poziom akademicki _(opcjonalnie — rozszerzenie z rachunkiem)_

1. Wyprowadź natężenie dla $N$ szczelin, sumując $N$ wskazów przesuniętych kolejno o fazę $\phi$: $I \propto \left(\dfrac{\sin(N\phi/2)}{\sin(\phi/2)}\right)^2$.

<details>
<summary>Odpowiedź</summary>

Suma szeregu geometrycznego $\sum_{k=0}^{N-1}e^{ik\phi} = \dfrac{e^{iN\phi} - 1}{e^{i\phi} - 1}$, moduł $\dfrac{\lvert\sin(N\phi/2)\rvert}{\lvert\sin(\phi/2)\rvert}$. Maksima główne dla $\phi = 2\pi m$, natężenie $N^2$.
</details>

2. Pokaż, że kątowa szerokość maksimum głównego (od maksimum do pierwszego minimum) wynosi $\Delta\theta \approx \dfrac{\lambda}{Nd\cos\theta}$, i wyprowadź z tego $R = Nm$.

<details>
<summary>Odpowiedź</summary>

Pierwsze minimum przy $N\phi/2 = \pi m N + \pi$, czyli zmiana różnicy dróg o $\lambda/N$: $d\cos\theta\,\Delta\theta = \lambda/N$. Kryterium Rayleigha: linia $\lambda + \Delta\lambda$ ma maksimum w minimum linii $\lambda$, a $d\cos\theta\,d\theta = m\,d\lambda$ daje $m\Delta\lambda = \lambda/N$, czyli $\lambda/\Delta\lambda = Nm$.
</details>

## Źródła

- OpenStax, *Fizyka dla szkół wyższych*, t. 3 — §3.3 (interferencja wielu szczelin) i §4.4 (siatki dyfrakcyjne).
- Halliday, Resnick, Walker, *Podstawy fizyki* — wyd. 2015: t. 4, §36.5–36.6; wyd. 1: t. 4, §37.7–37.8.
