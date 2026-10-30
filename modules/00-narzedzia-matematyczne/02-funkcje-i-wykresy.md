# 00.02 — Funkcje i wykresy w fizyce, linearyzacja

> **Moduł:** [00 — Narzędzia matematyczne fizyka](README.md) · **Poziom:** 🟢 matura R · **Status:** ✅ pełny
>
> **Czytaj:**
>
> - OpenStax, *Fizyka dla szkół wyższych*, t. 1, rozdz. 3: [§3.1–3.4](https://openstax.org/books/fizyka-dla-szk%C3%B3%C5%82-wy%C5%BCszych-tom-1/pages/3-1-polozenie-przemieszczenie-predkosc-srednia) · [wstęp do rozdziału](https://openstax.org/books/fizyka-dla-szk%C3%B3%C5%82-wy%C5%BCszych-tom-1/pages/3-wstep)
> - Halliday, Resnick, Walker, *Podstawy fizyki*, wyd. 2015, t. 1: §2.1–2.4 (s. 16)
> - Halliday, Resnick, Walker, *Podstawy fizyki*, wyd. 1 (2003), t. 1: [§2.2–2.5, s. 14](https://home.agh.edu.pl/~czapli/Resnick_1.pdf#page=26) — PDF z serwera AGH

← [Wektory: składowe, iloczyn skalarny i wektorowy](01-wektory.md) · [spis modułu](README.md) · [Pochodna jako szybkość zmian](03-pochodna.md) →

## Po co to jest

Prawa fizyki to zależności między wielkościami, a wykres jest najszybszym sposobem, żeby je zobaczyć i sprawdzić. Na maturze rozszerzonej co roku pojawia się zadanie, w którym trzeba narysować wykres z danych pomiarowych, dobrać zmienne tak, żeby wyszła prosta, i odczytać z niej stałą fizyczną. Ta sama umiejętność wraca w każdym doświadczeniu w module 01 i przy dopasowaniu modeli w module 25.

## Teoria w pigułce

**Rodziny funkcji, które spotkasz najczęściej:**

| Zależność | Postać | Przykład fizyczny |
|---|---|---|
| liniowa | $y = ax + b$ | prędkość w ruchu jednostajnie przyspieszonym $v = v_0 + at$ |
| kwadratowa | $y = ax^2 + bx + c$ | położenie $x = x_0 + v_0t + \tfrac12at^2$, energia kinetyczna $E = \tfrac12mv^2$ |
| odwrotna | $y = a/x$ | prawo Boyle'a–Mariotte'a $p = C/V$ |
| odwrotność kwadratu | $y = a/x^2$ | siła grawitacji i Coulomba, natężenie światła z punktowego źródła |
| pierwiastkowa | $y = a\sqrt{x}$ | okres wahadła $T = 2\pi\sqrt{l/g}$ |
| wykładnicza | $y = y_0e^{-x/\tau}$ | rozpad promieniotwórczy, rozładowanie kondensatora |
| trygonometryczna | $y = A\sin(\omega t + \varphi)$ | drgania, prąd przemienny |
| logarytmiczna | $y = a\log_{10}(x/x_0)$ | poziom natężenia dźwięku w decybelach |

**Co czytamy z wykresu.**
- **Nachylenie** (współczynnik kierunkowy) prostej $a = \Delta y/\Delta x$ ma jednostkę „jednostka $y$ / jednostka $x$” i zwykle jest wielkością fizyczną: nachylenie wykresu $x(t)$ to prędkość, wykresu $v(t)$ — przyspieszenie.
- **Punkt przecięcia z osią** $y$ (wyraz wolny $b$) to wartość początkowa, np. $v_0$.
- **Pole pod wykresem** to iloczyn wielkości z obu osi: pole pod $v(t)$ to droga, pole pod $F(x)$ — praca.

**Linearyzacja.** Prostą najłatwiej dopasować i ocenić „na oko”, więc zależność nieliniową przekształcamy tak, żeby stała się liniowa:

| Prawo | Co odkładamy | Nachylenie |
|---|---|---|
| $T = 2\pi\sqrt{l/g}$ | $T^2$ od $l$ | $4\pi^2/g$ |
| $p = C/V$ | $p$ od $1/V$ | $C$ |
| $F = k/r^2$ | $F$ od $1/r^2$ | $k$ |
| $N = N_0e^{-\lambda t}$ | $\ln N$ od $t$ | $-\lambda$ |
| $y = Ax^n$ (nieznane $n$) | $\ln y$ od $\ln x$ | $n$ |

Gdy z przekształconego wykresu wychodzi prosta, to potwierdza model. Gdy punkty układają się w łuk, model jest zły albo coś jest nie tak z pomiarem.

## Wzory i założenia

| Wzór | Znaczenie | Kiedy obowiązuje |
|---|---|---|
| $a = \dfrac{y_2 - y_1}{x_2 - x_1}$ | nachylenie prostej | punkty bierz **z narysowanej prostej**, daleko od siebie, a nie z tabeli pomiarów |
| $\ln(e^x) = x$, $\ln(ab) = \ln a + \ln b$, $\ln(a^n) = n\ln a$ | własności logarytmu | $a, b > 0$ |
| $e^{-\lambda T_{1/2}} = \tfrac12 \Rightarrow T_{1/2} = \dfrac{\ln 2}{\lambda}$ | czas połowicznego zaniku | zanik wykładniczy |
| $L = 10\log_{10}\dfrac{I}{I_0}\ \mathrm{dB}$ | poziom natężenia dźwięku | $I_0 = 10^{-12}\ \mathrm{W/m^2}$ |

## Przykład rozwiązany

**Zadanie.** Zmierzono okres wahadła $T$ dla kilku długości nici $l$:

| $l$ [m] | 0,20 | 0,40 | 0,60 | 0,80 | 1,00 |
|---|---|---|---|---|---|
| $T$ [s] | 0,90 | 1,27 | 1,55 | 1,80 | 2,01 |

Wyznacz przyspieszenie ziemskie $g$.

**Model.** Dla małych wychyleń $T = 2\pi\sqrt{l/g}$, czyli $T^2 = \dfrac{4\pi^2}{g}\,l$. Wykres $T^2(l)$ powinien być prostą przez początek układu.

**Linearyzacja.** Liczymy $T^2$ [s²]: 0,81; 1,61; 2,40; 3,24; 4,04. Punkty leżą na prostej (sprawdź na papierze milimetrowym albo w Pythonie poniżej).

**Nachylenie.** Z dwóch skrajnych punktów prostej: $a = \dfrac{4{,}04 - 0{,}81}{1{,}00 - 0{,}20}\ \mathrm{s^2/m} \approx 4{,}04\ \mathrm{s^2/m}$.

**Wynik.** $g = \dfrac{4\pi^2}{a} \approx \dfrac{39{,}5}{4{,}04}\ \mathrm{m/s^2} \approx 9{,}8\ \mathrm{m/s^2}$.

**Sprawdzenie.** Jednostka: $\mathrm{1/(s^2/m)} = \mathrm{m/s^2}$. Wynik bliski tablicowym $9{,}81\ \mathrm{m/s^2}$.

## Typowe pułapki

- **Nachylenie z dwóch punktów pomiarowych zamiast z prostej.** Rozrzut pojedynczych punktów przenosi się wtedy wprost na wynik. Najpierw narysuj prostą najlepiej pasującą, potem bierz z niej dwa odległe punkty.
- **Brak jednostek na osiach i przy nachyleniu.** Nachylenie bez jednostki to tylko liczba — a ta liczba jest wynikiem doświadczenia.
- **Odczytywanie wartości z „kratek” zamiast ze skali.** Sprawdź, ile wynosi jedna działka na każdej osi.
- **Logarytm wielkości z jednostką.** $\ln N$ ma sens dla liczby bezwymiarowej; dla napięcia pisz $\ln(U/1\ \mathrm{V})$ albo $\ln(U/U_0)$.
- **Prosta wymuszona przez zero.** Jeśli model przewiduje $b = 0$, a dopasowanie daje wyraźnie $b \neq 0$, to jest informacja (błąd systematyczny, np. źle zmierzona długość wahadła), a nie powód do „poprawienia” danych.

## Doświadczenie / symulacja

**Doświadczenie z telefonem.** Zawieś telefon na sznurku jako wahadło, uruchom w phyphox eksperyment *Pendulum* i zmierz okres dla 5 długości sznurka od 0,3 do 1,2 m (długość mierz do środka telefonu). Zrób wykres $T^2(l)$ i wyznacz $g$ jak w przykładzie.

**Python:** linearyzacja dwóch zależności — wahadła i zaniku wykładniczego.

```python
import numpy as np
import matplotlib.pyplot as plt

rng = np.random.default_rng(1)

# Wahadło: T = 2π√(l/g) z szumem pomiarowym
g_true = 9.81
l = np.array([0.2, 0.4, 0.6, 0.8, 1.0])
T = 2 * np.pi * np.sqrt(l / g_true) + rng.normal(0, 0.01, l.size)
a, b = np.polyfit(l, T**2, 1)          # prosta T² = a·l + b
print(f"nachylenie = {a:.3f} s²/m, wyraz wolny = {b:.3f} s², g = {4*np.pi**2/a:.2f} m/s²")

# Zanik wykładniczy: U = U0·exp(-t/τ) → ln U jest liniowe w t
tau_true = 2.0
t = np.linspace(0, 6, 13)
U = 12 * np.exp(-t / tau_true) * (1 + rng.normal(0, 0.02, t.size))
k, c = np.polyfit(t, np.log(U), 1)
print(f"τ = {-1/k:.2f} s, U0 = {np.exp(c):.2f} V")

fig, ax = plt.subplots(1, 2, figsize=(9, 3.5))
ax[0].plot(l, T**2, "o"); ax[0].plot(l, a*l + b, "-")
ax[0].set_xlabel("l [m]"); ax[0].set_ylabel("T² [s²]"); ax[0].grid(True)
ax[1].semilogy(t, U, "o"); ax[1].set_xlabel("t [s]"); ax[1].set_ylabel("U [V] (skala log)"); ax[1].grid(True)
plt.tight_layout(); plt.show()
```

## Zadania

### A. Poziom maturalny

1. Wykres prędkości od czasu jest prostą przechodzącą przez punkty $(0;\ 2\ \mathrm{m/s})$ i $(4\ \mathrm{s};\ 10\ \mathrm{m/s})$. Zapisz wzór $v(t)$, podaj przyspieszenie i oblicz drogę przebytą w ciągu 4 s.

<details>
<summary>Odpowiedź</summary>

$v = 2 + 2t$ (w m/s), $a = 2\ \mathrm{m/s^2}$, droga = pole trapezu $= \tfrac{2+10}{2}\cdot4 = 24\ \mathrm{m}$.
</details>

2. W stałej temperaturze iloczyn ciśnienia i objętości gazu jest stały. Jakie wielkości należy odłożyć na osiach, żeby otrzymać prostą? Co oznacza jej nachylenie?

<details>
<summary>Odpowiedź</summary>

$p$ od $1/V$; nachylenie to stała $pV$ (równa $nRT$).
</details>

3. Natężenie światła z punktowego źródła maleje z kwadratem odległości. Ile razy zmaleje natężenie, gdy odległość od źródła wzrośnie trzykrotnie?

<details>
<summary>Odpowiedź</summary>

9 razy.
</details>

4. Liczba jąder izotopu maleje o połowę co 8 dni. Na początku było $800$ (w jednostkach umownych). Ile zostanie po 24 dniach? Jaki wykres będzie prostą?

<details>
<summary>Odpowiedź</summary>

$800\cdot(1/2)^3 = 100$. Prostą jest wykres $\ln N$ od $t$.
</details>

5. Poziom natężenia dźwięku wzrósł z 60 dB do 80 dB. Ile razy wzrosło natężenie?

<details>
<summary>Odpowiedź</summary>

$10^{(80-60)/10} = 100$ razy.
</details>

### B. Poziom akademicki _(opcjonalnie — rozszerzenie z rachunkiem)_

1. Zmierzono $y = 3$ dla $x = 1$ oraz $y = 300$ dla $x = 10$. Zakładając $y = Ax^n$, wyznacz $A$ i $n$ z wykresu $\log_{10} y$ od $\log_{10} x$.

<details>
<summary>Odpowiedź</summary>

Nachylenie $n = \dfrac{\log 300 - \log 3}{\log 10 - \log 1} = 2$, $A = 3$.
</details>

2. Napięcie na rozładowującym się kondensatorze wynosi $12\ \mathrm{V}$ w chwili $t = 0$ i $4{,}41\ \mathrm{V}$ po 2 s. Zakładając $U = U_0e^{-t/\tau}$, oblicz stałą czasową $\tau$ i czas, po którym napięcie spadnie do 1 V.

<details>
<summary>Odpowiedź</summary>

$\tau = 2/\ln(12/4{,}41) \approx 2{,}0\ \mathrm{s}$; $t = \tau\ln 12 \approx 5{,}0\ \mathrm{s}$.
</details>

3. Uzasadnij, że dla $y = ax^2$ nachylenie wykresu $y(x)$ w punkcie $x$ wynosi $2ax$, korzystając z ilorazu różnicowego $\dfrac{a(x+h)^2 - ax^2}{h}$ przy $h \to 0$.

<details>
<summary>Odpowiedź</summary>

Iloraz to $\dfrac{a(2xh + h^2)}{h} = 2ax + ah \to 2ax$. To jest pochodna — temat 03.
</details>

## Źródła

- OpenStax, *Fizyka dla szkół wyższych*, t. 1, rozdz. 1 — §1.7 (rozwiązywanie zadań) oraz przykłady wykresów w §3.1–3.4.
- Halliday, Resnick, Walker, *Podstawy fizyki*, wyd. 2015, t. 1, rozdz. 2 — §2.1–2.4: odczytywanie prędkości i przyspieszenia z wykresów.
- CKE, [Informator o egzaminie maturalnym z fizyki](https://cke.gov.pl/images/_EGZAMIN_MATURALNY_OD_2023/Informatory/2024/Informator_EM2024_fizyka.pdf) — przykładowe zadania z opracowaniem wyników pomiarów na wykresie.
