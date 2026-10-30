# 21.05 — Widma atomowe i promieniowanie rentgenowskie

> **Moduł:** [21 — Fizyka atomowa](README.md) · **Poziom:** 🟢🔵 matura R + studia · **Status:** ✅ pełny
>
> **Czytaj:**
>
> - OpenStax, *Fizyka dla szkół wyższych*, t. 3, rozdz. 8: [§8.5](https://openstax.org/books/fizyka-dla-szk%C3%B3%C5%82-wy%C5%BCszych-tom-3/pages/8-5-widma-atomowe-i-promieniowanie-rentgenowskie) · [wstęp do rozdziału](https://openstax.org/books/fizyka-dla-szk%C3%B3%C5%82-wy%C5%BCszych-tom-3/pages/8-wstep)
> - Halliday, Resnick, Walker, *Podstawy fizyki*, wyd. 2015, t. 5: §40.6 (s. 109)
> - Halliday, Resnick, Walker, *Podstawy fizyki*, wyd. 1 (2003), t. 5: [§41.10, s. 85](https://home.agh.edu.pl/~czapli/Resnick_5.pdf#page=101) — PDF z serwera AGH

← [Zakaz Pauliego i układ okresowy](04-zakaz-pauliego.md) · [spis modułu](README.md) · [Emisja wymuszona i lasery](06-lasery.md) →

## Po co to jest

Każdy pierwiastek ma unikalne widmo, swój „odcisk palca”. Z linii w świetle gwiazd poznaje się ich skład i temperaturę (hel odkryto najpierw w widmie Słońca). Analizy spektralne identyfikują metale w wodzie, stopach i zabytkach. Promieniowanie rentgenowskie pozwala prześwietlać ciało, a widmo charakterystyczne z lampy rentgenowskiej umożliwiło Moseleyowi uporządkowanie układu okresowego według liczby atomowej, a nie masy.

## Teoria w pigułce

**Widma optyczne atomów.** Linie widzialne i nadfioletowe powstają przy przejściach **zewnętrznych** (walencyjnych) elektronów (21.01, 21.02). Energie to kilka eV. Przykład: żółty dublet sodu przy 589 nm (2,1 eV) w lampach ulicznych i płomieniu z solą.
- **Widmo emisyjne** to jasne linie gorącego gazu (lampy wyładowcze, mgławice, testy płomieniowe w chemii).
- **Widmo absorpcyjne** to ciemne linie w widmie ciągłym. Ten sam pierwiastek pochłania dokładnie te długości fal, które emituje (linie Fraunhofera w widmie Słońca).

**Lampa rentgenowska.** Elektrony przyspieszone napięciem $U$ (rzędu dziesiątek kV) uderzają w anodę. Widmo ma dwie części.

1. **Widmo ciągłe (promieniowanie hamowania).** Hamowany elektron emituje fotony o dowolnych energiach, ale najwyżej $eU$. Stąd ostra **granica krótkofalowa**:
   $$\lambda_{\min} = \frac{hc}{eU}.$$
   Dla 30 kV wynosi 41 pm i nie zależy od materiału anody.

2. **Widmo charakterystyczne.** Szybki elektron wybija elektron z **wewnętrznej** powłoki K ($n = 1$). Lukę zapełnia elektron z powłoki L ($n = 2$), co daje linię $K_\alpha$, albo z M, co daje $K_\beta$. Energie to keV, bo elektrony wewnętrzne są silnie związane.

**Prawo Moseleya (1913).** Elektron przeskakujący z L do K „widzi” jądro ekranowane przez pozostały elektron K, czyli ładunek ok. $(Z - 1)e$. Z modelu Bohra:

$$E_{K_\alpha} \approx 13{,}6\ \mathrm{eV}\cdot(Z - 1)^2\left(1 - \frac14\right) = 10{,}2\ \mathrm{eV}\cdot(Z - 1)^2.$$

$\sqrt{f}$ rośnie liniowo z $Z$. Moseley wykazał, że to liczba atomowa (ładunek jądra), a nie masa, porządkuje pierwiastki. Przewidział też brakujące pierwiastki (Z = 43, 61, 72, 75).

**Pochłanianie promieniowania rentgenowskiego** rośnie silnie z liczbą atomową (ok. $Z^4$) i maleje z energią. Kości (wapń, Z = 20) pochłaniają dużo więcej niż tkanki miękkie (C, H, O, N), co daje kontrast na zdjęciu.

## Wzory i założenia

| Wzór | Znaczenie | Kiedy obowiązuje |
|---|---|---|
| $\lambda_{\min} = hc/(eU)$ | granica widma ciągłego | lampa rentgenowska |
| $E_{K_\alpha} \approx 10{,}2\ \mathrm{eV}(Z - 1)^2$ | prawo Moseleya | linia $K_\alpha$ |
| $hc = 1240\ \mathrm{eV\cdot nm}$ | przeliczenie energii i długości fali | — |

## Przykład rozwiązany

**Zadanie.** Lampa z anodą miedzianą (Z = 29) pracuje przy 30 kV. Oblicz granicę krótkofalową widma ciągłego oraz energię i długość fali linii $K_\alpha$ z prawa Moseleya. Porównaj z wartością zmierzoną 0,154 nm.

$\lambda_{\min} = 1240\ \mathrm{eV\cdot nm}/30\,000\ \mathrm{eV} \approx 0{,}041\ \mathrm{nm}$.

$E_{K_\alpha} \approx 10{,}2\cdot28^2 \approx 8{,}0\ \mathrm{keV}$, $\lambda \approx 0{,}155\ \mathrm{nm}$. Wartość zmierzona to 8,05 keV i 0,154 nm, więc prosty model jest dokładny co do 1%.

### Wersja z rachunkiem różniczkowym i całkowym

**Zadanie.** Linia $K_\alpha$ nieznanego metalu ma długość fali 0,194 nm. Jaki to pierwiastek? Następnie wyznacz $Z$ z dopasowania prostej $\sqrt{E}$ od $Z$ dla znanych linii (kod niżej).

$E = 1240/0{,}194 \approx 6{,}39\ \mathrm{keV}$, $Z - 1 = \sqrt{6390/10{,}2} \approx 25$, więc $Z = 26$, czyli żelazo.

Z prawa Moseleya $\sqrt{E} = \sqrt{10{,}2\ \mathrm{eV}}(Z - 1)$: nachylenie wykresu $\sqrt{E}(Z)$ powinno wynosić $\sqrt{10{,}2\ \mathrm{eV}} \approx 3{,}19\ \sqrt{\mathrm{eV}}$, a przecięcie z osią $Z$ wypaść przy $Z = 1$ (stała ekranowania). Dopasowanie do zmierzonych linii od Fe do Ag daje ok. 3,28 i 1,6. Prosty model ekranowania jest tylko przybliżeniem, ale liniowość $\sqrt E$ od $Z$ jest bardzo dobra.

## Typowe pułapki

- **Granica krótkofalowa zależy od anody.** Zależy tylko od napięcia.
- **Linie charakterystyczne zależą od napięcia.** Zależą od materiału anody. Napięcie musi tylko przekroczyć energię jonizacji powłoki K.
- **$Z^2$ zamiast $(Z - 1)^2$.** Elektron L widzi jądro ekranowane przez drugi elektron K.
- **Promieniowanie rentgenowskie to przejścia elektronów zewnętrznych.** Linie charakterystyczne to przejścia na powłoki wewnętrzne, a widmo ciągłe to hamowanie.

## Doświadczenie / symulacja

**Test płomieniowy.** W płomieniu palnika gazowego posyp szczyptę soli kuchennej (żółty, Na), chlorku potasu (fioletowy, K) i węglanu litu lub chlorku strontu (czerwony). Obserwuj przez spektroskop z płyty CD (18.03). Widać pojedyncze linie zamiast ciągłego widma. Tylko pod opieką osoby dorosłej.

**Linie Fraunhofera.** Przez spektroskop o dobrej rozdzielczości (szczelina i siatka) skierowany na jasne niebo (nigdy wprost na Słońce) widać ciemne linie absorpcyjne, m.in. sodu przy 589 nm.

**Symulacja PhET:** *Światła neonowe i inne lampy wyładowcze* (*Neon Lights & Other Discharge Lamps*).

**Python:** widmo lampy rentgenowskiej (model Kramersa) z liniami charakterystycznymi i wykres Moseleya.

```python
import numpy as np
import matplotlib.pyplot as plt

hc = 1239.84                                        # eV·nm
U = 30e3
lam = np.linspace(0.02, 0.25, 1000)
E = hc/lam
I = np.clip(U - E, 0, None)/lam**2                  # model Kramersa: I(E) ∝ (eU − E), przeliczone na λ (|dE/dλ| ∝ 1/λ²)
I /= I.max()
for nazwa, l0 in [("Kα", 0.1542), ("Kβ", 0.1392)]:
    I += (0.8 if nazwa == "Kα" else 0.3)*np.exp(-((lam - l0)/0.001)**2)
print(f"λ_min przy 30 kV: {hc/U:.4f} nm")

pierwiastki = {"Fe": (26, 6.40), "Ni": (28, 7.48), "Cu": (29, 8.05), "Zn": (30, 8.64), "Mo": (42, 17.48), "Ag": (47, 22.16)}
Z = np.array([v[0] for v in pierwiastki.values()])
Ek = np.array([v[1] for v in pierwiastki.values()])*1e3
a, b = np.polyfit(Z, np.sqrt(Ek), 1)
print(f"Moseley: √E = {a:.3f}·(Z − {-b/a:.2f}), a² = {a**2:.2f} eV (teoria 10,2 eV)")
print(f"linia 0,194 nm → Z ≈ {np.sqrt(hc/0.194)/a - b/a:.1f}")
plt.plot(lam, I); plt.xlabel("λ [nm]"); plt.ylabel("natężenie (wzgl.)"); plt.title("lampa Cu, 30 kV"); plt.grid(True); plt.show()
```

## Zadania

### A. Poziom maturalny _(opcjonalnie — rozgrzewka)_

1. Jakie napięcie trzeba przyłożyć do lampy rentgenowskiej, żeby granica krótkofalowa wynosiła 0,0124 nm?

<details>
<summary>Odpowiedź</summary>

$U = 1240/0{,}0124\ \mathrm V = 100\ \mathrm{kV}$.
</details>

2. Dlaczego kości są dobrze widoczne na zdjęciu rentgenowskim?

<details>
<summary>Odpowiedź</summary>

Zawierają wapń i fosfor o większej liczbie atomowej niż tkanki miękkie. Pochłanianie rośnie bardzo silnie z $Z$.
</details>

### B. Poziom akademicki

1. Oblicz energię $K_\alpha$ dla molibdenu (Z = 42) z prawa Moseleya i porównaj z wartością zmierzoną 17,48 keV.

<details>
<summary>Odpowiedź</summary>

$10{,}2\cdot41^2 \approx 17{,}1\ \mathrm{keV}$, różnica ok. 2%.
</details>

2. Elektron o energii 30 keV traci energię w anodzie w wielu zderzeniach. Tylko ok. $10^{-9}ZU$ energii (U w woltach) zamienia się w promieniowanie. Oszacuj sprawność lampy wolframowej (Z = 74) przy 100 kV. Co dzieje się z resztą?

<details>
<summary>Odpowiedź</summary>

$10^{-9}\cdot74\cdot10^5 \approx 0{,}7\%$. Ponad 99% energii zamienia się w ciepło w anodzie, dlatego anody są masywne, chłodzone, a w tomografach obrotowe.
</details>

## Źródła

- OpenStax, *Fizyka dla szkół wyższych*, t. 3, rozdz. 8 — §8.5: widma atomowe i promieniowanie rentgenowskie.
- Halliday, Resnick, Walker, *Podstawy fizyki* — wyd. 2015: t. 5, §40.6; wyd. 1: t. 5, §41.10.
- Symulacja PhET *Światła neonowe i inne lampy wyładowcze*.
