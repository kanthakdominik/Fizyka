# 15.06 — Prąd przemienny: wartości skuteczne, impedancja, rezonans, moc

> **Moduł:** [15 — Indukcja elektromagnetyczna i prąd przemienny](README.md) · **Poziom:** 🟢🔵 matura R + studia · **Status:** ✅ pełny
>
> **Czytaj:**
>
> - OpenStax, *Fizyka dla szkół wyższych*, t. 2, rozdz. 15: [§15.1–15.5](https://openstax.org/books/fizyka-dla-szk%C3%B3%C5%82-wy%C5%BCszych-tom-2/pages/15-1-zrodla-pradu-zmiennego) · [wstęp do rozdziału](https://openstax.org/books/fizyka-dla-szk%C3%B3%C5%82-wy%C5%BCszych-tom-2/pages/15-wstep)
> - Halliday, Resnick, Walker, *Podstawy fizyki*, wyd. 2015, t. 3: §31.3–31.5 (s. 389)
> - Halliday, Resnick, Walker, *Podstawy fizyki*, wyd. 1 (2003), t. 3: §33.6–33.10, s. 330 (skan t. 3 na serwerze AGH kończy się na s. 127 — dalsze strony tylko w wydaniu papierowym)

← [Obwody RL, LC i RLC — drgania elektromagnetyczne](05-obwody-rl-lc-rlc.md) · [spis modułu](README.md) · [Transformator i przesył energii](07-transformator.md) →

## Po co to jest

W gniazdku płynie prąd przemienny 230 V, 50 Hz. Napięcie zmienia znak sto razy na sekundę, a jego szczytowa wartość to ok. 325 V. Prąd przemienny wygrał „wojnę prądów” dzięki transformatorom (15.07). Żeby liczyć obwody z cewkami i kondensatorami przy prądzie przemiennym, potrzebne są wartości skuteczne, reaktancje i impedancja, a do mocy współczynnik mocy. Rezonans szeregowy obwodu RLC wybiera jedną stację radiową spośród setek i pozwala budować filtry.

## Teoria w pigułce

**Napięcie sinusoidalne:** $u(t) = U_0\sin\omega t$, $\omega = 2\pi f$.

**Wartość skuteczna** to wartość napięcia stałego, które w oporniku wydzieli tę samą średnią moc. Średnia z $\sin^2$ wynosi $\tfrac12$, więc

$$U_{\text{sk}} = \frac{U_0}{\sqrt2}, \qquad I_{\text{sk}} = \frac{I_0}{\sqrt2}.$$

Napięcie sieci 230 V to wartość skuteczna, a amplituda wynosi $230\sqrt2 \approx 325\ \mathrm V$. Mierniki pokazują wartości skuteczne.

**Elementy w obwodzie prądu przemiennego:**

| Element | Opór dla prądu przemiennego | Faza prądu względem napięcia |
|---|---|---|
| opornik $R$ | $R$ | zgodna |
| cewka $L$ | reaktancja indukcyjna $X_L = \omega L$ | prąd **opóźnia się** o $90^\circ$ |
| kondensator $C$ | reaktancja pojemnościowa $X_C = \dfrac{1}{\omega C}$ | prąd **wyprzedza** o $90^\circ$ |

Cewka przepuszcza niskie częstotliwości i blokuje wysokie. Kondensator odwrotnie: blokuje prąd stały, a przepuszcza wysokie częstotliwości. Na tym opierają się filtry w zwrotnicach głośnikowych i zasilaczach.

**Obwód RLC szeregowy.** Napięcia na elementach mają różne fazy i dodaje się je jak wektory (**wskazy**, 09.06). Wynikowy „opór” to **impedancja**:

$$Z = \sqrt{R^2 + (X_L - X_C)^2}, \qquad I_{\text{sk}} = \frac{U_{\text{sk}}}{Z}, \qquad \tan\varphi = \frac{X_L - X_C}{R}.$$

**Rezonans:** dla $X_L = X_C$, czyli $\omega_0 = 1/\sqrt{LC}$, impedancja jest najmniejsza ($Z = R$), a prąd największy. Napięcia na cewce i kondensatorze mogą być wtedy wielokrotnie większe od napięcia zasilania (dobroć $Q$ razy), choć się wzajemnie znoszą. To drgania wymuszone z 09.05.

**Moc.** Średnią moc pobiera tylko opornik. Cewka i kondensator energię oddają z powrotem:

$$P = U_{\text{sk}}I_{\text{sk}}\cos\varphi = I_{\text{sk}}^2R.$$

$\cos\varphi$ to **współczynnik mocy**. Odbiorcy przemysłowi płacą dodatkowo za niski $\cos\varphi$, bo prąd płynący bez przenoszenia mocy i tak grzeje linie.

## Wzory i założenia

| Wzór | Znaczenie | Kiedy obowiązuje |
|---|---|---|
| $U_{\text{sk}} = U_0/\sqrt2$ | wartość skuteczna | przebieg sinusoidalny |
| $X_L = \omega L$, $X_C = 1/(\omega C)$ | reaktancje | — |
| $Z = \sqrt{R^2 + (X_L - X_C)^2}$ | impedancja RLC szeregowego | — |
| $\tan\varphi = (X_L - X_C)/R$ | przesunięcie fazy | — |
| $\omega_0 = 1/\sqrt{LC}$ | rezonans | — |
| $P = U_{\text{sk}}I_{\text{sk}}\cos\varphi$ | moc czynna | — |

## Przykład rozwiązany

**Zadanie.** Obwód szeregowy: $R = 100\ \Omega$, $L = 0{,}5\ \mathrm H$, $C = 10\ \mu\mathrm F$, zasilanie 230 V, 50 Hz. Oblicz reaktancje, impedancję, prąd, przesunięcie fazy i moc. Przy jakiej częstotliwości wystąpi rezonans i jakie napięcie będzie wtedy na cewce?

$X_L = 2\pi\cdot50\cdot0{,}5 \approx 157\ \Omega$, $X_C = \dfrac{1}{2\pi\cdot50\cdot10^{-5}} \approx 318\ \Omega$.

$Z = \sqrt{100^2 + (157 - 318)^2} \approx 190\ \Omega$, $I = 230/190 \approx 1{,}21\ \mathrm A$.

$\tan\varphi = -161/100 \Rightarrow \varphi \approx -58^\circ$. Obwód ma charakter pojemnościowy: prąd wyprzedza napięcie.

$P = I^2R \approx 147\ \mathrm W$, $\cos\varphi \approx 0{,}53$.

Rezonans: $f_0 = \dfrac{1}{2\pi\sqrt{0{,}5\cdot10^{-5}}} \approx 71\ \mathrm{Hz}$. Prąd wynosi wtedy $230/100 = 2{,}3\ \mathrm A$, a napięcie na cewce $I\omega_0L \approx 514\ \mathrm V$, ponad dwa razy więcej niż zasilanie.

### Wersja z rachunkiem różniczkowym i całkowym

**Wartość skuteczna jako całka:** $U_{\text{sk}}^2 = \dfrac1T\displaystyle\int_0^TU_0^2\sin^2\omega t\,dt = \dfrac{U_0^2}{2}$.

**Liczby zespolone.** Zapisując $u = \operatorname{Re}(U_0e^{i\omega t})$, otrzymujemy prawo Ohma dla impedancji zespolonych:

$$Z_R = R, \qquad Z_L = i\omega L, \qquad Z_C = \frac{1}{i\omega C}, \qquad Z = R + i\left(\omega L - \frac{1}{\omega C}\right).$$

Impedancje łączy się jak oporniki: szeregowo się dodają, równolegle dodaje się odwrotności. $\lvert Z\rvert$ to impedancja, a $\arg Z$ przesunięcie fazy. Tak liczy się każdy obwód prądu przemiennego, także z gałęziami równoległymi (kod poniżej).

## Typowe pułapki

- **230 V to amplituda.** To wartość skuteczna. Amplituda wynosi ok. 325 V, co ma znaczenie przy doborze kondensatorów i diod.
- **Napięcia na elementach dodają się arytmetycznie.** Dodają się wektorowo. Suma wartości skutecznych może przekraczać napięcie zasilania.
- **Cewka pobiera moc.** Idealna cewka i kondensator średnio nie pobierają mocy.
- **$X_C$ rośnie z częstotliwością.** Maleje: $X_C = 1/(\omega C)$. Rośnie $X_L$.
- **$\omega$ i $f$.** W reaktancjach jest $\omega = 2\pi f$, a nie $f$.

## Doświadczenie / symulacja

**Reaktancja kondensatora.** Transformator dzwonkowy (np. 12 V AC) zasila kondensator 10 μF przez opornik 100 Ω. Zmierz napięcia na oporniku i kondensatorze miernikiem AC. Sprawdź, że ich suma przekracza napięcie zasilania, a pierwiastek sumy kwadratów jest mu równy. Wyznacz $X_C$ i porównaj z $1/(\omega C)$. Nie podłączaj niczego bezpośrednio do sieci 230 V.

**Symulacja PhET:** *Zestaw do budowy obwodów AC* (*Circuit Construction Kit: AC*) — źródło przemienne, cewki i kondensatory z woltomierzem i wykresami.

**Python:** krzywa rezonansowa obwodu RLC liczona impedancjami zespolonymi.

```python
import numpy as np
import matplotlib.pyplot as plt

R, L, C, U = 100.0, 0.5, 10e-6, 230.0
f = np.linspace(10, 200, 2000)
w = 2*np.pi*f
Z = R + 1j*(w*L - 1/(w*C))
I = U/np.abs(Z)

w50 = 2*np.pi*50
Z50 = R + 1j*(w50*L - 1/(w50*C))
I50 = U/abs(Z50)
print(f"50 Hz: |Z| = {abs(Z50):.1f} Ω, I = {I50:.3f} A, φ = {np.degrees(np.angle(Z50)):.1f}°, P = {I50**2*R:.1f} W")
f0 = 1/(2*np.pi*np.sqrt(L*C))
print(f"rezonans f0 = {f0:.1f} Hz, I = {U/R:.2f} A, U_L = {U/R*2*np.pi*f0*L:.0f} V, Q = {2*np.pi*f0*L/R:.2f}")

# gałąź równoległa: (R + L) || C — impedancje jak oporniki
Zp = 1/(1/(R + 1j*w50*L) + 1j*w50*C)
print(f"(R + L) || C przy 50 Hz: |Z| = {abs(Zp):.1f} Ω, φ = {np.degrees(np.angle(Zp)):.1f}°")
plt.plot(f, I); plt.axvline(f0, ls="--", color="gray")
plt.xlabel("f [Hz]"); plt.ylabel("I_sk [A]"); plt.grid(True); plt.show()
```

## Zadania

### A. Poziom maturalny

1. Żelazko o mocy 1 kW zasilane jest napięciem 230 V. Oblicz wartość skuteczną i amplitudę prądu.

<details>
<summary>Odpowiedź</summary>

$I_{\text{sk}} \approx 4{,}35\ \mathrm A$, $I_0 \approx 6{,}15\ \mathrm A$.
</details>

2. Oblicz reaktancję cewki 0,2 H i kondensatora 50 μF przy 50 Hz i przy 500 Hz.

<details>
<summary>Odpowiedź</summary>

50 Hz: $X_L \approx 63\ \Omega$, $X_C \approx 64\ \Omega$. 500 Hz: $X_L \approx 628\ \Omega$, $X_C \approx 6{,}4\ \Omega$.
</details>

3. Dlaczego kondensator nie przepuszcza prądu stałego, a przepuszcza przemienny?

<details>
<summary>Odpowiedź</summary>

Przy prądzie stałym kondensator się ładuje i prąd ustaje. Przy przemiennym jest stale ładowany i rozładowywany, więc w obwodzie płynie prąd, choć ładunki nie przechodzą przez dielektryk. Reaktancja $1/(\omega C)$ dla $\omega \to 0$ dąży do nieskończoności.
</details>

### B. Poziom akademicki

1. Silnik pobiera z sieci 230 V prąd 5 A przy $\cos\varphi = 0{,}7$ (charakter indukcyjny). Oblicz moc czynną. Jaki kondensator podłączony równolegle podniesie $\cos\varphi$ do 1?

<details>
<summary>Odpowiedź</summary>

$P = 230\cdot5\cdot0{,}7 \approx 805\ \mathrm W$. Składowa bierna prądu: $5\sin\varphi \approx 3{,}57\ \mathrm A$. Kondensator musi pobierać tyle samo: $\omega CU = 3{,}57 \Rightarrow C \approx 49\ \mu\mathrm F$.
</details>

2. Pokaż, że w obwodzie RLC szeregowym średnia moc jest największa w rezonansie, a szerokość krzywej mocy w połowie wysokości wynosi $\Delta\omega = R/L$.

<details>
<summary>Odpowiedź</summary>

$P = U^2R/Z^2$ jest największa dla $Z = R$. Połowa mocy: $(X_L - X_C)^2 = R^2$, czyli $\omega L - 1/(\omega C) = \pm R$. Różnica dwóch dodatnich pierwiastków wynosi $R/L$ (porównaj $\Delta\omega = 2\beta$ w 09.05).
</details>

3. Filtr RC dolnoprzepustowy: napięcie wejściowe na szeregowym $R$ i $C$, wyjście z kondensatora. Wyznacz $\lvert U_{\text{wy}}/U_{\text{we}}\rvert$ w funkcji $\omega$ i częstotliwość graniczną (spadek do $1/\sqrt2$).

<details>
<summary>Odpowiedź</summary>

$\dfrac{U_{\text{wy}}}{U_{\text{we}}} = \dfrac{1/(i\omega C)}{R + 1/(i\omega C)} = \dfrac{1}{1 + i\omega RC}$, moduł $\dfrac{1}{\sqrt{1 + (\omega RC)^2}}$. Granica: $\omega = 1/(RC)$, czyli $f_g = 1/(2\pi RC)$.
</details>

## Źródła

- OpenStax, *Fizyka dla szkół wyższych*, t. 2, rozdz. 15 — §15.1–15.5: źródła prądu przemiennego, proste obwody AC, obwody RLC szeregowe, moc w obwodach AC, rezonans.
- Halliday, Resnick, Walker, *Podstawy fizyki* — wyd. 2015: t. 3, §31.3–31.5; wyd. 1: t. 3, §33.6–33.10.
- Symulacja PhET *Zestaw do budowy obwodów AC*.
