# 11.03 — Przewodnictwo, konwekcja i promieniowanie cieplne

> **Moduł:** [11 — Termodynamika i teoria kinetyczna](README.md) · **Poziom:** 🟢🔵 matura R + studia · **Status:** ✅ pełny
>
> **Czytaj:**
>
> - OpenStax, *Fizyka dla szkół wyższych*, t. 2, rozdz. 1: [§1.6](https://openstax.org/books/fizyka-dla-szk%C3%B3%C5%82-wy%C5%BCszych-tom-2/pages/1-6-mechanizmy-przekazywania-ciepla) · [wstęp do rozdziału](https://openstax.org/books/fizyka-dla-szk%C3%B3%C5%82-wy%C5%BCszych-tom-2/pages/1-wstep)
> - Halliday, Resnick, Walker, *Podstawy fizyki*, wyd. 2015, t. 2: §18.6 (s. 269)
> - Halliday, Resnick, Walker, *Podstawy fizyki*, wyd. 1 (2003), t. 2: [§19.11, s. 209](https://home.agh.edu.pl/~czapli/Resnick_2.pdf#page=225) — PDF z serwera AGH

← [Ciepło, ciepło właściwe, przemiany fazowe, kalorymetria](02-cieplo-i-przemiany-fazowe.md) · [spis modułu](README.md) · [Gaz doskonały i kinetyczna teoria gazów](04-gaz-doskonaly-i-teoria-kinetyczna.md) →

## Po co to jest

Ciepło płynie na trzy sposoby: przez przewodzenie, konwekcję i promieniowanie. Od tego zależy, ile kosztuje ogrzanie domu (współczynnik $U$ ścian i okien), jak chłodzi się procesor, dlaczego termos trzyma temperaturę i jak gruby lód urośnie na jeziorze. Promieniowanie cieplne wyznacza temperaturę Ziemi i gwiazd. Rozkład widmowy tego promieniowania doprowadził Plancka do narodzin fizyki kwantowej (20).

## Teoria w pigułce

**Przewodzenie** to przekazywanie energii przez zderzenia cząsteczek i ruch elektronów, bez ruchu materii. **Prawo Fouriera** dla płyty o grubości $L$ i polu $A$:

$$P = \frac{Q}{t} = kA\frac{\Delta T}{L}, \qquad \text{ogólnie} \quad \frac{P}{A} = -k\frac{dT}{dx}.$$

Przykładowe przewodności cieplne $k$ (w W/(m·K)):

| Materiał | $k$ |
|---|---|
| miedź | 400 |
| stal | 50 |
| szkło | ok. 1 |
| cegła | ok. 0,8 |
| woda | 0,6 |
| drewno | 0,1–0,2 |
| styropian | 0,04 |
| powietrze (nieruchome) | 0,026 |

**Opór cieplny** $R = L/(kA)$ działa jak opór elektryczny (13): $P = \Delta T/R$, a przy warstwach połączonych szeregowo opory się dodają. W budownictwie używa się **współczynnika przenikania** $U$ (W/(m²·K)): $P = UA\,\Delta T$. Nowe ściany mają $U \lesssim 0{,}2$, a okna ok. 1.

**Konwekcja** to przenoszenie ciepła przez ruch płynu: ciepłe powietrze unosi się, bo ma mniejszą gęstość (08.02). Konwekcja może być naturalna albo wymuszona (wentylator, wiatr). Wymianę ciepła z powierzchnią opisuje w przybliżeniu **prawo stygnięcia Newtona**:

$$P = hA(T - T_{\text{ot}}).$$

Ciało o pojemności cieplnej $C$ stygnie wykładniczo: $T - T_{\text{ot}} = (T_0 - T_{\text{ot}})e^{-t/\tau}$, gdzie $\tau = C/(hA)$.

**Promieniowanie cieplne.** Każde ciało emituje fale elektromagnetyczne. Dla ciała w temperaturze $T$ moc wynosi (**prawo Stefana–Boltzmanna**):

$$P = \varepsilon\sigma AT^4, \qquad \sigma = 5{,}67\cdot10^{-8}\ \mathrm{\frac{W}{m^2K^4}}.$$

$\varepsilon$ to emisyjność: 1 dla ciała doskonale czarnego, ok. 0,97 dla skóry, ok. 0,03 dla polerowanego srebra. Ciało pochłania też promieniowanie otoczenia, więc moc wypadkowa wynosi $\varepsilon\sigma A(T^4 - T_{\text{ot}}^4)$. Długość fali maksimum emisji spełnia **prawo Wiena**: $\lambda_{\max}T = 2{,}898\cdot10^{-3}\ \mathrm{m\cdot K}$. Słońce świeci najmocniej w zakresie widzialnym, a człowiek w podczerwieni (ok. 10 μm), co wykorzystują kamery termowizyjne.

## Wzory i założenia

| Wzór | Znaczenie | Kiedy obowiązuje |
|---|---|---|
| $P = kA\Delta T/L$ | przewodzenie przez płytę | stan ustalony |
| $R = L/(kA)$, $\ R_{\text{szer}} = \sum R_i$ | opór cieplny | warstwy szeregowo |
| $P = UA\Delta T$, $\ U = 1/\sum(L_i/k_i)$ | przenikanie przez przegrodę | j.w., na 1 m² |
| $P = hA(T - T_{\text{ot}})$ | prawo stygnięcia Newtona | niewielkie $\Delta T$, konwekcja |
| $P = \varepsilon\sigma AT^4$ | prawo Stefana–Boltzmanna | — |
| $\lambda_{\max}T = 2{,}898\cdot10^{-3}\ \mathrm{m\cdot K}$ | prawo Wiena | ciało doskonale czarne |

## Przykład rozwiązany

**Zadanie 1.** Ściana domu o polu 100 m² ma współczynnik $U = 0{,}35\ \mathrm{W/(m^2K)}$. Jaka moc ucieka przez nią przy temperaturze 20°C wewnątrz i 0°C na zewnątrz? Porównaj z pojedynczą szybą o polu 2 m² i grubości 4 mm, licząc tylko przewodzenie przez szkło.

Ściana: $P = 0{,}35\cdot100\cdot20 = 700\ \mathrm W$.

Szyba: gdyby powierzchnie szkła miały temperatury 20°C i 0°C, popłynęłoby $1\cdot2\cdot20/0{,}004 = 10\ \mathrm{kW}$. W rzeczywistości największy opór dają cienkie warstwy powietrza przy obu powierzchniach szyby. Pojedyncza szyba ma $U \approx 5{,}8\ \mathrm{W/(m^2K)}$, więc realna strata wynosi ok. $5{,}8\cdot2\cdot20 \approx 230\ \mathrm W$, a na samym szkle spada tylko ok. 0,5 K. Mimo to 2 m² szyby traci jedną trzecią tego, co 100 m² ściany. Okna zespolone mają więc kilka szyb z gazem między nimi.

**Zadanie 2.** Ile mocy człowiek traci przez promieniowanie? Przyjmij powierzchnię skóry 1,8 m², temperaturę 33°C, emisyjność 0,97 i pokój w 20°C.

$P = 0{,}97\cdot5{,}67\cdot10^{-8}\cdot1{,}8\cdot(306^4 - 293^4) \approx 140\ \mathrm W$. To więcej niż moc spoczynkowa człowieka (ok. 100 W). Ubranie znacznie to ogranicza.

### Wersja z rachunkiem różniczkowym i całkowym

**Zadanie.** Powietrze nad jeziorem ma −10°C, a woda pod lodem 0°C. Jak grubość lodu rośnie w czasie? Oblicz ją po dobie i po tygodniu ($k_{\text{lód}} = 2{,}2\ \mathrm{W/(m\cdot K)}$, $\rho = 917\ \mathrm{kg/m^3}$, $L_t = 334\ \mathrm{kJ/kg}$). Przyjmij, że górna powierzchnia lodu ma temperaturę powietrza.

Ciepło przewodzone przez lód o grubości $x$ odbiera wodzie ciepło krzepnięcia nowej warstwy $dx$:

$$kA\frac{\Delta T}{x}dt = \rho A L_t\,dx \quad\Rightarrow\quad x\,dx = \frac{k\Delta T}{\rho L_t}dt \quad\Rightarrow\quad x = \sqrt{\frac{2k\Delta T}{\rho L_t}t}.$$

Grubość rośnie jak $\sqrt t$. Po dobie wynosi ok. 11 cm, po tygodniu ok. 29 cm, czyli tylko $\sqrt7 \approx 2{,}6$ razy więcej. Śnieg na lodzie mocno spowalnia przyrost. Model zawyża wynik, bo pomija opór warstwy powietrza nad lodem.

## Typowe pułapki

- **Metal jest zimniejszy niż drewno.** W tym samym pokoju oba mają tę samą temperaturę. Metal szybciej odprowadza ciepło z dłoni, bo ma większe $k$.
- **Stefan–Boltzmann w stopniach Celsjusza.** $T^4$ wymaga kelwinów.
- **Zapominanie o pochłanianiu.** Moc wypadkowa promieniowania to $\varepsilon\sigma A(T^4 - T_{\text{ot}}^4)$.
- **Gruba warstwa = dobry izolator.** Liczy się $L/k$. 10 cm styropianu izoluje lepiej niż 1 m cegły.
- **Ciepło „unosi się do góry”.** Do góry unosi się ciepłe powietrze (konwekcja). Przewodzenie i promieniowanie nie mają kierunku wyróżnionego przez grawitację.

## Doświadczenie / symulacja

**Prawo stygnięcia Newtona.** Termometrem kuchennym (lub czujnikiem z Arduino) mierz co minutę temperaturę herbaty w kubku przez godzinę. Narysuj $\ln(T - T_{\text{ot}})$ od czasu i wyznacz $\tau$. Powtórz z przykrywką i porównaj. Przy dużych różnicach temperatur (powyżej ok. 30 K) wykres przestaje być prosty, bo parowanie i promieniowanie nie są liniowe.

**Termowizja.** Jeśli masz dostęp do kamery termowizyjnej (bywa w telefonach budowlanych lub jako przystawka), obejrzyj okna i narożniki domu zimą. Mostki cieplne będą wyraźnie widoczne.

**Symulacja PhET:** *Formy energii i jej przemiany* (*Energy Forms and Changes*) — przewodzenie między blokami i wymiana ciepła ([phet.colorado.edu/pl](https://phet.colorado.edu/pl/)).

**Python:** przyrost lodu ($\sqrt t$) i stygnięcie herbaty.

```python
import numpy as np
import matplotlib.pyplot as plt

k, rho, L, dT = 2.2, 917.0, 334e3, 10.0
t = np.linspace(0, 14*86400, 500)
x = np.sqrt(2*k*dT*t/(rho*L))
for d in (1, 7, 14):
    print(f"czas {d:2d} d: lód {np.sqrt(2*k*dT*d*86400/(rho*L))*100:.1f} cm")

# herbata: 90 → 60 °C w 10 min w pokoju 20 °C
T_ot, T0 = 20.0, 90.0
tau = 10/np.log((T0 - T_ot)/(60 - T_ot))
print(f"τ = {tau:.1f} min, 40 °C po {tau*np.log((T0 - T_ot)/(40 - T_ot)):.1f} min")

fig, ax = plt.subplots(1, 2, figsize=(10, 3.5))
ax[0].plot(t/86400, x*100); ax[0].set_xlabel("t [doby]"); ax[0].set_ylabel("grubość lodu [cm]"); ax[0].grid(True)
tm = np.linspace(0, 60, 200)
ax[1].plot(tm, T_ot + (T0 - T_ot)*np.exp(-tm/tau)); ax[1].set_xlabel("t [min]"); ax[1].set_ylabel("T [°C]"); ax[1].grid(True)
plt.tight_layout(); plt.show()
```

## Zadania

### A. Poziom maturalny

1. Pręt miedziany o długości 1 m i przekroju 1 cm² łączy zbiorniki o temperaturach 100°C i 0°C ($k = 400\ \mathrm{W/(m\cdot K)}$). Jaka moc płynie przez pręt?

<details>
<summary>Odpowiedź</summary>

$P = 400\cdot10^{-4}\cdot100/1 = 4\ \mathrm W$.
</details>

2. Jak termos ogranicza każdy z trzech sposobów przekazywania ciepła?

<details>
<summary>Odpowiedź</summary>

Próżnia między ściankami usuwa przewodzenie i konwekcję. Posrebrzane ścianki (mała emisyjność) ograniczają promieniowanie. Korek ogranicza konwekcję i parowanie.
</details>

3. Moc promieniowania Słońca wynosi $3{,}83\cdot10^{26}\ \mathrm W$, a promień $6{,}96\cdot10^8\ \mathrm m$. Oblicz temperaturę powierzchni Słońca i długość fali maksimum emisji.

<details>
<summary>Odpowiedź</summary>

$T = \left(\dfrac{P}{4\pi R^2\sigma}\right)^{1/4} \approx 5770\ \mathrm K$, $\lambda_{\max} \approx 502\ \mathrm{nm}$ (światło zielononiebieskie).
</details>

4. Ile razy wzrośnie moc promieniowania ciała, gdy jego temperatura bezwzględna wzrośnie dwukrotnie?

<details>
<summary>Odpowiedź</summary>

$2^4 = 16$ razy.
</details>

### B. Poziom akademicki

1. Ściana składa się z 25 cm cegły ($k = 0{,}8$) i 10 cm styropianu ($k = 0{,}04$). Oblicz $U$, strumień ciepła na 1 m² przy różnicy 20 K i spadek temperatury na cegle.

<details>
<summary>Odpowiedź</summary>

$R = 0{,}3125 + 2{,}5 = 2{,}81\ \mathrm{m^2K/W}$, $U \approx 0{,}36\ \mathrm{W/(m^2K)}$, $q \approx 7{,}1\ \mathrm{W/m^2}$. Na cegle spada tylko $7{,}1\cdot0{,}3125 \approx 2{,}2\ \mathrm K$, a resztę, ok. 17,8 K, przejmuje styropian.
</details>

2. Herbata stygnie od 90°C do 60°C w 10 minut w pokoju o temperaturze 20°C. Po jakim czasie od początku będzie miała 40°C? Przyjmij prawo Newtona.

<details>
<summary>Odpowiedź</summary>

$\tau = 10/\ln(70/40) \approx 17{,}9\ \mathrm{min}$. $t = \tau\ln(70/20) \approx 22\ \mathrm{min}$.
</details>

3. Oblicz temperaturę równowagową Ziemi bez efektu cieplarnianego. Ziemia pochłania $1361\cdot(1 - 0{,}3)\ \mathrm{W/m^2}$ na przekroju $\pi R^2$ i emituje jak ciało czarne z całej powierzchni $4\pi R^2$.

<details>
<summary>Odpowiedź</summary>

$\sigma T^4\cdot4\pi R^2 = 0{,}7\cdot1361\cdot\pi R^2 \Rightarrow T \approx 255\ \mathrm K = -18^\circ\mathrm C$. Rzeczywista średnia to ok. 15°C, a różnicę daje efekt cieplarniany.
</details>

4. Wyprowadź temperaturę $T(x)$ w płycie w stanie ustalonym z równania $\dfrac{d}{dx}\left(k\dfrac{dT}{dx}\right) = 0$. Co się zmieni, gdy $k$ zależy od $x$?

<details>
<summary>Odpowiedź</summary>

Dla stałego $k$ temperatura zmienia się liniowo. Ogólnie stały jest strumień $q = -k\,dT/dx$, więc $\Delta T = q\displaystyle\int\frac{dx}{k(x)}$, czyli opory warstw się sumują.
</details>

## Źródła

- OpenStax, *Fizyka dla szkół wyższych*, t. 2, rozdz. 1 — §1.6: mechanizmy przekazywania ciepła.
- Halliday, Resnick, Walker, *Podstawy fizyki* — wyd. 2015: t. 2, §18.6; wyd. 1: t. 2, §19.11.
- Symulacja PhET *Formy energii i jej przemiany*.
