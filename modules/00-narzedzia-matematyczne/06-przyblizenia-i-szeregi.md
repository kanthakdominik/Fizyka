# 00.06 — Przybliżenia i szeregi (małe kąty, dwumian, Taylor)

> **Moduł:** [00 — Narzędzia matematyczne fizyka](README.md) · **Poziom:** 🔵 studia · **Status:** ✅ pełny
>
> **Czytaj:**
>
> - OpenStax, *Fizyka dla szkół wyższych*, t. 1, rozdz. 15: [§15.4](https://openstax.org/books/fizyka-dla-szk%C3%B3%C5%82-wy%C5%BCszych-tom-1/pages/15-4-wahadla) · [wstęp do rozdziału](https://openstax.org/books/fizyka-dla-szk%C3%B3%C5%82-wy%C5%BCszych-tom-1/pages/15-wstep)
> - Halliday, Resnick, Walker, *Podstawy fizyki*, wyd. 2015, t. 2: §15.4 (s. 131)
> - Halliday, Resnick, Walker, *Podstawy fizyki*, wyd. 1 (2003): [t. 2, rozdz. 16](https://home.agh.edu.pl/~czapli/Resnick_2.pdf) — PDF z serwera AGH

← [Proste równania różniczkowe w fizyce](05-rownania-rozniczkowe.md) · [spis modułu](README.md) · [Współrzędne biegunowe, walcowe, sferyczne i całki wielokrotne](07-wspolrzedne-i-calki-wielokrotne.md) →

## Po co to jest

Fizyka prawie zawsze pracuje na przybliżeniach: wahadło jest harmoniczne „dla małych kątów”, ciężar jest stały „blisko powierzchni Ziemi”, energia kinetyczna to $\tfrac12mv^2$ „dla prędkości małych w porównaniu z $c$”. Za każdym z tych zdań stoi rozwinięcie funkcji w szereg i odrzucenie małych wyrazów. Umiejętność zrobienia takiego przybliżenia — i oceny, ile kosztuje — odróżnia rozumienie fizyki od zapamiętania wzorów.

## Teoria w pigułce

**Szereg Taylora.** Funkcję gładką w pobliżu punktu $x_0$ można zastąpić wielomianem:

$$f(x_0 + h) = f(x_0) + f'(x_0)\,h + \frac{f''(x_0)}{2!}h^2 + \frac{f'''(x_0)}{3!}h^3 + \dots$$

Gdy $h$ jest małe, kolejne wyrazy są coraz mniejsze i wystarczy kilka pierwszych. Błąd przybliżenia jest rzędu **pierwszego odrzuconego wyrazu**.

**Najważniejsze przybliżenia** (dla $\lvert x\rvert \ll 1$, kąty w radianach):

| Funkcja | Przybliżenie 1. rzędu | Następny wyraz |
|---|---|---|
| $\sin x$ | $x$ | $-x^3/6$ |
| $\cos x$ | $1$ | $-x^2/2$ |
| $\tan x$ | $x$ | $+x^3/3$ |
| $(1 + x)^n$ | $1 + nx$ | $+\tfrac{n(n-1)}{2}x^2$ |
| $e^x$ | $1 + x$ | $+x^2/2$ |
| $\ln(1 + x)$ | $x$ | $-x^2/2$ |

Wzór dwumianowy $(1 + x)^n \approx 1 + nx$ działa dla dowolnego $n$, także ujemnego i ułamkowego: $\sqrt{1 + x} \approx 1 + x/2$, $1/(1 + x) \approx 1 - x$, $1/(1+x)^2 \approx 1 - 2x$.

**Sztuczka: wyciągnij dużą wielkość przed nawias.** Żeby przybliżyć $\dfrac{1}{(R + h)^2}$ dla $h \ll R$, piszemy $\dfrac{1}{R^2}\left(1 + \dfrac{h}{R}\right)^{-2} \approx \dfrac{1}{R^2}\left(1 - \dfrac{2h}{R}\right)$. Mała wielkość musi być **bezwymiarowa** — porównujemy $h/R$ z jedynką.

**Każde małe drganie jest harmoniczne.** Blisko minimum energii potencjalnej $U(x) \approx U(x_0) + \tfrac12U''(x_0)(x - x_0)^2$ (wyraz liniowy znika, bo $U'(x_0) = 0$). To parabola, czyli sprężyna o $k = U''(x_0)$.

## Wzory i założenia

| Zastosowanie | Przybliżenie | Warunek |
|---|---|---|
| wahadło | $\sin\theta \approx \theta \Rightarrow T = 2\pi\sqrt{l/g}$ | $\theta_0 \lesssim 10^\circ$–$15^\circ$ (błąd okresu poniżej 0,5%) |
| ciążenie na wysokości $h$ | $g(h) \approx g_0\left(1 - \dfrac{2h}{R}\right)$ | $h \ll R$ |
| energia kinetyczna | $(\gamma - 1)mc^2 \approx \tfrac12mv^2$ | $v \ll c$ |
| interferencja | $\sin\theta \approx \tan\theta \approx y/L$ | $y \ll L$ |
| małe drgania wokół minimum $U$ | $k = U''(x_0)$, $\omega = \sqrt{U''(x_0)/m}$ | małe wychylenie |

## Przykład rozwiązany

### Wersja z rachunkiem różniczkowym i całkowym

**Zadanie.** O ile procent mniejsze jest przyspieszenie grawitacyjne na wysokości $h = 300\ \mathrm{km}$ (orbita stacji kosmicznej) niż na powierzchni Ziemi ($R = 6371\ \mathrm{km}$)? Policz dokładnie i w przybliżeniu.

**Dokładnie.** $\dfrac{g(h)}{g_0} = \left(\dfrac{R}{R+h}\right)^2 = \left(\dfrac{6371}{6671}\right)^2 \approx 0{,}912$ — mniej o 8,8%.

**Przybliżenie.** $\dfrac{g(h)}{g_0} = \left(1 + \dfrac{h}{R}\right)^{-2} \approx 1 - \dfrac{2h}{R} = 1 - \dfrac{600}{6371} \approx 0{,}906$ — mniej o 9,4%.

**Ocena błędu.** Następny wyraz szeregu to $+3(h/R)^2 \approx 0{,}0067$, co tłumaczy różnicę. Przy $h/R \approx 0{,}05$ przybliżenie liniowe myli się o ok. 0,6 punktu procentowego — wystarczająco do szacowania, za mało do nawigacji satelitarnej.

**Zadanie 2.** Pokaż, że dla małych prędkości relatywistyczna energia kinetyczna przechodzi w $\tfrac12mv^2$, i oszacuj poprawkę dla $v = 0{,}1c$.

$$E_k = (\gamma - 1)mc^2,\quad \gamma = \left(1 - \frac{v^2}{c^2}\right)^{-1/2} \approx 1 + \frac12\frac{v^2}{c^2} + \frac38\frac{v^4}{c^4}.$$

$$E_k \approx \frac12mv^2\left(1 + \frac34\frac{v^2}{c^2}\right).$$

Dla $v = 0{,}1c$ poprawka to $\tfrac34\cdot0{,}01 = 0{,}75\%$.

## Typowe pułapki

- **Kąt w stopniach.** $\sin x \approx x$ działa tylko w radianach: $\sin 10^\circ \approx 0{,}1745$, a nie $10$.
- **Porównywanie wielkości z jednostką z liczbą.** „$h$ jest małe” nic nie znaczy; małe jest $h/R$.
- **Przybliżenie przed odjęciem.** W wyrażeniu $\sqrt{1 + x} - 1$ przybliżenie $\sqrt{1+x} \approx 1$ daje zero; trzeba zostawić wyraz $x/2$. Zostawiaj tyle wyrazów, żeby różnica była niezerowa.
- **Przybliżenie poza zakresem.** Dla $\theta_0 = 60^\circ$ okres wahadła jest o ok. 7% dłuższy niż ze wzoru $2\pi\sqrt{l/g}$.

## Doświadczenie / symulacja

**Doświadczenie z telefonem.** Zawieś telefon jako wahadło i zmierz okres w phyphox (eksperyment *Pendulum*) dla amplitud ok. $10^\circ$, $30^\circ$ i $60^\circ$. Porównaj ze wzorem z poprawką $T \approx T_0\left(1 + \theta_0^2/16\right)$.

**Python:** jak szybko psuje się przybliżenie $\sin x \approx x$ i co daje kolejny wyraz.

```python
import numpy as np
import matplotlib.pyplot as plt

deg = np.array([1, 5, 10, 15, 20, 30, 45, 60])
x = np.radians(deg)
err1 = (x - np.sin(x)) / np.sin(x) * 100
err3 = (x - x**3/6 - np.sin(x)) / np.sin(x) * 100
for d, e1, e3 in zip(deg, err1, err3):
    print(f"{d:3d}°  błąd sin≈x: {e1:7.3f}%   błąd sin≈x−x³/6: {e3:8.4f}%")

xs = np.linspace(0, np.pi/2, 200)
plt.plot(np.degrees(xs), np.sin(xs), label="sin x")
plt.plot(np.degrees(xs), xs, "--", label="x")
plt.plot(np.degrees(xs), xs - xs**3/6, ":", label="x − x³/6")
plt.xlabel("kąt [°]"); plt.grid(True); plt.legend(); plt.show()
```

## Zadania

### A. Poziom maturalny _(opcjonalnie — rozgrzewka)_

1. Oblicz $\sin 10^\circ$ i kąt $10^\circ$ w radianach. O ile procent się różnią?

<details>
<summary>Odpowiedź</summary>

$0{,}1736$ i $0{,}1745$; różnica ok. 0,5%.
</details>

2. Oszacuj bez kalkulatora $1{,}02^3$ i $\sqrt{1{,}01}$.

<details>
<summary>Odpowiedź</summary>

$1{,}02^3 \approx 1 + 3\cdot0{,}02 = 1{,}06$ (dokładnie 1,0612); $\sqrt{1{,}01} \approx 1{,}005$.
</details>

3. Gdy promień okręgu wzrośnie o 1%, o ile procent wzrośnie jego pole? A objętość kuli?

<details>
<summary>Odpowiedź</summary>

Pole ok. 2%, objętość ok. 3% (z $(1 + x)^n \approx 1 + nx$).
</details>

### B. Poziom akademicki

1. Okres wahadła z poprawką na amplitudę: $T \approx T_0(1 + \theta_0^2/16)$. O ile procent okres przy $\theta_0 = 20^\circ$ jest dłuższy od $T_0$?

<details>
<summary>Odpowiedź</summary>

$\theta_0 = 0{,}349\ \mathrm{rad}$, $\theta_0^2/16 \approx 0{,}0076$ — o ok. 0,76%.
</details>

2. Na jakiej wysokości przyspieszenie grawitacyjne jest o 1% mniejsze niż na powierzchni Ziemi?

<details>
<summary>Odpowiedź</summary>

$2h/R = 0{,}01 \Rightarrow h \approx 0{,}005R \approx 32\ \mathrm{km}$.
</details>

3. Cząstka o masie $m$ porusza się w potencjale $U(x) = U_0\cosh(x/a)$. Znajdź częstość małych drgań wokół minimum.

<details>
<summary>Odpowiedź</summary>

$\cosh u \approx 1 + u^2/2$, więc $U \approx U_0 + \dfrac{U_0}{2a^2}x^2$, $k = U_0/a^2$, $\omega = \sqrt{U_0/(ma^2)}$.
</details>

4. Dwa ładunki $+q$ i $-q$ leżą na osi $x$ w punktach $\pm d/2$. Pokaż, że potencjał w punkcie $x \gg d$ na osi wynosi w przybliżeniu $V \approx \dfrac{kqd}{x^2}$.

<details>
<summary>Odpowiedź</summary>

$V = kq\left[\dfrac{1}{x - d/2} - \dfrac{1}{x + d/2}\right] = \dfrac{kq}{x}\left[\left(1 - \tfrac{d}{2x}\right)^{-1} - \left(1 + \tfrac{d}{2x}\right)^{-1}\right] \approx \dfrac{kq}{x}\cdot\dfrac{d}{x}$. To potencjał dipola.
</details>

5. Rozwiń $f(x) = \dfrac{1}{\sqrt{1 - x}}$ do wyrazu z $x^2$ i porównaj z wartością dokładną dla $x = 0{,}1$.

<details>
<summary>Odpowiedź</summary>

$1 + \tfrac12x + \tfrac38x^2$; dla $x = 0{,}1$: $1{,}05375$ wobec $1{,}05409$.
</details>

## Źródła

- OpenStax, *Fizyka dla szkół wyższych*, t. 1 — §15.4 (wahadło i przybliżenie małych kątów); t. 3, §5.9 (energia relatywistyczna i jej granica nierelatywistyczna).
- Halliday, Resnick, Walker, *Podstawy fizyki*, wyd. 2015, t. 2, rozdz. 15 — §15.4: wahadła; dodatek E: wzory matematyczne, w tym rozwinięcia w szereg.
