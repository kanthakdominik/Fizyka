# 16.01 — Prąd przesunięcia i równania Maxwella

> **Moduł:** [16 — Równania Maxwella i fale elektromagnetyczne](README.md) · **Poziom:** 🔵 studia · **Status:** ✅ pełny
>
> **Czytaj:**
>
> - OpenStax, *Fizyka dla szkół wyższych*, t. 2, rozdz. 16: [§16.1](https://openstax.org/books/fizyka-dla-szk%C3%B3%C5%82-wy%C5%BCszych-tom-2/pages/16-1-rownania-maxwella-i-fale-elektromagnetyczne) · [wstęp do rozdziału](https://openstax.org/books/fizyka-dla-szk%C3%B3%C5%82-wy%C5%BCszych-tom-2/pages/16-wstep)
> - Halliday, Resnick, Walker, *Podstawy fizyki*, wyd. 2015, t. 3: §32.1–32.3 (s. 426)
> - Halliday, Resnick, Walker, *Podstawy fizyki*, wyd. 1 (2003), t. 3: §32.2, s. 290, §32.9–32.11, s. 306 (skan t. 3 na serwerze AGH kończy się na s. 127 — dalsze strony tylko w wydaniu papierowym)

← (początek modułu) · [spis modułu](README.md) · [Płaska fala elektromagnetyczna](02-fala-elektromagnetyczna.md) →

## Po co to jest

Cztery równania Maxwella streszczają całą elektryczność i magnetyzm z modułów 12–15. Maxwell dodał do nich jeden wyraz, **prąd przesunięcia**, i z tak uzupełnionych równań wywnioskował, że muszą istnieć fale elektromagnetyczne biegnące z prędkością $1/\sqrt{\mu_0\varepsilon_0}$, czyli z prędkością światła. Światło okazało się falą elektromagnetyczną. Z tej obserwacji wyrosły radio, telewizja, radar, telefonia komórkowa i Wi-Fi. Równania Maxwella są też punktem wyjścia szczególnej teorii względności (19).

## Teoria w pigułce

**Problem z prawem Ampère'a.** Podczas ładowania kondensatora przez przewód płynie prąd $I$, a między okładkami prąd nie płynie. Prawo Ampère'a $\oint\vec B\cdot d\vec l = \mu_0I$ daje różne wyniki dla tego samego konturu wokół przewodu, zależnie od tego, czy rozpięta na nim powierzchnia przecina przewód, czy przechodzi między okładkami. Coś jest niepełne.

**Prąd przesunięcia.** Między okładkami zmienia się pole elektryczne. Maxwell zdefiniował

$$I_d = \varepsilon_0\frac{d\Phi_E}{dt}.$$

Dla kondensatora płaskiego $\Phi_E = EA = q/\varepsilon_0$, więc $I_d = dq/dt = I$. Prąd przesunięcia „ciągnie dalej” prąd przewodzenia przez szczelinę. Zmienne pole elektryczne wytwarza pole magnetyczne tak samo jak prąd.

**Równania Maxwella** (postać całkowa, w próżni):

| Równanie | Postać | Znaczenie |
|---|---|---|
| prawo Gaussa | $\oint\vec E\cdot d\vec A = \dfrac{Q_{\text{wewn}}}{\varepsilon_0}$ | ładunki są źródłami pola elektrycznego (12.04) |
| prawo Gaussa dla magnetyzmu | $\oint\vec B\cdot d\vec A = 0$ | nie ma ładunków magnetycznych, linie $\vec B$ są zamknięte |
| prawo Faradaya | $\oint\vec E\cdot d\vec l = -\dfrac{d\Phi_B}{dt}$ | zmienne pole magnetyczne wytwarza pole elektryczne (15.02) |
| prawo Ampère'a–Maxwella | $\oint\vec B\cdot d\vec l = \mu_0I + \mu_0\varepsilon_0\dfrac{d\Phi_E}{dt}$ | prądy i zmienne pole elektryczne wytwarzają pole magnetyczne |

Do tego dochodzi siła Lorentza $\vec F = q(\vec E + \vec v\times\vec B)$, która mówi, jak pola działają na ładunki.

**Wniosek: fale.** Zmienne $\vec B$ wytwarza $\vec E$, a zmienne $\vec E$ wytwarza $\vec B$. Pola mogą się nawzajem podtrzymywać i rozchodzić bez ładunków i prądów. Z równań wynika równanie falowe (10.02) z prędkością

$$c = \frac{1}{\sqrt{\mu_0\varepsilon_0}} \approx 3{,}00\cdot10^8\ \mathrm{m/s}.$$

Maxwell obliczył tę wartość w 1864 r. ze stałych zmierzonych w doświadczeniach z ładunkami i prądami. Zgodność z prędkością światła nie była przypadkowa. Hertz w 1887 r. wytworzył i wykrył fale radiowe.

## Wzory i założenia

| Wzór | Znaczenie | Kiedy obowiązuje |
|---|---|---|
| $I_d = \varepsilon_0\,d\Phi_E/dt$ | prąd przesunięcia | — |
| $\oint\vec B\cdot d\vec l = \mu_0(I + I_d)$ | prawo Ampère'a–Maxwella | zawsze |
| $c = 1/\sqrt{\mu_0\varepsilon_0}$ | prędkość fal EM w próżni | — |
| cztery równania Maxwella | pełny opis pól | w materii z $\varepsilon_r$, $\mu_r$ i ładunkami/prądami swobodnymi |

## Przykład rozwiązany

### Wersja z rachunkiem różniczkowym i całkowym

**Zadanie.** Kondensator o kołowych okładkach o promieniu 5 cm ładuje się prądem 1 A. Oblicz tempo zmian pola elektrycznego oraz pole magnetyczne między okładkami w odległości 2,5 cm i 5 cm od osi.

$E = \dfrac{q}{\varepsilon_0\pi R^2}$, więc $\dfrac{dE}{dt} = \dfrac{I}{\varepsilon_0\pi R^2} \approx 1{,}4\cdot10^{13}\ \mathrm{\dfrac{V}{m\cdot s}}$.

Prawo Ampère'a–Maxwella dla okręgu o promieniu $r < R$ między okładkami (prądu przewodzenia brak):

$$B\cdot2\pi r = \mu_0\varepsilon_0\frac{d}{dt}(E\pi r^2) = \mu_0I\frac{r^2}{R^2} \Rightarrow B = \frac{\mu_0Ir}{2\pi R^2}.$$

Dla $r = 2{,}5\ \mathrm{cm}$: $B = 2\ \mu\mathrm T$. Dla $r = R$: $B = \mu_0I/(2\pi R) = 4\ \mu\mathrm T$, dokładnie tyle samo co wokół przewodu w tej odległości. Pole jest ciągłe, choć w szczelinie nie płyną żadne ładunki.

**Sprawdzenie wartości $c$:** $1/\sqrt{4\pi\cdot10^{-7}\cdot8{,}854\cdot10^{-12}} \approx 2{,}998\cdot10^8\ \mathrm{m/s}$.

## Typowe pułapki

- **Prąd przesunięcia to ruch ładunków.** To zmiana pola elektrycznego. Między okładkami w próżni ładunki nie płyną.
- **Pole $\vec B$ może mieć źródła.** Strumień $\vec B$ przez zamkniętą powierzchnię zawsze wynosi zero. Magnes przecięty na pół daje dwa magnesy, a nie osobne bieguny.
- **Prawo Faradaya tylko dla przewodów.** Indukowane pole elektryczne istnieje także w próżni.
- **Prąd przesunięcia jest pomijalny.** W obwodach o niskiej częstotliwości tak, ale to on umożliwia istnienie fal elektromagnetycznych.

## Doświadczenie / symulacja

**Fala z obwodu.** Każdy obwód ze zmiennym prądem promieniuje. Zbliż radio AM (lub odbiornik fal średnich w telefonie, jeśli jest) do włączonej świetlówki kompaktowej, ładowarki albo silnika wiertarki i posłuchaj trzasków i buczenia. To fale elektromagnetyczne z szybko zmiennych prądów.

**Symulacja PhET:** *Fale radiowe i pola elektromagnetyczne* (*Radio Waves & Electromagnetic Fields*) — elektron w antenie nadawczej porusza się w górę i w dół, a fala rozchodzi się do anteny odbiorczej ([phet.colorado.edu/pl](https://phet.colorado.edu/pl/)).

**Python:** pole magnetyczne w ładowanym kondensatorze i obok przewodu oraz wyznaczenie $c$ ze stałych.

```python
import numpy as np
import matplotlib.pyplot as plt

mu0, eps0 = 4e-7*np.pi, 8.8541878128e-12
I, R = 1.0, 0.05
print(f"c = 1/√(μ0 ε0) = {1/np.sqrt(mu0*eps0):.6e} m/s")
print(f"dE/dt = {I/(eps0*np.pi*R**2):.3e} V/(m·s)")
r = np.linspace(0, 0.15, 300)
B = np.where(r < R, mu0*I*r/(2*np.pi*R**2), mu0*I/(2*np.pi*np.maximum(r, 1e-9)))
for rv in (0.025, 0.05, 0.1):
    print(f"r = {rv*100:4.1f} cm: B = {np.interp(rv, r, B)*1e6:.2f} µT")
plt.plot(r*100, B*1e6); plt.axvline(R*100, ls="--", color="gray")
plt.xlabel("r [cm]"); plt.ylabel("B [µT]"); plt.title("pole między okładkami (prąd przesunięcia)"); plt.grid(True); plt.show()
```

## Zadania

### A. Poziom maturalny _(opcjonalnie — rozgrzewka)_

1. Które z równań Maxwella opisuje działanie prądnicy, a które mówi, że nie istnieją pojedyncze bieguny magnetyczne?

<details>
<summary>Odpowiedź</summary>

Prądnica: prawo Faradaya. Brak monopoli: prawo Gaussa dla magnetyzmu.
</details>

2. Oblicz prędkość fal elektromagnetycznych ze stałych $\mu_0 = 4\pi\cdot10^{-7}\ \mathrm{T\cdot m/A}$ i $\varepsilon_0 = 8{,}85\cdot10^{-12}\ \mathrm{F/m}$.

<details>
<summary>Odpowiedź</summary>

$c \approx 3{,}00\cdot10^8\ \mathrm{m/s}$.
</details>

### B. Poziom akademicki

1. Napięcie na kondensatorze płaskim (okładki o polu 0,01 m², odległe o 1 mm) rośnie w tempie $10^6\ \mathrm{V/s}$. Oblicz prąd przesunięcia.

<details>
<summary>Odpowiedź</summary>

$I_d = \varepsilon_0A\dfrac{dE}{dt} = \varepsilon_0\dfrac Ad\dfrac{dU}{dt} = C\dfrac{dU}{dt} \approx 88{,}5\ \mathrm{pF}\cdot10^6\ \mathrm{V/s} \approx 89\ \mu\mathrm A$.
</details>

2. Pokaż, że $\mu_0\varepsilon_0$ ma wymiar $\mathrm{s^2/m^2}$.

<details>
<summary>Odpowiedź</summary>

$[\mu_0] = \mathrm{N/A^2}$, $[\varepsilon_0] = \mathrm{C^2/(N\cdot m^2)}$. Iloczyn: $\mathrm{C^2/(A^2m^2)} = \mathrm{s^2/m^2}$.
</details>

3. Gdyby istniały ładunki magnetyczne, jak trzeba by zmienić drugie i trzecie równanie Maxwella? Uzasadnij przez symetrię.

<details>
<summary>Odpowiedź</summary>

$\oint\vec B\cdot d\vec A = \mu_0q_m$ (źródła pola magnetycznego) oraz $\oint\vec E\cdot d\vec l = -\dfrac{d\Phi_B}{dt} - \mu_0I_m$ (prąd magnetyczny wytwarzałby wirowe pole elektryczne). Równania stałyby się symetryczne. Takich ładunków dotąd nie znaleziono.
</details>

## Źródła

- OpenStax, *Fizyka dla szkół wyższych*, t. 2, rozdz. 16 — §16.1: równania Maxwella i fale elektromagnetyczne.
- Halliday, Resnick, Walker, *Podstawy fizyki* — wyd. 2015: t. 3, §32.1–32.3; wyd. 1: t. 3, §32.2, §32.9–32.11.
- Symulacja PhET *Fale radiowe i pola elektromagnetyczne*.
