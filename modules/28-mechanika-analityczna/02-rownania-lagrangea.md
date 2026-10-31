# 28.02 — Więzy, współrzędne uogólnione i równania Lagrange'a

> **Moduł:** [28 — Mechanika analityczna (wstęp)](README.md) · **Poziom:** 🔵 studia · **Status:** ✅ pełny
>
> **Czytaj:**
>
> - _Podręczniki główne nie mają osobnego paragrafu na ten temat — materiały są w sekcji „Źródła”._

← [Rachunek wariacyjny i zasada najmniejszego działania](01-zasada-najmniejszego-dzialania.md) · [spis modułu](README.md) · [Symetrie i prawa zachowania — twierdzenie Noether](03-symetrie-i-prawa-zachowania.md) →

## Po co to jest

Rozwiązywanie zadań z równią, bloczkami czy wahadłami metodą sił (03.02) wymaga wyznaczania sił reakcji, których w ogóle nie potrzebujemy — nacisku podłoża, naciągu nici, siły od prowadnicy. Mechanika Lagrange'a omija je: wybieramy współrzędne, które automatycznie uwzględniają więzy (kąt wahadła zamiast $x$ i $y$), zapisujemy energię kinetyczną i potencjalną, a równania ruchu wychodzą mechanicznie z jednego wzoru. Dla układów takich jak wahadło podwójne, koralik na obracającym się okręgu czy bąk metoda sił jest bardzo uciążliwa, a metoda Lagrange'a — rutynowa. W ten sposób programy do symulacji robotów i mechanizmów wyprowadzają równania ruchu.

## Teoria w pigułce

**Więzy i stopnie swobody.** Punkt w przestrzeni ma 3 stopnie swobody, układ $N$ punktów — $3N$. **Więzy** to warunki ograniczające ruch: nić o stałej długości, ruch po powierzchni, sztywne pręty. Każdy więz typu „równanie wiążące współrzędne” (więz holonomiczny) usuwa jeden stopień swobody. Wahadło matematyczne w płaszczyźnie: 2 współrzędne $(x, y)$, jeden więz $x^2 + y^2 = l^2$ — jeden stopień swobody.

**Współrzędne uogólnione** $q_1, \dots, q_n$ to dowolny zestaw liczb jednoznacznie opisujący konfigurację, w liczbie równej liczbie stopni swobody. Mogą to być kąty, odległości, długości łuku. Dla wahadła — kąt $\theta$.

**Równania Lagrange'a.** Zapisz lagranżjan $L(q, \dot q, t) = E_k - E_p$ we współrzędnych uogólnionych. Dla każdej współrzędnej

$$\frac{d}{dt}\frac{\partial L}{\partial\dot q_i} - \frac{\partial L}{\partial q_i} = 0.$$

To równania Eulera–Lagrange'a z zasady najmniejszego działania (28.01). Siły więzów (naciąg nici, reakcja prowadnicy) nie wykonują pracy przy ruchu zgodnym z więzami i nie pojawiają się w równaniach.

**Przepis:**
1. Wybierz współrzędne uogólnione (tyle, ile stopni swobody).
2. Wyraź położenia wszystkich mas przez $q_i$, oblicz prędkości.
3. Zapisz $E_k$ i $E_p$, potem $L = E_k - E_p$.
4. Oblicz pochodne i zapisz równania Lagrange'a.
5. Rozwiąż (analitycznie dla małych drgań, numerycznie w ogólnym przypadku, 25.02).

**Przykłady:**
- **Wahadło:** $x = l\sin\theta$, $y = -l\cos\theta$; $L = \tfrac12ml^2\dot\theta^2 + mgl\cos\theta$; równanie: $ml^2\ddot\theta + mgl\sin\theta = 0$ — znane równanie wahadła (09.03) bez liczenia naciągu nici.
- **Maszyna Atwooda:** masy $m_1$, $m_2$ na nici przez bloczek. Jedna współrzędna $x$ (przesunięcie $m_1$ w dół). $L = \tfrac12(m_1 + m_2)\dot x^2 + (m_1 - m_2)gx$, skąd $a = \dfrac{m_1 - m_2}{m_1 + m_2}g$.
- **Koralik na obracającym się okręgu** (promień $R$, prędkość kątowa $\omega$ wokół pionowej średnicy): $L = \tfrac12mR^2(\dot\theta^2 + \omega^2\sin^2\theta) + mgR\cos\theta$. Dla $\omega^2 < g/R$ koralik spoczywa na dole, dla szybszego obrotu przesuwa się w górę do $\cos\theta_0 = g/(\omega^2R)$ — przykład **bifurkacji**.
- **Wahadło podwójne:** dwa kąty, równania nieliniowe i sprzężone. Dla małych wychyleń dwa mody drgań (28.05), dla dużych — chaos (25.03).

**Siły niezachowawcze** (tarcie, opór) dodaje się po prawej stronie jako siły uogólnione $Q_i$: $\dfrac{d}{dt}\dfrac{\partial L}{\partial\dot q_i} - \dfrac{\partial L}{\partial q_i} = Q_i$.

## Wzory i założenia

| Wzór | Znaczenie | Kiedy obowiązuje |
|---|---|---|
| $n = 3N - k$ | liczba stopni swobody | $N$ punktów, $k$ więzów holonomicznych |
| $L(q, \dot q, t) = E_k - E_p$ | lagranżjan | siły zachowawcze |
| $\dfrac{d}{dt}\dfrac{\partial L}{\partial\dot q_i} - \dfrac{\partial L}{\partial q_i} = Q_i$ | równania Lagrange'a | $Q_i$ — siły niezachowawcze (0, gdy ich brak) |
| $E_k = \tfrac12\sum m_j\dot{\vec r}_j^2$, $\vec r_j = \vec r_j(q_1, \dots, q_n, t)$ | energia kinetyczna przez $q_i$ | — |
| $\cos\theta_0 = g/(\omega^2R)$ | położenie koralika na okręgu | $\omega^2 > g/R$ |

## Przykład rozwiązany

**Zadanie.** Wyprowadź równanie ruchu wahadła, którego punkt zawieszenia porusza się poziomo zgodnie z $x_0(t) = A\cos\Omega t$.

Położenie masy: $x = x_0 + l\sin\theta$, $y = -l\cos\theta$. Prędkość: $\dot x = \dot x_0 + l\cos\theta\,\dot\theta$, $\dot y = l\sin\theta\,\dot\theta$.

$$L = \tfrac12m\left(\dot x_0^2 + 2\dot x_0l\cos\theta\,\dot\theta + l^2\dot\theta^2\right) + mgl\cos\theta.$$

$\dfrac{\partial L}{\partial\dot\theta} = ml\dot x_0\cos\theta + ml^2\dot\theta$, $\dfrac{\partial L}{\partial\theta} = -ml\dot x_0\sin\theta\,\dot\theta - mgl\sin\theta$. Po zróżniczkowaniu i uproszczeniu:

$$l\ddot\theta + g\sin\theta = -\ddot x_0\cos\theta = A\Omega^2\cos\Omega t\cos\theta.$$

Ruch zawieszenia działa jak siła wymuszająca (09.05) — w układzie zawieszenia to siła bezwładności (03.06). Metodą sił trzeba by uwzględnić naciąg nici i przejść do układu nieinercjalnego.

### Wersja z rachunkiem różniczkowym i całkowym

**Koralik na obracającym się okręgu — stabilność.** Równanie Lagrange'a:

$$mR^2\ddot\theta = mR^2\omega^2\sin\theta\cos\theta - mgR\sin\theta.$$

Położenia równowagi: $\sin\theta = 0$ ($\theta = 0$ lub $\pi$) albo $\cos\theta_0 = g/(\omega^2R)$. Dla małego odchylenia $\theta = \theta_0 + \varepsilon$ linearyzujemy prawą stronę: $\ddot\varepsilon = -\Omega^2\varepsilon$ z

$$\Omega^2 = \frac gR\cos\theta_0 - \omega^2\cos2\theta_0.$$

Dla $\theta_0 = 0$: $\Omega^2 = g/R - \omega^2$ — stabilne tylko dla $\omega^2 < g/R$. Dla $\cos\theta_0 = g/(\omega^2R)$: $\Omega^2 = \omega^2\sin^2\theta_0 > 0$ — stabilne. Dla $R = 0{,}2\ \mathrm m$ i $\omega = 10\ \mathrm{rad/s}$: $\theta_0 = 60{,}6°$, częstość drgań wokół niego $8{,}7\ \mathrm{rad/s}$.

## Typowe pułapki

- **Za dużo współrzędnych.** Współrzędnych uogólnionych ma być tyle, ile stopni swobody. Jeśli użyjesz $x$, $y$ i $\theta$ dla wahadła, musisz dołożyć więzy (mnożniki Lagrange'a).
- **Energia kinetyczna w ruchomym układzie.** Prędkość trzeba liczyć względem układu inercjalnego (uwzględniając ruch zawieszenia, obrót okręgu), a nie względem ruchomego elementu.
- **Pochodna $d/dt$ zamiast $\partial/\partial t$.** W $\dfrac{d}{dt}\dfrac{\partial L}{\partial\dot q}$ różniczkujemy po czasie z uwzględnieniem tego, że $q$ i $\dot q$ zależą od czasu (pochodna zupełna).
- **Tarcie w lagranżjanie.** Siły niezachowawczej nie da się zapisać jako energii potencjalnej — dopisuje się ją jako siłę uogólnioną $Q_i$.

## Doświadczenie / symulacja

**Wahadło z ruchomym zawieszeniem.** Trzymaj w palcach nitkę z ciężarkiem i poruszaj ręką poziomo z różnymi częstotliwościami. Przy częstotliwości bliskiej własnej ($\sqrt{g/l}$) amplituda gwałtownie rośnie — rezonans opisany wyprowadzonym równaniem. Ruch ręki możesz nagrać telefonem i porównać z symulacją.

**Wahadło podwójne.** Zrób wahadło z dwóch linijek połączonych śrubką (oś obrotu na łożysku lub nicie). Puść z dużego wychylenia kilka razy z „tego samego” położenia i nagraj — tory szybko się rozchodzą.

**Python:** wahadło podwójne z równań Lagrange'a — kontrola zachowania energii, wrażliwość na warunki początkowe przy małej i dużej amplitudzie oraz położenie równowagi koralika na obracającym się okręgu.

```python
import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp

g = 9.81                                                    # wahadło podwójne: m1 = m2 = 1 kg, l1 = l2 = 1 m
def rownania(t, y):
    t1, t2, w1, w2 = y
    d = t1 - t2; mian = 3 - np.cos(2*d)
    a1 = (-3*g*np.sin(t1) - g*np.sin(t1 - 2*t2) - 2*np.sin(d)*(w2**2 + w1**2*np.cos(d)))/mian
    a2 = 2*np.sin(d)*(2*w1**2 + 2*g*np.cos(t1) + w2**2*np.cos(d))/mian
    return [w1, w2, a1, a2]
energia = lambda y: y[2]**2 + 0.5*y[3]**2 + y[2]*y[3]*np.cos(y[0] - y[1]) - 2*g*np.cos(y[0]) - g*np.cos(y[1])

t = np.linspace(0, 20, 2001)
fig, ax = plt.subplots(1, 2, figsize=(12, 4))
for i, kat in enumerate((0.2, 2.0)):
    a = solve_ivp(rownania, [0, 20], [kat, kat, 0, 0], t_eval=t, rtol=1e-11, atol=1e-11)
    b = solve_ivp(rownania, [0, 20], [kat + 1e-6, kat, 0, 0], t_eval=t, rtol=1e-11, atol=1e-11)
    E = energia(a.y)
    roznica = np.abs(a.y[1] - b.y[1])
    print(f"θ0 = {kat} rad: zmiana energii {np.ptp(E):.1e} J, różnica θ2 po 20 s przy zaburzeniu 1e-6 rad: {roznica[-1]:.1e} rad")
    ax[i].plot(t, a.y[1], label="θ2"); ax[i].plot(t, b.y[1], "--", label="θ2 (zaburzone)")
    ax[i].set_title(f"θ1 = θ2 = {kat} rad na starcie"); ax[i].set_xlabel("t [s]"); ax[i].legend()

R = 0.2
for omega in (5, 7, 10, 20):
    th0 = np.degrees(np.arccos(g/(omega**2*R))) if omega**2*R > g else 0.0
    print(f"koralik, R = {R} m, ω = {omega:2d} rad/s: równowaga przy θ0 = {th0:.1f}° (próg ω = {np.sqrt(g/R):.2f} rad/s)")
plt.tight_layout(); plt.show()
```

## Zadania

### A. Poziom maturalny _(opcjonalnie — rozgrzewka)_

1. Ile stopni swobody ma: (a) koralik na sztywnym drucie, (b) wahadło matematyczne w płaszczyźnie, (c) wahadło sferyczne, (d) bryła sztywna swobodna?

<details>
<summary>Odpowiedź</summary>

(a) 1, (b) 1, (c) 2, (d) 6 (3 przesunięcia i 3 obroty).
</details>

2. Rozwiąż maszynę Atwooda dla $m_1 = 3\ \mathrm{kg}$, $m_2 = 2\ \mathrm{kg}$ metodą sił (z naciągiem nici) i porównaj z wynikiem z lagranżjanu.

<details>
<summary>Odpowiedź</summary>

$m_1a = m_1g - N$, $m_2a = N - m_2g$ ⇒ $a = \dfrac{m_1 - m_2}{m_1 + m_2}g = 1{,}96\ \mathrm{m/s^2}$, $N = 23{,}5\ \mathrm N$. Lagranżjan daje to samo przyspieszenie bez wprowadzania $N$.
</details>

### B. Poziom akademicki

1. Klocek o masie $m$ zsuwa się bez tarcia po klinie o masie $M$ i kącie $\alpha$, który może przesuwać się bez tarcia po stole. Wybierz współrzędne uogólnione ($X$ — położenie klina, $s$ — położenie klocka wzdłuż klina), zapisz lagranżjan i wyznacz przyspieszenie klina.

<details>
<summary>Odpowiedź</summary>

$L = \tfrac12M\dot X^2 + \tfrac12m\left[(\dot X + \dot s\cos\alpha)^2 + \dot s^2\sin^2\alpha\right] + mgs\sin\alpha$. Z dwóch równań: $\ddot X = -\dfrac{mg\sin\alpha\cos\alpha}{M + m\sin^2\alpha}$ (klin cofa się).
</details>

2. Zapisz lagranżjan cząstki w polu centralnym $V(r)$ we współrzędnych biegunowych i wyprowadź równania ruchu. Który pęd uogólniony jest zachowany?

<details>
<summary>Odpowiedź</summary>

$L = \tfrac12m(\dot r^2 + r^2\dot\varphi^2) - V(r)$. Równania: $m\ddot r = mr\dot\varphi^2 - V'(r)$, $\dfrac{d}{dt}(mr^2\dot\varphi) = 0$. Zachowany jest $p_\varphi = mr^2\dot\varphi$ — moment pędu (28.03).
</details>

3. Uruchom kod. Po jakim czasie różnica kątów w wahadle podwójnym puszczonym z 2 rad przekracza 0,1 rad przy zaburzeniu $10^{-6}$ rad? Co dzieje się dla 0,2 rad?

<details>
<summary>Odpowiedź</summary>

Dla 2 rad po ok. 11 s (ruch chaotyczny). Dla 0,2 rad różnica pozostaje rzędu $10^{-7}$ — małe drgania są regularne (złożenie dwóch modów normalnych, 28.05).
</details>

## Źródła

- J. R. Taylor, *Mechanika klasyczna*, PWN — rozdział o równaniach Lagrange'a (wiele przykładów z rozwiązaniami).
- W. Wojtyński, *Matematyczne metody mechaniki*, skrypt MIMUW (rozdz. 8: równania Eulera–Lagrange'a) — [mst.mimuw.edu.pl](https://mst.mimuw.edu.pl/wyklady/mmk/wyklad.pdf).
- S. Charzyński, K. Turzyński, *Mechanika analityczna*, „Delta” 9/2016 — [artykuł po polsku](https://deltami-old.mimuw.edu.pl/temat/fizyka/mechanika/2016/09/03/1609delta-mechanika-analityczna.pdf).
- Moduły 03.02 (diagramy sił i więzy), 09.03 (wahadła), 25.03 (wahadło nieliniowe i chaos).
