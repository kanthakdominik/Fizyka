# 20.04 — Fale materii de Broglie'a i dualizm korpuskularno-falowy

> **Moduł:** [20 — Podstawy fizyki kwantowej](README.md) · **Poziom:** 🟢 matura R · **Status:** ✅ pełny
>
> **Czytaj:**
>
> - OpenStax, *Fizyka dla szkół wyższych*, t. 3, rozdz. 6: [§6.5–6.6](https://openstax.org/books/fizyka-dla-szk%C3%B3%C5%82-wy%C5%BCszych-tom-3/pages/6-5-fale-de-brogliea) · [wstęp do rozdziału](https://openstax.org/books/fizyka-dla-szk%C3%B3%C5%82-wy%C5%BCszych-tom-3/pages/6-wstep)
> - Halliday, Resnick, Walker, *Podstawy fizyki*, wyd. 2015, t. 5: §38.5 (s. 19)
> - Halliday, Resnick, Walker, *Podstawy fizyki*, wyd. 1 (2003), t. 5: [§39.5–39.6, s. 12](https://home.agh.edu.pl/~czapli/Resnick_5.pdf#page=28) — PDF z serwera AGH

← [Efekt Comptona](03-efekt-comptona.md) · [spis modułu](README.md) · [Funkcja falowa i zasada nieoznaczoności](05-funkcja-falowa-i-nieoznaczonosc.md) →

## Po co to jest

Skoro światło, uważane za falę, okazało się strumieniem cząstek, to może cząstki są falami? Louis de Broglie zaproponował to w 1924 r., a trzy lata później elektrony dały obraz dyfrakcyjny na krysztale (18.07). Falowa natura materii jest podstawą mikroskopu elektronowego (rozdzielczość tysiące razy lepsza niż optycznego), dyfrakcji neutronów w badaniach materiałów, a przede wszystkim całej mechaniki kwantowej i budowy atomu (20.06, 21).

## Teoria w pigułce

**Hipoteza de Broglie'a.** Każdej cząstce o pędzie $p$ odpowiada fala o długości

$$\lambda = \frac hp.$$

To ten sam związek co dla fotonu (20.03), ale odczytany w drugą stronę. Dla cząstki przyspieszonej napięciem $U$ (nierelatywistycznie):

$$\lambda = \frac{h}{\sqrt{2meU}}, \qquad \lambda_{\text{elektron}} \approx \frac{1{,}226\ \mathrm{nm}}{\sqrt{U[\mathrm V]}}.$$

**Dlaczego nie widzimy fal piłek?** Dla piłki o masie 0,1 kg i prędkości 10 m/s $\lambda \approx 7\cdot10^{-34}\ \mathrm m$, o 18 rzędów mniej niż rozmiar protonu. Żadna szczelina ani kryształ nie ujawni takiej fali. Dla elektronu o energii 100 eV $\lambda \approx 0{,}12\ \mathrm{nm}$, czyli jak odległości między atomami.

**Potwierdzenia doświadczalne:**
- **Davisson–Germer** (1927): wiązka elektronów odbita od kryształu niklu dała maksimum dokładnie pod kątem przewidzianym warunkiem Bragga (18.07).
- **G. P. Thomson** (1927): elektrony przechodzące przez cienką folię dały pierścienie dyfrakcyjne jak promieniowanie rentgenowskie.
- **Doświadczenie dwuszczelinowe z elektronami** (Jönsson 1961, Tonomura 1989): pojedyncze elektrony, wysyłane jeden po drugim, tworzą stopniowo obraz interferencyjny. Każdy elektron „przechodzi przez obie szczeliny” jako fala, a rejestrowany jest jako cząstka w jednym punkcie (20.05).
- Interferencję zaobserwowano też dla neutronów, atomów, a nawet cząsteczek fulerenu C₆₀ (Zeilinger, 1999).

**Dualizm korpuskularno-falowy.** Zarówno światło, jak i materia przejawiają cechy falowe (interferencja, dyfrakcja) i korpuskularne (rejestracja w punkcie, zderzenia). To, które się ujawniają, zależy od doświadczenia.

**Mikroskop elektronowy.** Elektrony przyspieszone napięciem 100 kV mają długość fali ok. 3,7 pm (z poprawką relatywistyczną, 19.05). Rozdzielczość, ograniczona dyfrakcją ($\sim\lambda$), jest w praktyce ograniczona wadami soczewek magnetycznych do ok. 0,05–0,1 nm. Pozwala to oglądać pojedyncze kolumny atomów.

## Wzory i założenia

| Wzór | Znaczenie | Kiedy obowiązuje |
|---|---|---|
| $\lambda = h/p$ | długość fali de Broglie'a | każda cząstka |
| $\lambda = h/\sqrt{2mE_k}$ | z energii kinetycznej | $E_k \ll mc^2$ |
| $\lambda = h/\sqrt{2meU}$ | cząstka przyspieszona napięciem | j.w. |
| $pc = \sqrt{E_k^2 + 2E_kmc^2}$ | pęd relatywistyczny | dowolne $E_k$ |

## Przykład rozwiązany

**Zadanie.** Oblicz długość fali de Broglie'a: (a) elektronu przyspieszonego napięciem 54 V (doświadczenie Davissona–Germera), (b) neutronu termicznego o energii 0,025 eV, (c) elektronu w mikroskopie przy 100 kV, (d) piłki tenisowej (0,06 kg, 50 m/s).

(a) $\lambda = 1{,}226/\sqrt{54} \approx 0{,}167\ \mathrm{nm}$.

(b) $\lambda = h/\sqrt{2m_nE} \approx 0{,}18\ \mathrm{nm}$. Neutrony termiczne nadają się do dyfrakcji na kryształach, a do tego „widzą” lekkie atomy i momenty magnetyczne lepiej niż promienie rentgenowskie.

(c) Nierelatywistycznie 3,88 pm, relatywistycznie $pc = \sqrt{0{,}1^2 + 2\cdot0{,}1\cdot0{,}511}\ \mathrm{MeV} \approx 0{,}335\ \mathrm{MeV}$, czyli $\lambda = hc/(pc) \approx 3{,}70\ \mathrm{pm}$.

(d) $\lambda = h/(mv) \approx 2{,}2\cdot10^{-34}\ \mathrm m$.

## Typowe pułapki

- **$\lambda = h/(mv)$ dla fotonu.** Foton nie ma masy. Dla niego $\lambda = h/p = hc/E$.
- **$\lambda = hc/E$ dla elektronu.** Ten wzór jest tylko dla fotonów (cząstek bezmasowych). Dla elektronu $\lambda = h/p$, a $p = \sqrt{2mE_k}$.
- **Fala materii to drgania czegoś materialnego.** To fala amplitudy prawdopodobieństwa (20.05), a nie drgania ośrodka.
- **Pomijanie poprawki relatywistycznej.** Dla elektronów powyżej ok. 50 keV trzeba ją uwzględniać.

## Doświadczenie / symulacja

**Dyfrakcja elektronów w pracowni.** Lampa do dyfrakcji elektronów (szklana bańka z folią grafitową i ekranem fluorescencyjnym) jest w wielu pracowniach szkolnych i uczelnianych. Zmierz średnice pierścieni dla kilku napięć i sprawdź, że $D \propto 1/\sqrt U$, czyli $\propto\lambda$.

**Symulacja PhET:** *Interferencja kwantowa* (*Quantum Wave Interference*) — pojedyncze cząstki budują obraz interferencyjny ([phet.colorado.edu/pl](https://phet.colorado.edu/pl/)).

**Python:** długość fali de Broglie'a dla różnych cząstek i energii, z poprawką relatywistyczną.

```python
import numpy as np
import matplotlib.pyplot as plt

h, c, e = 6.62607015e-34, 2.99792458e8, 1.602176634e-19
masy = {"elektron": 9.1093837e-31, "neutron": 1.67492750e-27, "proton": 1.67262192e-27}

def lam(m, Ek_eV, rel=True):
    Ek = Ek_eV*e
    p = np.sqrt(Ek**2 + 2*Ek*m*c**2)/c if rel else np.sqrt(2*m*Ek)
    return h/p

print(f"elektron 54 eV: {lam(masy['elektron'], 54)*1e9:.3f} nm")
print(f"neutron 0,025 eV: {lam(masy['neutron'], 0.025)*1e9:.3f} nm")
print(f"elektron 100 keV: {lam(masy['elektron'], 1e5)*1e12:.2f} pm (bez poprawki {lam(masy['elektron'], 1e5, False)*1e12:.2f} pm)")
print(f"piłka 0,06 kg, 50 m/s: {h/(0.06*50):.1e} m")
E = np.logspace(-2, 6, 300)
for nazwa, m in masy.items():
    plt.loglog(E, [lam(m, x)*1e9 for x in E], label=nazwa)
plt.axhline(0.3, ls="--", color="gray", label="odległość między atomami")
plt.xlabel("E_k [eV]"); plt.ylabel("λ [nm]"); plt.legend(); plt.grid(True, which="both"); plt.show()
```

## Zadania

### A. Poziom maturalny

1. Jakim napięciem trzeba przyspieszyć elektron, żeby jego długość fali wynosiła 0,1 nm?

<details>
<summary>Odpowiedź</summary>

$U = (1{,}226/0{,}1)^2 \approx 150\ \mathrm V$.
</details>

2. Proton i elektron mają tę samą energię kinetyczną. Który ma krótszą długość fali i ile razy?

<details>
<summary>Odpowiedź</summary>

Proton, $\sqrt{m_p/m_e} \approx 43$ razy krótszą.
</details>

3. Proton i elektron mają tę samą prędkość. Porównaj długości fal.

<details>
<summary>Odpowiedź</summary>

$\lambda \propto 1/m$, więc fala protonu jest 1836 razy krótsza.
</details>

4. Dlaczego nie obserwujemy dyfrakcji ludzi przechodzących przez drzwi?

<details>
<summary>Odpowiedź</summary>

Długość fali człowieka (70 kg, 1 m/s) to ok. $10^{-35}\ \mathrm m$, nieporównanie mniej niż szerokość drzwi.
</details>

### B. Poziom akademicki _(opcjonalnie — rozszerzenie z rachunkiem)_

1. Wiązka elektronów o energii 50 eV pada na dwie szczeliny odległe o 1 μm. Oblicz odstęp prążków na ekranie odległym o 1 m. Czy to mierzalne?

<details>
<summary>Odpowiedź</summary>

$\lambda \approx 0{,}173\ \mathrm{nm}$, $\Delta y = \lambda L/d \approx 0{,}17\ \mathrm{mm}$. Mierzalne, ale wymaga bardzo precyzyjnych szczelin i powiększenia obrazu elektronowymi soczewkami, jak u Jönssona.
</details>

2. Pokaż, że dla cząstki relatywistycznej $\lambda = \dfrac{hc}{\sqrt{E_k^2 + 2E_kmc^2}}$, i znajdź energię, przy której poprawka relatywistyczna zmienia $\lambda$ elektronu o 1%.

<details>
<summary>Odpowiedź</summary>

$pc = \sqrt{E^2 - m^2c^4}$ z $E = E_k + mc^2$. Stosunek $\lambda_{\text{rel}}/\lambda_{\text{klas}} = (1 + E_k/(2mc^2))^{-1/2} \approx 1 - E_k/(4mc^2)$. 1% przy $E_k \approx 0{,}04mc^2 \approx 20\ \mathrm{keV}$.
</details>

## Źródła

- OpenStax, *Fizyka dla szkół wyższych*, t. 3, rozdz. 6 — §6.5 (fale materii de Broglie'a) i §6.6 (dualizm korpuskularno-falowy).
- Halliday, Resnick, Walker, *Podstawy fizyki* — wyd. 2015: t. 5, §38.5; wyd. 1: t. 5, §39.5–39.6.
- Symulacja PhET *Interferencja kwantowa*.
