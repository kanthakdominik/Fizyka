# 27.04 — Statystyki kwantowe: fermiony, bozony i promieniowanie cieplne

> **Moduł:** [27 — Fizyka statystyczna](README.md) · **Poziom:** 🔵 studia · **Status:** ✅ pełny
>
> **Czytaj:**
>
> - OpenStax, *Fizyka dla szkół wyższych*, t. 3, rozdz. 6: [§6.1](https://openstax.org/books/fizyka-dla-szk%C3%B3%C5%82-wy%C5%BCszych-tom-3/pages/6-1-promieniowanie-ciala-doskonale-czarnego) · [wstęp do rozdziału](https://openstax.org/books/fizyka-dla-szk%C3%B3%C5%82-wy%C5%BCszych-tom-3/pages/6-wstep)

← [Ekwipartycja energii i kwantowe zamrażanie stopni swobody](03-ekwipartycja-i-cieplo-wlasciwe.md) · [spis modułu](README.md) · [Model Isinga, przejścia fazowe i metoda Metropolisa](05-model-isinga.md) →

## Po co to jest

Cząstki tego samego rodzaju są w mechanice kwantowej nierozróżnialne, a to zmienia sposób liczenia stanów. Fermiony (elektrony, protony, neutrony) nie mogą zajmować tego samego stanu — stąd budowa układu okresowego (21.04), przewodnictwo metali (23.03) i stabilność białych karłów (26.03). Bozony (fotony, atomy helu-4) chętnie gromadzą się w jednym stanie — stąd promieniowanie ciała doskonale czarnego (20.01), laser (21.06), nadciekłość helu i kondensat Bosego–Einsteina. Ten temat zbiera te zjawiska w jeden obraz: dwa rozkłady różniące się jednym znakiem w mianowniku.

## Teoria w pigułce

**Rozkład obsadzeń.** Pytamy o średnią liczbę cząstek $\bar n(E)$ w jednym stanie kwantowym o energii $E$, w temperaturze $T$ i przy potencjale chemicznym $\mu$ (parametr ustalający całkowitą liczbę cząstek):

$$\bar n_{FD} = \frac{1}{e^{(E - \mu)/kT} + 1}\ \text{(fermiony)}, \qquad \bar n_{BE} = \frac{1}{e^{(E - \mu)/kT} - 1}\ \text{(bozony)}, \qquad \bar n_{MB} = e^{-(E - \mu)/kT}\ \text{(klasycznie)}.$$

- **Fermiony** (spin połówkowy): $\bar n \le 1$ — zakaz Pauliego. W 0 K wszystkie stany poniżej energii Fermiego $E_F = \mu(0)$ są pełne, powyżej puste (23.03).
- **Bozony** (spin całkowity): $\bar n$ może być dowolnie duże; gdy $E \to \mu$, obsadzenie rośnie bez ograniczeń.
- Dla $E - \mu \gg kT$ oba rozkłady przechodzą w klasyczny rozkład Boltzmanna (27.02).

**Kiedy trzeba statystyk kwantowych?** Gdy cząstki są tak gęsto upakowane, że ich fale się nakładają. Miarą jest **termiczna długość fali de Broglie'a** $\lambda_{th} = h/\sqrt{2\pi mkT}$ (20.04). Jeśli $n\lambda_{th}^3 \ll 1$, wystarczy statystyka klasyczna, jeśli $n\lambda_{th}^3 \gtrsim 1$ — trzeba kwantowej.
- Powietrze w 300 K: $\lambda_{th} \approx 0{,}02\ \mathrm{nm}$, $n\lambda_{th}^3 \approx 2\cdot10^{-7}$ — gaz klasyczny.
- Elektrony w miedzi w 300 K: $\lambda_{th} \approx 4\ \mathrm{nm}$, $n\lambda_{th}^3 \approx 7000$ — silnie kwantowy gaz Fermiego.

**Gaz fotonów i prawo Plancka.** Fotony to bozony, których liczba nie jest zachowana ($\mu = 0$). Liczba stanów fotonu o częstotliwości od $f$ do $f + df$ w objętości $V$ to $\dfrac{8\pi f^2}{c^3}V\,df$ (dwie polaryzacje). Mnożąc przez $hf\cdot\bar n_{BE}$, dostajemy gęstość energii promieniowania ciała doskonale czarnego:

$$u(f)\,df = \frac{8\pi hf^3}{c^3}\frac{df}{e^{hf/kT} - 1}.$$

To prawo Plancka (20.01) — Planck odkrył je w 1900 r., zanim istniało pojęcie fotonu. Promieniowanie tła Wszechświata (24.04) to gaz fotonów o temperaturze 2,725 K: ok. 411 fotonów na cm³.

**Kondensat Bosego–Einsteina.** Gaz bozonów o stałej liczbie cząstek poniżej temperatury krytycznej

$$T_c = \frac{2\pi\hbar^2}{mk}\left(\frac{n}{2{,}612}\right)^{2/3}$$

zaczyna gromadzić makroskopową część cząstek w stanie podstawowym. Pierwszy kondensat z atomów rubidu-87 (Cornell, Wieman, 1995; Nobel 2001) wymagał temperatury ok. 170 nK. Hel-4 staje się nadciekły w 2,17 K (wzór dla gazu idealnego o gęstości ciekłego helu daje 3,1 K — oddziaływania przesuwają tę wartość). Nadciekły hel płynie bez lepkości i wspina się po ściankach naczynia.

**Emisja wymuszona** (21.06) też jest efektem bozonowym: foton chętniej jest emitowany do stanu, w którym już są fotony (czynnik $1 + \bar n$). Na tym działa laser.

## Wzory i założenia

| Wzór | Znaczenie | Kiedy obowiązuje |
|---|---|---|
| $\bar n_{FD} = 1/(e^{(E - \mu)/kT} + 1)$ | rozkład Fermiego–Diraca | fermiony nierozróżnialne |
| $\bar n_{BE} = 1/(e^{(E - \mu)/kT} - 1)$ | rozkład Bosego–Einsteina | bozony; $\mu \le$ najniższa energia |
| $\bar n_{MB} = e^{-(E - \mu)/kT}$ | granica klasyczna | $E - \mu \gg kT$ |
| $\lambda_{th} = h/\sqrt{2\pi mkT}$ | termiczna długość fali | kryterium: $n\lambda_{th}^3 \sim 1$ |
| $u(f) = \dfrac{8\pi hf^3}{c^3}\dfrac{1}{e^{hf/kT} - 1}$ | prawo Plancka | gaz fotonów, $\mu = 0$ |
| $T_c = \dfrac{2\pi\hbar^2}{mk}\left(\dfrac{n}{2{,}612}\right)^{2/3}$ | temperatura kondensacji BE | gaz idealny bozonów |

## Przykład rozwiązany

**Zadanie 1.** Porównaj obsadzenie stanu o energii $E - \mu = kT$ w trzech statystykach.

FD: $1/(e + 1) \approx 0{,}27$. BE: $1/(e - 1) \approx 0{,}58$. MB: $1/e \approx 0{,}37$. Fermiony „unikają się” (mniejsze obsadzenie), bozony „przyciągają” (większe).

**Zadanie 2.** Oblicz termiczną długość fali i parametr $n\lambda_{th}^3$ dla azotu w warunkach pokojowych i dla elektronów w miedzi ($n = 8{,}5\cdot10^{28}\ \mathrm{m^{-3}}$) w 300 K.

N₂: $\lambda_{th} = h/\sqrt{2\pi mkT} \approx 1{,}9\cdot10^{-11}\ \mathrm m$, $n = p/kT = 2{,}4\cdot10^{25}\ \mathrm{m^{-3}}$, $n\lambda_{th}^3 \approx 1{,}7\cdot10^{-7}$ — klasyczny.

Elektrony: $\lambda_{th} \approx 4{,}3\cdot10^{-9}\ \mathrm m$, $n\lambda_{th}^3 \approx 6800$ — zdegenerowany gaz Fermiego. Dlatego elektrony w metalu mają energie rzędu eV nawet w zerze bezwzględnym (23.03).

### Wersja z rachunkiem różniczkowym i całkowym

**Wyprowadzenie rozkładów.** Jeden stan kwantowy może mieć $n$ cząstek o łącznej energii $n(E - \mu)$ (mierzonej względem $\mu$). Z czynnika Boltzmanna $P(n) \propto e^{-n x}$, $x = (E - \mu)/kT$.
- Fermiony: $n = 0$ lub 1: $\bar n = \dfrac{e^{-x}}{1 + e^{-x}} = \dfrac{1}{e^x + 1}$.
- Bozony: $n = 0, 1, 2, \dots$: $Z = \sum e^{-nx} = \dfrac{1}{1 - e^{-x}}$, $\bar n = -\dfrac{\partial\ln Z}{\partial x} = \dfrac{1}{e^x - 1}$.

**Prawo Stefana–Boltzmanna z prawa Plancka.** Całkowita gęstość energii (podstawienie $x = hf/kT$):

$$u = \int_0^\infty\frac{8\pi hf^3}{c^3}\frac{df}{e^{hf/kT} - 1} = \frac{8\pi(kT)^4}{(hc)^3}\int_0^\infty\frac{x^3dx}{e^x - 1} = \frac{8\pi^5(kT)^4}{15(hc)^3}.$$

Całka wynosi $\pi^4/15$ (25.01). Strumień z powierzchni to $\tfrac c4u = \sigma T^4$ ze stałą $\sigma = \dfrac{2\pi^5k^4}{15h^3c^2}$ — prawo Stefana–Boltzmanna wynika ze statystyki Bosego–Einsteina.

## Typowe pułapki

- **Rozkład Fermiego–Diraca to rozkład energii elektronów.** To obsadzenie **jednego stanu**. Liczba elektronów o danej energii to $g(E)\bar n(E)$ (gęstość stanów razy obsadzenie, 23.03).
- **Bozony muszą mieć zerowy spin.** Bozony mają spin całkowity (0, 1, 2…). Foton ma spin 1, atom ⁴He (2 protony, 2 neutrony, 2 elektrony — parzysta liczba fermionów) jest bozonem, a ³He fermionem.
- **Kondensat Bosego–Einsteina wymaga przyciągania między atomami.** Kondensacja zachodzi nawet w gazie idealnym — to efekt czysto statystyczny.
- **W wysokiej temperaturze wszystkie gazy są kwantowe.** Odwrotnie: wysoka temperatura i mała gęstość to granica klasyczna ($n\lambda_{th}^3 \ll 1$).

## Doświadczenie / symulacja

**Promieniowanie cieplne żarówki.** Zmierz w phyphox (*Natężenie światła*) natężenie światła żarówki tradycyjnej (lub halogenowej) zasilanej regulowanym napięciem. Przy niższej temperaturze włókna moc rośnie jak $T^4$, ale moc w świetle widzialnym rośnie znacznie szybciej — bo maksimum widma przesuwa się ku krótszym falom (26.01).

**Symulacja PhET:** *Widmo ciała doskonale czarnego* — porównaj kształt widma z rozkładem Bosego–Einsteina ([phet.colorado.edu/pl](https://phet.colorado.edu/pl/)).

**Python:** trzy rozkłady obsadzeń, prawo Plancka i stała Stefana–Boltzmanna z całki rozkładu Bosego–Einsteina, termiczna długość fali i temperatura kondensacji.

```python
import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import quad
from scipy.special import zeta

h, hbar, c, k, me, amu = 6.62607015e-34, 1.054571817e-34, 2.99792458e8, 1.380649e-23, 9.1093837e-31, 1.66054e-27
x = np.linspace(-3, 5, 400)                                   # (E − μ)/kT
plt.plot(x, 1/(np.exp(x) + 1), label="Fermi–Dirac")
xb = x[x > 0.05]; plt.plot(xb, 1/np.expm1(xb), label="Bose–Einstein")
plt.plot(x, np.exp(-x), "--", label="Maxwell–Boltzmann")
plt.ylim(0, 3); plt.xlabel("(E − μ)/kT"); plt.ylabel("średnie obsadzenie stanu"); plt.legend(); plt.grid(True)

I = quad(lambda t: t**3/np.expm1(t), 0, 60)[0]
sigma = 2*np.pi*k**4/(h**3*c**2)*I
print(f"∫x³/(eˣ−1) = {I:.5f} (π⁴/15 = {np.pi**4/15:.5f}), σ = {sigma:.4e} W/(m²K⁴)")
T = 2.7255
print(f"fotony promieniowania tła: {2*zeta(3)/np.pi**2*(k*T/(hbar*c))**3/1e6:.0f} na cm³")

lam = lambda m, T: h/np.sqrt(2*np.pi*m*k*T)
for nazwa, m, n, Tk in [("N₂ (powietrze)", 28*amu, 101325/(k*300), 300), ("elektrony w Cu", me, 8.5e28, 300),
                        ("⁴He ciekły", 4.0026*amu, 145/(4.0026*amu), 4.2), ("⁸⁷Rb w pułapce", 87*amu, 1e20, 1e-6)]:
    print(f"{nazwa:15s}: λ_th = {lam(m, Tk):.2e} m, nλ³ = {n*lam(m, Tk)**3:.1e}")
for nazwa, m, n in [("⁴He (ciecz, gaz idealny)", 4.0026*amu, 145/(4.0026*amu)), ("⁸⁷Rb, n = 1e20 m⁻³", 87*amu, 1e20)]:
    print(f"T_c kondensacji BE, {nazwa}: {2*np.pi*hbar**2/(m*k)*(n/zeta(1.5))**(2/3):.3g} K")
plt.show()
```

## Zadania

### A. Poziom maturalny _(opcjonalnie — rozgrzewka)_

1. Które z cząstek są fermionami, a które bozonami: elektron, foton, proton, atom ⁴He, atom ³He, neutron?

<details>
<summary>Odpowiedź</summary>

Fermiony: elektron, proton, neutron, ³He (5 fermionów). Bozony: foton, ⁴He (6 fermionów — parzysta liczba).
</details>

2. Dlaczego w każdym orbitalu atomu mogą być najwyżej dwa elektrony?

<details>
<summary>Odpowiedź</summary>

Elektrony są fermionami (zakaz Pauliego): w jednym stanie kwantowym może być najwyżej jeden. Orbital z dwoma możliwymi kierunkami spinu to dwa stany.
</details>

### B. Poziom akademicki

1. Pokaż, że dla $E - \mu \gg kT$ oba rozkłady kwantowe przechodzą w rozkład Boltzmanna, a dla bozonów przy $E - \mu \ll kT$: $\bar n \approx kT/(E - \mu)$.

<details>
<summary>Odpowiedź</summary>

Dla $x \gg 1$: $e^x \pm 1 \approx e^x$, więc $\bar n \approx e^{-x}$. Dla bozonów przy $x \ll 1$: $e^x - 1 \approx x$, więc $\bar n \approx 1/x = kT/(E - \mu)$. Dla fotonów ($\mu = 0$) daje to klasyczną granicę Rayleigha–Jeansa: $\bar n hf \approx kT$.
</details>

2. Oblicz temperaturę kondensacji gazu atomów sodu-23 o gęstości $10^{20}\ \mathrm{m^{-3}}$.

<details>
<summary>Odpowiedź</summary>

$T_c = \dfrac{2\pi\hbar^2}{mk}\left(\dfrac{n}{2{,}612}\right)^{2/3}$, $m = 23\ \mathrm u$: ok. $1{,}5\ \mu\mathrm K$ (dla rubidu-87 ok. 0,4 μK — cięższe atomy kondensują w niższej temperaturze).
</details>

3. Ile fotonów promieniowania tła przypada na jeden proton we Wszechświecie, jeśli średnia gęstość materii barionowej to ok. 0,25 protonu na m³?

<details>
<summary>Odpowiedź</summary>

$n_\gamma \approx 4{,}1\cdot10^8\ \mathrm{m^{-3}}$, więc ok. $1{,}6\cdot10^9$ fotonów na proton. Ten stosunek jest kluczowym parametrem nukleosyntezy (24.04).
</details>

## Źródła

- OpenStax, *Fizyka dla szkół wyższych*, t. 3, rozdz. 6 — §6.1: promieniowanie ciała doskonale czarnego.
- Halliday, Resnick, Walker, *Podstawy fizyki*, wyd. 2015, t. 5, §41.1 — rozkład Fermiego–Diraca w metalach.
- K. Huang, *Podstawy fizyki statystycznej*, PWN — statystyki kwantowe i kondensacja Bosego–Einsteina.
- Moduły 20.01 (prawo Plancka), 21.04 (zakaz Pauliego), 21.06 (lasery), 23.03 (gaz Fermiego), 26.03 (białe karły).
- Symulacja PhET *Widmo ciała doskonale czarnego*.
