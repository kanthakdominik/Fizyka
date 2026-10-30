# 09.03 — Wahadło matematyczne, fizyczne i torsyjne

> **Moduł:** [09 — Drgania](README.md) · **Poziom:** 🟢🔵 matura R + studia · **Status:** ✅ pełny
>
> **Czytaj:**
>
> - OpenStax, *Fizyka dla szkół wyższych*, t. 1, rozdz. 15: [§15.4](https://openstax.org/books/fizyka-dla-szk%C3%B3%C5%82-wy%C5%BCszych-tom-1/pages/15-4-wahadla) · [wstęp do rozdziału](https://openstax.org/books/fizyka-dla-szk%C3%B3%C5%82-wy%C5%BCszych-tom-1/pages/15-wstep)
> - Halliday, Resnick, Walker, *Podstawy fizyki*, wyd. 2015, t. 2: §15.3–15.4 (s. 129)
> - Halliday, Resnick, Walker, *Podstawy fizyki*, wyd. 1 (2003), t. 2: [§16.5–16.6, s. 102](https://home.agh.edu.pl/~czapli/Resnick_2.pdf#page=118) — PDF z serwera AGH

← [Energia w ruchu harmonicznym](02-energia-w-ruchu-harmonicznym.md) · [spis modułu](README.md) · [Drgania tłumione](04-drgania-tlumione.md) →

## Po co to jest

Wahadło przez trzy stulecia było najdokładniejszym zegarem świata, a dziś wciąż służy do pomiaru $g$ (projekt modułu 01). Wahadło fizyczne (dowolna bryła na osi) opisuje huśtawki, nogę idącego człowieka i wahadła zegarowe, a wahadło torsyjne — wagę skręceń, którą Cavendish zmierzył stałą grawitacji (07.01). Wszystkie trzy to ruch harmoniczny, ale tylko dla małych wychyleń.

## Teoria w pigułce

**Wahadło matematyczne** — punktowa masa na nieważkiej nici o długości $l$. Składowa ciężaru styczna do toru: $F = -mg\sin\theta$. Dla małych kątów $\sin\theta \approx \theta$ (00.06), więc

$$ml\ddot{\theta} = -mg\theta \Rightarrow \omega = \sqrt{\frac gl}, \qquad T = 2\pi\sqrt{\frac lg}.$$

Okres nie zależy od masy ani (dla małych kątów) od amplitudy.

**Wahadło fizyczne** — bryła o masie $m$ i momencie bezwładności $I$ względem osi obrotu, odległej o $d$ od środka masy. Z $\tau = I\varepsilon$ (06.03): $I\ddot\theta = -mgd\sin\theta$, więc

$$T = 2\pi\sqrt{\frac{I}{mgd}}.$$

**Długość zredukowana** $l_{\text{zr}} = I/(md)$ — długość wahadła matematycznego o tym samym okresie.

**Wahadło torsyjne** — bryła zawieszona na drucie, który skręcony o kąt $\theta$ działa momentem $\tau = -\kappa\theta$:

$$T = 2\pi\sqrt{\frac{I}{\kappa}}.$$

Tu nie trzeba przybliżenia małych kątów (dopóki drut spełnia prawo Hooke'a).

**Duże wychylenia.** Okres rośnie z amplitudą: $T \approx T_0\left(1 + \dfrac{\theta_0^2}{16}\right)$; dla $60^\circ$ o ok. 7%. Dokładny wynik wymaga całki eliptycznej.

## Wzory i założenia

| Wzór | Znaczenie | Kiedy obowiązuje |
|---|---|---|
| $T = 2\pi\sqrt{l/g}$ | wahadło matematyczne | małe kąty ($\lesssim 10^\circ$–$15^\circ$) |
| $T = 2\pi\sqrt{I/(mgd)}$ | wahadło fizyczne | małe kąty; $I$ względem osi obrotu |
| $T = 2\pi\sqrt{I/\kappa}$ | wahadło torsyjne | prawo Hooke'a dla skręcania |
| $T \approx T_0(1 + \theta_0^2/16)$ | poprawka na amplitudę | $\theta_0$ w radianach, umiarkowane kąty |
| $T = 2\pi\sqrt{l/g_{\text{ef}}}$ | wahadło w układzie przyspieszającym | $\vec g_{\text{ef}} = \vec g - \vec A$ (03.06) |

## Przykład rozwiązany

**Zadanie 1.** Oblicz okres wahadła o długości 1 m na Ziemi i na Księżycu ($g_K = 1{,}62\ \mathrm{m/s^2}$). Jaka jest długość „wahadła sekundowego” (półokres 1 s)?

$T_Z = 2\pi\sqrt{1/9{,}81} \approx 2{,}01\ \mathrm{s}$, $T_K \approx 4{,}94\ \mathrm{s}$. Dla $T = 2\ \mathrm{s}$: $l = gT^2/(4\pi^2) \approx 0{,}994\ \mathrm{m}$.

**Zadanie 2.** Jednorodny pręt o długości 1 m waha się wokół osi przechodzącej przez jego koniec. Oblicz okres.

$I = \tfrac13mL^2$, $d = L/2$: $T = 2\pi\sqrt{\dfrac{2L}{3g}} \approx 1{,}64\ \mathrm{s}$ — jak wahadło matematyczne o długości $\tfrac23L$.

### Wersja z rachunkiem różniczkowym i całkowym

**Zadanie.** Oblicz dokładny okres wahadła matematycznego wychylonego o $\theta_0 = 60^\circ$.

Z zasady zachowania energii: $\tfrac12ml^2\dot\theta^2 = mgl(\cos\theta - \cos\theta_0)$, więc

$$T = 4\int_0^{\theta_0}\frac{d\theta}{\dot\theta} = 4\sqrt{\frac{l}{2g}}\int_0^{\theta_0}\frac{d\theta}{\sqrt{\cos\theta - \cos\theta_0}} = T_0\cdot\frac2\pi K\!\left(\sin^2\frac{\theta_0}{2}\right),$$

gdzie $K$ to pełna całka eliptyczna pierwszego rodzaju. Dla $60^\circ$: $T/T_0 \approx 1{,}073$ (przybliżenie $1 + \theta_0^2/16$ daje 1,069).

## Typowe pułapki

- **Okres zależy od masy.** Dla wahadła matematycznego nie.
- **$T = 2\pi\sqrt{l/g}$ dla dużych kątów.** Przy $45^\circ$ błąd przekracza 4%.
- **Długość do punktu zaczepienia ciężarka.** Mierzy się do środka masy ciężarka.
- **Moment bezwładności względem środka masy w wahadle fizycznym.** We wzorze jest moment względem **osi obrotu** (Steiner).
- **Wahadło w windzie lub samochodzie.** Liczy się efektywne $g$.

## Doświadczenie / symulacja

**$g$ z wahadła.** To projekt modułu 01 — wykonaj go z telefonem jako wahadłem (phyphox, *Pendulum*), mierząc dla kilku długości i dopasowując $T^2(l)$.

**Okres a amplituda.** Zmierz okres tego samego wahadła dla amplitud $10^\circ$, $30^\circ$, $50^\circ$, $70^\circ$ i porównaj z poprawką $1 + \theta_0^2/16$ i z wynikiem dokładnym (kod poniżej).

**Symulacja PhET:** *Laboratorium wahadła* (*Pendulum Lab*, [phet.colorado.edu/pl](https://phet.colorado.edu/pl/)).

**Python:** okres w funkcji amplitudy — całka eliptyczna, przybliżenie i symulacja numeryczna.

```python
import numpy as np
import matplotlib.pyplot as plt
from scipy.special import ellipk
from scipy.integrate import solve_ivp

g, l = 9.81, 1.0
T0 = 2*np.pi*np.sqrt(l/g)
th0 = np.radians(np.linspace(1, 170, 200))
T_exact = T0*2/np.pi*ellipk(np.sin(th0/2)**2)

def period_numeric(theta0):
    ev = lambda t, s: s[0]; ev.direction = -1          # pierwsze przejście przez θ = 0 to ćwierć okresu
    sol = solve_ivp(lambda t, s: [s[1], -g/l*np.sin(s[0])], (0, 10*T0), [theta0, 0], events=ev, rtol=1e-10, atol=1e-12)
    return 4*sol.t_events[0][0]
for d in (10, 30, 60, 90):
    print(f"{d:3d}°: dokładnie {T0*2/np.pi*ellipk(np.sin(np.radians(d)/2)**2)/T0:.4f} T0, "
          f"numerycznie {period_numeric(np.radians(d))/T0:.4f} T0, przybliżenie {1 + np.radians(d)**2/16:.4f} T0")

plt.plot(np.degrees(th0), T_exact/T0, label="dokładnie"); plt.plot(np.degrees(th0), 1 + th0**2/16, "--", label="1 + θ²/16")
plt.xlabel("amplituda [°]"); plt.ylabel("T / T0"); plt.ylim(1, 2.5); plt.grid(True); plt.legend(); plt.show()
```

## Zadania

### A. Poziom maturalny

1. Jaką długość ma wahadło matematyczne o okresie 1 s?

<details>
<summary>Odpowiedź</summary>

$l = gT^2/(4\pi^2) \approx 24{,}8\ \mathrm{cm}$.
</details>

2. Zegar wahadłowy przeniesiono z Ziemi na Księżyc. Ile razy wolniej będzie chodził?

<details>
<summary>Odpowiedź</summary>

$\sqrt{9{,}81/1{,}62} \approx 2{,}46$ razy.
</details>

3. Wahadło o długości 1 m wisi w windzie przyspieszającej w górę z przyspieszeniem $2\ \mathrm{m/s^2}$. Oblicz okres.

<details>
<summary>Odpowiedź</summary>

$T = 2\pi\sqrt{l/(g + a)} \approx 1{,}83\ \mathrm{s}$.
</details>

4. Latem pręt wahadła zegara się wydłuża. Czy zegar się spieszy, czy spóźnia?

<details>
<summary>Odpowiedź</summary>

Spóźnia — okres rośnie z długością (11.01, zadanie B).
</details>

### B. Poziom akademicki

1. Obręcz o promieniu $R$ zawieszona na gwoździu waha się w swojej płaszczyźnie. Oblicz okres. Jakiej długości wahadło matematyczne ma ten sam okres?

<details>
<summary>Odpowiedź</summary>

$I = MR^2 + MR^2 = 2MR^2$, $d = R$: $T = 2\pi\sqrt{2R/g}$ — jak wahadło o długości $2R$ (średnica obręczy).
</details>

2. Tarcza o masie 0,5 kg i promieniu 10 cm wisi na drucie o stałej skręcania $\kappa = 0{,}01\ \mathrm{N\cdot m/rad}$ (oś drutu przechodzi przez środek tarczy, prostopadle do niej). Oblicz okres drgań skrętnych.

<details>
<summary>Odpowiedź</summary>

$I = \tfrac12\cdot0{,}5\cdot0{,}01 = 0{,}0025\ \mathrm{kg\cdot m^2}$; $T = 2\pi\sqrt{0{,}25} \approx 3{,}14\ \mathrm{s}$.
</details>

3. Pręt o długości $L$ waha się wokół osi odległej o $d$ od środka. Dla jakiego $d$ okres jest najmniejszy i ile wynosi?

<details>
<summary>Odpowiedź</summary>

$T = 2\pi\sqrt{\dfrac{L^2/12 + d^2}{gd}}$, minimum dla $d = L/\sqrt{12}$: $T_{\min} = 2\pi\sqrt{\dfrac{L}{\sqrt3g}}$; dla $L = 1\ \mathrm{m}$ ok. 1,52 s.
</details>

4. Oblicz okres wahadła o długości 1 m przy amplitudzie $60^\circ$ i porównaj z przybliżeniem małych kątów.

<details>
<summary>Odpowiedź</summary>

$T \approx 1{,}073\cdot2{,}006 \approx 2{,}15\ \mathrm{s}$ wobec $2{,}01\ \mathrm{s}$.
</details>

## Źródła

- OpenStax, *Fizyka dla szkół wyższych*, t. 1, rozdz. 15 — §15.4: wahadło matematyczne, fizyczne i torsyjne.
- Halliday, Resnick, Walker, *Podstawy fizyki* — wyd. 2015: t. 2, §15.3–15.4; wyd. 1: t. 2, §16.5–16.6.
- Symulacja PhET *Laboratorium wahadła*.
