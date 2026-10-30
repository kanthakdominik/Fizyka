# 19.01 — Postulaty Einsteina i względność równoczesności

> **Moduł:** [19 — Szczególna teoria względności](README.md) · **Poziom:** 🟢 matura R · **Status:** ✅ pełny
>
> **Czytaj:**
>
> - OpenStax, *Fizyka dla szkół wyższych*, t. 3, rozdz. 5: [§5.1–5.2](https://openstax.org/books/fizyka-dla-szk%C3%B3%C5%82-wy%C5%BCszych-tom-3/pages/5-1-niezmiennosc-praw-fizyki) · [wstęp do rozdziału](https://openstax.org/books/fizyka-dla-szk%C3%B3%C5%82-wy%C5%BCszych-tom-3/pages/5-wstep)
> - Halliday, Resnick, Walker, *Podstawy fizyki*, wyd. 2015, t. 4: §37.1 (s. 187)
> - Halliday, Resnick, Walker, *Podstawy fizyki*, wyd. 1 (2003), t. 4: [§38.1–38.4, s. 146](https://home.agh.edu.pl/~czapli/Resnick_4.pdf#page=161) — PDF z serwera AGH

← (początek modułu) · [spis modułu](README.md) · [Dylatacja czasu i skrócenie długości](02-dylatacja-i-skrocenie.md) →

## Po co to jest

Równania Maxwella (16) dają prędkość światła $c$ bez wskazania, względem czego. Mechanika Newtona mówi, że prędkości się dodają. Te dwie teorie nie mogą być jednocześnie prawdziwe. Einstein w 1905 r. rozstrzygnął ten konflikt, przyjmując, że prędkość światła jest taka sama dla wszystkich obserwatorów. Ceną jest rezygnacja z absolutnego czasu: zdarzenia równoczesne dla jednego obserwatora nie są równoczesne dla innego. Szczególna teoria względności jest potrzebna do akceleratorów, GPS, fizyki cząstek, energii jądrowej i astrofizyki.

## Teoria w pigułce

**Zasada względności Galileusza** (03.06): prawa mechaniki są takie same we wszystkich inercjalnych układach odniesienia. Prędkości się dodają: $u' = u - v$.

**Problem.** Z równań Maxwella wynika jedna prędkość fal elektromagnetycznych, $c$. Fizycy XIX wieku zakładali, że jest to prędkość względem ośrodka, eteru. Wtedy Ziemia, krążąca wokół Słońca z prędkością 30 km/s, powinna odczuwać „wiatr eteru”. **Doświadczenie Michelsona–Morleya** (1887) porównywało interferometrem (18.04) czasy przebiegu światła w dwóch prostopadłych ramionach. Nie wykryło żadnej różnicy.

**Postulaty Einsteina (1905):**
1. **Zasada względności**: wszystkie prawa fizyki (nie tylko mechaniki) są takie same we wszystkich inercjalnych układach odniesienia. Nie ma wyróżnionego układu ani eteru.
2. **Stałość prędkości światła**: prędkość światła w próżni wynosi $c$ dla każdego obserwatora inercjalnego, niezależnie od ruchu źródła i obserwatora.

**Względność równoczesności.** W środku jadącego wagonu błyska lampa.
- Dla pasażera światło biegnie z prędkością $c$ w obie strony i dociera do obu końców wagonu **jednocześnie**.
- Dla obserwatora na peronie światło też biegnie z prędkością $c$ w obie strony, ale tylna ściana wagonu wychodzi mu na spotkanie, a przednia ucieka. Światło dociera do tyłu **wcześniej**.

Oba opisy są poprawne. Równoczesność zdarzeń w różnych miejscach zależy od układu odniesienia. To nie złudzenie ani błąd pomiaru, tylko własność czasoprzestrzeni. Kolejność zdarzeń połączonych przyczynowo (takich, że sygnał z jednego może dotrzeć do drugiego) jest jednak taka sama dla wszystkich (19.03).

**Zdarzenie** to punkt w czasoprzestrzeni: miejsce i chwila $(x, y, z, t)$. Obserwator to układ odniesienia z zegarami zsynchronizowanymi sygnałami świetlnymi w całej przestrzeni, a nie człowiek, który coś „widzi”.

## Wzory i założenia

| Wzór / pojęcie | Znaczenie | Kiedy obowiązuje |
|---|---|---|
| $c = 299\,792\,458\ \mathrm{m/s}$ | prędkość światła, ta sama dla wszystkich | próżnia, układy inercjalne |
| $u' = u - v$ | dodawanie prędkości Galileusza | tylko $v, u \ll c$ (dokładnie: 19.03) |
| równoczesność zależy od układu | — | zdarzenia w różnych miejscach |
| $\gamma = 1/\sqrt{1 - v^2/c^2}$ | czynnik Lorentza (19.02) | — |

## Przykład rozwiązany

**Zadanie.** Wagon o długości 100 m jedzie z prędkością $0{,}6c$. W jego środku błyska lampa. Po jakim czasie światło dociera do przedniej i tylnej ściany według pasażera, a po jakim według obserwatora na peronie? Długość wagonu w układzie peronu wynosi 80 m (skrócenie Lorentza, 19.02).

Pasażer: do obu ścian po $50\ \mathrm m/c \approx 167\ \mathrm{ns}$, jednocześnie.

Peron: tył zbliża się z prędkością $0{,}6c$, więc $ct = 40 - 0{,}6ct \Rightarrow t_{\text{tył}} = \dfrac{40}{1{,}6c} \approx 83\ \mathrm{ns}$. Przód ucieka: $ct = 40 + 0{,}6ct \Rightarrow t_{\text{przód}} = \dfrac{40}{0{,}4c} \approx 334\ \mathrm{ns}$. Różnica wynosi 250 ns.

## Typowe pułapki

- **Teoria względności mówi, że wszystko jest względne.** Wiele wielkości jest absolutnych: prędkość światła, interwał czasoprzestrzenny (19.03), masa spoczynkowa, kolejność zdarzeń przyczynowo związanych.
- **Efekty wynikają z czasu biegu sygnału do obserwatora.** Uwzględniają już opóźnienie sygnałów. Pozostaje rzeczywista różnica w opisie zdarzeń.
- **Postulat o stałości $c$ dotyczy światła tylko w próżni.** W wodzie światło biegnie wolniej, ale granica $c$ dla wszystkich sygnałów nadal obowiązuje.
- **Prędkość światła źródła zależy od ruchu źródła.** Obserwacje gwiazd podwójnych i rozpadu szybkich pionów pokazują, że nie zależy.

## Doświadczenie / symulacja

**Michelson–Morley w liczbach.** Policz w Pythonie (kod niżej), o ile przesunęłyby się prążki w interferometrze Michelsona i Morleya (ramiona 11 m, światło 500 nm), gdyby istniał wiatr eteru 30 km/s, i porównaj z czułością ich pomiaru (ok. 0,01 prążka).

**Gra *A Slower Speed of Light*** (MIT Game Lab, darmowa) pokazuje efekty relatywistyczne, gdy prędkość światła jest bardzo mała.

**Python:** przewidywane przesunięcie prążków w doświadczeniu Michelsona–Morleya.

```python
import numpy as np

c, v, L, lam = 2.998e8, 3e4, 11.0, 500e-9
t_rown = 2*L/c/(1 - v**2/c**2)                 # ramię wzdłuż ruchu
t_prost = 2*L/c/np.sqrt(1 - v**2/c**2)         # ramię prostopadłe
dt = t_rown - t_prost
N = 2*c*dt/lam                                 # obrót aparatu o 90° zamienia ramiona
print(f"różnica czasów: {dt:.2e} s, oczekiwane przesunięcie po obrocie: {N:.2f} prążka")
print("zmierzone: < 0,01 prążka — brak wiatru eteru")

# względność równoczesności w wagonie 100 m przy 0,6c
L0, b = 100.0, 0.6
Lp = L0*np.sqrt(1 - b**2)
print(f"pasażer: {L0/2/c*1e9:.0f} ns do obu ścian; peron: tył {Lp/2/(1 + b)/c*1e9:.0f} ns, przód {Lp/2/(1 - b)/c*1e9:.0f} ns")
```

## Zadania

### A. Poziom maturalny

1. Rakieta leci z prędkością $0{,}5c$ i wysyła światło do przodu. Z jaką prędkością biegnie to światło według obserwatora na Ziemi?

<details>
<summary>Odpowiedź</summary>

$c$, nie $1{,}5c$.
</details>

2. Wymień dwa postulaty szczególnej teorii względności.

<details>
<summary>Odpowiedź</summary>

Prawa fizyki są takie same we wszystkich układach inercjalnych. Prędkość światła w próżni jest taka sama dla wszystkich obserwatorów inercjalnych.
</details>

3. Dlaczego wynik doświadczenia Michelsona–Morleya był dla fizyków XIX wieku zaskoczeniem?

<details>
<summary>Odpowiedź</summary>

Spodziewali się, że ruch Ziemi względem eteru zmieni czasy biegu światła w ramionach interferometru i przesunie prążki. Nie zaobserwowano żadnego przesunięcia.
</details>

### B. Poziom akademicki _(opcjonalnie — rozszerzenie z rachunkiem)_

1. Pokaż, że w teorii eteru czas biegu światła tam i z powrotem w ramieniu o długości $L$ wzdłuż ruchu wynosi $\dfrac{2L/c}{1 - v^2/c^2}$, a w ramieniu prostopadłym $\dfrac{2L/c}{\sqrt{1 - v^2/c^2}}$.

<details>
<summary>Odpowiedź</summary>

Wzdłuż: $\dfrac{L}{c - v} + \dfrac{L}{c + v} = \dfrac{2Lc}{c^2 - v^2}$. Prostopadle: światło musi biec ukośnie z prędkością $c$, a jej składowa prostopadła wynosi $\sqrt{c^2 - v^2}$, więc $2L/\sqrt{c^2 - v^2}$.
</details>

2. Dwa błyski piorunów uderzają jednocześnie (w układzie peronu) w punkty odległe o 1 km. Pociąg jedzie z prędkością $0{,}5c$. Oblicz różnicę czasów tych zdarzeń w układzie pociągu, korzystając z transformacji Lorentza $\Delta t' = \gamma(\Delta t - v\Delta x/c^2)$ (19.03). Który piorun uderzył pierwszy według pasażera?

<details>
<summary>Odpowiedź</summary>

$\lvert\Delta t'\rvert = \gamma v\Delta x/c^2 = 1{,}155\cdot0{,}5\cdot10^3/c \approx 1{,}9\ \mu\mathrm s$. Pierwszy był piorun od strony przodu pociągu (w kierunku ruchu).
</details>

## Źródła

- OpenStax, *Fizyka dla szkół wyższych*, t. 3, rozdz. 5 — §5.1 (niezmienniczość praw fizyki) i §5.2 (względność równoczesności).
- Halliday, Resnick, Walker, *Podstawy fizyki* — wyd. 2015: t. 4, §37.1; wyd. 1: t. 4, §38.1–38.4.
