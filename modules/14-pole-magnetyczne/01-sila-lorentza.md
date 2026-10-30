# 14.01 — Pole magnetyczne, siła Lorentza i ruch ładunku

> **Moduł:** [14 — Pole magnetyczne](README.md) · **Poziom:** 🟢 matura R · **Status:** ✅ pełny
>
> **Czytaj:**
>
> - OpenStax, *Fizyka dla szkół wyższych*, t. 2, rozdz. 11: [§11.1–11.3](https://openstax.org/books/fizyka-dla-szk%C3%B3%C5%82-wy%C5%BCszych-tom-2/pages/11-1-odkrywanie-magnetyzmu) · [wstęp do rozdziału](https://openstax.org/books/fizyka-dla-szk%C3%B3%C5%82-wy%C5%BCszych-tom-2/pages/11-wstep)
> - Halliday, Resnick, Walker, *Podstawy fizyki*, wyd. 2015, t. 3: §28.1–28.2 (s. 251), §28.4 (s. 265)
> - Halliday, Resnick, Walker, *Podstawy fizyki*, wyd. 1 (2003), t. 3: §29.1–29.2, s. 185, §29.5, s. 195 (skan t. 3 na serwerze AGH kończy się na s. 127 — dalsze strony tylko w wydaniu papierowym)

← (początek modułu) · [spis modułu](README.md) · [Siła elektrodynamiczna i moment sił na ramkę z prądem](02-sila-elektrodynamiczna.md) →

## Po co to jest

Pole magnetyczne działa tylko na ładunki w ruchu i zakrzywia ich tory. Dzięki temu działały kineskopy, działają akceleratory, spektrometry masowe i tokamaki utrzymujące gorącą plazmę. Ziemskie pole magnetyczne odchyla cząstki wiatru słonecznego i kieruje je ku biegunom, gdzie wywołują zorze polarne. Siła Lorentza to też podstawa silników elektrycznych (14.02) i indukcji (15).

## Teoria w pigułce

**Pole magnetyczne** $\vec B$ (indukcja magnetyczna) opisuje się przez siłę, jaką działa na poruszający się ładunek. Jednostką jest tesla: $1\ \mathrm T = 1\ \dfrac{\mathrm N}{\mathrm{A\cdot m}}$. Przykładowe wartości:
- pole Ziemi: ok. 50 μT;
- magnes na lodówkę: ok. 5 mT;
- magnes neodymowy przy powierzchni: ok. 1 T;
- tomograf MRI: 1,5–3 T.

Linie pola wychodzą z bieguna północnego magnesu (N) i wchodzą do południowego (S). Są zawsze zamknięte, bo nie ma ładunków magnetycznych.

**Siła Lorentza** (część magnetyczna):

$$\vec F = q\vec v\times\vec B, \qquad F = \lvert q\rvert vB\sin\alpha.$$

- Siła jest prostopadła do prędkości i do pola. Zwrot wyznacza **reguła prawej dłoni** dla ładunku dodatniego (palce wzdłuż $\vec v$, zgięte w stronę $\vec B$, kciuk wskazuje $\vec F$). Dla ujemnego zwrot jest przeciwny.
- Na ładunek poruszający się wzdłuż linii pola siła nie działa.
- Siła jest zawsze prostopadła do prędkości, więc **nie wykonuje pracy**. Zmienia kierunek prędkości, ale nie jej wartość ani energię kinetyczną.

Pełna siła Lorentza obejmuje też pole elektryczne: $\vec F = q(\vec E + \vec v\times\vec B)$.

**Ruch w polu jednorodnym.** Ładunek wpadający prostopadle do linii pola porusza się po okręgu. Siła Lorentza pełni rolę siły dośrodkowej (03.04):

$$\lvert q\rvert vB = \frac{mv^2}{r} \quad\Rightarrow\quad r = \frac{mv}{\lvert q\rvert B}, \qquad T = \frac{2\pi m}{\lvert q\rvert B}, \qquad f_c = \frac{\lvert q\rvert B}{2\pi m}.$$

Okres (**częstotliwość cyklotronowa**) nie zależy od prędkości. Szybsze cząstki zataczają większe okręgi w tym samym czasie (14.03).

Gdy prędkość ma też składową wzdłuż pola, tor jest **linią śrubową**. Tak cząstki z wiatru słonecznego nawijają się na linie pola Ziemi i wędrują ku biegunom.

**Selektor prędkości.** Skrzyżowane pola $\vec E \perp \vec B$ przepuszczają bez odchylenia tylko cząstki o prędkości $v = E/B$, bo wtedy $qE = qvB$.

## Wzory i założenia

| Wzór | Znaczenie | Kiedy obowiązuje |
|---|---|---|
| $\vec F = q\vec v\times\vec B$, $F = \lvert q\rvert vB\sin\alpha$ | siła Lorentza (magnetyczna) | — |
| $\vec F = q(\vec E + \vec v\times\vec B)$ | pełna siła Lorentza | — |
| $r = mv/(\lvert q\rvert B)$ | promień okręgu | $\vec v \perp \vec B$, pole jednorodne |
| $T = 2\pi m/(\lvert q\rvert B)$ | okres obiegu | $v \ll c$ |
| $v = E/B$ | selektor prędkości | $\vec E \perp \vec B \perp \vec v$ |

## Przykład rozwiązany

**Zadanie 1.** Elektron o prędkości $10^7\ \mathrm{m/s}$ wpada prostopadle w pole magnetyczne 1 mT. Oblicz promień okręgu i okres obiegu.

$r = \dfrac{9{,}11\cdot10^{-31}\cdot10^7}{1{,}6\cdot10^{-19}\cdot10^{-3}} \approx 5{,}7\ \mathrm{cm}$, $T = \dfrac{2\pi m}{eB} \approx 36\ \mathrm{ns}$.

**Zadanie 2.** Proton o energii 1 MeV porusza się prostopadle do pola 1 T. Oblicz promień jego toru.

$v = \sqrt{2E/m} \approx 1{,}38\cdot10^7\ \mathrm{m/s}$, $r = mv/(eB) \approx 14{,}5\ \mathrm{cm}$. Proton ma 1836 razy większą masę niż elektron, więc w tym samym polu zatacza dużo większe okręgi.

## Typowe pułapki

- **Pole magnetyczne przyspiesza ładunek.** Zmienia tylko kierunek prędkości. Energia kinetyczna się nie zmienia.
- **Siła wzdłuż linii pola.** Siła magnetyczna jest prostopadła do linii pola. W tym siła magnetyczna różni się od elektrycznej.
- **Reguła dłoni dla elektronu.** Dla ładunku ujemnego zwrot siły jest przeciwny.
- **Spoczywający ładunek w polu magnetycznym.** Gdy $v = 0$, siła wynosi zero.
- **Szybsza cząstka obiega szybciej.** Okres nie zależy od prędkości, rośnie tylko promień (do prędkości relatywistycznych).

## Doświadczenie / symulacja

**Wiązka elektronów i magnes.** Jeśli masz dostęp do starego oscyloskopu lub telewizora kineskopowego (albo w pracowni szkolnej do lampy z wiązką elektronów), zbliż magnes neodymowy do ekranu z boku. Obraz się przesuwa i odkształca. Uwaga: nie przykładaj silnego magnesu do kolorowego kineskopu, bo trwale namagnesuje maskę i zniekształci kolory.

**Magnetometr w telefonie.** phyphox (*Magnetometer*) mierzy trzy składowe pola. Zmierz pole Ziemi (ok. 50 μT) i jego nachylenie w Polsce (inklinacja ok. 65–70°).

**Symulacja PhET:** *Magnes i kompas* (*Magnet and Compass*) — linie pola magnesu sztabkowego ([phet.colorado.edu/pl](https://phet.colorado.edu/pl/)).

**Python:** numeryczne całkowanie ruchu ładunku w polu magnetycznym — okrąg, linia śrubowa i dryf w polach skrzyżowanych.

```python
import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp

q, m = -1.602e-19, 9.109e-31                       # elektron
B = np.array([0, 0, 1e-3])

def ruch(E, v0, t_end):
    f = lambda t, s: np.concatenate([s[3:], q/m*(E + np.cross(s[3:], B))])
    return solve_ivp(f, (0, t_end), np.concatenate([[0, 0, 0], v0]), max_step=t_end/2000, rtol=1e-9)

T = 2*np.pi*m/(abs(q)*np.linalg.norm(B))
s1 = ruch(np.zeros(3), np.array([1e7, 0, 0]), T)
r_num = (s1.y[1].max() - s1.y[1].min())/2
print(f"promień: numerycznie {r_num*100:.2f} cm, wzór {m*1e7/(abs(q)*1e-3)*100:.2f} cm, T = {T*1e9:.1f} ns")
print(f"|v| na końcu: {np.linalg.norm(s1.y[3:, -1]):.4e} m/s (siła nie wykonuje pracy)")
s2 = ruch(np.array([0, 2e3, 0]), np.array([1e6, 0, 0]), 5*T)      # E ⊥ B: dryf z prędkością E/B
print(f"dryf w polach skrzyżowanych: {s2.y[0, -1]/(5*T):.3e} m/s (E/B = {2e3/1e-3:.1e} m/s)")

fig, ax = plt.subplots(1, 2, figsize=(10, 4))
ax[0].plot(s1.y[0]*100, s1.y[1]*100); ax[0].set_aspect("equal"); ax[0].set_title("okrąg (B wzdłuż z)")
ax[1].plot(s2.y[0]*100, s2.y[1]*100); ax[1].set_title("dryf E×B")
for a in ax: a.set_xlabel("x [cm]"); a.set_ylabel("y [cm]"); a.grid(True)
plt.tight_layout(); plt.show()
```

## Zadania

### A. Poziom maturalny

1. Proton porusza się z prędkością $2\cdot10^6\ \mathrm{m/s}$ pod kątem $30^\circ$ do linii pola 0,5 T. Oblicz siłę Lorentza.

<details>
<summary>Odpowiedź</summary>

$F = evB\sin30^\circ \approx 8\cdot10^{-14}\ \mathrm N$.
</details>

2. Elektron o prędkości $10^6\ \mathrm{m/s}$ porusza się prostopadle do pola Ziemi (50 μT). Oblicz promień toru.

<details>
<summary>Odpowiedź</summary>

$r = mv/(eB) \approx 11\ \mathrm{cm}$.
</details>

3. W selektorze prędkości pole elektryczne wynosi $10^5\ \mathrm{V/m}$, a magnetyczne 0,1 T. Jakie cząstki przechodzą bez odchylenia? Czy ma znaczenie ich ładunek i masa?

<details>
<summary>Odpowiedź</summary>

$v = E/B = 10^6\ \mathrm{m/s}$, niezależnie od ładunku (także znaku) i masy.
</details>

4. Proton i elektron mają tę samą prędkość w tym samym polu. Porównaj promienie i okresy ich ruchu.

<details>
<summary>Odpowiedź</summary>

Promień i okres protonu są 1836 razy większe. Krążą w przeciwnych kierunkach.
</details>

### B. Poziom akademicki _(opcjonalnie — rozszerzenie z rachunkiem)_

1. Proton wpada w pole 0,1 T z prędkością $10^6\ \mathrm{m/s}$ pod kątem $60^\circ$ do linii pola. Oblicz promień i skok linii śrubowej.

<details>
<summary>Odpowiedź</summary>

$v_\perp = v\sin60^\circ$, $r = mv_\perp/(eB) \approx 9{,}0\ \mathrm{cm}$. $T = 2\pi m/(eB) \approx 0{,}66\ \mu\mathrm s$, skok $h = v_\parallel T = v\cos60^\circ\cdot T \approx 33\ \mathrm{cm}$.
</details>

2. Zapisz równania ruchu $m\dot{\vec v} = q\vec v\times\vec B$ dla $\vec B = B\hat z$ w składowych i pokaż, że $v_x = v_0\cos\omega t$, $v_y = \mp v_0\sin\omega t$ z $\omega = \lvert q\rvert B/m$.

<details>
<summary>Odpowiedź</summary>

$\dot v_x = (qB/m)v_y$, $\dot v_y = -(qB/m)v_x$, więc $\ddot v_x = -(qB/m)^2v_x$, czyli ruch harmoniczny z $\omega = \lvert q\rvert B/m$. Znak $v_y$ zależy od znaku ładunku.
</details>

3. Pokaż, że $\dfrac{d}{dt}\left(\tfrac12mv^2\right) = 0$ dla siły $q\vec v\times\vec B$.

<details>
<summary>Odpowiedź</summary>

$\dfrac{d}{dt}\left(\tfrac12m\vec v\cdot\vec v\right) = \vec v\cdot m\dot{\vec v} = q\vec v\cdot(\vec v\times\vec B) = 0$, bo iloczyn mieszany z dwoma tymi samymi wektorami znika.
</details>

## Źródła

- OpenStax, *Fizyka dla szkół wyższych*, t. 2, rozdz. 11 — §11.1 (magnetyzm i jego odkrycie), §11.2 (pole magnetyczne i jego linie), §11.3 (ruch cząstki naładowanej w polu magnetycznym).
- Halliday, Resnick, Walker, *Podstawy fizyki* — wyd. 2015: t. 3, §28.1–28.2, §28.4; wyd. 1: t. 3, §29.1–29.2, §29.5.
- Symulacja PhET *Magnes i kompas*.
