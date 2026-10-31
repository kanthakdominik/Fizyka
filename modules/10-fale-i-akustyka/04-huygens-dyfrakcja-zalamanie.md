# 10.04 — Zasada Huygensa: odbicie, załamanie i dyfrakcja fal

> **Moduł:** [10 — Fale mechaniczne i akustyka](README.md) · **Poziom:** 🟢 matura R · **Status:** ✅ pełny
>
> **Czytaj:**
>
> - OpenStax, *Fizyka dla szkół wyższych*, t. 3, rozdz. 1: [§1.6](https://openstax.org/books/fizyka-dla-szk%C3%B3%C5%82-wy%C5%BCszych-tom-3/pages/1-6-zasada-huygensa) · [wstęp do rozdziału](https://openstax.org/books/fizyka-dla-szk%C3%B3%C5%82-wy%C5%BCszych-tom-3/pages/1-wstep)
> - Halliday, Resnick, Walker, *Podstawy fizyki*, wyd. 2015, t. 4: §35.1 (s. 97)
> - Halliday, Resnick, Walker, *Podstawy fizyki*, wyd. 1 (2003), t. 4: [§36.2, s. 75](https://home.agh.edu.pl/~czapli/Resnick_4.pdf#page=90) — PDF z serwera AGH

← [Superpozycja, interferencja i fale stojące](03-interferencja-i-fale-stojace.md) · [spis modułu](README.md) · [Dźwięk: prędkość, natężenie, poziom w decybelach](05-dzwiek-i-natezenie.md) →

## Po co to jest

Fale odbijają się, załamują na granicy ośrodków i uginają na przeszkodach. Dzięki temu słychać kogoś zza rogu, nietoperze i sonary widzą echem, a fale morskie zawsze dobiegają do plaży prawie równolegle do brzegu. Zasada Huygensa wyjaśnia te zjawiska jednym obrazkiem i przenosi się bez zmian na światło (17, 18).

## Teoria w pigułce

**Czoło fali** (powierzchnia falowa) to zbiór punktów o tej samej fazie, na przykład grzbiet fali na wodzie. **Promień** to kierunek rozchodzenia się fali, prostopadły do czoła.

**Zasada Huygensa.** Każdy punkt czoła fali jest źródłem fali kulistej (cząstkowej). Nowe czoło fali po czasie $\Delta t$ to obwiednia tych fal cząstkowych o promieniu $v\,\Delta t$.

**Odbicie.** Kąt odbicia jest równy kątowi padania, a oba mierzy się od normalnej do powierzchni. Echo wraca po czasie $t = 2d/v$, na czym działają **echolokacja** (nietoperze, delfiny), sonar i USG.

**Załamanie.** Gdy fala przechodzi do ośrodka o innej prędkości, część czoła, która weszła pierwsza, porusza się szybciej lub wolniej i czoło się obraca. Z zasady Huygensa wynika **prawo załamania** (prawo Snelliusa dla fal):

$$\frac{\sin\theta_1}{\sin\theta_2} = \frac{v_1}{v_2}.$$

Częstotliwość się nie zmienia, a długość fali zmienia się proporcjonalnie do $v$. Fala przechodząca do ośrodka wolniejszego załamuje się **do normalnej**. Fale morskie zwalniają na płyciźnie, bo $v \approx \sqrt{gh}$ dla wody płytkiej w porównaniu z długością fali, i dlatego skręcają w stronę brzegu.

**Całkowite wewnętrzne odbicie.** Przy przejściu do ośrodka szybszego istnieje kąt graniczny $\sin\theta_{\text{gr}} = v_1/v_2$. Dla większych kątów fala w ogóle nie przechodzi. Dźwięk z powietrza do wody przechodzi tylko przy kątach mniejszych niż ok. $13^\circ$, a i wtedy większość energii się odbija.

**Dyfrakcja** (ugięcie) to rozchodzenie się fali za szczeliną lub przeszkodą także w obszar „cienia”. Jest silna, gdy rozmiar szczeliny lub przeszkody jest porównywalny z długością fali lub mniejszy, a słaba, gdy jest dużo większy. Dźwięk ($\lambda \sim 1\ \mathrm{m}$) ugina się na drzwiach, a światło ($\lambda \sim 0{,}5\ \mu\mathrm m$) nie, dlatego słyszymy zza rogu, ale nie widzimy. Ilościowo dyfrakcję opisuje 18.

## Wzory i założenia

| Wzór | Znaczenie | Kiedy obowiązuje |
|---|---|---|
| $\theta_{\text{odb}} = \theta_{\text{pad}}$ | prawo odbicia | gładka powierzchnia (nierówności $\ll\lambda$) |
| $\sin\theta_1/\sin\theta_2 = v_1/v_2$ | prawo załamania | — |
| $\sin\theta_{\text{gr}} = v_1/v_2$ | kąt graniczny | $v_2 > v_1$ |
| $t = 2d/v$ | czas powrotu echa | — |
| $v \approx \sqrt{gh}$ | fale na płytkiej wodzie | $h \ll \lambda$ |
| silna dyfrakcja, gdy $a \lesssim \lambda$ | ugięcie na szczelinie $a$ | — |

## Przykład rozwiązany

**Zadanie 1.** Fala o częstotliwości 2 Hz przechodzi z obszaru o głębokości 1 m do obszaru o głębokości 0,25 m. Kąt padania wynosi $30^\circ$. Oblicz prędkości, długości fal i kąt załamania (użyj $v = \sqrt{gh}$).

$v_1 = \sqrt{9{,}81\cdot1} \approx 3{,}13\ \mathrm{m/s}$, $v_2 \approx 1{,}57\ \mathrm{m/s}$.

$\lambda_1 = v_1/f \approx 1{,}57\ \mathrm{m}$, $\lambda_2 \approx 0{,}78\ \mathrm{m}$.

$\sin\theta_2 = \sin30^\circ\cdot\dfrac{1{,}57}{3{,}13} = 0{,}25 \Rightarrow \theta_2 \approx 14{,}5^\circ$. Fala skręca w stronę normalnej, czyli prostopadle do linii głębokości.

**Zadanie 2.** Pod jakim największym kątem padania dźwięk z powietrza ($343\ \mathrm{m/s}$) może wejść do wody ($1480\ \mathrm{m/s}$)?

$\sin\theta_{\text{gr}} = 343/1480 \approx 0{,}23$, więc $\theta_{\text{gr}} \approx 13{,}4^\circ$.

## Typowe pułapki

- **Kąty od powierzchni.** Kąty padania, odbicia i załamania mierzy się od **normalnej**.
- **Przy załamaniu zmienia się częstotliwość.** Zmieniają się prędkość i długość fali.
- **Całkowite odbicie przy przejściu do ośrodka wolniejszego.** Zachodzi tylko przy przejściu do ośrodka, w którym fala jest **szybsza**. Dla dźwięku woda jest „szybsza” niż powietrze, odwrotnie niż dla światła.
- **Dyfrakcja tylko na małych szczelinach.** Liczy się stosunek rozmiaru do długości fali, a nie sam rozmiar.
- **Echo — droga w jedną stronę.** Czas echa obejmuje drogę tam i z powrotem.

## Doświadczenie / symulacja

**Echo i odległość.** Stań 30–50 m od dużej ściany i klaśnij. W phyphox (*Audio Scope* lub *Acoustic Stopwatch*) zmierz czas między klaśnięciem a echem i oblicz odległość. Sprawdź wynik krokami lub mapą.

**Kuweta falowa w wannie lub brytfance.** Podnieś jedną stronę płaskiej blachy z wodą, żeby uzyskać płytszą strefę. Puszczaj fale linijką i obserwuj zmianę długości fali i kierunku przy przejściu na płyciznę. Ustaw dwie przeszkody ze szczeliną i porównaj ugięcie dla szczeliny wąskiej i szerokiej.

**Symulacja PhET:** *Interferencja fal* (*Wave Interference*), zakładka *Szczeliny* (*Slits*) — [phet.colorado.edu/pl](https://phet.colorado.edu/pl/).

**Python:** konstrukcja Huygensa przy załamaniu — czoło fali jako obwiednia fal cząstkowych.

```python
import numpy as np
import matplotlib.pyplot as plt

v1, v2 = np.sqrt(9.81*1.0), np.sqrt(9.81*0.25)   # głęboko (y > 0) i płytko (y < 0)
th1 = np.radians(30)
th2 = np.arcsin(np.sin(th1)*v2/v1)
print(f"kąt załamania = {np.degrees(th2):.1f}°")

# punkty granicy x_i, do których czoło padające dociera w chwilach t_i
xs = np.linspace(0, 4, 9)
t_hit = xs*np.sin(th1)/v1
T = t_hit[-1]
fig, ax = plt.subplots(figsize=(6, 5))
phi = np.linspace(np.pi, 2*np.pi, 100)
for x0, t0 in zip(xs, t_hit):
    r = v2*(T - t0)                                  # promień fali cząstkowej w ośrodku 2
    ax.plot(x0 + r*np.cos(phi), r*np.sin(phi), "c", lw=0.7)
# obwiednia: styczna z punktu (4, 0) do największej fali cząstkowej (środek w x = 0)
R = v2*T
P = R*np.array([np.sin(th2), -np.cos(th2)])         # punkt styczności: kierunek promienia pod kątem θ2
print(f"styczność: OP·(P − (4,0)) = {P @ (P - np.array([4, 0])):.1e}")
ax.plot([4, P[0]], [0, P[1]], "r", lw=2, label="nowe czoło fali")
ax.plot([0, 4*np.cos(th1)**2], [0, 4*np.sin(th1)*np.cos(th1)], "b", lw=2, label="czoło padające (t = 0)")
ax.axhline(0, color="k"); ax.set_aspect("equal"); ax.legend(); ax.set_title("konstrukcja Huygensa")
plt.show()
```

## Zadania

### A. Poziom maturalny

1. Echo od ściany lasu wraca po 1,5 s. Jak daleko jest las ($v = 343\ \mathrm{m/s}$)?

<details>
<summary>Odpowiedź</summary>

$d = vt/2 \approx 257\ \mathrm{m}$.
</details>

2. Nietoperz wysyła ultradźwięki o częstotliwości 50 kHz. Oblicz długość fali. Dlaczego nietoperze używają tak wysokich częstotliwości?

<details>
<summary>Odpowiedź</summary>

$\lambda \approx 6{,}9\ \mathrm{mm}$. Fala odbija się wyraźnie od obiektów większych od długości fali, a krótka fala pozwala wykryć małe owady. Przy dużo dłuższej fali dźwięk ugiąłby się wokół owada i nie dał echa.
</details>

3. Dlaczego słyszymy rozmowę za otwartymi drzwiami, choć nie widzimy rozmówców?

<details>
<summary>Odpowiedź</summary>

Długość fali dźwięku (dziesiątki centymetrów do metrów) jest porównywalna z szerokością drzwi, więc dźwięk silnie się ugina. Długość fali światła jest milion razy mniejsza.
</details>

4. Sonar statku odbiera echo od dna po 0,4 s. Oblicz głębokość ($v = 1480\ \mathrm{m/s}$).

<details>
<summary>Odpowiedź</summary>

$h \approx 296\ \mathrm{m}$.
</details>

### B. Poziom akademicki _(opcjonalnie — rozszerzenie z rachunkiem)_

1. Wyprowadź prawo załamania z zasady Fermata: fala biegnie z punktu $(0, a)$ do $(d, -b)$ drogą o najkrótszym czasie, a granica ośrodków to oś $x$.

<details>
<summary>Odpowiedź</summary>

$t(x) = \dfrac{\sqrt{a^2 + x^2}}{v_1} + \dfrac{\sqrt{b^2 + (d - x)^2}}{v_2}$. Warunek $t'(x) = 0$ daje $\dfrac{x}{v_1\sqrt{a^2 + x^2}} = \dfrac{d - x}{v_2\sqrt{b^2 + (d - x)^2}}$, czyli $\dfrac{\sin\theta_1}{v_1} = \dfrac{\sin\theta_2}{v_2}$.
</details>

2. Dźwięk pada z powietrza na wodę pod kątem $10^\circ$. Pod jakim kątem biegnie w wodzie?

<details>
<summary>Odpowiedź</summary>

$\sin\theta_2 = \sin10^\circ\cdot1480/343 \approx 0{,}75$, więc $\theta_2 \approx 49^\circ$.
</details>

3. W ciepły wieczór nad chłodnym jeziorem dźwięk niesie się wyjątkowo daleko. Temperatura powietrza rośnie z wysokością (inwersja). Wyjaśnij to za pomocą zasady Huygensa.

<details>
<summary>Odpowiedź</summary>

Wyżej powietrze jest cieplejsze, więc dźwięk biegnie tam szybciej. Górna część czoła fali wyprzedza dolną, czoło obraca się, a promienie zakrzywiają się w dół, z powrotem ku powierzchni wody, zamiast uciekać w górę.
</details>

### C. Zadania z arkuszy maturalnych CKE

Zadania z egzaminów maturalnych (poziom rozszerzony, formuła 2023), w których ten temat jest potrzebny. Rozwiąż je samodzielnie, a potem porównaj z zasadami oceniania. Pełne zestawienie: [matura/README.md](../../matura/README.md).

- Maj 2025, zad. 3.1 — odbicie i załamanie fali na granicy ośrodków ([arkusz](https://www.oke.poznan.pl/files/cms/875/mfap_r0_100_a_2505_arkusz.pdf), [zasady oceniania](https://cke.gov.pl/egzamin-maturalny/egzamin-maturalny-w-formule-2023/arkusze/2025-2/))
- Maj 2025, zad. 3.2 — prawo załamania, kąt graniczny (temat pomocniczy) ([arkusz](https://www.oke.poznan.pl/files/cms/875/mfap_r0_100_a_2505_arkusz.pdf), [zasady oceniania](https://cke.gov.pl/egzamin-maturalny/egzamin-maturalny-w-formule-2023/arkusze/2025-2/))
- Maj 2026, zad. 4.3 — powierzchnie falowe za wąską szczeliną (dyfrakcja) ([arkusz](https://oke.wroc.pl/egzamin-maturalny/egzamin-maturalny-2026-arkusze/), [zasady oceniania](https://cke.gov.pl/egzamin-maturalny/egzamin-maturalny-w-formule-2023/arkusze/))
- Maj 2026, zad. 4.4 — kierunek i długość fali po przejściu do innego ośrodka ([arkusz](https://oke.wroc.pl/egzamin-maturalny/egzamin-maturalny-2026-arkusze/), [zasady oceniania](https://cke.gov.pl/egzamin-maturalny/egzamin-maturalny-w-formule-2023/arkusze/))

## Źródła

- OpenStax, *Fizyka dla szkół wyższych*, t. 3, rozdz. 1 — §1.6: zasada Huygensa (dla światła, ta sama konstrukcja co dla fal mechanicznych).
- Halliday, Resnick, Walker, *Podstawy fizyki* — wyd. 2015: t. 4, §35.1; wyd. 1: t. 4, §36.2.
- Symulacja PhET *Interferencja fal*.
