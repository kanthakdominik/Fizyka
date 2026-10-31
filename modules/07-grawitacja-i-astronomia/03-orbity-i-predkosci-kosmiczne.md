# 07.03 — Orbity, satelity i prędkości kosmiczne

> **Moduł:** [07 — Grawitacja i elementy astronomii](README.md) · **Poziom:** 🟢 matura R · **Status:** ✅ pełny
>
> **Czytaj:**
>
> - OpenStax, *Fizyka dla szkół wyższych*, t. 1, rozdz. 13: [§13.4](https://openstax.org/books/fizyka-dla-szk%C3%B3%C5%82-wy%C5%BCszych-tom-1/pages/13-4-orbity-satelitow-i-ich-energia) · [wstęp do rozdziału](https://openstax.org/books/fizyka-dla-szk%C3%B3%C5%82-wy%C5%BCszych-tom-1/pages/13-wstep)
> - Halliday, Resnick, Walker, *Podstawy fizyki*, wyd. 2015, t. 2: §13.7 (s. 58)
> - Halliday, Resnick, Walker, *Podstawy fizyki*, wyd. 1 (2003), t. 2: [§14.8, s. 46](https://home.agh.edu.pl/~czapli/Resnick_2.pdf#page=62) — PDF z serwera AGH

← [Natężenie pola, potencjał i energia grawitacyjna](02-pole-i-potencjal-grawitacyjny.md) · [spis modułu](README.md) · [Prawa Keplera](04-prawa-keplera.md) →

## Po co to jest

Satelity telekomunikacyjne, GPS, Międzynarodowa Stacja Kosmiczna, Księżyc — wszystkie poruszają się po orbitach, na których grawitacja pełni rolę siły dośrodkowej. Z dwóch wzorów (prawa grawitacji i siły dośrodkowej) wynikają prędkości kosmiczne, okresy obiegu, wysokość orbity geostacjonarnej i energia potrzebna do zmiany orbity. To jeden z najczęstszych tematów maturalnych.

## Teoria w pigułce

**Orbita kołowa.** Grawitacja jest siłą dośrodkową:

$$\frac{GMm}{r^2} = \frac{mv^2}{r} \Rightarrow v = \sqrt{\frac{GM}{r}}, \qquad T = \frac{2\pi r}{v} = 2\pi\sqrt{\frac{r^3}{GM}}.$$

Prędkość orbitalna nie zależy od masy satelity. Im wyżej, tym wolniej i dłużej trwa obieg ($T^2 \propto r^3$ — III prawo Keplera, 07.04).

**Pierwsza prędkość kosmiczna** — prędkość orbity kołowej tuż nad powierzchnią (bez atmosfery):

$$v_I = \sqrt{\frac{GM}{R}} = \sqrt{gR} \approx 7{,}9\ \mathrm{km/s}.$$

**Druga prędkość kosmiczna** — ucieczki: $v_{II} = \sqrt2v_I \approx 11{,}2\ \mathrm{km/s}$ (07.02).

**Nieważkość** na stacji kosmicznej nie oznacza braku grawitacji (na 400 km $g$ jest tylko o 11% mniejsze), lecz to, że stacja i astronauci spadają swobodnie — razem, „obok” Ziemi.

**Energia na orbicie kołowej.** Z $mv^2 = GMm/r$:

$$E_k = \frac{GMm}{2r}, \qquad U = -\frac{GMm}{r}, \qquad E = E_k + U = -\frac{GMm}{2r} = -E_k.$$

Energia całkowita jest ujemna (orbita związana). Paradoks: satelita hamowany przez atmosferę traci energię, schodzi niżej i… **przyspiesza**.

**Orbita geostacjonarna** — okres równy dobie gwiazdowej, orbita w płaszczyźnie równika, ten sam kierunek obrotu co Ziemia; satelita „wisi” nad jednym punktem. Promień ok. 42 160 km (35 800 km nad powierzchnią).

## Wzory i założenia

| Wzór | Znaczenie | Kiedy obowiązuje |
|---|---|---|
| $v = \sqrt{GM/r}$ | prędkość na orbicie kołowej | $m \ll M$ |
| $T = 2\pi\sqrt{r^3/GM}$ | okres obiegu | orbita kołowa |
| $v_I = \sqrt{gR} \approx 7{,}9\ \mathrm{km/s}$ | I prędkość kosmiczna | Ziemia, bez atmosfery |
| $v_{II} = \sqrt{2gR} \approx 11{,}2\ \mathrm{km/s}$ | II prędkość kosmiczna | j.w. |
| $E = -GMm/(2r)$ | energia na orbicie kołowej | $U(\infty) = 0$ |
| $r_{\text{geo}} = \sqrt[3]{GMT^2/(4\pi^2)}$ | orbita geostacjonarna | $T$ — doba gwiazdowa |

## Przykład rozwiązany

**Zadanie 1.** Międzynarodowa Stacja Kosmiczna krąży na wysokości ok. 420 km. Oblicz jej prędkość i okres obiegu ($GM = 3{,}986\cdot10^{14}\ \mathrm{m^3/s^2}$, $R = 6371\ \mathrm{km}$).

$r = 6{,}791\cdot10^6\ \mathrm{m}$, $v = \sqrt{GM/r} \approx 7{,}66\ \mathrm{km/s}$, $T = 2\pi r/v \approx 5570\ \mathrm{s} \approx 93\ \mathrm{min}$ — ok. 15,5 obiegu na dobę.

**Zadanie 2.** Na jakiej wysokości krąży satelita geostacjonarny?

$r = \sqrt[3]{\dfrac{GMT^2}{4\pi^2}} = \sqrt[3]{\dfrac{3{,}986\cdot10^{14}\cdot86\,164^2}{4\pi^2}} \approx 4{,}216\cdot10^7\ \mathrm{m}$; wysokość $\approx 35\,800\ \mathrm{km}$. Sygnał radiowy potrzebuje ok. 0,24 s na drogę w górę i w dół — opóźnienie odczuwalne w rozmowach przez satelitę.

### Wersja z rachunkiem różniczkowym i całkowym

**Zadanie.** Ile energii trzeba, żeby przenieść satelitę o masie 1000 kg z orbity kołowej na wysokości 400 km na orbitę geostacjonarną?

$$\Delta E = \frac{GMm}{2}\left(\frac{1}{r_1} - \frac{1}{r_2}\right) = \frac{3{,}986\cdot10^{17}}{2}\left(\frac{1}{6{,}771\cdot10^6} - \frac{1}{4{,}216\cdot10^7}\right) \approx 2{,}5\cdot10^{10}\ \mathrm{J}.$$

Energia kinetyczna satelity **maleje** (z 29,4 do 4,7 GJ), a potencjalna rośnie dwa razy bardziej — stąd dodatni bilans. W praktyce zmianę orbity wykonuje się dwoma impulsami silnika (orbita transferowa Hohmanna).

**Pochodna energii po promieniu.** $\dfrac{dE}{dr} = \dfrac{GMm}{2r^2} > 0$ — wyższa orbita ma większą energię, choć mniejszą prędkość. Opór atmosfery zmniejsza $E$, więc $r$ maleje, a $v = \sqrt{GM/r}$ rośnie.

## Typowe pułapki

- **Prędkość orbitalna zależy od masy satelity.** Nie zależy — masa się skraca.
- **$h$ zamiast $r$.** We wzorach $r = R + h$.
- **Wyższa orbita = szybszy satelita.** Odwrotnie.
- **Nieważkość = brak grawitacji.** Nieważkość to stan swobodnego spadku.
- **Doba słoneczna dla orbity geostacjonarnej.** Właściwa jest doba gwiazdowa (23 h 56 min), choć różnica w wyniku jest niewielka.

## Doświadczenie / symulacja

**Symulacja PhET:** *Grawitacja i orbity* — zmieniaj prędkość Ziemi wokół Słońca i obserwuj przejście od orbity kołowej przez eliptyczną do ucieczki.

**Obserwacja ISS.** Sprawdź w serwisie *Spot the Station* (NASA) lub w aplikacji astronomicznej, kiedy stacja przelatuje nad Twoją miejscowością. Zmierz czas przelotu od horyzontu do horyzontu (ok. 5–6 min) i porównaj z prostym modelem geometrycznym.

**Python:** prędkość, okres i energia na orbitach kołowych od niskiej orbity do Księżyca.

```python
import numpy as np
import matplotlib.pyplot as plt

GM, R = 3.986e14, 6.371e6
h = np.logspace(5, 8.6, 300)                 # wysokość od 100 km do ~4·10⁸ m
r = R + h
v = np.sqrt(GM/r); T = 2*np.pi*r/v
for name, hh in [("ISS", 4.2e5), ("GPS", 2.02e7), ("geostacjonarna", 3.579e7)]:
    rr = R + hh
    print(f"{name:15s}: v = {np.sqrt(GM/rr)/1000:5.2f} km/s, T = {2*np.pi*np.sqrt(rr**3/GM)/3600:6.2f} h")

fig, ax = plt.subplots(1, 2, figsize=(9, 3.5))
ax[0].semilogx(h/1000, v/1000); ax[0].set_xlabel("wysokość [km]"); ax[0].set_ylabel("v [km/s]"); ax[0].grid(True, which="both")
ax[1].loglog(h/1000, T/3600); ax[1].set_xlabel("wysokość [km]"); ax[1].set_ylabel("T [h]"); ax[1].grid(True, which="both")
plt.tight_layout(); plt.show()
```

## Zadania

### A. Poziom maturalny

1. Oblicz pierwszą i drugą prędkość kosmiczną dla Ziemi.

<details>
<summary>Odpowiedź</summary>

$v_I = \sqrt{gR} \approx 7{,}9\ \mathrm{km/s}$, $v_{II} \approx 11{,}2\ \mathrm{km/s}$.
</details>

2. Oblicz okres obiegu Księżyca z jego odległości od Ziemi ($3{,}84\cdot10^8\ \mathrm{m}$).

<details>
<summary>Odpowiedź</summary>

$T = 2\pi\sqrt{r^3/GM} \approx 27{,}4$ doby (rzeczywiście 27,3 — Księżyc ma niezaniedbywalną masę).
</details>

3. Satelita A krąży na orbicie o promieniu $r$, satelita B — $4r$. Ile razy różnią się ich prędkości i okresy obiegu?

<details>
<summary>Odpowiedź</summary>

$v_A = 2v_B$; $T_B = 8T_A$.
</details>

4. Wyjaśnij, dlaczego astronauci na stacji kosmicznej są w stanie nieważkości, choć grawitacja jest tam niewiele mniejsza niż na Ziemi.

<details>
<summary>Odpowiedź</summary>

Stacja i astronauci spadają swobodnie z tym samym przyspieszeniem (grawitacja jest siłą dośrodkową); nic ich wzajemnie nie podpiera, więc nie odczuwają ciężaru.
</details>

5. Dlaczego rakiety startują na wschód i najchętniej blisko równika?

<details>
<summary>Odpowiedź</summary>

Wykorzystują prędkość obrotu Ziemi (na równiku ok. 0,46 km/s), która dodaje się do prędkości rakiety.
</details>

### B. Poziom akademicki _(opcjonalnie — rozszerzenie z rachunkiem)_

1. Pokaż, że dla orbity kołowej $E = -E_k$ i $U = -2E_k$ (twierdzenie o wiriale dla siły $1/r^2$).

<details>
<summary>Odpowiedź</summary>

$mv^2 = GMm/r \Rightarrow E_k = \dfrac{GMm}{2r} = -\dfrac{U}{2}$; $E = E_k + U = -E_k$.
</details>

2. Satelita o masie 500 kg na niskiej orbicie traci przez opór atmosfery 1 MJ energii na obieg. O ile zmienia się promień jego orbity i prędkość w jednym obiegu ($r \approx 6{,}8\cdot10^6\ \mathrm{m}$)?

<details>
<summary>Odpowiedź</summary>

$\Delta E = \dfrac{GMm}{2r^2}\Delta r \Rightarrow \Delta r = \dfrac{2r^2\Delta E}{GMm} \approx -460\ \mathrm{m}$; $\Delta v = -\dfrac{v}{2r}\Delta r \approx +0{,}26\ \mathrm{m/s}$ — satelita schodzi niżej i przyspiesza.
</details>

3. Oblicz energię potrzebną do przeniesienia satelity 1000 kg z orbity 400 km na geostacjonarną (przykład) i porównaj z energią potrzebną do wyniesienia go z powierzchni na orbitę 400 km.

<details>
<summary>Odpowiedź</summary>

Na GEO: ok. 24,7 GJ. Z powierzchni na orbitę 400 km: $E_{\text{orb}} - E_{\text{pow}} = -\dfrac{GMm}{2r} + \dfrac{GMm}{R} \approx 33{,}1\ \mathrm{GJ}$ (bez prędkości obrotu Ziemi).
</details>

### C. Zadania z arkuszy maturalnych CKE

Zadania z egzaminów maturalnych (poziom rozszerzony, formuła 2023), w których ten temat jest potrzebny. Rozwiąż je samodzielnie, a potem porównaj z zasadami oceniania. Pełne zestawienie: [matura/README.md](../../matura/README.md).

- Maj 2023, zad. 5.4 — wyprowadzenie stosunku mas dla orbit kołowych ([arkusz](https://cke.gov.pl/images/_EGZAMIN_MATURALNY_OD_2023/Arkusze_egzaminacyjne/2023/Fizyka/MFAP-R0-100-2305.pdf), [zasady oceniania](https://cke.gov.pl/images/_EGZAMIN_MATURALNY_OD_2023/Arkusze_egzaminacyjne/2023/Fizyka/MFAP-R0-100-2305-zasady.pdf))

## Źródła

- OpenStax, *Fizyka dla szkół wyższych*, t. 1, rozdz. 13 — §13.4: orbity satelitów i ich energia.
- Halliday, Resnick, Walker, *Podstawy fizyki* — wyd. 2015: t. 2, §13.7; wyd. 1: t. 2, §14.8.
- Symulacja PhET *Grawitacja i orbity*.
