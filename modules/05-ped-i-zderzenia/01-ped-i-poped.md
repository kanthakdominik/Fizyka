# 05.01 — Pęd i popęd siły

> **Moduł:** [05 — Pęd, środek masy i zderzenia](README.md) · **Poziom:** 🟢 matura R · **Status:** ✅ pełny
>
> **Czytaj:**
>
> - OpenStax, *Fizyka dla szkół wyższych*, t. 1, rozdz. 9: [§9.1–9.2](https://openstax.org/books/fizyka-dla-szk%C3%B3%C5%82-wy%C5%BCszych-tom-1/pages/9-1-ped) · [wstęp do rozdziału](https://openstax.org/books/fizyka-dla-szk%C3%B3%C5%82-wy%C5%BCszych-tom-1/pages/9-wstep)
> - Halliday, Resnick, Walker, *Podstawy fizyki*, wyd. 2015, t. 1: §9.3–9.4 (s. 283)
> - Halliday, Resnick, Walker, *Podstawy fizyki*, wyd. 1 (2003), t. 1: [§9.4, s. 213](https://home.agh.edu.pl/~czapli/Resnick_1.pdf#page=225), [§10.1–10.2, s. 234](https://home.agh.edu.pl/~czapli/Resnick_1.pdf#page=246) — PDF z serwera AGH

← (początek modułu) · [spis modułu](README.md) · [Zasada zachowania pędu](02-zasada-zachowania-pedu.md) →

## Po co to jest

Energia mówi, ile pracy potrzeba, żeby zatrzymać ciało; pęd mówi, jak długo i jak mocno trzeba na nie działać. Dlatego pęd i popęd tłumaczą, po co są poduszki powietrzne, kaski, strefy zgniotu i miękkie lądowanie na ugiętych nogach. Są też podstawą zasady zachowania pędu (05.02), dzięki której rozwiązujemy zderzenia i ruch rakiety.

## Teoria w pigułce

**Pęd** ciała to iloczyn masy i prędkości — wektor o kierunku prędkości:

$$\vec{p} = m\vec{v}, \qquad [p] = \mathrm{kg\cdot m/s}.$$

**II zasada dynamiki w postaci pędowej:**

$$\vec{F}_{\text{wyp}} = \frac{d\vec{p}}{dt}.$$

To ogólniejsza postać niż $\vec{F} = m\vec{a}$ — obowiązuje także wtedy, gdy masa układu się zmienia (05.05), i w teorii względności (19).

**Popęd siły** to iloczyn siły i czasu jej działania (dla siły zmiennej — całka):

$$\vec{J} = \vec{F}\Delta t, \qquad \vec{J} = \int_{t_1}^{t_2}\vec{F}\,dt.$$

Graficznie: pole pod wykresem $F(t)$. Jednostka $\mathrm{N\cdot s} = \mathrm{kg\cdot m/s}$.

**Twierdzenie o popędzie i pędzie:**

$$\vec{J} = \Delta\vec{p} = m\vec{v}_2 - m\vec{v}_1.$$

**Dlaczego miękkie lądowanie pomaga.** Zmiana pędu przy zatrzymaniu jest ustalona ($\Delta p = mv$). Średnia siła to $\bar{F} = \Delta p/\Delta t$ — wydłużając czas zatrzymania (poduszka, strefa zgniotu, ugięte kolana), zmniejszamy siłę.

**Pęd a energia.** $E_k = \dfrac{p^2}{2m}$. Dwa ciała o tym samym pędzie mają różne energie: lżejsze ma większą.

## Wzory i założenia

| Wzór | Znaczenie | Kiedy obowiązuje |
|---|---|---|
| $\vec{p} = m\vec{v}$ | pęd | $v \ll c$ |
| $\vec{F} = d\vec{p}/dt$ | II zasada dynamiki | układ inercjalny |
| $\vec{J} = \int\vec{F}\,dt = \Delta\vec{p}$ | popęd siły | — |
| $\bar{F} = \Delta p/\Delta t$ | średnia siła w czasie zderzenia | — |
| $E_k = p^2/(2m)$ | związek energii i pędu | $v \ll c$ |
| $F = \mu v$ | siła strumienia masy zatrzymywanej na przeszkodzie | $\mu$ — masa na sekundę, $v$ — prędkość strumienia |

## Przykład rozwiązany

**Zadanie 1.** Piłkarz kopie spoczywającą piłkę o masie 0,45 kg, nadając jej prędkość 25 m/s. Kontakt trwa 8 ms. Oblicz średnią siłę uderzenia.

$\Delta p = 0{,}45\cdot25 = 11{,}25\ \mathrm{kg\cdot m/s}$, $\bar{F} = 11{,}25/0{,}008 \approx 1{,}4\ \mathrm{kN}$ — ponad 300 razy więcej niż ciężar piłki.

**Zadanie 2.** Piłka tenisowa o masie 58 g uderza w ścianę z prędkością 30 m/s i odbija się z prędkością 25 m/s. Oblicz zmianę pędu.

Oś w stronę ściany: $v_1 = +30$, $v_2 = -25\ \mathrm{m/s}$. $\Delta p = 0{,}058\cdot(-25 - 30) \approx -3{,}19\ \mathrm{kg\cdot m/s}$. Zmiana pędu jest **większa**, niż gdyby piłka się zatrzymała — odbicie wymaga większego popędu.

### Wersja z rachunkiem różniczkowym i całkowym

**Zadanie.** Siła uderzenia kija w piłkę narasta i maleje parabolicznie: $F(t) = at(T - t)$ dla $0 \le t \le T$, gdzie $T = 2\ \mathrm{ms}$, a największa siła wynosi 3 kN. Oblicz popęd i prędkość piłki o masie 0,16 kg (spoczywającej przed uderzeniem).

Największa siła w $t = T/2$: $F_{\max} = aT^2/4 \Rightarrow a = 4F_{\max}/T^2$.

$$J = \int_0^Tat(T - t)\,dt = \frac{aT^3}{6} = \frac{2}{3}F_{\max}T = \frac23\cdot3000\cdot0{,}002 = 4\ \mathrm{N\cdot s}.$$

$v = J/m = 25\ \mathrm{m/s}$. Średnia siła to $\tfrac23F_{\max} = 2\ \mathrm{kN}$.

## Typowe pułapki

- **Pęd jako skalar.** Przy odbiciu zmienia się zwrot prędkości; zmiana pędu to suma, a nie różnica wartości.
- **Mylenie pędu i energii.** Pęd jest wektorem proporcjonalnym do $v$, energia — skalarem proporcjonalnym do $v^2$.
- **„Miękkie lądowanie zmniejsza zmianę pędu.”** Zmiana pędu jest ta sama; zmniejsza się siła, bo rośnie czas.
- **Popęd siły ciężkości w krótkim zderzeniu.** Zwykle pomijalny wobec ogromnej siły uderzenia, ale przy dłuższym czasie trzeba go uwzględnić.

## Doświadczenie / symulacja

**Jajko i prześcieradło.** Klasyczny pokaz: surowe jajko rzucone w napięte prześcieradło nie pęka, bo zatrzymuje się w długim czasie. (Wykonuj nad miską.)

**Pomiar siły uderzenia.** Upuść telefon owinięty ręcznikiem z niewielkiej wysokości (5–10 cm) na poduszkę, nagrywając przyspieszenie w phyphox (*Acceleration (without g)*, wysoka częstotliwość próbkowania). Zmierz czas trwania hamowania i największe przyspieszenie; porównaj z upadkiem na twardszą powierzchnię (gruby koc). **Nie upuszczaj telefonu na twarde podłoże.**

**Python:** ta sama zmiana pędu, różne czasy zatrzymania — siła uderzenia samochodu przy zderzeniu i hamowaniu.

```python
import numpy as np
import matplotlib.pyplot as plt

m, v = 1200.0, 20.0                      # samochód 1200 kg, 72 km/h
dt = np.logspace(-2, 1, 200)             # czas zatrzymania od 10 ms do 10 s
F = m*v/dt
for t in (0.05, 0.1, 0.5, 4.0):
    print(f"Δt = {t:5.2f} s: średnia siła {m*v/t/1000:8.1f} kN, czyli {m*v/t/(m*9.81):6.1f} × ciężar")
plt.loglog(dt, F/1000); plt.xlabel("czas zatrzymania [s]"); plt.ylabel("średnia siła [kN]")
plt.grid(True, which="both"); plt.show()
```

## Zadania

### A. Poziom maturalny

1. Samochód o masie 1200 kg jadący z prędkością 20 m/s zatrzymuje się a) przy zderzeniu w ciągu 0,1 s, b) przy hamowaniu w ciągu 4 s. Oblicz średnią siłę w obu przypadkach.

<details>
<summary>Odpowiedź</summary>

a) $240\ \mathrm{kN}$; b) $6\ \mathrm{kN}$. Zmiana pędu jest ta sama.
</details>

2. Piłka o masie 0,15 kg spada z wysokości 1,25 m i odbija się na wysokość 0,8 m. Oblicz zmianę pędu przy odbiciu.

<details>
<summary>Odpowiedź</summary>

$v_1 \approx 4{,}95\ \mathrm{m/s}$ w dół, $v_2 \approx 3{,}96\ \mathrm{m/s}$ w górę; $\Delta p = 0{,}15\cdot8{,}91 \approx 1{,}34\ \mathrm{kg\cdot m/s}$ w górę.
</details>

3. Wykres siły uderzenia w piłkę jest trójkątem o czasie trwania 0,01 s i wartości maksymalnej 1000 N. Jaką prędkość uzyska spoczywająca piłka o masie 0,5 kg?

<details>
<summary>Odpowiedź</summary>

$J = \tfrac12\cdot0{,}01\cdot1000 = 5\ \mathrm{N\cdot s}$; $v = 10\ \mathrm{m/s}$.
</details>

4. Wyjaśnij, dlaczego skacząc z wysokości, należy lądować na ugiętych nogach.

<details>
<summary>Odpowiedź</summary>

Ugięcie wydłuża czas hamowania; przy tej samej zmianie pędu średnia siła działająca na stawy jest mniejsza.
</details>

5. Dwa ciała mają ten sam pęd. Pierwsze ma masę 4 razy większą od drugiego. Jaki jest stosunek ich energii kinetycznych?

<details>
<summary>Odpowiedź</summary>

$E_k = p^2/(2m)$: cięższe ma 4 razy mniejszą energię.
</details>

### B. Poziom akademicki

1. Strumień wody z węża (2 L/s, prędkość 10 m/s) uderza prostopadle w ścianę i spływa po niej. Jaką siłą działa na ścianę?

<details>
<summary>Odpowiedź</summary>

$F = \mu v = \rho Qv = 1000\cdot0{,}002\cdot10 = 20\ \mathrm{N}$.
</details>

2. Na ciało o masie 2 kg działa siła $F(t) = 4 - t$ (N, s) przez 6 s. Ciało początkowo spoczywa. Oblicz końcową prędkość i największą prędkość w trakcie ruchu.

<details>
<summary>Odpowiedź</summary>

$J(t) = 4t - t^2/2$; $J(6) = 6\ \mathrm{N\cdot s}$, $v = 3\ \mathrm{m/s}$. Największa prędkość, gdy $F = 0$ ($t = 4$): $J = 8$, $v_{\max} = 4\ \mathrm{m/s}$.
</details>

3. Grad o masie łącznej $0{,}5\ \mathrm{kg/s}$ na metr kwadratowy spada pionowo z prędkością 15 m/s i odbija się od dachu z prędkością 5 m/s. Oblicz ciśnienie wywierane na dach (poza ciężarem gradu).

<details>
<summary>Odpowiedź</summary>

$p = \mu(v_1 + v_2) = 0{,}5\cdot20 = 10\ \mathrm{Pa}$.
</details>

## Źródła

- OpenStax, *Fizyka dla szkół wyższych*, t. 1, rozdz. 9 — §9.1 (pęd) i §9.2 (popęd siły i zderzenia).
- Halliday, Resnick, Walker, *Podstawy fizyki* — wyd. 2015: t. 1, §9.3–9.4; wyd. 1: t. 1, §9.4 i §10.1–10.2.
