# 10.01 — Fala biegnąca i jej opis matematyczny

> **Moduł:** [10 — Fale mechaniczne i akustyka](README.md) · **Poziom:** 🟢🔵 matura R + studia · **Status:** ✅ pełny
>
> **Czytaj:**
>
> - OpenStax, *Fizyka dla szkół wyższych*, t. 1, rozdz. 16: [§16.1–16.2](https://openstax.org/books/fizyka-dla-szk%C3%B3%C5%82-wy%C5%BCszych-tom-1/pages/16-1-fale-biegnace) · [wstęp do rozdziału](https://openstax.org/books/fizyka-dla-szk%C3%B3%C5%82-wy%C5%BCszych-tom-1/pages/16-wstep)
> - Halliday, Resnick, Walker, *Podstawy fizyki*, wyd. 2015, t. 2: §16.1 (s. 156)
> - Halliday, Resnick, Walker, *Podstawy fizyki*, wyd. 1 (2003), t. 2: [§17.1–17.5, s. 123](https://home.agh.edu.pl/~czapli/Resnick_2.pdf#page=139) — PDF z serwera AGH

← (początek modułu) · [spis modułu](README.md) · [Prędkość fali, energia i równanie falowe](02-predkosc-i-energia-fali.md) →

## Po co to jest

Fala przenosi energię i informację, a materia zostaje na miejscu. Kibice robiący „meksykańską falę” nie biegną wokół stadionu, a mimo to fala go okrąża. Ten sam opis matematyczny obejmuje fale na wodzie, dźwięk, fale sejsmiczne, światło i radio (16), a w mechanice kwantowej także cząstki (20). Umiejętność odczytania z wzoru $y(x, t)$ długości fali, prędkości i kierunku ruchu to podstawa całego działu.

## Teoria w pigułce

**Fala mechaniczna** to zaburzenie rozchodzące się w ośrodku sprężystym. Każdy element ośrodka drga wokół położenia równowagi i przekazuje ruch sąsiadom.

- **Fala poprzeczna**: drgania są prostopadłe do kierunku rozchodzenia się fali (lina, struna, fala S w skorupie Ziemi).
- **Fala podłużna**: drgania są wzdłuż kierunku rozchodzenia się fali, czyli zagęszczenia i rozrzedzenia (dźwięk w powietrzu, sprężyna, fala P).
- Fale na wodzie są mieszane: cząstki zakreślają okręgi.

**Parametry fali harmonicznej:**
- amplituda $A$;
- długość fali $\lambda$ (odległość między sąsiednimi grzbietami);
- okres $T$ i częstotliwość $f = 1/T$;
- liczba falowa $k = 2\pi/\lambda$ i częstość kołowa $\omega = 2\pi f$.

Fala przesuwa się o jedną długość fali w czasie jednego okresu:

$$v = \frac{\lambda}{T} = \lambda f = \frac{\omega}{k}.$$

**Funkcja falowa** fali harmonicznej biegnącej w kierunku $+x$:

$$y(x, t) = A\sin(kx - \omega t + \varphi).$$

Znak przy $\omega t$ mówi o kierunku. $(kx - \omega t)$ oznacza falę biegnącą w prawo (w stronę $+x$), a $(kx + \omega t)$ w lewo. Ogólnie każda funkcja postaci $f(x - vt)$ to kształt przesuwający się bez zmian w prawo z prędkością $v$.

**Prędkość fali a prędkość cząstek ośrodka** to dwie różne rzeczy:
- prędkość fali $v$ zależy od ośrodka (10.02);
- prędkość poprzeczna elementu struny $v_y = \partial y/\partial t$ zmienia się w czasie, a jej maksimum wynosi $A\omega$.

## Wzory i założenia

| Wzór | Znaczenie | Kiedy obowiązuje |
|---|---|---|
| $v = \lambda f = \omega/k$ | prędkość fali | fala harmoniczna |
| $k = 2\pi/\lambda$, $\ \omega = 2\pi f$ | liczba falowa, częstość | — |
| $y = A\sin(kx \mp \omega t + \varphi)$ | fala biegnąca w prawo / w lewo | fala harmoniczna |
| $v_y = \partial y/\partial t$, $\ v_{y,\max} = A\omega$ | prędkość elementu ośrodka | fala poprzeczna |
| $\dfrac{\partial^2y}{\partial t^2} = v^2\dfrac{\partial^2y}{\partial x^2}$ | równanie falowe | ośrodek liniowy, bez tłumienia (10.02) |

## Przykład rozwiązany

**Zadanie.** Fala na linie opisana jest wzorem $y(x, t) = 0{,}05\sin(\pi x - 4\pi t)$ (jednostki SI). Wyznacz amplitudę, długość fali, częstotliwość, prędkość i kierunek ruchu fali.

- $A = 5\ \mathrm{cm}$.
- $k = \pi\ \mathrm{rad/m}$, więc $\lambda = 2\pi/k = 2\ \mathrm{m}$.
- $\omega = 4\pi\ \mathrm{rad/s}$, więc $f = 2\ \mathrm{Hz}$ i $T = 0{,}5\ \mathrm{s}$.
- $v = \lambda f = \omega/k = 4\ \mathrm{m/s}$, w stronę $+x$ (znak minus przy $\omega t$).

### Wersja z rachunkiem różniczkowym i całkowym

**Zadanie.** Dla tej samej fali oblicz prędkość i przyspieszenie elementu liny w punkcie $x$. Sprawdź, że funkcja spełnia równanie falowe.

$$v_y = \frac{\partial y}{\partial t} = -0{,}05\cdot4\pi\cos(\pi x - 4\pi t), \qquad v_{y,\max} = 0{,}2\pi \approx 0{,}63\ \mathrm{m/s}.$$

$$a_y = \frac{\partial^2 y}{\partial t^2} = -(4\pi)^2y, \qquad \frac{\partial^2y}{\partial x^2} = -\pi^2y.$$

Stosunek wynosi $16 = v^2$. Równanie falowe jest spełnione z $v = 4\ \mathrm{m/s}$. Każdy element liny wykonuje ruch harmoniczny (09.01) o częstości $\omega$.

## Typowe pułapki

- **Cząstki ośrodka płyną z falą.** Drgają w miejscu; przemieszcza się tylko zaburzenie i energia.
- **Prędkość fali = $A\omega$.** To maksymalna prędkość elementu ośrodka, a nie prędkość fali.
- **Częstotliwość zmienia się przy przejściu do innego ośrodka.** Częstotliwość narzuca źródło i ona się nie zmienia. Zmieniają się prędkość i długość fali.
- **Mylenie $k$ z $\lambda$ i $\omega$ z $f$.** Z $\sin(\pi x)$ wynika $\lambda = 2\ \mathrm{m}$, a nie $\pi$.
- **Kierunek fali z $\sin(kx - \omega t)$.** Ten zapis oznacza ruch w stronę $+x$, mimo minusa.

## Doświadczenie / symulacja

**Symulacja PhET:** *Fala na strunie* (*Wave on a String*, [phet.colorado.edu/pl](https://phet.colorado.edu/pl/)). Ustaw tryb *Oscylator* i koniec bez odbić, zmierz linijką i stoperem z symulacji $\lambda$ i $T$. Sprawdź, że $v = \lambda f$ nie zależy od częstotliwości, a zmienia się z napięciem.

**Sprężyna „slinky”** (lub długa sprężyna od zabawki) pozwala pokazać falę poprzeczną i podłużną na jednym przedmiocie.

**Python:** migawki fali w kilku chwilach — grzbiet przesuwa się o $v\,\Delta t$.

```python
import numpy as np
import matplotlib.pyplot as plt

A, k, w = 0.05, np.pi, 4*np.pi
v = w/k
x = np.linspace(0, 6, 600)
for t in (0, 0.1, 0.2):
    plt.plot(x, A*np.sin(k*x - w*t)*100, label=f"t = {t} s")
print(f"v = {v:.1f} m/s, λ = {2*np.pi/k:.1f} m, przesunięcie w 0,1 s = {v*0.1:.1f} m")
print(f"maksymalna prędkość elementu liny = {A*w:.3f} m/s")
plt.xlabel("x [m]"); plt.ylabel("y [cm]"); plt.grid(True); plt.legend(); plt.show()
```

## Zadania

### A. Poziom maturalny

1. Stacja radiowa nadaje na częstotliwości 100 MHz. Oblicz długość fali ($c = 3\cdot10^8\ \mathrm{m/s}$).

<details>
<summary>Odpowiedź</summary>

$\lambda = c/f = 3\ \mathrm{m}$.
</details>

2. Człowiek słyszy dźwięki od 20 Hz do 20 kHz. Jakim długościom fal w powietrzu ($v = 343\ \mathrm{m/s}$) to odpowiada?

<details>
<summary>Odpowiedź</summary>

Od ok. 17 m do ok. 1,7 cm.
</details>

3. Grzbiety fal na jeziorze są odległe o 0,5 m, a o pomost uderzają 3 grzbiety na sekundę. Oblicz prędkość fali.

<details>
<summary>Odpowiedź</summary>

$v = \lambda f = 1{,}5\ \mathrm{m/s}$.
</details>

4. Fala przechodzi z powietrza do wody, a prędkość dźwięku rośnie z 343 do 1480 m/s. Co się dzieje z częstotliwością i długością fali?

<details>
<summary>Odpowiedź</summary>

Częstotliwość się nie zmienia. Długość fali rośnie ok. 4,3 razy.
</details>

### B. Poziom akademicki

1. Fala ma postać $y = 0{,}03\sin(4x + 20t)$ (SI). Podaj kierunek ruchu, prędkość, długość fali, okres i maksymalną prędkość elementu ośrodka.

<details>
<summary>Odpowiedź</summary>

Biegnie w stronę $-x$. $v = 20/4 = 5\ \mathrm{m/s}$, $\lambda = 2\pi/4 \approx 1{,}57\ \mathrm{m}$, $T = 2\pi/20 \approx 0{,}31\ \mathrm{s}$, $v_{y,\max} = A\omega = 0{,}6\ \mathrm{m/s}$.
</details>

2. Pokaż, że dowolna dwukrotnie różniczkowalna funkcja $y = f(x - vt)$ spełnia równanie falowe.

<details>
<summary>Odpowiedź</summary>

Niech $u = x - vt$. Wtedy $\partial^2y/\partial x^2 = f''(u)$ i $\partial^2y/\partial t^2 = v^2f''(u)$, więc $\partial_t^2y = v^2\partial_x^2y$.
</details>

3. Impuls na linie ma w chwili $t = 0$ kształt $y = \dfrac{0{,}1}{1 + 4x^2}$ (SI) i biegnie w stronę $-x$ z prędkością 2 m/s. Zapisz $y(x, t)$ i znajdź prędkość elementu w punkcie $x = 0{,}5\ \mathrm{m}$ w chwili $t = 0$.

<details>
<summary>Odpowiedź</summary>

$y = \dfrac{0{,}1}{1 + 4(x + 2t)^2}$. Dla $t = 0$: $\partial y/\partial t = -\dfrac{0{,}1\cdot16(x + 2t)}{[1 + 4(x + 2t)^2]^2} = -\dfrac{0{,}8}{4} = -0{,}2\ \mathrm{m/s}$, czyli w dół.
</details>

## Źródła

- OpenStax, *Fizyka dla szkół wyższych*, t. 1, rozdz. 16 — §16.1 (fale biegnące) i §16.2 (matematyczny opis fal).
- Halliday, Resnick, Walker, *Podstawy fizyki* — wyd. 2015: t. 2, §16.1; wyd. 1: t. 2, §17.1–17.5.
- Symulacja PhET *Fala na strunie*.
