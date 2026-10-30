# 09.01 — Ruch harmoniczny prosty i jego równanie

> **Moduł:** [09 — Drgania](README.md) · **Poziom:** 🟢🔵 matura R + studia · **Status:** ✅ pełny
>
> **Czytaj:**
>
> - OpenStax, *Fizyka dla szkół wyższych*, t. 1, rozdz. 15: [§15.1 i §15.3](https://openstax.org/books/fizyka-dla-szk%C3%B3%C5%82-wy%C5%BCszych-tom-1/pages/15-1-ruch-harmoniczny) · [wstęp do rozdziału](https://openstax.org/books/fizyka-dla-szk%C3%B3%C5%82-wy%C5%BCszych-tom-1/pages/15-wstep)
> - Halliday, Resnick, Walker, *Podstawy fizyki*, wyd. 2015, t. 2: §15.1 (s. 116)
> - Halliday, Resnick, Walker, *Podstawy fizyki*, wyd. 1 (2003), t. 2: [§16.1–16.3, s. 94](https://home.agh.edu.pl/~czapli/Resnick_2.pdf#page=110), [§16.7, s. 108](https://home.agh.edu.pl/~czapli/Resnick_2.pdf#page=124) — PDF z serwera AGH

← (początek modułu) · [spis modułu](README.md) · [Energia w ruchu harmonicznym](02-energia-w-ruchu-harmonicznym.md) →

## Po co to jest

Ruch harmoniczny to najważniejszy model drgań w fizyce. Każde ciało wychylone nieznacznie z położenia równowagi trwałej drga harmonicznie (04.06) — ciężarek na sprężynie, wahadło, atomy w krysztale, ładunek w obwodzie LC (15.05), membrana głośnika. Na nim zbudowane są fale (10), prąd przemienny (15) i optyka falowa (18); w mechanice kwantowej oscylator harmoniczny jest jednym z dwóch zagadnień rozwiązywanych dokładnie (20.06).

## Teoria w pigułce

**Ruch harmoniczny prosty** występuje, gdy siła jest proporcjonalna do wychylenia z położenia równowagi i skierowana do niego (siła sprężystości):

$$F = -kx \quad\Rightarrow\quad m\ddot{x} = -kx \quad\Rightarrow\quad \ddot{x} = -\omega^2x, \qquad \omega = \sqrt{\frac km}.$$

**Rozwiązanie** (00.05):

$$x(t) = A\cos(\omega t + \varphi),$$

- $A$ — **amplituda** (największe wychylenie),
- $\omega$ — **częstość kołowa** (rad/s), $T = 2\pi/\omega$ — **okres**, $f = 1/T$ — **częstotliwość** (Hz),
- $\omega t + \varphi$ — **faza**, $\varphi$ — **faza początkowa**.

Amplituda i faza początkowa zależą od warunków początkowych; okres — tylko od $k$ i $m$ (nie od amplitudy!). To cecha charakterystyczna drgań harmonicznych — **izochronizm**.

**Prędkość i przyspieszenie:**

$$v = -A\omega\sin(\omega t + \varphi), \quad v_{\max} = A\omega; \qquad a = -A\omega^2\cos(\omega t + \varphi) = -\omega^2x, \quad a_{\max} = A\omega^2.$$

W położeniu równowagi prędkość jest największa, a przyspieszenie zerowe; w skrajnych położeniach — odwrotnie.

**Ruch harmoniczny a ruch po okręgu.** Rzut punktu poruszającego się jednostajnie po okręgu o promieniu $A$ z prędkością kątową $\omega$ na średnicę wykonuje dokładnie ruch harmoniczny (02.06). Stąd nazwa „częstość kołowa”.

**Sprężyna pionowa.** Ciężar przesuwa tylko położenie równowagi (o $mg/k$); okres jest taki sam jak w poziomie.

## Wzory i założenia

| Wzór | Znaczenie | Kiedy obowiązuje |
|---|---|---|
| $x = A\cos(\omega t + \varphi)$ | równanie ruchu | siła $F = -kx$ |
| $\omega = \sqrt{k/m}$, $\ T = 2\pi\sqrt{m/k}$ | częstość i okres ciężarka na sprężynie | sprężyna nieważka, prawo Hooke'a |
| $v_{\max} = A\omega$, $\ a_{\max} = A\omega^2$ | wartości maksymalne | — |
| $a = -\omega^2x$ | warunek ruchu harmonicznego | — |
| $A = \sqrt{x_0^2 + (v_0/\omega)^2}$ | amplituda z warunków początkowych | — |
| $k_{\text{rów}} = k_1 + k_2$; $\ \dfrac{1}{k_{\text{szer}}} = \dfrac{1}{k_1} + \dfrac{1}{k_2}$ | sprężyny równolegle i szeregowo | — |

## Przykład rozwiązany

**Zadanie.** Ciężarek o masie 0,5 kg drga na sprężynie o współczynniku 200 N/m z amplitudą 5 cm. Oblicz okres, częstotliwość, największą prędkość i największe przyspieszenie.

$\omega = \sqrt{200/0{,}5} = 20\ \mathrm{rad/s}$, $T = 2\pi/20 \approx 0{,}314\ \mathrm{s}$, $f \approx 3{,}18\ \mathrm{Hz}$.

$v_{\max} = 0{,}05\cdot20 = 1\ \mathrm{m/s}$, $a_{\max} = 0{,}05\cdot400 = 20\ \mathrm{m/s^2}$ — ponad $2g$.

### Wersja z rachunkiem różniczkowym i całkowym

**Zadanie.** Ten sam ciężarek w chwili $t = 0$ jest w położeniu $x_0 = 3\ \mathrm{cm}$ i porusza się z prędkością $v_0 = -0{,}8\ \mathrm{m/s}$ (w stronę równowagi). Wyznacz amplitudę i fazę początkową.

Z $x(0) = A\cos\varphi = 0{,}03$ i $v(0) = -A\omega\sin\varphi = -0{,}8$:

$$A = \sqrt{x_0^2 + \left(\frac{v_0}{\omega}\right)^2} = \sqrt{0{,}03^2 + 0{,}04^2} = 0{,}05\ \mathrm{m}, \qquad \tan\varphi = -\frac{v_0}{\omega x_0} = \frac{0{,}8}{0{,}6} \Rightarrow \varphi \approx 53{,}1^\circ.$$

Sprawdzenie: $\cos53{,}1^\circ = 0{,}6$, $0{,}05\cdot0{,}6 = 0{,}03$ ✓; $\sin53{,}1^\circ = 0{,}8$, $-0{,}05\cdot20\cdot0{,}8 = -0{,}8$ ✓.

**Weryfikacja rozwiązania.** Wstawiając $x = A\cos(\omega t + \varphi)$ do $\ddot{x} + \omega^2x$: $-A\omega^2\cos(\cdot) + \omega^2A\cos(\cdot) = 0$ — równanie jest spełnione dla dowolnych $A$ i $\varphi$.

## Typowe pułapki

- **Okres zależy od amplitudy.** W ruchu harmonicznym nie zależy.
- **Prędkość największa w skrajnym położeniu.** Tam jest zerowa; największa jest w położeniu równowagi.
- **Kalkulator w stopniach.** Faza $\omega t$ jest w radianach.
- **Mylenie $\omega$ i $f$.** $\omega = 2\pi f$; w Hz podajemy $f$, w rad/s — $\omega$.
- **Sprężyny szeregowo „dodają się”.** Równolegle tak; szeregowo dają **mniejszy** współczynnik.

## Doświadczenie / symulacja

**Sprężyna i telefon.** Zawieś telefon (w woreczku) na gumie lub sprężynie i uruchom w phyphox eksperyment *Spring* (lub *Acceleration*). Aplikacja zmierzy okres. Dołóż znane masy (np. monety w woreczku) i narysuj $T^2$ od $m$: nachylenie to $4\pi^2/k$.

**Symulacja PhET:** *Masy i sprężyny* (*Masses and Springs*, [phet.colorado.edu/pl](https://phet.colorado.edu/pl/)) — wyznacz $k$ z wydłużenia statycznego i sprawdź okres.

**Python:** położenie, prędkość i przyspieszenie z przykładu oraz rozwiązanie numeryczne równania ruchu.

```python
import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp

m, k = 0.5, 200.0
w = np.sqrt(k/m)
x0, v0 = 0.03, -0.8
A = np.hypot(x0, v0/w); phi = np.arctan2(-v0/w, x0)
print(f"A = {A:.3f} m, φ = {np.degrees(phi):.1f}°, T = {2*np.pi/w:.4f} s")

t = np.linspace(0, 0.7, 500)
sol = solve_ivp(lambda t, s: [s[1], -k/m*s[0]], (0, 0.7), [x0, v0], t_eval=t, rtol=1e-10)
x = A*np.cos(w*t + phi)
print(f"maks. różnica numeryka–wzór: {np.max(abs(sol.y[0] - x)):.1e} m")

fig, ax = plt.subplots(3, 1, figsize=(6, 6), sharex=True)
ax[0].plot(t, x*100); ax[0].set_ylabel("x [cm]")
ax[1].plot(t, -A*w*np.sin(w*t + phi)); ax[1].set_ylabel("v [m/s]")
ax[2].plot(t, -w**2*x); ax[2].set_ylabel("a [m/s²]"); ax[2].set_xlabel("t [s]")
for a in ax: a.grid(True)
plt.tight_layout(); plt.show()
```

## Zadania

### A. Poziom maturalny

1. Ciężarek o masie 0,2 kg drga na sprężynie o współczynniku 80 N/m. Oblicz okres i częstotliwość.

<details>
<summary>Odpowiedź</summary>

$T = 2\pi\sqrt{0{,}2/80} \approx 0{,}314\ \mathrm{s}$, $f \approx 3{,}18\ \mathrm{Hz}$.
</details>

2. Po zawieszeniu ciężarka sprężyna wydłużyła się o 10 cm. Jaki będzie okres drgań ciężarka?

<details>
<summary>Odpowiedź</summary>

$k/m = g/\Delta l$: $T = 2\pi\sqrt{\Delta l/g} \approx 0{,}63\ \mathrm{s}$ — nie trzeba znać masy.
</details>

3. Jak zmieni się okres drgań, gdy masa ciężarka wzrośnie czterokrotnie? A gdy amplituda wzrośnie dwukrotnie?

<details>
<summary>Odpowiedź</summary>

Wzrośnie dwukrotnie; nie zmieni się.
</details>

4. Drgania opisuje równanie $x = 0{,}04\cos(5\pi t)$ (m, s). Podaj amplitudę, okres, częstotliwość i największą prędkość.

<details>
<summary>Odpowiedź</summary>

$A = 4\ \mathrm{cm}$, $\omega = 5\pi$, $T = 0{,}4\ \mathrm{s}$, $f = 2{,}5\ \mathrm{Hz}$, $v_{\max} = 0{,}2\pi \approx 0{,}63\ \mathrm{m/s}$.
</details>

5. Dwie jednakowe sprężyny o współczynniku $k$ połączono a) równolegle, b) szeregowo i zawieszono na nich ciężarek $m$. Ile razy różnią się okresy drgań?

<details>
<summary>Odpowiedź</summary>

a) $k_r = 2k$, b) $k_s = k/2$; $T_s/T_r = \sqrt{4} = 2$.
</details>

### B. Poziom akademicki

1. Gdy do samochodu o masie 1200 kg wsiadają cztery osoby (łącznie 300 kg), nadwozie obniża się o 3 cm. Oblicz okres drgań pionowych załadowanego samochodu (bez tłumienia).

<details>
<summary>Odpowiedź</summary>

$k = 300\cdot9{,}81/0{,}03 \approx 9{,}8\cdot10^4\ \mathrm{N/m}$; $T = 2\pi\sqrt{1500/98\,100} \approx 0{,}78\ \mathrm{s}$.
</details>

2. Wyprowadź współczynniki zastępcze dla sprężyn równoległych i szeregowych.

<details>
<summary>Odpowiedź</summary>

Równolegle — wspólne wydłużenie, siły się sumują: $k_r = k_1 + k_2$. Szeregowo — wspólna siła, wydłużenia się sumują: $F/k_s = F/k_1 + F/k_2$.
</details>

3. Ciało drga zgodnie z $x = A\cos(\omega t)$. Oblicz średnią wartość $v^2$ w ciągu okresu i porównaj z $v_{\max}^2$.

<details>
<summary>Odpowiedź</summary>

$\overline{v^2} = A^2\omega^2\overline{\sin^2} = \tfrac12v_{\max}^2$.
</details>

4. Pokaż, że $x = C_1\cos\omega t + C_2\sin\omega t$ to ta sama rodzina rozwiązań co $A\cos(\omega t + \varphi)$, i wyraź $A$, $\varphi$ przez $C_1$, $C_2$.

<details>
<summary>Odpowiedź</summary>

$A\cos(\omega t + \varphi) = A\cos\varphi\cos\omega t - A\sin\varphi\sin\omega t$: $C_1 = A\cos\varphi$, $C_2 = -A\sin\varphi$; $A = \sqrt{C_1^2 + C_2^2}$, $\tan\varphi = -C_2/C_1$.
</details>

## Źródła

- OpenStax, *Fizyka dla szkół wyższych*, t. 1, rozdz. 15 — §15.1 (ruch harmoniczny) i §15.3 (związek z ruchem po okręgu).
- Halliday, Resnick, Walker, *Podstawy fizyki* — wyd. 2015: t. 2, §15.1; wyd. 1: t. 2, §16.1–16.3 i §16.7.
- Symulacja PhET *Masy i sprężyny*.
