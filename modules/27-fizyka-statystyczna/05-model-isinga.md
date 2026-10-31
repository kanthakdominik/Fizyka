# 27.05 — Model Isinga, przejścia fazowe i metoda Metropolisa

> **Moduł:** [27 — Fizyka statystyczna](README.md) · **Poziom:** 🔵 studia · **Status:** ✅ pełny
>
> **Czytaj:**
>
> - _Podręczniki główne nie mają osobnego paragrafu na ten temat — materiały są w sekcji „Źródła”._

← [Statystyki kwantowe: fermiony, bozony i promieniowanie cieplne](04-statystyki-kwantowe.md) · [spis modułu](README.md) · (koniec modułu) →

## Po co to jest

Woda zamarza w dokładnie 0°C, a żelazo traci namagnesowanie w dokładnie 770°C (temperatura Curie). Jak to możliwe, że miliardy cząsteczek „naraz” zmieniają zachowanie, choć każda oddziałuje tylko z kilkoma sąsiadami? Model Isinga to najprostszy model takiego **przejścia fazowego**: siatka strzałek (spinów), z których każda może być skierowana w górę lub w dół. Mimo prostoty pokazuje najważniejsze zjawiska fizyki materii skondensowanej: porządek, który znika w temperaturze krytycznej, fluktuacje na wszystkich skalach i uniwersalność. Symulacja metodą Monte Carlo (25.06) to klasyczne ćwiczenie fizyki obliczeniowej i dobry przykład, jak rozkład Boltzmanna (27.02) działa w praktyce.

## Teoria w pigułce

**Model.** Na kwadratowej siatce $L\times L$ w każdym węźle jest spin $s_i = \pm1$ (moment magnetyczny w górę lub w dół). Energia:

$$E = -J\sum_{\langle ij\rangle}s_is_j - h\sum_is_i,$$

gdzie pierwsza suma przebiega po parach najbliższych sąsiadów. Dla $J > 0$ sąsiednie spiny „wolą” być równoległe (ferromagnetyk), $h$ to zewnętrzne pole magnetyczne. Namagnesowanie (parametr porządku): $m = \dfrac1N\sum s_i$.

**Konkurencja energii i entropii.** W niskiej temperaturze wygrywa energia: wszystkie spiny równoległe, $\lvert m\rvert \approx 1$ (faza uporządkowana). W wysokiej wygrywa entropia (27.01): stanów nieuporządkowanych jest nieporównanie więcej, $m \approx 0$. Przejście zachodzi w **temperaturze krytycznej** $T_c$. Dla dwuwymiarowego modelu Onsager (1944) znalazł rozwiązanie dokładne:

$$kT_c = \frac{2J}{\ln(1 + \sqrt2)} \approx 2{,}269J, \qquad m(T) = \left[1 - \sinh^{-4}\left(\frac{2J}{kT}\right)\right]^{1/8}\ \text{dla } T < T_c.$$

W jednym wymiarze przejścia fazowego nie ma (Ising, 1925).

**Przybliżenie pola średniego.** Każdy spin „czuje” średnie pole od $z$ sąsiadów, $zJm$. Dla spinu w polu średni stan to $\tanh(\text{pole}/kT)$ (27.02), co daje równanie samouzgodnione

$$m = \tanh\frac{zJm + h}{kT}.$$

Dla $h = 0$ rozwiązanie niezerowe istnieje tylko dla $kT < zJ$, czyli $kT_c = 4J$ dla siatki kwadratowej — dwa razy za dużo w porównaniu z wynikiem Onsagera, ale jakościowo poprawnie. To model ferromagnetyzmu Weissa (14.07).

**Zjawiska krytyczne.** W pobliżu $T_c$:
- tworzą się obszary (domeny) uporządkowanych spinów wszystkich rozmiarów — fluktuacje sięgają całego układu;
- ciepło właściwe i podatność magnetyczna rosną gwałtownie (w nieskończonym układzie — do nieskończoności);
- namagnesowanie znika jak $(T_c - T)^\beta$, gdzie wykładnik $\beta$ jest **uniwersalny** — taki sam dla wielu różnych układów (2D Ising: $\beta = 1/8$; pole średnie: $\beta = 1/2$). Ten sam model opisuje punkt krytyczny ciecz–para (11.02) i stopy dwuskładnikowe.

**Metoda Metropolisa (1953).** Nie da się przejrzeć wszystkich $2^N$ stanów (dla $N = 1024$ to $10^{308}$), ale można wylosować stany z prawdopodobieństwem $\propto e^{-E/kT}$:
1. Wybierz spin i oblicz zmianę energii $\Delta E$ przy jego odwróceniu.
2. Jeśli $\Delta E \le 0$, odwróć go. Jeśli $\Delta E > 0$, odwróć z prawdopodobieństwem $e^{-\Delta E/kT}$.
3. Powtarzaj. Po dojściu do równowagi średnie po kolejnych konfiguracjach dają wielkości termodynamiczne.

Dla jednego spinu $\Delta E = 2s_i(J\sum_{\text{sąsiedzi}}s_j + h)$, więc obliczenia są bardzo szybkie.

## Wzory i założenia

| Wzór | Znaczenie | Kiedy obowiązuje |
|---|---|---|
| $E = -J\sum_{\langle ij\rangle}s_is_j - h\sum s_i$ | energia modelu Isinga | spiny $\pm1$, oddziaływanie najbliższych sąsiadów |
| $kT_c = 2J/\ln(1 + \sqrt2) \approx 2{,}269J$ | temperatura krytyczna (Onsager) | 2D, siatka kwadratowa, $h = 0$ |
| $m = [1 - \sinh^{-4}(2J/kT)]^{1/8}$ | namagnesowanie spontaniczne | 2D, $T < T_c$ |
| $m = \tanh\dfrac{zJm + h}{kT}$, $kT_c = zJ$ | przybliżenie pola średniego | $z$ — liczba sąsiadów |
| $P_{\text{akcept}} = \min(1, e^{-\Delta E/kT})$ | krok Metropolisa | równowaga, rozkład Boltzmanna |
| $C = \dfrac{\langle E^2\rangle - \langle E\rangle^2}{kT^2}$ | ciepło właściwe z fluktuacji | zespół kanoniczny |

## Przykład rozwiązany

**Zadanie 1.** Spin w środku siatki ma trzech sąsiadów skierowanych w górę i jednego w dół. Sam jest skierowany w dół. Oblicz zmianę energii przy jego odwróceniu ($h = 0$) i prawdopodobieństwo akceptacji w temperaturze $kT = 2J$.

Suma sąsiadów: $3 - 1 = 2$. $\Delta E = 2s_iJ\sum s_j = 2\cdot(-1)\cdot J\cdot2 = -4J < 0$ — odwrócenie obniża energię, więc zawsze je akceptujemy. Odwrotny ruch (z góry na dół) ma $\Delta E = +4J$ i prawdopodobieństwo $e^{-2} \approx 0{,}14$.

**Zadanie 2.** Żelazo ma temperaturę Curie 1043 K, a każdy atom ma 8 najbliższych sąsiadów (sieć bcc, 23.02). Oszacuj energię oddziaływania $J$ w przybliżeniu pola średniego.

$J = kT_c/z = 1{,}38\cdot10^{-23}\cdot1043/8 \approx 1{,}8\cdot10^{-21}\ \mathrm J \approx 0{,}011\ \mathrm{eV}$. To energia oddziaływania wymiennego — efektu kwantowego (zakaz Pauliego, 21.04), a nie oddziaływania magnetycznego dipoli, które jest ok. 1000 razy słabsze.

### Wersja z rachunkiem różniczkowym i całkowym

**Pole średnie w pobliżu $T_c$.** Rozwijając $\tanh y \approx y - y^3/3$ dla małych $m$ i $h = 0$:

$$m \approx \frac{T_c}{T}m - \frac13\left(\frac{T_c}{T}\right)^3m^3 \Rightarrow m^2 \approx 3\left(\frac{T}{T_c}\right)^3\frac{T_c - T}{T} \approx 3\frac{T_c - T}{T_c}.$$

Stąd $m \propto (T_c - T)^{1/2}$: wykładnik krytyczny pola średniego $\beta = 1/2$. Dokładny wynik 2D daje $\beta = 1/8$ — namagnesowanie rośnie poniżej $T_c$ znacznie szybciej.

**Ciepło właściwe z fluktuacji.** Z $\langle E\rangle = -\partial\ln Z/\partial\beta$ (27.02):

$$C = \frac{\partial\langle E\rangle}{\partial T} = \frac{1}{kT^2}\frac{\partial^2\ln Z}{\partial\beta^2} = \frac{\langle E^2\rangle - \langle E\rangle^2}{kT^2}.$$

Ciepło właściwe jest proporcjonalne do wariancji energii, więc symulacja nie musi różniczkować — wystarczy zmierzyć rozrzut energii. Maksimum $C$ wyznacza $T_c$.

## Typowe pułapki

- **W wysokiej temperaturze spiny „nie mają energii”.** Mają, ale entropia wygrywa: nieuporządkowanych konfiguracji jest dużo więcej.
- **Model Isinga opisuje tylko magnesy.** Ten sam model (gaz sieciowy) opisuje przejście ciecz–para, mieszaniny stopów, a nawet niektóre modele w biologii i ekonomii.
- **Za krótka symulacja.** Blisko $T_c$ układ dochodzi do równowagi bardzo powoli („spowolnienie krytyczne”). Trzeba odrzucić początkowe kroki i uśredniać długo.
- **Mała siatka daje ostre przejście.** Na skończonej siatce przejście jest rozmyte, a maksimum ciepła właściwego przesunięte. Ostre przejście fazowe istnieje tylko w granicy nieskończonego układu.

## Doświadczenie / symulacja

**Temperatura Curie.** Zawieś na nitce mały gwóźdź przyciągany przez magnes i ogrzewaj go zapalniczką (z zachowaniem ostrożności, nad niepalnym podłożem). Po przekroczeniu temperatury Curie (ok. 770°C dla żelaza) gwóźdź odpada od magnesu, a po ostygnięciu znów jest przyciągany. Lepiej działa drut niklowy (temperatura Curie 358°C).

**Python:** symulacja 2D modelu Isinga metodą Metropolisa (aktualizacja „szachownicowa”, wektorowo w NumPy), namagnesowanie i ciepło właściwe w funkcji temperatury, porównanie z rozwiązaniem Onsagera i z przybliżeniem pola średniego.

```python
import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import brentq

rng = np.random.default_rng(0)
L = 32
I, J = np.indices((L, L))
maski = [(I + J) % 2 == 0, (I + J) % 2 == 1]                    # szachownica: sąsiedzi spinu są na drugim kolorze

def krok(s, T):                                                  # jeden przebieg Metropolisa (J = k = 1, h = 0)
    for m in maski:
        sasiedzi = np.roll(s, 1, 0) + np.roll(s, -1, 0) + np.roll(s, 1, 1) + np.roll(s, -1, 1)
        dE = 2*s*sasiedzi
        s[m & (rng.random((L, L)) < np.exp(-dE/T))] *= -1

Ts = np.linspace(1.5, 3.5, 17)
s = np.ones((L, L), dtype=int)
Ms, Cs, migawki = [], [], {}
for T in Ts:
    for _ in range(400):
        krok(s, T)
    m_lista, e_lista = [], []
    for _ in range(800):
        krok(s, T)
        m_lista.append(abs(s.mean()))
        e_lista.append(-(s*(np.roll(s, 1, 0) + np.roll(s, 1, 1))).sum())
    Ms.append(np.mean(m_lista)); Cs.append(np.var(e_lista)/T**2/L**2)
    if np.isclose(T, [2.0, 2.25, 3.0]).any():
        migawki[round(T, 2)] = s.copy()
Tc = 2/np.log(1 + np.sqrt(2))
print(f"T_c (Onsager) = {Tc:.4f}; maksimum ciepła właściwego w symulacji przy T = {Ts[np.argmax(Cs)]:.3f}")
for T, m in zip(Ts[::4], Ms[::4]):
    dokl = (1 - np.sinh(2/T)**-4)**0.125 if T < Tc else 0.0
    sr = brentq(lambda x: x - np.tanh(4*x/T), 1e-9, 1) if T < 4 else 0.0
    print(f"T = {T:.2f}: |m| symulacja {m:.3f}, Onsager {dokl:.3f}, pole średnie {sr:.3f}")

fig, ax = plt.subplots(1, 4, figsize=(15, 3.6))
Td = np.linspace(1.5, Tc - 1e-4, 200)
ax[0].plot(Ts, Ms, "o", label="Metropolis 32×32"); ax[0].plot(Td, (1 - np.sinh(2/Td)**-4)**0.125, label="Onsager")
ax[0].set_xlabel("kT/J"); ax[0].set_ylabel("|m|"); ax[0].legend()
for a, (T, konf) in zip(ax[1:], sorted(migawki.items())):
    a.imshow(konf, cmap="gray"); a.set_title(f"kT/J = {T}"); a.axis("off")
plt.tight_layout(); plt.show()
```

## Zadania

### A. Poziom maturalny _(opcjonalnie — rozgrzewka)_

1. Dlaczego magnes trwały ogrzany powyżej temperatury Curie traci namagnesowanie?

<details>
<summary>Odpowiedź</summary>

Ruchy cieplne (energia $kT$) przeważają nad oddziaływaniem porządkującym sąsiednie momenty magnetyczne. Momenty ustawiają się chaotycznie i ich suma znika.
</details>

2. Ile różnych konfiguracji ma siatka 10×10 spinów? Ile lat zajęłoby ich przejrzenie, gdyby komputer sprawdzał $10^9$ konfiguracji na sekundę?

<details>
<summary>Odpowiedź</summary>

$2^{100} \approx 1{,}3\cdot10^{30}$; czas $1{,}3\cdot10^{21}\ \mathrm s \approx 4\cdot10^{13}$ lat — 3000 razy dłużej niż wiek Wszechświata. Dlatego używa się losowania (Monte Carlo).
</details>

### B. Poziom akademicki

1. Rozwiąż numerycznie równanie pola średniego $m = \tanh(4m/T)$ dla $T = 2$, 3 i 3,9 (w jednostkach $J/k$). Porównaj z przybliżeniem $m \approx \sqrt{3(T_c - T)/T_c}$.

<details>
<summary>Odpowiedź</summary>

$T = 2$: $m \approx 0{,}958$; $T = 3$: $0{,}776$; $T = 3{,}9$: $0{,}271$. Przybliżenie: 1,22 (bez sensu, daleko od $T_c$), 0,87, 0,27 — dobre tylko blisko $T_c = 4$.
</details>

2. Pokaż, że reguła Metropolisa spełnia **równowagę szczegółową**: $P(a)W(a \to b) = P(b)W(b \to a)$ dla $P \propto e^{-E/kT}$.

<details>
<summary>Odpowiedź</summary>

Niech $E_b > E_a$. Wtedy $W(a \to b) = e^{-(E_b - E_a)/kT}$, $W(b \to a) = 1$. $P(a)W(a \to b) = e^{-E_a/kT}e^{-(E_b - E_a)/kT} = e^{-E_b/kT} = P(b)W(b \to a)$. Rozkład Boltzmanna jest więc stanem stacjonarnym procesu.
</details>

3. Zmodyfikuj symulację, dodając pole $h = 0{,}1$ ($\Delta E = 2s_i(\sum s_j + h)$). Co dzieje się z ostrością przejścia?

<details>
<summary>Odpowiedź</summary>

Namagnesowanie nie spada do zera powyżej $T_c$ — pole wyróżnia kierunek. Przejście fazowe się rozmywa (w polu nie ma ostrego przejścia), a maksimum ciepła właściwego się obniża i przesuwa.
</details>

4. Oszacuj z danych symulacji wykładnik $\beta$: dopasuj prostą do $\ln\lvert m\rvert$ od $\ln(T_c - T)$ dla $T$ od 1,8 do 2,2. Dlaczego wynik odbiega od 1/8?

<details>
<summary>Odpowiedź</summary>

Wychodzi zwykle 0,1–0,2. Odchylenia biorą się ze skończonego rozmiaru siatki (blisko $T_c$ fluktuacje są większe niż układ), z krótkich przebiegów i z tego, że prawo potęgowe obowiązuje dopiero bardzo blisko $T_c$.
</details>

## Źródła

- K. Huang, *Podstawy fizyki statystycznej*, PWN — przejścia fazowe i model Isinga.
- Moduły 14.07 (ferromagnetyki), 25.06 (Monte Carlo), 27.02 (rozkład Boltzmanna).
- M. Newman, *Computational Physics*, rozdz. 10 (metoda Monte Carlo, model Isinga) — materiał dodatkowy, po angielsku.
