# 03.04 — Dynamika ruchu po okręgu

> **Moduł:** [03 — Dynamika punktu materialnego](README.md) · **Poziom:** 🟢 matura R · **Status:** ✅ pełny
>
> **Czytaj:**
>
> - OpenStax, *Fizyka dla szkół wyższych*, t. 1, rozdz. 6: [§6.3](https://openstax.org/books/fizyka-dla-szk%C3%B3%C5%82-wy%C5%BCszych-tom-1/pages/6-3-sila-dosrodkowa) · [wstęp do rozdziału](https://openstax.org/books/fizyka-dla-szk%C3%B3%C5%82-wy%C5%BCszych-tom-1/pages/6-wstep)
> - Halliday, Resnick, Walker, *Podstawy fizyki*, wyd. 2015, t. 1: §6.3 (s. 167)
> - Halliday, Resnick, Walker, *Podstawy fizyki*, wyd. 1 (2003), t. 1: [§6.4, s. 127](https://home.agh.edu.pl/~czapli/Resnick_1.pdf#page=139) — PDF z serwera AGH

← [Tarcie statyczne i kinetyczne](03-tarcie.md) · [spis modułu](README.md) · [Opór ośrodka i prędkość graniczna — równanie ruchu](05-opor-osrodka.md) →

## Po co to jest

Każde ciało poruszające się po okręgu ma przyspieszenie dośrodkowe $v^2/R$ (02.06), więc coś musi wytwarzać siłę skierowaną do środka. Ten temat odpowiada na pytanie, **co** to jest w konkretnej sytuacji: tarcie opon na zakręcie, naciąg linki, grawitacja Słońca, siła Lorentza. Tak liczy się bezpieczną prędkość na zakręcie, wyprofilowanie toru, pętlę kolejki górskiej i orbitę satelity (07).

## Teoria w pigułce

**Siła dośrodkowa nie jest nowym rodzajem siły.** To nazwa wypadkowej składowej sił rzeczywistych, skierowanej do środka okręgu:

$$\sum F_{\text{do środka}} = \frac{mv^2}{R} = m\omega^2R.$$

Na diagramie sił rysujemy tylko siły rzeczywiste (ciężar, nacisk, naciąg, tarcie); ich wypadkowa w kierunku środka musi równać się $mv^2/R$.

**Typowe sytuacje.**

| Sytuacja | Co daje siłę dośrodkową | Wynik |
|---|---|---|
| samochód na płaskim zakręcie | tarcie statyczne opon | $v_{\max} = \sqrt{\mu_sgR}$ |
| zakręt wyprofilowany (kąt $\theta$), bez tarcia | składowa pozioma siły nacisku | $\tan\theta = \dfrac{v^2}{gR}$ |
| wahadło stożkowe | składowa pozioma naciągu | $\tan\theta = \dfrac{v^2}{gR}$ |
| kamień na lince w pionie, górny punkt | ciężar + naciąg | $v_{\min} = \sqrt{gR}$ (gdy $T = 0$) |
| samochód na szczycie wzniesienia | ciężar − nacisk | odrywa się dla $v > \sqrt{gR}$ |
| satelita | grawitacja | moduł 07 |

**Wypukłość i wklęsłość.** Na szczycie wzniesienia nacisk maleje ($N = mg - mv^2/R$), w dolinie rośnie ($N = mg + mv^2/R$). Dlatego na „hopce” czujemy się lżej, a w zagłębieniu drogi — ciężej.

## Wzory i założenia

| Wzór | Znaczenie | Kiedy obowiązuje |
|---|---|---|
| $\sum F_r = mv^2/R$ | II zasada w kierunku do środka | ruch po okręgu (także niejednostajny — składowa promieniowa) |
| $v_{\max} = \sqrt{\mu_sgR}$ | płaski zakręt | koła się nie ślizgają |
| $\tan\theta = v^2/(gR)$ | idealne wyprofilowanie | bez tarcia |
| $v_{\min} = \sqrt{gR}$ | górny punkt pętli / okręgu na lince | ciało nie odpada / linka napięta |
| $T = 2\pi\sqrt{\dfrac{L\cos\theta}{g}}$ | okres wahadła stożkowego | długość linki $L$, kąt od pionu $\theta$ |

## Przykład rozwiązany

**Zadanie 1.** Z jaką największą prędkością samochód może pokonać płaski zakręt o promieniu 50 m, jeśli $\mu_s = 0{,}8$?

Siła dośrodkowa to tarcie statyczne: $\dfrac{mv^2}{R} \le \mu_smg \Rightarrow v_{\max} = \sqrt{0{,}8\cdot9{,}81\cdot50} \approx 19{,}8\ \mathrm{m/s} \approx 71\ \mathrm{km/h}$.

Wynik nie zależy od masy — ciężarówka i rower mają (przy tym samym $\mu$) tę samą prędkość graniczną. Na mokrej jezdni ($\mu = 0{,}4$) prędkość spada do ok. 50 km/h.

**Zadanie 2.** Pod jakim kątem należy wyprofilować zakręt o promieniu 200 m, żeby przy prędkości 90 km/h samochód nie potrzebował tarcia?

Na samochód działają ciężar i nacisk prostopadły do nachylonej jezdni. Pionowo: $N\cos\theta = mg$; poziomo (do środka): $N\sin\theta = mv^2/R$. Dzieląc:

$$\tan\theta = \frac{v^2}{gR} = \frac{25^2}{9{,}81\cdot200} \approx 0{,}319 \Rightarrow \theta \approx 17{,}7^\circ.$$

## Typowe pułapki

- **Rysowanie siły dośrodkowej obok innych sił.** To dubluje siłę. Siła dośrodkowa to *wypadkowa* sił rzeczywistych.
- **Siła odśrodkowa w układzie inercjalnym.** Nie istnieje; pojawia się tylko w układzie obracającym się (03.06).
- **Naciąg w górnym i dolnym punkcie okręgu pionowego jest taki sam.** W dolnym punkcie naciąg musi zrównoważyć ciężar i jeszcze dać siłę dośrodkową: $T_d = mg + mv^2/R$; w górnym $T_g = mv^2/R - mg$.
- **Kąt wahadła stożkowego mierzony od poziomu.** Sprawdź, od czego mierzy kąt treść zadania.

## Doświadczenie / symulacja

**Wahadło stożkowe.** Zakręć ciężarek na nitce długości 0,5–1 m tak, żeby zataczał poziomy okrąg. Zmierz czas 10 obiegów i promień okręgu (np. nad kartką z narysowanymi okręgami). Oblicz kąt $\theta$ z $\sin\theta = R/L$ i porównaj zmierzony okres ze wzorem $2\pi\sqrt{L\cos\theta/g}$.

**Python:** naciąg linki z kamieniem krążącym w pionie, w funkcji położenia (z zasadą zachowania energii z modułu 04).

```python
import numpy as np
import matplotlib.pyplot as plt

m, R, g = 0.2, 0.8, 9.81
v_bottom = 6.0                                   # prędkość w najniższym punkcie [m/s]
phi = np.linspace(0, 2*np.pi, 361)               # kąt od najniższego punktu
h = R * (1 - np.cos(phi))                        # wysokość nad najniższym punktem
v2 = v_bottom**2 - 2*g*h                         # zasada zachowania energii
T = m*v2/R + m*g*np.cos(phi)                     # składowa promieniowa II zasady

print(f"dół: T = {T[0]:.2f} N, góra: T = {T[180]:.2f} N")
print(f"minimalna prędkość na dole, żeby linka była napięta w górze: {np.sqrt(5*g*R):.2f} m/s")
plt.plot(np.degrees(phi), T); plt.axhline(0, color="gray")
plt.xlabel("kąt od najniższego punktu [°]"); plt.ylabel("naciąg [N]"); plt.grid(True); plt.show()
```

## Zadania

### A. Poziom maturalny

1. Kamień o masie 0,2 kg krąży na lince długości 0,8 m w płaszczyźnie pionowej. a) Jaka jest najmniejsza prędkość w górnym punkcie, przy której linka jest napięta? b) Jaki jest naciąg w dolnym punkcie, gdy prędkość wynosi tam 6 m/s?

<details>
<summary>Odpowiedź</summary>

a) $\sqrt{gR} \approx 2{,}8\ \mathrm{m/s}$; b) $T = mg + mv^2/R \approx 11{,}0\ \mathrm{N}$.
</details>

2. Pętla kolejki górskiej ma w górnym punkcie promień 10 m. Jaka musi być tam najmniejsza prędkość wagonika?

<details>
<summary>Odpowiedź</summary>

$\sqrt{gR} \approx 9{,}9\ \mathrm{m/s}$.
</details>

3. Samochód przejeżdża przez szczyt wzniesienia o promieniu krzywizny 40 m. Przy jakiej prędkości koła oderwą się od drogi?

<details>
<summary>Odpowiedź</summary>

$v = \sqrt{gR} \approx 19{,}8\ \mathrm{m/s} \approx 71\ \mathrm{km/h}$.
</details>

4. Bęben pralki o promieniu 25 cm wiruje z prędkością 1200 obr/min. Ile razy siła, z jaką bęben działa na mokrą tkaninę, przewyższa jej ciężar?

<details>
<summary>Odpowiedź</summary>

$a = \omega^2R \approx 3950\ \mathrm{m/s^2} \approx 400g$.
</details>

5. Samochód o masie 1000 kg pokonuje płaski zakręt o promieniu 80 m z prędkością 54 km/h. Jaka siła tarcia na niego działa? Jaki najmniejszy współczynnik tarcia jest potrzebny?

<details>
<summary>Odpowiedź</summary>

$F = 1000\cdot15^2/80 \approx 2810\ \mathrm{N}$; $\mu \ge 225/(9{,}81\cdot80) \approx 0{,}29$.
</details>

### B. Poziom akademicki _(opcjonalnie — rozszerzenie z rachunkiem)_

1. Wahadło stożkowe ma linkę długości 1 m nachyloną pod kątem $30^\circ$ do pionu. Oblicz okres obiegu.

<details>
<summary>Odpowiedź</summary>

$T = 2\pi\sqrt{L\cos\theta/g} \approx 1{,}87\ \mathrm{s}$.
</details>

2. Zakręt o promieniu 100 m jest wyprofilowany pod kątem $15^\circ$, $\mu_s = 0{,}5$. Oblicz prędkość idealną (bez tarcia) i największą prędkość bezpieczną.

<details>
<summary>Odpowiedź</summary>

$v_{\text{id}} = \sqrt{gR\tan\theta} \approx 16{,}2\ \mathrm{m/s}$; $v_{\max} = \sqrt{gR\dfrac{\sin\theta + \mu\cos\theta}{\cos\theta - \mu\sin\theta}} \approx 29{,}5\ \mathrm{m/s}$ (ok. 106 km/h).
</details>

3. Pokaż, korzystając z zasady zachowania energii, że kamień na lince wykona pełny obrót w pionie, gdy prędkość w dolnym punkcie wynosi co najmniej $\sqrt{5gR}$, oraz że różnica naciągów w dolnym i górnym punkcie wynosi zawsze $6mg$.

<details>
<summary>Odpowiedź</summary>

$v_g^2 = v_d^2 - 4gR \ge gR \Rightarrow v_d^2 \ge 5gR$. $T_d - T_g = \left(mg + \dfrac{mv_d^2}{R}\right) - \left(\dfrac{mv_g^2}{R} - mg\right) = 2mg + \dfrac{m\cdot4gR}{R} = 6mg$.
</details>

## Źródła

- OpenStax, *Fizyka dla szkół wyższych*, t. 1, rozdz. 6 — §6.3: siła dośrodkowa, zakręty płaskie i wyprofilowane.
- Halliday, Resnick, Walker, *Podstawy fizyki* — wyd. 2015: t. 1, §6.3; wyd. 1: t. 1, §6.4.
