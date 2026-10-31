# 22.03 — Rozpady promieniotwórcze i prawo rozpadu

> **Moduł:** [22 — Fizyka jądrowa](README.md) · **Poziom:** 🟢🔵 matura R + studia · **Status:** ✅ pełny
>
> **Czytaj:**
>
> - OpenStax, *Fizyka dla szkół wyższych*, t. 3, rozdz. 10: [§10.3](https://openstax.org/books/fizyka-dla-szk%C3%B3%C5%82-wy%C5%BCszych-tom-3/pages/10-3-rozpad-promieniotworczy) · [wstęp do rozdziału](https://openstax.org/books/fizyka-dla-szk%C3%B3%C5%82-wy%C5%BCszych-tom-3/pages/10-wstep)
> - Halliday, Resnick, Walker, *Podstawy fizyki*, wyd. 2015, t. 5: §42.3–42.6 (s. 175)
> - Halliday, Resnick, Walker, *Podstawy fizyki*, wyd. 1 (2003), t. 5: [§43.3–43.6, s. 144](https://home.agh.edu.pl/~czapli/Resnick_5.pdf#page=160) — PDF z serwera AGH

← [Energia wiązania i deficyt masy](02-energia-wiazania.md) · [spis modułu](README.md) · [Reakcje jądrowe i zasady zachowania](04-reakcje-jadrowe.md) →

## Po co to jest

Jądra niestabilne rozpadają się samorzutnie, emitując promieniowanie. Prawo rozpadu pozwala datować wykopaliska (węgiel-14), skały i wiek Ziemi (uran-ołów), dobierać izotopy do diagnostyki i terapii (technet-99m, jod-131, fluor-18 w PET), planować składowanie odpadów jądrowych i oceniać zagrożenie radonem w domach. To też najlepszy przykład wykładniczego zaniku w przyrodzie, z tą samą matematyką co rozładowanie kondensatora (13.06).

## Teoria w pigułce

**Rodzaje rozpadów:**

| Rozpad | Co emituje | Zmiana jądra | Przykład |
|---|---|---|---|
| alfa (α) | jądro ⁴He | $Z - 2$, $A - 4$ | $^{238}\mathrm U \to {}^{234}\mathrm{Th} + \alpha$ |
| beta minus (β⁻) | elektron i antyneutrino | $Z + 1$, $A$ bez zmian ($n \to p$) | $^{14}\mathrm C \to {}^{14}\mathrm N + e^- + \bar\nu$ |
| beta plus (β⁺) | pozyton i neutrino | $Z - 1$ ($p \to n$) | $^{18}\mathrm F \to {}^{18}\mathrm O + e^+ + \nu$ |
| wychwyt elektronu | neutrino | $Z - 1$ | $^{40}\mathrm K + e^- \to {}^{40}\mathrm{Ar} + \nu$ |
| gamma (γ) | foton | bez zmian ($Z$, $A$), jądro przechodzi na niższy poziom | $^{60}\mathrm{Ni}^* \to {}^{60}\mathrm{Ni} + \gamma$ |

W każdym rozpadzie zachowane są ładunek, liczba nukleonów, energia i pęd. Energia rozpadu $Q$ to różnica mas przed i po.
- W rozpadzie alfa cząstki mają ściśle określone energie (rozpad na dwa ciała).
- W rozpadzie beta elektrony mają widmo ciągłe, bo energię dzieli się z neutrinem. To doprowadziło Pauliego do postulowania neutrina w 1930 r.

**Prawo rozpadu.** Każde jądro ma stałe prawdopodobieństwo rozpadu na jednostkę czasu $\lambda$ (stała rozpadu), niezależne od wieku, temperatury i chemii. Stąd

$$\frac{dN}{dt} = -\lambda N \Rightarrow N(t) = N_0e^{-\lambda t} = N_0\left(\frac12\right)^{t/T_{1/2}}, \qquad T_{1/2} = \frac{\ln2}{\lambda}.$$

Średni czas życia: $\tau = 1/\lambda = T_{1/2}/\ln2$.

**Aktywność** to liczba rozpadów na sekundę, $A = \lambda N$. Jednostką jest bekerel ($1\ \mathrm{Bq} = 1$ rozpad/s). Dawna jednostka to kiur, $1\ \mathrm{Ci} = 3{,}7\cdot10^{10}\ \mathrm{Bq}$ (aktywność 1 g radu-226). Aktywność maleje tak samo jak liczba jąder.

**Datowanie radiowęglowe.** Promieniowanie kosmiczne stale wytwarza ¹⁴C w atmosferze ($T_{1/2} = 5730$ lat). Żywe organizmy mają stały stosunek ¹⁴C/¹²C, a po śmierci ¹⁴C zanika. Pomiar aktywności lub liczby atomów ¹⁴C (spektrometria mas, 14.03) daje wiek do ok. 50 000 lat.

**Szeregi promieniotwórcze.** Ciężkie jądra rozpadają się wielokrotnie, aż do stabilnego ołowiu. Na przykład szereg uranowo-radowy ²³⁸U → … → ²⁰⁶Pb ma 8 rozpadów α i 6 rozpadów β. Po drodze powstaje radon-222, gaz gromadzący się w piwnicach, główne źródło naturalnej dawki promieniowania (22.07).

## Wzory i założenia

| Wzór | Znaczenie | Kiedy obowiązuje |
|---|---|---|
| $N = N_0e^{-\lambda t} = N_0(1/2)^{t/T_{1/2}}$ | prawo rozpadu | duża liczba jąder |
| $T_{1/2} = \ln2/\lambda$, $\tau = 1/\lambda$ | czas połowicznego zaniku, średni czas życia | — |
| $A = \lambda N$ | aktywność | — |
| $t = \dfrac{T_{1/2}}{\ln2}\ln\dfrac{A_0}{A}$ | wiek z aktywności | datowanie |
| $Q = (m_{\text{przed}} - m_{\text{po}})c^2$ | energia rozpadu | masy atomowe (dla β⁺ trzeba dodać $2m_ec^2$) |

## Przykład rozwiązany

**Zadanie 1.** Próbka drewna z wykopaliska ma 25% aktywności ¹⁴C świeżego drewna. Ile ma lat? A gdyby miała 30%?

25%: dwa okresy połowicznego zaniku, 11 460 lat. 30%: $t = 5730\cdot\dfrac{\ln(1/0{,}3)}{\ln2} \approx 9950$ lat.

**Zadanie 2.** Oblicz aktywność 1 g radu-226 ($T_{1/2} = 1600$ lat).

$N = 6{,}022\cdot10^{23}/226 \approx 2{,}66\cdot10^{21}$, $\lambda = \ln2/(1600\cdot3{,}156\cdot10^7\ \mathrm s) \approx 1{,}37\cdot10^{-11}\ \mathrm{s^{-1}}$, $A \approx 3{,}7\cdot10^{10}\ \mathrm{Bq}$, czyli 1 Ci.

**Zadanie 3.** Oblicz energię rozpadu alfa uranu-238 (masy: ²³⁸U 238,050788 u, ²³⁴Th 234,043601 u, ⁴He 4,002603 u). Jaką energię kinetyczną ma cząstka alfa?

$Q = (238{,}050788 - 234{,}043601 - 4{,}002603)\cdot931{,}5 \approx 4{,}27\ \mathrm{MeV}$. Z zasady zachowania pędu cząstka alfa unosi ułamek $\dfrac{m_{\mathrm{Th}}}{m_{\mathrm{Th}} + m_\alpha} \approx \dfrac{234}{238}$, czyli ok. 4,2 MeV.

### Wersja z rachunkiem różniczkowym i całkowym

**Szereg dwóch rozpadów** A → B → C (stałe $\lambda_A$, $\lambda_B$):

$$\frac{dN_B}{dt} = \lambda_AN_A - \lambda_BN_B \Rightarrow N_B(t) = N_{A0}\frac{\lambda_A}{\lambda_B - \lambda_A}\left(e^{-\lambda_At} - e^{-\lambda_Bt}\right).$$

Gdy matka żyje dużo dłużej ($\lambda_A \ll \lambda_B$), po kilku okresach córki ustala się **równowaga wiekowa**: $\lambda_AN_A = \lambda_BN_B$, czyli aktywności matki i córki są równe. Dlatego w rudzie uranowej rad i radon mają tę samą aktywność co uran. Podobnie działa generator technetu w szpitalach (⁹⁹Mo, 66 h → ⁹⁹ᵐTc, 6 h). Tu okresy różnią się tylko 11 razy, więc ustala się równowaga przejściowa: aktywność córki to ok. $\lambda_B/(\lambda_B - \lambda_A) \approx 1{,}1$ aktywności matki.

## Typowe pułapki

- **Po dwóch okresach połowicznego zaniku nie zostaje nic.** Zostaje 1/4, po trzech 1/8.
- **Można przewidzieć, kiedy rozpadnie się dane jądro.** Prawo rozpadu jest statystyczne. Pojedyncze jądro rozpada się w przypadkowej chwili.
- **Rozpad beta minus = elektron z powłoki.** Elektron powstaje w jądrze z przemiany neutronu w proton.
- **W rozpadzie gamma zmienia się pierwiastek.** $Z$ i $A$ się nie zmieniają, jądro tylko traci energię wzbudzenia.
- **Aktywność zależy od masy, nie od okresu.** $A = \lambda N$: przy tej samej liczbie atomów krótko żyjący izotop jest dużo bardziej aktywny.

## Doświadczenie / symulacja

**Rzut kostkami.** Rzuć 100 kostkami do gry (albo cukierkami z napisem po jednej stronie). Te, które pokażą „6”, odkładasz jako „rozpadnięte”. Powtarzaj i notuj liczbę pozostałych. Wykres $\ln N$ od numeru rzutu jest w przybliżeniu prostą o nachyleniu $\ln(5/6)$. Okres połowicznego zaniku to ok. 3,8 rzutu.

**Licznik Geigera.** Jeśli masz dostęp (szkoła, aplikacja z zewnętrznym licznikiem), zmierz tło promieniowania w domu, w piwnicy i na zewnątrz. Rozkład liczby zliczeń w krótkich przedziałach czasu to rozkład Poissona (01.03).

**Symulacja PhET:** *Rozpad alfa*, *Rozpad beta*, *Datowanie radiometryczne* (*Alpha Decay*, *Beta Decay*, *Radioactive Dating Game*) — [phet.colorado.edu/pl](https://phet.colorado.edu/pl/).

**Python:** Monte Carlo rozpadu pojedynczych jąder porównane z prawem wykładniczym oraz szereg rozpadów.

```python
import numpy as np
import matplotlib.pyplot as plt

rng = np.random.default_rng(0)
N0, p = 10000, 1/6                                 # „kostki”: prawdopodobieństwo rozpadu na krok
N, hist = N0, [N0]
for _ in range(30):
    N -= rng.binomial(N, p); hist.append(N)
hist = np.array(hist)
k = np.arange(len(hist))
lam = -np.polyfit(k[:20], np.log(hist[:20]), 1)[0]
print(f"λ z symulacji = {lam:.4f}, teoria −ln(5/6) = {-np.log(5/6):.4f}, T½ = {np.log(2)/lam:.2f} kroku")

print(f"wiek przy 25 % ¹⁴C: {5730*2:.0f} lat; przy 30 %: {5730*np.log(1/0.3)/np.log(2):.0f} lat")
NA = 6.02214076e23
print(f"aktywność 1 g Ra-226: {np.log(2)/(1600*3.15576e7)*NA/226:.3e} Bq")

lA, lB = np.log(2)/66, np.log(2)/6                  # Mo-99 → Tc-99m (godziny)
t = np.linspace(0, 120, 500)
NB = lA/(lB - lA)*(np.exp(-lA*t) - np.exp(-lB*t))
plt.semilogy(k, hist, "o", label="symulacja"); plt.semilogy(k, N0*(5/6)**k, label="N0 (5/6)^k")
plt.xlabel("krok"); plt.ylabel("N"); plt.legend(); plt.grid(True, which="both"); plt.show()
print(f"generator Tc: maksimum Tc-99m po {t[np.argmax(NB)]:.1f} h, potem A_Tc/A_Mo → {lB*NB[-1]/(lA*np.exp(-lA*t[-1])):.3f}")
```

## Zadania

### A. Poziom maturalny

1. Jod-131 ma $T_{1/2} = 8$ dni. Jaka część dawki zostanie w organizmie po 30 dniach (pomiń wydalanie)?

<details>
<summary>Odpowiedź</summary>

$(1/2)^{30/8{,}02} \approx 0{,}075$, ok. 7,5%.
</details>

2. Uzupełnij: $^{226}_{88}\mathrm{Ra} \to {}^{?}_{?}\mathrm{Rn} + \alpha$ oraz $^{60}_{27}\mathrm{Co} \to {}^{?}_{?}\mathrm{Ni} + e^- + \bar\nu$.

<details>
<summary>Odpowiedź</summary>

$^{222}_{86}\mathrm{Rn}$ i $^{60}_{28}\mathrm{Ni}$.
</details>

3. Ile rozpadów α i β⁻ zachodzi w szeregu od ²³⁸U do ²⁰⁶Pb?

<details>
<summary>Odpowiedź</summary>

$A$ maleje o 32, więc 8 rozpadów α. To obniża $Z$ o 16 (z 92 do 76), a ołów ma $Z = 82$, więc potrzeba 6 rozpadów β⁻.
</details>

4. Ludzkie ciało zawiera ok. 140 g potasu, z czego 0,0117% to promieniotwórczy ⁴⁰K ($T_{1/2} = 1{,}25\cdot10^9$ lat). Oblicz aktywność.

<details>
<summary>Odpowiedź</summary>

$N \approx 2{,}5\cdot10^{20}$, $A = \lambda N \approx 4400\ \mathrm{Bq}$. Każdy z nas jest lekko promieniotwórczy.
</details>

### B. Poziom akademicki

1. Pokaż, że średni czas życia $\tau = \dfrac{1}{N_0}\displaystyle\int_0^\infty t\lambda N(t)\,dt = 1/\lambda$.

<details>
<summary>Odpowiedź</summary>

$\lambda N(t)\,dt/N_0$ to ułamek jąder rozpadających się w chwili $t$, więc $\tau = \displaystyle\int_0^\infty t\lambda e^{-\lambda t}dt = \lambda\cdot\frac{1}{\lambda^2} = \frac1\lambda$ (całka $\int_0^\infty te^{-\lambda t}dt = 1/\lambda^2$).
</details>

2. Stosunek ²⁰⁶Pb do ²³⁸U w skale wynosi 0,9 (cały ołów pochodzi z rozpadu). Oblicz wiek skały ($T_{1/2} = 4{,}47\cdot10^9$ lat).

<details>
<summary>Odpowiedź</summary>

$N_{\mathrm{Pb}}/N_{\mathrm U} = e^{\lambda t} - 1 = 0{,}9 \Rightarrow t = \dfrac{T_{1/2}}{\ln2}\ln1{,}9 \approx 4{,}1\cdot10^9$ lat.
</details>

3. Wyprowadź warunek równowagi wiekowej $\lambda_AN_A = \lambda_BN_B$ z rozwiązania dla szeregu dwóch rozpadów przy $\lambda_A \ll \lambda_B$ i $t \gg 1/\lambda_B$.

<details>
<summary>Odpowiedź</summary>

Wtedy $e^{-\lambda_Bt} \to 0$, a $\lambda_B - \lambda_A \approx \lambda_B$, więc $N_B \approx N_{A0}\dfrac{\lambda_A}{\lambda_B}e^{-\lambda_At} = \dfrac{\lambda_A}{\lambda_B}N_A$.
</details>

### C. Zadania z arkuszy maturalnych CKE

Zadania z egzaminów maturalnych (poziom rozszerzony, formuła 2023), w których ten temat jest potrzebny. Rozwiąż je samodzielnie, a potem porównaj z zasadami oceniania. Pełne zestawienie: [matura/README.md](../../matura/README.md).

- Maj 2023, zad. 11.2 — pierwiastek po sześciu rozpadach α ([arkusz](https://cke.gov.pl/images/_EGZAMIN_MATURALNY_OD_2023/Arkusze_egzaminacyjne/2023/Fizyka/MFAP-R0-100-2305.pdf), [zasady oceniania](https://cke.gov.pl/images/_EGZAMIN_MATURALNY_OD_2023/Arkusze_egzaminacyjne/2023/Fizyka/MFAP-R0-100-2305-zasady.pdf))
- Maj 2024, zad. 11.1 — czas połowicznego rozpadu fluoru-18 z wykresu ([arkusz](https://cke.gov.pl/images/_EGZAMIN_MATURALNY_OD_2023/Arkusze_egzaminacyjne/2024/Fizyka/MFAP-R0-100-A-2405-arkusz.pdf), [zasady oceniania](https://cke.gov.pl/egzamin-maturalny/egzamin-maturalny-w-formule-2023/arkusze/2024-2/))
- Maj 2024, zad. 11.2 — równanie rozpadu β⁺ ([arkusz](https://cke.gov.pl/images/_EGZAMIN_MATURALNY_OD_2023/Arkusze_egzaminacyjne/2024/Fizyka/MFAP-R0-100-A-2405-arkusz.pdf), [zasady oceniania](https://cke.gov.pl/egzamin-maturalny/egzamin-maturalny-w-formule-2023/arkusze/2024-2/))
- Maj 2025, zad. 12.1 — rozpad α plutonu-238 ([arkusz](https://www.oke.poznan.pl/files/cms/875/mfap_r0_100_a_2505_arkusz.pdf), [zasady oceniania](https://cke.gov.pl/egzamin-maturalny/egzamin-maturalny-w-formule-2023/arkusze/2025-2/))
- Maj 2025, zad. 12.3 — czas połowicznego rozpadu z mocy cieplnej źródła ([arkusz](https://www.oke.poznan.pl/files/cms/875/mfap_r0_100_a_2505_arkusz.pdf), [zasady oceniania](https://cke.gov.pl/egzamin-maturalny/egzamin-maturalny-w-formule-2023/arkusze/2025-2/))
- Maj 2026, zad. 11.1 — równanie rozpadu β⁻ neonu-23 ([arkusz](https://oke.wroc.pl/egzamin-maturalny/egzamin-maturalny-2026-arkusze/), [zasady oceniania](https://cke.gov.pl/egzamin-maturalny/egzamin-maturalny-w-formule-2023/arkusze/))
- Maj 2026, zad. 11.3 — czas połowicznego rozpadu z wykresu log m(t) ([arkusz](https://oke.wroc.pl/egzamin-maturalny/egzamin-maturalny-2026-arkusze/), [zasady oceniania](https://cke.gov.pl/egzamin-maturalny/egzamin-maturalny-w-formule-2023/arkusze/))

## Źródła

- OpenStax, *Fizyka dla szkół wyższych*, t. 3, rozdz. 10 — §10.3: rozpady promieniotwórcze.
- Halliday, Resnick, Walker, *Podstawy fizyki* — wyd. 2015: t. 5, §42.3–42.6; wyd. 1: t. 5, §43.3–43.6.
- Symulacje PhET o rozpadach i datowaniu.
