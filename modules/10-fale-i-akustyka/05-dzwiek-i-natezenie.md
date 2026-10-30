# 10.05 — Dźwięk: prędkość, natężenie, poziom w decybelach

> **Moduł:** [10 — Fale mechaniczne i akustyka](README.md) · **Poziom:** 🟢 matura R · **Status:** ✅ pełny
>
> **Czytaj:**
>
> - OpenStax, *Fizyka dla szkół wyższych*, t. 1, rozdz. 17: [§17.1–17.3](https://openstax.org/books/fizyka-dla-szk%C3%B3%C5%82-wy%C5%BCszych-tom-1/pages/17-1-fale-dzwiekowe) · [wstęp do rozdziału](https://openstax.org/books/fizyka-dla-szk%C3%B3%C5%82-wy%C5%BCszych-tom-1/pages/17-wstep)
> - Halliday, Resnick, Walker, *Podstawy fizyki*, wyd. 2015, t. 2: §17.1–17.2 (s. 200), §17.4 (s. 211)
> - Halliday, Resnick, Walker, *Podstawy fizyki*, wyd. 1 (2003), t. 2: [§18.1–18.3, s. 155](https://home.agh.edu.pl/~czapli/Resnick_2.pdf#page=171), [§18.5, s. 164](https://home.agh.edu.pl/~czapli/Resnick_2.pdf#page=180) — PDF z serwera AGH

← [Zasada Huygensa: odbicie, załamanie i dyfrakcja fal](04-huygens-dyfrakcja-zalamanie.md) · [spis modułu](README.md) · [Struny i piszczałki: mody własne, dudnienia](06-struny-rury-dudnienia.md) →

## Po co to jest

Dźwięk to fala podłużna, czyli drobne wahania ciśnienia powietrza. Ucho rejestruje je w ogromnym zakresie: najgłośniejszy znośny dźwięk ma natężenie $10^{12}$ razy większe niż najcichszy słyszalny. Dlatego głośność mierzy się w skali logarytmicznej, w decybelach. Ta wiedza jest potrzebna w ochronie słuchu i przepisach o hałasie, przy projektowaniu sal i ekranów akustycznych, a także do pracy z każdą skalą logarytmiczną (pH, magnitudo gwiazd, wzmocnienie w elektronice).

## Teoria w pigułce

**Fala dźwiękowa** to podłużna fala zagęszczeń i rozrzedzeń. Można ją opisać przez wychylenie cząsteczek powietrza $s(x, t) = s_m\cos(kx - \omega t)$ albo przez **zmianę ciśnienia** $\Delta p = \Delta p_m\sin(kx - \omega t)$. Amplitudy łączy wzór $\Delta p_m = \rho v\omega s_m$. Ciśnienie ma maksima tam, gdzie wychylenie jest zerowe (przesunięcie fazy o $90^\circ$).

**Zakres słyszalny** człowieka to ok. 20 Hz – 20 kHz. Poniżej leżą infradźwięki (słonie, trzęsienia ziemi), powyżej ultradźwięki (nietoperze, USG, czyszczenie ultradźwiękowe).

**Natężenie** to średnia moc przenoszona przez jednostkową powierzchnię prostopadłą do kierunku fali:

$$I = \frac{P}{S}, \qquad I = \frac{\Delta p_m^2}{2\rho v}.$$

Źródło punktowe promieniujące równomiernie we wszystkich kierunkach rozkłada moc na sferę: $I = \dfrac{P}{4\pi r^2}$. Natężenie maleje z kwadratem odległości.

**Poziom natężenia dźwięku** w decybelach:

$$L = 10\log_{10}\frac{I}{I_0}\ \mathrm{dB}, \qquad I_0 = 10^{-12}\ \mathrm{W/m^2}\ \text{(próg słyszalności przy 1 kHz)}.$$

- Każde 10 dB oznacza 10 razy większe natężenie.
- Podwojenie natężenia daje +3 dB.
- Podwojenie odległości od źródła punktowego daje −6 dB.
- Przykłady: szept ok. 20 dB, rozmowa ok. 60 dB, ruchliwa ulica ok. 80 dB, koncert rockowy ok. 110 dB, próg bólu ok. 120 dB. Długotrwały hałas powyżej ok. 85 dB uszkadza słuch.

**Głośność subiektywna** to coś innego niż natężenie. Ucho jest najczulsze przy 2–5 kHz, a dźwięk odbieramy jako „dwa razy głośniejszy” przy wzroście poziomu o ok. 10 dB.

## Wzory i założenia

| Wzór | Znaczenie | Kiedy obowiązuje |
|---|---|---|
| $\Delta p_m = \rho v\omega s_m$ | amplituda ciśnienia a amplituda wychylenia | fala harmoniczna |
| $I = \Delta p_m^2/(2\rho v)$ | natężenie fali dźwiękowej | j.w. |
| $I = P/(4\pi r^2)$ | źródło punktowe | brak odbić i pochłaniania |
| $L = 10\log(I/I_0)$ | poziom natężenia w dB | $I_0 = 10^{-12}\ \mathrm{W/m^2}$ |
| $L_2 - L_1 = 10\log(I_2/I_1) = 20\log(r_1/r_2)$ | różnica poziomów | źródło punktowe |

## Przykład rozwiązany

**Zadanie 1.** Głośnik o mocy akustycznej 1 W promieniuje równomiernie we wszystkich kierunkach. Oblicz natężenie i poziom dźwięku w odległości 10 m i 20 m.

$I_{10} = \dfrac{1}{4\pi\cdot100} \approx 8{,}0\cdot10^{-4}\ \mathrm{W/m^2}$, $L = 10\log(8{,}0\cdot10^8) \approx 89\ \mathrm{dB}$.

W odległości 20 m natężenie jest 4 razy mniejsze, czyli $L \approx 83\ \mathrm{dB}$ (−6 dB).

**Zadanie 2.** Jeden głośnik daje w danym miejscu 80 dB. Ile dadzą dwa takie głośniki, a ile dziesięć? Głośniki są niespójne, więc dodaje się natężenia.

Dwa: $80 + 10\log2 \approx 83\ \mathrm{dB}$. Dziesięć: $90\ \mathrm{dB}$.

**Zadanie 3.** Oblicz amplitudę zmian ciśnienia i amplitudę wychylenia cząsteczek powietrza dla tonu 1 kHz na progu bólu ($I = 1\ \mathrm{W/m^2}$) i na progu słyszalności ($\rho = 1{,}2\ \mathrm{kg/m^3}$).

$\Delta p_m = \sqrt{2\rho vI} \approx 29\ \mathrm{Pa}$ (ok. 0,03% ciśnienia atmosferycznego), $s_m = \Delta p_m/(\rho v\omega) \approx 11\ \mu\mathrm m$.

Na progu słyszalności: $\Delta p_m \approx 3\cdot10^{-5}\ \mathrm{Pa}$, $s_m \approx 10^{-11}\ \mathrm{m}$, czyli mniej niż rozmiar atomu.

## Typowe pułapki

- **Decybele się dodają.** Dodaje się natężenia, a nie poziomy. 80 dB + 80 dB to 83 dB, a nie 160 dB.
- **Dwa razy dalej = połowa natężenia.** Natężenie maleje czterokrotnie, czyli o 6 dB.
- **Decybel to jednostka natężenia.** To miara stosunku do wartości odniesienia.
- **Natężenie proporcjonalne do amplitudy.** Jest proporcjonalne do kwadratu amplitudy.
- **Ultradźwięki są głośne.** Są niesłyszalne niezależnie od natężenia, bo leżą poza zakresem częstotliwości ucha.

## Doświadczenie / symulacja

**Prawo odwrotnych kwadratów.** Ustaw telefon z generatorem tonu (1 kHz) na otwartej przestrzeni, a drugim telefonem z miernikiem poziomu dźwięku (phyphox, *Audio Amplitude*, po kalibracji) mierz poziom w odległościach 0,5; 1; 2; 4; 8 m. Narysuj $L$ od $\log r$. Nachylenie powinno wynosić −20 dB na dekadę. W pomieszczeniu odbicia od ścian zaburzą wynik, więc porównaj oba przypadki.

**Hałas w otoczeniu.** Zmierz poziom w kilku miejscach (pokój, ulica, autobus, słuchawki przy maksymalnej głośności przyłożone do mikrofonu) i porównaj z normami.

**Python:** poziom dźwięku od źródła punktowego i dodawanie źródeł.

```python
import numpy as np
import matplotlib.pyplot as plt

I0, P = 1e-12, 1.0
r = np.logspace(-0.5, 3, 200)
L = 10*np.log10(P/(4*np.pi*r**2)/I0)
plt.semilogx(r, L)
for d in (10, 20, 100):
    print(f"r = {d:4d} m: L = {10*np.log10(P/(4*np.pi*d**2)/I0):.1f} dB")

def suma_dB(*Ls):                      # źródła niespójne: dodajemy natężenia
    return 10*np.log10(sum(10**(l/10) for l in Ls))
print(f"80 dB + 80 dB = {suma_dB(80, 80):.1f} dB, 80 + 85 = {suma_dB(80, 85):.1f} dB, 10 × 80 = {suma_dB(*[80]*10):.1f} dB")
print(f"amplituda ciśnienia przy 1 W/m²: {np.sqrt(2*1.2*343*1):.1f} Pa")
plt.axhline(85, ls="--", color="r", label="85 dB — granica bezpiecznej ekspozycji")
plt.xlabel("r [m]"); plt.ylabel("L [dB]"); plt.grid(True, which="both"); plt.legend(); plt.show()
```

## Zadania

### A. Poziom maturalny

1. Poziom dźwięku wzrósł z 60 dB do 90 dB. Ile razy wzrosło natężenie?

<details>
<summary>Odpowiedź</summary>

$10^3 = 1000$ razy.
</details>

2. Na koncercie w odległości 3 m od głośnika poziom wynosi 100 dB. Oblicz moc akustyczną głośnika, przyjmując źródło punktowe.

<details>
<summary>Odpowiedź</summary>

$I = 10^{-2}\ \mathrm{W/m^2}$, $P = I\cdot4\pi r^2 \approx 1{,}1\ \mathrm{W}$.
</details>

3. Jak daleko od głośnika z przykładu 1 (89 dB w odległości 10 m) poziom spadnie do 60 dB?

<details>
<summary>Odpowiedź</summary>

$20\log(r/10) = 29 \Rightarrow r \approx 280\ \mathrm{m}$ (bez uwzględnienia pochłaniania w powietrzu).
</details>

4. Dwa źródła dają w danym miejscu 80 dB i 85 dB. Jaki jest poziom łączny?

<details>
<summary>Odpowiedź</summary>

$10\log(10^8 + 10^{8{,}5}) \approx 86{,}2\ \mathrm{dB}$.
</details>

### B. Poziom akademicki _(opcjonalnie — rozszerzenie z rachunkiem)_

1. Wyprowadź związek $\Delta p_m = \rho v\omega s_m$ z definicji modułu ściśliwości $\Delta p = -K\,\dfrac{\Delta V}{V}$ i wzoru $v = \sqrt{K/\rho}$.

<details>
<summary>Odpowiedź</summary>

Dla warstwy powietrza $\Delta V/V = \partial s/\partial x$, więc $\Delta p = -K\,\partial s/\partial x = -K(-ks_m)\sin(kx - \omega t)$. Amplituda wynosi $Kks_m = \rho v^2\cdot\dfrac{\omega}{v}s_m = \rho v\omega s_m$.
</details>

2. Pokaż, że $I = \Delta p_m^2/(2\rho v)$. Natężenie to średnia z iloczynu $\Delta p\cdot\partial s/\partial t$.

<details>
<summary>Odpowiedź</summary>

$\Delta p\cdot\dot s = \Delta p_m\sin(\cdot)\cdot\omega s_m\sin(\cdot)$, średnio $\tfrac12\Delta p_m\omega s_m = \tfrac12\Delta p_m\cdot\Delta p_m/(\rho v)$.
</details>

3. Powietrze pochłania dźwięk 4 kHz w tempie ok. 0,03 dB/m. Porównaj spadek poziomu na odcinku od 10 m do 1 km wynikający z rozchodzenia się sferycznego i z pochłaniania.

<details>
<summary>Odpowiedź</summary>

Rozchodzenie sferyczne: $20\log100 = 40\ \mathrm{dB}$. Pochłanianie: $0{,}03\cdot990 \approx 30\ \mathrm{dB}$. Na dużych odległościach pochłanianie jest porównywalne z geometrią i silniej tłumi wysokie tony, dlatego daleka burza tylko dudni.
</details>

## Źródła

- OpenStax, *Fizyka dla szkół wyższych*, t. 1, rozdz. 17 — §17.1 (fale dźwiękowe), §17.2 (prędkość dźwięku), §17.3 (natężenie dźwięku).
- Halliday, Resnick, Walker, *Podstawy fizyki* — wyd. 2015: t. 2, §17.1–17.2, §17.4; wyd. 1: t. 2, §18.1–18.3, §18.5.
