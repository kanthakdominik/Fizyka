# 28.05 — Małe drgania i drgania sprzężone — mody normalne

> **Moduł:** [28 — Mechanika analityczna (wstęp)](README.md) · **Poziom:** 🔵 studia · **Status:** ✅ pełny
>
> **Czytaj:**
>
> - _Podręczniki główne nie mają osobnego paragrafu na ten temat — materiały są w sekcji „Źródła”._

← [Funkcja Hamiltona, równania Hamiltona i przestrzeń fazowa](04-rownania-hamiltona.md) · [spis modułu](README.md) · (koniec modułu) →

## Po co to jest

Drgania układów z wieloma elementami — dwóch wahadeł połączonych sprężyną, atomów w cząsteczce, mostu, budynku przy trzęsieniu ziemi — wyglądają chaotycznie. Okazuje się jednak, że każde małe drganie jest sumą kilku prostych ruchów, w których wszystkie części drgają z jedną częstotliwością: **modów normalnych**. Ich znajomość pozwala projektować konstrukcje odporne na rezonans (09.05), rozumieć widma oscylacyjne cząsteczek (23.01) i dźwięk instrumentów (10.06). W granicy wielu ciał mody normalne przechodzą w fale (10) i fonony w kryształach (23). Matematycznie to zagadnienie własne macierzy — jeden z najważniejszych rachunków w fizyce.

## Teoria w pigułce

**Małe drgania wokół równowagi.** Rozwijając energię potencjalną wokół minimum (00.06, 04.06) do drugiego rzędu, dostajemy dla $n$ współrzędnych

$$E_p \approx \tfrac12\sum_{ij}K_{ij}x_ix_j, \qquad E_k = \tfrac12\sum_{ij}M_{ij}\dot x_i\dot x_j,$$

gdzie $K$ to macierz sztywności, a $M$ — macierz mas. Równania Lagrange'a (28.02) dają układ liniowy $M\ddot{\vec x} = -K\vec x$.

**Mody normalne.** Szukamy ruchów, w których wszystkie współrzędne drgają z tą samą częstością: $\vec x(t) = \vec a\cos(\omega t + \varphi)$. Podstawienie daje **zagadnienie własne**:

$$(K - \omega^2M)\vec a = 0 \Rightarrow \det(K - \omega^2M) = 0.$$

Układ o $n$ stopniach swobody ma $n$ częstości własnych i $n$ modów (wektorów $\vec a$). Dowolne małe drganie to ich superpozycja.

**Dwa wahadła połączone sprężyną** (długość $l$, masy $m$, sprężyna $\kappa$):
- **mod zgodny** — oba wahadła wychylają się tak samo, sprężyna się nie odkształca: $\omega_1 = \sqrt{g/l}$;
- **mod przeciwny** — wahadła drgają w przeciwfazie, sprężyna pracuje podwójnie: $\omega_2 = \sqrt{g/l + 2\kappa/m}$.

Gdy wychylimy tylko jedno wahadło, oba mody są wzbudzone jednocześnie i powstają **dudnienia** (09.06): energia przelewa się z jednego wahadła na drugie i z powrotem. Pełne przekazanie trwa $\pi/(\omega_2 - \omega_1)$ — przy słabym sprzężeniu wiele okresów.

**Łańcuch $N$ mas** połączonych sprężynami (końce zamocowane). Częstości własne:

$$\omega_n = 2\sqrt{\frac km}\sin\frac{n\pi}{2(N + 1)}, \qquad n = 1, \dots, N.$$

Mod $n$ to fala stojąca z $n - 1$ węzłami (10.03). Dla bardzo długiego łańcucha i długich fal $\omega \approx \sqrt{k/m}\cdot qa$ — fala o stałej prędkości (10.02). Dla krótkich fal pojawia się **dyspersja** i maksymalna częstość $2\sqrt{k/m}$. W krysztale mody normalne sieci to **fonony**, które przenoszą ciepło i dźwięk oraz wyznaczają ciepło właściwe (27.03).

**Cząsteczki.** Cząsteczka CO₂ (O=C=O) ma dwa mody rozciągające: symetryczny (tlen–tlen w przeciwfazie, węgiel stoi) i asymetryczny (węgiel drga między tlenami). W prostym modelu sprężynowym stosunek ich częstości to $\sqrt{1 + 2m_O/m_C} \approx 1{,}9$ (zmierzone ok. 1,8). Tylko mod asymetryczny i mod zginający zmieniają moment dipolowy, więc tylko one pochłaniają podczerwień — dlatego CO₂ jest gazem cieplarnianym (23.01).

## Wzory i założenia

| Wzór | Znaczenie | Kiedy obowiązuje |
|---|---|---|
| $M\ddot{\vec x} = -K\vec x$ | równania małych drgań | rozwinięcie wokół minimum energii |
| $\det(K - \omega^2M) = 0$ | równanie na częstości własne | — |
| $\omega_1 = \sqrt{g/l}$, $\omega_2 = \sqrt{g/l + 2\kappa/m}$ | wahadła sprzężone | małe wychylenia |
| $T_{\text{przek}} = \pi/(\omega_2 - \omega_1)$ | czas przekazania energii | jedno wahadło wychylone na starcie |
| $\omega_n = 2\sqrt{k/m}\sin\dfrac{n\pi}{2(N + 1)}$ | łańcuch $N$ mas | końce zamocowane |
| $\omega(q) = 2\sqrt{k/m}\lvert\sin(qa/2)\rvert$ | związek dyspersyjny łańcucha | łańcuch nieskończony, $a$ — odstęp mas |

## Przykład rozwiązany

**Zadanie.** Dwie masy $m$ połączone trzema jednakowymi sprężynami $k$ (ściana–masa–masa–ściana). Znajdź częstości i mody.

Energia potencjalna: $\tfrac12kx_1^2 + \tfrac12k(x_2 - x_1)^2 + \tfrac12kx_2^2$, więc $K = k\begin{pmatrix}2 & -1\\ -1 & 2\end{pmatrix}$, $M = m\cdot\mathbb 1$.

$\det\begin{pmatrix}2k - m\omega^2 & -k\\ -k & 2k - m\omega^2\end{pmatrix} = (2k - m\omega^2)^2 - k^2 = 0 \Rightarrow \omega^2 = \dfrac km$ lub $\dfrac{3k}m$.

- $\omega_1 = \sqrt{k/m}$, mod $(1, 1)$ — masy drgają razem, środkowa sprężyna się nie odkształca.
- $\omega_2 = \sqrt{3k/m}$, mod $(1, -1)$ — masy w przeciwfazie.

### Wersja z rachunkiem różniczkowym i całkowym

**Dudnienia wahadeł sprzężonych.** Warunki początkowe: $x_1(0) = A$, $x_2(0) = 0$, prędkości zerowe. W modach: $x_1 = \tfrac A2(\cos\omega_1t + \cos\omega_2t)$, $x_2 = \tfrac A2(\cos\omega_1t - \cos\omega_2t)$. Ze wzorów na sumę cosinusów:

$$x_1 = A\cos\frac{\Delta\omega\,t}{2}\cos\bar\omega t, \qquad x_2 = A\sin\frac{\Delta\omega\,t}{2}\sin\bar\omega t,$$

gdzie $\Delta\omega = \omega_2 - \omega_1$, $\bar\omega = (\omega_1 + \omega_2)/2$. Amplituda pierwszego wahadła spada do zera po czasie $\pi/\Delta\omega$, gdy drugie drga z pełną amplitudą. Dla $l = 1\ \mathrm m$ i $\kappa/m = 1\ \mathrm{s^{-2}}$: $\omega_1 = 3{,}13$, $\omega_2 = 3{,}44\ \mathrm{rad/s}$, przekazanie energii po ok. 10,3 s, czyli po ok. 5 okresach.

**Łańcuch mas.** Równanie dla masy $j$: $m\ddot x_j = k(x_{j+1} - 2x_j + x_{j-1})$. Podstawiając falę $x_j = Ae^{i(qja - \omega t)}$:

$$-m\omega^2 = k(e^{iqa} - 2 + e^{-iqa}) = -2k(1 - \cos qa) = -4k\sin^2\frac{qa}{2}.$$

Zamocowane końce wybierają $q = n\pi/((N + 1)a)$, co daje wzór na $\omega_n$. Dla $qa \ll 1$: $\omega \approx a\sqrt{k/m}\,q$ — fala dźwiękowa o prędkości $v = a\sqrt{k/m}$, czyli równanie falowe (10.02) jako granica ciągła łańcucha.

## Typowe pułapki

- **Każda masa ma „swoją” częstość.** W układzie sprzężonym częstości należą do całego układu (do modów), a nie do pojedynczych elementów.
- **Dudnienia to tłumienie.** Energia nie znika, tylko przepływa między wahadłami i wraca.
- **Mody istnieją tylko w układach symetrycznych.** Istnieją zawsze (macierze $K$ i $M$ są symetryczne), ale w układach niesymetrycznych nie są tak łatwe do odgadnięcia — trzeba rozwiązać zagadnienie własne.
- **Liniowe przybliżenie działa dla dowolnych drgań.** Tylko dla małych. Przy dużych amplitudach mody się sprzęgają, a ruch może stać się chaotyczny (wahadło podwójne, 28.02).

## Doświadczenie / symulacja

**Wahadła sprzężone.** Zawieś dwa jednakowe wahadła (np. butelki z wodą na sznurkach) na wspólnym, lekko uginającym się sznurku lub połącz je słabą gumką. Wychyl jedno i obserwuj przelewanie się drgań. Zmierz czas przekazania energii dla dwóch różnych sprzężeń. Wychyl oba jednakowo, a potem przeciwnie — zobaczysz czyste mody o stałych amplitudach. Telefon zawieszony jako jedno z wahadeł zarejestruje dudnienia w phyphox (*Akcelerometr*).

**Python:** częstości łańcucha mas z zagadnienia własnego (NumPy) w porównaniu ze wzorem, kształty modów i symulacja dudnień dwóch sprzężonych wahadeł.

```python
import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp

N = 8                                                       # łańcuch: k = m = 1, końce zamocowane
K = 2*np.eye(N) - np.eye(N, k=1) - np.eye(N, k=-1)
w2, mody = np.linalg.eigh(K)
wzor = 2*np.sin(np.arange(1, N + 1)*np.pi/(2*(N + 1)))
print("ω z macierzy:", np.round(np.sqrt(w2), 4))
print("ω ze wzoru:  ", np.round(wzor, 4))

g, l, kap = 9.81, 1.0, 1.0                                  # wahadła sprzężone (κ/m = 1 s⁻²)
w1, w2_ = np.sqrt(g/l), np.sqrt(g/l + 2*kap)
def rownania(t, y):
    x1, x2, v1, v2 = y
    return [v1, v2, -g/l*x1 - kap*(x1 - x2), -g/l*x2 - kap*(x2 - x1)]
t = np.linspace(0, 40, 4000)
s = solve_ivp(rownania, [0, 40], [0.1, 0, 0, 0], t_eval=t, rtol=1e-10, atol=1e-12)
print(f"ω1 = {w1:.3f}, ω2 = {w2_:.3f} rad/s; przekazanie energii po π/Δω = {np.pi/(w2_ - w1):.2f} s")
idx = np.argmax(np.abs(s.y[1]) > 0.099)
print(f"w symulacji drugie wahadło osiąga 99% amplitudy po {t[idx]:.2f} s")

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 4))
j = np.arange(N + 2)
for n in range(3):
    ax1.plot(j, np.concatenate([[0], mody[:, n], [0]]), "o-", label=f"mod {n + 1}, ω = {np.sqrt(w2[n]):.3f}")
ax1.set_xlabel("numer masy"); ax1.set_ylabel("amplituda"); ax1.legend()
ax2.plot(t, s.y[0], label="wahadło 1"); ax2.plot(t, s.y[1], label="wahadło 2")
ax2.set_xlabel("t [s]"); ax2.set_ylabel("wychylenie [rad]"); ax2.legend()
plt.tight_layout(); plt.show()
```

## Zadania

### A. Poziom maturalny _(opcjonalnie — rozgrzewka)_

1. Dwa jednakowe wahadła połączone słabą sprężyną. Jedno wychylono i puszczono. Opisz, co się dzieje z ruchem wahadeł w ciągu kilkudziesięciu sekund.

<details>
<summary>Odpowiedź</summary>

Amplituda pierwszego maleje, a drugiego rośnie, aż pierwsze prawie się zatrzyma, a drugie drga z pełną amplitudą. Potem proces się odwraca. Energia przelewa się między wahadłami (dudnienia).
</details>

2. Most piesi przechodzą w rytmie 2 kroków na sekundę. Dlaczego projektanci sprawdzają, czy żaden mod normalny mostu nie ma częstotliwości ok. 2 Hz (lub 1 Hz w kierunku poprzecznym)?

<details>
<summary>Odpowiedź</summary>

Wymuszenie o częstotliwości bliskiej częstotliwości modu powoduje rezonans (09.05) i duże drgania. Tak było z Millennium Bridge w Londynie (2000), który kołysał się poprzecznie.
</details>

### B. Poziom akademicki

1. Wyznacz częstości modów cząsteczki liniowej A–B–A (masy $m_A$, $m_B$, dwie sprężyny $k$) dla ruchu wzdłuż osi. Który mod ma zerową częstość i co oznacza?

<details>
<summary>Odpowiedź</summary>

Częstości: $0$, $\sqrt{k/m_A}$ (symetryczny, B stoi), $\sqrt{k(1/m_A + 2/m_B)}$ (asymetryczny). Mod o zerowej częstości to przesunięcie całej cząsteczki (ruch środka masy). Dla CO₂ stosunek niezerowych częstości $\sqrt{1 + 2m_O/m_C} \approx 1{,}9$.
</details>

2. Pokaż, że dla łańcucha $N$ mas największa częstość dąży do $2\sqrt{k/m}$ przy $N \to \infty$. Jaki mod ma tę częstość?

<details>
<summary>Odpowiedź</summary>

$\omega_N = 2\sqrt{k/m}\sin\dfrac{N\pi}{2(N + 1)} \to 2\sqrt{k/m}$. To mod, w którym sąsiednie masy drgają w przeciwfazie (długość fali równa dwóm odstępom, $qa = \pi$).
</details>

3. Zmień w kodzie sprzężenie $\kappa/m$ na 0,25 s⁻². Ile razy wydłuża się czas przekazania energii? Wyjaśnij z przybliżenia $\Delta\omega \approx \kappa/(m\omega_1)$ dla słabego sprzężenia.

<details>
<summary>Odpowiedź</summary>

$\omega_2 = \sqrt{\omega_1^2 + 2\kappa/m} \approx \omega_1 + \kappa/(m\omega_1)$, więc $\Delta\omega \propto \kappa$, a czas przekazania $\propto 1/\kappa$ — ok. 4 razy dłużej (ok. 39 s zamiast 10,3 s).
</details>

## Źródła

- J. R. Taylor, *Mechanika klasyczna*, PWN — rozdział o drganiach sprzężonych i modach normalnych.
- Halliday, Resnick, Walker, *Podstawy fizyki*, wyd. 2015, t. 2, rozdz. 15–16 — drgania i fale (podstawa do tego tematu).
- Moduły 09.05 (rezonans), 09.06 (dudnienia), 10.03 (fale stojące), 23.01 (widma cząsteczek), 27.03 (fonony i ciepło właściwe).
