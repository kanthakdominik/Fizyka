# 19.02 — Dylatacja czasu i skrócenie długości

> **Moduł:** [19 — Szczególna teoria względności](README.md) · **Poziom:** 🟢 matura R · **Status:** ✅ pełny
>
> **Czytaj:**
>
> - OpenStax, *Fizyka dla szkół wyższych*, t. 3, rozdz. 5: [§5.3–5.4](https://openstax.org/books/fizyka-dla-szk%C3%B3%C5%82-wy%C5%BCszych-tom-3/pages/5-3-dylatacja-czasu) · [wstęp do rozdziału](https://openstax.org/books/fizyka-dla-szk%C3%B3%C5%82-wy%C5%BCszych-tom-3/pages/5-wstep)
> - Halliday, Resnick, Walker, *Podstawy fizyki*, wyd. 2015, t. 4: §37.1–37.2 (s. 187)
> - Halliday, Resnick, Walker, *Podstawy fizyki*, wyd. 1 (2003), t. 4: [§38.5–38.6, s. 152](https://home.agh.edu.pl/~czapli/Resnick_4.pdf#page=167) — PDF z serwera AGH

← [Postulaty Einsteina i względność równoczesności](01-postulaty-i-rownoczesnosc.md) · [spis modułu](README.md) · [Transformacja Lorentza i składanie prędkości](03-transformacja-lorentza.md) →

## Po co to jest

Poruszający się zegar chodzi wolniej, a poruszający się pręt jest krótszy. Te efekty, choć sprzeczne z intuicją, są mierzone codziennie. Miony z promieniowania kosmicznego docierają do powierzchni Ziemi tylko dzięki dylatacji czasu. Zegary w satelitach GPS trzeba korygować, bo inaczej pozycja rozjeżdżałaby się o kilometry na dobę. Cząstki w akceleratorach żyją dziesiątki razy dłużej, niż wynikałoby z ich czasu życia w spoczynku.

## Teoria w pigułce

**Zegar świetlny.** Impuls światła odbija się między dwoma lustrami odległymi o $L$. W układzie zegara jeden „tik” (tam i z powrotem) trwa $\Delta t_0 = 2L/c$. Gdy zegar porusza się z prędkością $v$, światło biegnie po ukosie. Ponieważ jego prędkość nadal wynosi $c$ (19.01), z twierdzenia Pitagorasa:

$$\left(\frac{c\Delta t}{2}\right)^2 = L^2 + \left(\frac{v\Delta t}{2}\right)^2 \Rightarrow \Delta t = \gamma\Delta t_0, \qquad \gamma = \frac{1}{\sqrt{1 - v^2/c^2}}.$$

**Dylatacja czasu.** Odstęp czasu między dwoma zdarzeniami w tym samym miejscu w danym układzie to **czas własny** $\Delta t_0$. W układzie, w którym ten zegar się porusza, odstęp jest $\gamma$ razy dłuższy. Poruszające się zegary chodzą wolniej. Efekt jest symetryczny: każdy obserwator widzi, że zegar drugiego się późni.

**Skrócenie długości (Lorentza).** Długość pręta w układzie, w którym spoczywa, to **długość własna** $L_0$. W układzie, w którym pręt porusza się wzdłuż swojej długości, jest ona mniejsza:

$$L = \frac{L_0}{\gamma}.$$

Rozmiary poprzeczne się nie zmieniają.

**Czynnik Lorentza** $\gamma \ge 1$. Dla $v = 0{,}1c$ wynosi 1,005, dla $0{,}6c$ 1,25, dla $0{,}8c$ 1,67, dla $0{,}99c$ 7,1. Przy prędkościach codziennych ($v \ll c$) $\gamma \approx 1 + \tfrac12v^2/c^2$, a efekty są niezauważalne.

**Paradoks bliźniąt.** Bliźniak, który odbył podróż w kosmos i wrócił, jest młodszy od tego, który został. Sytuacja nie jest symetryczna, bo podróżnik zmieniał układ inercjalny (zawracał). Potwierdzono to zegarami atomowymi w samolotach (Hafele–Keating, 1971).

## Wzory i założenia

| Wzór | Znaczenie | Kiedy obowiązuje |
|---|---|---|
| $\gamma = 1/\sqrt{1 - v^2/c^2}$ | czynnik Lorentza | $v < c$ |
| $\Delta t = \gamma\Delta t_0$ | dylatacja czasu | $\Delta t_0$ — czas własny (zdarzenia w jednym miejscu) |
| $L = L_0/\gamma$ | skrócenie Lorentza | $L_0$ — długość własna, wzdłuż ruchu |
| $\gamma \approx 1 + v^2/(2c^2)$ | przybliżenie | $v \ll c$ |

## Przykład rozwiązany

**Zadanie 1.** Miony powstają w atmosferze na wysokości ok. 10 km i lecą z prędkością $0{,}998c$. Ich średni czas życia w spoczynku wynosi 2,2 μs. Jak daleko dolecą bez uwzględnienia efektów relatywistycznych, a jak daleko z nimi?

Bez: $0{,}998c\cdot2{,}2\ \mu\mathrm s \approx 660\ \mathrm m$. Prawie żaden mion nie dotarłby do ziemi.

Z dylatacją: $\gamma \approx 15{,}8$, czas życia w układzie Ziemi ok. 35 μs, zasięg ok. 10,4 km. Miony rzeczywiście są rejestrowane na powierzchni.

W układzie mionu: żyje on 2,2 μs, ale grubość atmosfery jest skrócona 15,8 razy, do ok. 630 m. Oba opisy dają ten sam wynik.

**Zadanie 2.** Satelita GPS porusza się z prędkością 3,87 km/s. O ile jego zegar spóźnia się na dobę z powodu dylatacji czasu?

$\dfrac{\Delta t - \Delta t_0}{\Delta t} \approx \dfrac{v^2}{2c^2} \approx 8{,}3\cdot10^{-11}$, czyli ok. 7 μs na dobę. Ogólna teoria względności (słabsza grawitacja na orbicie) daje przyspieszenie o ok. 46 μs na dobę. Netto zegary satelitów spieszą się o ok. 38 μs na dobę. Bez korekty błąd położenia rósłby o ok. $38\ \mu\mathrm s\cdot c \approx 11\ \mathrm{km}$ dziennie.

## Typowe pułapki

- **Który czas jest czasem własnym.** Czas własny mierzy zegar obecny przy obu zdarzeniach (np. zegar mionu przy jego narodzinach i rozpadzie). Ten czas jest najkrótszy.
- **Skrócenie jest złudzeniem optycznym.** To rzeczywisty wynik pomiaru długości (położenia końców w tej samej chwili w danym układzie). Wygląd (fotografia) to inna sprawa i daje dodatkowo obrót obrazu.
- **Skrócenie poprzeczne.** Skracają się tylko wymiary wzdłuż ruchu.
- **Paradoks bliźniąt jest symetryczny.** Nie jest, bo tylko jeden z bliźniaków zmienia układ inercjalny.
- **$\gamma$ dla małych prędkości ma znaczenie.** Dla samolotu $\gamma - 1 \sim 10^{-12}$. Mierzy się to tylko zegarami atomowymi.

## Doświadczenie / symulacja

**Detektor mionów.** Proste liczniki promieniowania kosmicznego (np. CosmicWatch, projekty otwarte na Arduino ze scyntylatorem) rejestrują ok. 1 mion na cm² na minutę na poziomie morza. Sam fakt, że miony docierają do powierzchni, jest dowodem dylatacji czasu. Porównaj liczbę zliczeń na parterze i na najwyższym piętrze lub w górach.

**Projekt Credo** (krakowski IFJ PAN) pozwala rejestrować cząstki kosmiczne kamerą telefonu.

**Python:** czynnik Lorentza, zasięg mionów i bilans zegarów GPS.

```python
import numpy as np
import matplotlib.pyplot as plt

c = 2.998e8
gamma = lambda b: 1/np.sqrt(1 - b**2)
b = 0.998
print(f"mion: γ = {gamma(b):.1f}, zasięg bez SR {b*c*2.2e-6:.0f} m, z SR {b*c*2.2e-6*gamma(b)/1e3:.1f} km")
H = 10e3
for nazwa, zasieg in [("bez SR", b*c*2.2e-6), ("z SR", b*c*2.2e-6*gamma(b))]:
    print(f"ułamek mionów docierających z 10 km ({nazwa}): {np.exp(-H/zasieg):.2e}")
v = 3874.0
GM, R, r = 3.986e14, 6.371e6, 26.56e6
sr = -v**2/(2*c**2)*86400e6
gr = GM/c**2*(1/R - 1/r)*86400e6
print(f"GPS: SR {sr:.1f} µs/d, GR {gr:+.1f} µs/d, razem {sr + gr:+.1f} µs/d → {abs(sr + gr)*1e-6*c/1e3:.1f} km/d")
bb = np.linspace(0, 0.995, 300)
plt.plot(bb, gamma(bb)); plt.xlabel("v / c"); plt.ylabel("γ"); plt.grid(True); plt.show()
```

## Zadania

### A. Poziom maturalny

1. Oblicz $\gamma$ dla $v = 0{,}6c$ i $v = 0{,}8c$.

<details>
<summary>Odpowiedź</summary>

1,25 i 1,67.
</details>

2. Statek kosmiczny o długości własnej 100 m leci z prędkością $0{,}8c$. Jaką długość zmierzy obserwator na Ziemi?

<details>
<summary>Odpowiedź</summary>

60 m.
</details>

3. Astronauta leci do gwiazdy odległej o 4 lata świetlne z prędkością $0{,}8c$ i wraca. Ile czasu minie na Ziemi, a ile według astronauty?

<details>
<summary>Odpowiedź</summary>

Na Ziemi $2\cdot4/0{,}8 = 10$ lat. Dla astronauty $10/1{,}67 = 6$ lat.
</details>

4. Pion o czasie życia 26 ns leci z prędkością $0{,}99c$. Jak daleko średnio doleci?

<details>
<summary>Odpowiedź</summary>

$\gamma \approx 7{,}1$, zasięg $\gamma\tau v \approx 55\ \mathrm m$ (bez dylatacji ok. 7,7 m).
</details>

### B. Poziom akademicki _(opcjonalnie — rozszerzenie z rachunkiem)_

1. Pokaż, że dla $v \ll c$: $\gamma \approx 1 + \dfrac{v^2}{2c^2}$. O ile spóźni się zegar w samolocie lecącym z prędkością 250 m/s przez 10 godzin (tylko efekt prędkości)?

<details>
<summary>Odpowiedź</summary>

$(1 - x)^{-1/2} \approx 1 + x/2$. $\Delta t\cdot v^2/(2c^2) = 36\,000\cdot3{,}5\cdot10^{-13} \approx 12\ \mathrm{ns}$.
</details>

2. Wyprowadź skrócenie Lorentza z dylatacji czasu na przykładzie mionu: w układzie Ziemi atmosfera ma grubość $H$, a mion leci z prędkością $v$. Ile czasu własnego mija dla mionu i jak gruba jest dla niego atmosfera?

<details>
<summary>Odpowiedź</summary>

W układzie Ziemi lot trwa $H/v$, a czas własny mionu $H/(\gamma v)$. W układzie mionu atmosfera przesuwa się z prędkością $v$ przez ten czas, więc ma grubość $v\cdot H/(\gamma v) = H/\gamma$.
</details>

3. Czas własny ciała o zmiennej prędkości to $\tau = \displaystyle\int\sqrt{1 - v^2(t)/c^2}\,dt$. Rakieta przyspiesza ze stałym przyspieszeniem własnym $a$, więc w układzie Ziemi $v(t) = \dfrac{at}{\sqrt{1 + (at/c)^2}}$. Pokaż, że $\tau = \dfrac ca\operatorname{arsinh}\dfrac{at}{c}$, i oblicz $\tau$ oraz $v$ dla $a = g$ po 10 latach ziemskich.

<details>
<summary>Odpowiedź</summary>

$1 - v^2/c^2 = \dfrac{1}{1 + (at/c)^2}$, a $\displaystyle\int\frac{dt}{\sqrt{1 + (at/c)^2}} = \frac ca\operatorname{arsinh}\frac{at}{c}$. Dla $a = g$, $t = 10$ lat: $at/c \approx 10{,}3$, $\tau \approx 2{,}9$ roku, $v \approx 0{,}995c$.
</details>

## Źródła

- OpenStax, *Fizyka dla szkół wyższych*, t. 3, rozdz. 5 — §5.3 (dylatacja czasu) i §5.4 (skrócenie długości).
- Halliday, Resnick, Walker, *Podstawy fizyki* — wyd. 2015: t. 4, §37.1–37.2; wyd. 1: t. 4, §38.5–38.6.
