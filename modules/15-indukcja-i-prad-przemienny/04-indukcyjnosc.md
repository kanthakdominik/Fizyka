# 15.04 — Indukcyjność własna i wzajemna, energia pola magnetycznego

> **Moduł:** [15 — Indukcja elektromagnetyczna i prąd przemienny](README.md) · **Poziom:** 🟢🔵 matura R + studia · **Status:** ✅ pełny
>
> **Czytaj:**
>
> - OpenStax, *Fizyka dla szkół wyższych*, t. 2, rozdz. 14: [§14.1–14.3](https://openstax.org/books/fizyka-dla-szk%C3%B3%C5%82-wy%C5%BCszych-tom-2/pages/14-1-indukcyjnosc-wzajemna) · [wstęp do rozdziału](https://openstax.org/books/fizyka-dla-szk%C3%B3%C5%82-wy%C5%BCszych-tom-2/pages/14-wstep)
> - Halliday, Resnick, Walker, *Podstawy fizyki*, wyd. 2015, t. 3: §30.4–30.5 (s. 348), §30.7–30.9 (s. 357)
> - Halliday, Resnick, Walker, *Podstawy fizyki*, wyd. 1 (2003), t. 3: §31.7–31.8, s. 264, §31.10–31.12, s. 271 (skan t. 3 na serwerze AGH kończy się na s. 127 — dalsze strony tylko w wydaniu papierowym)

← [Prądy wirowe, prądnice i SEM wsteczna](03-pradnice-i-prady-wirowe.md) · [spis modułu](README.md) · [Obwody RL, LC i RLC — drgania elektromagnetyczne](05-obwody-rl-lc-rlc.md) →

## Po co to jest

Cewka „nie lubi” zmian prądu: sprzeciwia się im napięciem samoindukcji. Na tym działają dławiki w zasilaczach, filtry, przetwornice napięcia w ładowarkach, zapłon w silnikach benzynowych (iskra kilkunastu kilowoltów z akumulatora 12 V) i czujniki pętli indukcyjnych pod skrzyżowaniami. Indukcyjność wzajemna to zasada działania transformatora (15.07) i ładowarek bezprzewodowych. Energię można magazynować w polu magnetycznym, tak jak w polu elektrycznym kondensatora.

## Teoria w pigułce

**Indukcyjność wzajemna.** Prąd $I_1$ w cewce 1 wytwarza strumień przez cewkę 2. Strumień jest proporcjonalny do prądu: $N_2\Phi_{21} = MI_1$. Zmiana prądu indukuje w cewce 2 SEM:

$$\varepsilon_2 = -M\frac{dI_1}{dt}.$$

$M$ to indukcyjność wzajemna, zależna od geometrii i ułożenia cewek. Zachodzi symetria $M_{12} = M_{21}$.

**Samoindukcja.** Prąd w cewce wytwarza strumień przez nią samą: $N\Phi = LI$. Zmiana prądu indukuje SEM przeciwdziałającą tej zmianie:

$$\varepsilon_L = -L\frac{dI}{dt}, \qquad [L] = \mathrm H = \mathrm{\frac{V\cdot s}{A}}.$$

Cewka działa jak „bezwładność” prądu. Przy nagłym przerwaniu prądu $dI/dt$ jest ogromne i powstaje wysokie napięcie (iskra na stykach wyłącznika, cewka zapłonowa). Dlatego przekaźniki zabezpiecza się diodą równoległą do cewki.

**Indukcyjność długiego solenoidu** ($N$ zwojów, długość $l$, pole przekroju $A$): $B = \mu_0NI/l$, $\Phi = BA$, więc

$$L = \frac{\mu_0N^2A}{l}.$$

Rdzeń ferromagnetyczny mnoży indukcyjność przez $\mu_r$ (14.07).

**Energia w cewce.** Żeby zwiększyć prąd od 0 do $I$, źródło musi pokonać SEM samoindukcji: $dW = LI\,dI$. Stąd

$$W = \tfrac12LI^2.$$

Energia siedzi w polu magnetycznym, a jej **gęstość** wynosi

$$w = \frac{B^2}{2\mu_0}.$$

To odpowiednik $\tfrac12\varepsilon_0E^2$ dla pola elektrycznego (12.06).

## Wzory i założenia

| Wzór | Znaczenie | Kiedy obowiązuje |
|---|---|---|
| $\varepsilon_2 = -M\,dI_1/dt$ | indukcja wzajemna | — |
| $\varepsilon_L = -L\,dI/dt$ | samoindukcja | — |
| $L = N\Phi/I$ | definicja indukcyjności | — |
| $L = \mu_0N^2A/l$ | solenoid | $l \gg$ średnica, bez rdzenia |
| $W = \tfrac12LI^2$ | energia cewki | — |
| $w = B^2/(2\mu_0)$ | gęstość energii pola | próżnia |

## Przykład rozwiązany

**Zadanie.** Solenoid z 14.06 (1000 zwojów, długość 50 cm) ma promień 2 cm. Oblicz jego indukcyjność i energię przy prądzie 2 A. Jakie napięcie powstanie, gdy prąd spadnie do zera w czasie 1 ms?

$A = \pi\cdot0{,}02^2 \approx 1{,}26\cdot10^{-3}\ \mathrm{m^2}$, $L = \dfrac{4\pi\cdot10^{-7}\cdot10^6\cdot1{,}26\cdot10^{-3}}{0{,}5} \approx 3{,}2\ \mathrm{mH}$.

$W = \tfrac12\cdot3{,}2\cdot10^{-3}\cdot4 \approx 6{,}3\ \mathrm{mJ}$.

$\lvert\varepsilon\rvert = L\Delta I/\Delta t \approx 3{,}2\cdot10^{-3}\cdot2/10^{-3} \approx 6{,}3\ \mathrm V$. Przy przerwaniu w mikrosekundę byłoby to ponad 6 kV.

### Wersja z rachunkiem różniczkowym i całkowym

**Sprawdzenie energii przez gęstość pola.** W solenoidzie $B = \mu_0nI \approx 5{,}0\ \mathrm{mT}$, więc $w = B^2/(2\mu_0) \approx 10\ \mathrm{J/m^3}$. Objętość: $Al \approx 6{,}3\cdot10^{-4}\ \mathrm{m^3}$. Energia: $W = wAl \approx 6{,}3\ \mathrm{mJ}$, tyle samo co z $\tfrac12LI^2$.

**Indukcyjność wzajemna dwóch współosiowych solenoidów.** Na zewnętrzny solenoid (1000 zwojów, $l = 0{,}5\ \mathrm m$) nawinięto ciasno drugą cewkę o 100 zwojach. Pole pierwszego przechodzi przez wszystkie zwoje drugiego:

$$M = \frac{N_2\Phi_{21}}{I_1} = \frac{\mu_0N_1N_2A}{l} \approx 0{,}32\ \mathrm{mH}.$$

## Typowe pułapki

- **Cewka przeciwdziała prądowi.** Przeciwdziała **zmianie** prądu. Przy stałym prądzie idealna cewka zachowuje się jak zwykły przewód.
- **$L$ zależy od prądu.** Dla cewki bez rdzenia to stała geometryczna. W rdzeniu ferromagnetycznym zależy od prądu (nasycenie).
- **$L \propto N$.** Indukcyjność rośnie jak $N^2$: więcej zwojów to większe pole i więcej zwojów, przez które ono przechodzi.
- **Energia cewki $LI^2$.** Energia to $\tfrac12LI^2$.
- **Indukcyjność wzajemna zależy od tego, która cewka jest „pierwsza”.** $M_{12} = M_{21}$.

## Doświadczenie / symulacja

**Neonówka i cewka.** Cewka z rdzeniem (np. uzwojenie starego transformatora sieciowego) połączona równolegle z neonówką i zasilana z baterii 4,5 V. Neonówka zapala się dopiero przy **rozłączaniu** obwodu, gdy napięcie samoindukcji przekracza ok. 70 V.

**Ładowarka bezprzewodowa.** Cewka nadawcza i odbiorcza ładowarki Qi to indukcja wzajemna. Sprawdź, jak zmienia się ładowanie, gdy odsuwasz telefon o kilka milimetrów albo przesuwasz go w bok. $M$ szybko maleje z odległością.

**Python:** indukcyjność solenoidu i energia — trzy sposoby.

```python
import numpy as np

mu0 = 4e-7*np.pi
N, l, r, I = 1000, 0.5, 0.02, 2.0
A = np.pi*r**2
L = mu0*N**2*A/l
B = mu0*N/l*I
print(f"L = {L*1e3:.3f} mH")
print(f"energia: ½LI² = {0.5*L*I**2*1e3:.3f} mJ, z gęstości pola {B**2/(2*mu0)*A*l*1e3:.3f} mJ, "
      f"z całki ∫LI dI = {np.sum(L*np.linspace(0, I, 100001)[:-1]*I/100000)*1e3:.3f} mJ")
for dt in (1e-3, 1e-6):
    print(f"przerwanie prądu w {dt:.0e} s: |ε| = {L*I/dt:.1f} V")
print(f"M (100 zwojów nawiniętych na solenoid) = {mu0*N*100*A/l*1e3:.3f} mH")
```

## Zadania

### A. Poziom maturalny

1. Prąd w cewce o indukcyjności 50 mH zmienia się w tempie 200 A/s. Jaka SEM samoindukcji powstaje?

<details>
<summary>Odpowiedź</summary>

10 V.
</details>

2. Ile energii jest zgromadzone w cewce 0,5 H przy prądzie 3 A?

<details>
<summary>Odpowiedź</summary>

2,25 J.
</details>

3. Jak zmieni się indukcyjność solenoidu, gdy dwukrotnie zwiększymy liczbę zwojów przy tej samej długości? A gdy włożymy rdzeń o $\mu_r = 500$?

<details>
<summary>Odpowiedź</summary>

Wzrośnie 4 razy. Z rdzeniem wzrośnie ok. 500 razy (dopóki rdzeń się nie nasyci).
</details>

### B. Poziom akademicki

1. Wyprowadź indukcyjność na jednostkę długości kabla koncentrycznego (przewód o promieniu $a$, ekran o promieniu $b$), licząc energię pola między nimi.

<details>
<summary>Odpowiedź</summary>

$B = \mu_0I/(2\pi r)$, $W/l = \displaystyle\int_a^b\frac{B^2}{2\mu_0}2\pi r\,dr = \frac{\mu_0I^2}{4\pi}\ln\frac ba$. Z $W = \tfrac12LI^2$: $L/l = \dfrac{\mu_0}{2\pi}\ln\dfrac ba$.
</details>

2. Cewka zapłonowa ma uzwojenie pierwotne o indukcyjności 5 mH i prądzie 5 A. Przerwanie prądu trwa 50 μs. Oszacuj napięcie na uzwojeniu pierwotnym. Uzwojenie wtórne ma 100 razy więcej zwojów. Jakie napięcie może tam powstać?

<details>
<summary>Odpowiedź</summary>

Pierwotne: $L\Delta I/\Delta t = 5\cdot10^{-3}\cdot5/5\cdot10^{-5} = 500\ \mathrm V$. Wtórne do ok. 50 kV (w praktyce iskra przeskakuje przy 10–30 kV).
</details>

3. Dwie cewki o indukcyjnościach $L_1$, $L_2$ i indukcyjności wzajemnej $M$ połączono szeregowo zgodnie i przeciwnie. Pokaż, że indukcyjność zastępcza wynosi $L_1 + L_2 \pm 2M$.

<details>
<summary>Odpowiedź</summary>

Ten sam prąd płynie przez obie. SEM całkowita: $-(L_1 + L_2)\dot I \mp 2M\dot I$, bo każda cewka indukuje w drugiej $M\dot I$. Tak mierzy się $M$: $M = (L_{\text{zg}} - L_{\text{przec}})/4$.
</details>

## Źródła

- OpenStax, *Fizyka dla szkół wyższych*, t. 2, rozdz. 14 — §14.1 (indukcyjność wzajemna), §14.2 (samoindukcja i cewki), §14.3 (energia w polu magnetycznym).
- Halliday, Resnick, Walker, *Podstawy fizyki* — wyd. 2015: t. 3, §30.4–30.5, §30.7–30.9; wyd. 1: t. 3, §31.7–31.8, §31.10–31.12.
