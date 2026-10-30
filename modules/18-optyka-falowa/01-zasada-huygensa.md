# 18.01 — Zasada Huygensa dla światła

> **Moduł:** [18 — Optyka falowa](README.md) · **Poziom:** 🟢 matura R · **Status:** ✅ pełny
>
> **Czytaj:**
>
> - OpenStax, *Fizyka dla szkół wyższych*, t. 3, rozdz. 1: [§1.6](https://openstax.org/books/fizyka-dla-szk%C3%B3%C5%82-wy%C5%BCszych-tom-3/pages/1-6-zasada-huygensa) · [wstęp do rozdziału](https://openstax.org/books/fizyka-dla-szk%C3%B3%C5%82-wy%C5%BCszych-tom-3/pages/1-wstep)
> - Halliday, Resnick, Walker, *Podstawy fizyki*, wyd. 2015, t. 4: §35.1 (s. 97)
> - Halliday, Resnick, Walker, *Podstawy fizyki*, wyd. 1 (2003), t. 4: [§36.1–36.3, s. 75](https://home.agh.edu.pl/~czapli/Resnick_4.pdf#page=90) — PDF z serwera AGH

← (początek modułu) · [spis modułu](README.md) · [Doświadczenie Younga](02-doswiadczenie-younga.md) →

## Po co to jest

Optyka geometryczna (17) traktuje światło jak promienie. Gdy rozmiary szczelin i warstw są porównywalne z długością fali, światło zachowuje się jak fala: interferuje i ugina się. Ten moduł zaczyna się od narzędzi potrzebnych do opisu tych zjawisk: zasady Huygensa, długości fali w ośrodku, drogi optycznej i spójności. Bez nich nie da się zrozumieć barw baniek mydlanych, powłok antyrefleksyjnych, interferometrów mierzących fale grawitacyjne ani granicy rozdzielczości mikroskopów.

## Teoria w pigułce

**Zasada Huygensa** (10.04): każdy punkt czoła fali jest źródłem fali cząstkowej, a nowe czoło to ich obwiednia. Fresnel uzupełnił ją o interferencję fal cząstkowych, co pozwoliło liczyć dyfrakcję (zasada Huygensa–Fresnela). Z zasady Huygensa wynikają prawo odbicia i prawo załamania z $n = c/v$ (17.02). Wynika z niej też, że światło w ośrodku gęstszym biegnie **wolniej**, co rozstrzygnęło spór z korpuskularną teorią Newtona (pomiar Foucaulta, 1850).

**Długość fali w ośrodku.** Częstotliwość się nie zmienia, więc

$$\lambda_n = \frac{\lambda}{n}.$$

**Droga optyczna** to iloczyn drogi geometrycznej i współczynnika załamania, $nL$. Mówi, ile długości fali (w próżni) mieści się na odcinku $L$ w ośrodku. Różnica faz dwóch fal, które przebyły drogi optyczne $n_1L_1$ i $n_2L_2$, wynosi

$$\Delta\varphi = \frac{2\pi}{\lambda}(n_2L_2 - n_1L_1).$$

To podstawa wszystkich obliczeń interferencji.

**Zmiana fazy przy odbiciu.** Fala odbita od ośrodka o **większym** współczynniku załamania zmienia fazę o $\pi$ (pół długości fali), jak fala na linie odbita od zamocowanego końca (10.03). Odbita od ośrodka o mniejszym $n$ nie zmienia fazy. To ważne w cienkich warstwach (18.04).

**Spójność (koherencja).** Stały obraz interferencyjny dają tylko fale o stałej różnicy faz. Zwykłe źródła (żarówka, Słońce) emitują krótkie, niezależne ciągi fal, więc dwa różne źródła nie interferują. Interferencję otrzymuje się, dzieląc światło z jednego źródła na dwie wiązki (szczeliny, odbicie od dwóch powierzchni, półprzepuszczalne lustro). **Droga spójności** $l_c \approx \lambda^2/\Delta\lambda$ to największa różnica dróg, przy której prążki są jeszcze widoczne:
- światło białe: ok. 1 μm;
- dioda LED: kilkanaście μm;
- dobry laser: od centymetrów do kilometrów.

## Wzory i założenia

| Wzór | Znaczenie | Kiedy obowiązuje |
|---|---|---|
| $\lambda_n = \lambda/n$ | długość fali w ośrodku | — |
| $\Delta\varphi = (2\pi/\lambda)\Delta(nL)$ | różnica faz z różnicy dróg optycznych | — |
| odbicie od większego $n$: przesunięcie fazy $\pi$ | — | padanie prawie prostopadłe |
| $l_c \approx \lambda^2/\Delta\lambda$ | droga spójności | — |

## Przykład rozwiązany

**Zadanie.** Wiązkę światła 550 nm podzielono na dwie. Jedna przechodzi przez płytkę szklaną ($n = 1{,}5$) o grubości 1 cm, druga przez tę samą drogę w powietrzu. Oblicz różnicę dróg optycznych w długościach fali. Czy prążki będą widoczne dla diody LED o szerokości widma 20 nm?

$\Delta = (n - 1)L = 0{,}5\ \mathrm{cm}$, czyli $0{,}005/550\cdot10^{-9} \approx 9100$ długości fali.

Droga spójności LED: $l_c \approx (550\ \mathrm{nm})^2/20\ \mathrm{nm} \approx 15\ \mu\mathrm m$, dużo mniej niż 5 mm. Prążki nie będą widoczne. Laser o drodze spójności rzędu centymetrów lub więcej je da.

## Typowe pułapki

- **Przy załamaniu zmienia się częstotliwość.** Zmienia się długość fali i prędkość.
- **Dwie żarówki interferują.** Nie, bo nie są spójne. Prążki daje podział światła z jednego źródła.
- **Różnica dróg geometrycznych.** W ośrodkach liczy się różnica dróg **optycznych** $nL$.
- **Zmiana fazy przy każdym odbiciu.** Tylko przy odbiciu od ośrodka o większym $n$.

## Doświadczenie / symulacja

**Fale na wodzie.** W kuwecie falowej (lub w brytfannie z wodą) puść płaską falę na przeszkodę ze szczeliną i na granicę płytkiej wody. Zobacz, że czoła fal wychodzące ze szczeliny są koliste, a przy przejściu na płyciznę fala skraca się i zmienia kierunek. To zasada Huygensa w działaniu.

**Symulacja PhET:** *Interferencja fal* (*Wave Interference*) — zakładka *Światło*, jedna i dwie szczeliny ([phet.colorado.edu/pl](https://phet.colorado.edu/pl/)).

**Python:** różnica faz z drogi optycznej i widzialność prążków w zależności od drogi spójności (model widma gaussowskiego).

```python
import numpy as np
import matplotlib.pyplot as plt

lam0 = 550e-9
L, n = 0.01, 1.5
print(f"różnica dróg optycznych: {(n - 1)*L/lam0:.0f} długości fali")

for nazwa, dlam in [("światło białe", 300e-9), ("LED", 20e-9), ("laser He-Ne", 1e-12)]:
    print(f"{nazwa:14s}: droga spójności ≈ {lam0**2/dlam:.2e} m")

dlam = 20e-9                                         # LED: widzialność prążków ~ |γ(Δ)|
delta = np.linspace(0, 60e-6, 1000)
lams = np.linspace(lam0 - 3*dlam, lam0 + 3*dlam, 401)
w = np.exp(-((lams - lam0)/(dlam/2.355))**2/2)       # widmo gaussowskie o szerokości połówkowej dlam
I = [np.sum(w*(1 + np.cos(2*np.pi*d/lams)))/np.sum(w) for d in delta]
plt.plot(delta*1e6, I)
plt.xlabel("różnica dróg [µm]"); plt.ylabel("natężenie (względne)"); plt.title("prążki zanikają po kilkunastu µm (LED)"); plt.grid(True); plt.show()
```

## Zadania

### A. Poziom maturalny

1. Światło czerwone (650 nm) przechodzi do wody ($n = 1{,}33$). Jaka jest jego długość fali w wodzie? Czy zmienia barwę?

<details>
<summary>Odpowiedź</summary>

ok. 489 nm. Barwa się nie zmienia, bo oko reaguje na częstotliwość, która pozostaje taka sama.
</details>

2. Dlaczego dwie latarki świecące na ten sam ekran nie dają prążków interferencyjnych?

<details>
<summary>Odpowiedź</summary>

Ich fale nie są spójne: różnica faz zmienia się chaotycznie miliardy razy na sekundę i prążki się uśredniają.
</details>

3. O ile długości fali (500 nm) przesunie się faza, gdy na drodze wiązki postawimy folię o grubości 10 μm i $n = 1{,}5$?

<details>
<summary>Odpowiedź</summary>

$(n - 1)t/\lambda = 0{,}5\cdot10^{-5}/5\cdot10^{-7} = 10$ długości fali.
</details>

### B. Poziom akademicki _(opcjonalnie — rozszerzenie z rachunkiem)_

1. Wyprowadź prawo załamania z zasady Huygensa, rysując czoło fali padające ukośnie na granicę i fale cząstkowe biegnące z prędkościami $v_1$ i $v_2$.

<details>
<summary>Odpowiedź</summary>

W czasie $t$ jeden koniec czoła przebiega w ośrodku 1 drogę $v_1t = d\sin\theta_1$, a fala cząstkowa z drugiego końca w ośrodku 2 drogę $v_2t = d\sin\theta_2$ ($d$ — odcinek granicy). Stąd $\sin\theta_1/\sin\theta_2 = v_1/v_2 = n_2/n_1$.
</details>

2. Pokaż, że droga spójności wynosi w przybliżeniu $\lambda^2/\Delta\lambda$, żądając, by różnica faz dla skrajnych długości fali $\lambda$ i $\lambda + \Delta\lambda$ przy różnicy dróg $l$ była mniejsza od $2\pi$.

<details>
<summary>Odpowiedź</summary>

$2\pi l\left(\dfrac1\lambda - \dfrac1{\lambda + \Delta\lambda}\right) \approx 2\pi l\dfrac{\Delta\lambda}{\lambda^2} < 2\pi \Rightarrow l < \lambda^2/\Delta\lambda$.
</details>

## Źródła

- OpenStax, *Fizyka dla szkół wyższych*, t. 3, rozdz. 1 — §1.6: zasada Huygensa.
- Halliday, Resnick, Walker, *Podstawy fizyki* — wyd. 2015: t. 4, §35.1; wyd. 1: t. 4, §36.1–36.3.
- Symulacja PhET *Interferencja fal*.
