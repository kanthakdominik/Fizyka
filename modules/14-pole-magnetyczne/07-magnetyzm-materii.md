# 14.07 — Magnetyzm materii: dia-, para- i ferromagnetyki

> **Moduł:** [14 — Pole magnetyczne](README.md) · **Poziom:** 🟢🔵 matura R + studia · **Status:** ✅ pełny
>
> **Czytaj:**
>
> - OpenStax, *Fizyka dla szkół wyższych*, t. 2, rozdz. 12: [§12.7](https://openstax.org/books/fizyka-dla-szk%C3%B3%C5%82-wy%C5%BCszych-tom-2/pages/12-7-magnetyzm-materii) · [wstęp do rozdziału](https://openstax.org/books/fizyka-dla-szk%C3%B3%C5%82-wy%C5%BCszych-tom-2/pages/12-wstep)
> - Halliday, Resnick, Walker, *Podstawy fizyki*, wyd. 2015, t. 3: §32.4–32.8 (s. 437)
> - Halliday, Resnick, Walker, *Podstawy fizyki*, wyd. 1 (2003), t. 3: §32.1, s. 290, §32.3–32.8, s. 292 (skan t. 3 na serwerze AGH kończy się na s. 127 — dalsze strony tylko w wydaniu papierowym)

← [Prawo Ampère'a, solenoid i toroid](06-prawo-ampera.md) · [spis modułu](README.md) · (koniec modułu) →

## Po co to jest

Dlaczego żelazo przyciąga magnes, a aluminium i miedź prawie wcale? Odpowiedź tkwi w atomach. Każdy elektron to maleńki magnes, a w ferromagnetykach miliardy takich magnesów porządkują się wspólnie w domeny. Magnetyzm materii decyduje o rdzeniach transformatorów i silników, magnesach neodymowych w samochodach elektrycznych i turbinach wiatrowych, zapisie na dyskach twardych i kontraście w obrazach MRI. Nawet woda jest magnetyczna, tylko bardzo słabo: w polu 16 T można zawiesić w powietrzu żabę.

## Teoria w pigułce

**Źródła magnetyzmu atomów.** Elektron krążący wokół jądra to mała pętla z prądem, czyli moment magnetyczny (14.02). Elektron ma też własny, **spinowy** moment magnetyczny (efekt kwantowy, 21). Naturalną jednostką jest **magneton Bohra**:

$$\mu_B = \frac{e\hbar}{2m_e} \approx 9{,}27\cdot10^{-24}\ \mathrm{A\cdot m^2}.$$

W większości atomów i cząsteczek momenty elektronów kompensują się parami. Zostają tylko w atomach z niesparowanymi elektronami (Fe, Co, Ni, Gd, O₂).

**Namagnesowanie** $\vec M$ to wypadkowy moment magnetyczny na jednostkę objętości. W materiale pole wynosi:

$$\vec B = \mu_0(\vec H + \vec M), \qquad \vec M = \chi\vec H, \qquad \vec B = \mu_r\mu_0\vec H,\ \ \mu_r = 1 + \chi.$$

$\vec H$ to natężenie pola magnetycznego wytwarzane przez prądy swobodne (w solenoidzie $H = nI$). $\chi$ to podatność magnetyczna, a $\mu_r$ przenikalność względna.

**Trzy rodzaje materiałów:**

| Rodzaj | $\chi$ | Mechanizm | Przykłady |
|---|---|---|---|
| diamagnetyki | ujemna, ok. $-10^{-5}$ | pole indukuje momenty przeciwne do siebie (reguła Lenza, 15); występuje we wszystkich materiałach | woda ($-9\cdot10^{-6}$), miedź, bizmut ($-1{,}7\cdot10^{-4}$), nadprzewodniki ($\chi = -1$) |
| paramagnetyki | dodatnia, $10^{-5}$–$10^{-3}$ | trwałe momenty częściowo porządkują się w polu, przeszkadzają ruchy cieplne | aluminium ($2{,}2\cdot10^{-5}$), tlen, platyna |
| ferromagnetyki | ogromna, $\mu_r \sim 10^2$–$10^5$ | sąsiednie momenty porządkują się samorzutnie (oddziaływanie kwantowe) w **domeny** | żelazo, kobalt, nikiel, stopy NdFeB |

Diamagnetyk jest wypychany z obszaru silnego pola, a paramagnetyk i ferromagnetyk są do niego wciągane.

**Prawo Curie dla paramagnetyków:** $\chi \propto 1/T$. Im wyższa temperatura, tym trudniej uporządkować momenty.

**Ferromagnetyki:**
- Bez pola zewnętrznego domeny są ułożone przypadkowo. Pole powiększa domeny zgodne z nim i obraca pozostałe.
- **Pętla histerezy**: namagnesowanie zależy od historii. Wielkości charakterystyczne to **nasycenie** (wszystkie momenty zgodne), **pozostałość** (remanencja, magnes trwały) i **koercja** (pole potrzebne do rozmagnesowania).
- Materiały **magnetycznie miękkie** (wąska pętla) stosuje się w rdzeniach transformatorów, bo mają małe straty. Materiały **twarde** (szeroka pętla) to magnesy trwałe i nośniki zapisu.
- Powyżej **temperatury Curie** ferromagnetyk staje się paramagnetykiem. Dla żelaza to 1043 K (770°C).

## Wzory i założenia

| Wzór | Znaczenie | Kiedy obowiązuje |
|---|---|---|
| $\mu_B = e\hbar/(2m_e) \approx 9{,}27\cdot10^{-24}\ \mathrm{A\cdot m^2}$ | magneton Bohra | — |
| $\vec B = \mu_0(\vec H + \vec M)$ | pole w materiale | — |
| $\vec M = \chi\vec H$, $\mu_r = 1 + \chi$ | materiał liniowy | dia- i paramagnetyki |
| $B = \mu_r\mu_0nI$ | solenoid z rdzeniem | ferromagnetyk poniżej nasycenia |
| $\chi = C/T$ | prawo Curie | paramagnetyki, $\mu B \ll kT$ |
| $M_s = n\mu_{\text{at}}$ | namagnesowanie nasycenia | wszystkie momenty zgodne |

## Przykład rozwiązany

**Zadanie 1.** Atom żelaza ma średnio moment ok. $2{,}2\mu_B$, a w 1 m³ żelaza jest $8{,}5\cdot10^{28}$ atomów. Oszacuj namagnesowanie nasycenia i odpowiadające mu pole $\mu_0M_s$.

$M_s = 8{,}5\cdot10^{28}\cdot2{,}2\cdot9{,}27\cdot10^{-24} \approx 1{,}7\cdot10^6\ \mathrm{A/m}$, więc $\mu_0M_s \approx 2{,}2\ \mathrm T$. Doświadczalnie żelazo nasyca się przy ok. 2,15 T. Dlatego rdzenie elektromagnesów nie dają więcej niż ok. 2 T.

**Zadanie 2.** Solenoid z 14.06 (5 mT bez rdzenia) wypełniono żelazem o $\mu_r = 1000$. Jakie pole można uzyskać?

Liniowo wychodziłoby $1000\cdot5\ \mathrm{mT} = 5\ \mathrm T$, ale to ponad nasycenie. Rzeczywiste pole wyniesie ok. 2 T. Przy słabszym prądzie (np. 0,2 A, czyli 0,5 mT bez rdzenia) rdzeń wzmacnia pole ok. 1000 razy, do 0,5 T.

### Wersja z rachunkiem różniczkowym i całkowym

**Zadanie.** Wyprowadź prawo Curie dla układu momentów $\mu$, które mogą ustawić się zgodnie z polem (energia $-\mu B$) albo przeciwnie ($+\mu B$). Oszacuj stopień uporządkowania dla $\mu = \mu_B$ w polu 1 T w temperaturze 300 K.

Z rozkładu Boltzmanna (11.07) prawdopodobieństwa obu stanów są proporcjonalne do $e^{\pm\mu B/kT}$. Średni moment:

$$\bar\mu = \mu\frac{e^{x} - e^{-x}}{e^{x} + e^{-x}} = \mu\tanh x, \qquad x = \frac{\mu B}{kT}.$$

Dla $x \ll 1$: $\tanh x \approx x$, więc $M = n\bar\mu \approx \dfrac{n\mu^2B}{kT}$, czyli $\chi \propto 1/T$ (prawo Curie).

Dla $\mu_B$, 1 T i 300 K: $x \approx 2{,}2\cdot10^{-3}$. Tylko 0,2% uporządkowania. Ruchy cieplne niemal całkowicie zacierają wpływ pola. W 4 K i 10 T uporządkowanie byłoby prawie pełne.

## Typowe pułapki

- **Niemagnetyczne materiały.** Każdy materiał reaguje na pole. Dia- i paramagnetyzm są tylko $10^4$–$10^5$ razy słabsze od ferromagnetyzmu.
- **$\mu_r$ żelaza to stała.** W ferromagnetykach $\mu_r$ zależy od pola i od historii (histereza), a przy nasyceniu spada.
- **Magnes podgrzany staje się silniejszy.** Powyżej temperatury Curie ferromagnetyk traci uporządkowanie. Już poniżej niej namagnesowanie słabnie z temperaturą.
- **Diamagnetyk przyciągany słabiej niż paramagnetyk.** Diamagnetyk jest **odpychany** od obszaru silnego pola.
- **$B$ i $H$ to to samo.** W próżni różnią się tylko stałą $\mu_0$. W materiale $H$ zależy od prądów swobodnych, a $B$ także od namagnesowania.

## Doświadczenie / symulacja

**Woda i winogrona.** Zawieś na cienkiej nitce słomkę z dwoma winogronami na końcach (lub z dwiema małymi butelkami wody) tak, by się swobodnie obracała. Zbliż silny magnes neodymowy do jednego winogrona. Winogrono powoli się **odsuwa**, bo woda jest diamagnetykiem.

**Temperatura Curie.** Gwóźdź stalowy przyciągany przez magnes podgrzej palnikiem do czerwoności (ok. 770°C). Odpada od magnesu, a po ostygnięciu znowu się przyciąga. Doświadczenie z ogniem, tylko pod opieką dorosłych.

**Pomiar pola magnesu.** Magnetometrem telefonu zmierz pole magnesu w funkcji odległości. Daleko od magnesu pole dipola maleje jak $1/r^3$ (14.04).

**Symulacja PhET:** *Magnesy i elektromagnesy* (*Magnets and Electromagnets*) — porównanie magnesu sztabkowego i elektromagnesu.

**Python:** dwustanowy paramagnetyk (tanh) i prawo Curie.

```python
import numpy as np
import matplotlib.pyplot as plt

muB, k = 9.274e-24, 1.381e-23
x = np.linspace(0, 4, 300)
plt.plot(x, np.tanh(x), label="dokładnie: tanh(μB/kT)")
plt.plot(x, x, "--", label="prawo Curie: μB/kT")
plt.ylim(0, 1.1)
for B, T in [(1, 300), (1, 4), (10, 4), (10, 1)]:
    xv = muB*B/(k*T)
    print(f"B = {B:2d} T, T = {T:3d} K: x = {xv:.4f}, uporządkowanie = {np.tanh(xv):.4f}")
n, m_at = 8.5e28, 2.2*muB
print(f"nasycenie żelaza: M = {n*m_at:.2e} A/m, μ0M = {4e-7*np.pi*n*m_at:.2f} T")
plt.xlabel("x = μB/kT"); plt.ylabel("M / M_nasycenia"); plt.grid(True); plt.legend(); plt.show()
```

## Zadania

### A. Poziom maturalny

1. Podziel materiały na dia-, para- i ferromagnetyki: miedź, żelazo, aluminium, woda, nikiel, tlen.

<details>
<summary>Odpowiedź</summary>

Diamagnetyki: miedź, woda. Paramagnetyki: aluminium, tlen. Ferromagnetyki: żelazo, nikiel.
</details>

2. Dlaczego rdzenie transformatorów robi się z żelaza miękkiego magnetycznie, a magnesy trwałe z materiałów twardych?

<details>
<summary>Odpowiedź</summary>

Rdzeń transformatora jest przemagnesowywany 50 razy na sekundę, a straty energii w każdym cyklu są proporcjonalne do pola pętli histerezy, więc musi ona być wąska. Magnes trwały ma zachować namagnesowanie mimo zakłóceń, więc potrzebuje dużej koercji (szerokiej pętli).
</details>

3. Magnes trwały upuszczony lub mocno podgrzany słabnie. Wyjaśnij to modelem domen.

<details>
<summary>Odpowiedź</summary>

Wstrząsy i ruchy cieplne pozwalają domenom zmieniać orientację na przypadkową, więc wypadkowe namagnesowanie maleje. Powyżej temperatury Curie uporządkowanie znika całkowicie.
</details>

### B. Poziom akademicki

1. Rdzeń transformatora o objętości 0,01 m³ ma pętlę histerezy o polu 100 J/m³. Jaka moc jest tracona przy 50 Hz?

<details>
<summary>Odpowiedź</summary>

$P = 100\cdot0{,}01\cdot50 = 50\ \mathrm W$.
</details>

2. Pokaż, że moment magnetyczny elektronu na orbicie kołowej jest związany z jego momentem pędu wzorem $\mu = \dfrac{e}{2m_e}L$. Ile wynosi dla $L = \hbar$?

<details>
<summary>Odpowiedź</summary>

$I = e/T = ev/(2\pi r)$, $\mu = I\pi r^2 = evr/2$, a $L = m_evr$, więc $\mu = eL/(2m_e)$. Dla $L = \hbar$ wychodzi magneton Bohra.
</details>

3. Żaba lewituje w polu, gdy siła diamagnetyczna na jednostkę objętości $\dfrac{\lvert\chi\rvert}{\mu_0}B\dfrac{dB}{dz}$ równoważy ciężar $\rho g$. Oszacuj potrzebne $B\,dB/dz$ dla wody ($\chi = -9\cdot10^{-6}$) i porównaj z elektromagnesem 16 T o gradiencie ok. 100 T/m.

<details>
<summary>Odpowiedź</summary>

$B\dfrac{dB}{dz} = \dfrac{\mu_0\rho g}{\lvert\chi\rvert} \approx 1400\ \mathrm{T^2/m}$. Magnes 16 T z gradientem 100 T/m daje ok. 1600 T²/m, czyli wystarczy, co w 1997 r. pokazali Geim i Berry.
</details>

## Źródła

- OpenStax, *Fizyka dla szkół wyższych*, t. 2, rozdz. 12 — §12.7: magnetyzm materii.
- Halliday, Resnick, Walker, *Podstawy fizyki* — wyd. 2015: t. 3, §32.4–32.8; wyd. 1: t. 3, §32.1, §32.3–32.8.
- Symulacja PhET *Magnesy i elektromagnesy*.
