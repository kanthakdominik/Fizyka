# 28.03 — Symetrie i prawa zachowania — twierdzenie Noether

> **Moduł:** [28 — Mechanika analityczna (wstęp)](README.md) · **Poziom:** 🔵 studia · **Status:** ✅ pełny
>
> **Czytaj:**
>
> - _Podręczniki główne nie mają osobnego paragrafu na ten temat — materiały są w sekcji „Źródła”._

← [Więzy, współrzędne uogólnione i równania Lagrange'a](02-rownania-lagrangea.md) · [spis modułu](README.md) · [Funkcja Hamiltona, równania Hamiltona i przestrzeń fazowa](04-rownania-hamiltona.md) →

## Po co to jest

Dlaczego energia, pęd i moment pędu są zachowane? W fizyce szkolnej to po prostu prawa doświadczalne. Emmy Noether pokazała w 1918 r., że każde z nich wynika z symetrii: energia jest zachowana, bo prawa fizyki nie zmieniają się w czasie, pęd — bo są takie same w każdym miejscu, a moment pędu — bo żaden kierunek nie jest wyróżniony. Twierdzenie Noether to jedna z najgłębszych idei fizyki. Służy do odkrywania nowych praw zachowania (ładunek elektryczny, liczba barionowa, 24.01) i w praktyce pozwala od razu zobaczyć, które wielkości są stałe w danym zagadnieniu, co często wystarcza do jego rozwiązania.

## Teoria w pigułce

**Pęd uogólniony.** Dla współrzędnej uogólnionej $q_i$ definiujemy

$$p_i = \frac{\partial L}{\partial\dot q_i}.$$

Dla współrzędnej kartezjańskiej to zwykły pęd $m\dot x$, dla kąta obrotu — moment pędu $mr^2\dot\varphi$.

**Współrzędna cykliczna.** Jeśli lagranżjan nie zależy od $q_i$ (zależy tylko od $\dot q_i$), równanie Lagrange'a daje

$$\frac{dp_i}{dt} = \frac{\partial L}{\partial q_i} = 0 \Rightarrow p_i = \text{const}.$$

Brak zależności od współrzędnej to symetria: przesunięcie układu wzdłuż $q_i$ nie zmienia jego dynamiki.

**Twierdzenie Noether** (wersja dla mechaniki): każdej ciągłej symetrii lagranżjanu odpowiada wielkość zachowana.

| Symetria | Wielkość zachowana |
|---|---|
| przesunięcie w przestrzeni (jednorodność) | pęd (05.02) |
| obrót (izotropia przestrzeni) | moment pędu (06.05) |
| przesunięcie w czasie | energia (04.05) |
| zmiana fazy funkcji falowej (elektrodynamika) | ładunek elektryczny |

**Energia z symetrii czasu.** Jeśli $L$ nie zależy jawnie od czasu, zachowana jest **funkcja energii** (całka Jacobiego)

$$h = \sum_i\dot q_i\frac{\partial L}{\partial\dot q_i} - L.$$

Dla $L = E_k - E_p$ z $E_k$ kwadratową w prędkościach $h = E_k + E_p$ — energia mechaniczna. Uwaga: gdy więzy zależą od czasu, $h$ może się różnić od energii. Dla koralika na okręgu obracającym się ze stałą prędkością (28.02) zachowane jest $h$, a energia mechaniczna nie — silnik obracający okrąg wykonuje pracę.

**Ruch w polu centralnym.** Lagranżjan $L = \tfrac12m(\dot r^2 + r^2\dot\varphi^2) - V(r)$ nie zależy od $\varphi$ (symetria obrotowa) ani od $t$:
- $p_\varphi = mr^2\dot\varphi = \text{const}$ — moment pędu, czyli II prawo Keplera (pole zakreślane w jednostce czasu $\tfrac12r^2\dot\varphi$ jest stałe, 07.04);
- $E = \tfrac12m\dot r^2 + \dfrac{p_\varphi^2}{2mr^2} + V(r) = \text{const}$.

Ruch radialny jest jak ruch jednowymiarowy w **potencjale efektywnym** $V_{\text{ef}}(r) = V(r) + \dfrac{p_\varphi^2}{2mr^2}$. Drugi wyraz („bariera odśrodkowa”) nie pozwala ciału z niezerowym momentem pędu spaść na centrum. Z wykresu $V_{\text{ef}}$ (04.06) od razu widać, czy orbita jest związana (elipsa), czy nie (hiperbola).

**Symetrie ukryte.** W problemie Keplera ($V \propto -1/r$) zachowany jest jeszcze wektor Laplace'a–Rungego–Lenza — dlatego orbity są zamknięte, a elipsa nie obraca się. Przy innym potencjale (np. poprawka z ogólnej teorii względności) ta symetria znika i peryhelium precesuje (Merkury, 26.04).

## Wzory i założenia

| Wzór | Znaczenie | Kiedy obowiązuje |
|---|---|---|
| $p_i = \partial L/\partial\dot q_i$ | pęd uogólniony | — |
| $\partial L/\partial q_i = 0 \Rightarrow p_i = \text{const}$ | współrzędna cykliczna | — |
| $h = \sum\dot q_i\,\partial L/\partial\dot q_i - L = \text{const}$ | całka Jacobiego (energia) | $L$ nie zależy jawnie od $t$ |
| $h = E_k + E_p$ | — | $E_k$ kwadratowa w $\dot q$, więzy niezależne od czasu |
| $V_{\text{ef}}(r) = V(r) + p_\varphi^2/(2mr^2)$ | potencjał efektywny | pole centralne |
| $\dfrac{dA}{dt} = \dfrac{p_\varphi}{2m}$ | prędkość polowa | II prawo Keplera |

## Przykład rozwiązany

**Zadanie.** Kulka porusza się bez tarcia po wewnętrznej powierzchni stożka o kącie rozwarcia $2\alpha$ (oś pionowa, wierzchołek w dół). Wybierz współrzędne, znajdź wielkości zachowane i warunek ruchu po okręgu na wysokości $z_0$.

Współrzędne: $r$ (odległość od wierzchołka wzdłuż tworzącej) i $\varphi$ (kąt wokół osi). Promień okręgu $\rho = r\sin\alpha$, wysokość $z = r\cos\alpha$:

$$L = \tfrac12m\left(\dot r^2 + r^2\sin^2\alpha\,\dot\varphi^2\right) - mgr\cos\alpha.$$

- $\varphi$ jest cykliczna: $p_\varphi = mr^2\sin^2\alpha\,\dot\varphi = \text{const}$ (moment pędu względem osi).
- $L$ nie zależy od $t$: $E = \tfrac12m\dot r^2 + \dfrac{p_\varphi^2}{2mr^2\sin^2\alpha} + mgr\cos\alpha = \text{const}$.

Ruch po okręgu to minimum potencjału efektywnego: $\dfrac{dV_{\text{ef}}}{dr} = -\dfrac{p_\varphi^2}{mr^3\sin^2\alpha} + mg\cos\alpha = 0$. Wstawiając $p_\varphi$: $r\sin^2\alpha\,\dot\varphi^2 = g\cos\alpha$, czyli $\omega^2 = \dfrac{g\cos\alpha}{r\sin^2\alpha}$. Kulka z większym momentem pędu krąży wyżej.

### Wersja z rachunkiem różniczkowym i całkowym

**Dowód zachowania $h$.** Pochodna zupełna lagranżjanu $L(q, \dot q)$ (bez jawnej zależności od $t$):

$$\frac{dL}{dt} = \sum_i\left(\frac{\partial L}{\partial q_i}\dot q_i + \frac{\partial L}{\partial\dot q_i}\ddot q_i\right) = \sum_i\left(\frac{d}{dt}\frac{\partial L}{\partial\dot q_i}\dot q_i + \frac{\partial L}{\partial\dot q_i}\ddot q_i\right) = \frac{d}{dt}\sum_i\dot q_i\frac{\partial L}{\partial\dot q_i}.$$

W drugim kroku użyliśmy równań Lagrange'a. Stąd $\dfrac{d}{dt}\left(\sum\dot q_i\dfrac{\partial L}{\partial\dot q_i} - L\right) = 0$.

**Moment pędu z symetrii obrotowej.** Obrót o mały kąt $\varepsilon$ wokół osi $z$ zmienia położenia o $\delta\vec r = \varepsilon\hat z\times\vec r$. Jeśli $L$ się nie zmienia: $0 = \delta L = \sum\left(\dfrac{\partial L}{\partial\vec r}\cdot\delta\vec r + \dfrac{\partial L}{\partial\dot{\vec r}}\cdot\delta\dot{\vec r}\right) = \varepsilon\dfrac{d}{dt}\sum\vec p\cdot(\hat z\times\vec r) = \varepsilon\dfrac{d}{dt}\sum(\vec r\times\vec p)_z$. Zachowana jest składowa $z$ momentu pędu.

## Typowe pułapki

- **Energia jest zawsze zachowana.** Całkowita energia izolowanego układu — tak. Ale w opisie z zewnętrznie wymuszonymi więzami (obracający się okrąg, ruchome zawieszenie) energia mechaniczna układu się zmienia, a zachowana jest tylko całka Jacobiego $h$ (o ile istnieje).
- **Pęd uogólniony ma zawsze jednostkę pędu.** Zależy od współrzędnej: dla kąta to moment pędu (J·s).
- **Wystarczy, że układ „wygląda symetrycznie”.** Liczy się symetria lagranżjanu, łącznie z potencjałem. Kulka na stożku ma symetrię obrotową (zachowany $L_z$), ale nie przesunięciową (pęd nie jest zachowany).
- **Wybór współrzędnych nie ma znaczenia.** Ma ogromne: w kartezjańskich nie widać, że moment pędu jest zachowany, bo żadna współrzędna nie jest cykliczna.

## Doświadczenie / symulacja

**Kulka w lejku.** Wpraw kulkę (np. monetę lub kulkę stalową) w ruch po wnętrzu lejka lub miski. Gdy opada ku środkowi, kręci się coraz szybciej — zachowanie momentu pędu, ten sam efekt co piruet łyżwiarki (06.05). Dzięki tarciu powoli traci energię i spiralnie opada (podobnie jak modele „studni grawitacyjnej” w muzeach nauki).

**Python:** orbita w polu centralnym we współrzędnych biegunowych — kontrola zachowania momentu pędu i energii, potencjał efektywny, oraz koralik na obracającym się okręgu, gdzie zachowana jest całka Jacobiego, a energia mechaniczna nie.

```python
import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp

GM = 4*np.pi**2                                             # AU, lata
def orbita(t, y):
    r, phi, vr, w = y
    return [vr, w, r*w**2 - GM/r**2, -2*vr*w/r]             # równania Lagrange'a we współrzędnych biegunowych
s = solve_ivp(orbita, [0, 3], [1, 0, 0, 1.2*2*np.pi], t_eval=np.linspace(0, 3, 600), rtol=1e-11, atol=1e-12)
r, phi, vr, w = s.y
p_phi, E = r**2*w, 0.5*(vr**2 + r**2*w**2) - GM/r
print(f"orbita: p_φ = {p_phi[0]:.4f} (zmiana {np.ptp(p_phi):.1e}), E = {E[0]:.4f} (zmiana {np.ptp(E):.1e})")

g, R, Om = 9.81, 0.2, 10.0                                  # koralik na okręgu obracanym ze stałą ω
def koralik(t, y):
    th, thd = y
    return [thd, Om**2*np.sin(th)*np.cos(th) - g/R*np.sin(th)]
k = solve_ivp(koralik, [0, 5], [0.3, 0], t_eval=np.linspace(0, 5, 500), rtol=1e-11, atol=1e-12)
th, thd = k.y
h = 0.5*R**2*(thd**2 - Om**2*np.sin(th)**2) - g*R*np.cos(th)          # całka Jacobiego (na jednostkę masy)
Em = 0.5*R**2*(thd**2 + Om**2*np.sin(th)**2) - g*R*np.cos(th)         # energia mechaniczna
print(f"koralik: zmiana h = {np.ptp(h):.1e} J/kg, zmiana energii mechanicznej = {np.ptp(Em):.2f} J/kg")

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(11, 4))
rr = np.linspace(0.2, 4, 400)
for L_ in (0.6, 1.0, 1.4):
    pf = L_*2*np.pi
    ax1.plot(rr, -GM/rr + pf**2/(2*rr**2), label=f"p_φ = {L_:.1f}·2π")
ax1.set_ylim(-60, 20); ax1.set_xlabel("r [AU]"); ax1.set_ylabel("V_ef (na jedn. masy)"); ax1.legend(); ax1.grid(True)
ax2.plot(k.t, h - h[0], label="h − h₀"); ax2.plot(k.t, Em - Em[0], label="E − E₀"); ax2.set_xlabel("t [s]"); ax2.legend()
plt.tight_layout(); plt.show()
```

## Zadania

### A. Poziom maturalny _(opcjonalnie — rozgrzewka)_

1. Łyżwiarka kręci się z rozłożonymi rękami z częstotliwością 1 obrotu na sekundę. Po przyciągnięciu rąk jej moment bezwładności maleje trzykrotnie. Z jaką częstotliwością się kręci i dlaczego jej energia kinetyczna wzrosła?

<details>
<summary>Odpowiedź</summary>

$I\omega = \text{const}$: 3 obroty na sekundę. $E_k = \tfrac12I\omega^2$ rośnie 3 razy — łyżwiarka wykonała pracę, przyciągając ręce wbrew „sile odśrodkowej”.
</details>

2. Kometa ma w peryhelium odległość 0,5 AU i prędkość 60 km/s. Jaką prędkość ma w aphelium w odległości 30 AU?

<details>
<summary>Odpowiedź</summary>

Zachowanie momentu pędu ($r\perp v$ w obu punktach): $v_A = 60\cdot0{,}5/30 = 1\ \mathrm{km/s}$.
</details>

### B. Poziom akademicki

1. Cząstka porusza się w polu $V(x, y) = mgy$ (jednorodne pole grawitacyjne). Które składowe pędu są zachowane? Jaka symetria za to odpowiada?

<details>
<summary>Odpowiedź</summary>

$L = \tfrac12m(\dot x^2 + \dot y^2) - mgy$ nie zależy od $x$, więc $p_x = m\dot x$ jest zachowane (jednorodność w kierunku poziomym). $p_y$ nie jest. Zachowana jest też energia (brak jawnej zależności od $t$).
</details>

2. Dla koralika na obracającym się okręgu oblicz $h$ i pokaż, że różni się od energii mechanicznej. Dlaczego energia nie jest zachowana?

<details>
<summary>Odpowiedź</summary>

$h = \tfrac12mR^2(\dot\theta^2 - \omega^2\sin^2\theta) - mgR\cos\theta$, a $E = \tfrac12mR^2(\dot\theta^2 + \omega^2\sin^2\theta) - mgR\cos\theta$. Różnica $mR^2\omega^2\sin^2\theta$ zmienia się w czasie. Napęd utrzymujący stałe $\omega$ wykonuje pracę (moment siły zmienia się, gdy koralik zmienia odległość od osi).
</details>

3. Pokaż, że dla potencjału efektywnego $V_{\text{ef}} = -\dfrac{GMm}{r} + \dfrac{p_\varphi^2}{2mr^2}$ minimum odpowiada orbicie kołowej o prędkości $v = \sqrt{GM/r}$.

<details>
<summary>Odpowiedź</summary>

$V_{\text{ef}}' = \dfrac{GMm}{r^2} - \dfrac{p_\varphi^2}{mr^3} = 0 \Rightarrow p_\varphi^2 = GMm^2r$. Z $p_\varphi = mrv$: $v^2 = GM/r$ (07.03).
</details>

## Źródła

- J. R. Taylor, *Mechanika klasyczna*, PWN — rozdziały o prawach zachowania i ruchu w polu centralnym.
- W. Wojtyński, *Matematyczne metody mechaniki*, skrypt MIMUW (rozdz. 4: symetrie i całki pierwsze; rozdz. 5–6: symetria sferyczna, ruch w polu grawitacyjnym) — [mst.mimuw.edu.pl](https://mst.mimuw.edu.pl/wyklady/mmk/wyklad.pdf).
- Moduły 04.05 (zasada zachowania energii), 05.02 (pędu), 06.05 (momentu pędu), 07.04 (prawa Keplera).
