# 16.04 — Widmo fal elektromagnetycznych

> **Moduł:** [16 — Równania Maxwella i fale elektromagnetyczne](README.md) · **Poziom:** 🟢 matura R · **Status:** ✅ pełny
>
> **Czytaj:**
>
> - OpenStax, *Fizyka dla szkół wyższych*, t. 2, rozdz. 16: [§16.5](https://openstax.org/books/fizyka-dla-szk%C3%B3%C5%82-wy%C5%BCszych-tom-2/pages/16-5-widmo-promieniowania-elektromagnetycznego) · [wstęp do rozdziału](https://openstax.org/books/fizyka-dla-szk%C3%B3%C5%82-wy%C5%BCszych-tom-2/pages/16-wstep)
> - Halliday, Resnick, Walker, *Podstawy fizyki*, wyd. 2015, t. 4: §33.1 (s. 1)
> - Halliday, Resnick, Walker, *Podstawy fizyki*, wyd. 1 (2003), t. 4: [§34.1, s. 2](https://home.agh.edu.pl/~czapli/Resnick_4.pdf#page=17) — PDF z serwera AGH

← [Energia, wektor Poyntinga i ciśnienie promieniowania](03-energia-i-ped-fali.md) · [spis modułu](README.md) · (koniec modułu) →

## Po co to jest

Radio, mikrofalówka, pilot do telewizora, światło, opalanie, prześwietlenie i promieniowanie z jąder atomowych to ta sama fala elektromagnetyczna, tylko o różnej długości. Znajomość widma pozwala zrozumieć, dlaczego Wi-Fi przechodzi przez ściany słabiej niż radio UKF, dlaczego ultrafiolet szkodzi skórze, a fale radiowe nie, jak działa termowizja, dlaczego niebo jest niebieskie i co widzą teleskopy w różnych zakresach.

## Teoria w pigułce

Wszystkie fale elektromagnetyczne biegną w próżni z prędkością $c$ i spełniają $c = \lambda f$. Różnią się częstotliwością, a więc sposobem powstawania, oddziaływaniem z materią i zastosowaniami. Energia pojedynczej porcji (fotonu) wynosi $E = hf$ (20). Od niej zależy, czy promieniowanie może zrywać wiązania chemiczne i jonizować atomy (powyżej ok. 10 eV, czyli od dalekiego ultrafioletu w górę).

| Zakres | Długość fali | Częstotliwość | Źródła | Zastosowania i zjawiska |
|---|---|---|---|---|
| fale radiowe | > 1 m | < 300 MHz | drgające prądy w antenach | radio AM/FM, łączność, radioastronomia |
| mikrofale | 1 mm – 1 m | 300 MHz – 300 GHz | magnetrony, tranzystory, anteny | telefonia, Wi-Fi, GPS, radar, mikrofalówka, promieniowanie reliktowe (24) |
| podczerwień | 750 nm – 1 mm | 300 GHz – 400 THz | drgania cząsteczek, ciała ciepłe | termowizja, piloty, światłowody (1,3–1,55 μm), efekt cieplarniany |
| światło widzialne | 380–750 nm | 400–790 THz | przejścia elektronów w atomach, ciała gorące | wzrok, fotosynteza |
| ultrafiolet | 10–380 nm | 790 THz – 30 PHz | Słońce, lampy wyładowcze | opalanie, sterylizacja, witamina D, oparzenia, nowotwory skóry |
| promieniowanie rentgenowskie | 0,01–10 nm | 30 PHz – 30 EHz | hamowanie elektronów, przejścia wewnętrzne | diagnostyka medyczna, krystalografia (18) |
| promieniowanie gamma | < 0,01 nm | > 30 EHz | przemiany jądrowe | radioterapia, sterylizacja, astrofizyka (22) |

Granice między zakresami są umowne i zachodzą na siebie. Nazwę często wybiera się według źródła promieniowania, a nie samej długości fali.

**Oddziaływanie z materią zależy od długości fali.**
- Atmosfera przepuszcza światło widzialne, część podczerwieni i fale radiowe (okna atmosferyczne). Pochłania ultrafiolet (ozon) i promieniowanie rentgenowskie, dlatego teleskopy rentgenowskie umieszcza się na orbicie.
- Fale dłuższe od przeszkody uginają się wokół niej (10.04), więc fale długie docierają za wzgórza, a mikrofale wymagają widoczności anten.
- Woda pochłania mikrofale, i to coraz silniej w stronę kilkudziesięciu GHz. Kuchenka używa 2,45 GHz, bo przy tej częstotliwości fala wnika w jedzenie na kilka centymetrów. Z tego samego powodu ludzie i mokre ściany tłumią Wi-Fi.

## Wzory i założenia

| Wzór | Znaczenie | Kiedy obowiązuje |
|---|---|---|
| $c = \lambda f$ | związek długości fali i częstotliwości | próżnia |
| $E = hf = hc/\lambda$ | energia fotonu (20) | $h = 6{,}63\cdot10^{-34}\ \mathrm{J\cdot s}$ |
| $hc \approx 1240\ \mathrm{eV\cdot nm}$ | wygodna stała | $E[\mathrm{eV}] \approx 1240/\lambda[\mathrm{nm}]$ |

## Przykład rozwiązany

**Zadanie.** Oblicz długość fali i energię fotonu dla: radia UKF (100 MHz), Wi-Fi (2,4 GHz), światła zielonego (550 nm) i promieniowania rentgenowskiego (0,1 nm). Które może zrywać wiązania chemiczne (kilka eV)?

| Fala | $\lambda$ | $E$ fotonu |
|---|---|---|
| UKF 100 MHz | 3 m | $4\cdot10^{-7}\ \mathrm{eV}$ |
| Wi-Fi 2,4 GHz | 12,5 cm | $10^{-5}\ \mathrm{eV}$ |
| zielone 550 nm | 550 nm | 2,25 eV |
| rentgen 0,1 nm | 0,1 nm | 12 400 eV |

Wiązania chemiczne zrywają dopiero fotony z ultrafioletu i krótszych fal. Światło widzialne wywołuje reakcje fotochemiczne w oku i liściach. Fotony radiowe i mikrofalowe są milion razy za słabe. Mikrofale mogą jedynie grzać, wprawiając cząsteczki w ruch.

## Typowe pułapki

- **Fale radiowe i światło to różne zjawiska.** To ta sama fala elektromagnetyczna, różniąca się tylko częstotliwością.
- **Wyższa moc nadajnika = jonizacja.** O jonizacji decyduje energia pojedynczego fotonu ($hf$), a nie moc. Silny nadajnik radiowy może grzać, ale nie jonizuje.
- **Promieniowanie podczerwone to „ciepło”.** Podczerwień to promieniowanie, które grzeje po pochłonięciu, tak jak każde inne. Ciało gorące emituje też światło widzialne.
- **Pomylenie GHz z nm.** Przeliczaj przez $\lambda = c/f$ i pamiętaj o przedrostkach.

## Doświadczenie / symulacja

**Pilot w aparacie telefonu.** Skieruj pilot od telewizora na kamerę telefonu i naciśnij przycisk. Na ekranie widać migającą diodę, której oko nie widzi. Matryca rejestruje bliską podczerwień (ok. 940 nm). Uwaga: główne aparaty niektórych telefonów mają filtr podczerwieni, wtedy spróbuj przedniej kamery.

**Ekranowanie.** Telefon włożony do mikrofalówki (wyłączonej!) zwykle traci zasięg lub Wi-Fi, bo siatka w drzwiach ma oczka dużo mniejsze od długości fali.

**Symulacje PhET:** *Efekt cieplarniany* (*Greenhouse Effect*) i *Mikrofale* (*Microwaves*) — [phet.colorado.edu/pl](https://phet.colorado.edu/pl/).

**Python:** długości fal i energie fotonów dla popularnych źródeł.

```python
import numpy as np

c, h, eV = 299792458.0, 6.62607015e-34, 1.602176634e-19
zrodla = {"radio AM 1 MHz": 1e6, "radio FM 100 MHz": 100e6, "GPS L1": 1575.42e6,
          "Wi-Fi 2,4 GHz": 2.4e9, "5G 3,5 GHz": 3.5e9, "pilot IR 940 nm": c/940e-9,
          "zielone 550 nm": c/550e-9, "UV-B 300 nm": c/300e-9, "rentgen 0,1 nm": c/0.1e-9}
for nazwa, f in zrodla.items():
    lam = c/f
    E = h*f/eV
    print(f"{nazwa:18s} λ = {lam:10.3e} m, E fotonu = {E:10.3e} eV {'(jonizuje)' if E > 10 else ''}")
print(f"hc = {h*c/eV*1e9:.1f} eV·nm")
```

## Zadania

### A. Poziom maturalny

1. Uporządkuj według rosnącej długości fali: promieniowanie rentgenowskie, mikrofale, światło czerwone, ultrafiolet, fale radiowe, podczerwień.

<details>
<summary>Odpowiedź</summary>

Rentgenowskie, ultrafiolet, światło czerwone, podczerwień, mikrofale, fale radiowe.
</details>

2. Oblicz częstotliwość światła czerwonego (700 nm) i fioletowego (400 nm).

<details>
<summary>Odpowiedź</summary>

$4{,}3\cdot10^{14}\ \mathrm{Hz}$ i $7{,}5\cdot10^{14}\ \mathrm{Hz}$.
</details>

3. Dlaczego teleskopy rentgenowskie i ultrafioletowe umieszcza się na orbicie, a radioteleskopy na Ziemi?

<details>
<summary>Odpowiedź</summary>

Atmosfera pochłania promieniowanie rentgenowskie i większość ultrafioletu, a dla fal radiowych jest przezroczysta.
</details>

4. Ciało człowieka emituje najwięcej promieniowania przy ok. 10 μm (11.03). W jakim to zakresie? Jaka to częstotliwość?

<details>
<summary>Odpowiedź</summary>

Podczerwień (daleka), $f = 3\cdot10^{13}\ \mathrm{Hz}$.
</details>

### B. Poziom akademicki _(opcjonalnie — rozszerzenie z rachunkiem)_

1. Oblicz energię fotonu w eV dla promieniowania UV-B (300 nm) i porównaj z energią wiązania C–C (ok. 3,6 eV). Dlaczego UV-B uszkadza DNA, a światło czerwone nie?

<details>
<summary>Odpowiedź</summary>

$E = 1240/300 \approx 4{,}1\ \mathrm{eV}$, więcej niż energia wiązania. Czerwone (700 nm): 1,8 eV, za mało, niezależnie od natężenia.
</details>

2. Ile fotonów na sekundę emituje nadajnik radiowy o mocy 10 kW na częstotliwości 100 MHz, a ile wskaźnik laserowy 1 mW (650 nm)?

<details>
<summary>Odpowiedź</summary>

Nadajnik: $N = P/(hf) \approx 1{,}5\cdot10^{29}\ \mathrm{s^{-1}}$. Laser: $\approx 3{,}3\cdot10^{15}\ \mathrm{s^{-1}}$. Dla fal radiowych ziarnistość fotonów jest całkowicie niewidoczna.
</details>

## Źródła

- OpenStax, *Fizyka dla szkół wyższych*, t. 2, rozdz. 16 — §16.5: widmo promieniowania elektromagnetycznego.
- Halliday, Resnick, Walker, *Podstawy fizyki* — wyd. 2015: t. 4, §33.1; wyd. 1: t. 4, §34.1.
- Symulacje PhET *Efekt cieplarniany* i *Mikrofale*.
