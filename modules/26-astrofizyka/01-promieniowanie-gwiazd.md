# 26.01 — Promieniowanie gwiazd: moc, temperatura, widma i diagram H–R

> **Moduł:** [26 — Astrofizyka](README.md) · **Poziom:** 🟢🔵 matura R + studia · **Status:** ✅ pełny
>
> **Czytaj:**
>
> - OpenStax, *Fizyka dla szkół wyższych*, t. 3, rozdz. 6: [§6.1](https://openstax.org/books/fizyka-dla-szk%C3%B3%C5%82-wy%C5%BCszych-tom-3/pages/6-1-promieniowanie-ciala-doskonale-czarnego) · [wstęp do rozdziału](https://openstax.org/books/fizyka-dla-szk%C3%B3%C5%82-wy%C5%BCszych-tom-3/pages/6-wstep)

← (początek modułu) · [spis modułu](README.md) · [Budowa gwiazd: równowaga hydrostatyczna, źródła energii, czas życia](02-budowa-gwiazd.md) →

## Po co to jest

Gwiazd nie da się dotknąć ani zważyć. Prawie wszystko, co o nich wiemy, pochodzi ze światła: z jego natężenia, barwy i linii widmowych. Dwa prawa promieniowania ciała doskonale czarnego (20.01) — Wiena i Stefana–Boltzmanna — pozwalają z widma odczytać temperaturę gwiazdy, a z temperatury i mocy promieniowania jej promień. Diagram Hertzsprunga–Russella porządkuje gwiazdy tak, jak układ okresowy porządkuje pierwiastki, i jest punktem wyjścia do zrozumienia ich budowy i ewolucji (26.02–26.03). Prawo Stefana–Boltzmanna i prawo Wiena są na karcie wzorów maturalnych.

## Teoria w pigułce

**Gwiazda jako ciało doskonale czarne.** Fotosfera gwiazdy (warstwa, z której ucieka światło) promieniuje w przybliżeniu jak ciało doskonale czarne o temperaturze $T$.
- **Prawo Wiena:** maksimum widma przypada na $\lambda_{\max} = b/T$, $b = 2{,}898\cdot10^{-3}\ \mathrm{m\cdot K}$. Słońce (5772 K): 502 nm. Czerwony nadolbrzym Betelgeza (ok. 3600 K): 805 nm. Gorąca gwiazda typu B (25 000 K): 116 nm, w nadfiolecie.
- **Prawo Stefana–Boltzmanna:** każdy metr kwadratowy powierzchni wysyła moc $\sigma T^4$, więc **moc promieniowania** (jasność absolutna, *luminosity*) gwiazdy o promieniu $R$ to

$$L = 4\pi R^2\sigma T^4.$$

Dla Słońca $L_\odot = 3{,}83\cdot10^{26}\ \mathrm W$.

**Strumień obserwowany.** Na odległości $d$ moc rozkłada się na sferze o polu $4\pi d^2$:

$$F = \frac{L}{4\pi d^2}.$$

Przy Ziemi strumień od Słońca (stała słoneczna) wynosi ok. 1361 W/m². Astronomowie wyrażają jasność w **wielkościach gwiazdowych**: różnica 5 magnitudo to 100 razy w strumieniu, $m_1 - m_2 = -2{,}5\log_{10}(F_1/F_2)$.

**Odległości.** Najbliższe gwiazdy mierzy się **paralaksą**: gwiazda w odległości 1 parseka (pc) przesuwa się na niebie o 1″ w ciągu pół roku. $d\,[\mathrm{pc}] = 1/p\,[″]$, 1 pc ≈ 3,26 roku świetlnego (07.06). Proxima Centauri ma paralaksę 0,768″, czyli $d = 1{,}30\ \mathrm{pc} = 4{,}25$ roku świetlnego. Satelita Gaia zmierzył paralaksy ponad miliarda gwiazd.

**Widma i typy widmowe.** Na ciągłe widmo nakładają się linie absorpcyjne pierwiastków z chłodniejszych zewnętrznych warstw (21.01, 21.05). Ich obecność i siła zależą głównie od temperatury, nie od składu (większość gwiazd ma podobny skład: ok. 73% wodoru i 25% helu masowo). Typy widmowe od najgorętszych: **O B A F G K M** (Słońce to G2). Linie Balmera wodoru są najsilniejsze w gwiazdach typu A (ok. 10 000 K): w chłodniejszych mało atomów jest wzbudzonych do poziomu $n = 2$, w gorętszych wodór jest zjonizowany. Z przesunięcia linii (efekt Dopplera, 10.07) mierzy się prędkość radialną gwiazdy.

**Diagram Hertzsprunga–Russella** to wykres mocy promieniowania od temperatury (oś temperatury rośnie w lewo). Gwiazdy nie są rozrzucone przypadkowo:
- **ciąg główny** (ok. 90% gwiazd, w tym Słońce) — gwiazdy spalające wodór w jądrze; im większa masa, tym większa moc i temperatura;
- **olbrzymy i nadolbrzymy** (prawy górny róg) — chłodne, ale ogromne, o dużej mocy;
- **białe karły** (lewy dolny róg) — gorące, ale małe, o małej mocy.

Linie stałego promienia na diagramie wynikają z $L = 4\pi R^2\sigma T^4$.

## Wzory i założenia

| Wzór | Znaczenie | Kiedy obowiązuje |
|---|---|---|
| $\lambda_{\max}T = b$, $b = 2{,}898\cdot10^{-3}\ \mathrm{m\cdot K}$ | prawo Wiena | ciało doskonale czarne |
| $L = 4\pi R^2\sigma T^4$ | moc promieniowania gwiazdy | fotosfera jak ciało doskonale czarne |
| $F = L/(4\pi d^2)$ | strumień w odległości $d$ | promieniowanie izotropowe, bez pochłaniania |
| $\dfrac{R}{R_\odot} = \sqrt{\dfrac{L}{L_\odot}}\left(\dfrac{T_\odot}{T}\right)^2$ | promień z mocy i temperatury | — |
| $d\,[\mathrm{pc}] = 1/p\,[″]$ | paralaksa | małe kąty |
| $m_1 - m_2 = -2{,}5\log_{10}(F_1/F_2)$ | wielkości gwiazdowe | — |

## Przykład rozwiązany

**Zadanie 1.** Oblicz moc promieniowania Słońca ($R_\odot = 6{,}96\cdot10^8\ \mathrm m$, $T = 5772\ \mathrm K$) i strumień przy Ziemi (1 AU).

$L = 4\pi(6{,}96\cdot10^8)^2\cdot5{,}67\cdot10^{-8}\cdot5772^4 \approx 3{,}83\cdot10^{26}\ \mathrm W$. $F = L/(4\pi(1{,}496\cdot10^{11})^2) \approx 1361\ \mathrm{W/m^2}$.

**Zadanie 2.** Syriusz B ma temperaturę ok. 25 000 K i moc $0{,}025L_\odot$. Oblicz jego promień.

$\dfrac{R}{R_\odot} = \sqrt{0{,}025}\left(\dfrac{5772}{25\,000}\right)^2 \approx 0{,}0084$, czyli $R \approx 5900\ \mathrm{km}$ — mniej niż promień Ziemi (6400 km), choć masa jest równa masie Słońca. To biały karzeł (26.03).

**Zadanie 3.** Betelgeza ma temperaturę 3600 K i moc ok. $1{,}1\cdot10^5L_\odot$. Oblicz promień.

$R \approx \sqrt{1{,}1\cdot10^5}\cdot(5772/3600)^2R_\odot \approx 850R_\odot$, czyli ok. 4 AU. Umieszczona w miejscu Słońca sięgałaby poza orbitę Marsa.

### Wersja z rachunkiem różniczkowym i całkowym

**Jaka część promieniowania Słońca to światło widzialne?** Z rozkładu Plancka (20.01) moc w przedziale długości fal:

$$\frac{L_{400-700}}{L} = \frac{\displaystyle\int_{400\ \mathrm{nm}}^{700\ \mathrm{nm}}\frac{d\lambda}{\lambda^5(e^{hc/\lambda kT} - 1)}}{\displaystyle\int_0^\infty\frac{d\lambda}{\lambda^5(e^{hc/\lambda kT} - 1)}}.$$

Całkowanie numeryczne daje ok. 37% dla Słońca, 33% dla gwiazdy o temperaturze 10 000 K i tylko 16% dla Betelgezy. Większość mocy chłodnych gwiazd to podczerwień.

**Prawo Wiena z rozkładu Plancka.** Podstawiając $x = hc/(\lambda kT)$ i przyrównując pochodną do zera, dostajemy $5(1 - e^{-x}) = x$, czyli $x = 4{,}965$ (rozwiązanie numeryczne w 25.01) i $\lambda_{\max}T = hc/(4{,}965k)$.

## Typowe pułapki

- **Jasna gwiazda na niebie to gwiazda o dużej mocy.** Jasność obserwowana zależy też od odległości ($F \propto 1/d^2$). Syriusz jest najjaśniejszy na niebie, bo jest blisko (2,6 pc), a nie dlatego, że świeci najmocniej.
- **Gwiazda czerwona jest „słabsza” od niebieskiej.** Czerwone nadolbrzymy mają ogromną moc, bo są ogromne. O mocy decydują razem $R$ i $T$.
- **Większa wielkość gwiazdowa — jaśniejsza gwiazda.** Odwrotnie: skala jest „odwrócona”, gwiazda 1 mag jest jaśniejsza od gwiazdy 6 mag.
- **Linie widmowe wskazują skład.** Głównie temperaturę. Gwiazda bez linii wodoru nie musi być go pozbawiona — może być za gorąca albo za zimna.

## Doświadczenie / symulacja

**Barwy gwiazd.** W pogodną noc porównaj Betelgezę (lewy górny róg Oriona, pomarańczowa) z Rigelem (prawy dolny, niebiesko-biały) albo Antaresa z Wegą latem. W programie Stellarium (polski interfejs) sprawdź ich temperatury i typy widmowe. Zdjęcie aparatem lekko poza ostrością pokazuje barwy wyraźniej niż oko.

**Symulacja PhET:** *Widmo ciała doskonale czarnego* — porównaj krzywe dla temperatur Słońca, Syriusza i Betelgezy ([phet.colorado.edu/pl](https://phet.colorado.edu/pl/)).

**Python:** widma gwiazd z rozkładu Plancka, ułamek mocy w świetle widzialnym i diagram H–R dla modelowych gwiazd ciągu głównego, olbrzymów i białych karłów.

```python
import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import quad

h, c, k, sigma = 6.62607015e-34, 2.99792458e8, 1.380649e-23, 5.670374e-8
Lsun, Rsun, Tsun = 3.828e26, 6.957e8, 5772
planck = lambda lam, T: 2*h*c**2/lam**5/np.expm1(h*c/(lam*k*T))

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 4.5))
lam = np.linspace(80e-9, 3000e-9, 1000)
for nazwa, T in [("Betelgeza", 3600), ("Słońce", 5772), ("Syriusz A", 9940), ("Syriusz B", 25000)]:
    calk = quad(planck, 10e-9, 1e-3, args=(T,), limit=400, points=[2.9e-3/T])[0]
    wid = quad(planck, 400e-9, 700e-9, args=(T,))[0]
    print(f"{nazwa:10s}: T = {T:5d} K, λmax = {2.898e-3/T*1e9:5.0f} nm, w świetle widzialnym {wid/calk:.0%} mocy")
    ax1.plot(lam*1e9, planck(lam, T)/planck(2.898e-3/T, T), label=f"{nazwa} ({T} K)")
ax1.axvspan(400, 700, color="yellow", alpha=0.2); ax1.set_xlabel("λ [nm]"); ax1.set_ylabel("widmo (znormalizowane)"); ax1.legend()

print(f"L☉ z prawa Stefana–Boltzmanna: {4*np.pi*Rsun**2*sigma*Tsun**4:.3e} W")
rng = np.random.default_rng(0)
M = 10**rng.uniform(-0.7, 1.3, 300)                       # masy gwiazd ciągu głównego [M☉]
L_cg, R_cg = M**3.5, M**0.8                               # przybliżone zależności masa–moc i masa–promień
T_cg = Tsun*(L_cg/R_cg**2)**0.25
ax2.scatter(T_cg, L_cg, s=6, label="ciąg główny")
ax2.scatter(rng.uniform(3300, 5000, 40), 10**rng.uniform(2, 5, 40), s=10, c="r", label="olbrzymy")
ax2.scatter(rng.uniform(7000, 30000, 30), 10**rng.uniform(-4, -1.5, 30), s=10, c="gray", label="białe karły")
for R in (0.01, 1, 100):                                  # linie stałego promienia
    T = np.logspace(np.log10(2500), np.log10(40000), 50)
    ax2.plot(T, R**2*(T/Tsun)**4, "k:", lw=0.8)
ax2.set_xscale("log"); ax2.set_yscale("log"); ax2.invert_xaxis(); ax2.set_ylim(1e-5, 1e7)
ax2.set_xlabel("T [K]"); ax2.set_ylabel("L / L☉"); ax2.legend(); ax2.set_title("diagram H–R (model)")
plt.tight_layout(); plt.show()
```

## Zadania

### A. Poziom maturalny

1. Maksimum widma gwiazdy przypada na 290 nm. Oblicz jej temperaturę. Jaką barwę ma ta gwiazda?

<details>
<summary>Odpowiedź</summary>

$T = b/\lambda_{\max} = 2{,}898\cdot10^{-3}/2{,}9\cdot10^{-7} \approx 10\,000\ \mathrm K$. Biało-niebieską (np. Syriusz A, Wega).
</details>

2. Ile razy większą moc ma gwiazda o takim samym promieniu jak Słońce, ale dwa razy wyższej temperaturze?

<details>
<summary>Odpowiedź</summary>

$L \propto T^4$: $2^4 = 16$ razy.
</details>

3. Gwiazda A ma taką samą moc jak gwiazda B, ale jest 10 razy dalej. Ile razy mniejszy strumień od niej dociera?

<details>
<summary>Odpowiedź</summary>

$F \propto 1/d^2$: 100 razy mniejszy, czyli o 5 wielkości gwiazdowych słabsza.
</details>

4. Paralaksa Syriusza wynosi 0,379″. Oblicz jego odległość w parsekach i latach świetlnych.

<details>
<summary>Odpowiedź</summary>

$d = 1/0{,}379 \approx 2{,}64\ \mathrm{pc} \approx 8{,}6$ roku świetlnego.
</details>

### B. Poziom akademicki

1. Słońce traci masę na promieniowanie. Oblicz ubytek masy na sekundę i ułamek masy utracony w ciągu 10 mld lat ($M_\odot = 1{,}99\cdot10^{30}\ \mathrm{kg}$).

<details>
<summary>Odpowiedź</summary>

$\dot M = L/c^2 \approx 4{,}3\cdot10^9\ \mathrm{kg/s}$ (4 mln ton na sekundę). W 10 mld lat: $1{,}3\cdot10^{27}\ \mathrm{kg}$, ok. 0,07% masy Słońca.
</details>

2. Pokaż, że na diagramie $\log L$ od $\log T$ linie stałego promienia są prostymi o nachyleniu 4.

<details>
<summary>Odpowiedź</summary>

$\log L = \log(4\pi\sigma R^2) + 4\log T$. Przy stałym $R$ pierwszy wyraz jest stały, więc zależność jest liniowa z nachyleniem 4.
</details>

3. Oblicz, jaka część mocy Słońca przypada na promieniowanie o długości fali powyżej 700 nm (całkowanie numeryczne rozkładu Plancka).

<details>
<summary>Odpowiedź</summary>

Ok. 51% (podczerwień). W świetle widzialnym 37%, w nadfiolecie (poniżej 400 nm) ok. 12%. Wartości dla rzeczywistego Słońca różnią się nieco, bo jego widmo ma linie absorpcyjne i nie jest dokładnie widmem ciała doskonale czarnego.
</details>

4. Dwie gwiazdy mają wielkości gwiazdowe 1,0 i 6,0. Ile razy różnią się strumienie?

<details>
<summary>Odpowiedź</summary>

$F_1/F_2 = 10^{0{,}4\cdot5} = 100$.
</details>

## Źródła

- OpenStax, *Fizyka dla szkół wyższych*, t. 3, rozdz. 6 — §6.1: promieniowanie ciała doskonale czarnego.
- Moduły 20.01 (ciało doskonale czarne), 07.06 (odległości w astronomii), 21.01 (widma atomowe).
- OpenStax, *Astronomy 2e*, rozdz. 17–18 (analiza światła gwiazd, diagram H–R) — [openstax.org/details/books/astronomy-2e](https://openstax.org/details/books/astronomy-2e), materiał dodatkowy, po angielsku.
- Symulacja PhET *Widmo ciała doskonale czarnego*.
