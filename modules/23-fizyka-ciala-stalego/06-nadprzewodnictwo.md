# 23.06 — Nadprzewodnictwo

> **Moduł:** [23 — Fizyka ciała stałego](README.md) · **Poziom:** 🔵 studia · **Status:** ✅ pełny
>
> **Czytaj:**
>
> - OpenStax, *Fizyka dla szkół wyższych*, t. 3, rozdz. 9: [§9.8](https://openstax.org/books/fizyka-dla-szk%C3%B3%C5%82-wy%C5%BCszych-tom-3/pages/9-8-nadprzewodnictwo) · [wstęp do rozdziału](https://openstax.org/books/fizyka-dla-szk%C3%B3%C5%82-wy%C5%BCszych-tom-3/pages/9-wstep)
> - Halliday, Resnick, Walker, *Podstawy fizyki*, wyd. 2015, t. 3: §26.5 (s. 196)
> - Halliday, Resnick, Walker, *Podstawy fizyki*, wyd. 1 (2003), t. 3: §27.9, s. 147 (skan t. 3 na serwerze AGH kończy się na s. 127 — dalsze strony tylko w wydaniu papierowym)

← [Półprzewodniki, domieszkowanie i złącze p-n](05-polprzewodniki.md) · [spis modułu](README.md) · (koniec modułu) →

## Po co to jest

Poniżej temperatury krytycznej niektóre materiały tracą opór elektryczny całkowicie, a nie tylko prawie. Prąd w pierścieniu nadprzewodzącym krąży latami bez zasilania. Nadprzewodniki wypychają też pole magnetyczne (efekt Meissnera), co pozwala lewitować magnesom. Z nadprzewodników są uzwojenia magnesów w tomografach MRI, akceleratorach (LHC) i tokamakach (22.06), najczulsze magnetometry (SQUID) i kubity wielu komputerów kwantowych. To makroskopowy efekt kwantowy: miliardy elektronów zachowują się jak jedna fala.

## Teoria w pigułce

**Zanik oporu.** W 1911 r. Heike Kamerlingh Onnes zauważył, że rtęć poniżej 4,2 K ma opór równy zeru (w granicach pomiaru). **Temperatura krytyczna** $T_c$ jest cechą materiału:

| Materiał | $T_c$ | Uwagi |
|---|---|---|
| Al | 1,2 K | — |
| Hg | 4,2 K | pierwszy odkryty |
| Pb | 7,2 K | — |
| Nb | 9,3 K | najwyższa wśród pierwiastków (pod ciśnieniem normalnym) |
| NbTi | ok. 10 K | druty w MRI i LHC |
| Nb₃Sn | 18 K | magnesy wysokopolowe, ITER |
| MgB₂ | 39 K | — |
| YBa₂Cu₃O₇ (YBCO) | 92 K | **wysokotemperaturowy**, powyżej 77 K (ciekły azot) |

Miedzianowe nadprzewodniki wysokotemperaturowe (1986) można chłodzić tanim ciekłym azotem zamiast ciekłego helu (4,2 K).

**Efekt Meissnera.** Nadprzewodnik to nie tylko „idealny przewodnik”. Wypycha pole magnetyczne ze swego wnętrza (jest idealnym diamagnetykiem, $\chi = -1$, 14.07), nawet gdy pole było przyłożone przed schłodzeniem. Pole wnika tylko na **głębokość wnikania** ok. 50–500 nm. Dlatego magnes lewituje nad nadprzewodnikiem.

**Pole krytyczne.** Zbyt silne pole niszczy nadprzewodnictwo:

$$B_c(T) \approx B_c(0)\left[1 - \left(\frac{T}{T_c}\right)^2\right].$$

- **Nadprzewodniki I rodzaju** (Pb, Hg, Al): pole krytyczne poniżej 0,1 T.
- **Nadprzewodniki II rodzaju** (NbTi, Nb₃Sn, YBCO): pole wnika w postaci kwantowanych wirów strumienia i nadprzewodnictwo przetrwa do kilkunastu–kilkudziesięciu tesli. Tylko one nadają się na magnesy.

**Teoria BCS (Bardeen, Cooper, Schrieffer, 1957).** Elektron przelatujący przez sieć lekko przyciąga dodatnie jony. Powstałe zagęszczenie ładunku dodatniego przyciąga drugi elektron. W ten sposób elektrony o przeciwnych pędach i spinach łączą się w **pary Coopera**. Para ma spin całkowity 0 i zachowuje się jak bozon, więc wszystkie pary mogą zająć jeden wspólny stan kwantowy (por. kondensat Bosego–Einsteina). Rozbicie pary wymaga energii $2\Delta$ (**przerwa nadprzewodząca**, w teorii BCS $\Delta \approx 1{,}76kT_c$, rzędu meV). Drgania sieci w niskiej temperaturze nie mają takiej energii, więc nie mogą rozpraszać par i opór znika.

Dowodem roli sieci jest **efekt izotopowy**: $T_c \propto M^{-1/2}$ (cięższe izotopy mają niższe $T_c$). Teoria BCS nie wyjaśnia w pełni nadprzewodników wysokotemperaturowych. Ich mechanizm wciąż jest badany.

**Kwantowanie strumienia.** Strumień magnetyczny przez pierścień nadprzewodzący jest wielokrotnością kwantu strumienia:

$$\Phi_0 = \frac{h}{2e} \approx 2{,}07\cdot10^{-15}\ \mathrm{Wb}.$$

Czynnik $2e$ to bezpośredni dowód, że nośnikami są pary.

**Złącze Josephsona** to dwa nadprzewodniki rozdzielone cienką barierą izolatora (ok. 1 nm). Pary tunelują przez nią (20.07). Przy stałym napięciu $U$ płynie prąd przemienny o częstotliwości $f = 2eU/h$ (483,6 MHz na μV). Służy to do realizacji wzorca wolta. SQUID (pierścień z dwoma złączami) mierzy pola rzędu $10^{-15}$ T, np. pola magnetyczne mózgu.

## Wzory i założenia

| Wzór | Znaczenie | Kiedy obowiązuje |
|---|---|---|
| $R = 0$ dla $T < T_c$ | brak oporu | prąd i pole poniżej krytycznych |
| $B_c(T) \approx B_c(0)[1 - (T/T_c)^2]$ | pole krytyczne | przybliżenie empiryczne |
| $\Delta \approx 1{,}76kT_c$ | przerwa nadprzewodząca w 0 K | teoria BCS, słabe sprzężenie |
| $\Phi = n\Phi_0$, $\Phi_0 = h/(2e)$ | kwantowanie strumienia | pierścień nadprzewodzący |
| $f = 2eU/h$ | efekt Josephsona (zmiennoprądowy) | złącze Josephsona |
| $T_c \propto M^{-1/2}$ | efekt izotopowy | nadprzewodniki konwencjonalne |

## Przykład rozwiązany

### Wersja z rachunkiem różniczkowym i całkowym

**Zadanie 1.** Ołów: $T_c = 7{,}2\ \mathrm K$, $B_c(0) = 0{,}080\ \mathrm T$. Oblicz pole krytyczne w 4,2 K i największy prąd, jaki może płynąć bez oporu w drucie o promieniu 0,5 mm (reguła Silsbee: pole przy powierzchni nie może przekroczyć $B_c$).

$B_c(4{,}2\ \mathrm K) = 0{,}080\left[1 - (4{,}2/7{,}2)^2\right] \approx 0{,}053\ \mathrm T$.

Z prawa Ampère'a (14.05) $B = \mu_0I/(2\pi r)$, więc $I_c = \dfrac{2\pi rB_c}{\mu_0} \approx 132\ \mathrm A$ (w 0 K: 200 A).

Pochodna pola krytycznego przy $T_c$: $\dfrac{dB_c}{dT}\Big|_{T_c} = -\dfrac{2B_c(0)}{T_c} \approx -0{,}022\ \mathrm{T/K}$.

**Zadanie 2.** Oblicz przerwę nadprzewodzącą niobu ($T_c = 9{,}3\ \mathrm K$) i częstotliwość fotonu, który rozbija parę Coopera.

$\Delta = 1{,}76\cdot8{,}62\cdot10^{-5}\cdot9{,}3 \approx 1{,}4\ \mathrm{meV}$ (zmierzone ok. 1,5 meV).

$f = 2\Delta/h \approx 680\ \mathrm{GHz}$ ($\lambda \approx 0{,}44\ \mathrm{mm}$). Na tym działają nadprzewodnikowe detektory promieniowania submilimetrowego w radioastronomii.

**Zadanie 3.** Oblicz energię zgromadzoną w polu magnesu MRI o indukcji 3 T w objętości ok. 1 m³.

$E = \dfrac{B^2}{2\mu_0}V \approx 3{,}6\ \mathrm{MJ}$ (16.04). Przy utracie nadprzewodnictwa (**quench**) ta energia zamienia się w ciepło i odparowuje hel, dlatego magnesy mają systemy zabezpieczeń.

## Typowe pułapki

- **Nadprzewodnik to po prostu idealny przewodnik.** Idealny przewodnik zachowałby pole, które było w nim przed schłodzeniem. Nadprzewodnik je wypycha (efekt Meissnera). To odrębny stan materii.
- **Najlepsze przewodniki (miedź, srebro, złoto) są najlepszymi nadprzewodnikami.** Nie są w ogóle nadprzewodnikami, bo ich elektrony słabo oddziałują z siecią. A to oddziaływanie jest potrzebne do tworzenia par Coopera.
- **Nadprzewodnik przewodzi dowolny prąd.** Zbyt duży prąd lub pole niszczą nadprzewodnictwo.
- **Nadprzewodniki wysokotemperaturowe działają w temperaturze pokojowej.** „Wysoka” temperatura to ok. 90–130 K. Doniesienia o nadprzewodnictwie w temperaturze pokojowej (np. LK-99 w 2023 r.) nie zostały potwierdzone.

## Doświadczenie / symulacja

**Lewitacja nad YBCO.** Zestawy edukacyjne zawierają krążek YBCO i mały magnes neodymowy. Schłodź krążek ciekłym azotem (77 K, z zachowaniem zasad BHP: rękawice, okulary) i połóż magnes nad nim. Magnes lewituje. W nadprzewodniku II rodzaju wiry strumienia „przypinają” magnes, więc można go nawet zawiesić pod krążkiem. Zmierz czas, po jakim krążek się ogrzeje i magnes opadnie.

**Python:** pole krytyczne $B_c(T)$, przerwa BCS z równania na przerwę i kwantowanie strumienia.

```python
import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import quad
from scipy.optimize import brentq

e, h, kB, mu0 = 1.602176634e-19, 6.62607015e-34, 8.617333e-5, 4e-7*np.pi
for nazwa, Tc, Bc0 in [("Al", 1.18, 0.0105), ("Pb", 7.2, 0.080), ("Nb", 9.3, 0.20)]:
    T = np.linspace(0, Tc, 200)
    plt.plot(T, Bc0*(1 - (T/Tc)**2), label=nazwa)
    D = 1.76*kB*Tc
    print(f"{nazwa}: Δ(0) = {D*1e3:.2f} meV, foton rozbijający parę: {2*D*e/h/1e9:.0f} GHz")
print(f"Pb w 4,2 K: B_c = {0.080*(1 - (4.2/7.2)**2):.4f} T, I_c (r = 0,5 mm) = {2*np.pi*5e-4*0.080*(1 - (4.2/7.2)**2)/mu0:.0f} A")
print(f"kwant strumienia h/2e = {h/(2*e):.4e} Wb, Josephson: {2*e/h/1e12:.2f} MHz/μV")

# równanie BCS na przerwę: 1 = λ ∫_0^{ħω_D} tanh(√(ε²+Δ²)/2kT)/√(ε²+Δ²) dε
wD, lam = 1.0, 0.3                                      # energia Debye'a (jednostki umowne), stała sprzężenia
def rown(D, T):
    f = lambda x: np.tanh(np.sqrt(x**2 + D**2)/(2*T))/np.sqrt(x**2 + D**2)
    return lam*quad(f, 0, wD, limit=200)[0] - 1
D0 = 2*wD*np.exp(-1/lam)
Tc = brentq(lambda T: rown(1e-9, T), 1e-3, 1.0)
print(f"BCS: Δ(0)/kTc = {D0/Tc:.3f} (teoria: 1,764)")
Ts = np.linspace(0.02*Tc, 0.999*Tc, 40)
Ds = [brentq(rown, 1e-9, 2*D0, args=(T,)) for T in Ts]
plt.figure(); plt.plot(Ts/Tc, np.array(Ds)/D0); plt.xlabel("T / Tc"); plt.ylabel("Δ(T) / Δ(0)"); plt.grid(True); plt.show()
```

## Zadania

### A. Poziom maturalny _(opcjonalnie — rozgrzewka)_

1. Czym różni się zachowanie oporu metalu i nadprzewodnika przy chłodzeniu do 0 K?

<details>
<summary>Odpowiedź</summary>

Opór metalu maleje stopniowo do wartości resztkowej (domieszki, defekty). Opór nadprzewodnika spada skokowo do zera w temperaturze krytycznej.
</details>

2. Dlaczego odkrycie nadprzewodników o $T_c > 77\ \mathrm K$ było tak ważne?

<details>
<summary>Odpowiedź</summary>

Można je chłodzić ciekłym azotem, który jest tani i łatwo dostępny, zamiast drogiego i rzadkiego ciekłego helu.
</details>

### B. Poziom akademicki

1. Pierścień nadprzewodzący o powierzchni 1 cm² schłodzono w polu Ziemi (50 μT, prostopadle). Ile kwantów strumienia jest uwięzionych?

<details>
<summary>Odpowiedź</summary>

$\Phi/\Phi_0 = \dfrac{5\cdot10^{-5}\cdot10^{-4}}{2{,}07\cdot10^{-15}} \approx 2{,}4\cdot10^6$.
</details>

2. Na złączu Josephsona jest napięcie 10 μV. Jaka jest częstotliwość prądu? Dlaczego to pozwala zdefiniować wolt?

<details>
<summary>Odpowiedź</summary>

$f = 2eU/h \approx 4{,}84\ \mathrm{GHz}$. Częstotliwości mierzy się z dokładnością zegarów atomowych, a $2e/h$ jest stałą o ustalonej wartości (SI od 2019 r.), więc napięcie wyznacza się przez pomiar częstotliwości.
</details>

3. W jakiej temperaturze pole krytyczne ołowiu spada do połowy wartości w 0 K?

<details>
<summary>Odpowiedź</summary>

$1 - (T/T_c)^2 = \tfrac12 \Rightarrow T = T_c/\sqrt2 \approx 5{,}1\ \mathrm K$.
</details>

4. Rtęć ²⁰⁰Hg ma $T_c = 4{,}17\ \mathrm K$. Oszacuj $T_c$ dla ²⁰⁴Hg z efektu izotopowego.

<details>
<summary>Odpowiedź</summary>

$T_c = 4{,}17\sqrt{200/204} \approx 4{,}13\ \mathrm K$.
</details>

## Źródła

- OpenStax, *Fizyka dla szkół wyższych*, t. 3, rozdz. 9 — §9.8: nadprzewodnictwo.
- Halliday, Resnick, Walker, *Podstawy fizyki* — wyd. 2015: t. 3, §26.5; wyd. 1: t. 3, §27.9.
