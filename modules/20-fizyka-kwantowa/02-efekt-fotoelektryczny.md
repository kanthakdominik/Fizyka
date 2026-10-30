# 20.02 — Efekt fotoelektryczny

> **Moduł:** [20 — Podstawy fizyki kwantowej](README.md) · **Poziom:** 🟢 matura R · **Status:** ✅ pełny
>
> **Czytaj:**
>
> - OpenStax, *Fizyka dla szkół wyższych*, t. 3, rozdz. 6: [§6.2](https://openstax.org/books/fizyka-dla-szk%C3%B3%C5%82-wy%C5%BCszych-tom-3/pages/6-2-efekt-fotoelektryczny) · [wstęp do rozdziału](https://openstax.org/books/fizyka-dla-szk%C3%B3%C5%82-wy%C5%BCszych-tom-3/pages/6-wstep)
> - Halliday, Resnick, Walker, *Podstawy fizyki*, wyd. 2015, t. 5: §38.1–38.2 (s. 1)
> - Halliday, Resnick, Walker, *Podstawy fizyki*, wyd. 1 (2003), t. 5: [§39.1–39.3, s. 2](https://home.agh.edu.pl/~czapli/Resnick_5.pdf#page=18) — PDF z serwera AGH

← [Promieniowanie ciała doskonale czarnego](01-cialo-doskonale-czarne.md) · [spis modułu](README.md) · [Efekt Comptona](03-efekt-comptona.md) →

## Po co to jest

Światło wybija elektrony z metalu, ale tylko wtedy, gdy ma dostatecznie krótką falę, niezależnie od jasności. Fizyka falowa nie potrafiła tego wyjaśnić. Einstein w 1905 r. zaproponował, że światło składa się z fotonów o energii $hf$, i za to dostał Nagrodę Nobla. Na zjawisku fotoelektrycznym (zewnętrznym i wewnętrznym) działają fotopowielacze, czujniki w aparatach, ogniwa słoneczne, fotodiody w światłowodach i automatyczne drzwi. To najczęstszy temat fizyki kwantowej na maturze.

## Teoria w pigułce

**Obserwacje doświadczalne** (fotokomórka: oświetlona katoda, anoda, regulowane napięcie):
1. Elektrony są emitowane tylko wtedy, gdy częstotliwość światła przekracza **częstotliwość graniczną** $f_0$ zależną od metalu. Poniżej nie ma emisji nawet przy bardzo silnym świetle.
2. Maksymalna energia kinetyczna elektronów zależy liniowo od częstotliwości, a **nie** od natężenia światła.
3. Natężenie światła zwiększa tylko **liczbę** elektronów (prąd nasycenia).
4. Emisja zaczyna się natychmiast, nawet przy bardzo słabym świetle. Według teorii falowej elektron musiałby „zbierać” energię przez długi czas.

**Wyjaśnienie Einsteina.** Światło to strumień fotonów o energii $E = hf$. Jeden foton oddaje całą energię jednemu elektronowi. Elektron zużywa część na wyjście z metalu (**praca wyjścia** $W$), a resztę unosi jako energię kinetyczną:

$$hf = W + E_{k,\max}.$$

- Częstotliwość graniczna: $hf_0 = W$, a długość fali graniczna $\lambda_0 = hc/W$.
- Maksymalną energię kinetyczną mierzy się **napięciem hamowania** $U_h$, przy którym prąd zanika: $eU_h = E_{k,\max}$.
- Wykres $U_h(f)$ to prosta o nachyleniu $h/e$, niezależnie od metalu. Millikan zmierzył tak stałą Plancka (1916), chcąc obalić teorię Einsteina.

Przykładowe prace wyjścia: cez ok. 2,1 eV, sód 2,28 eV, cynk 4,3 eV, platyna 5,6 eV.

**Zjawisko fotoelektryczne wewnętrzne.** W półprzewodniku foton przenosi elektron z pasma walencyjnego do przewodnictwa (23). Na tym działają ogniwa słoneczne, fotodiody i matryce CMOS.

**Liczba fotonów.** Wiązka o mocy $P$ niesie $N = P/(hf)$ fotonów na sekundę. Wskaźnik laserowy 1 mW to ok. $3\cdot10^{15}$ fotonów na sekundę.

## Wzory i założenia

| Wzór | Znaczenie | Kiedy obowiązuje |
|---|---|---|
| $E = hf = hc/\lambda$ | energia fotonu | $hc \approx 1240\ \mathrm{eV\cdot nm}$ |
| $hf = W + E_{k,\max}$ | równanie Einsteina | jeden foton — jeden elektron |
| $eU_h = E_{k,\max}$ | napięcie hamowania | — |
| $f_0 = W/h$, $\lambda_0 = hc/W$ | próg fotoefektu | — |
| $N = P\lambda/(hc)$ | liczba fotonów na sekundę | wiązka monochromatyczna |

## Przykład rozwiązany

**Zadanie.** Sód ($W = 2{,}28\ \mathrm{eV}$) oświetlono światłem 400 nm. Oblicz energię fotonu, maksymalną energię kinetyczną elektronów, napięcie hamowania i długość fali graniczną. Czy wystąpi fotoefekt przy świetle 600 nm?

$E = 1240/400 \approx 3{,}10\ \mathrm{eV}$, $E_{k,\max} = 3{,}10 - 2{,}28 = 0{,}82\ \mathrm{eV}$, $U_h = 0{,}82\ \mathrm V$.

$\lambda_0 = 1240/2{,}28 \approx 544\ \mathrm{nm}$. Światło 600 nm ma fotony o energii 2,07 eV, za mało. Fotoefektu nie będzie, nawet przy bardzo silnym oświetleniu.

## Typowe pułapki

- **Silniejsze światło daje szybsze elektrony.** Daje więcej elektronów. Ich energię wyznacza częstotliwość.
- **Energia fotonu zależy od natężenia.** Energia pojedynczego fotonu to $hf$. Natężenie to liczba fotonów.
- **Wszystkie elektrony mają $E_{k,\max}$.** To energia najszybszych. Elektrony z głębszych warstw tracą więcej energii.
- **Napięcie hamowania w woltach = energia w dżulach.** Energia w eV liczbowo równa się napięciu hamowania w woltach. W dżulach trzeba pomnożyć przez $e$.
- **Mylenie $W$ z energią fotonu.** Praca wyjścia to cecha metalu, a energia fotonu to cecha światła.

## Doświadczenie / symulacja

**Diody LED a stała Plancka.** Dioda LED zaczyna świecić przy napięciu $U \approx hc/(e\lambda)$. Zmierz napięcie progowe (z charakterystyki $I(U)$, ekstrapolując liniową część do zera) dla diod czerwonej, żółtej, zielonej i niebieskiej o znanych długościach fali. Wykres $U$ od $1/\lambda$ jest prostą o nachyleniu $hc/e$. Wyznacz $h$. Zwykle wychodzi z dokładnością 10–20%.

**Symulacja PhET:** *Efekt fotoelektryczny* (*Photoelectric Effect*) — zmieniaj metal, długość fali, natężenie i napięcie, mierz prąd ([phet.colorado.edu/pl](https://phet.colorado.edu/pl/)).

**Python:** napięcie hamowania w funkcji częstotliwości dla kilku metali i wyznaczenie $h$ z „pomiarów”.

```python
import numpy as np
import matplotlib.pyplot as plt

h, e, c = 6.62607015e-34, 1.602176634e-19, 2.99792458e8
metale = {"cez": 2.1, "sód": 2.28, "cynk": 4.3}
f = np.linspace(4e14, 1.6e15, 200)
for nazwa, W in metale.items():
    U = h*f/e - W
    plt.plot(f/1e14, np.where(U > 0, U, np.nan), label=nazwa)
    print(f"{nazwa}: λ0 = {h*c/(W*e)*1e9:.0f} nm")
Ef = h*c/400e-9/e
print(f"sód, 400 nm: E = {Ef:.2f} eV, Ek_max = {Ef - 2.28:.2f} eV")

rng = np.random.default_rng(3)                     # symulowany pomiar Millikana dla sodu
fp = np.array([6.0, 7.0, 8.0, 9.0, 10.0])*1e14
Up = h*fp/e - 2.28 + rng.normal(0, 0.02, fp.size)
a, b = np.polyfit(fp, Up, 1)
print(f"z dopasowania: h = {a*e:.3e} J·s, W = {-b:.2f} eV")
plt.xlabel("f [10¹⁴ Hz]"); plt.ylabel("U_h [V]"); plt.legend(); plt.grid(True); plt.show()
```

## Zadania

### A. Poziom maturalny

1. Praca wyjścia cynku wynosi 4,3 eV. Czy światło widzialne wywoła fotoefekt w cynku? Jaka jest długość fali graniczna?

<details>
<summary>Odpowiedź</summary>

$\lambda_0 = 1240/4{,}3 \approx 288\ \mathrm{nm}$ (ultrafiolet). Światło widzialne nie wywoła fotoefektu.
</details>

2. Napięcie hamowania wynosi 1,5 V przy oświetleniu światłem 300 nm. Oblicz pracę wyjścia.

<details>
<summary>Odpowiedź</summary>

$E = 1240/300 \approx 4{,}13\ \mathrm{eV}$, $W = 4{,}13 - 1{,}5 \approx 2{,}6\ \mathrm{eV}$.
</details>

3. Jak zmieni się prąd fotokomórki i maksymalna energia elektronów, gdy natężenie światła wzrośnie dwukrotnie (przy tej samej barwie)?

<details>
<summary>Odpowiedź</summary>

Prąd nasycenia wzrośnie dwukrotnie, a maksymalna energia się nie zmieni.
</details>

4. Ile fotonów na sekundę emituje wskaźnik laserowy o mocy 1 mW i długości fali 650 nm?

<details>
<summary>Odpowiedź</summary>

$N = P\lambda/(hc) \approx 3{,}3\cdot10^{15}$.
</details>

### B. Poziom akademicki _(opcjonalnie — rozszerzenie z rachunkiem)_

1. Według teorii falowej elektron w atomie (powierzchnia ok. $10^{-20}\ \mathrm{m^2}$) zbiera energię ze światła o natężeniu $10^{-3}\ \mathrm{W/m^2}$. Ile czasu potrzebowałby, żeby zebrać 2 eV? Co pokazuje doświadczenie?

<details>
<summary>Odpowiedź</summary>

Moc $10^{-23}\ \mathrm W$, czas $3{,}2\cdot10^{-19}/10^{-23} \approx 3\cdot10^4\ \mathrm s$, czyli ok. 9 godzin. Doświadczalnie emisja zaczyna się w czasie krótszym niż $10^{-9}$ s, co potwierdza obraz fotonowy.
</details>

2. Pokaż, że foton nie może zostać całkowicie pochłonięty przez **swobodny** elektron (z zachowaniem energii i pędu). Dlaczego w metalu jest to możliwe?

<details>
<summary>Odpowiedź</summary>

Z $hf + mc^2 = \sqrt{(pc)^2 + m^2c^4}$ i $p = hf/c$ wynika $(hf + mc^2)^2 = (hf)^2 + m^2c^4$, czyli $2hfmc^2 = 0$. Sprzeczność. W metalu część pędu przejmuje sieć krystaliczna (jony).
</details>

## Źródła

- OpenStax, *Fizyka dla szkół wyższych*, t. 3, rozdz. 6 — §6.2: efekt fotoelektryczny.
- Halliday, Resnick, Walker, *Podstawy fizyki* — wyd. 2015: t. 5, §38.1–38.2; wyd. 1: t. 5, §39.1–39.3.
- Symulacja PhET *Efekt fotoelektryczny*.
