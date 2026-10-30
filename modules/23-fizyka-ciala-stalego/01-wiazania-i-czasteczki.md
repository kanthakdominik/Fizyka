# 23.01 — Wiązania chemiczne i widma cząsteczkowe

> **Moduł:** [23 — Fizyka ciała stałego](README.md) · **Poziom:** 🔵 studia · **Status:** ✅ pełny
>
> **Czytaj:**
>
> - OpenStax, *Fizyka dla szkół wyższych*, t. 3, rozdz. 9: [§9.1–9.2](https://openstax.org/books/fizyka-dla-szk%C3%B3%C5%82-wy%C5%BCszych-tom-3/pages/9-1-rodzaje-wiazan-czasteczkowych) · [wstęp do rozdziału](https://openstax.org/books/fizyka-dla-szk%C3%B3%C5%82-wy%C5%BCszych-tom-3/pages/9-wstep)

← (początek modułu) · [spis modułu](README.md) · [Struktura krystaliczna ciał stałych](02-krysztaly.md) →

## Po co to jest

Atomy łączą się w cząsteczki i kryształy dzięki siłom elektrycznym, a o kształcie i trwałości wiązań decyduje mechanika kwantowa. Rodzaj wiązania wyjaśnia, dlaczego sól jest krucha i rozpuszcza się w wodzie, metal jest kowalny i przewodzi, diament twardy, a wosk miękki. Widma rotacyjne i oscylacyjne cząsteczek to narzędzie chemii analitycznej, radioastronomii (cząsteczki w obłokach międzygwiazdowych) i fizyki atmosfery (gazy cieplarniane).

## Teoria w pigułce

**Rodzaje wiązań:**

| Wiązanie | Mechanizm | Energia na wiązanie | Przykłady i właściwości |
|---|---|---|---|
| jonowe | przeniesienie elektronu, przyciąganie jonów | kilka eV | NaCl: twarde, kruche, izolatory, rozpuszczalne w wodzie |
| kowalencyjne | wspólne pary elektronów (nakładanie orbitali) | 2–10 eV | H₂ (4,5 eV), diament, krzem: twarde, kierunkowe |
| metaliczne | elektrony walencyjne wspólne dla całego kryształu | 1–5 eV | Cu, Fe, Al: przewodzą, są kowalne |
| wodorowe | przyciąganie H związanego z atomem elektroujemnym do innego takiego atomu | 0,1–0,5 eV | woda, DNA, białka |
| van der Waalsa | przyciąganie chwilowych dipoli | 0,01–0,1 eV | gazy szlachetne, wosk, grafit między warstwami |

**Wiązanie jonowe na przykładzie NaCl.** Oderwanie elektronu od Na kosztuje 5,14 eV (energia jonizacji). Przyłączenie elektronu do Cl daje 3,61 eV (powinowactwo elektronowe). Bilans to −1,53 eV, więc samo przeniesienie się nie opłaca. Opłaca się dopiero przyciąganie jonów: w odległości 0,236 nm energia kulombowska wynosi $ke^2/r \approx 6{,}1\ \mathrm{eV}$. Na małych odległościach jony odpycha zakaz Pauliego (nakładanie się zamkniętych powłok), co ustala długość wiązania.

**Wiązanie kowalencyjne (H₂).** Elektrony o przeciwnych spinach mogą zajmować wspólny orbital między jądrami. Gęstość elektronów między protonami przyciąga oba jądra. Energia wiązania H₂ wynosi 4,5 eV, a długość 0,074 nm.

**Energia cząsteczki dwuatomowej** to suma części elektronowej, oscylacyjnej i rotacyjnej, w malejącej skali:

$$E_{\text{osc}} = \left(n + \tfrac12\right)\hbar\omega\ \ (\sim0{,}1\ \mathrm{eV}), \qquad E_{\text{rot}} = \frac{\hbar^2}{2I}l(l + 1)\ \ (\sim\mathrm{meV}),$$

gdzie $I = \mu r^2$ to moment bezwładności, a $\mu = m_1m_2/(m_1 + m_2)$ masa zredukowana.
- Przejścia elektronowe dają światło widzialne i nadfiolet.
- Oscylacyjne dają podczerwień (20.06): CO₂ i H₂O pochłaniają promieniowanie cieplne Ziemi.
- Rotacyjne dają mikrofale. Reguła wyboru $\Delta l = \pm1$ daje linie co $\hbar^2/I$. Linia CO 115 GHz to podstawowe narzędzie radioastronomii do mapowania obłoków molekularnych.

## Wzory i założenia

| Wzór | Znaczenie | Kiedy obowiązuje |
|---|---|---|
| $U = -ke^2/r + U_{\text{odp}}$ | energia pary jonów | — |
| $\mu = m_1m_2/(m_1 + m_2)$, $I = \mu r^2$ | masa zredukowana, moment bezwładności | cząsteczka dwuatomowa |
| $E_l = \dfrac{\hbar^2}{2I}l(l + 1)$ | poziomy rotacyjne | sztywny rotator |
| $\Delta E_{l\to l+1} = \dfrac{\hbar^2}{I}(l + 1)$ | linie rotacyjne | $\Delta l = \pm1$ |
| $E_n = (n + \tfrac12)\hbar\omega$, $\omega = \sqrt{k/\mu}$ | poziomy oscylacyjne | oscylator harmoniczny |

## Przykład rozwiązany

### Wersja z rachunkiem różniczkowym i całkowym

**Zadanie 1.** Oszacuj energię wiązania NaCl (względem atomów Na i Cl) z energii kulombowskiej w odległości równowagi 0,236 nm, energii jonizacji Na (5,14 eV) i powinowactwa Cl (3,61 eV).

$E \approx 6{,}10 - 5{,}14 + 3{,}61 \approx 4{,}6\ \mathrm{eV}$. Zmierzona wartość to 4,26 eV. Różnicę daje energia odpychania, której model pominął.

**Zadanie 2.** Cząsteczka CO ma długość wiązania 0,113 nm. Oblicz moment bezwładności, odstęp linii rotacyjnych i częstotliwość przejścia $l = 0 \to 1$.

$\mu = \dfrac{12\cdot16}{28}\ \mathrm u \approx 6{,}86\ \mathrm u$, $I = \mu r^2 \approx 1{,}45\cdot10^{-46}\ \mathrm{kg\cdot m^2}$.

$\Delta E_{0\to1} = \hbar^2/I \approx 0{,}48\ \mathrm{meV}$, $f = \Delta E/h \approx 116\ \mathrm{GHz}$, $\lambda \approx 2{,}6\ \mathrm{mm}$. Zmierzona linia: 115,27 GHz.

## Typowe pułapki

- **Wiązanie jonowe opłaca się, bo Na „chce” oddać elektron.** Samo przeniesienie elektronu kosztuje energię. Zysk daje przyciąganie jonów.
- **Wiązania van der Waalsa są nieistotne.** Są słabe, ale decydują o skraplaniu gazów, przyczepności gekonów i właściwościach grafitu.
- **Masa całkowita w momencie bezwładności.** Dla cząsteczki dwuatomowej trzeba użyć masy zredukowanej.
- **Linie rotacyjne są w podczerwieni.** Są w mikrofalach (meV). Oscylacyjne są w podczerwieni.

## Doświadczenie / symulacja

**Symulacja PhET:** *Kształty cząsteczek* (*Molecule Shapes*) i *Polarność cząsteczek* (*Molecule Polarity*) — [phet.colorado.edu/pl](https://phet.colorado.edu/pl/).

**Kryształki soli pod lupą.** Odparuj roztwór soli kuchennej na szkiełku. Pod lupą widać sześcienne kryształki, ślad sieci regularnej NaCl (23.02).

**Python:** krzywa energii potencjalnej pary jonów (model z odpychaniem $B/r^n$) i widmo rotacyjne CO.

```python
import numpy as np
import matplotlib.pyplot as plt

k, e, u, hbar, h = 8.98755e9, 1.602177e-19, 1.66054e-27, 1.054572e-34, 6.62607e-34
r0, n, dE_ion = 0.236e-9, 9, 5.14 - 3.61          # równowaga, wykładnik odpychania, bilans jonizacji [eV]
B = k*e**2*r0**(n - 1)/n                            # z warunku dU/dr = 0 w r0
r = np.linspace(0.15e-9, 1.0e-9, 500)
U = (-k*e**2/r + B/r**n)/e + dE_ion
print(f"energia wiązania NaCl (model): {-(U.min()):.2f} eV przy r = {r[np.argmin(U)]*1e9:.3f} nm (zmierzona 4,26 eV)")

mu = 12*16/28*u; I = mu*(0.1128e-9)**2
for l in range(4):
    dE = hbar**2/I*(l + 1)
    print(f"CO: przejście l = {l} → {l + 1}: {dE/h/1e9:.1f} GHz")
plt.plot(r*1e9, U); plt.axhline(0, color="gray")
plt.ylim(-6, 4); plt.xlabel("r [nm]"); plt.ylabel("U [eV]"); plt.title("Na⁺ + Cl⁻"); plt.grid(True); plt.show()
```

## Zadania

### A. Poziom maturalny _(opcjonalnie — rozgrzewka)_

1. Dlaczego sól kuchenna jest krucha, a miedź kowalna?

<details>
<summary>Odpowiedź</summary>

W krysztale jonowym przesunięcie warstwy ustawia obok siebie jony jednoimienne, które się odpychają, i kryształ pęka. W metalu „gaz” elektronów wiąże jony niezależnie od ich ułożenia, więc warstwy mogą się przesuwać.
</details>

2. Uszereguj wiązania od najsłabszego: kowalencyjne, van der Waalsa, wodorowe.

<details>
<summary>Odpowiedź</summary>

Van der Waalsa, wodorowe, kowalencyjne.
</details>

### B. Poziom akademicki

1. Cząsteczka HCl ma linie rotacyjne odległe o ok. 0,63 THz ($\Delta f = \hbar/(2\pi I)$). Oblicz długość wiązania.

<details>
<summary>Odpowiedź</summary>

$\Delta E = \hbar^2/I = h\Delta f \Rightarrow I = \hbar/(2\pi\Delta f) \approx 2{,}7\cdot10^{-47}\ \mathrm{kg\cdot m^2}$. $\mu \approx \dfrac{1\cdot35}{36}\ \mathrm u = 1{,}61\cdot10^{-27}\ \mathrm{kg}$, $r = \sqrt{I/\mu} \approx 0{,}13\ \mathrm{nm}$.
</details>

2. Cząsteczka CO drga z częstotliwością $6{,}4\cdot10^{13}\ \mathrm{Hz}$ (20.06). Oblicz stałą sprężystości wiązania.

<details>
<summary>Odpowiedź</summary>

$k = \mu\omega^2 = 6{,}86\cdot1{,}66\cdot10^{-27}\cdot(2\pi\cdot6{,}4\cdot10^{13})^2 \approx 1850\ \mathrm{N/m}$. To sztywność zwykłej sprężyny, choć dotyczy pojedynczego wiązania o długości ułamka nanometra.
</details>

3. Dla modelu $U(r) = -\dfrac{ke^2}{r} + \dfrac{B}{r^n}$ wyznacz $B$ z warunku równowagi w $r_0$ i pokaż, że energia wiązania pary jonów wynosi $\dfrac{ke^2}{r_0}\left(1 - \dfrac1n\right)$.

<details>
<summary>Odpowiedź</summary>

$U'(r_0) = 0 \Rightarrow B = \dfrac{ke^2r_0^{n-1}}{n}$. $U(r_0) = -\dfrac{ke^2}{r_0} + \dfrac{ke^2}{nr_0} = -\dfrac{ke^2}{r_0}\left(1 - \dfrac1n\right)$.
</details>

## Źródła

- OpenStax, *Fizyka dla szkół wyższych*, t. 3, rozdz. 9 — §9.1 (rodzaje wiązań) i §9.2 (widma cząsteczek).
- Halliday, Resnick, Walker, *Podstawy fizyki*, wyd. 2015, t. 5, rozdz. 41 (wstęp o wiązaniach w ciałach stałych).
- Symulacje PhET *Kształty cząsteczek* i *Polarność cząsteczek*.
