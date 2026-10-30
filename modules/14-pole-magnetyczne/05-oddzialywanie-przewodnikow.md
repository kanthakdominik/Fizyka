# 14.05 — Oddziaływanie przewodników z prądem

> **Moduł:** [14 — Pole magnetyczne](README.md) · **Poziom:** 🟢 matura R · **Status:** ✅ pełny
>
> **Czytaj:**
>
> - OpenStax, *Fizyka dla szkół wyższych*, t. 2, rozdz. 12: [§12.3](https://openstax.org/books/fizyka-dla-szk%C3%B3%C5%82-wy%C5%BCszych-tom-2/pages/12-3-oddzialywanie-magnetyczne-dwoch-rownoleglych-przewodow-z-pradem) · [wstęp do rozdziału](https://openstax.org/books/fizyka-dla-szk%C3%B3%C5%82-wy%C5%BCszych-tom-2/pages/12-wstep)
> - Halliday, Resnick, Walker, *Podstawy fizyki*, wyd. 2015, t. 3: §29.2 (s. 301)
> - Halliday, Resnick, Walker, *Podstawy fizyki*, wyd. 1 (2003), t. 3: §30.2, s. 226 (skan t. 3 na serwerze AGH kończy się na s. 127 — dalsze strony tylko w wydaniu papierowym)

← [Prawo Biota–Savarta](04-prawo-biota-savarta.md) · [spis modułu](README.md) · [Prawo Ampère'a, solenoid i toroid](06-prawo-ampera.md) →

## Po co to jest

Dwa przewody z prądem przyciągają się albo odpychają. Przez ponad pół wieku (1948–2019) to oddziaływanie definiowało amper. W technice ma poważne skutki: przy zwarciu w rozdzielni prądy rzędu dziesiątek kiloamperów wyginają szyny zbiorcze i rozrywają uzwojenia transformatorów, więc konstrukcje projektuje się na te siły. To samo zjawisko ściska plazmę w przewodzie (efekt „pinch”) i jest podstawą działania działa szynowego.

## Teoria w pigułce

Przewód 1 z prądem $I_1$ wytwarza w odległości $d$ pole $B_1 = \dfrac{\mu_0I_1}{2\pi d}$ (14.04). Przewód 2 z prądem $I_2$ jest w tym polu, więc działa na niego siła $F = B_1I_2L$ (14.02). Na jednostkę długości:

$$\frac FL = \frac{\mu_0I_1I_2}{2\pi d}.$$

- Prądy **zgodne** się **przyciągają**, a prądy **przeciwne** się **odpychają**. To odwrotnie niż dla ładunków elektrycznych.
- Siły spełniają III zasadę dynamiki: przewód 1 działa na 2 tak samo jak 2 na 1.

**Dawna definicja ampera (1948–2019).** 1 A to taki prąd, który płynąc w dwóch nieskończenie długich, cienkich, równoległych przewodach odległych o 1 m w próżni, wywołuje między nimi siłę $2\cdot10^{-7}\ \mathrm N$ na każdy metr długości. Z niej wynikała dokładna wartość $\mu_0 = 4\pi\cdot10^{-7}$. Od 2019 r. amper definiuje się przez ustaloną wartość ładunku elementarnego (01.01).

**Efekt „pinch”.** W grubym przewodzie lub kolumnie plazmy wszystkie „nitki” prądu płyną zgodnie, więc się przyciągają i ściskają przewodnik. W plazmie wykorzystuje się to do jej utrzymania i podgrzania. W metalu przy ogromnych impulsach prądu może to zgnieść rurkę.

**Przewody w kablu.** W przewodzie zasilającym prądy w żyłach płyną w przeciwnych kierunkach, więc żyły się odpychają, ale ich pola prawie się znoszą na zewnątrz kabla.

## Wzory i założenia

| Wzór | Znaczenie | Kiedy obowiązuje |
|---|---|---|
| $F/L = \mu_0I_1I_2/(2\pi d)$ | siła między przewodami równoległymi | długie, cienkie, $d \ll L$ |
| zgodne prądy — przyciąganie | kierunek siły | — |
| $\mu_0/(2\pi) = 2\cdot10^{-7}\ \mathrm{T\cdot m/A}$ | wygodna stała | — |

## Przykład rozwiązany

**Zadanie 1.** Oblicz siłę na metr długości między dwoma przewodami z prądem 1 A odległymi o 1 m oraz między przewodami linii energetycznej z prądami 1000 A odległymi o 0,5 m.

$F/L = 2\cdot10^{-7}\cdot1\cdot1/1 = 2\cdot10^{-7}\ \mathrm{N/m}$, zgodnie z dawną definicją ampera.

Linia: $F/L = 2\cdot10^{-7}\cdot10^6/0{,}5 = 0{,}4\ \mathrm{N/m}$, niewiele w porównaniu z ciężarem przewodu (rzędu 10–20 N/m).

**Zadanie 2.** Przy zwarciu w rozdzielni przez szyny odległe o 10 cm płynie prąd 20 kA. Oblicz siłę na metr.

$F/L = 2\cdot10^{-7}\cdot(2\cdot10^4)^2/0{,}1 = 800\ \mathrm{N/m}$. To jak ciężar 80 kg na każdy metr szyny, działający w ułamku sekundy. Szyny muszą być mocno zamocowane.

## Typowe pułapki

- **Prądy zgodne się odpychają (jak ładunki jednoimienne).** Przyciągają się.
- **Siła na przewód od jego własnego pola.** Przewód prosty nie działa sam na siebie siłą wypadkową. Liczy się pole od drugiego przewodu.
- **Wzór dla krótkich przewodów.** Wzór zakłada przewody długie w porównaniu z odległością. Dla krótkich odcinków trzeba całkować.
- **Siła na każdy przewód inna przy różnych prądach.** Siły są równe (III zasada), choć prądy mogą być różne.

## Doświadczenie / symulacja

**Dwie taśmy aluminiowe.** Dwa paski folii aluminiowej (szerokie na 1 cm, długie na 50 cm) zawieś pionowo obok siebie w odległości kilku milimetrów. Podłącz je przez opornik mocy do akumulatora lub zasilacza laboratoryjnego (kilka amperów) raz zgodnie, raz przeciwnie. Paski przyciągają się lub odpychają. Zachowaj ostrożność: duże prądy grzeją przewody, a zwarcie akumulatora jest niebezpieczne.

**Python:** siła na prostokątną ramkę obok przewodu — wzór i całkowanie numeryczne.

```python
import numpy as np
from scipy.integrate import quad

mu0 = 4e-7*np.pi
I1, I2 = 10.0, 5.0
a, b, L = 0.01, 0.05, 0.2                     # ramka: boki L równoległe do przewodu w odległościach a i a + b

F_bliski = mu0*I1*I2*L/(2*np.pi*a)            # przyciąganie (prąd zgodny)
F_daleki = mu0*I1*I2*L/(2*np.pi*(a + b))      # odpychanie (prąd przeciwny)
print(f"siła wypadkowa na ramkę: {(F_bliski - F_daleki)*1e6:.1f} µN w stronę przewodu")

# boki prostopadłe: siły równe i przeciwne, ale każda z osobna wynosi
F_bok = quad(lambda x: mu0*I1*I2/(2*np.pi*x), a, a + b)[0]
print(f"siła na każdy bok prostopadły: {F_bok*1e6:.2f} µN (wzór μ0 I1 I2 ln((a+b)/a)/(2π) = "
      f"{mu0*I1*I2/(2*np.pi)*np.log((a + b)/a)*1e6:.2f} µN)")
for I, d in [(1, 1), (1000, 0.5), (2e4, 0.1)]:
    print(f"I = {I:>6} A, d = {d} m: F/L = {mu0*I*I/(2*np.pi*d):.3g} N/m")
```

## Zadania

### A. Poziom maturalny

1. Dwa równoległe przewody odległe o 2 cm przewodzą prądy 3 A i 4 A w przeciwnych kierunkach. Oblicz siłę na 50 cm długości i określ jej zwrot.

<details>
<summary>Odpowiedź</summary>

$F = 2\cdot10^{-7}\cdot12\cdot0{,}5/0{,}02 = 6\cdot10^{-5}\ \mathrm N$, odpychająca.
</details>

2. Jak zmieni się siła między przewodami, gdy oba prądy wzrosną dwukrotnie, a odległość też wzrośnie dwukrotnie?

<details>
<summary>Odpowiedź</summary>

Wzrośnie dwukrotnie ($\times4/2$).
</details>

3. Trzy długie równoległe przewody leżą w jednej płaszczyźnie co 10 cm, każdy z prądem 10 A w tym samym kierunku. Oblicz siłę na metr działającą na przewód środkowy i na skrajny.

<details>
<summary>Odpowiedź</summary>

Środkowy: siły od sąsiadów się znoszą, więc 0. Skrajny: $2\cdot10^{-7}\cdot100(1/0{,}1 + 1/0{,}2) = 3\cdot10^{-4}\ \mathrm{N/m}$, do środka.
</details>

### B. Poziom akademicki _(opcjonalnie — rozszerzenie z rachunkiem)_

1. Prostokątna ramka z prądem $I_2$ leży obok długiego przewodu z prądem $I_1$. Boki o długości $L$ są równoległe do przewodu w odległościach $a$ i $a + b$. Wyprowadź siłę wypadkową i oblicz ją dla $I_1 = 10\ \mathrm A$, $I_2 = 5\ \mathrm A$, $a = 1\ \mathrm{cm}$, $b = 5\ \mathrm{cm}$, $L = 20\ \mathrm{cm}$ (prąd w bliższym boku zgodny z $I_1$).

<details>
<summary>Odpowiedź</summary>

$F = \dfrac{\mu_0I_1I_2L}{2\pi}\left(\dfrac1a - \dfrac{1}{a + b}\right) \approx 1{,}7\cdot10^{-4}\ \mathrm N$, w stronę przewodu. Siły na boki prostopadłe się znoszą.
</details>

2. Odcinek przewodu o długości $b$ jest prostopadły do długiego przewodu, a jego bliższy koniec jest w odległości $a$. Oblicz całkowaniem siłę, jeśli płyną przez nie prądy $I_1$ i $I_2$.

<details>
<summary>Odpowiedź</summary>

$F = \displaystyle\int_a^{a+b}\frac{\mu_0I_1I_2}{2\pi x}dx = \frac{\mu_0I_1I_2}{2\pi}\ln\frac{a + b}{a}$, równolegle do długiego przewodu.
</details>

3. Dwa długie poziome przewody: górny wisi nad dolnym, nieruchomo przymocowanym, na skutek odpychania. Dolny przewodzi 100 A, górny ma masę 10 g/m. Na jakiej wysokości wisi górny, jeśli płynie w nim 50 A w przeciwnym kierunku? Czy ta równowaga jest trwała w pionie?

<details>
<summary>Odpowiedź</summary>

$\dfrac{\mu_0I_1I_2}{2\pi d} = mg/L \Rightarrow d = \dfrac{2\cdot10^{-7}\cdot5000}{0{,}0981} \approx 1{,}0\ \mathrm{cm}$. W pionie trwała (gdy przewód opada, siła rośnie), ale nie w poziomie: przewód zsunie się na bok.
</details>

## Źródła

- OpenStax, *Fizyka dla szkół wyższych*, t. 2, rozdz. 12 — §12.3: siła magnetyczna między dwoma równoległymi przewodnikami.
- Halliday, Resnick, Walker, *Podstawy fizyki* — wyd. 2015: t. 3, §29.2; wyd. 1: t. 3, §30.2.
