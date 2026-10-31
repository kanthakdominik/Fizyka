# 13.03 — Praca i moc prądu

> **Moduł:** [13 — Prąd stały](README.md) · **Poziom:** 🟢 matura R · **Status:** ✅ pełny
>
> **Czytaj:**
>
> - OpenStax, *Fizyka dla szkół wyższych*, t. 2, rozdz. 9: [§9.5](https://openstax.org/books/fizyka-dla-szk%C3%B3%C5%82-wy%C5%BCszych-tom-2/pages/9-5-energia-i-moc-elektryczna) · [wstęp do rozdziału](https://openstax.org/books/fizyka-dla-szk%C3%B3%C5%82-wy%C5%BCszych-tom-2/pages/9-wstep)
> - Halliday, Resnick, Walker, *Podstawy fizyki*, wyd. 2015, t. 3: §26.5 (s. 196)
> - Halliday, Resnick, Walker, *Podstawy fizyki*, wyd. 1 (2003), t. 3: §27.7, s. 144 (skan t. 3 na serwerze AGH kończy się na s. 127 — dalsze strony tylko w wydaniu papierowym)

← [Opór, opór właściwy i prawo Ohma](02-opor-i-prawo-ohma.md) · [spis modułu](README.md) · [SEM, opór wewnętrzny, łączenie oporników](04-sem-i-laczenie-opornikow.md) →

## Po co to jest

Rachunek za prąd płaci się za energię w kilowatogodzinach. Moc urządzenia decyduje o tym, ile prądu pobiera i czy wytrzyma bezpiecznik. Ciepło Joule'a grzeje czajnik, kuchenkę i żelazko, a w przewodach i procesorach jest stratą, którą trzeba odprowadzić. Ten sam wzór wyjaśnia, dlaczego energię przesyła się liniami o napięciu setek kilowoltów.

## Teoria w pigułce

**Praca prądu.** Ładunek $q$ przechodzący przez różnicę potencjałów $U$ traci energię $qU$ (12.05). W czasie $t$ przy prądzie $I$ przepływa $q = It$:

$$W = UIt, \qquad P = UI.$$

W oporniku cała ta energia zamienia się w ciepło (**ciepło Joule'a**). Elektrony przyspieszane polem oddają energię sieci krystalicznej przy zderzeniach (13.01). Korzystając z $U = IR$:

$$P = UI = I^2R = \frac{U^2}{R}.$$

- Przy **stałym prądzie** (połączenie szeregowe) więcej ciepła wydziela się na **większym** oporze ($I^2R$).
- Przy **stałym napięciu** (połączenie równoległe, gniazdka w domu) więcej mocy pobiera **mniejszy** opór ($U^2/R$).

**Kilowatogodzina:** $1\ \mathrm{kWh} = 1000\ \mathrm W\cdot3600\ \mathrm s = 3{,}6\ \mathrm{MJ}$.

**Przesył energii.** Elektrownia oddaje moc $P = UI$. Straty w liniach o oporze $R_l$ wynoszą

$$P_{\text{strat}} = I^2R_l = \left(\frac PU\right)^2R_l.$$

Podniesienie napięcia $n$ razy zmniejsza straty $n^2$ razy. Napięcie podwyższa się i obniża transformatorami (15), co jest głównym powodem stosowania prądu przemiennego.

**Sprawność** odbiornika to stosunek mocy użytecznej do pobranej. Silnik elektryczny ma do ok. 95%, a żarówka tradycyjna zamienia na światło zaledwie kilka procent mocy.

## Wzory i założenia

| Wzór | Znaczenie | Kiedy obowiązuje |
|---|---|---|
| $P = UI$ | moc prądu | każdy odbiornik |
| $P = I^2R = U^2/R$ | moc cieplna | opornik |
| $W = Pt = UIt$ | energia | moc stała w czasie |
| $W = \int P\,dt$ | energia | moc zmienna |
| $1\ \mathrm{kWh} = 3{,}6\cdot10^6\ \mathrm J$ | jednostka rozliczeniowa | — |
| $P_{\text{strat}} = (P/U)^2R_l$ | straty przesyłu | — |

## Przykład rozwiązany

**Zadanie 1.** Czajnik ma moc 2 kW przy 230 V. Oblicz prąd, opór grzałki i koszt gotowania przez 5 minut dziennie przez rok (przyjmij 1 zł za kWh).

$I = P/U \approx 8{,}7\ \mathrm A$. $R = U^2/P \approx 26{,}5\ \Omega$. Energia: $2\ \mathrm{kW}\cdot\tfrac{5}{60}\ \mathrm h\cdot365 \approx 61\ \mathrm{kWh}$, czyli ok. 61 zł rocznie.

**Zadanie 2.** Elektrownia przesyła 1 MW linią o oporze 5 Ω. Oblicz straty przy napięciu 10 kV i 400 kV.

Przy 10 kV: $I = 100\ \mathrm A$, $P_{\text{strat}} = 100^2\cdot5 = 50\ \mathrm{kW}$, czyli 5%.

Przy 400 kV: $I = 2{,}5\ \mathrm A$, $P_{\text{strat}} \approx 31\ \mathrm W$. Straty są 1600 razy mniejsze.

## Typowe pułapki

- **„Większy opór — większa moc”.** Zależy od tego, co jest stałe. Przy stałym napięciu (gniazdko) większą moc ma mniejszy opór.
- **Straty przesyłu jako $U^2/R_l$.** $U$ to napięcie linii względem ziemi, a nie spadek napięcia na linii. Straty trzeba liczyć z prądu: $I^2R_l$.
- **kW i kWh.** kW to moc, kWh energia. Urządzenie 2 kW pracujące pół godziny zużywa 1 kWh.
- **Żarówki w szeregu świecą jak osobno.** Dwie jednakowe żarówki 230 V połączone szeregowo przy 230 V świecą słabo: każda ma cztery razy mniejszą moc niż podłączona osobno, a razem pobierają połowę (przy stałym oporze).
- **Moc znamionowa przy innym napięciu.** Przy napięciu $U$ odbiornik o mocy $P_n$ przy $U_n$ ma moc $P_n(U/U_n)^2$, przy stałym oporze.

## Doświadczenie / symulacja

**Licznik zużycia energii.** Watomierzem gniazdkowym zmierz pobór mocy kilku urządzeń (ładowarka, laptop, czajnik, telewizor w trybie czuwania). Oblicz roczne zużycie i koszt. Sprawdź, ile kosztuje tryb czuwania wszystkich urządzeń w domu przez rok.

**Sprawność czajnika.** Zmierz czas zagotowania 1 kg wody i porównaj ciepło $mc\Delta T$ (11.02) z energią elektryczną $Pt$.

**Python:** straty przesyłu w funkcji napięcia linii.

```python
import numpy as np
import matplotlib.pyplot as plt

P, Rl = 1e6, 5.0
U = np.logspace(4, 6, 200)                        # od 10 kV (przy niższych napięciach model traci sens)
straty = (P/U)**2*Rl
for u in (1e4, 3e4, 1.1e5, 4e5):
    print(f"U = {u/1e3:6.0f} kV: I = {P/u:8.1f} A, straty = {(P/u)**2*Rl:10.1f} W ({(P/u)**2*Rl/P*100:.4f} %)")
print(f"czajnik 2 kW, 5 min dziennie przez rok: {2*5/60*365:.0f} kWh")
plt.loglog(U/1e3, straty/P*100)
plt.xlabel("napięcie linii [kV]"); plt.ylabel("straty [% mocy]"); plt.grid(True, which="both"); plt.show()
```

## Zadania

### A. Poziom maturalny

1. Żarówka LED pobiera 8 W i zastępuje tradycyjną żarówkę 60 W. Ile energii i pieniędzy oszczędza się w ciągu 1000 godzin świecenia (1 zł za kWh)?

<details>
<summary>Odpowiedź</summary>

52 kWh, czyli ok. 52 zł.
</details>

2. Dwie żarówki 230 V / 100 W połączono szeregowo i podłączono do 230 V. Jaką moc pobiera każda (przyjmij stały opór)?

<details>
<summary>Odpowiedź</summary>

$R = 529\ \Omega$ każda, $I = 230/1058 \approx 0{,}22\ \mathrm A$, $P = I^2R = 25\ \mathrm W$ każda.
</details>

3. Grzałkę 1000 W / 230 V podłączono do 115 V. Jaką ma moc?

<details>
<summary>Odpowiedź</summary>

250 W (przy stałym oporze moc maleje z kwadratem napięcia).
</details>

4. Bezpiecznik w obwodzie ma 16 A. Czy można jednocześnie włączyć czajnik 2,2 kW i grzejnik 2 kW (230 V)?

<details>
<summary>Odpowiedź</summary>

Prąd łączny $4200/230 \approx 18{,}3\ \mathrm A > 16\ \mathrm A$, więc bezpiecznik zadziała.
</details>

### B. Poziom akademicki _(opcjonalnie — rozszerzenie z rachunkiem)_

1. Kondensator $C$ naładowany do napięcia $U_0$ rozładowuje się przez opornik $R$: $I = \dfrac{U_0}{R}e^{-t/(RC)}$. Oblicz całkowite ciepło wydzielone w oporniku.

<details>
<summary>Odpowiedź</summary>

$Q = \displaystyle\int_0^\infty I^2R\,dt = \frac{U_0^2}{R}\cdot\frac{RC}{2} = \tfrac12CU_0^2$, czyli cała energia kondensatora, niezależnie od $R$.
</details>

2. Przewód o promieniu $r$ i długości $L$ przewodzi prąd $I$. Pokaż, że moc wydzielona na jednostkę objętości wynosi $J^2\rho = \sigma E^2$.

<details>
<summary>Odpowiedź</summary>

$P/V = I^2R/(AL) = I^2\rho L/(A\cdot AL) = (I/A)^2\rho = J^2\rho$, a $J = \sigma E$, więc $J^2\rho = \sigma E^2$.
</details>

3. Ile energii (w kWh i MJ) zużywa przez rok router o stałym poborze 10 W?

<details>
<summary>Odpowiedź</summary>

$10\cdot8760 = 87{,}6\ \mathrm{kWh} \approx 315\ \mathrm{MJ}$.
</details>

### C. Zadania z arkuszy maturalnych CKE

Zadania z egzaminów maturalnych (poziom rozszerzony, formuła 2023), w których ten temat jest potrzebny. Rozwiąż je samodzielnie, a potem porównaj z zasadami oceniania. Pełne zestawienie: [matura/README.md](../../matura/README.md).

- Maj 2023, zad. 8.2 — temperatura włókna żarówki 60 W / 230 V ([arkusz](https://cke.gov.pl/images/_EGZAMIN_MATURALNY_OD_2023/Arkusze_egzaminacyjne/2023/Fizyka/MFAP-R0-100-2305.pdf), [zasady oceniania](https://cke.gov.pl/images/_EGZAMIN_MATURALNY_OD_2023/Arkusze_egzaminacyjne/2023/Fizyka/MFAP-R0-100-2305-zasady.pdf))
- Maj 2024, zad. 7.2 — moc wydzielana na oporniku po przerwaniu gałęzi ([arkusz](https://cke.gov.pl/images/_EGZAMIN_MATURALNY_OD_2023/Arkusze_egzaminacyjne/2024/Fizyka/MFAP-R0-100-A-2405-arkusz.pdf), [zasady oceniania](https://cke.gov.pl/egzamin-maturalny/egzamin-maturalny-w-formule-2023/arkusze/2024-2/))

## Źródła

- OpenStax, *Fizyka dla szkół wyższych*, t. 2, rozdz. 9 — §9.5: energia elektryczna i moc.
- Halliday, Resnick, Walker, *Podstawy fizyki* — wyd. 2015: t. 3, §26.5; wyd. 1: t. 3, §27.7.
