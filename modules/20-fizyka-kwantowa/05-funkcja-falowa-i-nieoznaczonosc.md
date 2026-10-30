# 20.05 — Funkcja falowa i zasada nieoznaczoności

> **Moduł:** [20 — Podstawy fizyki kwantowej](README.md) · **Poziom:** 🔵 studia · **Status:** ✅ pełny
>
> **Czytaj:**
>
> - OpenStax, *Fizyka dla szkół wyższych*, t. 3, rozdz. 7: [§7.1–7.2](https://openstax.org/books/fizyka-dla-szk%C3%B3%C5%82-wy%C5%BCszych-tom-3/pages/7-1-funkcje-falowe) · [wstęp do rozdziału](https://openstax.org/books/fizyka-dla-szk%C3%B3%C5%82-wy%C5%BCszych-tom-3/pages/7-wstep)
> - Halliday, Resnick, Walker, *Podstawy fizyki*, wyd. 2015, t. 5: §38.6–38.7 (s. 23)
> - Halliday, Resnick, Walker, *Podstawy fizyki*, wyd. 1 (2003), t. 5: [§39.7–39.8, s. 18](https://home.agh.edu.pl/~czapli/Resnick_5.pdf#page=34) — PDF z serwera AGH

← [Fale materii de Broglie'a i dualizm korpuskularno-falowy](04-fale-materii.md) · [spis modułu](README.md) · [Równanie Schrödingera: studnia potencjału i oscylator](06-rownanie-schrodingera.md) →

## Po co to jest

W mechanice kwantowej stan cząstki opisuje funkcja falowa $\psi$. Jej kwadrat mówi, gdzie cząstkę **prawdopodobnie** znajdziemy. Nie ma toru jak w mechanice klasycznej. Z falowej natury wynika zasada nieoznaczoności Heisenberga: nie da się jednocześnie dokładnie znać położenia i pędu. Ta zasada wyjaśnia, dlaczego atomy są stabilne i mają określony rozmiar, dlaczego linie widmowe mają szerokość, a hel nie zamarza pod normalnym ciśnieniem nawet w zerze bezwzględnym.

## Teoria w pigułce

**Funkcja falowa** $\psi(x, t)$ to liczba zespolona przypisana każdemu punktowi. Interpretacja Borna (1926):

$$P(a \le x \le b) = \int_a^b\lvert\psi(x, t)\rvert^2dx.$$

$\lvert\psi\rvert^2$ to **gęstość prawdopodobnieństwa** znalezienia cząstki. Normalizacja: $\int_{-\infty}^{\infty}\lvert\psi\rvert^2dx = 1$, bo cząstka gdzieś jest.

**Wartości oczekiwane** to średnie z wielu pomiarów na identycznie przygotowanych układach:

$$\langle x\rangle = \int x\lvert\psi\rvert^2dx, \qquad \Delta x = \sqrt{\langle x^2\rangle - \langle x\rangle^2}.$$

**Doświadczenie dwuszczelinowe z pojedynczymi elektronami** (20.04). Każdy elektron trafia w jeden punkt ekranu. Rozkład wielu trafień daje prążki interferencyjne, opisane przez $\lvert\psi_1 + \psi_2\rvert^2$, a nie przez sumę prawdopodobieństw. Jeśli sprawdzamy, przez którą szczelinę przeszedł elektron, prążki znikają.

**Zasada nieoznaczoności Heisenberga:**

$$\Delta x\,\Delta p_x \ge \frac\hbar2, \qquad \hbar = \frac{h}{2\pi} = 1{,}055\cdot10^{-34}\ \mathrm{J\cdot s}.$$

To nie jest niedoskonałość przyrządów, tylko własność fal. Fala o ściśle określonej długości (pędzie) jest nieskończenie długa, a krótki impuls (paczka falowa) wymaga mieszaniny wielu długości fali. Tak samo krótki dźwięk ma szerokie widmo (09.06).

**Nieoznaczoność energia–czas:** $\Delta E\,\Delta t \gtrsim \hbar/2$. Stan wzbudzony atomu żyjący przez czas $\tau$ ma energię rozmytą o $\sim\hbar/\tau$. Daje to naturalną szerokość linii widmowych.

**Konsekwencje:**
- elektron uwięziony w atomie (0,1 nm) ma pęd i energię kinetyczną rzędu kilku eV, co nie pozwala mu spaść na jądro;
- energia drgań atomów w krysztale nie spada do zera nawet w $T = 0$ (energia drgań zerowych).

## Wzory i założenia

| Wzór | Znaczenie | Kiedy obowiązuje |
|---|---|---|
| $\lvert\psi\rvert^2$ | gęstość prawdopodobieństwa | — |
| $\int\lvert\psi\rvert^2dx = 1$ | normalizacja | — |
| $\langle x\rangle = \int x\lvert\psi\rvert^2dx$ | wartość oczekiwana położenia | — |
| $\Delta x\Delta p \ge \hbar/2$ | zasada nieoznaczoności | równość dla paczki gaussowskiej |
| $\Delta E\Delta t \gtrsim \hbar/2$ | nieoznaczoność energia–czas | $\Delta t$ — czas życia, czas pomiaru |

## Przykład rozwiązany

**Zadanie 1.** Elektron jest zamknięty w obszarze o rozmiarze atomu, $\Delta x = 0{,}1\ \mathrm{nm}$. Oblicz najmniejszą nieoznaczoność pędu i prędkości. Porównaj z kulką o masie 1 g zlokalizowaną z dokładnością do 1 μm.

Elektron: $\Delta p \ge \hbar/(2\Delta x) \approx 5{,}3\cdot10^{-25}\ \mathrm{kg\cdot m/s}$, $\Delta v \ge 5{,}8\cdot10^5\ \mathrm{m/s}$. To prędkość rzędu prędkości elektronów w atomie.

Kulka: $\Delta v \ge \hbar/(2m\Delta x) \approx 5\cdot10^{-26}\ \mathrm{m/s}$. Zupełnie niemierzalne.

**Zadanie 2.** Stan wzbudzony atomu żyje średnio 10 ns. Jaka jest naturalna szerokość energetyczna linii?

$\Delta E \approx \hbar/(2\tau) \approx 3\cdot10^{-8}\ \mathrm{eV}$. To bardzo mało w porównaniu z energią fotonu (ok. 2 eV), ale mierzalne spektroskopią laserową.

### Wersja z rachunkiem różniczkowym i całkowym

**Zadanie.** Funkcja falowa ma postać $\psi(x) = Ae^{-x^2/(4\sigma^2)}$. Znormalizuj ją, oblicz $\Delta x$ i prawdopodobieństwo znalezienia cząstki w przedziale $[-\sigma, \sigma]$.

$\lvert\psi\rvert^2 = A^2e^{-x^2/(2\sigma^2)}$. Z całki Gaussa $\int e^{-x^2/(2\sigma^2)}dx = \sigma\sqrt{2\pi}$, więc $A^2 = \dfrac{1}{\sigma\sqrt{2\pi}}$.

$\lvert\psi\rvert^2$ to rozkład normalny o odchyleniu $\sigma$ (01.03), więc $\langle x\rangle = 0$, $\Delta x = \sigma$, a $P(\lvert x\rvert \le \sigma) \approx 68\%$.

Rozkład pędów tej paczki też jest gaussowski, z $\Delta p = \hbar/(2\sigma)$. Iloczyn $\Delta x\Delta p = \hbar/2$, czyli paczka gaussowska ma najmniejszą możliwą nieoznaczoność (sprawdzenie numeryczne niżej).

## Typowe pułapki

- **Nieoznaczoność wynika z zakłócania pomiarem.** To podstawowa własność stanu kwantowego, a nie skutek niezgrabnych przyrządów.
- **$\lvert\psi\rvert^2$ to rozkład masy elektronu.** To prawdopodobieństwo znalezienia całego elektronu w danym miejscu.
- **$\psi$ jest mierzalna.** Mierzalne jest $\lvert\psi\rvert^2$ (i wielkości pochodne). Sama $\psi$ ma fazę, która ujawnia się tylko w interferencji.
- **Zasada dotyczy tylko małych obiektów.** Dotyczy wszystkich, ale dla ciał makroskopowych jest niezauważalna.
- **$\hbar$ i $h$.** W zasadzie nieoznaczoności jest $\hbar = h/(2\pi)$.

## Doświadczenie / symulacja

**Analogia z dźwiękiem.** Nagraj w phyphox (*Audio Spectrum*) krótkie klaśnięcie i długi ton z generatora. Krótki impuls ma bardzo szerokie widmo, a długi ton wąskie. To ta sama matematyka co $\Delta x\Delta k \ge 1/2$ (transformata Fouriera).

**Symulacja PhET:** *Interferencja kwantowa* — pojedyncze cząstki tworzące obraz interferencyjny, oraz *Stany związane kwantowe* (*Quantum Bound States*).

**Python:** paczka gaussowska — sprawdzenie $\Delta x\Delta p = \hbar/2$ transformatą Fouriera.

```python
import numpy as np

hbar = 1.0                                         # jednostki: ħ = 1
N, Lbox = 4096, 200.0
x = np.linspace(-Lbox/2, Lbox/2, N, endpoint=False)
dx = x[1] - x[0]
sigma, k0 = 2.0, 1.5
psi = np.exp(-x**2/(4*sigma**2))*np.exp(1j*k0*x)
psi /= np.sqrt(np.sum(np.abs(psi)**2)*dx)          # normalizacja

P = np.abs(psi)**2
mx = np.sum(x*P)*dx
Dx = np.sqrt(np.sum((x - mx)**2*P)*dx)

k = 2*np.pi*np.fft.fftfreq(N, d=dx)
phi = np.fft.fft(psi)
Pk = np.abs(phi)**2; Pk /= Pk.sum()
mk = np.sum(k*Pk)
Dk = np.sqrt(np.sum((k - mk)**2*Pk))
print(f"⟨x⟩ = {mx:.3f}, Δx = {Dx:.4f}; ⟨p⟩ = {mk:.3f}, Δp = {Dk:.4f}")
print(f"Δx·Δp = {Dx*Dk:.4f} (minimum ħ/2 = 0,5)")
print(f"P(|x| ≤ σ) = {np.sum(P[np.abs(x) <= sigma])*dx:.3f}")

hb, me = 1.0546e-34, 9.109e-31
print(f"elektron w 0,1 nm: Δv ≥ {hb/(2*me*1e-10):.2e} m/s")
```

## Zadania

### A. Poziom maturalny _(opcjonalnie — rozgrzewka)_

1. Jaka jest najmniejsza nieoznaczoność prędkości protonu w jądrze ($\Delta x \approx 10^{-14}\ \mathrm m$)?

<details>
<summary>Odpowiedź</summary>

$\Delta v \ge \hbar/(2m_p\Delta x) \approx 3\cdot10^6\ \mathrm{m/s}$.
</details>

2. Co oznacza, że $\lvert\psi(x)\rvert^2$ ma w pewnym punkcie wartość zero?

<details>
<summary>Odpowiedź</summary>

Że cząstki nigdy nie znajdziemy dokładnie w tym punkcie (węzeł funkcji falowej).
</details>

### B. Poziom akademicki

1. Funkcja falowa cząstki w przedziale $[0, L]$ ma postać $\psi = A\sin(\pi x/L)$, a poza nim zero. Znormalizuj ją i oblicz prawdopodobieństwo znalezienia cząstki w przedziale $[0, L/4]$.

<details>
<summary>Odpowiedź</summary>

$A = \sqrt{2/L}$. $P = \dfrac2L\displaystyle\int_0^{L/4}\sin^2\frac{\pi x}{L}dx = \frac14 - \frac{1}{2\pi} \approx 0{,}091$.
</details>

2. Oszacuj energię stanu podstawowego atomu wodoru z zasady nieoznaczoności. Przyjmij $p \approx \hbar/r$ i zminimalizuj $E(r) = \dfrac{\hbar^2}{2mr^2} - \dfrac{ke^2}{r}$.

<details>
<summary>Odpowiedź</summary>

$dE/dr = 0 \Rightarrow r = \dfrac{\hbar^2}{mke^2} \approx 0{,}053\ \mathrm{nm}$ (promień Bohra), $E_{\min} = -\dfrac{mk^2e^4}{2\hbar^2} \approx -13{,}6\ \mathrm{eV}$. Zasada nieoznaczoności zapobiega spadkowi elektronu na jądro.
</details>

3. Wiązka elektronów przechodzi przez szczelinę o szerokości $a$. Pokaż, że kąt ugięcia z zasady nieoznaczoności, $\theta \sim \Delta p_y/p$, jest zgodny co do rzędu wielkości z dyfrakcją $\theta \sim \lambda/a$.

<details>
<summary>Odpowiedź</summary>

$\Delta y = a$, $\Delta p_y \sim \hbar/a$, więc $\theta \sim \dfrac{\hbar}{ap} = \dfrac{\lambda}{2\pi a}$, czyli $\sim\lambda/a$ z dokładnością do czynnika liczbowego.
</details>

## Źródła

- OpenStax, *Fizyka dla szkół wyższych*, t. 3, rozdz. 7 — §7.1 (funkcje falowe) i §7.2 (zasada nieoznaczoności Heisenberga).
- Halliday, Resnick, Walker, *Podstawy fizyki* — wyd. 2015: t. 5, §38.6–38.7; wyd. 1: t. 5, §39.7–39.8.
- Symulacje PhET *Interferencja kwantowa* i *Stany związane kwantowe*.
