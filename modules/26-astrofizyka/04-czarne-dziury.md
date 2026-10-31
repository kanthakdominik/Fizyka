# 26.04 — Czarne dziury i fale grawitacyjne

> **Moduł:** [26 — Astrofizyka](README.md) · **Poziom:** 🔵 studia · **Status:** ✅ pełny
>
> **Czytaj:**
>
> - OpenStax, *Fizyka dla szkół wyższych*, t. 1, rozdz. 13: [§13.7](https://openstax.org/books/fizyka-dla-szk%C3%B3%C5%82-wy%C5%BCszych-tom-1/pages/13-7-teoria-grawitacji-einsteina) · [wstęp do rozdziału](https://openstax.org/books/fizyka-dla-szk%C3%B3%C5%82-wy%C5%BCszych-tom-1/pages/13-wstep)
> - Halliday, Resnick, Walker, *Podstawy fizyki*, wyd. 2015, t. 2: §13.8 (s. 62)
> - Halliday, Resnick, Walker, *Podstawy fizyki*, wyd. 1 (2003), t. 2: [§14.9, s. 48](https://home.agh.edu.pl/~czapli/Resnick_2.pdf#page=64) — PDF z serwera AGH

← [Ewolucja gwiazd: białe karły, gwiazdy neutronowe, supernowe](03-ewolucja-gwiazd.md) · [spis modułu](README.md) · [Egzoplanety: metody wykrywania i warunki do życia](05-egzoplanety.md) →

## Po co to jest

Czarna dziura to obszar, z którego nic, nawet światło, nie może uciec. Jeszcze kilkadziesiąt lat temu była to ciekawostka teoretyczna, a dziś mamy zdjęcia cienia czarnych dziur w galaktyce M87 i w centrum Drogi Mlecznej oraz setki zarejestrowanych fal grawitacyjnych ze zderzeń czarnych dziur i gwiazd neutronowych. Te same efekty ogólnej teorii względności, które dominują przy czarnych dziurach, są mierzalne na Ziemi: bez poprawki na zegary w polu grawitacyjnym nawigacja GPS myliłaby się o ponad 10 km na dobę. Temat łączy prawo grawitacji (07), prędkość ucieczki (07.03) i szczególną teorię względności (19).

## Teoria w pigułce

**Promień Schwarzschilda.** Prędkość ucieczki z powierzchni ciała o masie $M$ i promieniu $R$ to $\sqrt{2GM/R}$ (07.03). Przyrównanie jej do $c$ daje promień

$$R_S = \frac{2GM}{c^2}.$$

Ten rachunek z fizyki klasycznej (Michell, 1783) przypadkiem daje wynik zgodny z ogólną teorią względności (Schwarzschild, 1916). Sfera o promieniu $R_S$ to **horyzont zdarzeń**: nic, co przekroczy go do wewnątrz, nie może wrócić.
- Słońce: $R_S = 2{,}95\ \mathrm{km}$; Ziemia: 9 mm.
- Sgr A* w centrum Drogi Mlecznej ($4{,}3\cdot10^6M_\odot$): $1{,}27\cdot10^{10}\ \mathrm m \approx 0{,}085\ \mathrm{AU}$.
- M87* ($6{,}5\cdot10^9M_\odot$): ok. 130 AU, więcej niż rozmiar Układu Słonecznego do Plutona.

**Ogólna teoria względności (Einstein, 1915)** opisuje grawitację jako zakrzywienie czasoprzestrzeni przez masę i energię. Podstawą jest **zasada równoważności**: lokalnie nie da się odróżnić pola grawitacyjnego od przyspieszenia układu (03.06). Przewidywania sprawdzone doświadczalnie:
- **ugięcie światła** przy Słońcu o 1,75″ (Eddington, 1919) — soczewkowanie grawitacyjne;
- **grawitacyjne spowolnienie czasu:** zegar niżej w polu grawitacyjnym chodzi wolniej. Dla słabego pola $\Delta f/f \approx \Delta\Phi/c^2$, na wysokości $h$ przy Ziemi $gh/c^2$. Pound i Rebka (1959) zmierzyli przesunięcie $2{,}5\cdot10^{-15}$ na wysokości 22,5 m;
- **precesja peryhelium Merkurego** o 43″ na stulecie;
- **fale grawitacyjne**.

**Czas przy horyzoncie.** Zegar spoczywający na odległości $r$ od czarnej dziury chodzi wolniej o czynnik $\sqrt{1 - R_S/r}$ względem odległego obserwatora. Przy samym horyzoncie dąży on do zera: dla dalekiego obserwatora spadające ciało „zamiera” przy horyzoncie i coraz bardziej się zaczerwienia, choć samo przekracza horyzont w skończonym czasie własnym.

**Siły pływowe** (07.05) przy horyzoncie małej czarnej dziury są zabójcze („spaghettyfikacja”): dla $10M_\odot$ różnica przyspieszeń na długości 2 m wynosi ok. $2\cdot10^8\ \mathrm{m/s^2}$. Przy horyzoncie supermasywnej Sgr A* tylko ok. $10^{-3}\ \mathrm{m/s^2}$, bo $\Delta a \propto M/R_S^3 \propto 1/M^2$.

**Jak obserwujemy czarne dziury:**
- ruch gwiazd wokół niewidocznego obiektu: orbity gwiazd wokół Sgr A* (zadanie z matury 2023, Nagroda Nobla 2020);
- promieniowanie X gorącego dysku akrecyjnego;
- **cień czarnej dziury** (Event Horizon Telescope, 2019 i 2022) — ciemny obszar o średnicy ok. $2\sqrt{27}GM/c^2 \approx 5{,}2R_S$, otoczony pierścieniem światła;
- **fale grawitacyjne**.

**Fale grawitacyjne** to zaburzenia czasoprzestrzeni rozchodzące się z prędkością światła, emitowane przez masy poruszające się z przyspieszeniem (np. ciasne układy podwójne). Fala o amplitudzie (odkształceniu) $h$ zmienia długość $L$ o $\Delta L \approx hL$. Pierwszy sygnał GW150914 (LIGO, 14 września 2015, Nagroda Nobla 2017): zlanie czarnych dziur 36 i $29M_\odot$ w odległości ok. 400 Mpc. W ciągu ok. 0,2 s częstotliwość rosła od 35 do ok. 250 Hz („świergot”, *chirp*), a w fale zamieniła się energia ok. $3M_\odot c^2 \approx 5\cdot10^{47}\ \mathrm J$. Na Ziemi $h \approx 10^{-21}$, czyli ramię interferometru (18.04) o długości 4 km zmieniło się o $4\cdot10^{-18}\ \mathrm m$ — tysiąc razy mniej niż średnica protonu. W 2017 r. zarejestrowano zderzenie gwiazd neutronowych GW170817 razem z błyskiem gamma i kilonową — źródłem złota i innych ciężkich pierwiastków (26.03). Polscy naukowcy współtworzą detektor Virgo (grupa POLGRAW).

**Promieniowanie Hawkinga.** Efekty kwantowe sprawiają, że czarna dziura promieniuje jak ciało o temperaturze $T = \hbar c^3/(8\pi GMk)$. Dla masy Słońca to $6\cdot10^{-8}\ \mathrm K$ — niemierzalnie mało.

## Wzory i założenia

| Wzór | Znaczenie | Kiedy obowiązuje |
|---|---|---|
| $R_S = 2GM/c^2$ | promień Schwarzschilda | czarna dziura bez obrotu i ładunku |
| $\dfrac{\Delta t_r}{\Delta t_\infty} = \sqrt{1 - R_S/r}$ | grawitacyjne spowolnienie czasu | zegar spoczywający na $r > R_S$ |
| $\dfrac{\Delta f}{f} \approx \dfrac{gh}{c^2}$ | przesunięcie grawitacyjne | słabe pole, mała wysokość |
| $\alpha = \dfrac{4GM}{c^2b}$ | kąt ugięcia światła | parametr zderzenia $b \gg R_S$ |
| $\Delta L \approx hL$ | zmiana długości ramienia detektora | fala grawitacyjna o amplitudzie $h$ |
| $\mathcal M = \dfrac{(m_1m_2)^{3/5}}{(m_1 + m_2)^{1/5}}$ | masa „świergotowa” (*chirp mass*) | układ podwójny przed zlaniem |

## Przykład rozwiązany

**Zadanie 1.** Oblicz promień Schwarzschilda Słońca, Ziemi i Sgr A* ($4{,}3\cdot10^6M_\odot$).

$R_S = 2GM/c^2$: Słońce $\dfrac{2\cdot6{,}67\cdot10^{-11}\cdot1{,}99\cdot10^{30}}{(3\cdot10^8)^2} \approx 2{,}95\ \mathrm{km}$; Ziemia 8,9 mm; Sgr A* $1{,}27\cdot10^{10}\ \mathrm m$ — ok. 18 promieni Słońca, mniej niż orbita Merkurego.

**Zadanie 2.** Satelity GPS krążą na wysokości 20 200 km z prędkością 3,87 km/s. O ile ich zegary spieszą się lub spóźniają na dobę względem zegarów na Ziemi?

- Szczególna teoria względności (ruch): $-\dfrac{v^2}{2c^2}\cdot86\,400\ \mathrm s \approx -7{,}2\ \mu\mathrm s$ (19.02).
- Ogólna (wyżej w polu): $+\dfrac{GM}{c^2}\left(\dfrac1{R_Z} - \dfrac1r\right)\cdot86\,400\ \mathrm s \approx +45{,}7\ \mu\mathrm s$.

Razem $+38{,}5\ \mu\mathrm s$ na dobę. Przemnożone przez $c$ daje błąd położenia ok. 11,5 km na dobę. Zegary satelitów są dlatego fabrycznie przestrojone.

### Wersja z rachunkiem różniczkowym i całkowym

**Przesunięcie grawitacyjne z zasady zachowania energii.** Foton o energii $hf$ ma „masę” $hf/c^2$. Wznosząc się z $r_1$ do $r_2$ w polu masy $M$, traci energię równą pracy przeciwko grawitacji:

$$h\,df = -\frac{hf}{c^2}\frac{GM}{r^2}dr \Rightarrow \ln\frac{f_2}{f_1} = -\frac{GM}{c^2}\int_{r_1}^{r_2}\frac{dr}{r^2} = -\frac{GM}{c^2}\left(\frac1{r_1} - \frac1{r_2}\right).$$

Dla małych zmian $\Delta f/f \approx -gh/c^2$ (przy Ziemi). Dla wieży w doświadczeniu Pounda–Rebki ($h = 22{,}5\ \mathrm m$): $2{,}5\cdot10^{-15}$. Ten sam wynik daje wzór na spowolnienie czasu, bo częstotliwość to „tykanie” zegara.

**Kąt cienia M87*.** Średnica cienia $2\sqrt{27}GM/c^2 \approx 9{,}9\cdot10^{13}\ \mathrm m$ z odległości 16,8 Mpc ($5{,}2\cdot10^{23}\ \mathrm m$) to kąt $1{,}9\cdot10^{-10}\ \mathrm{rad} \approx 40\ \mu$as (mikrosekund łuku). EHT zmierzył 42 μas. Taka zdolność rozdzielcza (18.05) wymaga teleskopu wielkości Ziemi: $\lambda/D = 1{,}3\ \mathrm{mm}/10\,000\ \mathrm{km} \approx 27\ \mu$as.

## Typowe pułapki

- **Czarna dziura „wsysa” wszystko jak odkurzacz.** Daleko od niej grawitacja jest taka sama jak gwiazdy o tej samej masie. Gdyby Słońce stało się czarną dziurą o tej samej masie, Ziemia krążyłaby dalej po tej samej orbicie.
- **Promień Schwarzschilda to rozmiar „powierzchni” z materii.** To granica, a nie powierzchnia. Materia, która ją przekroczyła, nie zatrzymuje się na niej.
- **Fale grawitacyjne to fale w polu grawitacyjnym jak fale dźwiękowe w powietrzu.** To drgania samej geometrii czasoprzestrzeni, rozchodzące się z prędkością światła także w próżni.
- **Ogólna teoria względności dotyczy tylko ekstremalnych obiektów.** Poprawki są małe, ale mierzalne na Ziemi (GPS, zegary atomowe na różnych wysokościach).

## Doświadczenie / symulacja

**Model zakrzywionej przestrzeni.** Rozciągnij elastyczną tkaninę (lycra) na obręczy i połóż w środku ciężką kulę. Toczące się po tkaninie kulki krążą wokół niej po orbitach i spadają do środka. To tylko analogia (zakrzywiona jest przestrzeń dwuwymiarowa, a „grawitację” daje tu ziemska grawitacja), ale dobrze pokazuje soczewkowanie i orbity.

**Symulacja PhET:** *Grawitacja i orbity* — porównaj orbity wokół Słońca i wokół obiektu o tej samej masie, ale mniejszym promieniu: orbity są takie same, dopóki nie zbliżysz się do powierzchni ([phet.colorado.edu/pl](https://phet.colorado.edu/pl/)).

**Python:** promienie Schwarzschilda, poprawki zegarów GPS, kąt cienia czarnych dziur i uproszczony „świergot” fali grawitacyjnej GW150914.

```python
import numpy as np
import matplotlib.pyplot as plt

G, c, Msun, AU, pc = 6.674e-11, 2.998e8, 1.989e30, 1.496e11, 3.0857e16
Mz, Rz = 5.972e24, 6.371e6
for nazwa, M in [("Ziemia", Mz), ("Słońce", Msun), ("Sgr A*", 4.3e6*Msun), ("M87*", 6.5e9*Msun)]:
    print(f"{nazwa:7s}: R_S = {2*G*M/c**2:.3e} m = {2*G*M/c**2/AU:.2e} AU")

r = Rz + 20200e3
v = np.sqrt(G*Mz/r)
sr, ogt = -v**2/(2*c**2)*86400e6, G*Mz/c**2*(1/Rz - 1/r)*86400e6
print(f"GPS: STW {sr:.1f} μs/dobę, OTW {ogt:+.1f} μs/dobę, razem {sr + ogt:+.1f} μs/dobę → {(sr + ogt)*1e-6*c/1e3:.1f} km/dobę")
for nazwa, M, d in [("M87*", 6.5e9*Msun, 16.8e6*pc), ("Sgr A*", 4.3e6*Msun, 8.18e3*pc)]:
    print(f"cień {nazwa}: {2*np.sqrt(27)*G*M/c**2/d*206265e6:.0f} μas")

m1, m2 = 36, 29
Mc = (m1*m2)**0.6/(m1 + m2)**0.2
tau0 = G*Mc*Msun/c**3
t = np.linspace(-0.25, -0.003, 4000)                       # czas do zlania [s]
f = (1/np.pi)*(5/(256*(-t)))**(3/8)*tau0**(-5/8)          # częstotliwość fali (przybliżenie newtonowskie)
faza = 2*np.pi*np.cumsum(f)*(t[1] - t[0])
h = (f/f[-1])**(2/3)*np.cos(faza)                          # amplituda rośnie jak f^(2/3)
print(f"masa świergotowa {Mc:.1f} M☉; f(−0,2 s) = {f[np.searchsorted(t, -0.2)]:.0f} Hz, f(−0,01 s) = {f[np.searchsorted(t, -0.01)]:.0f} Hz")
print(f"energia fal: 3 M☉c² = {3*Msun*c**2:.1e} J; ΔL ramienia 4 km przy h = 1e-21: {1e-21*4e3:.0e} m")
plt.plot(t, h); plt.xlabel("czas do zlania [s]"); plt.ylabel("h (jedn. umowne)"); plt.title("model świergotu GW150914"); plt.show()
```

## Zadania

### A. Poziom maturalny _(opcjonalnie — rozgrzewka)_

1. Do jakiego promienia trzeba by ścisnąć Ziemię, żeby stała się czarną dziurą? Jaką miałaby wtedy gęstość?

<details>
<summary>Odpowiedź</summary>

$R_S = 2GM/c^2 \approx 8{,}9\ \mathrm{mm}$. Gęstość $M/(\tfrac43\pi R_S^3) \approx 2\cdot10^{30}\ \mathrm{kg/m^3}$.
</details>

2. Gwiazda S2 krąży wokół Sgr A* z okresem 16 lat po orbicie o półosi wielkiej ok. 1000 AU. Oblicz masę Sgr A* z III prawa Keplera.

<details>
<summary>Odpowiedź</summary>

W jednostkach AU, lata, $M_\odot$: $M = a^3/T^2 = 1000^3/16^2 \approx 3{,}9\cdot10^6M_\odot$ (dokładne pomiary: $4{,}3\cdot10^6M_\odot$).
</details>

### B. Poziom akademicki

1. Oblicz przesunięcie częstotliwości światła wysłanego z powierzchni białego karła ($M = M_\odot$, $R = 6000\ \mathrm{km}$) i odebranego daleko. Jaką prędkość radialną dałby taki sam efekt Dopplera?

<details>
<summary>Odpowiedź</summary>

$\Delta f/f \approx GM/(Rc^2) = 1{,}48\cdot10^3/6\cdot10^6 \approx 2{,}5\cdot10^{-4}$. Odpowiada to prędkości $v = c\Delta f/f \approx 74\ \mathrm{km/s}$. Tak zmierzono przesunięcie grawitacyjne w widmie Syriusza B.
</details>

2. Wyprowadź, że przyspieszenie pływowe na długości $l$ przy horyzoncie czarnej dziury maleje jak $1/M^2$.

<details>
<summary>Odpowiedź</summary>

$\Delta a = \dfrac{2GMl}{r^3}$; dla $r = R_S = 2GM/c^2$: $\Delta a = \dfrac{2GMl\,c^6}{8G^3M^3} = \dfrac{lc^6}{4G^2M^2}$.
</details>

3. Uruchom kod i sprawdź, jak zmienia się częstotliwość fali grawitacyjnej w ostatnich 0,2 s przed zlaniem. Pokaż, że z $f(t) \propto (t_c - t)^{-3/8}$ wynika $\dfrac{df}{dt} \propto f^{11/3}$.

<details>
<summary>Odpowiedź</summary>

Z kodu: od ok. 34 Hz do ponad 100 Hz (model newtonowski zawodzi tuż przed zlaniem, gdzie rzeczywista częstotliwość dochodzi do ok. 250 Hz). $f = A(t_c - t)^{-3/8} \Rightarrow \dfrac{df}{dt} = \dfrac38A(t_c - t)^{-11/8} = \dfrac38A^{-8/3}f^{11/3}$.
</details>

4. Oblicz temperaturę Hawkinga czarnej dziury o masie Księżyca ($7{,}3\cdot10^{22}\ \mathrm{kg}$). Czy taka czarna dziura parowałaby we współczesnym Wszechświecie?

<details>
<summary>Odpowiedź</summary>

$T = \hbar c^3/(8\pi GMk) \approx 1{,}7\ \mathrm K$ — mniej niż temperatura promieniowania tła (2,7 K). Pochłaniałaby więcej, niż emituje, więc by nie parowała.
</details>

## Źródła

- OpenStax, *Fizyka dla szkół wyższych*, t. 1, rozdz. 13 — §13.7: teoria grawitacji Einsteina.
- Halliday, Resnick, Walker, *Podstawy fizyki* — wyd. 2015: t. 2, §13.8; wyd. 1: t. 2, §14.9 (grawitacja według Einsteina).
- Moduły 07.03 (prędkość ucieczki), 07.04 (prawa Keplera), 07.05 (siły pływowe), 19.02 (dylatacja czasu).
- OpenStax, *Astronomy 2e*, rozdz. 24 (czarne dziury i zakrzywiona czasoprzestrzeń) — [openstax.org/details/books/astronomy-2e](https://openstax.org/details/books/astronomy-2e), materiał dodatkowy, po angielsku.
- Symulacja PhET *Grawitacja i orbity*.
