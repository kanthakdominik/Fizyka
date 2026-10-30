# 12.06 — Kondensatory: pojemność, łączenie, energia

> **Moduł:** [12 — Elektrostatyka](README.md) · **Poziom:** 🟢 matura R · **Status:** ✅ pełny
>
> **Czytaj:**
>
> - OpenStax, *Fizyka dla szkół wyższych*, t. 2, rozdz. 8: [§8.1–8.3](https://openstax.org/books/fizyka-dla-szk%C3%B3%C5%82-wy%C5%BCszych-tom-2/pages/8-1-kondensatory-i-pojemnosc-elektryczna) · [wstęp do rozdziału](https://openstax.org/books/fizyka-dla-szk%C3%B3%C5%82-wy%C5%BCszych-tom-2/pages/8-wstep)
> - Halliday, Resnick, Walker, *Podstawy fizyki*, wyd. 2015, t. 3: §25.1–25.4 (s. 143)
> - Halliday, Resnick, Walker, *Podstawy fizyki*, wyd. 1 (2003), t. 3: [§26.1–26.5, s. 102](https://home.agh.edu.pl/~czapli/Resnick_3.pdf#page=112) — PDF z serwera AGH

← [Potencjał, energia potencjalna i związek E z V](05-potencjal.md) · [spis modułu](README.md) · [Dielektryki w polu elektrycznym](07-dielektryki.md) →

## Po co to jest

Kondensator gromadzi ładunek i energię w polu elektrycznym. Jest w każdym urządzeniu elektronicznym: wygładza napięcie w zasilaczach, filtruje sygnały, odmierza czas (13.06) i dostraja radio (15). Oddaje energię bardzo szybko, więc działa w lampach błyskowych, defibrylatorach i laserach impulsowych. Superkondensatory wspierają akumulatory w autobusach i odzyskują energię hamowania. Na zmianie pojemności opierają się ekrany dotykowe i mikrofony pojemnościowe.

## Teoria w pigułce

**Pojemność.** Dwa przewodniki (okładki) z ładunkami $+Q$ i $-Q$ mają między sobą napięcie $U$ proporcjonalne do $Q$:

$$C = \frac QU, \qquad [C] = \mathrm F = \mathrm{C/V}.$$

Farad to ogromna jednostka. Typowe kondensatory mają pikofarady do milifaradów. Pojemność zależy tylko od geometrii i materiału między okładkami, a nie od ładunku.

**Kondensator płaski** (okładki o polu $A$ w odległości $d \ll \sqrt A$): pole między okładkami $E = \sigma/\varepsilon_0$ (12.03), napięcie $U = Ed$, więc

$$C = \frac{\varepsilon_0A}{d}.$$

**Łączenie kondensatorów:**
- **Równoległe**: wspólne napięcie, ładunki się sumują: $C = C_1 + C_2 + \dots$
- **Szeregowe**: wspólny ładunek, napięcia się sumują: $\dfrac1C = \dfrac1{C_1} + \dfrac1{C_2} + \dots$

Zasady są odwrotne niż dla oporników (13.04).

**Energia kondensatora.** Przenoszenie kolejnych porcji $dq$ przy rosnącym napięciu $u = q/C$ wymaga pracy $\int_0^Qu\,dq$:

$$W = \frac{Q^2}{2C} = \frac12CU^2 = \frac12QU.$$

Energia jest zmagazynowana w polu. Jej **gęstość** wynosi

$$w = \frac12\varepsilon_0E^2.$$

Ten wzór obowiązuje dla każdego pola elektrycznego, nie tylko w kondensatorze.

## Wzory i założenia

| Wzór | Znaczenie | Kiedy obowiązuje |
|---|---|---|
| $C = Q/U$ | definicja pojemności | — |
| $C = \varepsilon_0A/d$ | kondensator płaski | $d \ll$ rozmiar okładek, próżnia |
| $C = C_1 + C_2$ | łączenie równoległe | — |
| $1/C = 1/C_1 + 1/C_2$ | łączenie szeregowe | — |
| $W = \tfrac12CU^2 = Q^2/(2C)$ | energia kondensatora | — |
| $w = \tfrac12\varepsilon_0E^2$ | gęstość energii pola | próżnia |

## Przykład rozwiązany

**Zadanie 1.** Kondensator płaski ma kwadratowe okładki o boku 10 cm odległe o 1 mm. Oblicz pojemność, ładunek i energię przy napięciu 100 V.

$C = 8{,}85\cdot10^{-12}\cdot0{,}01/0{,}001 \approx 88{,}5\ \mathrm{pF}$. $Q = CU \approx 8{,}9\ \mathrm{nC}$. $W = \tfrac12CU^2 \approx 0{,}44\ \mu\mathrm J$. Zwykły kondensator płaski bez dielektryka ma bardzo małą pojemność. Praktyczne kondensatory mają cieniutki dielektryk i zwiniętą folię (12.07).

**Zadanie 2.** Kondensator 2 μF połączono szeregowo z równoległym układem 3 μF i 6 μF. Całość podłączono do 12 V. Oblicz pojemność zastępczą i ładunek na każdym kondensatorze.

Równolegle: $3 + 6 = 9\ \mu\mathrm F$. Szeregowo z 2 μF: $C = \dfrac{2\cdot9}{11} \approx 1{,}64\ \mu\mathrm F$.

Ładunek na 2 μF i na całym układzie równoległym: $Q = 1{,}64\cdot12 \approx 19{,}6\ \mu\mathrm C$. Napięcie na układzie równoległym: $19{,}6/9 \approx 2{,}18\ \mathrm V$, więc $Q_3 \approx 6{,}5\ \mu\mathrm C$ i $Q_6 \approx 13{,}1\ \mu\mathrm C$. Na 2 μF jest $9{,}82\ \mathrm V$. Suma napięć wynosi 12 V.

## Typowe pułapki

- **Pojemność rośnie z ładunkiem.** $C$ zależy tylko od budowy. Większy ładunek oznacza większe napięcie.
- **Łączenie jak oporniki.** Dla kondensatorów równolegle się dodaje, a szeregowo odwrotności.
- **Energia $QU$.** Energia to $\tfrac12QU$. Drugą połowę pracy baterii przy ładowaniu traci się w oporze obwodu (13.06).
- **Ładunek kondensatora = $2Q$.** „Ładunek kondensatora” to $Q$ na jednej okładce. Całkowity ładunek obu okładek wynosi zero.
- **Odłączony czy podłączony do źródła.** Odłączony kondensator ma stały ładunek, a podłączony stałe napięcie. Przy rozsuwaniu okładek czy wkładaniu dielektryka (12.07) daje to różne wyniki.

## Doświadczenie / symulacja

**Kondensator z folii.** Dwa arkusze folii aluminiowej przełożone folią spożywczą lub kartką i dociśnięte książkami to kondensator rzędu nanofaradów. Zmierz pojemność miernikiem uniwersalnym z zakresem pojemności. Sprawdź, jak zależy od pola nakładających się arkuszy i od liczby przekładek.

**Symulacja PhET:** *Laboratorium kondensatora* (*Capacitor Lab: Basics*) — zmieniaj pole i odległość okładek, obserwuj ładunek, energię i pole ([phet.colorado.edu/pl](https://phet.colorado.edu/pl/)).

**Python:** pojemność zastępcza dowolnej sieci szeregowo-równoległej i energia.

```python
eps0 = 8.854e-12

def szeregowo(*C):
    return 1/sum(1/c for c in C)

def rownolegle(*C):
    return sum(C)

A, d, U = 0.1*0.1, 1e-3, 100
C = eps0*A/d
print(f"płaski: C = {C*1e12:.1f} pF, Q = {C*U*1e9:.2f} nC, W = {0.5*C*U**2*1e6:.3f} µJ")
print(f"gęstość energii pola: {0.5*eps0*(U/d)**2*A*d*1e6:.3f} µJ (to samo)")

Cz = szeregowo(2e-6, rownolegle(3e-6, 6e-6))
Q = Cz*12
print(f"sieć: C = {Cz*1e6:.3f} µF, Q = {Q*1e6:.2f} µC, U(2 µF) = {Q/2e-6:.2f} V, U(3||6) = {Q/9e-6:.2f} V")
print(f"superkondensator 3000 F / 2,7 V: W = {0.5*3000*2.7**2/1e3:.1f} kJ = {0.5*3000*2.7**2/3600:.2f} Wh")
```

## Zadania

### A. Poziom maturalny

1. Trzy kondensatory 2 μF, 3 μF i 6 μF połączono szeregowo, a potem równolegle. Oblicz pojemność zastępczą w obu przypadkach.

<details>
<summary>Odpowiedź</summary>

Szeregowo 1 μF, równolegle 11 μF.
</details>

2. Defibrylator ma dostarczyć 200 J przy napięciu 5 kV. Jaka musi być pojemność jego kondensatora?

<details>
<summary>Odpowiedź</summary>

$C = 2W/U^2 = 16\ \mu\mathrm F$.
</details>

3. Superkondensator 3000 F ma napięcie znamionowe 2,7 V. Ile energii gromadzi? Porównaj z akumulatorem telefonu (ok. 15 Wh).

<details>
<summary>Odpowiedź</summary>

$W \approx 10{,}9\ \mathrm{kJ} \approx 3\ \mathrm{Wh}$, ok. pięć razy mniej niż akumulator telefonu, ale może je oddać w kilka sekund.
</details>

4. Odległość okładek naładowanego i **odłączonego** kondensatora płaskiego zwiększono dwukrotnie. Jak zmieniły się pojemność, ładunek, napięcie i energia? Skąd wziął się przyrost energii?

<details>
<summary>Odpowiedź</summary>

$C$ maleje 2 razy, $Q$ bez zmian, $U$ i $W$ rosną 2 razy. Przyrost energii to praca wykonana przy rozsuwaniu przyciągających się okładek.
</details>

### B. Poziom akademicki _(opcjonalnie — rozszerzenie z rachunkiem)_

1. Wyprowadź pojemność kondensatora walcowego (kabla koncentrycznego) o promieniach $a < b$ i długości $L$. Oblicz ją na metr dla $a = 0{,}5\ \mathrm{mm}$, $b = 2\ \mathrm{mm}$.

<details>
<summary>Odpowiedź</summary>

$E = \lambda/(2\pi\varepsilon_0r)$, $U = \displaystyle\int_a^bE\,dr = \frac{\lambda}{2\pi\varepsilon_0}\ln\frac ba$, więc $C = \dfrac{2\pi\varepsilon_0L}{\ln(b/a)} \approx 40\ \mathrm{pF/m}$. Z dielektrykiem polietylenowym ($\varepsilon_r \approx 2{,}3$) ok. 90 pF/m, jak w typowych kablach.
</details>

2. Oblicz pojemność Ziemi jako przewodzącej kuli o promieniu 6371 km.

<details>
<summary>Odpowiedź</summary>

$C = 4\pi\varepsilon_0R \approx 710\ \mu\mathrm F$. Cała planeta ma pojemność mniejszą niż jeden typowy kondensator elektrolityczny.
</details>

3. Kondensator 10 μF naładowany do 100 V połączono z identycznym, nienaładowanym. Oblicz energię przed połączeniem i po nim. Gdzie podziała się różnica?

<details>
<summary>Odpowiedź</summary>

Przed: 0,05 J. Po: napięcie 50 V na 20 μF, czyli 0,025 J. Połowa energii zamieniła się w ciepło w przewodach i w promieniowanie, niezależnie od wartości oporu.
</details>

4. Pokaż, że okładki kondensatora płaskiego przyciągają się siłą $F = \dfrac{Q^2}{2\varepsilon_0A}$. Skorzystaj z $F = -dW/dx$ przy stałym ładunku.

<details>
<summary>Odpowiedź</summary>

$W = \dfrac{Q^2x}{2\varepsilon_0A}$, więc $\lvert dW/dx\rvert = \dfrac{Q^2}{2\varepsilon_0A}$. Nie $QE$, bo każda okładka jest w polu drugiej, czyli $E/2$.
</details>

## Źródła

- OpenStax, *Fizyka dla szkół wyższych*, t. 2, rozdz. 8 — §8.1 (kondensatory i pojemność), §8.2 (łączenie kondensatorów), §8.3 (energia zgromadzona w kondensatorze).
- Halliday, Resnick, Walker, *Podstawy fizyki* — wyd. 2015: t. 3, §25.1–25.4; wyd. 1: t. 3, §26.1–26.5.
- Symulacja PhET *Laboratorium kondensatora*.
