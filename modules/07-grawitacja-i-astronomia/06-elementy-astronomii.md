# 07.06 — Elementy astronomii: odległości, gwiazdy, galaktyki

> **Moduł:** [07 — Grawitacja i elementy astronomii](README.md) · **Poziom:** 🟢 matura R · **Status:** ✅ pełny
>
> **Czytaj:**
>
> - _Podręczniki główne nie mają osobnego paragrafu na ten temat — materiały są w sekcji „Źródła”._

← [Pole rozkładu masy i siły pływowe](05-pole-rozkladu-masy-i-plywy.md) · [spis modułu](README.md) · (koniec modułu) →

## Po co to jest

Elementy astronomii są w podstawie programowej matury rozszerzonej, a na studiach wracają przy promieniowaniu cieplnym (11, 20), widmach atomowych (21), fizyce jądrowej (22) i kosmologii (24). Ten temat zbiera najważniejsze narzędzia: jak mierzymy odległości do gwiazd, skąd wiemy, jak gorące i jak duże są gwiazdy, i co mówi prawo Hubble'a o rozszerzającym się Wszechświecie.

## Teoria w pigułce

**Jednostki odległości.**

| Jednostka | Definicja | Wartość |
|---|---|---|
| jednostka astronomiczna (j.a., au) | średnia odległość Ziemia–Słońce | $1{,}496\cdot10^{11}\ \mathrm{m}$ |
| rok świetlny (ly) | droga światła w ciągu roku | $9{,}46\cdot10^{15}\ \mathrm{m}$ |
| parsek (pc) | odległość, z której 1 j.a. widać pod kątem 1″ | $3{,}086\cdot10^{16}\ \mathrm{m} \approx 3{,}26\ \mathrm{ly}$ |

**Paralaksa.** Bliska gwiazda w ciągu roku pozornie przesuwa się na tle dalekich gwiazd, bo patrzymy na nią z różnych punktów orbity Ziemi. Kąt paralaksy $p$ (połowa przesunięcia) i odległość $d$:

$$d\ [\mathrm{pc}] = \frac{1}{p\ [\text{″}]}.$$

Najbliższa gwiazda, Proxima Centauri, ma $p \approx 0{,}77$″, czyli $d \approx 1{,}3\ \mathrm{pc}$. Satelita Gaia mierzy paralaksy z dokładnością do mikrosekund łuku.

**Gwiazdy jako ciała doskonale czarne** (dokładniej w 20.01).
- **Prawo Wiena:** $\lambda_{\max}T = b \approx 2{,}898\cdot10^{-3}\ \mathrm{m\cdot K}$ — kolor gwiazdy mówi o temperaturze powierzchni (czerwone ok. 3000 K, Słońce ok. 5800 K, niebieskie powyżej 10 000 K).
- **Prawo Stefana–Boltzmanna:** moc promieniowania (jasność absolutna) gwiazdy o promieniu $R$:
  $$L = 4\pi R^2\sigma T^4, \qquad \sigma = 5{,}67\cdot10^{-8}\ \mathrm{W/(m^2K^4)}.$$
- **Natężenie promieniowania** w odległości $d$: $I = L/(4\pi d^2)$. Dla Słońca na orbicie Ziemi to **stała słoneczna** ok. $1360\ \mathrm{W/m^2}$.

**Diagram Hertzsprunga–Russella** przedstawia jasność gwiazd w funkcji temperatury. Większość gwiazd (w tym Słońce) leży na **ciągu głównym** — spalają wodór w jądrach. Powyżej leżą olbrzymy i nadolbrzymy (chłodne, ale ogromne), poniżej — białe karły (gorące, ale małe).

**Ewolucja gwiazd** w skrócie: gwiazda podobna do Słońca → czerwony olbrzym → mgławica planetarna i biały karzeł; gwiazda o masie powyżej ok. 8 mas Słońca → nadolbrzym → supernowa → gwiazda neutronowa lub czarna dziura. Źródłem energii gwiazd jest synteza jądrowa (22.06).

**Prawo Hubble'a.** Odległe galaktyki oddalają się od nas z prędkością proporcjonalną do odległości:

$$v = H_0d, \qquad H_0 \approx 70\ \mathrm{km/(s\cdot Mpc)}.$$

Prędkość mierzy się z przesunięcia linii widmowych ku czerwieni ($v \approx cz$ dla $z = \Delta\lambda/\lambda \ll 1$). Wniosek: Wszechświat się rozszerza; jego wiek jest rzędu $1/H_0 \approx 14$ mld lat (24.04).

## Wzory i założenia

| Wzór | Znaczenie | Kiedy obowiązuje |
|---|---|---|
| $d\ [\mathrm{pc}] = 1/p\ [\text{″}]$ | odległość z paralaksy | małe kąty, gwiazdy bliskie (do kilku kpc) |
| $\lambda_{\max}T = 2{,}898\cdot10^{-3}\ \mathrm{m\cdot K}$ | prawo Wiena | ciało doskonale czarne |
| $L = 4\pi R^2\sigma T^4$ | jasność gwiazdy | j.w. |
| $I = L/(4\pi d^2)$ | natężenie w odległości $d$ | brak pochłaniania |
| $v = H_0d$, $\ v \approx cz$ | prawo Hubble'a | $z \ll 1$, galaktyki dalsze niż kilka Mpc |

## Przykład rozwiązany

**Zadanie 1.** Gwiazda ma paralaksę 0,1″. W jakiej jest odległości? Ile lat leci do nas jej światło?

$d = 10\ \mathrm{pc} \approx 32{,}6$ roku świetlnego — tyle lat temu wysłała światło, które teraz widzimy.

**Zadanie 2.** Maksimum widma Słońca przypada na ok. 500 nm, a jego promień wynosi $6{,}96\cdot10^8\ \mathrm{m}$. Oblicz temperaturę powierzchni, moc promieniowania i stałą słoneczną.

- $T = 2{,}898\cdot10^{-3}/500\cdot10^{-9} \approx 5800\ \mathrm{K}$.
- $L = 4\pi R^2\sigma T^4 \approx 4\pi(6{,}96\cdot10^8)^2\cdot5{,}67\cdot10^{-8}\cdot5778^4 \approx 3{,}8\cdot10^{26}\ \mathrm{W}$.
- $I = L/(4\pi\cdot(1{,}496\cdot10^{11})^2) \approx 1370\ \mathrm{W/m^2}$ (zmierzona: ok. 1361 W/m²).

**Zadanie 3.** Galaktyka oddala się z prędkością 7000 km/s. Jak daleko się znajduje?

$d = v/H_0 = 7000/70 = 100\ \mathrm{Mpc} \approx 330$ mln lat świetlnych.

## Typowe pułapki

- **Parsek jako jednostka czasu.** To jednostka odległości.
- **Kąt paralaksy to całe przesunięcie.** To połowa rocznego przesunięcia (promień orbity, a nie średnica).
- **Jasność a temperatura.** Chłodna gwiazda może być bardzo jasna, jeśli jest ogromna ($L \propto R^2T^4$).
- **Galaktyki „uciekają od nas”.** Rozszerza się cała przestrzeń; obserwator w dowolnej galaktyce zobaczy to samo prawo Hubble'a.
- **Jednostki $H_0$.** Przy liczeniu wieku zamień megaparseki na kilometry.

## Doświadczenie / symulacja

**Stellarium.** W programie [Stellarium](https://stellarium.org/) znajdź gwiazdy o różnych kolorach (Betelgeza, Rigel, Syriusz, Arktur) i odczytaj ich typ widmowy i odległość. Oszacuj temperatury z prawa Wiena, przyjmując typowe długości fal maksimum dla danego koloru.

**Paralaksa na palcu.** Wyciągnij palec przed siebie i patrz na niego na przemian lewym i prawym okiem. Zmierz pozorne przesunięcie na tle ściany i odległość oczu — oblicz odległość palca ze wzoru paralaksy. To dokładnie ta sama metoda co dla gwiazd (rozstaw oczu ↔ średnica orbity Ziemi).

**Python:** uproszczony diagram Hertzsprunga–Russella dla kilku znanych gwiazd z promieni i temperatur.

```python
import numpy as np
import matplotlib.pyplot as plt

sigma, R_sun, L_sun = 5.67e-8, 6.96e8, 3.83e26
stars = {                     # temperatura [K], promień [R_Słońca] (wartości przybliżone)
    "Słońce": (5772, 1.0), "Syriusz A": (9940, 1.71), "Rigel": (12100, 79),
    "Betelgeza": (3600, 760), "Proxima Cen": (3040, 0.15), "Syriusz B": (25000, 0.0084),
}
for name, (T, R) in stars.items():
    L = 4*np.pi*(R*R_sun)**2*sigma*T**4
    plt.scatter(T, L/L_sun); plt.annotate(name, (T, L/L_sun))
    print(f"{name:11s}: L = {L/L_sun:10.3g} L_Słońca, λ_max = {2.898e-3/T*1e9:6.0f} nm")
plt.xscale("log"); plt.yscale("log"); plt.gca().invert_xaxis()
plt.xlabel("temperatura powierzchni [K]"); plt.ylabel("jasność [L_Słońca]"); plt.grid(True, which="both"); plt.show()
```

## Zadania

### A. Poziom maturalny

1. Proxima Centauri ma paralaksę 0,768″. Oblicz jej odległość w parsekach i latach świetlnych.

<details>
<summary>Odpowiedź</summary>

$d \approx 1{,}30\ \mathrm{pc} \approx 4{,}25$ roku świetlnego.
</details>

2. Maksimum widma Betelgezy przypada na ok. 830 nm. Oszacuj temperaturę jej powierzchni. Jakiego jest koloru?

<details>
<summary>Odpowiedź</summary>

$T \approx 3500\ \mathrm{K}$ — czerwonopomarańczowa.
</details>

3. Ile czasu leci światło ze Słońca do Ziemi?

<details>
<summary>Odpowiedź</summary>

$1{,}496\cdot10^{11}/3\cdot10^8 \approx 499\ \mathrm{s} \approx 8{,}3\ \mathrm{min}$.
</details>

4. Galaktyka oddala się od nas z prędkością 14 000 km/s. Oblicz jej odległość ($H_0 = 70\ \mathrm{km/(s\cdot Mpc)}$).

<details>
<summary>Odpowiedź</summary>

$200\ \mathrm{Mpc}$.
</details>

5. Dwie gwiazdy mają tę samą jasność, ale temperatury 3000 K i 6000 K. Ile razy różnią się ich promienie?

<details>
<summary>Odpowiedź</summary>

$R \propto T^{-2}$ przy stałym $L$: chłodniejsza ma promień 4 razy większy.
</details>

### B. Poziom akademicki _(opcjonalnie — rozszerzenie z rachunkiem)_

1. Oblicz czas Hubble'a $1/H_0$ w latach dla $H_0 = 70\ \mathrm{km/(s\cdot Mpc)}$.

<details>
<summary>Odpowiedź</summary>

$1\ \mathrm{Mpc} = 3{,}086\cdot10^{19}\ \mathrm{km}$; $1/H_0 = 4{,}41\cdot10^{17}\ \mathrm{s} \approx 14$ mld lat.
</details>

2. Satelita Gaia mierzy paralaksy z niepewnością ok. $20\ \mu$as (mikrosekund łuku). Dla gwiazdy w odległości 1 kpc oszacuj niepewność względną odległości.

<details>
<summary>Odpowiedź</summary>

$p = 1\ \mathrm{mas} = 1000\ \mu$as; $u(d)/d = u(p)/p = 2\%$.
</details>

3. Oszacuj temperaturę równowagową Ziemi (bez efektu cieplarnianego), przyjmując, że pochłania 70% padającego promieniowania słonecznego (1360 W/m²) i wypromieniowuje jak ciało doskonale czarne całą powierzchnią.

<details>
<summary>Odpowiedź</summary>

$0{,}7\cdot1360\cdot\pi R^2 = 4\pi R^2\sigma T^4 \Rightarrow T = \left(\dfrac{0{,}7\cdot1360}{4\sigma}\right)^{1/4} \approx 255\ \mathrm{K}$ ($-18\ ^\circ$C); średnia rzeczywista ok. 288 K — różnica to efekt cieplarniany.
</details>

## Źródła

- CKE, [Informator o egzaminie maturalnym z fizyki](https://cke.gov.pl/images/_EGZAMIN_MATURALNY_OD_2023/Informatory/2024/Informator_EM2024_fizyka.pdf) — zakres wymagań z elementów astronomii.
- OpenStax, *Fizyka dla szkół wyższych*, t. 3 — §6.1 (promieniowanie ciała doskonale czarnego) i §11.6 (prawo Hubble'a, Wielki Wybuch).
- [OpenStax, *Astronomy 2e*](https://openstax.org/details/books/astronomy-2e) _(po angielsku)_ — pełny podręcznik astronomii: odległości, gwiazdy, diagram H-R, galaktyki.
- [Stellarium](https://stellarium.org/) — planetarium na komputer.
