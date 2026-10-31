# 26.02 — Budowa gwiazd: równowaga hydrostatyczna, źródła energii, czas życia

> **Moduł:** [26 — Astrofizyka](README.md) · **Poziom:** 🔵 studia · **Status:** ✅ pełny
>
> **Czytaj:**
>
> - OpenStax, *Fizyka dla szkół wyższych*, t. 3, rozdz. 10: [§10.6](https://openstax.org/books/fizyka-dla-szk%C3%B3%C5%82-wy%C5%BCszych-tom-3/pages/10-6-fuzja-jadrowa) · [wstęp do rozdziału](https://openstax.org/books/fizyka-dla-szk%C3%B3%C5%82-wy%C5%BCszych-tom-3/pages/10-wstep)
> - Halliday, Resnick, Walker, *Podstawy fizyki*, wyd. 2015, t. 5: §43.5 (s. 221)
> - Halliday, Resnick, Walker, *Podstawy fizyki*, wyd. 1 (2003), t. 5: [§44.7, s. 185](https://home.agh.edu.pl/~czapli/Resnick_5.pdf#page=201) — PDF z serwera AGH

← [Promieniowanie gwiazd: moc, temperatura, widma i diagram H–R](01-promieniowanie-gwiazd.md) · [spis modułu](README.md) · [Ewolucja gwiazd: białe karły, gwiazdy neutronowe, supernowe](03-ewolucja-gwiazd.md) →

## Po co to jest

Gwiazda to kula gazu, która przez miliardy lat utrzymuje się w równowadze między grawitacją ściskającą ją do środka a ciśnieniem gorącej plazmy. Proste prawa fizyki (równowaga sił, gaz doskonały, przewodzenie energii) z dodatkiem fizyki jądrowej wystarczają, żeby oszacować temperaturę we wnętrzu Słońca, jego ciśnienie i czas życia. Historycznie to był ważny problem: w XIX w. żadne znane źródło energii nie tłumaczyło, jak Słońce może świecić dłużej niż kilkadziesiąt milionów lat. Rozwiązaniem okazała się synteza jądrowa (22.06).

## Teoria w pigułce

**Równowaga hydrostatyczna.** Warstwa gazu na odległości $r$ od środka jest przyciągana przez masę $M(r)$ zawartą wewnątrz i podtrzymywana przez różnicę ciśnień (08.01):

$$\frac{dP}{dr} = -\frac{GM(r)\rho(r)}{r^2}.$$

Ciśnienie rośnie w głąb gwiazdy. Proste oszacowanie (zamiana pochodnej na iloraz): $P_c \sim GM^2/R^4 \approx 10^{15}\ \mathrm{Pa}$ dla Słońca. Model numeryczny (politropa) daje $1{,}2\cdot10^{16}\ \mathrm{Pa}$, a dokładne modele $2{,}5\cdot10^{16}\ \mathrm{Pa}$ — 250 miliardów atmosfer.

**Temperatura we wnętrzu.** Z równania gazu doskonałego (11.04) i oszacowania ciśnienia: energia cieplna cząstki jest rzędu jej energii grawitacyjnej, $kT_c \sim GM\bar m/R$, gdzie $\bar m \approx 0{,}6m_p$ to średnia masa cząstki zjonizowanej plazmy. Daje to $T_c \sim 10^7\ \mathrm K$. Model Słońca: $1{,}57\cdot10^7\ \mathrm K$ — dość, żeby zachodziła synteza wodoru (22.06).

**Twierdzenie o wiriale.** Dla gwiazdy w równowadze energia cieplna $U$ i grawitacyjna $E_g$ spełniają $2U + E_g = 0$. Wniosek zaskakujący: gwiazda tracąca energię (świecąca) bez źródeł wewnętrznych **kurczy się i nagrzewa**. Połowa energii wydzielonej przy kurczeniu idzie na promieniowanie, a połowa na podgrzanie gazu.

**Źródła energii:**
- **grawitacyjne (Kelvin, Helmholtz):** czas, przez który Słońce mogłoby świecić z samego kurczenia, to $t_{KH} \sim GM^2/(RL) \approx 30$ mln lat — za mało wobec wieku Ziemi (4,5 mld lat);
- **jądrowe:** w jądrze (ok. 10% masy) wodór zamienia się w hel. Wydziela się 0,7% energii spoczynkowej: $t_{\text{jądr}} \approx 0{,}1\cdot0{,}007\cdot Mc^2/L \approx 10^{10}$ lat. Cykl pp (22.06) daje 26,7 MeV na każde jądro helu i dwa neutrina. Neutrina słoneczne docierają do Ziemi w liczbie ok. $6\cdot10^{10}$ na cm² na sekundę.

**Transport energii.** Energia z jądra płynie na zewnątrz przez **promieniowanie** (fotony są wielokrotnie pochłaniane i emitowane, błądzenie losowe 25.06 — dziesiątki tysięcy lat) i przez **konwekcję** (w zewnętrznych 30% promienia Słońca; widać ją jako granulację na powierzchni).

**Zależności dla ciągu głównego.** Moc rośnie bardzo szybko z masą, w przybliżeniu $L \propto M^{3{,}5}$. Paliwo rośnie tylko jak $M$, więc czas życia na ciągu głównym

$$t \propto \frac{M}{L} \propto M^{-2{,}5}: \quad t \approx 10^{10}\ \mathrm{lat}\cdot\left(\frac{M}{M_\odot}\right)^{-2{,}5}.$$

Gwiazda o masie $10M_\odot$ żyje ok. 30 mln lat, czerwony karzeł $0{,}5M_\odot$ — ok. 60 mld lat (dłużej niż obecny wiek Wszechświata). Najmniejsze gwiazdy mają ok. $0{,}08M_\odot$ — mniejsze obiekty nie osiągają temperatury zapłonu wodoru (brązowe karły).

## Wzory i założenia

| Wzór | Znaczenie | Kiedy obowiązuje |
|---|---|---|
| $dP/dr = -GM(r)\rho/r^2$ | równowaga hydrostatyczna | gwiazda statyczna, symetria sferyczna |
| $dM/dr = 4\pi r^2\rho$ | masa wewnątrz promienia $r$ | — |
| $P = \rho kT/\bar m$ | gaz doskonały | plazma niezdegenerowana |
| $2U + E_g = 0$ | twierdzenie o wiriale | układ w równowadze |
| $t_{KH} \sim GM^2/(RL)$ | czas kurczenia grawitacyjnego | oszacowanie |
| $L \propto M^{3{,}5}$, $t \propto M^{-2{,}5}$ | zależności dla ciągu głównego | gwiazdy ok. $0{,}5$–$20M_\odot$ |

## Przykład rozwiązany

**Zadanie 1.** Oszacuj czas świecenia Słońca: (a) z energii grawitacyjnej, (b) z syntezy wodoru w jądrze ($M_\odot = 1{,}99\cdot10^{30}\ \mathrm{kg}$, $R_\odot = 6{,}96\cdot10^8\ \mathrm m$, $L_\odot = 3{,}83\cdot10^{26}\ \mathrm W$).

(a) $t_{KH} = \dfrac{GM^2}{RL} \approx \dfrac{6{,}67\cdot10^{-11}\cdot(1{,}99\cdot10^{30})^2}{6{,}96\cdot10^8\cdot3{,}83\cdot10^{26}}\ \mathrm s \approx 10^{15}\ \mathrm s \approx 31$ mln lat.

(b) $t = \dfrac{0{,}1\cdot0{,}007\cdot Mc^2}{L} \approx 3{,}3\cdot10^{17}\ \mathrm s \approx 10$ mld lat. Słońce ma 4,6 mld lat, więc jest mniej więcej w połowie życia na ciągu głównym.

**Zadanie 2.** Ile neutrin ze Słońca przechodzi w ciągu sekundy przez 1 cm² na Ziemi?

Na każde 26,7 MeV powstają 2 neutrina. Liczba neutrin na sekundę: $2L/(26{,}7\ \mathrm{MeV}) \approx 1{,}8\cdot10^{38}$. Na odległości 1 AU: $\dfrac{1{,}8\cdot10^{38}}{4\pi(1{,}5\cdot10^{13}\ \mathrm{cm})^2} \approx 6\cdot10^{10}\ \mathrm{cm^{-2}s^{-1}}$.

### Wersja z rachunkiem różniczkowym i całkowym

**Ciśnienie w środku gwiazdy o stałej gęstości.** Dla $\rho = \text{const}$: $M(r) = \tfrac43\pi r^3\rho$, więc

$$\frac{dP}{dr} = -\frac43\pi G\rho^2r \Rightarrow P(r) = \frac23\pi G\rho^2(R^2 - r^2), \qquad P_c = \frac{3GM^2}{8\pi R^4} \approx 1{,}3\cdot10^{14}\ \mathrm{Pa}.$$

To 200 razy za mało, bo prawdziwa gęstość w środku Słońca (ok. $1{,}5\cdot10^5\ \mathrm{kg/m^3}$) jest ponad 100 razy większa od średniej ($1410\ \mathrm{kg/m^3}$).

**Lepszy model: politropa.** Przyjmując $P = K\rho^{1+1/n}$, z równowagi hydrostatycznej dostaje się równanie Lane'a–Emdena

$$\frac{1}{\xi^2}\frac{d}{d\xi}\left(\xi^2\frac{d\theta}{d\xi}\right) = -\theta^n, \qquad \theta(0) = 1,\ \theta'(0) = 0.$$

Dla $n = 3$ (model Eddingtona) rozwiązanie numeryczne daje promień $\xi_1 = 6{,}897$ i stosunek gęstości centralnej do średniej 54,2, a ciśnienie centralne Słońca $1{,}2\cdot10^{16}\ \mathrm{Pa}$.

## Typowe pułapki

- **Słońce się pali.** Spalanie to reakcja chemiczna (ok. 1 eV na cząsteczkę). Słońce świeci dzięki syntezie jądrowej (MeV na reakcję). Węglowe Słońce wypaliłoby się w kilka tysięcy lat.
- **Światło ze środka Słońca dociera do nas w 8 minut.** Z powierzchni — tak. Energia z jądra wędruje do powierzchni dziesiątki tysięcy lat.
- **Masywniejsze gwiazdy żyją dłużej, bo mają więcej paliwa.** Żyją krócej, bo moc rośnie z masą znacznie szybciej niż zapas paliwa.
- **Gwiazda tracąca energię stygnie.** Bez źródła jądrowego gwiazda kurczy się i jej wnętrze się nagrzewa (twierdzenie o wiriale) — tak zapala się synteza w protogwiazdach i kolejne etapy syntezy w starzejących się gwiazdach.

## Doświadczenie / symulacja

**Obserwacja Słońca metodą projekcji.** Nigdy nie patrz na Słońce przez lornetkę ani teleskop bez certyfikowanego filtra. Bezpieczna metoda: lornetka na statywie rzuca obraz Słońca na biały karton w cieniu. Widać plamy słoneczne. Obserwując je przez kilka dni, wyznacz okres obrotu Słońca (ok. 27 dni na równiku).

**Python:** model gwiazdy — rozwiązanie równania Lane'a–Emdena dla politropy $n = 3$, profile gęstości i ciśnienia, ciśnienie i gęstość centralna Słońca, czas życia gwiazd ciągu głównego.

```python
import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp

G, c, k, mp = 6.674e-11, 2.998e8, 1.380649e-23, 1.6726e-27
M, R, L = 1.989e30, 6.957e8, 3.828e26
rok = 3.156e7

def lane_emden(n):
    f = lambda x, y: [y[1], -np.clip(y[0], 0, None)**n - 2*y[1]/x]
    brzeg = lambda x, y: y[0]; brzeg.terminal = True
    x0 = 1e-6
    return solve_ivp(f, [x0, 50], [1 - x0**2/6, -x0/3], events=brzeg, rtol=1e-10, atol=1e-12, dense_output=True)

for n in (1.5, 3):
    s = lane_emden(n)
    xi1, dth = s.t_events[0][0], s.y_events[0][0][1]
    gest = -xi1/(3*dth)                                    # ρc / ρ_średnie
    Pc = G*M**2/R**4/(4*np.pi*(n + 1)*dth**2)
    print(f"politropa n = {n}: ξ1 = {xi1:.3f}, ρc/ρśr = {gest:.1f}, Pc(Słońce) = {Pc:.2e} Pa")
print(f"stała gęstość: Pc = {3*G*M**2/(8*np.pi*R**4):.2e} Pa; model Słońca: 2,5e16 Pa")
print(f"czas Kelvina–Helmholtza: {G*M**2/(R*L)/rok/1e6:.0f} mln lat; jądrowy: {0.1*0.007*M*c**2/L/rok/1e9:.1f} mld lat")
print(f"neutrina słoneczne przy Ziemi: {2*L/(26.7e6*1.602e-19)/(4*np.pi*1.496e13**2):.1e} na cm² na s")
for m in (0.5, 1, 2, 5, 10, 20):
    print(f"M = {m:4.1f} M☉: L ≈ {m**3.5:9.1f} L☉, czas na ciągu głównym ≈ {1e10*m**-2.5:.1e} lat")

s = lane_emden(3)
xi = np.linspace(1e-6, s.t_events[0][0], 300)
th = np.clip(s.sol(xi)[0], 0, None)
plt.plot(xi/xi[-1], th**3, label="gęstość ρ/ρc"); plt.plot(xi/xi[-1], th**4, label="ciśnienie P/Pc")
plt.plot(xi/xi[-1], th, label="temperatura T/Tc")
plt.xlabel("r / R"); plt.legend(); plt.grid(True); plt.title("politropa n = 3"); plt.show()
```

## Zadania

### A. Poziom maturalny _(opcjonalnie — rozgrzewka)_

1. Ile masy traci Słońce w ciągu sekundy na promieniowanie, a ile wodoru zamienia w hel? (Przy zamianie 4 protonów w hel 0,7% masy zamienia się w energię.)

<details>
<summary>Odpowiedź</summary>

$\Delta m = L/c^2 \approx 4{,}3\cdot10^9\ \mathrm{kg/s}$. Wodoru zamienia się $4{,}3\cdot10^9/0{,}007 \approx 6\cdot10^{11}\ \mathrm{kg/s}$, czyli ok. 600 mln ton na sekundę.
</details>

2. Dlaczego gwiazda nie zapada się pod wpływem własnej grawitacji?

<details>
<summary>Odpowiedź</summary>

Grawitację równoważy siła parcia wynikająca z różnicy ciśnień gorącego gazu (ciśnienie rośnie w głąb gwiazdy). Wysoką temperaturę utrzymuje energia z syntezy jądrowej.
</details>

### B. Poziom akademicki

1. Gwiazda o masie $3M_\odot$. Oszacuj jej moc i czas życia na ciągu głównym.

<details>
<summary>Odpowiedź</summary>

$L \approx 3^{3{,}5} \approx 47L_\odot$, $t \approx 10^{10}\cdot3^{-2{,}5} \approx 6\cdot10^8$ lat.
</details>

2. Wyprowadź twierdzenie o wiriale dla gwiazdy z gazu jednoatomowego: pomnóż równanie równowagi hydrostatycznej przez $4\pi r^3$ i scałkuj od 0 do $R$ (ciśnienie na powierzchni równe zeru).

<details>
<summary>Odpowiedź</summary>

$\int_0^R4\pi r^3\dfrac{dP}{dr}dr = [4\pi r^3P]_0^R - 3\int_0^R4\pi r^2P\,dr = -3\int P\,dV$. Prawa strona: $-\int\dfrac{GM(r)}{r}dM = E_g$. Dla gazu jednoatomowego $\int P\,dV = \tfrac23U$, więc $-2U = E_g$, czyli $2U + E_g = 0$.
</details>

3. Oszacuj temperaturę w środku Słońca z $kT_c \approx GM\bar m/R$, gdzie $\bar m = 0{,}6m_p$.

<details>
<summary>Odpowiedź</summary>

$T_c \approx \dfrac{6{,}67\cdot10^{-11}\cdot1{,}99\cdot10^{30}\cdot0{,}6\cdot1{,}67\cdot10^{-27}}{1{,}38\cdot10^{-23}\cdot6{,}96\cdot10^8} \approx 1{,}4\cdot10^7\ \mathrm K$ (model: $1{,}57\cdot10^7\ \mathrm K$).
</details>

4. Uruchom kod dla politropy $n = 1{,}5$ (gwiazda konwekcyjna, np. czerwony karzeł). O ile mniejszy jest stosunek gęstości centralnej do średniej niż dla $n = 3$?

<details>
<summary>Odpowiedź</summary>

Dla $n = 1{,}5$: $\xi_1 \approx 3{,}654$, $\rho_c/\bar\rho \approx 6{,}0$ (dla $n = 3$: 54,2). Gwiazdy w pełni konwekcyjne są znacznie mniej skoncentrowane ku środkowi.
</details>

## Źródła

- OpenStax, *Fizyka dla szkół wyższych*, t. 3, rozdz. 10 — §10.6: fuzja jądrowa (energia Słońca).
- Halliday, Resnick, Walker, *Podstawy fizyki* — wyd. 2015: t. 5, §43.5 (synteza termojądrowa w Słońcu i innych gwiazdach); wyd. 1: t. 5, §44.7.
- Moduły 08.01 (ciśnienie hydrostatyczne), 11.04 (gaz doskonały), 22.06 (synteza termojądrowa).
- OpenStax, *Astronomy 2e*, rozdz. 15–16 (Słońce, źródła energii) — [openstax.org/details/books/astronomy-2e](https://openstax.org/details/books/astronomy-2e), materiał dodatkowy, po angielsku.
