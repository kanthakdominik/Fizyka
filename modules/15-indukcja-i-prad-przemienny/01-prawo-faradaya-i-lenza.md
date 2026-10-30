# 15.01 — Prawo Faradaya i reguła Lenza

> **Moduł:** [15 — Indukcja elektromagnetyczna i prąd przemienny](README.md) · **Poziom:** 🟢 matura R · **Status:** ✅ pełny
>
> **Czytaj:**
>
> - OpenStax, *Fizyka dla szkół wyższych*, t. 2, rozdz. 13: [§13.1–13.2](https://openstax.org/books/fizyka-dla-szk%C3%B3%C5%82-wy%C5%BCszych-tom-2/pages/13-1-prawo-faradaya) · [wstęp do rozdziału](https://openstax.org/books/fizyka-dla-szk%C3%B3%C5%82-wy%C5%BCszych-tom-2/pages/13-wstep)
> - Halliday, Resnick, Walker, *Podstawy fizyki*, wyd. 2015, t. 3: §30.1 (s. 329)
> - Halliday, Resnick, Walker, *Podstawy fizyki*, wyd. 1 (2003), t. 3: §31.1–31.4, s. 248 (skan t. 3 na serwerze AGH kończy się na s. 127 — dalsze strony tylko w wydaniu papierowym)

← (początek modułu) · [spis modułu](README.md) · [SEM ruchu i indukowane pole elektryczne](02-sem-ruchu-i-pole-indukowane.md) →

## Po co to jest

Zmienne pole magnetyczne wytwarza prąd. Tak Faraday w 1831 r. odkrył zjawisko, na którym opiera się prawie cała energetyka: prądnice w elektrowniach, transformatory, ładowarki indukcyjne telefonów, kuchenki indukcyjne, mikrofony dynamiczne, czytniki kart zbliżeniowych i wykrywacze metali. Reguła Lenza, która mówi, w którą stronę płynie prąd indukowany, jest wyrazem zasady zachowania energii.

## Teoria w pigułce

**Strumień pola magnetycznego** przez powierzchnię:

$$\Phi_B = \int\vec B\cdot d\vec A, \qquad \Phi_B = BA\cos\theta \ \text{(pole jednorodne, płaska powierzchnia)}, \qquad 1\ \mathrm{Wb} = 1\ \mathrm{T\cdot m^2}.$$

Strumień przez obwód można zmienić na trzy sposoby: zmieniając pole $B$, pole powierzchni $A$ albo kąt $\theta$ (obrót).

**Prawo Faradaya.** Zmiana strumienia przez obwód wytwarza w nim siłę elektromotoryczną (SEM) indukcji:

$$\varepsilon = -N\frac{d\Phi_B}{dt}.$$

$N$ to liczba zwojów. Jeśli obwód jest zamknięty i ma opór $R$, płynie prąd $I = \varepsilon/R$. Przepływający ładunek $q = N\Delta\Phi/R$ zależy tylko od zmiany strumienia, a nie od jej szybkości.

**Reguła Lenza** (znak minus). Prąd indukowany płynie w takim kierunku, że jego pole magnetyczne **przeciwdziała zmianie** strumienia, która go wywołała.
- Zbliżamy magnes biegunem N do pętli: prąd indukowany wytwarza po stronie magnesu biegun N i odpycha magnes.
- Oddalamy magnes: pętla go przyciąga.

W obu przypadkach trzeba wykonać pracę, która zamienia się w energię prądu. Gdyby było odwrotnie, magnes sam by się rozpędzał wbrew zasadzie zachowania energii.

## Wzory i założenia

| Wzór | Znaczenie | Kiedy obowiązuje |
|---|---|---|
| $\Phi_B = BA\cos\theta$ | strumień magnetyczny | pole jednorodne, płaska pętla |
| $\varepsilon = -N\,d\Phi_B/dt$ | prawo Faradaya | zawsze |
| $\lvert\varepsilon\rvert = N\Delta\Phi/\Delta t$ | średnia SEM | zmiana w czasie $\Delta t$ |
| $q = N\Delta\Phi/R$ | ładunek indukowany | obwód zamknięty o oporze $R$ |

## Przykład rozwiązany

**Zadanie.** Cewka ma 100 zwojów o polu 10 cm² i jest ustawiona prostopadle do pola. Pole rośnie równomiernie od 0 do 0,5 T w czasie 0,1 s. Oblicz SEM indukcji. Jaki prąd płynie i jaki ładunek przepłynie, jeśli cewka ma opór 2 Ω?

$\Delta\Phi = 0{,}5\cdot10^{-3} = 5\cdot10^{-4}\ \mathrm{Wb}$, $\varepsilon = 100\cdot5\cdot10^{-4}/0{,}1 = 0{,}5\ \mathrm V$.

$I = 0{,}25\ \mathrm A$, $q = It = 0{,}025\ \mathrm C$. To samo daje $q = N\Delta\Phi/R$.

## Typowe pułapki

- **SEM zależy od wartości strumienia.** Zależy od **szybkości zmian** strumienia. Duże, ale stałe pole nie indukuje niczego.
- **Prąd indukowany przeciwdziała polu.** Przeciwdziała **zmianie** strumienia. Gdy strumień maleje, prąd indukowany go podtrzymuje.
- **Kąt $\theta$ między polem a płaszczyzną.** We wzorze $\Phi = BA\cos\theta$ to kąt między polem a **normalną** do powierzchni.
- **Zapominanie o $N$.** Strumień przez cewkę mnoży się przez liczbę zwojów.
- **Indukcja tylko w obwodach zamkniętych.** SEM pojawia się zawsze. Prąd płynie tylko w obwodzie zamkniętym.

## Doświadczenie / symulacja

**Magnes i cewka.** Cewkę (np. 200–500 zwojów drutu w lakierze nawiniętych na rurkę) podłącz do miernika na zakresie mV albo do wejścia mikrofonowego komputera (rejestrator dźwięku jako oscyloskop). Wrzucaj magnes neodymowy przez cewkę i obserwuj impuls: najpierw w jedną stronę, potem w drugą. Zmień prędkość, liczbę zwojów i orientację magnesu.

**Hamowanie magnesu w rurce.** Magnes neodymowy wrzucony do rurki miedzianej lub aluminiowej spada wiele razy wolniej niż w plastikowej. To reguła Lenza (prądy wirowe, 15.03).

**Symulacja PhET:** *Prawo Faradaya* (*Faraday's Law*) — magnes i cewka z żarówką i woltomierzem ([phet.colorado.edu/pl](https://phet.colorado.edu/pl/)).

**Python:** SEM indukowana w cewce przy przelocie magnesu (model dipola na osi).

```python
import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import trapezoid

mu0 = 4e-7*np.pi
m_dip, R, N, v = 1.0, 0.01, 200, 1.0        # moment magnesu [A·m²], promień cewki, zwoje, prędkość
t = np.linspace(-0.1, 0.1, 4000)
z = v*t                                     # położenie magnesu względem cewki

# strumień pola dipola przez pętlę o promieniu R na osi: Φ = μ0 m R² / (2 (z² + R²)^{3/2})
Phi = mu0*m_dip*R**2/(2*(z**2 + R**2)**1.5)
eps = -N*np.gradient(Phi, t)
print(f"maksymalny strumień: {Phi.max()*1e6:.2f} µWb, maksymalna SEM: {eps.max()*1e3:.1f} mV")
print(f"pole pod krzywą SEM (powinno być ~0): {trapezoid(eps, t)*1e6:.3f} µV·s")
plt.plot(t*1e3, eps*1e3)
plt.xlabel("t [ms]"); plt.ylabel("ε [mV]"); plt.title("magnes przelatujący przez cewkę"); plt.grid(True); plt.show()
```

## Zadania

### A. Poziom maturalny

1. Pętla o polu 0,02 m² leży prostopadle do pola 0,3 T. W ciągu 0,05 s obrócono ją tak, że jej płaszczyzna jest równoległa do pola. Oblicz średnią SEM.

<details>
<summary>Odpowiedź</summary>

$\Delta\Phi = 0{,}3\cdot0{,}02 = 6\cdot10^{-3}\ \mathrm{Wb}$, $\varepsilon = 0{,}12\ \mathrm V$.
</details>

2. Magnes zbliżamy biegunem S do pierścienia aluminiowego zawieszonego na nitce. Co się stanie z pierścieniem? A gdy pierścień jest przecięty?

<details>
<summary>Odpowiedź</summary>

Pierścień zostanie odepchnięty (prąd indukowany przeciwdziała wzrostowi strumienia). Przecięty pierścień prawie nie zareaguje, bo prąd nie może płynąć.
</details>

3. Dlaczego magnes spada powoli w rurce miedzianej, choć miedź nie jest przyciągana przez magnes?

<details>
<summary>Odpowiedź</summary>

Ruch magnesu zmienia strumień przez kolejne „pierścienie” rurki. Indukują się w nich prądy, których pole hamuje magnes (powyżej odpycha, poniżej przyciąga). Energia ruchu zamienia się w ciepło w rurce.
</details>

### B. Poziom akademicki _(opcjonalnie — rozszerzenie z rachunkiem)_

1. Pole przez cewkę ($N$ zwojów, pole $A$) zmienia się jak $B = B_0\sin\omega t$. Wyznacz $\varepsilon(t)$ i jej amplitudę dla $N = 100$, $A = 10\ \mathrm{cm^2}$, $B_0 = 0{,}1\ \mathrm T$, $f = 50\ \mathrm{Hz}$.

<details>
<summary>Odpowiedź</summary>

$\varepsilon = -NAB_0\omega\cos\omega t$, amplituda $NAB_0\omega \approx 3{,}1\ \mathrm V$.
</details>

2. Pokaż, że całkowity ładunek indukowany przy przelocie magnesu przez cewkę (od bardzo daleka do bardzo daleka) wynosi zero, a przy wsunięciu magnesu do środka wynosi $N\Phi_{\text{środek}}/R$.

<details>
<summary>Odpowiedź</summary>

$q = \displaystyle\int I\,dt = -\frac NR\int\frac{d\Phi}{dt}dt = -\frac NR\Delta\Phi$. Przy przelocie strumień wraca do zera, więc $\Delta\Phi = 0$. Przy wsunięciu $\Delta\Phi = \Phi_{\text{środek}}$.
</details>

3. Kwadratowa pętla o boku $a$ leży w odległości $d$ od długiego przewodu, w jego płaszczyźnie. Prąd w przewodzie rośnie jak $I = kt$. Oblicz SEM w pętli.

<details>
<summary>Odpowiedź</summary>

$\Phi = \displaystyle\int_d^{d+a}\frac{\mu_0I}{2\pi x}a\,dx = \frac{\mu_0Ia}{2\pi}\ln\frac{d + a}{d}$, więc $\lvert\varepsilon\rvert = \dfrac{\mu_0ka}{2\pi}\ln\dfrac{d + a}{d}$.
</details>

## Źródła

- OpenStax, *Fizyka dla szkół wyższych*, t. 2, rozdz. 13 — §13.1 (prawo Faradaya) i §13.2 (reguła Lenza).
- Halliday, Resnick, Walker, *Podstawy fizyki* — wyd. 2015: t. 3, §30.1; wyd. 1: t. 3, §31.1–31.4.
- Symulacja PhET *Prawo Faradaya*.
