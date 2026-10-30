# 21.01 — Model Bohra i widmo atomu wodoru

> **Moduł:** [21 — Fizyka atomowa](README.md) · **Poziom:** 🟢 matura R · **Status:** ✅ pełny
>
> **Czytaj:**
>
> - OpenStax, *Fizyka dla szkół wyższych*, t. 3, rozdz. 6: [§6.4](https://openstax.org/books/fizyka-dla-szk%C3%B3%C5%82-wy%C5%BCszych-tom-3/pages/6-4-model-atomu-wodoru-bohra) · [wstęp do rozdziału](https://openstax.org/books/fizyka-dla-szk%C3%B3%C5%82-wy%C5%BCszych-tom-3/pages/6-wstep)
> - Halliday, Resnick, Walker, *Podstawy fizyki*, wyd. 2015, t. 5: §39.5 (s. 65)
> - Halliday, Resnick, Walker, *Podstawy fizyki*, wyd. 1 (2003), t. 5: [§40.8, s. 50](https://home.agh.edu.pl/~czapli/Resnick_5.pdf#page=66) — PDF z serwera AGH

← (początek modułu) · [spis modułu](README.md) · [Atom wodoru w mechanice kwantowej, liczby kwantowe](02-atom-wodoru-kwantowo.md) →

## Po co to jest

Rozżarzony wodór nie świeci wszystkimi barwami, tylko kilkoma ostrymi liniami. Ich długości fal spełniają prosty wzór, znaleziony przez Balmera w 1885 r. bez żadnego uzasadnienia. Bohr w 1913 r. wyjaśnił go, przyjmując, że elektron może krążyć tylko po wybranych orbitach. Model jest dziś przestarzały (21.02), ale daje poprawne energie wodoru i stanowi najprostszą drogę do zrozumienia, skąd biorą się widma liniowe, na których opiera się spektroskopia w chemii i astronomii. To stały temat matury rozszerzonej.

## Teoria w pigułce

**Problem klasyczny.** Elektron krążący wokół jądra ma przyspieszenie dośrodkowe, więc według elektrodynamiki (16.02) powinien promieniować, tracić energię i w ułamku nanosekundy spaść na jądro. Atomy są jednak stabilne.

**Postulaty Bohra:**
1. Elektron krąży tylko po orbitach, na których moment pędu jest wielokrotnością $\hbar$: $L = mvr = n\hbar$, $n = 1, 2, 3, \dots$ Na tych orbitach nie promieniuje.
2. Atom emituje lub pochłania foton tylko przy przejściu między orbitami: $hf = E_n - E_m$.

Warunek kwantyzacji to warunek fali stojącej de Broglie'a (20.04) na obwodzie orbity: $2\pi r = n\lambda$.

**Wyniki dla wodoru.** Siła Coulomba pełni rolę siły dośrodkowej: $\dfrac{ke^2}{r^2} = \dfrac{mv^2}{r}$. Razem z warunkiem kwantyzacji:

$$r_n = n^2a_0, \qquad a_0 = \frac{\hbar^2}{mke^2} \approx 0{,}0529\ \mathrm{nm},$$

$$E_n = -\frac{13{,}6\ \mathrm{eV}}{n^2}.$$

Ujemna energia oznacza stan związany. $E_1 = -13{,}6\ \mathrm{eV}$ to stan podstawowy, a 13,6 eV to energia jonizacji. Dla jonów z jednym elektronem (He⁺, Li²⁺) energie są $Z^2$ razy większe.

**Widmo wodoru.** Foton emitowany przy przejściu $n_2 \to n_1$:

$$\frac1\lambda = R\left(\frac1{n_1^2} - \frac1{n_2^2}\right), \qquad R \approx 1{,}097\cdot10^7\ \mathrm{m^{-1}}.$$

- **Seria Lymana** ($n_1 = 1$): nadfiolet, od 121,6 nm do 91,2 nm.
- **Seria Balmera** ($n_1 = 2$): widzialna. $\mathrm H\alpha$ (3→2) ok. 656 nm czerwona, $\mathrm H\beta$ 486 nm, $\mathrm H\gamma$ 434 nm, $\mathrm H\delta$ 410 nm, granica 365 nm.
- **Seria Paschena** ($n_1 = 3$): podczerwień.

Widmo **emisyjne** to jasne linie gorącego gazu, a **absorpcyjne** to ciemne linie w widmie ciągłym, gdy światło przechodzi przez chłodniejszy gaz (linie Fraunhofera w widmie Słońca).

**Ograniczenia modelu Bohra.** Model nie wyjaśnia natężeń linii, struktury subtelnej, atomów wieloelektronowych ani tego, dlaczego stan podstawowy wodoru ma zerowy moment pędu. Elektron nie porusza się po torze, tylko jest opisany funkcją falową (21.02).

## Wzory i założenia

| Wzór | Znaczenie | Kiedy obowiązuje |
|---|---|---|
| $mvr = n\hbar$ | kwantyzacja momentu pędu | model Bohra |
| $r_n = n^2a_0$, $a_0 = 0{,}0529\ \mathrm{nm}$ | promienie orbit | wodór |
| $E_n = -13{,}6\ \mathrm{eV}\cdot Z^2/n^2$ | poziomy energii | atom z jednym elektronem |
| $hf = E_{n_2} - E_{n_1}$ | foton przy przejściu | — |
| $1/\lambda = R(1/n_1^2 - 1/n_2^2)$ | wzór Rydberga | wodór |

## Przykład rozwiązany

**Zadanie 1.** Oblicz długość fali linii $\mathrm H\alpha$ (przejście 3→2) i najkrótszą długość fali w serii Balmera.

$E_3 - E_2 = 13{,}6(1/4 - 1/9) \approx 1{,}89\ \mathrm{eV}$, $\lambda = 1240/1{,}89 \approx 656\ \mathrm{nm}$.

Granica serii ($n_2 \to \infty$): $E = 13{,}6/4 = 3{,}4\ \mathrm{eV}$, $\lambda \approx 365\ \mathrm{nm}$.

**Zadanie 2.** Ile linii może wyemitować wodór wzbudzony do poziomu $n = 4$?

Przejścia między dowolnymi dwoma z czterech poziomów: $\binom42 = 6$ linii (4→3, 4→2, 4→1, 3→2, 3→1, 2→1).

## Typowe pułapki

- **Energia poziomu dodatnia.** Energie stanów związanych są ujemne, a zero odpowiada elektronowi swobodnemu w spoczynku.
- **Foton ma energię poziomu.** Ma energię równą **różnicy** poziomów.
- **Wodór pochłania wszystkie fotony powyżej 10,2 eV.** Poniżej jonizacji pochłania tylko fotony o energiach dokładnie równych różnicom poziomów.
- **Elektron krąży po orbicie.** To obraz z modelu Bohra. W mechanice kwantowej elektron ma tylko rozkład prawdopodobieństwa.
- **$Z^2$ we wzorze dla atomów wieloelektronowych.** Wzór działa tylko dla jonów z jednym elektronem.

## Doświadczenie / symulacja

**Widmo lampy wodorowej lub świetlówki.** Przez spektroskop z płyty CD (18.03) obejrzyj lampę wyładowczą z wodorem (pracownia) albo świetlówkę (linie rtęci: 436, 546, 577/579 nm). Z położeń znanych linii wyskaluj spektroskop i zmierz linie wodoru. Sprawdź wzór Rydberga.

**Symulacja PhET:** *Modele atomu wodoru* (*Models of the Hydrogen Atom*) — od modelu Thomsona do Schrödingera, ze strzelaniem fotonami ([phet.colorado.edu/pl](https://phet.colorado.edu/pl/)).

**Python:** poziomy energii wodoru i linie serii widmowych.

```python
import numpy as np
import matplotlib.pyplot as plt

R, hc = 1.0973731e7, 1239.84                     # m⁻¹, eV·nm
E = lambda n: -13.606/n**2
for nazwa, n1 in [("Lyman", 1), ("Balmer", 2), ("Paschen", 3)]:
    linie = [1e9/(R*(1/n1**2 - 1/n2**2)) for n2 in range(n1 + 1, n1 + 5)]
    print(f"{nazwa:8s}: " + ", ".join(f"{l:.1f}" for l in linie) + f" … granica {1e9/(R/n1**2):.1f} nm")
print(f"Hα z poziomów: {hc/(E(3) - E(2)):.1f} nm; jonizacja He⁺: {13.606*4:.1f} eV")
fig, ax = plt.subplots(figsize=(4, 5))
for n in range(1, 7):
    ax.hlines(E(n), 0, 1); ax.text(1.02, E(n), f"n = {n}", va="center")
for n2 in range(3, 7):
    ax.annotate("", xy=(0.2 + 0.12*n2, E(2)), xytext=(0.2 + 0.12*n2, E(n2)), arrowprops=dict(arrowstyle="->", color="r"))
ax.set_ylabel("E [eV]"); ax.set_xticks([]); ax.set_title("seria Balmera"); plt.show()
```

## Zadania

### A. Poziom maturalny

1. Oblicz energię fotonu i długość fali linii Lymana α (2→1).

<details>
<summary>Odpowiedź</summary>

$10{,}2\ \mathrm{eV}$, $\approx 122\ \mathrm{nm}$ (nadfiolet).
</details>

2. Atom wodoru w stanie podstawowym pochłania foton o energii 12,75 eV. Na który poziom przechodzi elektron?

<details>
<summary>Odpowiedź</summary>

$13{,}6(1 - 1/n^2) = 12{,}75 \Rightarrow n = 4$.
</details>

3. Oblicz promień orbity $n = 3$ w atomie wodoru i energię potrzebną do jonizacji z tego poziomu.

<details>
<summary>Odpowiedź</summary>

$r_3 = 9a_0 \approx 0{,}48\ \mathrm{nm}$, energia jonizacji $13{,}6/9 \approx 1{,}51\ \mathrm{eV}$.
</details>

4. Dlaczego widmo gazu jest liniowe, a widmo żarówki ciągłe?

<details>
<summary>Odpowiedź</summary>

W rozrzedzonym gazie atomy są niezależne i emitują fotony o energiach równych różnicom ich poziomów. W ciele stałym atomy silnie oddziałują, poziomy tworzą pasma (23.04), a promieniowanie jest termiczne (20.01).
</details>

### B. Poziom akademicki _(opcjonalnie — rozszerzenie z rachunkiem)_

1. Wyprowadź $r_n$ i $E_n$ z warunku $mvr = n\hbar$ i równowagi sił. Oblicz prędkość elektronu na pierwszej orbicie w jednostkach $c$.

<details>
<summary>Odpowiedź</summary>

$mv^2 = ke^2/r$ i $v = n\hbar/(mr)$ dają $r = n^2\hbar^2/(mke^2)$. $E = \tfrac12mv^2 - ke^2/r = -\dfrac{ke^2}{2r} = -\dfrac{mk^2e^4}{2\hbar^2n^2}$. $v_1 = ke^2/\hbar \approx 2{,}19\cdot10^6\ \mathrm{m/s} \approx c/137$ (stała struktury subtelnej).
</details>

2. Uwzględnij skończoną masę jądra: w obliczeniach zastąp $m_e$ masą zredukowaną $\mu = m_em_p/(m_e + m_p)$. O ile zmienia się długość fali $\mathrm H\alpha$? Jak różnią się linie wodoru i deuteru (odkrycie deuteru, Urey 1932)?

<details>
<summary>Odpowiedź</summary>

$E \propto \mu$, więc $\lambda$ rośnie o czynnik $1 + m_e/m_p$, czyli o ok. 0,054% (0,36 nm). Dla deuteru $m_e/m_D$ jest dwa razy mniejsze, więc linia D jest krótsza o ok. 0,18 nm. Tę różnicę zaobserwował Urey.
</details>

## Źródła

- OpenStax, *Fizyka dla szkół wyższych*, t. 3, rozdz. 6 — §6.4: model atomu wodoru Bohra.
- Halliday, Resnick, Walker, *Podstawy fizyki* — wyd. 2015: t. 5, §39.5; wyd. 1: t. 5, §40.8.
- Symulacja PhET *Modele atomu wodoru*.
