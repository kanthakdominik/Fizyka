# 10.03 — Superpozycja, interferencja i fale stojące

> **Moduł:** [10 — Fale mechaniczne i akustyka](README.md) · **Poziom:** 🟢 matura R · **Status:** ✅ pełny
>
> **Czytaj:**
>
> - OpenStax, *Fizyka dla szkół wyższych*, t. 1, rozdz. 16: [§16.5–16.6](https://openstax.org/books/fizyka-dla-szk%C3%B3%C5%82-wy%C5%BCszych-tom-1/pages/16-5-interferencja-fal) · [wstęp do rozdziału](https://openstax.org/books/fizyka-dla-szk%C3%B3%C5%82-wy%C5%BCszych-tom-1/pages/16-wstep)
> - Halliday, Resnick, Walker, *Podstawy fizyki*, wyd. 2015, t. 2: §16.5–16.7 (s. 173), §17.3 (s. 208)
> - Halliday, Resnick, Walker, *Podstawy fizyki*, wyd. 1 (2003), t. 2: [§17.8–17.12, s. 136](https://home.agh.edu.pl/~czapli/Resnick_2.pdf#page=152), [§18.4, s. 162](https://home.agh.edu.pl/~czapli/Resnick_2.pdf#page=178) — PDF z serwera AGH

← [Prędkość fali, energia i równanie falowe](02-predkosc-i-energia-fali.md) · [spis modułu](README.md) · [Zasada Huygensa: odbicie, załamanie i dyfrakcja fal](04-huygens-dyfrakcja-zalamanie.md) →

## Po co to jest

Dwie fale w tym samym miejscu po prostu się dodają. Ta prosta zasada daje ciszę w słuchawkach z redukcją szumów, „martwe punkty” na sali koncertowej i barwne smugi na bańce mydlanej (18). Fale odbite od końców struny lub ścian rury tworzą **fale stojące**, a z nich biorą się dźwięki instrumentów muzycznych (10.06), mody drgań budynków i mostów, a w fizyce kwantowej skwantowane poziomy energii elektronu w atomie (20).

## Teoria w pigułce

**Zasada superpozycji.** W ośrodku liniowym wypadkowe wychylenie jest sumą wychyleń od poszczególnych fal: $y = y_1 + y_2$. Fale przechodzą przez siebie bez zmian.

**Interferencja dwóch fal o tej samej częstotliwości** zależy od różnicy faz w danym punkcie, tak jak przy składaniu drgań (09.06):
- **wzmocnienie** (interferencja konstruktywna), gdy fazy są zgodne;
- **wygaszenie** (interferencja destruktywna), gdy fazy są przeciwne.

Dwa źródła drgające w fazie, w odległościach $r_1$ i $r_2$ od punktu, dają w nim różnicę faz $k(r_2 - r_1)$. Stąd warunki:

$$\Delta r = m\lambda \ \text{(wzmocnienie)}, \qquad \Delta r = \left(m + \tfrac12\right)\lambda \ \text{(wygaszenie)}, \qquad m = 0, 1, 2, \dots$$

**Odbicie od końca.** Na końcu zamocowanym fala odbija się z odwróceniem fazy (grzbiet wraca jako dolina). Na końcu swobodnym odbija się bez odwrócenia.

**Fala stojąca** powstaje z dwóch jednakowych fal biegnących w przeciwne strony:

$$y = A\sin(kx - \omega t) + A\sin(kx + \omega t) = 2A\sin(kx)\cos(\omega t).$$

- Każdy punkt drga z amplitudą $2A\lvert\sin kx\rvert$, zależną od położenia.
- **Węzły** (amplituda zero) leżą w punktach $kx = n\pi$, co $\lambda/2$.
- **Strzałki** (amplituda największa) leżą w połowie między węzłami.
- Energia nie płynie wzdłuż fali stojącej, tylko przelewa się między postacią kinetyczną a potencjalną.

**Struna zamocowana na obu końcach** może drgać tylko tak, by na końcach były węzły. Mieści się na niej całkowita liczba połówek fali:

$$L = n\frac{\lambda_n}{2} \quad\Rightarrow\quad f_n = n\frac{v}{2L} = nf_1, \qquad n = 1, 2, 3, \dots$$

$f_1$ to **częstotliwość podstawowa**, a $f_n$ to kolejne **harmoniczne** (mody własne). Rury i piszczałki opisuje 10.06.

## Wzory i założenia

| Wzór | Znaczenie | Kiedy obowiązuje |
|---|---|---|
| $y = y_1 + y_2$ | zasada superpozycji | ośrodek liniowy |
| $\Delta r = m\lambda$ / $\Delta r = (m + \tfrac12)\lambda$ | wzmocnienie / wygaszenie | źródła spójne, w fazie |
| $y = 2A\sin kx\cos\omega t$ | fala stojąca | dwie jednakowe fale przeciwbieżne |
| odległość węzłów $= \lambda/2$ | — | fala stojąca |
| $f_n = nv/(2L)$ | mody struny | oba końce zamocowane |

## Przykład rozwiązany

**Zadanie 1.** Dwa głośniki grają w fazie ton 200 Hz. Słuchacz stoi 3,00 m od jednego i 3,85 m od drugiego. Czy słyszy wzmocnienie, czy osłabienie ($v = 343\ \mathrm{m/s}$)?

$\lambda = 343/200 \approx 1{,}715\ \mathrm{m}$, $\Delta r = 0{,}85\ \mathrm{m} \approx 0{,}50\lambda$. Zachodzi prawie dokładnie wygaszenie. W praktyce dźwięk będzie wyraźnie cichszy, ale nie zniknie, bo docierają też fale odbite od ścian.

**Zadanie 2.** Struna gitary o długości drgającej 65 cm ma częstotliwość podstawową 110 Hz (struna A). Oblicz prędkość fali na strunie i trzy pierwsze harmoniczne. Jaki jest naciąg, jeśli $\mu = 7\ \mathrm{g/m}$?

$v = 2Lf_1 = 143\ \mathrm{m/s}$. Harmoniczne: 110, 220, 330 Hz. $F = \mu v^2 \approx 0{,}007\cdot143^2 \approx 143\ \mathrm{N}$ (jak ciężar ok. 15 kg).

## Typowe pułapki

- **Odległość węzłów = $\lambda$.** Wynosi $\lambda/2$.
- **W wygaszeniu energia znika.** Energia przenosi się w miejsca wzmocnienia; średnio nic nie ginie.
- **Interferencja dowolnych źródeł.** Stały obraz interferencyjny wymaga źródeł spójnych, czyli o stałej różnicy faz (np. dwa głośniki z jednego wzmacniacza).
- **Fala stojąca „stoi”, więc $v = 0$.** Składa się z dwóch fal biegnących z prędkością $v$. Wzór $f_n = nv/(2L)$ używa właśnie tej prędkości.
- **Na strunie mieści się całkowita liczba długości fali.** Mieści się całkowita liczba **połówek** fali.

## Doświadczenie / symulacja

**Dwa głośniki.** Podłącz dwa głośniki do jednego źródła tonu 500–1000 Hz (generator w phyphox lub w przeglądarce). Przechodząc wzdłuż linii równoległej do głośników, usłyszysz na przemian głośniej i ciszej. Zmierz odległość między minimami i porównaj z przewidywaniem. Najlepiej robić to na zewnątrz, gdzie jest mniej odbić.

**Symulacje PhET:** *Interferencja fal* (*Wave Interference*) i *Fala na strunie* (*Wave on a String*, tryb *Oscylator* z zamocowanym końcem; dobierz częstotliwość tak, by powstała fala stojąca) — [phet.colorado.edu/pl](https://phet.colorado.edu/pl/).

**Python:** suma dwóch fal przeciwbieżnych daje falę stojącą.

```python
import numpy as np
import matplotlib.pyplot as plt

A, L, n, v = 1.0, 0.65, 3, 143.0
lam = 2*L/n; k = 2*np.pi/lam; w = k*v
x = np.linspace(0, L, 400)
for t in np.linspace(0, np.pi/w, 6):
    y = A*np.sin(k*x - w*t) + A*np.sin(k*x + w*t)        # superpozycja
    assert np.allclose(y, 2*A*np.sin(k*x)*np.cos(w*t))    # = fala stojąca
    plt.plot(x*100, y, lw=1)
print(f"mod n = {n}: λ = {lam*100:.1f} cm, f = {n*v/(2*L):.0f} Hz, węzły co {lam/2*100:.1f} cm")
plt.xlabel("x [cm]"); plt.ylabel("y"); plt.title("fala stojąca, 3. harmoniczna"); plt.grid(True); plt.show()
```

## Zadania

### A. Poziom maturalny

1. Węzły fali stojącej na sznurze są odległe o 40 cm, a częstotliwość drgań wynosi 5 Hz. Oblicz prędkość fal biegnących w sznurze.

<details>
<summary>Odpowiedź</summary>

$\lambda = 0{,}8\ \mathrm{m}$, $v = \lambda f = 4\ \mathrm{m/s}$.
</details>

2. Struna o długości 0,5 m ma częstotliwość podstawową 200 Hz. Oblicz częstotliwość trzeciej harmonicznej i długość fali w tym modzie.

<details>
<summary>Odpowiedź</summary>

$f_3 = 600\ \mathrm{Hz}$, $\lambda_3 = 2L/3 \approx 33\ \mathrm{cm}$.
</details>

3. Gitarzysta skraca palcem strunę z 65 cm do 49 cm. Jak zmienia się częstotliwość podstawowa 110 Hz?

<details>
<summary>Odpowiedź</summary>

$f \propto 1/L$, więc $110\cdot65/49 \approx 146\ \mathrm{Hz}$ (ok. kwarty wyżej, dźwięk D).
</details>

4. Dwa głośniki w fazie wysyłają ton o długości fali 0,5 m. W jakich punktach słuchacz usłyszy wygaszenie: $\Delta r = 0{,}25\ \mathrm{m}$, $0{,}5\ \mathrm{m}$, $0{,}75\ \mathrm{m}$?

<details>
<summary>Odpowiedź</summary>

Przy 0,25 m i 0,75 m (nieparzysta liczba połówek fali). Przy 0,5 m zachodzi wzmocnienie.
</details>

### B. Poziom akademicki _(opcjonalnie — rozszerzenie z rachunkiem)_

1. Wyprowadź postać fali stojącej z tożsamości $\sin a + \sin b = 2\sin\frac{a + b}{2}\cos\frac{a - b}{2}$.

<details>
<summary>Odpowiedź</summary>

$a = kx - \omega t$, $b = kx + \omega t$: $\tfrac{a + b}{2} = kx$, $\tfrac{a - b}{2} = -\omega t$, więc $y = 2A\sin kx\cos\omega t$.
</details>

2. Dwa głośniki w fazie stoją w punktach $x = 0$ i $x = 3\ \mathrm{m}$ i grają ton o długości fali 1 m. Znajdź na odcinku między nimi punkty wygaszenia.

<details>
<summary>Odpowiedź</summary>

$\Delta r = \lvert(3 - x) - x\rvert = \lvert3 - 2x\rvert = (m + \tfrac12)\cdot1$, stąd $x = 0{,}25;\ 0{,}75;\ 1{,}25;\ 1{,}75;\ 2{,}25;\ 2{,}75\ \mathrm{m}$, czyli co $\lambda/2$ (fala stojąca).
</details>

3. Pokaż, że w fali stojącej $y = 2A\sin kx\cos\omega t$ średni w czasie strumień energii przez dowolny punkt jest zerowy. Moc przekazywana przez punkt struny to $P = -F\,\dfrac{\partial y}{\partial x}\dfrac{\partial y}{\partial t}$.

<details>
<summary>Odpowiedź</summary>

$P = -F\cdot2Ak\cos kx\cos\omega t\cdot(-2A\omega\sin kx\sin\omega t) = F A^2k\omega\sin2kx\sin2\omega t$. Średnia z $\sin2\omega t$ w okresie wynosi zero.
</details>

## Źródła

- OpenStax, *Fizyka dla szkół wyższych*, t. 1, rozdz. 16 — §16.5 (interferencja fal) i §16.6 (fale stojące i rezonans).
- Halliday, Resnick, Walker, *Podstawy fizyki* — wyd. 2015: t. 2, §16.5–16.7, §17.3; wyd. 1: t. 2, §17.8–17.12, §18.4.
- Symulacje PhET *Interferencja fal* i *Fala na strunie*.
