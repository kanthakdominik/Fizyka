# 28.01 — Rachunek wariacyjny i zasada najmniejszego działania

> **Moduł:** [28 — Mechanika analityczna (wstęp)](README.md) · **Poziom:** 🔵 studia · **Status:** ✅ pełny
>
> **Czytaj:**
>
> - _Podręczniki główne nie mają osobnego paragrafu na ten temat — materiały są w sekcji „Źródła”._

← (początek modułu) · [spis modułu](README.md) · [Więzy, współrzędne uogólnione i równania Lagrange'a](02-rownania-lagrangea.md) →

## Po co to jest

Prawa Newtona mówią, jak ruch zmienia się z chwili na chwilę. Istnieje zupełnie inne, równoważne sformułowanie: spośród wszystkich możliwych ruchów między dwoma położeniami natura wybiera ten, dla którego pewna wielkość — **działanie** — jest najmniejsza (dokładniej: stacjonarna). Z tej jednej zasady wynikają prawa Newtona, prawo załamania światła, równania Maxwella, ogólna teoria względności i mechanika kwantowa (całki po trajektoriach Feynmana). To język całej fizyki teoretycznej i punkt wyjścia do równań Lagrange'a (28.02) i Hamiltona (28.04). Narzędziem jest rachunek wariacyjny — szukanie funkcji, która minimalizuje całkę.

## Teoria w pigułce

**Funkcjonał.** Zwykła funkcja przyporządkowuje liczbie liczbę. **Funkcjonał** przyporządkowuje liczbę całej funkcji, np. długość krzywej $y(x)$ między dwoma punktami albo czas zsuwania się koralika po drucie o kształcie $y(x)$:

$$J[y] = \int_{x_1}^{x_2}F(y, y', x)\,dx.$$

**Rachunek wariacyjny** szuka funkcji $y(x)$ (o ustalonych końcach), dla której $J$ jest ekstremalny. Warunek konieczny to **równanie Eulera–Lagrange'a**:

$$\frac{d}{dx}\frac{\partial F}{\partial y'} - \frac{\partial F}{\partial y} = 0.$$

**Klasyczne przykłady:**
- **Najkrótsza droga na płaszczyźnie:** $F = \sqrt{1 + y'^2}$, nie zależy od $y$, więc $\partial F/\partial y' = \text{const}$, czyli $y' = \text{const}$ — prosta.
- **Brachistochrona (Bernoulli, 1696):** kształt rynny, po której koralik zsunie się najszybciej z punktu A do B. Rozwiązaniem jest **cykloida**, a nie prosta. Dla zjazdu na odległość $\pi$ m w poziomie i 2 m w pionie: po cykloidzie 1,00 s, po prostej 1,19 s.
- **Zasada Fermata:** światło biegnie po drodze, którą pokonuje w najkrótszym czasie. Wynika z niej prawo odbicia i prawo załamania $n_1\sin\alpha_1 = n_2\sin\alpha_2$ (17.02).

**Zasada najmniejszego działania (Hamiltona).** Dla układu mechanicznego definiujemy **funkcję Lagrange'a** (lagranżjan)

$$L = E_k - E_p$$

i **działanie** $S = \displaystyle\int_{t_1}^{t_2}L\,dt$. Spośród wszystkich ruchów $x(t)$ łączących położenie $x_1$ w chwili $t_1$ z $x_2$ w chwili $t_2$ rzeczywisty ruch to ten, dla którego $S$ jest stacjonarne ($\delta S = 0$). Równanie Eulera–Lagrange'a z $L = \tfrac12m\dot x^2 - V(x)$:

$$\frac{d}{dt}(m\dot x) + \frac{dV}{dx} = 0 \Rightarrow m\ddot x = -\frac{dV}{dx} = F.$$

To druga zasada dynamiki Newtona (03.01).

**Dlaczego to ważne:**
- działanie jest **skalarem**, więc łatwo zmieniać współrzędne (biegunowe, kąty, współrzędne uogólnione 28.02);
- symetrie lagranżjanu prowadzą wprost do praw zachowania (28.03);
- ta sama zasada działa w elektrodynamice, teorii względności i fizyce cząstek — teorię zapisuje się, podając jej lagranżjan (np. Model Standardowy, 24.02);
- w mechanice kwantowej cząstka „bada” wszystkie drogi naraz, a klasyczna droga to ta, wokół której fazy $e^{iS/\hbar}$ się wzmacniają.

## Wzory i założenia

| Wzór | Znaczenie | Kiedy obowiązuje |
|---|---|---|
| $J[y] = \int F(y, y', x)\,dx$ | funkcjonał | ustalone końce $y(x_1)$, $y(x_2)$ |
| $\dfrac{d}{dx}\dfrac{\partial F}{\partial y'} - \dfrac{\partial F}{\partial y} = 0$ | równanie Eulera–Lagrange'a | warunek ekstremum |
| $F - y'\dfrac{\partial F}{\partial y'} = \text{const}$ | całka pierwsza (tożsamość Beltramiego) | $F$ nie zależy jawnie od $x$ |
| $L = E_k - E_p$ | lagranżjan | siły zachowawcze |
| $S = \int L\,dt$, $\delta S = 0$ | zasada Hamiltona | ustalone położenia w $t_1$ i $t_2$ |
| $x = R(\varphi - \sin\varphi)$, $y = -R(1 - \cos\varphi)$ | cykloida (brachistochrona) | start z zerową prędkością |

## Przykład rozwiązany

**Zadanie.** Kamień rzucony pionowo wraca na ziemię po $T = 1\ \mathrm s$. Porównaj działanie dla prawdziwego ruchu $y_0(t) = \tfrac12gt(T - t)$ i dla ruchów zaburzonych $y(t) = y_0(t) + \varepsilon\sin(\pi t/T)$ (te same końce).

Dla $m = 1\ \mathrm{kg}$ całkowanie numeryczne $S = \int_0^T(\tfrac12m\dot y^2 - mgy)dt$ daje: $\varepsilon = 0$: $S = -4{,}010\ \mathrm{J\cdot s}$; $\varepsilon = \pm0{,}1\ \mathrm m$: $S = -3{,}985\ \mathrm{J\cdot s}$. Działanie jest najmniejsze dla prawdziwego ruchu, a zaburzenie zwiększa je o $\dfrac{m\pi^2}{4T}\varepsilon^2$ — kwadratowo, bez wyrazu liniowego. To właśnie znaczy, że $S$ jest stacjonarne.

### Wersja z rachunkiem różniczkowym i całkowym

**Wyprowadzenie równania Eulera–Lagrange'a.** Niech $y(x)$ będzie ekstremalna, a $\eta(x)$ dowolną funkcją z $\eta(x_1) = \eta(x_2) = 0$. Dla $y + \varepsilon\eta$:

$$\frac{dJ}{d\varepsilon}\Big|_{\varepsilon=0} = \int_{x_1}^{x_2}\left(\frac{\partial F}{\partial y}\eta + \frac{\partial F}{\partial y'}\eta'\right)dx = \int_{x_1}^{x_2}\left(\frac{\partial F}{\partial y} - \frac{d}{dx}\frac{\partial F}{\partial y'}\right)\eta\,dx = 0.$$

Drugi wyraz scałkowaliśmy przez części, a wyraz brzegowy znika, bo $\eta$ zeruje się na końcach. Całka ma znikać dla **każdego** $\eta$, więc nawias musi być równy zeru.

**Brachistochrona.** Prędkość z zasady zachowania energii: $v = \sqrt{2g\lvert y\rvert}$ (oś $y$ w dół). Czas $t = \int\dfrac{ds}{v} = \int\dfrac{\sqrt{1 + y'^2}}{\sqrt{2gy}}dx$. $F$ nie zależy od $x$, więc z tożsamości Beltramiego $\dfrac{1}{\sqrt{y(1 + y'^2)}} = \text{const}$, czyli $y(1 + y'^2) = 2R$. Rozwiązaniem jest cykloida — krzywa zakreślana przez punkt toczącego się koła o promieniu $R$.

## Typowe pułapki

- **Natura „wie”, dokąd zmierza.** Zasada działania jest równoważna równaniom Newtona, które są lokalne. Warunki na obu końcach to sposób sformułowania problemu, a nie przyczynowość wstecz.
- **Działanie jest zawsze minimalne.** Jest stacjonarne. Dla krótkich odcinków ruchu to minimum, ale np. dla oscylatora na czasie dłuższym niż pół okresu bywa punktem siodłowym.
- **$L = E_k + E_p$.** Lagranżjan to różnica energii. Suma to energia całkowita (hamiltonian, 28.04).
- **Prosta jest zawsze najszybsza.** Najkrótsza — tak, najszybsza w polu grawitacyjnym — nie. Na początku warto szybko nabrać prędkości.

## Doświadczenie / symulacja

**Wyścig koralików.** Zbuduj z kartonu lub giętkiej listwy dwa tory o tych samych końcach: prosty i zbliżony do cykloidy (szybki spadek na początku). Puść jednocześnie dwie kulki i nagraj telefonem w zwolnionym tempie. Zmierz czasy i porównaj z obliczeniami.

**Python:** działanie dla prawdziwego i zaburzonych ruchów, wyznaczenie toru przez numeryczną minimalizację działania (dyskretyzacja) i porównanie czasu zjazdu po prostej i po cykloidzie.

```python
import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import quad
from scipy.optimize import minimize

g, m, T = 9.81, 1.0, 1.0
def dzialanie(eps):
    y = lambda t: g*t*(T - t)/2 + eps*np.sin(np.pi*t/T)
    v = lambda t: g*(T - 2*t)/2 + eps*np.pi/T*np.cos(np.pi*t/T)
    return quad(lambda t: 0.5*m*v(t)**2 - m*g*y(t), 0, T)[0]
for eps in (0, 0.05, 0.1, -0.1):
    print(f"ε = {eps:5.2f} m: S = {dzialanie(eps):.4f} J·s (przyrost {dzialanie(eps) - dzialanie(0):.4f}, teoria {m*np.pi**2/(4*T)*eps**2:.4f})")

N = 40                                                      # minimalizacja dyskretnego działania po położeniach w N−1 chwilach
t = np.linspace(0, T, N + 1); dt = t[1] - t[0]
def S_dyskr(y_wew):
    y = np.concatenate([[0], y_wew, [0]])
    return np.sum(0.5*m*(np.diff(y)/dt)**2*dt - m*g*0.5*(y[1:] + y[:-1])*dt)
wynik = minimize(S_dyskr, np.zeros(N - 1), method="BFGS")
y_num = np.concatenate([[0], wynik.x, [0]])
print(f"maks. różnica toru numerycznego od paraboli: {np.max(np.abs(y_num - g*t*(T - t)/2))*1e3:.2f} mm")

R = 1.0                                                     # brachistochrona: zjazd o πR w poziomie i 2R w pionie
t_cykl = np.pi*np.sqrt(R/g)
Lp = np.sqrt((np.pi*R)**2 + (2*R)**2)
t_prosta = np.sqrt(2*Lp/(g*2*R/Lp))
print(f"czas zjazdu: cykloida {t_cykl:.3f} s, prosta {t_prosta:.3f} s")

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(11, 4))
ax1.plot(t, g*t*(T - t)/2, label="parabola (Newton)"); ax1.plot(t, y_num, "o", ms=3, label="minimum działania")
ax1.set_xlabel("t [s]"); ax1.set_ylabel("y [m]"); ax1.legend()
phi = np.linspace(0, np.pi, 200)
ax2.plot(R*(phi - np.sin(phi)), -R*(1 - np.cos(phi)), label="cykloida")
ax2.plot([0, np.pi*R], [0, -2*R], label="prosta"); ax2.set_aspect("equal"); ax2.legend(); ax2.set_title("brachistochrona")
plt.tight_layout(); plt.show()
```

## Zadania

### A. Poziom maturalny _(opcjonalnie — rozgrzewka)_

1. Ratownik stoi na plaży, a tonący jest w wodzie. Na piasku ratownik biegnie szybciej niż płynie. Czy powinien biec prosto do tonącego? Jakie prawo optyki opisuje najlepszą drogę?

<details>
<summary>Odpowiedź</summary>

Nie — powinien przebiec dłuższy odcinek po piasku, a krótszy przepłynąć. Najszybsza droga spełnia warunek $\dfrac{\sin\alpha_1}{v_1} = \dfrac{\sin\alpha_2}{v_2}$, czyli prawo załamania (zasada Fermata, 17.02).
</details>

2. Zapisz lagranżjan ciała o masie $m$ spadającego swobodnie (oś $y$ w górę).

<details>
<summary>Odpowiedź</summary>

$L = \tfrac12m\dot y^2 - mgy$.
</details>

### B. Poziom akademicki

1. Z równania Eulera–Lagrange'a dla $L = \tfrac12m\dot y^2 - mgy$ wyprowadź równanie ruchu. Rozwiąż je z warunkami $y(0) = y(T) = 0$.

<details>
<summary>Odpowiedź</summary>

$\dfrac{d}{dt}(m\dot y) + mg = 0 \Rightarrow \ddot y = -g$, $y = -\tfrac12gt^2 + v_0t$; z $y(T) = 0$: $v_0 = gT/2$, $y = \tfrac12gt(T - t)$.
</details>

2. Wyprowadź prawo załamania z zasady Fermata: światło biegnie z punktu $(0, a)$ w ośrodku o prędkości $v_1$ do punktu $(d, -b)$ w ośrodku o prędkości $v_2$, przecinając granicę $y = 0$ w punkcie $x$. Zminimalizuj czas $t(x)$.

<details>
<summary>Odpowiedź</summary>

$t = \dfrac{\sqrt{a^2 + x^2}}{v_1} + \dfrac{\sqrt{b^2 + (d - x)^2}}{v_2}$. $\dfrac{dt}{dx} = \dfrac{x}{v_1\sqrt{a^2 + x^2}} - \dfrac{d - x}{v_2\sqrt{b^2 + (d - x)^2}} = 0 \Rightarrow \dfrac{\sin\alpha_1}{v_1} = \dfrac{\sin\alpha_2}{v_2}$, a z $v = c/n$: $n_1\sin\alpha_1 = n_2\sin\alpha_2$.
</details>

3. Pokaż, że najkrótszą krzywą łączącą dwa punkty na płaszczyźnie jest prosta, i że dla funkcjonału $\int\sqrt{1 + y'^2}\,dx$ równanie Eulera–Lagrange'a daje $y'' = 0$.

<details>
<summary>Odpowiedź</summary>

$\partial F/\partial y = 0$, więc $\dfrac{d}{dx}\dfrac{y'}{\sqrt{1 + y'^2}} = 0 \Rightarrow \dfrac{y'}{\sqrt{1 + y'^2}} = \text{const} \Rightarrow y' = \text{const}$, czyli $y'' = 0$.
</details>

4. Zmień w kodzie liczbę punktów dyskretyzacji $N$ na 10 i 100. Jak zmienia się różnica między minimum dyskretnego działania a parabolą?

<details>
<summary>Odpowiedź</summary>

Dla tej dyskretyzacji (trapezowa całka energii potencjalnej) minimum leży dokładnie na paraboli w węzłach — różnica jest na poziomie dokładności minimalizacji (ułamki mm), niezależnie od $N$. Inne schematy dyskretyzacji dają błąd malejący jak $1/N^2$.
</details>

## Źródła

- S. Charzyński, K. Turzyński, *Mechanika analityczna*, „Delta” 9/2016 — [artykuł po polsku](https://deltami-old.mimuw.edu.pl/temat/fizyka/mechanika/2016/09/03/1609delta-mechanika-analityczna.pdf).
- W. Wojtyński, *Matematyczne metody mechaniki*, skrypt MIMUW (rozdz. 7–8: rachunek wariacyjny, równania Eulera–Lagrange'a) — [mst.mimuw.edu.pl](https://mst.mimuw.edu.pl/wyklady/mmk/wyklad.pdf).
- J. R. Taylor, *Mechanika klasyczna*, PWN — rozdziały o rachunku wariacyjnym i równaniach Lagrange'a.
- R. Feynman, *Feynmana wykłady z fizyki*, t. II, rozdz. 19 „Zasada najmniejszego działania” (PWN); wersja angielska online: [feynmanlectures.caltech.edu/II_19.html](https://www.feynmanlectures.caltech.edu/II_19.html) (materiał dodatkowy).
- Moduły 03.01 (zasady dynamiki), 17.02 (prawo załamania).
