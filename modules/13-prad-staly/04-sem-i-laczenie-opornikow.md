# 13.04 — SEM, opór wewnętrzny, łączenie oporników

> **Moduł:** [13 — Prąd stały](README.md) · **Poziom:** 🟢 matura R · **Status:** ✅ pełny
>
> **Czytaj:**
>
> - OpenStax, *Fizyka dla szkół wyższych*, t. 2, rozdz. 10: [§10.1–10.2](https://openstax.org/books/fizyka-dla-szk%C3%B3%C5%82-wy%C5%BCszych-tom-2/pages/10-1-sila-elektromotoryczna) · [wstęp do rozdziału](https://openstax.org/books/fizyka-dla-szk%C3%B3%C5%82-wy%C5%BCszych-tom-2/pages/10-wstep)
> - Halliday, Resnick, Walker, *Podstawy fizyki*, wyd. 2015, t. 3: §27.1–27.2 (s. 210)
> - Halliday, Resnick, Walker, *Podstawy fizyki*, wyd. 1 (2003), t. 3: §28.1–28.5, s. 155 (skan t. 3 na serwerze AGH kończy się na s. 127 — dalsze strony tylko w wydaniu papierowym)

← [Praca i moc prądu](03-praca-i-moc-pradu.md) · [spis modułu](README.md) · [Prawa Kirchhoffa i mierniki](05-prawa-kirchhoffa.md) →

## Po co to jest

Bateria nie jest idealnym źródłem napięcia. Ma opór wewnętrzny, przez który napięcie spada przy dużym obciążeniu: światła samochodu przygasają przy uruchamianiu rozrusznika. Łączenie oporników w szereg i równolegle to codzienność elektroniki: dzielniki napięcia, instalacja domowa (wszystkie odbiorniki równolegle), łańcuchy LED. Warunek dopasowania $R = r$ mówi, kiedy źródło oddaje największą moc, co ma znaczenie w głośnikach, antenach i panelach fotowoltaicznych.

## Teoria w pigułce

**Siła elektromotoryczna (SEM)** $\varepsilon$ to praca, jaką źródło (bateria, prądnica, ogniwo słoneczne) wykonuje nad jednostkowym ładunkiem, przenosząc go „pod górę” potencjału. Jednostką jest wolt. To napięcie źródła, przez które nie płynie prąd.

**Opór wewnętrzny** $r$ to opór samego źródła. Gdy płynie prąd $I$, napięcie na zaciskach wynosi:

$$U = \varepsilon - Ir, \qquad I = \frac{\varepsilon}{R + r}.$$

- Bez obciążenia ($I = 0$): $U = \varepsilon$.
- Zwarcie ($R = 0$): $I_{\text{zw}} = \varepsilon/r$. Prąd jest ograniczony tylko oporem wewnętrznym, co jest niebezpieczne dla akumulatorów o małym $r$.

**Moc oddawana do odbiornika** $P = I^2R = \dfrac{\varepsilon^2R}{(R + r)^2}$ jest największa, gdy $R = r$ (**dopasowanie**). Wynosi wtedy $\varepsilon^2/(4r)$, a sprawność $\eta = R/(R + r)$ to tylko 50%. W sieci energetycznej dąży się do wysokiej sprawności, więc $R \gg r$. Dopasowanie stosuje się tam, gdzie liczy się moc z małego sygnału.

**Łączenie oporników:**
- **Szeregowo**: ten sam prąd, napięcia się sumują: $R = R_1 + R_2 + \dots$ Napięcie dzieli się proporcjonalnie do oporów (**dzielnik napięcia**: $U_1 = U\dfrac{R_1}{R_1 + R_2}$).
- **Równolegle**: to samo napięcie, prądy się sumują: $\dfrac1R = \dfrac1{R_1} + \dfrac1{R_2} + \dots$ Opór zastępczy jest mniejszy od najmniejszego z oporów. Dla dwóch: $R = \dfrac{R_1R_2}{R_1 + R_2}$.

**Łączenie ogniw:**
- szeregowo: $\varepsilon = \sum\varepsilon_i$, $r = \sum r_i$ (baterie w latarce);
- równolegle (jednakowe ogniwa): $\varepsilon$ bez zmian, $r$ maleje $n$ razy, więc można pobrać większy prąd.

## Wzory i założenia

| Wzór | Znaczenie | Kiedy obowiązuje |
|---|---|---|
| $U = \varepsilon - Ir$ | napięcie na zaciskach | źródło rozładowywane |
| $I = \varepsilon/(R + r)$ | prąd w obwodzie z jednym źródłem | — |
| $P_{\max} = \varepsilon^2/(4r)$ dla $R = r$ | dopasowanie mocy | — |
| $R = R_1 + R_2 + \dots$ | połączenie szeregowe | — |
| $1/R = 1/R_1 + 1/R_2 + \dots$ | połączenie równoległe | — |
| $U_1 = UR_1/(R_1 + R_2)$ | dzielnik napięcia | bez obciążenia wyjścia |

## Przykład rozwiązany

**Zadanie 1.** Bateria 9 V ma opór wewnętrzny 1 Ω i zasila opornik 8 Ω. Oblicz prąd, napięcie na zaciskach i moc na oporniku. Przy jakim oporze moc byłaby największa?

$I = 9/(8 + 1) = 1\ \mathrm A$, $U = 9 - 1 = 8\ \mathrm V$, $P = 8\ \mathrm W$.

Największa moc przy $R = 1\ \Omega$: $P = 81/4 \approx 20\ \mathrm W$. Bateria równie mocno grzeje się wtedy od środka.

**Zadanie 2.** Akumulator samochodowy ma SEM 12,6 V i opór wewnętrzny 0,02 Ω. Rozrusznik pobiera 150 A. Jakie napięcie mają w tym czasie reflektory?

$U = 12{,}6 - 150\cdot0{,}02 = 9{,}6\ \mathrm V$. Reflektory wyraźnie przygasają.

## Typowe pułapki

- **SEM = napięcie na zaciskach.** Są równe tylko wtedy, gdy nie płynie prąd.
- **Równolegle opory się dodają.** Dodają się odwrotności. Wynik jest mniejszy od najmniejszego oporu.
- **Wzór na dwa oporniki równoległe dla trzech.** $R_1R_2/(R_1 + R_2)$ działa tylko dla dwóch. Dla trzech trzeba sumować odwrotności (albo łączyć parami).
- **Dzielnik pod obciążeniem.** Wzór na dzielnik zakłada, że do wyjścia nic nie podłączono. Obciążenie łączy się równolegle z dolnym opornikiem i zmienia wynik.
- **Ogniwa równolegle dają wyższe napięcie.** Dają to samo napięcie i mniejszy opór wewnętrzny.

## Doświadczenie / symulacja

**SEM i opór wewnętrzny baterii.** Podłącz do baterii 4,5 V kolejno oporniki 2–20 Ω (lub żarówki) i mierz napięcie na zaciskach i prąd. Wykres $U(I)$ jest prostą: przecięcie z osią $U$ daje $\varepsilon$, a nachylenie $-r$. Powtórz dla baterii zużytej. Jej opór wewnętrzny jest wyraźnie większy.

**Symulacja PhET:** *Zestaw do budowy obwodów DC* — buduj układy szeregowe i równoległe, włącz opór wewnętrzny baterii w ustawieniach.

**Python:** moc i sprawność w funkcji oporu obciążenia oraz opór zastępczy sieci.

```python
import numpy as np
import matplotlib.pyplot as plt

eps, r = 9.0, 1.0
R = np.linspace(0.01, 10, 500)
P = eps**2*R/(R + r)**2
eta = R/(R + r)
print(f"maksimum mocy {P.max():.2f} W przy R = {R[np.argmax(P)]:.2f} Ω (teoria: {eps**2/(4*r):.2f} W przy R = r)")

par = lambda *Rs: 1/sum(1/x for x in Rs)
print(f"2 || 3 || 6 = {par(2, 3, 6):.3f} Ω, (2 + 4) || 3 = {par(2 + 4, 3):.3f} Ω")
# drabinka nieskończona: R_ekw = R + (R || R_ekw) → R_ekw = R(1 + √5)/2
Rek = 1.0
for _ in range(30):
    Rek = 1 + par(1, Rek)
print(f"nieskończona drabinka z oporników 1 Ω: {Rek:.5f} Ω ((1 + √5)/2 = {(1 + np.sqrt(5))/2:.5f})")

fig, ax = plt.subplots()
ax.plot(R, P, label="P [W]"); ax.plot(R, eta*P.max(), "--", label="sprawność (skala)")
ax.set_xlabel("R [Ω]"); ax.grid(True); ax.legend(); plt.show()
```

## Zadania

### A. Poziom maturalny

1. Oblicz opór zastępczy oporników 2 Ω, 3 Ω i 6 Ω połączonych szeregowo oraz równolegle.

<details>
<summary>Odpowiedź</summary>

11 Ω i 1 Ω.
</details>

2. Bateria przy prądzie 1 A ma na zaciskach 4,0 V, a przy prądzie 2,25 A ma 3,375 V. Oblicz SEM i opór wewnętrzny.

<details>
<summary>Odpowiedź</summary>

$r = \dfrac{4{,}0 - 3{,}375}{2{,}25 - 1} = 0{,}5\ \Omega$, $\varepsilon = 4{,}0 + 1\cdot0{,}5 = 4{,}5\ \mathrm V$.
</details>

3. Dzielnik napięcia z oporników 10 kΩ i 5 kΩ zasilany jest napięciem 12 V. Jakie napięcie jest na oporniku 5 kΩ? Jak zmieni się ono po podłączeniu do niego odbiornika 5 kΩ?

<details>
<summary>Odpowiedź</summary>

4 V; po podłączeniu dolna część ma 2,5 kΩ i napięcie spada do $12\cdot2{,}5/12{,}5 = 2{,}4\ \mathrm V$.
</details>

4. Dlaczego odbiorniki w mieszkaniu łączy się równolegle, a nie szeregowo?

<details>
<summary>Odpowiedź</summary>

Każdy dostaje pełne napięcie sieci i działa niezależnie od pozostałych. Przy połączeniu szeregowym wyłączenie jednego przerywa obwód wszystkich.
</details>

### B. Poziom akademicki _(opcjonalnie — rozszerzenie z rachunkiem)_

1. Wyprowadź warunek $R = r$, różniczkując $P(R) = \dfrac{\varepsilon^2R}{(R + r)^2}$.

<details>
<summary>Odpowiedź</summary>

$\dfrac{dP}{dR} = \varepsilon^2\dfrac{(R + r) - 2R}{(R + r)^3} = 0 \Rightarrow R = r$.
</details>

2. Nieskończona drabinka składa się z oporników $R$ (jeden w gałęzi poziomej, jeden w poprzecznej, i tak dalej). Wyznacz opór zastępczy.

<details>
<summary>Odpowiedź</summary>

Dodanie jednego ogniwa nie zmienia wyniku: $R_e = R + \dfrac{RR_e}{R + R_e}$, stąd $R_e^2 - RR_e - R^2 = 0$ i $R_e = R\dfrac{1 + \sqrt5}{2} \approx 1{,}618R$ (złota proporcja).
</details>

3. $n$ jednakowych ogniw ($\varepsilon$, $r$) łączy się w $m$ gałęzi równoległych po $n/m$ ogniw szeregowo i zasila opór $R$. Pokaż, że prąd jest największy, gdy opór wewnętrzny baterii równa się $R$.

<details>
<summary>Odpowiedź</summary>

SEM baterii $\varepsilon n/m$, opór wewnętrzny $\dfrac{(n/m)r}{m} = \dfrac{nr}{m^2}$. $I = \dfrac{\varepsilon n/m}{R + nr/m^2}$. Maksimum względem $m$ daje $R = nr/m^2$.
</details>

## Źródła

- OpenStax, *Fizyka dla szkół wyższych*, t. 2, rozdz. 10 — §10.1 (siła elektromotoryczna) i §10.2 (łączenie oporników).
- Halliday, Resnick, Walker, *Podstawy fizyki* — wyd. 2015: t. 3, §27.1–27.2; wyd. 1: t. 3, §28.1–28.5.
- Symulacja PhET *Zestaw do budowy obwodów DC*.
