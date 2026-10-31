# 09.02 — Energia w ruchu harmonicznym

> **Moduł:** [09 — Drgania](README.md) · **Poziom:** 🟢 matura R · **Status:** ✅ pełny
>
> **Czytaj:**
>
> - OpenStax, *Fizyka dla szkół wyższych*, t. 1, rozdz. 15: [§15.2](https://openstax.org/books/fizyka-dla-szk%C3%B3%C5%82-wy%C5%BCszych-tom-1/pages/15-2-energia-w-ruchu-harmonicznym) · [wstęp do rozdziału](https://openstax.org/books/fizyka-dla-szk%C3%B3%C5%82-wy%C5%BCszych-tom-1/pages/15-wstep)
> - Halliday, Resnick, Walker, *Podstawy fizyki*, wyd. 2015, t. 2: §15.2 (s. 127)
> - Halliday, Resnick, Walker, *Podstawy fizyki*, wyd. 1 (2003), t. 2: [§16.4, s. 100](https://home.agh.edu.pl/~czapli/Resnick_2.pdf#page=116) — PDF z serwera AGH

← [Ruch harmoniczny prosty i jego równanie](01-ruch-harmoniczny.md) · [spis modułu](README.md) · [Wahadło matematyczne, fizyczne i torsyjne](03-wahadla.md) →

## Po co to jest

Opis energetyczny daje najprostsze odpowiedzi na pytania o drgania: jaka jest prędkość w danym punkcie, jak amplituda zależy od energii, gdzie energie kinetyczna i potencjalna są równe. W drganiach energia przelewa się cyklicznie między dwiema formami — tak samo jak w obwodzie LC między polem elektrycznym i magnetycznym (15.05) i w fali między odkształceniem a ruchem (10.02).

## Teoria w pigułce

**Energia potencjalna sprężystości:** $E_p = \tfrac12kx^2$. **Energia kinetyczna:** $E_k = \tfrac12mv^2$.

Dla $x = A\cos(\omega t + \varphi)$ i $k = m\omega^2$:

$$E_p = \tfrac12kA^2\cos^2(\omega t + \varphi), \qquad E_k = \tfrac12kA^2\sin^2(\omega t + \varphi),$$

$$E = E_k + E_p = \tfrac12kA^2 = \tfrac12mv_{\max}^2 = \text{const}.$$

Energia całkowita jest proporcjonalna do **kwadratu amplitudy**. Obie energie zmieniają się z częstotliwością dwa razy większą niż wychylenie i średnio każda wynosi połowę energii całkowitej.

**Prędkość w funkcji położenia** — z zasady zachowania energii:

$$v(x) = \pm\omega\sqrt{A^2 - x^2}.$$

**Wykres energii potencjalnej** to parabola; ruch odbywa się między punktami zwrotu $x = \pm A$, gdzie $E_p = E$ (04.06).

## Wzory i założenia

| Wzór | Znaczenie | Kiedy obowiązuje |
|---|---|---|
| $E = \tfrac12kA^2 = \tfrac12m\omega^2A^2$ | energia drgań | brak tłumienia |
| $E_p = \tfrac12kx^2$, $\ E_k = E - E_p$ | podział energii | — |
| $v(x) = \omega\sqrt{A^2 - x^2}$ | prędkość w położeniu $x$ | — |
| $\overline{E_k} = \overline{E_p} = E/2$ | średnie w okresie | — |
| $E_k = E_p$ dla $x = \pm A/\sqrt2$ | punkt równego podziału | — |

## Przykład rozwiązany

**Zadanie.** Ciężarek o masie 0,5 kg drga na sprężynie o współczynniku 200 N/m z amplitudą 5 cm. Oblicz energię drgań oraz prędkość, energię kinetyczną i potencjalną w punkcie $x = 3\ \mathrm{cm}$.

$E = \tfrac12\cdot200\cdot0{,}05^2 = 0{,}25\ \mathrm{J}$.

$E_p = \tfrac12\cdot200\cdot0{,}03^2 = 0{,}09\ \mathrm{J}$, $E_k = 0{,}16\ \mathrm{J}$, $v = \sqrt{2\cdot0{,}16/0{,}5} = 0{,}8\ \mathrm{m/s}$ (ze wzoru: $20\sqrt{0{,}0025 - 0{,}0009} = 0{,}8$).

## Typowe pułapki

- **Energia proporcjonalna do amplitudy.** Do kwadratu amplitudy.
- **W połowie amplitudy energie są równe.** Dla $x = A/2$: $E_p = E/4$. Równe są dla $x = A/\sqrt2$.
- **Energia potencjalna grawitacji przy sprężynie pionowej.** Mierząc wychylenie od nowego położenia równowagi, można ją pominąć — suma grawitacyjnej i sprężystej zachowuje się jak $\tfrac12kx^2$ (zadanie B2).
- **Częstotliwość zmian energii.** Energie zmieniają się z częstotliwością $2f$.

## Doświadczenie / symulacja

**Symulacja PhET:** *Masy i sprężyny* — zakładka *Energia*: obserwuj słupki energii kinetycznej, potencjalnej grawitacyjnej i sprężystości; włącz tarcie i zobacz energię termiczną.

**Python:** energie w funkcji czasu i położenia.

```python
import numpy as np
import matplotlib.pyplot as plt

m, k, A = 0.5, 200.0, 0.05
w = np.sqrt(k/m)
t = np.linspace(0, 2*2*np.pi/w, 500)
x = A*np.cos(w*t); v = -A*w*np.sin(w*t)
Ek, Ep = 0.5*m*v**2, 0.5*k*x**2
print(f"E = {0.5*k*A**2:.3f} J, średnio Ek = {Ek.mean():.3f} J, Ep = {Ep.mean():.3f} J")
print(f"Ek = Ep dla x = {A/np.sqrt(2)*100:.2f} cm")

fig, ax = plt.subplots(1, 2, figsize=(9, 3.5))
ax[0].plot(t, Ek, label="Ek"); ax[0].plot(t, Ep, label="Ep"); ax[0].plot(t, Ek + Ep, "k--", label="E")
ax[0].set_xlabel("t [s]"); ax[0].set_ylabel("E [J]"); ax[0].legend(); ax[0].grid(True)
xs = np.linspace(-A, A, 200)
ax[1].plot(xs*100, 0.5*k*xs**2, label="Ep(x)"); ax[1].axhline(0.5*k*A**2, ls="--", color="gray", label="E")
ax[1].set_xlabel("x [cm]"); ax[1].legend(); ax[1].grid(True)
plt.tight_layout(); plt.show()
```

## Zadania

### A. Poziom maturalny

1. Jak zmieni się energia drgań, gdy amplituda wzrośnie dwukrotnie?

<details>
<summary>Odpowiedź</summary>

Wzrośnie czterokrotnie.
</details>

2. Klocek o masie 0,2 kg drga na sprężynie ($k = 50\ \mathrm{N/m}$) z amplitudą 10 cm. Oblicz największą prędkość.

<details>
<summary>Odpowiedź</summary>

$v_{\max} = A\sqrt{k/m} \approx 1{,}58\ \mathrm{m/s}$.
</details>

3. W jakim położeniu energia kinetyczna jest równa potencjalnej? Jaką część amplitudy stanowi to wychylenie?

<details>
<summary>Odpowiedź</summary>

$x = A/\sqrt2 \approx 0{,}71A$.
</details>

4. Energia drgań wynosi 0,4 J, a w położeniu $x = 2\ \mathrm{cm}$ energia kinetyczna wynosi 0,3 J. Oblicz współczynnik sprężystości i amplitudę.

<details>
<summary>Odpowiedź</summary>

$E_p = 0{,}1 = \tfrac12k\cdot0{,}0004 \Rightarrow k = 500\ \mathrm{N/m}$; $A = \sqrt{2\cdot0{,}4/500} = 4\ \mathrm{cm}$.
</details>

### B. Poziom akademicki _(opcjonalnie — rozszerzenie z rachunkiem)_

1. Pokaż, że średnie (w okresie) energie kinetyczna i potencjalna są równe.

<details>
<summary>Odpowiedź</summary>

$\overline{\sin^2} = \overline{\cos^2} = \tfrac12$, więc obie średnie wynoszą $\tfrac14kA^2 = E/2$.
</details>

2. Ciężarek wisi na sprężynie pionowej. Pokaż, że suma energii sprężystości i grawitacyjnej, liczona względem położenia równowagi $x_0 = mg/k$, wynosi $\tfrac12ky^2 + \text{const}$, gdzie $y$ to wychylenie od równowagi.

<details>
<summary>Odpowiedź</summary>

$\tfrac12k(x_0 + y)^2 - mg(x_0 + y) = \tfrac12ky^2 + (kx_0 - mg)y + \text{const} = \tfrac12ky^2 + \text{const}$.
</details>

3. Z zasady zachowania energii $\tfrac12m\dot{x}^2 + \tfrac12kx^2 = E$ wyprowadź równanie ruchu, różniczkując po czasie.

<details>
<summary>Odpowiedź</summary>

$m\dot{x}\ddot{x} + kx\dot{x} = 0 \Rightarrow m\ddot{x} = -kx$.
</details>

### C. Zadania z arkuszy maturalnych CKE

Zadania z egzaminów maturalnych (poziom rozszerzony, formuła 2023), w których ten temat jest potrzebny. Rozwiąż je samodzielnie, a potem porównaj z zasadami oceniania. Pełne zestawienie: [matura/README.md](../../matura/README.md).

- Maj 2024, zad. 3.1 — siły, energia i przyspieszenie w oscylatorze sprężynowym (temat pomocniczy) ([arkusz](https://cke.gov.pl/images/_EGZAMIN_MATURALNY_OD_2023/Arkusze_egzaminacyjne/2024/Fizyka/MFAP-R0-100-A-2405-arkusz.pdf), [zasady oceniania](https://cke.gov.pl/egzamin-maturalny/egzamin-maturalny-w-formule-2023/arkusze/2024-2/))
- Maj 2024, zad. 3.3 — siła sprężystości w najniższym położeniu drgającego ciała (temat pomocniczy) ([arkusz](https://cke.gov.pl/images/_EGZAMIN_MATURALNY_OD_2023/Arkusze_egzaminacyjne/2024/Fizyka/MFAP-R0-100-A-2405-arkusz.pdf), [zasady oceniania](https://cke.gov.pl/egzamin-maturalny/egzamin-maturalny-w-formule-2023/arkusze/2024-2/))

## Źródła

- OpenStax, *Fizyka dla szkół wyższych*, t. 1, rozdz. 15 — §15.2: energia w ruchu harmonicznym.
- Halliday, Resnick, Walker, *Podstawy fizyki* — wyd. 2015: t. 2, §15.2; wyd. 1: t. 2, §16.4.
