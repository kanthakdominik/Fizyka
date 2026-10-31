# 28.04 — Funkcja Hamiltona, równania Hamiltona i przestrzeń fazowa

> **Moduł:** [28 — Mechanika analityczna (wstęp)](README.md) · **Poziom:** 🔵 studia · **Status:** ✅ pełny
>
> **Czytaj:**
>
> - _Podręczniki główne nie mają osobnego paragrafu na ten temat — materiały są w sekcji „Źródła”._

← [Symetrie i prawa zachowania — twierdzenie Noether](03-symetrie-i-prawa-zachowania.md) · [spis modułu](README.md) · [Małe drgania i drgania sprzężone — mody normalne](05-mody-normalne.md) →

## Po co to jest

Sformułowanie Hamiltona opisuje ruch nie przez położenie i prędkość, ale przez położenie i pęd, a równania drugiego rzędu zamienia na pary równań pierwszego rzędu. Stan układu to punkt w **przestrzeni fazowej**, a ruch — przepływ tego punktu. Z tego obrazu wyrastają: mechanika kwantowa (hamiltonian staje się operatorem energii w równaniu Schrödingera, 20.06), fizyka statystyczna (objętość w przestrzeni fazowej liczy mikrostany, 27.01), teoria chaosu i stabilności, a także metody numeryczne zachowujące strukturę ruchu (metody symplektyczne, 25.02). Portret fazowy pozwala zrozumieć ruch wahadła czy oscylatora bez rozwiązywania równań.

## Teoria w pigułce

**Pędy kanoniczne i hamiltonian.** Z lagranżjanu definiujemy pędy $p_i = \partial L/\partial\dot q_i$ (28.03) i **funkcję Hamiltona** (hamiltonian)

$$H(q, p, t) = \sum_ip_i\dot q_i - L,$$

wyrażoną przez $q$ i $p$ (a nie przez $\dot q$). Dla typowych układów mechanicznych $H = E_k + E_p$ — energia całkowita zapisana przez pędy, np. $H = \dfrac{p^2}{2m} + V(x)$.

**Równania Hamiltona:**

$$\dot q_i = \frac{\partial H}{\partial p_i}, \qquad \dot p_i = -\frac{\partial H}{\partial q_i}.$$

Dla $H = p^2/2m + V(x)$: $\dot x = p/m$ (definicja pędu) i $\dot p = -V'(x) = F$ (druga zasada dynamiki). Zamiast jednego równania drugiego rzędu mamy dwa pierwszego — dokładnie w tej postaci rozwiązuje się je numerycznie (25.02).

**Przestrzeń fazowa.** Stan układu o $n$ stopniach swobody to punkt w $2n$-wymiarowej przestrzeni $(q_1, \dots, q_n, p_1, \dots, p_n)$. Przez każdy punkt przechodzi dokładnie jedna trajektoria (deterministyczność), więc trajektorie się nie przecinają. Jeśli $H$ nie zależy od czasu, jest zachowany, a trajektorie leżą na „poziomicach” $H(q, p) = E$.

**Portrety fazowe:**
- **oscylator harmoniczny** $H = \dfrac{p^2}{2m} + \tfrac12m\omega^2x^2$: elipsy; pole elipsy to $2\pi E/\omega$;
- **wahadło** $H = \dfrac{p_\theta^2}{2ml^2} - mgl\cos\theta$: wokół $\theta = 0$ zamknięte krzywe (drgania), dla dużych energii krzywe otwarte (obroty — wahadło „kręci się” dookoła), a między nimi **separatrysa** ($E = mgl$) przechodząca przez niestabilne położenie odwrócone $\theta = \pi$;
- **cząstka swobodna**: proste poziome ($p = \text{const}$).

**Twierdzenie Liouville'a.** Zbiór punktów w przestrzeni fazowej (np. wiele kopii układu o nieco różnych warunkach początkowych) przemieszcza się jak nieściśliwa ciecz: jego objętość jest stała, choć kształt może się dowolnie odkształcać. Konsekwencje:
- w fizyce statystycznej objętość w przestrzeni fazowej to sensowna miara liczby stanów (27.01);
- metody numeryczne, które zachowują pole w przestrzeni fazowej (Verlet, Euler–Cromer — **symplektyczne**), nie mają systematycznego dryfu energii, a metoda Eulera — tak (25.02);
- w układach chaotycznych mała kropla w przestrzeni fazowej zachowuje objętość, ale rozciąga się w długie nitki — stąd nieprzewidywalność.

**Most do mechaniki kwantowej.** W mechanice kwantowej $q$ i $p$ stają się operatorami, $\hat p = -i\hbar\,\partial/\partial x$, a hamiltonian — operatorem energii: $\hat H\psi = E\psi$ (20.06). Pole w przestrzeni fazowej przypadające na jeden stan kwantowy to $h$ (stała Plancka) — stąd liczba stanów w fizyce statystycznej i zasada nieoznaczoności (20.05).

## Wzory i założenia

| Wzór | Znaczenie | Kiedy obowiązuje |
|---|---|---|
| $p_i = \partial L/\partial\dot q_i$ | pęd kanoniczny | — |
| $H = \sum p_i\dot q_i - L$ | hamiltonian | wyrażony przez $q$, $p$ |
| $\dot q_i = \partial H/\partial p_i$, $\dot p_i = -\partial H/\partial q_i$ | równania Hamiltona | — |
| $dH/dt = \partial H/\partial t$ | zachowanie $H$ | $H = \text{const}$, gdy nie zależy jawnie od $t$ |
| $H = \dfrac{p^2}{2m} + V(x)$ | cząstka w potencjale | — |
| $\oint p\,dq = 2\pi E/\omega$ | pole elipsy fazowej oscylatora | oscylator harmoniczny |

## Przykład rozwiązany

**Zadanie.** Wahadło matematyczne ($m$, $l$). Zapisz hamiltonian, równania Hamiltona i znajdź energię separatrysy. Jaką największą prędkość kątową ma wahadło na separatrysie?

$L = \tfrac12ml^2\dot\theta^2 + mgl\cos\theta$, $p_\theta = ml^2\dot\theta$,

$$H = \frac{p_\theta^2}{2ml^2} - mgl\cos\theta, \qquad \dot\theta = \frac{p_\theta}{ml^2}, \qquad \dot p_\theta = -mgl\sin\theta.$$

Separatrysa przechodzi przez punkt $\theta = \pi$, $p_\theta = 0$: $E_s = mgl$. Najszybciej wahadło porusza się w $\theta = 0$: $\dfrac{p^2}{2ml^2} = 2mgl \Rightarrow \dot\theta_{\max} = 2\sqrt{g/l}$. Wahadło na separatrysie zbliża się do pozycji odwróconej nieskończenie długo.

### Wersja z rachunkiem różniczkowym i całkowym

**Wyprowadzenie równań Hamiltona.** Różniczka $H(q, p) = p\dot q - L(q, \dot q)$:

$$dH = \dot q\,dp + p\,d\dot q - \frac{\partial L}{\partial q}dq - \frac{\partial L}{\partial\dot q}d\dot q = \dot q\,dp - \dot p\,dq.$$

Wyrazy z $d\dot q$ skróciły się, bo $p = \partial L/\partial\dot q$, a $\partial L/\partial q = \dot p$ z równania Lagrange'a. Porównując z $dH = \dfrac{\partial H}{\partial q}dq + \dfrac{\partial H}{\partial p}dp$, dostajemy równania Hamiltona.

**Twierdzenie Liouville'a (wersja jednowymiarowa).** Pole prędkości w przestrzeni fazowej $\vec u = (\dot q, \dot p) = (\partial H/\partial p, -\partial H/\partial q)$ ma zerową dywergencję:

$$\frac{\partial\dot q}{\partial q} + \frac{\partial\dot p}{\partial p} = \frac{\partial^2H}{\partial q\partial p} - \frac{\partial^2H}{\partial p\partial q} = 0.$$

Przepływ o zerowej dywergencji zachowuje pole (objętość), tak jak przepływ cieczy nieściśliwej (08.03). Dla metody Eulera jakobian kroku $(q, p) \to (q + hp, p - hV'(q))$ to $1 + h^2V''(q) \ne 1$, więc pole rośnie; dla metody Verleta jakobian jest równy dokładnie 1.

## Typowe pułapki

- **$H$ wyrażony przez prędkości.** Hamiltonian musi być funkcją $q$ i $p$. $H = \tfrac12mv^2 + V$ to energia, ale żeby użyć równań Hamiltona, trzeba podstawić $v = p/m$.
- **Pęd kanoniczny = $mv$.** Nie zawsze. Dla współrzędnej kątowej to moment pędu, a dla ładunku w polu magnetycznym $\vec p = m\vec v + q\vec A$ (z potencjałem wektorowym).
- **Hamiltonian = energia zawsze.** Gdy więzy zależą od czasu albo lagranżjan zawiera wyrazy liniowe w prędkościach (układ obracający się), $H$ może różnić się od energii (28.03).
- **Trajektorie w przestrzeni fazowej się przecinają.** Dla układu z $H$ niezależnym od czasu — nigdy; przecięcie oznaczałoby dwa różne ruchy z tego samego stanu.

## Doświadczenie / symulacja

**Portret fazowy z pomiaru.** Zawieś telefon jako wahadło (sztywny pręt lub dwie nici) i nagraj w phyphox żyroskop (prędkość kątowa) przez kilka okresów. Scałkuj prędkość kątową numerycznie do kąta (25.01) i narysuj $\dot\theta$ od $\theta$. Dla małych drgań wyjdzie elipsa, a z tłumieniem — spirala zbiegająca do punktu równowagi.

**Python:** portret fazowy wahadła (poziomice hamiltonianu, separatrysa) i test twierdzenia Liouville'a — ewolucja okręgu warunków początkowych metodą Eulera i Verleta.

```python
import numpy as np
import matplotlib.pyplot as plt

H = lambda q, p: p**2/2 - np.cos(q)                          # wahadło w jednostkach g/l = 1, ml² = 1
Q, P = np.meshgrid(np.linspace(-2*np.pi, 2*np.pi, 400), np.linspace(-3, 3, 300))
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(13, 4.5))
ax1.contour(Q, P, H(Q, P), levels=np.linspace(-0.95, 2.5, 15), colors="gray", linewidths=0.7)
ax1.contour(Q, P, H(Q, P), levels=[1.0], colors="r")         # separatrysa: E = mgl
ax1.set_xlabel("θ"); ax1.set_ylabel("p_θ"); ax1.set_title("portret fazowy wahadła (czerwona: separatrysa)")
print(f"maks. prędkość kątowa na separatrysie: {np.sqrt(2*(1 - H(0, 0))):.3f} √(g/l) (teoria 2)")

def euler(q, p, h):  return q + h*p, p - h*np.sin(q)
def verlet(q, p, h):
    p = p - 0.5*h*np.sin(q); q = q + h*p
    return q, p - 0.5*h*np.sin(q)
pole = lambda q, p: 0.5*abs(np.dot(q, np.roll(p, -1)) - np.dot(p, np.roll(q, -1)))   # wzór na pole wielokąta

phi = np.linspace(0, 2*np.pi, 400, endpoint=False)
for nazwa, krok, styl in [("Euler", euler, "b"), ("Verlet", verlet, "g")]:
    q, p = 1 + 0.15*np.cos(phi), 0.15*np.sin(phi)
    A0 = pole(q, p)
    for n in range(1, 1201):
        q, p = krok(q, p, 0.05)
        if n % 300 == 0:
            ax2.plot(q, p, styl, lw=0.8)
    print(f"{nazwa:6s}: pole zbioru po 1200 krokach / pole początkowe = {pole(q, p)/A0:.4f}")
ax2.set_xlabel("θ"); ax2.set_ylabel("p_θ"); ax2.set_title("zbiór stanów: Euler (niebieski) i Verlet (zielony)")
plt.tight_layout(); plt.show()
```

## Zadania

### A. Poziom maturalny _(opcjonalnie — rozgrzewka)_

1. Zapisz energię całkowitą ciężarka na sprężynie jako funkcję położenia $x$ i pędu $p$. Jak wygląda wykres $p(x)$ dla stałej energii?

<details>
<summary>Odpowiedź</summary>

$E = \dfrac{p^2}{2m} + \dfrac{kx^2}{2}$. Dla stałego $E$ to elipsa o półosiach $\sqrt{2E/k}$ (amplituda) i $\sqrt{2mE}$ (pęd maksymalny).
</details>

2. Wahadło ma długość 1 m. Z jaką najmniejszą prędkością trzeba popchnąć ciężarek w najniższym położeniu (na sztywnym pręcie), żeby wykonał pełny obrót?

<details>
<summary>Odpowiedź</summary>

Energia musi przekroczyć energię separatrysy: $\tfrac12mv^2 > 2mgl$, $v > 2\sqrt{gl} \approx 6{,}3\ \mathrm{m/s}$ (na nici potrzeba więcej, bo nić musi być napięta w górnym punkcie).
</details>

### B. Poziom akademicki

1. Dla oscylatora harmonicznego oblicz pole elipsy fazowej $\oint p\,dx$ i pokaż, że wynosi $2\pi E/\omega$. Co daje warunek kwantowania Bohra–Sommerfelda $\oint p\,dx = nh$?

<details>
<summary>Odpowiedź</summary>

Półosie $a = \sqrt{2E/(m\omega^2)}$, $b = \sqrt{2mE}$; pole $\pi ab = 2\pi E/\omega$. Z $2\pi E/\omega = nh$: $E_n = n\hbar\omega$ — poziomy oscylatora kwantowego (z dokładnością do energii zerowej $\tfrac12\hbar\omega$, 20.06).
</details>

2. Cząstka o masie $m$ w polu centralnym: zapisz hamiltonian we współrzędnych biegunowych i równania Hamiltona. Które z nich wyraża zachowanie momentu pędu?

<details>
<summary>Odpowiedź</summary>

$H = \dfrac{p_r^2}{2m} + \dfrac{p_\varphi^2}{2mr^2} + V(r)$. $\dot r = p_r/m$, $\dot\varphi = p_\varphi/(mr^2)$, $\dot p_r = \dfrac{p_\varphi^2}{mr^3} - V'(r)$, $\dot p_\varphi = -\partial H/\partial\varphi = 0$ — zachowanie momentu pędu.
</details>

3. Pokaż, że jakobian jednego kroku metody Verleta (w wersji „pół kroku pędu — krok położenia — pół kroku pędu”) jest równy 1. Uruchom kod i sprawdź, jak zmienia się pole zbioru stanów dla metody Eulera.

<details>
<summary>Odpowiedź</summary>

Każdy z trzech etapów to przesunięcie jednej współrzędnej o funkcję drugiej (np. $p \to p - \tfrac h2V'(q)$ przy stałym $q$), a takie „ścinanie” ma jakobian 1. Złożenie ma jakobian 1. W kodzie Verlet zachowuje pole z dokładnością ok. $10^{-4}$, a metoda Eulera powiększa je kilkadziesiąt razy (ok. 70 razy po 1200 krokach).
</details>

## Źródła

- W. Wojtyński, *Matematyczne metody mechaniki*, skrypt MIMUW (rozdz. 10–11: mechanika hamiltonowska) — [mst.mimuw.edu.pl](https://mst.mimuw.edu.pl/wyklady/mmk/wyklad.pdf).
- J. R. Taylor, *Mechanika klasyczna*, PWN — rozdział o mechanice Hamiltona i przestrzeni fazowej.
- S. Charzyński, K. Turzyński, *Mechanika analityczna*, „Delta” 9/2016 — [artykuł po polsku](https://deltami-old.mimuw.edu.pl/temat/fizyka/mechanika/2016/09/03/1609delta-mechanika-analityczna.pdf).
- Moduły 09.03 (wahadło), 20.06 (równanie Schrödingera), 25.02 (metody symplektyczne), 27.01 (mikrostany).
